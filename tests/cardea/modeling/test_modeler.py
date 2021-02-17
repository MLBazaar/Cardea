#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from mlblocks import MLPipeline
from sklearn.datasets import load_iris

from cardea.modeling.modeler import Modeler


@pytest.fixture()
def get_pipeline():
    pipeline = MLPipeline(['sklearn.preprocessing.MinMaxScaler',
                           'sklearn.ensemble.RandomForestClassifier'])
    return pipeline


@pytest.fixture()
def get_model(get_pipeline):
    model = Modeler(get_pipeline, problem_type='classification')
    return model


@pytest.fixture()
def get_data():
    return load_iris(return_X_y=True)


def test_k_fold_validation(get_model, get_data):
    X, y = get_data
    score = get_model.k_fold_validation(hyperparameters=None, X=X, y=y)
    assert 1 >= score > 0


def test_tune(get_model, get_data):
    X, y = get_data
    get_model.tune(X, y, max_evals=10, scoring='F1 Macro', verbose=False)


def test_evaluate_without_tuning(get_model, get_data):
    X, y = get_data
    scores = get_model.evaluate(X, y, tune=False)
    assert isinstance(scores, dict) and len(scores) > 0


def test_evaluate_with_tuning(get_model, get_data):
    X, y = get_data
    scores = get_model.evaluate(X, y, tune=True)
    assert isinstance(scores, dict) and len(scores) > 0


def test_fit_predict(get_model, get_data):
    X, y = get_data
    X_train, X_test, y_train, y_test = Modeler.train_test_split(X, y)
    model = get_model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    assert y_pred.shape == y_test.shape


def test_regression_metrics_property(get_model):
    regression_metrics = get_model.regression_metrics
    assert isinstance(regression_metrics, dict) and len(regression_metrics) > 0
