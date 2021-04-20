#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import FunctionType
from unittest.mock import Mock, patch

import featuretools as ft
import pandas as pd

from cardea.data_labeling import readmission


@patch('cardea.data_labeling.utils.denormalize')
def test_readmission_fhir(denormalize_mock):
    es = Mock(autospec=ft.EntitySet, id="fhir")

    df = pd.DataFrame({
        'col 1': range(5),
        'start': range(5),
        'end': range(5)
    })
    denormalize_mock.return_value = df

    returned = readmission(es)

    assert isinstance(returned, tuple)
    assert len(returned) == 3

    function, dataframe, meta = returned

    assert isinstance(function, FunctionType)
    assert isinstance(dataframe, pd.DataFrame)
    assert isinstance(meta, dict)


@patch('cardea.data_labeling.utils.denormalize')
def test_readmission_mimic(denormalize_mock):
    es = Mock(autospec=ft.EntitySet, id="mimic")

    df = pd.DataFrame({
        'col 1': range(5),
        'admittime': range(5),
        'dischtime': range(5)
    })
    denormalize_mock.return_value = df

    returned = readmission(es)

    assert isinstance(returned, tuple)
    assert len(returned) == 3

    function, dataframe, meta = returned

    assert isinstance(function, FunctionType)
    assert isinstance(dataframe, pd.DataFrame)
    assert isinstance(meta, dict)
