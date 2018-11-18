# -*- coding: utf-8 -*-

import logging

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

LOGGER = logging.getLogger(__name__)


class OneHotLabelEncoder(object):
    """Combination of LabelEncoder + OneHotEncoder.

    >>> df = pd.DataFrame([
    ... {'a': 'a', 'b': 1, 'c': 1},
    ... {'a': 'a', 'b': 2, 'c': 2},
    ... {'a': 'b', 'b': 2, 'c': 1},
    ... ])
    >>> OneHotLabelEncoder().fit_transform(df.a)
       a=a  a=b
    0    1    0
    1    1    0
    2    0    1
    >>> OneHotLabelEncoder(max_labels=1).fit_transform(df.a)
       a=a
    0    1
    1    1
    2    0
    >>> OneHotLabelEncoder(name='a_name').fit_transform(df.a)
       a_name=a  a_name=b
    0         1         0
    1         1         0
    2         0         1
    """

    def __init__(self, name=None, max_labels=None):
        self.name = name
        self.max_labels = max_labels

    def fit(self, feature):
        self.dummies = pd.Series(feature.value_counts().index).astype(str)
        if self.max_labels:
            self.dummies = self.dummies[:self.max_labels]

    def transform(self, feature):
        name = self.name or feature.name
        dummies = pd.get_dummies(feature.astype(str))
        dummies = dummies.reindex(columns=self.dummies, fill_value=0)
        dummies.columns = ['{}={}'.format(name, c) for c in self.dummies]
        return dummies

    def fit_transform(self, feature):
        self.fit(feature)
        return self.transform(feature)


class FeatureExtractor(object):
    """Single FeatureExtractor applied to multiple features."""

    def __init__(self, copy=True, features=None):
        self.copy = copy
        self.features = features or []
        self._features = []

    def detect_features(self, X):
        features = []
        for column in X.columns:
            if not np.issubdtype(X[column].dtype, np.number):
                features.append(column)

        return features

    def _fit(self, x):
        pass

    def fit(self, X, y=None):
        if self.features == 'auto':
            self._features = self.detect_features(X)
        else:
            self._features = self.features

        for feature in self._features:
            self._fit(X[feature])

    def _transform(self, x):
        pass

    def transform(self, X):
        if self.copy and self._features:
            X = X.copy()

        for feature in self._features:
            LOGGER.debug("Extracting feature %s", feature)
            x = X.pop(feature)
            extracted = self._transform(x)
            X = pd.concat([X, extracted], axis=1)

        return X

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)


class CategoricalEncoder(FeatureExtractor):
    """Use the OneHotLabelEncoder only on categorical features.

    NOTE: At the moment of this release, sklearn.preprocessing.data.CategoricalEncoder
    has not been released yet, this is why we write our own version of it.

    >>> df = pd.DataFrame([
    ... {'a': 'a', 'b': 1, 'c': 1},
    ... {'a': 'a', 'b': 2, 'c': 2},
    ... {'a': 'b', 'b': 2, 'c': 1},
    ... ])
    >>> ce = CategoricalEncoder()
    >>> ce.fit_transform(df, categorical_features=['a', 'c'])
       b  a=a  a=b  c=1  c=2
    0  1    1    0    1    0
    1  2    1    0    0    1
    2  2    0    1    1    0
    """

    def __init__(self, max_labels=None, **kwargs):
        self.max_labels = max_labels
        super(CategoricalEncoder, self).__init__(**kwargs)

    def fit(self, X, y=None):
        self.encoders = dict()
        super(CategoricalEncoder, self).fit(X)

    def _fit(self, x):
        encoder = OneHotLabelEncoder(x.name, self.max_labels)
        encoder.fit(x)
        self.encoders[x.name] = encoder

    def _transform(self, x):
        encoder = self.encoders[x.name]
        return encoder.transform(x)


class StringVectorizer(FeatureExtractor):
    """Use the sklearn CountVectorizer only on string features."""

    def __init__(self, copy=True, features=None, **kwargs):
        self.kwargs = kwargs
        super(StringVectorizer, self).__init__(copy, features)

    def fit(self, X, y=None):
        self.vectorizers = dict()
        super(StringVectorizer, self).fit(X)

    def _fit(self, x):
        vectorizer = CountVectorizer(**self.kwargs)
        vectorizer.fit(x.fillna('').astype(str))
        self.vectorizers[x.name] = vectorizer

    def _transform(self, x):
        vectorizer = self.vectorizers[x.name]
        bow = vectorizer.transform(x.fillna('').astype(str))
        bow_columns = ['{}_{}'.format(x.name, f) for f in vectorizer.get_feature_names()]
        return pd.DataFrame(bow.toarray(), columns=bow_columns, index=x.index)


class DatetimeFeaturizer(FeatureExtractor):
    """Extract features from a datetime."""

    def detect_features(self, X):
        features = []
        for column in X.columns:
            if np.issubdtype(X[column].dtype, np.datetime64):
                features.append(column)

        return features

    def _transform(self, x):
        if not np.issubdtype(x.dtype, np.datetime64):
            x = pd.to_datetime(x)

        prefix = x.name + '_'
        features = {
            prefix + 'year': x.dt.year,
            prefix + 'month': x.dt.month,
            prefix + 'day': x.dt.day,
            prefix + 'weekday': x.dt.day,
            prefix + 'hour': x.dt.hour,
        }
        return pd.DataFrame(features)
