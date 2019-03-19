#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mlblocks
import pytest
from sklearn.datasets import load_iris

from cardea.modeling.modeler import Modeler


@pytest.fixture()
def path():
    path = mlblocks.get_primitives_paths()[-1]
    return path


@pytest.fixture()
def primitives(get_model):
    primitives = get_model.check_path(['sklearn.ensemble.RandomForestRegressor'])
    return primitives


@pytest.fixture()
def primitives_list(get_model):
    primitives_list = get_model.check_path([
        'sklearn.preprocessing.imputer',
        'sklearn.ensemble.RandomForestRegressor'])
    return primitives_list


@pytest.fixture()
def load_data():
    training_testing = {}
    training_testing['X_train'] = [
        [5.5, 2.6, 4.4, 1.2],
        [5.8, 4.0, 1.2, 0.2],
        [5.0, 3.4, 1.6, 0.4],
        [6.2, 3.4, 5.4, 2.3],
        [5.4, 3.4, 1.5, 0.4],
        [5.4, 3.9, 1.3, 0.4],
        [4.6, 3.2, 1.4, 0.2],
        [5.1, 2.5, 3.0, 1.1],
        [5.5, 3.5, 1.3, 0.2],
        [5.2, 3.4, 1.4, 0.2]]
    training_testing['X_test'] = [[6., 3.4, 4.5, 1.6], [5., 3.3, 1.4, 0.2]]
    training_testing['y_train'] = [1, 0, 0, 2, 0, 0, 0, 1, 0, 0]
    training_testing['y_test'] = [1, 0]
    return training_testing


@pytest.fixture()
def get_model():
    model = Modeler()
    return model


@pytest.fixture()
def get_pipeline():
    model = Modeler()
    pipeline = model.create_pipeline(['sklearn.ensemble.RandomForestRegressor'])
    return pipeline


def test_get_directory(get_model, path):
    assert set(path) == set(get_model.get_directory())


def test_check_path(get_model):
    with pytest.raises(ValueError):
        get_model.check_path(['sklearn.ensemble.RandomForestClassifier1'])


def test_check_path_hyperparameters(get_model):
    with pytest.raises(ValueError):
        get_model.check_path_hyperparameters({'sklearn.svm.SVCC': {
            'max_iter': -1}})


def test_create_pipeline(get_model):
    with pytest.raises(ValueError):
        get_model.create_pipeline(['sklearn.svm.SVCC'])


def test_fit_predict_model_length(get_model, load_data, primitives):
    test_case = get_model.fit_predict_model(
        load_data['X_train'], load_data['y_train'], load_data['X_test'], get_model.create_pipeline(
            primitives))
    assert len(test_case) == 2


def test_create_kfold(get_model, primitives_list):
    iris = load_iris()
    get_model.data_frame = iris.data
    get_model.target = iris.target
    result = get_model.create_kfold(primitives_list)
    assert 10 == len(result)


def test_search_all_possible_primitives(get_model, primitives):
    iris = load_iris()
    get_model.data_frame = iris.data
    get_model.target = iris.target
    result = get_model.search_all_possible_primitives(primitives)
    assert len(result[0]) == 10


def test_create_space(get_model, get_pipeline):
    test_output = [
        'criterion',
        'max_features',
        'max_depth',
        'min_samples_split',
        'min_samples_leaf',
        'n_estimators',
        'min_impurity_decrease',
        'min_weight_fraction_leaf',
        'bootstrap',
        'oob_score']
    space = get_model.create_space(get_pipeline)
    space_values = list(space.values())[0]
    parameter = list(space_values.keys())
    assert set(parameter) == set(test_output)


def test_execute_pipeline_with_optimize(get_model):
    iris = load_iris()
    first_pipeline = ['sklearn.linear_model.LinearRegression']
    pipeline_list = [first_pipeline]
    result = get_model.execute_pipeline(iris.data, iris.target, pipeline_list, "regression", True)
    assert list(
        result.keys()) == [
            'pipeline0'] and result['pipeline0']['primitives'] == first_pipeline


def test_execute_pipeline_without_optimize(get_model):
    iris = load_iris()
    first_pipeline = ['sklearn.ensemble.RandomForestRegressor']
    second_pipeline = ['sklearn.linear_model.LinearRegression']
    pipeline_list = [first_pipeline, second_pipeline]
    result = get_model.execute_pipeline(iris.data, iris.target, pipeline_list, "regression", False)
    result_hyperparameter = result['pipeline0']['hyperparameter']
    assert set(list(result.keys())) == set(['pipeline0',
                                            'pipeline1']) and result_hyperparameter is None
