"""Cardea Functional API.

This module provides a collection of simple python functions that
allow using Cardea performing as little steps as possible. The
API is oriented around various prediction problems.
"""
import logging
from typing import List, Union

import pandas as pd
from mlblocks import MLPipeline

from cardea import Cardea
from cardea.core import DEFAULT_METRICS, DEFAULT_PIPELINE
from cardea.data_labeling import appointment_no_show

LOGGER = logging.getLogger(__name__)


def _run(cls, labeler, max_depth, max_features, n_jobs, test_size, shuffle, tune, max_evals,
         scoring, evaluate, metrics, return_lt, return_fm, return_pred, verbose):
    output = dict()
    # labeling
    label_times = cls.label(labeler, verbose=verbose)
    if return_lt:
        output['label_times'] = label_times

    # featurizing
    fm = cls.featurize(label_times, max_depth=max_depth, max_features=max_features,
                       n_jobs=n_jobs, verbose=verbose)
    if return_fm:
        output['feature_matrix'] = fm

    # modeling
    y = fm.pop('label').values
    X = fm.values
    X_train, X_test, y_train, y_test = cls.train_test_split(
        X, y, test_size=test_size, shuffle=shuffle)

    if test_size == 0.:
        LOGGER.info("Setting test data equal to train data")
        X_test, y_test = X_train, y_train

    cls.fit(X_train, y_train, tune=tune, max_evals=max_evals, scoring=scoring, verbose=verbose)

    if return_pred:
        y_pred = cls.predict(X_test)
        output['prediction'] = y_pred

    if evaluate:
        result = cls.evaluate(X=X_test, y=y_test, fit=False, metrics=metrics)
        output['evaluate'] = result

    if len(output) > 0:
        return output

    return None


def model_appnoshow(data_path: str, fhir: bool = False,
                    pipeline: Union[str, dict, MLPipeline] = DEFAULT_PIPELINE,
                    hyperparameters: Union[str, pd.DataFrame] = None, max_depth: int = 1,
                    max_features: int = -1, n_jobs: int = 1, test_size: float = 0.2,
                    shuffle: bool = True, tune: bool = False, max_evals: int = 10,
                    scoring: str = None, evaluate: bool = False,
                    metrics: List[str] = DEFAULT_METRICS, return_lt: bool = False,
                    return_fm: bool = False, return_pred: bool = False, verbose: bool = False,
                    save_path: str = None) -> Cardea:
    """Create and train an appointment no show cardea instance.

    Return a cardea class object that has been trained on the given
    dataset. The function loads the data, extracts label times, generates
    features, then trains the pipeline all in one command.

    Args:
        data_path (str):
            A directory of all .csv files that should be loaded.
        fhir (bool):
            An indicator whether FHIR or MIMIC schema is used.
        pipeline (str or MLPipeline or dict):
            Pipeline to use. It can be passed as:
                * An ``str`` with a path to a JSON file.
                * An ``str`` with the name of a registered pipeline.
                * An ``str`` with the path to a pickle file.
                * An ``MLPipeline`` instance.
                * A ``dict`` with an ``MLPipeline`` specification.
        hyperparameters (str or dict):
            Hyperparameters to set to the pipeline. It can be passed as
            a hyperparameters ``dict`` in the ``mlblocks`` format or as
            a path to the corresponding JSON file. Defaults to ``None``.
        max_depth (int):
            Maximum allowed depth of features.
        max_features (int):
            Cap to the number of generated features. If -1, no limit.
        n_jobs (int):
            Number of parallel processes to use when calculating the
            feature matrix.
        test_size (float):
            The proportion of the dataset to include in the test dataset.
        shuffle (bool):
            Whether or not to shuffle the data before splitting.
        tune (bool):
            Whether to optimize hyper-parameters of the pipelines.
        max_evals (int):
            Maximum number of hyper-parameter optimization iterations.
        scoring (str):
            The name of the scoring function used in the hyper-parameter
            optimization.
        evaluate (bool):
            Whether to evaluate the performance of the pipeline. If True,
            we evaluate the performance on the test data, if not given,
            evaluate on train data.
        metrics (list):
            A list of scoring function names. The scoring functions should
            be consistent with the problem type.
        return_lt (bool):
            Whether to return ``label_times``.
        return_fm (bool):
            Whether to return the calculated feature matrix.
        return_pred (bool):
            Whether to return the predictions of the pipeline.
        verbose (bool):
            Whether to log information during processing.
        save_path (str):
            Path to the file where the fitted pipeline will be stored
            using ``pickle``.

        Returns:
            Cardea:
                A fitted Cardea instance.
        """

    cardea = Cardea(data_path=data_path,
                    fhir=fhir,
                    pipeline=pipeline,
                    hyperparameters=hyperparameters)

    # define labeler
    labeler = appointment_no_show
    output = _run(cardea, labeler, max_depth, max_features, n_jobs, test_size, shuffle, tune,
                  max_evals, scoring, evaluate, metrics, return_lt, return_fm, return_pred,
                  verbose)

    if save_path:
        cardea.save(save_path)

    if len(output) > 0:
        return cardea, output

    return cardea
