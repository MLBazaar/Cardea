# -*- coding: utf-8 -*-

"""
MLPrimitives Evaluation functions.

Collection of functions and tools to evaluate the performance
of a pipeline over a given dataset.
"""

import json
import logging
from copy import copy

import numpy as np
from mlblocks import MLPipeline, datasets

LOGGER = logging.getLogger(__name__)


def build_pipeline(pipeline_spec):
    pipeline = MLPipeline(
        pipeline_spec['primitives'],
        pipeline_spec.get('init_params', dict()),
        pipeline_spec.get('input_names', dict()),
        pipeline_spec.get('output_names', dict()),
    )

    hyperparameters = pipeline_spec.get('hyperparameters')
    if hyperparameters:
        pipeline.set_hyperparameters(hyperparameters)

    return pipeline


def load_dataset(name):
    loader_name = 'load_' + name
    loader = getattr(datasets, loader_name)
    return loader()


def get_value(dataset, value):
    if isinstance(value, str) and value.startswith('$'):
        value = getattr(dataset, value[1:])
    elif isinstance(value, dict):
        value = get_context(dataset, value)
    elif isinstance(value, list):
        value = [get_value(dataset, v) for v in value]

    return copy(value)


def get_context(dataset, context_spec):
    context = dict()
    for key, value in context_spec.items():
        context[key] = get_value(dataset, value)

    return context


def score_pipeline(pipeline_metadata, n_splits=5):
    if isinstance(pipeline_metadata, str):
        LOGGER.info('Loading pipeline %s', pipeline_metadata)
        with open(pipeline_metadata, 'r') as pipeline_file:
            pipeline_metadata = json.load(pipeline_file)

    validation = pipeline_metadata['validation']
    dataset = validation['dataset']
    LOGGER.info('Loading dataset %s', dataset)
    dataset = load_dataset(dataset)

    scores = list()
    splits = dataset.get_splits(n_splits)
    if n_splits == 1:
        splits = [splits]

    for split, (X_train, X_test, y_train, y_test) in enumerate(splits):
        LOGGER.info('Scoring split %s', split + 1)
        context = get_context(dataset, validation.get('context', dict()))
        pipeline = build_pipeline(pipeline_metadata)
        pipeline.fit(X_train, y_train, **context)
        predictions = pipeline.predict(X_test, **context)

        score = dataset.score(y_test, predictions)
        LOGGER.info('Obtained score %s', score)

        scores.append(score)

    return np.mean(scores), np.std(scores)
