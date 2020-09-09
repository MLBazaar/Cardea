# -*- coding: utf-8 -*-

"""Main module."""
import warnings
from collections import Counter
from math import sqrt

import mlprimitives
import numpy as np
from mlblocks import MLPipeline
from scipy.stats import entropy
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from cardea.modeling.modeler import Modeler


class ModelAuditor():
    __name__ = 'ModelAuditor'

    def run_fold(self, features_train, target, feature_test, primitive, hyperparameters=None):
        '''Runs Kfold cross-validation where it predicts all the primitives within the pipeline.

        Args:
            features_train: the training features.
            features_test: the testing features.
            target: a list of the folds targets.
            primitive: the machine learning primitive to run.
            hyperparameters: the hyperparameters of the given primitives.

        Returns:
            A list of the folds' results for the primitives that are passed.
        '''

        # assert that the features and targets have the same size
        modeler = Modeler()
        #pipeline = self.create_pipeline(primitive, hyperparameters)
        pipeline = modeler.create_pipeline(primitive, hyperparameters)
        last_block_in_pipeline = list(pipeline.blocks.values())[-1]
        #Add an if statement based on the type of output for the last block (array, ndarray, DataFrame)
        for output in last_block_in_pipeline.produce_output:
            check_name = output['name'] == 'X' or output['name'] == 'y'
            check_numpy = output['type'] == 'array' or output['type'] == 'ndarray'
            check_pandas = output['type'] == 'DataFrame' or output['type'] == 'Series'
            if check_name and (check_numpy or check_pandas):
                features_train = pd.DataFrame(features_train)
                feature_test = pd.DataFrame(feature_test)
                target = pd.Series(target)
                return modeler.fit_predict_model(features_train, target, feature_test, pipeline)
        return None

    def generate_kfolds(self, features, target, n_folds=10):
        '''Creates Kfold cross-validation for the given features and targets

        Args:
            features: The features as a numpy array to create the k-folds for
            target: a list of the folds targets
            n_folds: the number of folds to create

        Returns:
            a tuple that consist of two values, the folds features and the folds targets
        '''
        kf = KFold(n_splits=n_folds, shuffle=True)
        folds_features = []
        folds_targets = []
        for train_index, test_index in kf.split(features):
            X_train = features[train_index]
            X_test = features[test_index]
            y_train = target[train_index]
            y_test = target[test_index]
            folds_features.append([X_train, X_test])
            folds_targets.append([y_train, y_test])

        return folds_features, folds_targets

    def execute_pipeline(self, pipeline_primitives, features_train, target,
                         features_test, problem_type, hyperparameters = None,
                         with_intermediate = False):
        '''Executes a pipeline and generates all the intermediates of the pipeline.

        Args:
            pipeline_primitives: Array of the pipeline primitives.
            features_train: the training features data to run through the pipeline.
            features_test: the testing features data to run through the pipeline.
            target: The target of the training data to run through the pipeline.
            problem_type: the type of the problem (classification or regression).
            hyperparameters: the hyperparameters to run for the model
            with_intermediate: A boolean to add or ignore the intermediates metrics.

        Returns:
            a tuple that consist of three values,the intermediates,
            the folds features and the folds targets.
        '''
        pipeline_intermediates = []
        if with_intermediate:
            all_partial_primitives = [pipeline_primitives[:index] for index in range(1,len(pipeline_primitives) + 1)]
        else:
            all_partial_primitives = [pipeline_primitives]
        for partial_primitives in all_partial_primitives:
            pipeline_results = self.run_fold(features_train, target,
                                             features_test, partial_primitives,
                                             hyperparameters)

            #if pipeline_results != None:
            pipeline_intermediates.append(pipeline_results)

        return pipeline_intermediates

    def report_regression_result(self, actual, predicted):
        '''Reports the prediction results for a regression model.

        Args:
            actual: A 1d list of the target variable for the actual test data.
            predicted: A 1d list of the prediction result.

        Returns:
            A json object of various evaluation metrics for regression.
        '''
        metrics_to_calculate = [['explained_variance_score', metrics.explained_variance_score],
                                ['mean_absolute_error', metrics.mean_absolute_error],
                                ['mean_squared_error', metrics.mean_squared_error],
                                ['mean_squared_log_error', metrics.mean_squared_log_error],
                                ['median_absolute_error', metrics.median_absolute_error],
                                ['r2_score', metrics.r2_score]]
        results_dict = {}
        for metric in metrics_to_calculate:
            try:
                results_dict[metric[0]] = metric[1](actual, predicted)
            except BaseException:
                warnings.warn(
                    '{} can\'t be calculated for this data'.format(metric[0]),
                    UserWarning)
        return results_dict

    def report_classification_result(self, actual, predicted):
        '''Reports the prediction results for a classification model.

        Args:
            actual: A 1d list of the target variable for the actual test data.
            predicted: A 1d list of the prediction result.
            n_class: Int of the number of classes in the classification problem.
            prediction_proba: The classes prediction probabilities that are
            produced by predict_proba.


        Returns:
            A json object of various evaluation metrics for classification.
        '''
        metrics_to_calculate = [['accuracy', metrics.accuracy_score],
                                ['f1', metrics.f1_score],
                                ['precision', metrics.precision_score],
                                ['recall', metrics.recall_score],
                                ['class_count', Counter]]
        results_dict = {}
        for metric in metrics_to_calculate:
            try:
                if metric[0] == 'accuracy':
                    results_dict[metric[0]] = metric[1](actual, predicted)
                elif metric[0] == 'class_count':
                    counter_dict = metric[1](predicted)
                    label_count_sum = sum(counter_dict.values())
                    for label in counter_dict.keys():
                        results_dict['{}_{}'.format(metric[0], str(
                            label))] = counter_dict[label] / label_count_sum
                else:
                    results_dict['{}_macro'.format(metric[0])] = metric[1](
                        actual, predicted, average='macro')
            except BaseException:
                warnings.warn(
                    '{} can\'t be calculated for this data'.format(metric[0]),
                    UserWarning)
        return results_dict

    def euclidean_distance(self, x, y):
        '''Computes the euclidean distance between two vectors.

        Args:
            x: The first vector.
            y: The second vector.

        Returns:
            The euclidean distance.
        '''
        return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))

    def intermediate_metrics(self, intermediate):
        '''Generates metrics of the intermediates (features data in-between primitives).

        Args:
            intermediate: The intermediate data that must be investigated (for a single fold).

        Returns:
            A Summary metrics for the different data columns in the intermediate.
        '''
        if type(intermediate) != pd.DataFrame:
            intermediate = pd.DataFrame(intermediate)
        summary = {}
        for column_name in list(intermediate.columns):
            intermediate_column = intermediate[column_name]
            col_metrics = {}
            col_metrics['index'] = column_name
            
            col_metrics['perc_25'] = np.percentile(intermediate_column, 25)
            col_metrics['perc_50'] = np.percentile(intermediate_column, 50)
            col_metrics['perc_75'] = np.percentile(intermediate_column, 75)
            
            col_metrics['variance'] = np.var(intermediate_column)
            col_metrics['std'] = np.std(intermediate_column)
            
            col_metrics['entropy'] = entropy(intermediate_column)

            summary[column_name] = col_metrics
        return summary

    def find_k_nearest_neighbors(self, data, instance, k=5):
        '''Finds the k-nearest neighbors from the data to an instance.

        Args:
            data: The data that will be searched to find the nearest neighbors.
            instance: the instance that needs to identify its nearest neighbors.
            k: the number of nearest neighbors to consider.

        Returns:
            Array of the k nearest neighbors to the instance.
        '''
        nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(data)
        distances, indices = nbrs.kneighbors([instance])

        return data[indices]

    def summarize_nearest_neighbors(self, folds_features, folds_targets, k=5):
        '''Summarizes the nearest neighbors of a sample in the data.

        Args:
            folds_features: The folds containing the training and testing of the features data.
            folds_targets: The folds containing the training and testing of the target data.
            k: the number of nearest neighbors to consider

        Returns:
            Summary of all the features for the nearest neighbors.
        '''
        nearest_neighbors_summary = []
        for x, y in zip(folds_features, folds_targets):
            X_train = x[0]
            X_test = x[1]
            y_test = y[1]

            indices_to_select = np.random.choice(range(len(X_test)), k, replace=False)
            chosen_instances_features = X_test[indices_to_select]
            chosen_instances_targets = y_test[indices_to_select]
            fold_nearest_neighbors_summary = []
            for instance_features, instance_target in zip(
                    chosen_instances_features, chosen_instances_targets):
                nearest_neighbors = self.find_k_nearest_neighbors(X_train, instance_features, k)
                neighbors_summary = self.intermediate_metrics(nearest_neighbors)
                fold_nearest_neighbors_summary.append({'instance_features': instance_features,
                                                       'instance_target': instance_target,
                                                       'neighbors_summary': neighbors_summary})

            nearest_neighbors_summary.append(fold_nearest_neighbors_summary)

        return nearest_neighbors_summary

    def generate_pipeline_report(self, pipeline_primitives, features,
                                 target, problem_type, hyperparameters = None,
                                 with_intermediates_metrics = False,
                                 with_nearest_neighbors = False):
        '''Generates the full report of the model auditor in a json format.

        Args:
            pipeline_primitives: Array of the pipeline primitives to run.
            features: The features data to run through the pipeline.
            target: The target data to run through the pipeline.
            problem_type: The type of the problem (classification or regression).
            hyperparameters: Specify parameters that must be specified in the primitives.
            with_nearest_neighbors: A boolean to add or ignore the nearest neighbors metrics.
            with_intermediates_metrics: A boolean to add or ignore the intermediates metrics.

        Returns:
            A json file of the model auditing results.
        '''

        report = {}
        # Generate the folds
        columns_names = list(features.columns)
        features = np.array(features)
        target = np.array(target)
        folds_features, folds_targets = self.generate_kfolds(features, target)
        # create the intermediates
        intermediates_list = []
        for x, y in zip(folds_features, folds_targets):
            X_train = pd.DataFrame(x[0],columns = columns_names)
            X_test = pd.DataFrame(x[1],columns = columns_names)
            y_train = y[0]
            fold_intermediates_list = self.execute_pipeline(pipeline_primitives, X_train,
                                                            y_train, X_test, problem_type,
                                                            with_intermediate = with_intermediates_metrics,
                                                            hyperparameters = hyperparameters)
            intermediates_list.append(fold_intermediates_list)

        # print(intermediates_list)
        output_result = []
        if problem_type == 'classification':
            for actual, predicted in zip(folds_targets, intermediates_list):
                fold_result = self.report_classification_result(actual[1], predicted[-1])
                output_result.append(fold_result)
        elif problem_type == 'regression':
            for actual, predicted in zip(folds_targets, intermediates_list):
                fold_result = self.report_regression_result(actual[1], predicted[-1])
                output_result.append(fold_result)
        report['output_result'] = output_result

        if with_intermediates_metrics:
            intermediates_metrics = {}
            for fold in intermediates_list:
                for idx,intermediate in enumerate(fold[:-1]):
                    intermediate_key = str(idx)+ '.' + pipeline_primitives[idx]
                    try:
                        intermediate_result = self.intermediate_metrics(intermediate)
                        intermediates_metrics[intermediate_key] = intermediate_result
                    except BaseException as e:
                        print(e.args)
                        warnings.warn(
                            'intermediate metrics can\'t be calculated for {}'.format(intermediate_key),
                            UserWarning)
            report['intermediates_result'] = intermediates_metrics

        if with_nearest_neighbors:
            nearest_neighbors = self.summarize_nearest_neighbors(folds_features, folds_targets, k=5)
            report['nearest_neighbors'] = nearest_neighbors

        return report

    def generate_pipeline_report_with_test(self, pipeline_primitives, features,
                                 target, test, actual, problem_type, hyperparameters = None,
                                 with_intermediates_metrics = False,
                                 with_nearest_neighbors = False):

        '''Generates the full report of the model auditor in a json format.

        Args:
            pipeline_primitives: Array of the pipeline primitives to run.
            features: The features data to run through the pipeline.
            target: The target data to run through the pipeline.
            problem_type: The type of the problem (classification or regression).
            hyperparameters: Specify parameters that must be specified in the primitives.
            with_nearest_neighbors: A boolean to add or ignore the nearest neighbors metrics.
            with_intermediates_metrics: A boolean to add or ignore the intermediates metrics.

        Returns:
            A json file of the model auditing results.
        '''

        report = {}
        # Generate the folds
        columns_names = list(features.columns)
        X_train = np.array(features)
        y_train = np.array(target)

        X_test = np.array(test)
        y_test = np.array(actual)

        # print("X_train ", X_train.shape)
        # print("y_train ", y_train.shape)
        # print("X_test ", X_test.shape)
        # print("y_test ", y_test.shape)

        y_pred = self.execute_pipeline(pipeline_primitives, X_train, y_train, X_test, problem_type,
                                                        with_intermediate=False,
                                                        hyperparameters=hyperparameters)

        output_result = []
        if problem_type == 'classification':
            fold_result = self.report_classification_result(y_test, y_pred[-1])
            output_result.append(fold_result)
        elif problem_type == 'regression':
            fold_result = self.report_regression_result(y_test, y_pred[-1])
            output_result.append(fold_result)
        report['output_result'] = output_result

        if with_nearest_neighbors:
            nearest_neighbors = self.summarize_nearest_neighbors(X_test, y_test, k=5)
            report['nearest_neighbors'] = nearest_neighbors

        return report

