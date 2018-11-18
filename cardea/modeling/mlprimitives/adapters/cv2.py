# -*- coding: utf-8 -*-

import cv2
from mlprimitives.utils import image_transform


def GaussianBlur(X, ksize_width, ksize_height, sigma_x, sigma_y):
    """Apply Gaussian blur to the given data.

    Args:
        X: data to blur
        kernel_size: Gaussian kernel size
        stddev: Gaussian kernel standard deviation (in both X and Y directions)
    """
    return image_transform(
        X,
        cv2.GaussianBlur,
        ksize=(ksize_width, ksize_height),
        sigmaX=sigma_x,
        sigmaY=sigma_y
    )
