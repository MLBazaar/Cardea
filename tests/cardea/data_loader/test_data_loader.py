#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

from cardea.data_loader import DataLoader


@pytest.fixture()
def patient_df():
    return pd.DataFrame({"identifier": [0, 1, 2, 3],
                         "gender": ['female', 'female', 'male', 'female'],
                         "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000', '9/16/2000'],
                         "active": ['True', 'True', 'False', 'False']})


@pytest.fixture()
def loader():
    return DataLoader()


def test_data_loader_create_object(loader, patient_df):
    object = loader.create_object(patient_df, 'Patient')
    object_df = object.get_dataframe()
    assert len(object_df) == len(patient_df)


def test_fhir_class_exist(loader, patient_df):
    with pytest.raises(LookupError):
        loader.create_object(patient_df, 'Inpatient')


def test_assert_object_identifier(loader, patient_df):
    df = patient_df[['gender']]
    with pytest.raises(LookupError):
        loader.create_object(df, 'Patient')
