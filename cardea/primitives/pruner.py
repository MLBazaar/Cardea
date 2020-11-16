import numpy as np
import pandas as pd

from sklearn.base import TransformerMixin


class Pruner(TransformerMixin):
    """Impute missing values. Columns of dtype object are imputed with the most frequent value
    in column. Columns of other types are imputed with mean of column.

    Args:
        strategy: str, the imputation strategy for numerical columns, should be either "mean",
        "median", and "most_frequent".

    """

    def __init__(self):
        self.pruned_columns = ['subjuct_id', 'row_id', 'hadm_id', 'cgid', 'itemid', 'icustay_id']

    def fit(self, X):
        for col in X.columns:
            num = X[col].nunique()
            if X[col].dtype == object and num > 100:
                self.pruned_columns.append(col)
        return self

    def transform(self, X):
        X = X.copy()
        for column in X.columns:
            if column in self.pruned_columns:
                X.drop(column, axis=1, inplace=True)
        return X
