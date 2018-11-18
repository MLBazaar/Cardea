# -*- coding: utf-8 -*-

import logging
import types

import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


class TrivialPredictor(object):

    def __init__(self, default=0, method=None):
        self.prediction = default
        self.method = method
        self._method = getattr(self, '_' + method) if method else None

    def _mode(self, y):
        return y.mode().iloc[0]

    def _median(self, y):
        return y.median()

    def fit(self, y):
        if self._method:
            try:
                if not isinstance(y, pd.Series):
                    y = pd.Series(y)

                self.prediction = self._method(y)
            except Exception:
                LOGGER.error('Could not compute y.%s(). Using default.', self.method)

    def get_length(self, X):
        if isinstance(X, types.GeneratorType):
            try:
                return sum(len(x) for x in X)
            except TypeError:
                return sum(1 for _ in X)
        else:
            return len(X)

    def predict(self, X, length=None):
        length = length or self.get_length(X)
        return np.full(length, self.prediction)
