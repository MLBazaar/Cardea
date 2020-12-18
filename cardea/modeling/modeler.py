import os
import pickle

from btb.session import BTBSession
import numpy as np
import sklearn
from mlblocks import MLPipeline
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold, train_test_split


class Modeler:
    """A class responsible for executing various Machine Learning Pipelines using MLBlocks."""

    _regression_metrics = {
        'explained_variance_score': sklearn.metrics.explained_variance_score,
        'mean_absolute_error': sklearn.metrics.mean_absolute_error,
        'mean_squared_error': sklearn.metrics.mean_squared_error,
        'mean_squared_log_error': sklearn.metrics.mean_squared_log_error,
        'median_absolute_error': sklearn.metrics.median_absolute_error,
        'r2_score': sklearn.metrics.r2_score
    }

    _classification_metrics = {
        'accuracy': sklearn.metrics.accuracy_score,
        'f1': lambda y_true, y_pred: sklearn.metrics.f1_score(y_true, y_pred, average="macro"),
        'precision': lambda y_true, y_pred: sklearn.metrics.precision_score(y_true, y_pred,
                                                                            average="macro"),
        'recall': lambda y_true, y_pred: sklearn.metrics.recall_score(y_true, y_pred,
                                                                      average="macro"),
    }

    def __init__(self, pipelines, problem_type):
        if isinstance(pipelines, dict):
            self._pipelines = {name: MLPipeline(pipeline) for name, pipeline in pipelines.items()}
        elif isinstance(pipelines, list):
            self._pipelines = {'pipeline_{}'.format(i): MLPipeline(pipeline)
                               for i, pipeline in enumerate(pipelines)}
        else:
            raise TypeError("Pipelines should be either list or dict. ")
        self._problem_type = problem_type
        self._best_name = None

    @staticmethod
    def train_test_split(X, y, test_size=0.2, shuffle=True):
        """Split the training dataset and the testing dataset."""
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

    def scoring_function(self, model_name, hyperparameters, X, y, scoring=None):
        """Score the pipeline through k-fold validation with the given scoring function.

        Args:
            model_name (str):
                The name of the target pipeline.
            hyperparameters (dict or None):
                A dictionary of hyper-parameters for each primitive in the target pipeline.
            X (array-like):
                Inputs of the pipeline.
            y (array-like):
                Target values.
            scoring (str):
                The name of the scoring function.

        Returns:
            np.float64:
                The average score in the k-fold validation.
        """
        model_instance = MLPipeline(self._pipelines[model_name])

        if hyperparameters:
            model_instance.set_hyperparameters(hyperparameters)

        if self._problem_type == 'regression':
            scorer = self.regression_metrics[scoring or 'r2_score']
        else:
            scorer = self.classification_metrics[scoring or 'f1']

        scores = []
        kf = KFold(n_splits=10, random_state=None, shuffle=True)
        for train_index, test_index in kf.split(X):
            model_instance.fit(X.iloc[train_index], y.iloc[train_index])
            y_pred = model_instance.predict(X.iloc[test_index])
            scores.append(scorer(y.iloc[test_index], y_pred))

        return np.mean(scores)

    def tune_select(self, X, y, max_evals=10, scoring=None, verbose=False):
        """ Tune the pipeline hyper-parameters and select the optimized model.

        Args:
            X (array-like):
                Inputs to the pipeline.
            y (array-like):
                Target values.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function.
            verbose(bool):
                Whether to log information during processing.
        """
        tunables = {name: pipeline.get_tunable_hyperparameters(flat=True)
                    for name, pipeline in self._pipelines.items()}

        session = BTBSession(tunables, lambda name, hyparam: self.scoring_function(
            name, hyparam, X=X, y=y, scoring=scoring), verbose=verbose)
        best_proposal = session.run(max_evals)
        self._best_name = best_proposal['name']
        self._pipelines[self._best_name].set_hyperparameters(best_proposal['config'])

    def fit(self, X_train, y_train, tune=False, max_evals=10, scoring=None, verbose=False):
        """Fit the pipelines.

        Args:
            X_train (array-like):
                Training data, inputs to the pipeline.
            y_train (array-like):
                Target values.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function.
            verbose(bool):
                Whether to log information during processing.
        """
        if tune:
            self.tune_select(X_train, y_train, max_evals=max_evals, scoring=scoring,
                             verbose=verbose)
        else:
            model_names = list(self._pipelines.keys())
            scores = [self.scoring_function(name, None, X_train, y_train, scoring=scoring)
                      for name in model_names]
            self._best_name = model_names[np.argmax(scores)]
        self._pipelines[self._best_name].fit(X_train, y_train)

    def predict(self, X_test):
        """Predict the input data

        Args:
            X_test (array-like):
                Testing data, inputs to the pipeline.

        Returns:
            array-like:
                Predictions to the input data.
        """
        if self._best_name:
            return self._pipelines[self._best_name].predict(X_test)
        else:
            raise ValueError("Modeler should be fitted before predict.")

    def test(self, X_test, y_test, scoring=None):
        """Test the trained pipeline.

        Args:
            X_test (array-like):
                Testing data, inputs to the pipeline.
            y_test (array-like):
                Target values.
            scoring (str):
                The name of the scoring function.

        Returns:
            float:
                The score of the trained pipeline on the inputs.
        """
        if self._problem_type == 'regression':
            scorer = self.regression_metrics[scoring or 'r2_score']
        else:
            scorer = self.classification_metrics[scoring or 'f1']
        return scorer(y_test, self.predict(X_test))

    def fit_predict(self, X_train, y_train, tune=False, max_evals=10, scoring=None, verbose=False):
        """Fit the pipeline and make predictions

        Args:
            X_train (array-like):
                Training data, inputs to the pipeline.
            y_train (array-like):
                Target values.
            tune (bool):
                Whether to optimize hyper-parameters of the pipelines.
            max_evals (int):
                Maximum number of hyper-parameter optimization iterations.
            scoring (str):
                The name of the scoring function.
            verbose(bool):
                Whether to log information during processing.

        Returns:
            array-like:
                Predictions to the input data.
        """
        self.fit(X_train, y_train, tune=tune, max_evals=max_evals, scoring=scoring,
                 verbose=verbose)
        return self.predict(X_train)

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
            raise ValueError('Serialized object is not an Modeler instance')
        return obj
