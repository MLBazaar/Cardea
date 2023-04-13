"""Cardea Core module.

This module defines the Cardea Class, which is responsible for the
tying all components together, as well as the interact with them.
"""
import json
import logging
import os
import pickle
from functools import partial
from inspect import getfullargspec
from types import FunctionType
from typing import List, Union

import numpy as np
import pandas as pd
from mlblocks import MLPipeline
from featuretools import EntitySet

import cardea
from cardea.data_assembling import EntitySetLoader, load_mimic_data
from cardea.data_labeling import DataLabeler
from cardea.featurizing import Featurization
from cardea.modeling import Modeler

LOGGER = logging.getLogger(__name__)

DEFAULT_PIPELINE = 'XGB'
DEFAULT_METRICS = ["Accuracy", "F1 Macro", "Precision", "Recall"]


class Cardea:
    """Cardea Class.

    The Cardea Class provides the main functionalities
    to load data, create prediction tasks, and build
    pipelines.

    Args:
        data_path (str):
            Path or name of the dataset to load into an entityset.
        fhir (bool):
            Indicator of whether to use FHIR or MIMIC schema.
        pipeline (str, dict or MLPipeline):
            Pipeline to use. It can be passed as:
                * An ``str`` with a path to a JSON file.
                * An ``str`` with the name of a registered pipeline.
                * An ``MLPipeline`` instance.
                * A ``dict`` with an ``MLPipeline`` specification.
        hyperparameters (dict):
            Additional hyperparameters to set to the pipeline.
    """

    def _load_entityset(self, data_path, fhir):
        """Returns an entityset loaded with .csv files in data.

        Load the given dataset into an entityset. The dataset
        must be in FHIR or MIMIC structure format.

        Args:
            data (str):
                Path or name of the dataset to load into an entityset. Or
                a preloaded entityset
            fhir (bool):
                An indicator whether FHIR or MIMIC schema is used. This parameter is
                ignored when loading demo data. Default is ``True``.

        Returns:
            featuretools.EntitySet:
                An entityset with loaded data.
        """
        function = load_mimic_data
        if fhir:
            function = self._es_loader.load_data_entityset

        LOGGER.info("Loading data %s", data_path)

        return function(data_path)

    def _set_modeler(self):
        pipeline = self._pipeline
        if isinstance(pipeline, str) and os.path.isfile(pipeline):
            with open(pipeline) as json_file:
                pipeline = json.load(json_file)

        mlpipeline = MLPipeline(pipeline)
        if self._hyperparameters:
            mlpipeline.set_hyperparameters(self._hyperparameters)

        self._modeler = Modeler(mlpipeline, self._type)

    def __init__(self, data_path: str, fhir: bool = True,
                 pipeline: Union[str, dict, MLPipeline] = None, hyperparameters: dict = None):
        self._pipeline = pipeline or DEFAULT_PIPELINE
        self._hyperparameters = hyperparameters

        self._es_loader = EntitySetLoader()
        self._featurization = Featurization()
        self._modeler = None

        self._fhir = fhir
        self._target = None

        # load dataset
        self._entityset = self._load_entityset(data_path, fhir)

    def list_labelers(self) -> set:
        """Returns a list of the currently available data labelers.

        Returns:
            list:
                A list of the available data labelers.
        """

        labelers = set()
        for labeler_string in dir(cardea.data_labeling):
            labeler = getattr(cardea.data_labeling, labeler_string)
            if isinstance(labeler, FunctionType):
                labelers.add(labeler.__name__)

        return labelers

    def label(self, labeler: FunctionType,
              parameters: dict = None,
              subset: Union[list or float] = None,
              verbose: bool = False) -> pd.DataFrame:
        """Create label times using the data labeler.

        Use the labeling function to generate label times

        Args:
            labeler (function):
                Function that defines the prediction task, it should return a
                tuple of labeling function, the dataframe, and the name of the
                target entity.
            parameter (dict):
                Variables to change the default parameters, if any.
            subset (list or float):
                If float, fraction of data to label. If list, it should
                reference the instances for while to calculat the label
                for.
            verbose (bool):
                Indicate verbosity of the labeler.

        Returns:
            pandas.DataFrame:
                A dataframe of cutoff times and their target labels.
        """
        if parameters:
            labeler = partial(labeler, **parameters)

        LOGGER.info("Using labeler %s", str(labeler.__name__))
        data_labeler = DataLabeler(labeler)

        # target label calculation
        label_times, self._type, self._meta = data_labeler.generate_label_times(
            self._entityset, subset=subset, verbose=verbose)

        # set modeler if pipeline defined
        if self._pipeline:
            self._set_modeler()

        return label_times

    def featurize(self, label_times: pd.DataFrame,
                  seed_features: Union[bool, list] = None, max_depth: int = 1,
                  max_features: int = -1, n_jobs: int = 1,
                  verbose: bool = False) -> pd.DataFrame:
        """Returns a the calculated feature matrix.

        Args:
            label_times (pandas.DataFrame):
                A dataframe that indicates cutoff time for each instance.
            max_depth (int):
                Maximum allowed depth of features.
            max_features (int):
                Cap the number of generated features to this number. If -1, no limit.
            n_jobs (int):
                Number of parallel processes to use when calculating feature matrix.
            seed_features (bool or list):
                List of manually defined features to use. If boolean, then use previously
                created features as seed.
            verbose (bool):
                Indicate verbosity of the featurization.

        Returns:
            pandas.DataFrame:
                Generated feature matrix.
        """
        if isinstance(seed_features, bool):
            seed_features = self._fm_defs

        method = self._featurization.generate_feature_matrix
        target = self._meta.get('entity')
        arguments = set(getfullargspec(method)[0]) - set(getfullargspec(self.featurize)[0])
        kwargs = {k: self._meta.get(k) for k in arguments if self._meta.get(k) is not None}
        fm, self._fm_defs = method(
            self._entityset, target, label_times,
            seed_features=seed_features, max_depth=max_depth,
            max_features=max_features, n_jobs=n_jobs, verbose=verbose, **kwargs)

        return fm

    def set_pipeline(self, pipeline: Union[str, dict, MLPipeline],
                     hyperparameters: dict = None) -> None:
        """Select a pipeline.

        Args:
            pipeline (str, dict or MLPipeline):
                Pipeline to use. It can be passed as:
                    * An ``str`` with a path to a JSON file.
                    * An ``str`` with the name of a registered pipeline.
                    * An ``MLPipeline`` instance.
                    * A ``dict`` with an ``MLPipeline`` specification.
            hyperparameters (dict):
                Additional hyperparameters to set to the pipeline.
        """
        LOGGER.info("Setting %s pipeline", pipeline)

        self._pipeline = pipeline
        self._hyperparameters = hyperparameters
        self._set_modeler()

    def train_test_split(self, X: Union[np.ndarray, pd.DataFrame],
                         y: Union[np.ndarray, pd.Series, list], test_size: float = 0.2,
                         shuffle: bool = True) -> List[Union[pd.DataFrame, np.ndarray]]:
        """Split the training dataset and the testing dataset.

        Args:
            X (pandas.DataFrame or numpy.ndarray):
                Inputs to the pipeline.
            y (pandas.Series, numpy.ndarray or list):
                Target values.
            test_size (float):
                The proportion of the dataset to include in the test dataset.
            shuffle (bool):
                Whether or not to shuffle the data before splitting.

        Returns:
            list:
                List containing the train-test split of the inputs and targets.
        """
        return self._modeler.train_test_split(X, y, test_size, shuffle)

    def fit(self, X: Union[np.ndarray, pd.DataFrame], y: Union[np.ndarray, pd.Series, list],
            tune: bool = False, max_evals: int = 10, scoring: str = None,
            verbose: bool = False) -> None:
        """Train the cardea pipeline.

        Args:
            X (pandas.DataFrame or numpy.ndarray):
                Inputs to the pipeline.
            y (pandas.Series, numpy.ndarray or list):
                Target values.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function used in the hyper-parameter optimization.
            verbose (bool):
                Whether to log information during processing.
        """
        self._modeler.fit(X, y, tune, max_evals, scoring, verbose)

    def predict(self, X: Union[str, np.ndarray, pd.DataFrame]) -> Union[np.ndarray, list]:
        """Get predictions from the cardea pipeline.

        Args:
            X (str, pandas.DataFrame or ndarray):
                Inputs to the pipeline. If string, it points to the data path.

        Returns:
            numpy.ndarray or list:
                Predictions to the input data.
        """
        return self._modeler.predict(X)

    def fit_predict(self, X: Union[np.ndarray, pd.DataFrame],
                    y: Union[np.ndarray, pd.Series, list], tune: bool = False,
                    max_evals: int = 10, scoring: str = None,
                    verbose: bool = False) -> Union[np.ndarray, list]:
        """Train a cardea pipeline then make predictions.

        Args:
            X (pandas.DataFrame or numpy.ndarray):
                Inputs to the pipeline.
            y (pandas.Series, numpy.ndarray or list):
                Target values.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function used in the hyper-parameter optimization.
            verbose (bool):
                Whether to log information during processing.

        Returns:
            ndarray:
                Predictions to the input data.
        """
        return self._modeler.fit_predict(X, y, tune, max_evals, scoring, verbose)

    def evaluate(self, X: Union[np.ndarray, pd.DataFrame], y: Union[np.ndarray, pd.Series, list],
                 test_size: float = 0.2, shuffle: bool = True, fit: bool = False,
                 tune: bool = False, max_evals: int = 10, scoring: str = None,
                 metrics: List[str] = DEFAULT_METRICS, verbose: bool = False) -> pd.Series:
        """Evaluate the cardea pipeline.

        Args:
            X (pandas.DataFrame or numpy.ndarray):
                Inputs to the pipeline.
            y (pandas.Series, numpy.ndarray or list):
                Target values.
            test_size (float):
                The proportion of the dataset to include in the test dataset.
            shuffle (bool):
                Whether or not to shuffle the data before splitting.
            fit (bool):
                Whether to fit the pipeline before evaluating it.
                Defaults to ``False``.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function used in the hyper-parameter optimization.
            metrics (list):
                A list of scoring function names. The scoring functions should be consistent
                with the problem type.
            verbose (bool):
                Whether to log information during processing.

        Returns:
            Series:
                ``pandas.Series`` containing one element for each
                metric applied, with the metric name as index.
        """
        if fit:
            X_train, X_test, y_train, y_test = self.train_test_split(
                X, y, test_size=test_size, shuffle=shuffle)

            self._modeler.fit(
                X_train, y_train, tune=tune, max_evals=max_evals, scoring=scoring, verbose=verbose)

        else:
            X_test, y_test = X, y

        scores = {
            metric: self._modeler.test(X_test, y_test, scoring=metric)
            for metric in metrics
        }

        return pd.Series(scores)

    def save(self, path: str):
        """Save this object using pickle.

        Args:
            path (str):
                Path to the file where the serialization of
                this object will be stored.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as pickle_file:
            pickle.dump(self, pickle_file)

    @classmethod
    def load(cls, path: str):
        """Load a Cardea instance from a pickle file.

        Args:
            path (str):
                Path to the file where the instance has been
                previously serialized.

        Returns:
            Cardea:
                A Cardea instance

        Raises:
            ValueError:
                If the serialized object is not an Cardea instance.
        """
        with open(path, 'rb') as pickle_file:
            cardea = pickle.load(pickle_file)
            if not isinstance(cardea, cls):
                raise ValueError('Serialized object is not a Cardea instance')

            return cardea

    @property
    def entityset(self) -> EntitySet:
        """Get the entityset of the data Cardea is modeling.

        Returns:
            Featuretools.EntitySet:
                Entityset of the pipeline.
        """
        return self._entityset
