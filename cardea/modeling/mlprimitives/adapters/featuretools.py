# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
from featuretools import variable_types as vtypes
from featuretools.selection import remove_low_information_features


class DFS(object):

    def __init__(self, max_depth, features_only=True, remove_low_information=True):
        self.max_depth = max_depth
        self.features_only = features_only
        self.features = None
        self.remove_low_information = remove_low_information

    def fit(self, X, **kwargs):
        self.features = ft.dfs(
            cutoff_time=X,
            features_only=self.features_only,
            max_depth=self.max_depth,
            **kwargs
        )

    def produce(self, X, instance_ids=None, **kwargs):
        # TODO: review this

        if instance_ids is not None:
            feature_matrix = ft.calculate_feature_matrix(
                self.features,
                instance_ids=instance_ids,
                **kwargs
            )

            feature_matrix = (feature_matrix.reset_index('time')
                                            .loc[instance_ids, :]
                                            .set_index('time', append=True))

        else:
            feature_matrix = ft.calculate_feature_matrix(
                self.features, cutoff_time=X, **kwargs)

        for f in self.features:
            if issubclass(f.variable_type, vtypes.Discrete):
                feature_matrix[f.get_name()] = feature_matrix[f.get_name()].astype(object)
            elif issubclass(f.variable_type, vtypes.Numeric):
                feature_matrix[f.get_name()] = pd.to_numeric(feature_matrix[f.get_name()])
            elif issubclass(f.variable_type, vtypes.Datetime):
                feature_matrix[f.get_name()] = pd.to_datetime(feature_matrix[f.get_name()])

        encoded_fm, encoded_fl = ft.encode_features(feature_matrix, self.features)

        if self.remove_low_information:
            encoded_fm, encoded_fl = remove_low_information_features(encoded_fm, encoded_fl)

        encoded_fm.reset_index('time', drop=True, inplace=True)

        return encoded_fm.fillna(0)
