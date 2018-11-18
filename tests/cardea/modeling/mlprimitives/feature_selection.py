"""
Feature selection based on the scikit-learn
ExtraTreesClassifier and SelectFromModel solution.

>>> from sklearn.ensemble import ExtraTreesClassifier
>>> from sklearn.datasets import load_iris
>>> from sklearn.feature_selection import SelectFromModel
>>> iris = load_iris()
>>> X, y = iris.data, iris.target
>>> X.shape
(150, 4)
>>> clf = ExtraTreesClassifier()
>>> clf = clf.fit(X, y)
>>> clf.feature_importances_
array([ 0.04...,  0.05...,  0.4...,  0.4...])
>>> model = SelectFromModel(clf, prefit=True)
>>> X_new = model.transform(X)
>>> X_new.shape
(150, 2)
"""

import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier, ExtraTreesRegressor
from sklearn.feature_selection import SelectFromModel


class EstimatorFeatureSelector(object):
    """Feature Selector based on sklearn.feature_selection.SelectFromModel.

    Attributes:
        ESTIMATOR (class): Estimator class to use. To be defined in subclasses.
        selector (SelectFromModel): sklearn.ensemble.SelectFromModel that will
                                    perform the actual feature selection.

    Example:
        This example below shows simple usage case using an ExtraTreesClassifier
        as the estimator, and shows the output when passing both a pandas.DataFrame
        and a numpy.ndarray.

        >>> import pandas as pd
        >>> df = pd.DataFrame([
            ... {'a': 1, 'b': 1, 'c': 1},
            ... {'a': 1, 'b': 2, 'c': 1},
            ... {'a': 2, 'b': 1, 'c': 2},
            ... {'a': 2, 'b': 2, 'c': 2}
            ... ])
        >>> X = df[['a', 'b']]
        >>> y = df.c
        >>> from mlblocks.primitives.custom.preprocessors.feature_selection \
        ...         import EstimatorFeatureSelector
        >>> from sklearn.ensemble import ExtraTreesClassifier
        >>> efs = EstimatorFeatureSelector(ExtraTreesClassifier)
        >>> efs.fit(X, y)
        >>> efs.transform(X)
           a
           0  1
           1  1
           2  2
           3  2
        >>> efs.transform(X.values)
        array([[1],
               [1],
               [2],
               [2]])
    """

    ESTIMATOR = None

    def __init__(self, estimator_class=None, bypass=False, threshold=None,
                 norm_order=1, *args, **kwargs):
        self.bypass = bypass
        if not bypass:
            estimator = (self.ESTIMATOR or estimator_class)(*args, **kwargs)
            self.selector = SelectFromModel(estimator, threshold, False, norm_order)

    def fit(self, X, y):
        if not self.bypass:
            self.selector.fit(X, y)

    def _get_df(self, X, new_X):
        columns_idx = self.selector.get_support()
        columns = X.columns[columns_idx]
        return pd.DataFrame(new_X, index=X.index, columns=columns)

    def transform(self, X):
        if self.bypass:
            return X

        new_X = self.selector.transform(X)
        if isinstance(X, pd.DataFrame):
            new_X = self._get_df(X, new_X)

        return new_X

    def fit_transform(self, X, y):
        self.fit(X, y)
        return self.transform(X)


class ExtraTreesClassifierFeatureSelector(EstimatorFeatureSelector):
    """EstimatorFeatureSelector based on ExtraTreesClassifier."""

    ESTIMATOR = ExtraTreesClassifier


class ExtraTreesRegressorFeatureSelector(EstimatorFeatureSelector):
    """EstimatorFeatureSelector based on ExtraTreesRegressor."""

    ESTIMATOR = ExtraTreesRegressor
