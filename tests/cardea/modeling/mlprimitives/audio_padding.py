# -*- coding: utf-8 -*-

import numpy as np


class AudioPadder(object):
    def __init__(self):
        self.padding = 0

    def fit(self, X):
        # Just obtain padding.
        for features in X:
            if len(features) > self.padding:
                self.padding = len(features)

    def _pad(self, features):
        if len(features) < self.padding:
            return np.lib.pad(
                features,
                (0, self.padding - len(features)),
                'constant',
                constant_values=0
            )

        else:
            return features[:self.padding]

    def produce(self, X):
        padded_features = np.vstack(map(self.pad, X))

        return np.nan_to_num(padded_features)
