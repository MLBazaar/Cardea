# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


class Counter():

    def __init__(self, scalar=True, add=0):
        self.scalar = scalar
        self.add = add

    def _count(self, column):
        raise NotImplementedError

    def count(self, X):
        if len(X.shape) > 2:
            raise ValueError('Only 1d or 2d arrays are supported')

        elif self.scalar and len(X.shape) == 2 and X.shape[1] == 2:
            raise ValueError('If scalar is True, only single column arrays are supported')

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X)

        self.counts = list()
        for column in X:
            count = self._count(X[column]) + self.add
            self.counts.append(count)

    def get_counts(self):
        if self.scalar:
            return self.counts[0]
        else:
            return np.array(self.counts)


class UniqueCounter(Counter):

    def _count(self, column):
        return len(np.unique(column))


class VocabularyCounter(Counter):

    def __init__(self, total=True, *args, **kwargs):
        self.total = total
        super().__init__(*args, **kwargs)

    def _count(self, column):
        count = 0
        if self.total:
            vocabulary = set()

        for text in column:
            words = text.split()
            if self.total:
                vocabulary.update(words)
                count = len(vocabulary)
            else:
                count = max(count, len(words))

        return count
