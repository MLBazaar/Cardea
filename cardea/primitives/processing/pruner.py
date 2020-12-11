import pandas as pd
from sklearn.base import TransformerMixin


class Pruner(TransformerMixin):
    """Prune identifier columns, columns with numerous tokens (>100) and columns
    with low information."""

    def __init__(self):
        self.pruned_columns = ['subjuct_id', 'row_id', 'hadm_id', 'cgid', 'itemid', 'icustay_id']

    def fit(self, X):
        X = pd.DataFrame(X)
        for col in X.columns:
            num = X[col].nunique()
            # Remove columns with numerous tokens (>100)
            if X[col].dtype == object and num > 100:
                self.pruned_columns.append(col)
            # Remove columns with low information (unique values <2)
            elif num <= 1 or X[col].dropna().shape[0] == 0:
                self.pruned_columns.append(col)
        return self

    def transform(self, X):
        X = pd.DataFrame(X)
        for column in X.columns:
            if column in self.pruned_columns:
                X.drop(column, axis=1, inplace=True)
        return X
