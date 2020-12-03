import copy
import os

import hyperopt
import mlblocks
import numpy as np
import pandas as pd
from hyperopt import STATUS_OK, Trials, base, fmin, hp, tpe
from mlblocks import MLPipeline
from sklearn import metrics
from sklearn.model_selection import KFold

base.have_bson = False


class Modeler():
    """A class responsible for executing various Machine Learning Pipelines using MLBlocks."""

    problem_type = None
    primitive = []
    pipeline_dict = {}
    scoring = None
    data_frame = None
    target = None
    minimize_cost = False

    regression_scoring_function = {'explained_variance_score': metrics.explained_variance_score,
                                   'mean_absolute_error': metrics.mean_absolute_error,
                                   'mean_squared_error': metrics.mean_squared_error,
                                   'mean_squared_log_error': metrics.mean_squared_log_error,
                                   'median_absolute_error': metrics.median_absolute_error,
                                   'r2_score': metrics.r2_score}
    classification_scoring_function = {'accuracy': metrics.accuracy_score,
                                       'f1': metrics.f1_score,
                                       'precision': metrics.precision_score,
                                       'recall': metrics.recall_score,
                                       }

    def get_directory(self):
        """Returns the path of the directory.

        Returns:
            The absolute path of MLplrimitive directory.
        """
        mypath = mlblocks.get_primitives_paths()[-1]
        return mypath

    def check_path(self, primitives):
        """Checks the path of each primitive in the pipeline.

        Args:
            primitives: A list of primitive.

        Returns:
            A list of primitives after edition.
        """
        new_list = []
        mypath = self.get_directory()

        for primitive in primitives:
            mypath = mypath + '/'
            primitive_file_name = primitive + '.json'
            if (mypath in primitive and os.path.exists(primitive_file_name)):
                new_list.append(primitive)
            elif (os.path.exists(mypath + primitive_file_name)):
                new_list.append(mypath + primitive)
        if new_list == []:
            raise ValueError(primitives, 'is not found in MLprimitives.')
        return new_list

    def check_path_hyperparameters(self, hyperparameters):
        """Checks the path of each hyperparameters in the pipeline.

        Args:
            hyperparameters: A list of hyperparameters.

        Returns:
            A list of hyperparameters after edition.
        """

        new_list = {}
        mypath = self.get_directory()
        hyperparameters_keys = hyperparameters.keys()

        for hyperparameter in hyperparameters_keys:
            mypath = mypath + '/'
            primitive_file_name = hyperparameter + '.json'

            if (mypath in hyperparameter and os.path.exists(primitive_file_name)):
                new_list[hyperparameter] = hyperparameters[hyperparameter]
            elif (os.path.exists(mypath + hyperparameter + ".json")):
                new_list[mypath + hyperparameter] = hyperparameters[hyperparameter]
        if new_list == {}:
            raise ValueError(list(hyperparameters_keys), 'is not found in MLprimitives.')
        return new_list

    def create_pipeline(self, primitives, hyperparameters=None):
        """Creates a pipeline of primitives.

        Args:
            primitives: A list of primitive.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A MLPipeline instance.
        """

        self.primitive = self.check_path(primitives)

        if hyperparameters is not None:
            hyperparameters = self.check_path_hyperparameters(hyperparameters)
            pipeline = MLPipeline(self.primitive, hyperparameters)
        else:
            pipeline = MLPipeline(self.primitive)
        return pipeline

    def fit_predict_model(self, X_train, y_train, X_test, pipeline):
        """Fits and predicts all the primitives within the pipeline.

        Args:
            X_train: A ndarray of the training data.
            y_train: An array of the training target variable.
            X_test: A ndarray of the testing data.
            pipeline: A MLPipeline instance.

        Returns:
            A list consists of the used pipeline and an array of the predicted values.
        """
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        return y_pred

    def search_all_possible_primitives(
            self, primitives, hyperparameters=None):
        """Searches for all primitives similar to the ones provided.

        Args:
            primitives: A list of primitive.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A list that encapsulate a list consisting of the fold number and the used pipeline and
            an array of the predicted values and an array of the actual values.
        """

        pipeline_list = []
        pipeline_list.append(
            self.create_kfold(primitives))

        return pipeline_list

    def create_kfold(self, primitives, hyperparameters=None):
        """Creates Kfold cross-validation and predicts all the primitives within the pipeline.

        Args:
            primitive: The name of the primitive.
            primitives_names: A list of the names of all the primitives similar
            to the ones provided.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A list consists of the fold number and the used pipeline and an array of
            the predicted values and an array of the actual values.
        """
        pipeline_list = []
        kf = KFold(n_splits=10, random_state=None, shuffle=True)
        self.data_frame = pd.DataFrame(self.data_frame)
        i = 0

        for train_index, test_index in kf.split(self.data_frame):
            predict_result = []

            X_train = self.data_frame.loc[train_index]
            X_test = self.data_frame.loc[test_index]
            y_train = self.target[train_index]
            y_test = self.target[test_index]

            # Append the fold number.
            predict_result.append(i)

            if hyperparameters is not None:
                pipeline = self.create_pipeline(primitives, hyperparameters)
            else:
                pipeline = self.create_pipeline(primitives)

            # Append the primitive name.
            predict_result.append(primitives)

            # Append the predicted labels.
            y_predict = self.fit_predict_model(X_train, y_train, X_test, pipeline)
            predict_result.append(y_predict)
            # Append the Actual labels.

            predict_result.append(y_test)
            pipeline_list.append(predict_result)

            i = i + 1
        return pipeline_list

    def kfold_scoring(self, data_frame, target, pipeline):
        """Calculate the average Kfold cross-validation score.

        Args:
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.
            pipeline: A MLPipeline instance.

        Returns:
            The average folds score.
        """

        fold_score = []
        macro = ['recall', 'f1', 'precision']
        number_of_folds = -1
        Folds = {}

        kf = KFold(n_splits=10, random_state=None, shuffle=True)
        data_frame = pd.DataFrame(data_frame)

        for train_index, test_index in kf.split(data_frame):
            X_train = data_frame.loc[train_index]
            X_test = data_frame.loc[test_index]
            y_train = target[train_index]
            y_test = target[test_index]
            number_of_folds = number_of_folds + 1
            # Append the predicted labels.
            # TODO: use MLPipeline(pipeline) to copy a pipeline with MLBlocks >= 0.3.4
            fold_pipeline = copy.deepcopy(pipeline)
            y_predict = self.fit_predict_model(X_train, y_train, X_test, fold_pipeline)

            Folds[str(number_of_folds)] = {
                "predicted": y_predict,
                "Actual": y_test,
                "pipeline": copy.deepcopy(fold_pipeline),
                "test_index": test_index
            }

            if self.problem_type == 'regression':
                if self.scoring is not None:
                    result = self.regression_scoring_function[self.scoring](y_predict, y_test)
                else:
                    result = self.regression_scoring_function['r2_score'](y_predict, y_test)
            else:
                if self.scoring is not None:
                    if self.scoring not in macro:
                        result = self.classification_scoring_function[self.scoring](
                            y_predict, y_test)
                    else:
                        result = self.classification_scoring_function[self.scoring](
                            y_predict, y_test, average='macro')
                else:
                    result = self.classification_scoring_function['f1'](
                        y_predict, y_test, average='macro')

            fold_score.append(result)
        self.pipeline_dict['folds'] = Folds
        return np.mean(fold_score)

    def create_space(self, pipeline):
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
        for block in list(pipeline.blocks.values()):
            space = {}

            tunable_hyperparameters = block.get_tunable_hyperparameters()
            primitive = str(block).split('MLBlock - ')[1]

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

    def hyperopt_train_test(self, params, pipeline=None):
        """Creates the objective function to minimize.

        Args:
            params: The parameter for a specific pipleline.

        Returns:
            The the model secore after K-fold corss-validation.
        """
        if pipeline is None:
            pipeline = self.create_pipeline(self.primitive, params)

        return self.kfold_scoring(self.data_frame, self.target, pipeline)

    def objective(self, params, pipeline=None):

        accuracy = self.hyperopt_train_test(params, pipeline)
        if not self.minimize_cost:
            accuracy = -accuracy
        return {'loss': accuracy, 'status': STATUS_OK}

    def hyperparameter_tunning(self, pipeline, max_evals):
        """Tuens and optimize the models' hyperparameter.

        Args:
            pipeline: A MLPipeline instance.
            max_evals: Maximum number of hyperparameter evaluations.

        Returns:
            A list of the tuned hyperparameter that best fits the model.
        """
        space = self.create_space(pipeline)

        trials = Trials()
        best = fmin(
            lambda param: self.objective(param, pipeline),
            space,
            algo=tpe.suggest,
            max_evals=max_evals,
            catch_eval_exceptions=True,
            trials=trials)

        best = hyperopt.space_eval(space, best)
        return best

    def optimization(self, pipeline, max_evals):
        """Tuens and optimize the models' hyperparameter.

        Args:
            pipeline: A MLPipeline instance.
            max_evals: Maximum number of hyperparameter evaluations.
        """
        hyperparameter = self.hyperparameter_tunning(pipeline, max_evals)
        self.pipeline_dict['hyperparameter'] = hyperparameter

    # TODO: remove this function in a later version
    def execute_pipeline(self, data_frame, target, primitives_list, problem_type,
                         optimize=False, max_evals=10, scoring=None,
                         minimize_cost=False, hyperparameters=None):
        """Executes and predict all the pipelines.

        Args:
            data_frame (pandas.DataFrame or ndarray):
                A dataframe which holds the feature matrix.
            target (ndarray):
                An array of labels for the target variable.
            primitives_list (list):
                A list of the primitives within a pipeline.
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
        all_pipeline_dict = {}
        Folds = {}
        self.scoring = scoring
        self.data_frame = data_frame
        self.problem_type = problem_type
        self.minimize_cost = minimize_cost
        if (not isinstance(target, np.ndarray)):
            target = np.asarray(target)
        self.target = target

        list_of_executed_pipelines = []
        for index, primitives in enumerate(primitives_list):

            pipleline_order = "pipeline" + str(index)

            if (optimize):
                self.primitive = primitives
                self.pipeline_dict['primitives'] = primitives
                pipeline = self.create_pipeline(primitives)
                self.optimization(pipeline, max_evals)

            else:
                list_of_executed_pipelines.append(
                    self.search_all_possible_primitives(primitives, hyperparameters))

                for fold in list_of_executed_pipelines[0][0]:
                    fold_number = fold[0]
                    Folds[str(fold_number)] = {"predicted": list_of_executed_pipelines[0][0][0][2],
                                               "Actual": list_of_executed_pipelines[0][0][0][3]}

                self.pipeline_dict = {'primitives': primitives,
                                      'folds': Folds,
                                      'hyperparameter': None}

            all_pipeline_dict[pipleline_order] = self.pipeline_dict
            self.pipeline_dict = {}
        return all_pipeline_dict

    def create_kfold_from_pipeline(self, pipeline):
        """Creates Kfold cross-validation and predicts all the primitives within the pipeline.

        Args:
            pipeline: A MLPipeline instance.

        Returns:
            Prediction results and trained models of each fold stored in a dictionary.
        """
        fold_dict = {}
        kf = KFold(n_splits=10, random_state=None, shuffle=True)
        self.data_frame = pd.DataFrame(self.data_frame)

        for i, (train_index, test_index) in enumerate(kf.split(self.data_frame)):
            fold_pipeline = copy.deepcopy(pipeline)

            X_train = self.data_frame.loc[train_index]
            X_test = self.data_frame.loc[test_index]
            y_train = self.target[train_index]
            y_test = self.target[test_index]

            # Append the predicted labels.
            y_predict = self.fit_predict_model(X_train, y_train, X_test, fold_pipeline)
            fold_dict[str(i)] = {"predicted": y_predict, "Actual": y_test,
                                 "pipeline": copy.deepcopy(fold_pipeline),
                                 "test_index": test_index}

        return fold_dict

    def execute_pipeline_from_pipeline(self, data_frame, target, pipelines, problem_type,
                                       optimize=False, max_evals=10, scoring=None,
                                       minimize_cost=False):
        """Executes and predict all the pipelines.

        Args:
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.
            pipelines: A list of MLPipeline instances.
            problem_type: A label to specify the type of problem whether
            regression or classification.
            optimize: A boolean value which indicates whether to optimize the model or not.
            max_evals: Maximum number of hyperparameter evaluations.
            scoring: A label to specify the scoring function.
            minimize_cost: A boolean value indicating whether to get minimum or maximum cost value.

        Returns:
            A list for all the pipelines which consists of: the fold number, the used pipeline
            and an array of the predicted values and an array of the actual values.
        """
        all_pipeline_dict = {}
        self.scoring = scoring
        self.data_frame = data_frame
        self.problem_type = problem_type
        self.minimize_cost = minimize_cost
        if not isinstance(target, np.ndarray):
            target = np.asarray(target)
        self.target = target

        for index, pipeline in enumerate(pipelines):
            pipleline_order = "pipeline" + str(index)

            if optimize:
                self.optimization(pipeline, max_evals)
                # TODO: Pass training results in function returns instead of class attributes
                pipeline_dict = self.pipeline_dict

            else:
                fold_dict = self.create_kfold_from_pipeline(pipeline)
                pipeline_dict = {
                    'primitives': pipeline.primitives,
                    'folds': fold_dict,
                    'hyperparameters': None
                }

            all_pipeline_dict[pipleline_order] = pipeline_dict
            self.pipeline_dict = {}
        return all_pipeline_dict
