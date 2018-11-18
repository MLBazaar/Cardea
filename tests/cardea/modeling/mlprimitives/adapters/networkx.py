# -*- coding: utf-8 -*-

import logging

import numpy as np
import pandas as pd

from mlprimitives.utils import import_object

LOGGER = logging.getLogger(__name__)


def graph_pairs_feature_extraction(X, functions, node_columns, graph=None):
    functions = [import_object(function) for function in functions]

    X = X.copy()

    pairs = X[node_columns].values

    # for i, graph in enumerate(graphs):
    def apply(function):
        try:
            values = function(graph, pairs)
            return np.array(list(values))[:, 2]

        except ZeroDivisionError:
            LOGGER.warn("ZeroDivisionError captured running %s", function)
            return np.zeros(len(pairs))

    for function in functions:
        name = '{}_{}_{}'.format(function.__name__, *node_columns)
        X[name] = apply(function)

    return X


def graph_feature_extraction(X, functions, graphs):
    functions = [import_object(function) for function in functions]

    for node_column, graph in graphs.items():
        index_type = type(X[node_column].values[0])

        features = pd.DataFrame(index=graph.nodes)
        features.index = features.index.astype(index_type)

        def apply(function):
            values = function(graph)
            return np.array(list(values.values()))

        for function in functions:
            name = '{}_{}'.format(function.__name__, node_column)
            features[name] = apply(function)

        X = X.merge(features, left_on=node_column, right_index=True, how='left')

        graph_data = pd.DataFrame(dict(graph.nodes.items())).T
        graph_data.index = graph_data.index.astype(index_type)

        X = X.merge(graph_data, left_on=node_column, right_index=True, how='left')

    return X
