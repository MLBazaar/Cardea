# A more powerful imputation transformer that can be used to transform both numerical columns and
# categorical columns. This class is built from an answer on stackoverflow:
# https://stackoverflow.com/questions/25239958/impute-categorical-missing-values-in-scikit-learn

import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin


class Imputer(TransformerMixin):
    """Impute missing values. Columns of dtype object are imputed with the most frequent value
    in column. Columns of other types are imputed with mean of column.

    Args:
        strategy: str, the imputation strategy for numerical columns, should be either "mean",
        "median", and "most_frequent".

    """

    def __init__(self, strategy):
        self.fill = None
        self.strategy = strategy

    def fit(self, X):
        fill = []
        X = pd.DataFrame(X)
        for column in X.columns:
            if X[column].dropna().shape[0] > 0:
                if X[column].dtype == np.dtype('O'):
                    default_value = X[column].value_counts().index[0]
                else:
                    if self.strategy == 'mean':
                        default_value = X[column].mean()
                    elif self.strategy == 'median':
                        default_value = X[column].median()
                    elif self.strategy == 'most_frequent':
                        default_value = X[column].mode().iloc[0]
                    else:
                        raise ValueError("Strategy should be either \"mean\", \"median\", "
                                         "and \"most_frequent\".")
            else:  # TODO: remove totally null columns before running this primitive
                default_value = 0
            fill.append(default_value)
        self.fill = pd.Series(fill, index=X.columns)
        return self

    def transform(self, X):
        X = pd.DataFrame(X)
        X = X.fillna(self.fill)
        for column in X.columns:
            if X[column].dtype == np.dtype('O'):
                X[column] = X[column].apply(lambda x: str(x))
        return X
