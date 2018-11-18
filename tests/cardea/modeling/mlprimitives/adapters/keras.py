# -*- coding: utf-8 -*-

import logging
import tempfile

import numpy as np

import keras
from mlprimitives.utils import import_object

LOGGER = logging.getLogger(__name__)


class Sequential(object):
    """A Wrapper around Sequential Keras models with a simpler interface."""

    def __getstate__(self):
        state = self.__dict__.copy()

        with tempfile.NamedTemporaryFile(suffix='.hdf5', delete=True) as fd:
            keras.models.save_model(state.pop('model'), fd.name, overwrite=True)
            state['model_str'] = fd.read()

        return state

    def __setstate__(self, state):
        with tempfile.NamedTemporaryFile(suffix='.hdf5', delete=True) as fd:
            fd.write(state.pop('model_str'))
            fd.flush()

            state['model'] = keras.models.load_model(fd.name)

        self.__dict__ = state

    def _build_model(self, **kwargs):
        model = keras.models.Sequential()

        hyperparameters = self.hyperparameters.copy()
        hyperparameters.update(kwargs)

        for layer in self.layers:
            layer_kwargs = layer['parameters'].copy()
            for key, value in layer_kwargs.items():
                if isinstance(value, str):
                    layer_kwargs[key] = hyperparameters.get(value, value)

            model.add(layer['class'](**layer_kwargs))

        model.compile(loss=self.loss, optimizer=self.optimizer(), metrics=self.metrics)

        return model

    def __init__(self, layers, loss, optimizer, classification,
                 metrics=None, epochs=10, **hyperparameters):

        self.layers = list()
        for layer in layers:
            layer = layer.copy()
            layer['class'] = import_object(layer['class'])
            self.layers.append(layer)

        self.optimizer = import_object(optimizer)
        self.loss = import_object(loss)
        self.metrics = metrics

        self.epochs = epochs
        self.classification = classification
        self.hyperparameters = hyperparameters

    def fit(self, X, y, **kwargs):
        self.model = self._build_model(**kwargs)

        if self.classification:
            y = keras.utils.to_categorical(y)

        self.model.fit(X, y, epochs=self.epochs)

    def predict(self, X):
        y = self.model.predict(X)

        if self.classification:
            y = np.argmax(y, axis=1)

        return y
