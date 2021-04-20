#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest.mock import Mock

import featuretools as ft

from cardea.data_labeling import DataLabeler


class TestDataLabeler:

    @classmethod
    def setup_class(cls):
        cls.function = lambda x: x
        cls.es = Mock(autospec=ft.EntitySet)
        cls.subset = None
        cls.verbose = False

    def test_data_labeler(self):
        def function(x):
            return x

        DataLabeler(function)
