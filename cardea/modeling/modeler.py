from btb.session import BTBSession
import hyperopt
import numpy as np
import sklearn
from hyperopt import Trials, base, fmin, hp, tpe
from mlblocks import MLPipeline
from sklearn.model_selection import KFold

base.have_bson = False


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

    def __init__(self):
        self.problem_type = None
        self.minimize_cost = False
        self.features = None
        self.target = None
        self.metric = None
        self.max_evals = None

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

    def _run_kfolds(self, pipeline):
        """Creates Kfold cross-validation and predicts all the primitives within the pipeline.

        Args:
            pipeline (MLPipeline):
                A MLPipeline instance.

        Returns:
            dict:
                A dictionary for prediction results and trained models of each fold.
        """
        fold_dict = {}
        kf = KFold(n_splits=10, random_state=None, shuffle=True)

        for i, (train_index, test_index) in enumerate(kf.split(self.features)):
            fold_pipeline = MLPipeline(pipeline)

            X_train = self.features.loc[train_index]
            X_test = self.features.loc[test_index]
            y_train = self.target[train_index]
            y_test = self.target[test_index]

            fold_pipeline.fit(X_train, y_train)
            y_predict = fold_pipeline.predict(X_test)

            fold_dict[str(i)] = {"predicted": y_predict, "Actual": y_test,
                                 "pipeline": MLPipeline(fold_pipeline),
                                 "test_index": test_index}

        return fold_dict

    def _score_kfolds(self, fold_dict):
        """Score the average prediction results from Kfold cross-validation results.

        Args:
            fold_dict (dict):
                A dictionary for prediction results and trained models of each fold.

        Returns:
            float:
                The average score in the Kfold cross-validation.
        """

        fold_score = []
        metric = self.metric
        for _, fold in fold_dict.items():
            if self.problem_type == 'regression':
                if metric is None:
                    metric = 'r2_score'
                result = self.regression_metrics[metric](fold['Actual'], fold['predicted'])
            else:
                if metric is None:
                    metric = 'f1'
                result = self.classification_metrics[metric](fold['Actual'], fold['predicted'])

            fold_score.append(result)
        return np.mean(fold_score)

    def _cross_validate(self, hyperparameters, pipeline):
        """Calculate the average Kfold cross-validation score.

        Args:
            hyperparameters (dict):
                A dictionary of hyperparameters for each primitives.
            pipeline (MLPipeline):
                A MLPipeline instance.

        Returns:
            float:
                The average score in the Kfold cross-validation.
        """
        pipeline = MLPipeline(pipeline)

        if hyperparameters:
            pipeline.set_hyperparameters(hyperparameters)

        fold_dict = self._run_kfolds(pipeline)
        score = self._score_kfolds(fold_dict)

        if not self.minimize_cost:
            score = -score

        return score

    # TODO: remove this function in the future version
    def _create_space(self, pipeline):
        """Creates the search space.
        Args:
            pipeline: A MLPipeline instance.
        Raises:
        Exception: If the value of tunnable hyperparameters is empty.
        Returns:
            A dictionary of the space over which to search.
        """
        space = {}
        space_list = {}
        for primitive, block in pipeline.blocks.items():
            space = {}

            tunable_hyperparameters = block.get_tunable_hyperparameters()

            for hyperparameter in tunable_hyperparameters:
                hp_type = list(tunable_hyperparameters[hyperparameter].keys())
                if ('values' in hp_type):
                    value = tunable_hyperparameters[hyperparameter]['values']
                    space[hyperparameter] = hp.choice(hyperparameter, value)
                elif ('range' in hp_type):
                    value = tunable_hyperparameters[hyperparameter]['range']
                    if (tunable_hyperparameters[hyperparameter]['type'] == 'float'):
                        values = np.linspace(value[0], value[1], 10)
                        if (tunable_hyperparameters[hyperparameter]['default'] is None):
                            np.append(values, None)
                        space[hyperparameter] = hp.choice(
                            hyperparameter, values)
                    elif (tunable_hyperparameters[hyperparameter]['type'] == 'str'):
                        space[hyperparameter] = hp.choice(hyperparameter, value)
                    else:
                        values = np.arange(value[0], value[1], 1)
                        if (tunable_hyperparameters[hyperparameter]['default'] is None):
                            np.append(values, None)
                        space[hyperparameter] = hp.choice(
                            hyperparameter, values)
                elif (tunable_hyperparameters[hyperparameter]['type'] == 'bool'):
                    space[hyperparameter] = hp.choice(hyperparameter, [True, False])

            space_list[primitive] = space
            if (space_list == {}):
                raise Exception('Can not create the domain Space.\
                    The value of tunnable hyperparameters is: {}')
        return space_list

    # TODO: remove this function in the future version
    def _optimize_with_hyperopt(self, pipeline):
        """Tuens and optimize the models' hyperparameter.

        Args:
            pipeline: A MLPipeline instance.
            max_evals: Maximum number of hyperparameter evaluations.
        """
        space = self._create_space(pipeline)

        trials = Trials()
        best = fmin(
            lambda param: self._cross_validate(param, pipeline),
            space,
            algo=tpe.suggest,
            max_evals=self.max_evals,
            catch_eval_exceptions=False,
            trials=trials)

        return hyperopt.space_eval(space, best)

    def _optimize_with_btb(self, pipeline):
        """Optimize the pipeline's hyperparameters.

        Args:
            pipeline (MLPipeline):
                A MLPipeline instance.

        Returns:
            dict:
                The optimized hyperparameters,
        """
        tunables = {'0': pipeline.get_tunable_hyperparameters(flat=True)}
        session = BTBSession(tunables, lambda _, hyparam: self._cross_validate(hyparam, pipeline),
                             verbose=True)
        session.run(self.max_evals)
        return session.best_proposal['config']

    def execute_pipeline(self, data_frame, target, pipelines, problem_type,
                         optimize=False, max_evals=10, scoring=None,
                         minimize_cost=False, hyperparameters=None):
        """Executes and predict all the pipelines.

        Args:
            data_frame (pandas.DataFrame or ndarray):
                A dataframe which holds the feature matrix.
            target (ndarray):
                An array of labels for the target variable.
            pipelines (list):
                A list of MLPipeline instances or the primitives within a pipeline.
            problem_type (str):
                A label to specify the type of problem whether regression or classification.
            optimize (bool):
                A boolean value which indicates whether to optimize the model or not.
            max_evals (int):
                Maximum number of hyperparameter evaluations.
            scoring (str):
                A label to specify the scoring function.
            minimize_cost (bool):
                A boolean value indicating whether to get minimum or maximum cost value.
            hyperparameters (dict):
                A dictionary of hyperparameters for each primitives.

        Returns:
            dict:
                A dictionary for all the pipelines which consists of: the fold number, the used
                pipeline and an array of the predicted values and an array of the actual values.
        """
        self.problem_type = problem_type
        self.minimize_cost = minimize_cost
        self.features = data_frame
        self.target = target
        self.metric = scoring
        self.max_evals = max_evals

        all_pipeline_dict = {}
        for index, pipeline in enumerate(pipelines):

            pipeline = MLPipeline(pipeline)
            pipeline_dict = {'primitives': pipeline.primitives,
                             'folds': None, 'hyperparameters': None}

            if optimize:
                pipeline_dict['hyperparameters'] = self._optimize_with_btb(pipeline)
                pipeline.set_hyperparameters(pipeline_dict['hyperparameters'])

            pipeline_dict['folds'] = self._run_kfolds(pipeline)
            all_pipeline_dict["pipeline" + str(index)] = pipeline_dict

        return all_pipeline_dict
