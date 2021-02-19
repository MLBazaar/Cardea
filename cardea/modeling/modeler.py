import os
import pickle

import numpy as np
import pandas as pd
import sklearn
from btb.session import BTBSession
from mlblocks import MLPipeline
from sklearn.model_selection import KFold, train_test_split


class Modeler:
    """A class responsible for executing various Machine Learning Pipelines using MLBlocks."""

    _regression_metrics = {
        'Explained Variance Score': sklearn.metrics.explained_variance_score,
        'Mean Absolute Error': sklearn.metrics.mean_absolute_error,
        'Mean Squared Error': sklearn.metrics.mean_squared_error,
        'Mean Squared Log Error': sklearn.metrics.mean_squared_log_error,
        'Median Absolute Error': sklearn.metrics.median_absolute_error,
        'R2 Score': sklearn.metrics.r2_score
    }

    _classification_metrics = {
        'Accuracy': sklearn.metrics.accuracy_score,
        'F1 Macro': lambda y_true, y_pred: sklearn.metrics.f1_score(y_true, y_pred,
                                                                    average="macro"),
        'Precision': lambda y_true, y_pred: sklearn.metrics.precision_score(y_true, y_pred,
                                                                            average="macro"),
        'Recall': lambda y_true, y_pred: sklearn.metrics.recall_score(y_true, y_pred,
                                                                      average="macro"),
        'Confusion Matrix': sklearn.metrics.confusion_matrix
    }

    def __init__(self, pipeline, problem_type):
        self._pipeline = MLPipeline(pipeline)
        self._problem_type = problem_type

    @staticmethod
    def train_test_split(X, y, test_size=0.2, shuffle=True):
        """Split the training dataset and the testing dataset.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            test_size (float):
                The proportion of the dataset to include in the test dataset.
            shuffle (bool):
                Whether or not to shuffle the data before splitting.

        Returns:
            list:
                List containing the train-test split of the inputs and targets.
        """
        return train_test_split(X, y, test_size=test_size, shuffle=shuffle)

    @property
    def regression_metrics(self):
        """Supported regression metrics functions.

        Returns:
            dict:
                A dictionary for regression metric functions.
        """
        return self._regression_metrics

    @property
    def classification_metrics(self):
        """Supported classification metrics functions.

        Returns:
            dict:
                A dictionary for classification metric functions.
        """
        return self._classification_metrics

    @property
    def target_metrics(self):
        """Supported metrics functions for the given problem type.

        Returns:
            dict:
                A dictionary for metric functions.
        """
        if self._problem_type == 'classification':
            return self._classification_metrics
        else:
            return self._regression_metrics

    @property
    def pipeline(self):
        """Pipeline.

        Returns:
            MLPipeline:
                The pipeline in the modeler.
        """
        return MLPipeline(self._pipeline)

    def k_fold_validation(self, hyperparameters, X, y, scoring=None):
        """Score the pipeline through k-fold validation with the given scoring function.

        Args:
            hyperparameters (dict or None):
                A dictionary of hyper-parameters for each primitive in the target pipeline.
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            scoring (str):
                The name of the scoring function.

        Returns:
            np.float64:
                The average score in the k-fold validation.
        """
        model_instance = MLPipeline(self._pipeline)
        X = pd.DataFrame(X)
        y = pd.Series(y)

        if hyperparameters:
            model_instance.set_hyperparameters(hyperparameters)

        if self._problem_type == 'regression':
            scorer = self.regression_metrics[scoring or 'R2 Score']
        else:
            scorer = self.classification_metrics[scoring or 'F1 Macro']

        scores = []
        kf = KFold(n_splits=10, random_state=None, shuffle=True)
        for train_index, test_index in kf.split(X):
            model_instance.fit(X.iloc[train_index], y.iloc[train_index])
            y_pred = model_instance.predict(X.iloc[test_index])
            scores.append(scorer(y.iloc[test_index], y_pred))

        return np.mean(scores)

    def tune(self, X, y, max_evals=10, scoring=None, verbose=False):
        """ Tune the pipeline hyper-parameters and select the optimized model.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function.
            verbose (bool):
                Whether to log information during processing.
        """
        tunables = {'0': self._pipeline.get_tunable_hyperparameters(flat=True)}

        session = BTBSession(tunables, lambda _, hyparam: self.k_fold_validation(
            hyparam, X=X, y=y, scoring=scoring), max_errors=max_evals, verbose=verbose)

        best_proposal = session.run(max_evals)
        self._pipeline.set_hyperparameters(best_proposal['config'])

    def fit(self, X, y, tune=False, max_evals=10, scoring=None, verbose=False):
        """Fit and select the pipelines.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
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
        if tune:
            # tune and select pipeline
            self.tune(X, y, max_evals=max_evals, scoring=scoring, verbose=verbose)

        # fit pipeline
        self._pipeline.fit(X, y)

    def predict(self, X):
        """Predict the input data

        Args:
            X (pandas.DataFrame or ndarray):
                Testing data, inputs to the pipeline.

        Returns:
            pandas.Series or ndarray:
                Predictions to the input data.
        """
        return self._pipeline.predict(X)

    def test(self, X, y, scoring=None):
        """Test the trained pipeline.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            scoring (str):
                The name of the scoring function.

        Returns:
            float:
                The score of the trained pipeline on the inputs.
        """
        if self._problem_type == 'regression':
            scorer = self.regression_metrics[scoring or 'R2 Score']
        else:
            scorer = self.classification_metrics[scoring or 'F1 Macro']
        return scorer(y, self.predict(X))

    def fit_predict(self, X, y, tune=False, max_evals=10, scoring=None, verbose=False):
        """Fit the pipeline and make predictions

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function used in the hyper-parameter optimization.
            verbose(bool):
                Whether to log information during processing.

        Returns:
            pandas.Series or ndarray:
                Predictions to the input data.
        """
        self.fit(X, y, tune=tune, max_evals=max_evals, scoring=scoring,
                 verbose=verbose)
        return self.predict(X)

    def evaluate(self, X, y, test_size=0.2, shuffle=True, tune=False, max_evals=10, scoring=None,
                 metrics=None, verbose=False):
        """Evaluate the pipelines.

        Args:
            X (pandas.DataFrame or ndarray):
                Inputs to the pipeline.
            y (pandas.Series or ndarray):
                Target values.
            test_size (float):
                The proportion of the dataset to include in the test dataset.
            shuffle (bool):
                Whether or not to shuffle the data before splitting.
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
        """
        X_train, X_test, y_train, y_test = self.train_test_split(X, y, test_size=test_size,
                                                                 shuffle=shuffle)
        metrics = metrics or self.target_metrics.keys()

        scores = {}
        self.fit(X_train, y_train, tune=tune, max_evals=max_evals, scoring=scoring,
                 verbose=verbose)
        for metric in metrics:
            scores[metric] = self.test(X_test, y_test, scoring=metric)
        return scores

    def save(self, path):
        """Save the object in a pickle file.

        Args:
            path (str): The path to store the modeler.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as pickle_file:
            pickle.dump(self, pickle_file)

    @staticmethod
    def load(path):
        """Load a Modeler object from a pickle file

        Args:
            path (str): The path to load the modeler.

        Returns:
            Modeler:
                A Modeler instance.
        """
        with open(path, 'rb') as pickle_file:
            obj = pickle.load(pickle_file)
        if not isinstance(obj, Modeler):
            raise ValueError('Serialized object is not a Modeler instance')
        return obj
