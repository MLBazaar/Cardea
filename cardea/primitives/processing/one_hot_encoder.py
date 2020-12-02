import pandas as pd
from sklearn.base import TransformerMixin


class OneHotEncoder(TransformerMixin):
    """Encode categorical columns into one-hot codes.
    """

    def __init__(self):
        self.dummy_columns = None

    def fit(self, X):
        X = pd.DataFrame(X)
        dummies = pd.get_dummies(X)
        self.dummy_columns = dummies.columns
        return self

    def transform(self, X):
        X = pd.DataFrame(X)
        dummies = pd.get_dummies(X)
        return dummies.reindex(columns=self.dummy_columns, fill_value=0)
