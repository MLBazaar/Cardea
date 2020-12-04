# -*- coding: utf-8 -*-


__author__ = """MIT Data To AI Lab"""
__email__ = 'dailabmit@gmail.com'
__version__ = '0.1.1.dev0'

import logging
import os

from cardea.cardea import Cardea

logging.getLogger('cardea').addHandler(logging.NullHandler())

_BASE_PATH = os.path.abspath(os.path.dirname(__file__))
MLBLOCKS_PRIMITIVES = os.path.join(_BASE_PATH, 'primitives', 'jsons')
MLBLOCKS_PIPELINES = os.path.join(_BASE_PATH, 'pipelines')

__all__ = (
    "Cardea"
)
