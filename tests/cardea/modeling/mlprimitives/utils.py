# -*- coding: utf-8 -*-

import importlib
import logging
import math

import numpy as np

LOGGER = logging.getLogger(__name__)


def import_object(object_name):
    """Import an object from its Fully Qualified Name."""
    package, name = object_name.rsplit('.', 1)
    return getattr(importlib.import_module(package), name)


def image_transform(X, function, reshape_before=False, reshape_after=False,
                    width=None, height=None, **kwargs):
    """Apply a function image by image.

    Args:
        reshape_before: whether 1d array needs to be reshaped to a 2d image
        reshape_after: whether the returned values need to be reshaped back to a 1d array
        width: image width used to rebuild the 2d images. Required if the image is not square.
        height: image height used to rebuild the 2d images. Required if the image is not square.
    """

    if not callable(function):
        function = import_object(function)

    elif not callable(function):
        raise ValueError("function must be a str or a callable")

    flat_image = len(X[0].shape) == 1

    if reshape_before and flat_image:
        if not (width and height):
            side_length = math.sqrt(X.shape[1])
            if side_length.is_integer():
                side_length = int(side_length)
                width = side_length
                height = side_length

            else:
                raise ValueError("Image sizes must be given for non-square images")
    else:
        reshape_before = False

    new_X = []
    for image in X:
        if reshape_before:
            image = image.reshape((width, height))

        features = function(
            image,
            **kwargs
        )

        if reshape_after:
            features = np.reshape(features, X.shape[1])

        new_X.append(features)

    return np.array(new_X)
