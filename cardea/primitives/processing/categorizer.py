import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin


class Categorizer(TransformerMixin):
    """Transform categorical values into numerical codes.
    """

    def __init__(self):
        self.categories = None
        self.dtype = None

    def fit(self, y):
        self.categories = pd.Categorical(y, ordered=True).categories
        self.dtype = np.array(y).dtype
        return self

    def transform(self, y):
        if y is None:
            return y
        return pd.Categorical(y, categories=self.categories).codes

    def inverse_transform(self, y_codes):
        return np.array(pd.Categorical.from_codes(y_codes, categories=self.categories))\
            .astype(self.dtype)
