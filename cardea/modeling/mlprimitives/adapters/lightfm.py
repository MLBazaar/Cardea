# -*- coding: utf-8 -*-

from scipy import sparse

import lightfm


class LightFM(lightfm.LightFM):

    def __init__(self, epochs=1, num_threads=1, *args, **kwargs):
        self.epochs = epochs
        self.num_threads = num_threads
        super(LightFM, self).__init__(*args, **kwargs)

    def get_columns(self, X):
        if hasattr(X, 'iloc'):
            return X.iloc[:, 0].values, X.iloc[:, 1].values
        else:
            return X[:, 0], X[:, 1]

    def fit(self, X, y):
        user_ids, item_ids = self.get_columns(X)
        X = sparse.csr_matrix((y, (user_ids, item_ids)))
        super(LightFM, self).fit(X, epochs=self.epochs, num_threads=self.num_threads)

    def predict(self, X):
        user_ids, item_ids = self.get_columns(X)
        predict = super(LightFM, self).predict
        return predict(user_ids, item_ids, num_threads=self.num_threads)
