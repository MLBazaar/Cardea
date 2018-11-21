from os import listdir
from os.path import isfile, join

import hyperopt
import mlprimitives
import numpy as np
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
from mlblocks import MLPipeline
from sklearn.model_selection import KFold, cross_val_score, train_test_split


class Modeler():
    '''A class responsible for executing various Machine Learning Pipelines using MLBlocks.'''

    result = {}
    problem_type = ""
    block_instance = ""
    primitive = []

    def get_directory(self):
        '''Returns the path of the directory.

        Returns:
            The absolute path of the directory.
        '''
        mypath = mlprimitives.get_primitives_paths()[1] + "/"
        return mypath

    def check_path(self, primitives):
        '''Checks the path of each primitive in the pipeline.

        Args:
            primitives: A list of primitive.

        Returns:
            A list of primitives after edition.

        '''
        new_list = []
        mypath = self.get_directory()

        for primitive in primitives:
            if(mypath in primitive):
                new_list.append(primitive)
            else:
                new_list.append(mypath + primitive)
        return new_list

    def create_pipeline(self, primitives, hyperparameters=None):
        '''Creates a pipeline of primitives.

        Args:
            primitives: A list of primitive.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A MLPipeline instance.
        '''

        self.primitives = self.check_path(primitives)

        if hyperparameters is not None:
            pipeline = MLPipeline(primitives, hyperparameters)
        else:
            pipeline = MLPipeline(primitives)
        return pipeline

    def set_data(self, data_frame, target, test_size):
        '''Splits the data into training and testing data.

        Args:
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.
            test_size: The proportion of the dataset to include in the test split.

        Returns:
            A dictionary of the training and testing data.
        '''
        if(not isinstance(target, np.ndarray)):
            target = np.asarray(target)

        splitted = train_test_split(data_frame, target, test_size=test_size)
        self.result['X_train'] = splitted[0]
        self.result['X_test'] = splitted[1]
        self.result['y_train'] = splitted[2]
        self.result['y_test'] = splitted[3]
        return self.result

    def fit_predict_model(self, X_train, y_train, X_test, pipeline):
        '''Fits and predicts all the primitives within the pipeline.

        Args:
            X_train: A ndarray of the training data.
            y_train: An array of the training target variable.
            X_test: A ndarray of the testing data.

        Returns:
            A list consists of the used pipeline and an array of the predicted values.
        '''

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        return y_pred

    def search_all_possible_primitives(
            self, data_frame, target, primitives, hyperparameters=None):
        '''Searches for all primitives similar to the ones provided.

        Args:
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.
            primitives: A list of primitive.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A list that encapsulate a list consisting of the fold number and the used pipeline and
            an array of the predicted values and an array of the actual values.
        '''

        pipeline_list = []
        mypath = self.get_directory()

        primitives_names = []
        for primitive in primitives:
            primitive = primitive.split('/')[-1]
            primitives_names.append(mypath + primitive)

            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            for file in onlyfiles:
                file = file.split('/')[-1]
                filename = file.split(".json")[0]
                index = filename.rfind('_')
                file = filename[:index]
                if(file == primitive):
                    primitives_names.append(mypath + filename)

            pipeline_list = self.create_kfold(data_frame, target, primitive, primitives_names)
        return pipeline_list

    def create_kfold(self, data_frame, target, primitive, primitives_names, hyperparameters=None):
        '''Creates Kfold cross-validation and predicts all the primitives within the pipeline.

        Args:
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.
            primitive: The name of the primitive.
            primitives_names: A list of the names of all the primitives similar
            to the ones provided.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A list consists of the fold number and the used pipeline and an array of
            the predicted values and an array of the actual values.
        '''

        pipeline_list = []
        kf = KFold(n_splits=10, random_state=None, shuffle=True)
        i = 0

        for train_index, test_index in kf.split(data_frame):
            predict_result = []

            X_train = data_frame[train_index]
            X_test = data_frame[test_index]
            y_train = target[train_index]
            y_test = target[test_index]

            # Append the fold number.
            predict_result.append(i)

            for name in primitives_names:
                if hyperparameters is not None:
                    pipeline = self.create_pipeline([name], hyperparameters)
                else:
                    pipeline = self.create_pipeline([name])

                # Append the primitive name.
                if(primitive == name.split('/')[-1]):
                    predict_result.append(pipeline)

                # Append the predicted labels.
                predict_result.append(self.fit_predict_model(X_train, y_train, X_test, pipeline))
            # Append the Actual labels.
            if(len(primitives_names) == 1):
                predict_result.append(None)
            predict_result.append(y_test)
            pipeline_list.append(predict_result)

            i = i + 1
        return pipeline_list

    def execute_pipeline(self, data_frame, target, primitives_list,
                         problem_type, optimize=False, hyperparameters=None,):
        '''Executes and predict all the pipelines.

        Args:
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.
            primitives_list: A list of the primitives within a pipeline.
            problem_type: A label to specify the type of problem whether
            regression or classification.
            optimize: A boolean value which indicates whether to optimize the model or not.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A list for all the pipelines which consists of, the fold number and the used pipeline
            and an array of the predicted values and an array of the actual values.
        '''
        if(not isinstance(target, np.ndarray)):
            target = np.asarray(target)

        list_of_executed_pipelines = []
        for primitives in primitives_list:
            if(optimize):
                list_of_executed_pipelines.append([
                    self.find_opt_proba(primitives, data_frame, target, problem_type)])
            else:
                list_of_executed_pipelines.append(
                    self.search_all_possible_primitives(data_frame, target,
                                                        primitives, hyperparameters))
        return list_of_executed_pipelines

    def fit_predict_optimize_model(self, X_train, y_train, X_test, pipeline):
        '''Fits and predicts all the primitives within the pipeline to find
        the optimal hyperparameter.

        Args:
            X_train: A ndarray of the training data.
            y_train: An array of the training target variable.
            X_test: A ndarray of the testing data.
            pipeline: A MLPipeline instance.

        Returns:
            A list consists of the used pipeline and an array of the predicted values.
        '''
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        predict_result = [0, pipeline, y_pred, None, self.result['y_test']]
        return [predict_result]

    def create_space(self, pipeline):
        '''Creates the search space.

        Args:
            pipeline: A MLPipeline instance.

        Raises:
        Exception: If the value of tunnable hyperparameters is empty.

        Returns:
            A dictionary of the space over which to search.
        '''
        space = {}
        self.get_block(pipeline)
        tunable_hyperparameters = self.block_instance.get_tunable_hyperparameters()

        if(tunable_hyperparameters == {}):
            raise Exception(
                'Can not create the domain Space. The value of tunnable hyperparameters is: {}')

        for hyperparameter in tunable_hyperparameters:
            hp_type = list(tunable_hyperparameters[hyperparameter].keys())
            if('values' in hp_type):
                value = tunable_hyperparameters[hyperparameter]['values']
                space[hyperparameter] = hp.choice(hyperparameter, value)
            elif('range' in hp_type):
                value = tunable_hyperparameters[hyperparameter]['range']
                if(tunable_hyperparameters[hyperparameter]['type'] == 'float'):
                    space[hyperparameter] = hp.choice(
                        hyperparameter, np.linspace(
                            value[0], value[1], 10))
                elif (tunable_hyperparameters[hyperparameter]['type'] == 'str'):
                    space[hyperparameter] = hp.choice(hyperparameter, value)
                else:
                    space[hyperparameter] = hp.choice(
                        hyperparameter, np.arange(value[0], value[1], 1))
        return space

    def get_block(self, pipeline):
        blocks = pipeline.blocks
        block = blocks.popitem()
        self.block_instance = block[1]

    def hyperopt_train_test(self, params):
        '''Creates the objective function to minimize.

        Args:
            params: The parameter for a specific pipleline.

        Returns:
            The the model secore after K-fold corss-validation.
        '''
        pipeline = self.create_pipeline(self.primitives, {self.primitives[0]: params})
        self.get_block(pipeline)
        model = self.block_instance.instance
        if(self.problem_type == 'regression'):
            return cross_val_score(
                model, self.result['X_train'], self.result['y_train'], scoring='r2').mean()
        return cross_val_score(model, self.result['X_train'], self.result['y_train']).mean()

    def objective(self, params):

        accuracy = self.hyperopt_train_test(params)
        return {'loss': -accuracy, 'status': STATUS_OK}

    def hyperparameter_tunning(self, pipeline, data_frame, target):
        '''Tuens and optimize the models' hyperparameter.

        Args:
            pipeline: A MLPipeline instance.
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.

        Returns:
            A list of the tuned hyperparameter that best fits the model.
        '''
        self.set_data(data_frame, target, 0.3)
        space = self.create_space(pipeline)

        trials = Trials()
        best = fmin(self.objective, space, algo=tpe.suggest, max_evals=10, trials=trials)

        best = hyperopt.space_eval(space, best)
        return best

    def optimization(self, pipeline, data_frame, target, problem_type, opt_list):
        '''Tuens and optimize the models' hyperparameter.

        Args:
            pipeline: A MLPipeline instance.
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.

        Returns:
            A list of the tuned hyperparameter that best fits the model.
        '''
        self.problem_type = problem_type
        hyperparameter = self.hyperparameter_tunning(pipeline, data_frame, target)
        pipeline = self.create_pipeline(self.primitives, {self.primitives[0]: hyperparameter})
        opt_list.append(
            self.fit_predict_model(
                self.result['X_train'],
                self.result['y_train'],
                self.result['X_test'],
                pipeline))
        return opt_list

    def find_opt_proba(self, primitives_list, data_frame, target, problem_type):
        '''Tuens and optimize the models' hyperparameter.

        Args:
            pipeline: A MLPipeline instance.
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.

        Returns:
            A list of the tuned hyperparameter that best fits the model.
        '''
        not_predict_proba = True
        opt_list = []
        opt_list.append(0)

        mypath = self.get_directory()
        for primitive in primitives_list:
            primitive = primitive.split('/')[-1]

            primitives = mypath + primitive
            pipeline = self.create_pipeline([primitives])
            opt_list.append(pipeline)

            opt_list = self.optimization(pipeline, data_frame, target, problem_type, opt_list)

            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
            for file in onlyfiles:
                file = file.split('/')[-1]
                filename = file.split(".json")[0]
                index = filename.rfind('_')
                file = filename[:index]
                if(file == primitive):
                    primitives = mypath + primitive
                    opt_list = self.optimization(
                        self.create_pipeline(
                            [primitives]),
                        data_frame,
                        target,
                        problem_type,
                        opt_list)
                    not_predict_proba = False

            if(not_predict_proba):
                opt_list.append(None)

        opt_list.append(self.result['y_test'])
        return opt_list
