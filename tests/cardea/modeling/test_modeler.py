#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mlprimitives
import numpy as np
import pytest
from mlblocks import MLPipeline
from sklearn.datasets import load_iris

from cardea.modeling.modeler import Modeler


@pytest.fixture()
def path():
    path = mlprimitives.get_primitives_paths()[1] + '/'
    return path


@pytest.fixture()
def primitives(path):
    primitives = [path + 'sklearn.ensemble.RandomForestRegressor']
    return primitives


@pytest.fixture()
def primitives_no_tunning(path):
    primitive = MLPipeline([path + 'sklearn.decomposition.PCA'])
    return primitive


@pytest.fixture()
def primitives_list(path):
    primitives_list = [path + 'sklearn.ensemble.RandomForestClassifier',
                       path + 'sklearn.ensemble.RandomForestClassifier_proba']
    return primitives_list


@pytest.fixture()
def hyperparameters():
    hyperparameters = {
        'sklearn.svm.SVC': {
            'max_iter': -1
        }
    }
    return hyperparameters


@pytest.fixture()
def load_data():
    training_testing = {}
    training_testing['X_train'] = [
        [
            5.5, 2.6, 4.4, 1.2], [
            5.8, 4.0, 1.2, 0.2], [
                5.0, 3.4, 1.6, 0.4], [
                    6.2, 3.4, 5.4, 2.3], [
                        5.4, 3.4, 1.5, 0.4], [
                            5.4, 3.9, 1.3, 0.4], [
                                4.6, 3.2, 1.4, 0.2], [
                                    5.1, 2.5, 3.0, 1.1], [
                                        5.5, 3.5, 1.3, 0.2], [
                                            5.2, 3.4, 1.4, 0.2]]
    training_testing['X_test'] = [[6., 3.4, 4.5, 1.6], [5., 3.3, 1.4, 0.2]]
    training_testing['y_train'] = [1, 0, 0, 2, 0, 0, 0, 1, 0, 0]
    training_testing['y_test'] = [1, 0]
    return training_testing


@pytest.fixture()
def get_model():
    model = Modeler()
    return model


def test_get_directory(get_model, path):
    assert path == get_model.get_directory()


def test_check_path(get_model, path):
    path = path + 'sklearn.ensemble.RandomForestClassifier'
    result = get_model.check_path(['sklearn.ensemble.RandomForestClassifier'])
    assert [path] == result


def test_set_data(get_model):
    iris = load_iris()
    assert 4 == len(get_model.set_data(iris.data, iris.target, 0.2))


def test_search_all_possible_primitives(get_model, primitives):
    iris = load_iris()

    result = get_model.search_all_possible_primitives(iris.data, iris.target, primitives)
    assert 10 == len(result) and (result[0][3] is None)


def test_fit_predict_model_length(get_model, load_data, primitives):
    test_case = get_model.fit_predict_model(
        load_data['X_train'], load_data['y_train'], load_data['X_test'], get_model.create_pipeline(
            primitives))
    assert len(test_case) == 2


def test_create_kfold(get_model, primitives_list):
    iris = load_iris()
    print(primitives_list)
    result = get_model.create_kfold(
        iris.data,
        iris.target,
        'sklearn.ensemble.RandomForestClassifier',
        primitives_list)
    assert 5 == len(result[0])


def test_create_space(get_model, primitives_no_tunning):
    with pytest.raises(Exception):
        get_model.create_space(primitives_no_tunning)


def test_get_block(get_model):
    with pytest.raises(KeyError):
        get_model.get_block(MLPipeline(""))


def test_execute_pipeline(get_model, path):
    iris = load_iris()
    primitives_list = [
        [path + 'xgboost.XGBRegressor'],
        [path + 'sklearn.ensemble.RandomForestRegressor']]
    result = get_model.execute_pipeline(
        iris.data,
        iris.target,
        primitives_list,
        'regression',
        False)
    result = np.array(result)
    assert result.ndim == 3
