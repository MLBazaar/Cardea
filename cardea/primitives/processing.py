# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from featuretools.selection import remove_low_information_features


def prune_cols(X):
    pruned = X.copy()
    identifiers = ['subjuct_id', 'row_id', 'hadm_id', 'cgid', 'itemid', 'icustay_id']

    # check what columns to make binary
    for col in X.columns:
        num = X[col].nunique()
        if (pruned[col].dtype == object and num > 100) \
                or col in identifiers:
            pruned.drop(col, axis=1, inplace=True)

    return pruned


def split_feature_matrix(X, problem=None, categorize=False):
    fm = X.copy()
    if problem is not None:
        try:
            fm = fm.drop([problem], axis=1)
        except BaseException:
            pass

    y = fm.pop('label')
    fm = remove_low_information_features(fm)

    fm = fm.fillna(0)
    fm = pd.get_dummies(fm)

    if categorize:
        if problem == 'los':
            y = np.digitize(y, [y.min(), 7, y.max() + 1])

        y = pd.Categorical(y).codes

    return fm.reset_index(drop=True).values, y


def digitize_los(y):
    if y is None:
        return None
    bins = [y.min(), 7, y.max() + 1]
    return np.digitize(y, bins)


def categorize(y):
    if y is None:
        return y
    dtype = pd.Categorical(y, ordered=True)
    y = dtype.codes
    return y, dtype


def from_codes(y, dtype):
    if y is None or dtype is None:
        return y
    return pd.Categorical.from_codes(y, dtype=dtype)


def preprocess_features(X):
    X = remove_low_information_features(X)
    X = X.fillna(0)
    X = pd.get_dummies(X)
    return X.values
