"""Cardea Core module.

This module defines the Cardea Class, which is responsible for the
tying all components together, as well as the interact with them.
"""
import json
import logging
import os
import pickle
from functools import partial
from inspect import ismethod
from types import FunctionType
from typing import List, Union

import numpy as np
import pandas as pd
from mlblocks import MLPipeline

import cardea
from cardea.data import DEMO_DATA, download
from cardea.data_assembling import EntitySetLoader, load_mimic_data
from cardea.data_labeling import DataLabeler, appointment_no_show
from cardea.featurizing import Featurization
from cardea.modeling import Modeler

LOGGER = logging.getLogger(__name__)

DEFAULT_DATA = 'kaggle'
DEFAULT_FHIR = True
DEFAULT_LABELER = appointment_no_show
DEFAULT_PIPELINE = 'XGB'
DEFAULT_METRICS = ["Accuracy", "F1 Macro", "Precision", "Recall"]

class Cardea:
    """Cardea Class.

    The Cardea Class provides the main functionalities
    to load data, create prediction tasks, and build
    pipelines.

    Args:
        data (str):
            Path or name of the dataset to load into an entityset.
        fhir (bool):
            Indicator of whether to use FHIR or MIMIC schema.
        labeler (method):
            Function to defined the data labeler for the wanted prediction problem.
        pipeline (str, dict or MLPipeline):
            Pipeline to use. It can be passed as:
                * An ``str`` with a path to a JSON file.
                * An ``str`` with the name of a registered pipeline.
                * An ``MLPipeline`` instance.
                * A ``dict`` with an ``MLPipeline`` specification.
        hyperparameters (dict):
            Additional hyperparameters to set to the pipeline.
    """

    def load_entityset(self, data_path: str, fhir: bool = False) -> None:
        """Returns an entityset loaded with .csv files in data.

        Load the given dataset into an entityset. The dataset
        must be in FHIR or MIMIC structure format.

        Args:
            data_path (str):
                A directory of all .csv files that should be loaded.
            fhir (bool):
                An indicator whether FHIR or MIMIC schema is used. This parameter is
                ignored when loading demo data.

        Returns:
            featuretools.EntitySet:
                An entityset with loaded data.
        """
        LOGGER.info("Loading data %s", data_path)

        if fhir:
            self.es = self._es_loader.load_data_entityset(data_path)

        else:
            self.es = load_mimic_data(data_path)

    def _set_modeler(self):
        pipeline = self._pipeline
        if isinstance(pipeline, str) and os.path.isfile(pipeline):
            with open(pipeline) as json_file:
                pipeline = json.load(json_file)

        mlpipeline = MLPipeline(pipeline)
        if self._hyperparameters:
            mlpipeline.set_hyperparameters(self._hyperparameters)

        self._modeler = Modeler(mlpipeline, self._type)

    def _set_entityset(self):
        data = self._data

        if data in DEMO_DATA:
            fhir = False if data == "mimic" else True
            data_path = download(data)

        self.load_entityset(data_path, fhir)

    def __init__(self, data: str = None, labeler: FunctionType = None,
                 pipeline: Union[str, dict, MLPipeline] = None, hyperparameters: dict = None):
        self._data = data or DEFAULT_DATA
        self._pipeline = pipeline or DEFAULT_PIPELINE
        self._hyperparameters = hyperparameters

        self._es_loader = EntitySetLoader()
        self._featurization = Featurization()
        self._modeler = None

        self._target = None
        self._set_entityset()

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

    def create_label_times(self, labeler: FunctionType = None,
                           parameter: dict = None) -> pd.DataFrame:
        """Create label times using the data labeler.

        Update the labeling function and generate the label times,

        Args:
            labeler (function):
                Function that defines the prediction task, it should return a
                tuple of labeling function, the dataframe, and the name of the
                target entity.
            parameter (dict):
                Variables to change the default parameters, if any.

        Returns:
            pandas.DataFrame:
                A dataframe of cutoff times and their target labels.
        """
        labeler = labeler or DEFAULT_LABELER

        if parameter:
            labeler = partial(labeler, **parameter)

        LOGGER.info("Using labeler %s", str(labeler.__name__))
        data_labeler = DataLabeler(labeler)

        # target label calculation
        label_times, self._target, self._type = data_labeler.generate_label_times(
            self.es)

        # set default pipeline
        self._set_modeler()

        return label_times

    def generate_features(self, label_times: pd.DataFrame,
                          verbose: bool = False) -> pd.DataFrame:
        """Returns a the calculated feature matrix.

        Args:
            label_times (pandas.DataFrame):
                A dataframe that indicates cutoff time for each instance.
            verbose (bool):
                Indicate verbosity of the featurization.

        Returns:
            pandas.DataFrame:
                Generated feature matrix.
        """

        fm, _ = self._featurization.generate_feature_matrix(
            self.es, self._target, label_times, verbose=verbose)

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

    def predict(self, X: Union[np.ndarray, pd.DataFrame]) -> Union[np.ndarray, list]:
        """Get predictions from the cardea pipeline.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.

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
            X_test = X
            y_test = y

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
        """Load an Orion instance from a pickle file.

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
