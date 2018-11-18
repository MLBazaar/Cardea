# -*- coding: utf-8 -*-

from sklearn.preprocessing import LabelEncoder


class ClassEncoder():

    def __init__(self):
        self._label_encoder = LabelEncoder()

    def fit(self, y):
        self._label_encoder.fit(y)

    def encode(self, y):
        if y is not None:
            classes = self._label_encoder.classes_
            y = self._label_encoder.transform(y)
            return y, classes


class ClassDecoder():

    def __init__(self):
        self._label_encoder = LabelEncoder()

    def fit(self, classes):
        self._label_encoder.classes_ = classes

    def decode(self, y):
        return self._label_encoder.inverse_transform(y)
