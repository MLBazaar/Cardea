# -*- coding: utf-8 -*-


__author__ = """MIT Data To AI Lab"""
__email__ = 'dailabmit@gmail.com'
__version__ = '0.1.1.dev0'

import logging

from cardea.cardea import Cardea

logging.getLogger('cardea').addHandler(logging.NullHandler())

__all__ = (
    "Cardea"
)
