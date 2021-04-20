#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import FunctionType
from unittest.mock import Mock, patch

import featuretools as ft
import pandas as pd

from cardea.data_labeling import mortality_prediction


@patch('cardea.data_labeling.utils.denormalize')
def test_mortality_prediction_mimic(denormalize_mock):
    es = Mock(autospec=ft.EntitySet, id='mimic')
    df = Mock(autospec=pd.DataFrame)
    denormalize_mock.return_value = df

    returned = mortality_prediction(es)

    assert isinstance(returned, tuple)
    assert len(returned) == 3

    function, dataframe, meta = returned

    assert isinstance(function, FunctionType)
    assert isinstance(meta, dict)
