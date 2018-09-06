#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

from cardea.data_loader import DataLoader

@pytest.fixture()
def patient_df():
    return pd.DataFrame({"identifier": [0, 1, 2, 3, 4],
                         "gender": ['female', 'female', 'male', 'female', 'female'],
                         "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000', '9/16/2000', '4/12/2000'],
                         "active": ['True', 'True', 'False', 'False', 'False']})

@pytest.fixture()
def loader():
    return DataLoader()

@pytest.fixture()
def patient_object(patient_df, loader):
    return loader.create_object(patient_df, 'Patient')

@pytest.fixture()
def patient_object_df(patient_object):
    return patient_object.get_dataframe()

def test_object_number_of_attributes(patient_object_df, patient_df):
    assert len(patient_object_df.columns) == len(patient_df.columns)

def test_object_number_of_tuples(patient_object_df, patient_df):
    assert len(patient_object_df) == len(patient_df)

def test_get_relationships(patient_object):
    relationships = patient_object.get_relationships()
    assert len(relationships) == 12

def test_assert_object_identifier(loader):
    df = pd.DataFrame({"gender": ['female', 'male']})
    with pytest.raises(Exception):
        loader.create_object(df, 'Patient')

def test_assert_type_enum(loader):
    df = pd.DataFrame({"identifier": [0, 1], "gender": ['female', 'F']}) # F should be female
    with pytest.raises(Exception):
        loader.create_object(df, 'Patient')
