#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

from cardea.fhir import Patient


@pytest.fixture()
def patient_df():
    return pd.DataFrame({"identifier": [0, 1, 2, 3],
                         "gender": ['female', 'female', 'male', 'female'],
                         "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000', '9/16/2000'],
                         "active": ['True', 'True', 'False', 'False']})


@pytest.fixture()
def patient_object(patient_df):
    object_values = patient_df.to_dict('list')
    return Patient(object_values)


@pytest.fixture()
def patient_object_df(patient_object):
    return patient_object.get_dataframe()


def test_object_number_of_attributes(patient_object_df, patient_df):
    assert len(patient_object_df.columns) == len(patient_df.columns)


def test_object_number_of_tuples(patient_object_df, patient_df):
    assert len(patient_object_df) == len(patient_df)


def test_get_id(patient_object):
    assert patient_object.get_id() == 'identifier'


def test_get_relationships(patient_object):
    relationships = patient_object.get_relationships()
    assert len(relationships) == 12


def test_get_eligible_relationships(patient_object):
    elig_relationships = patient_object.get_eligible_relationships()
    assert len(elig_relationships) == 1


def test_get_id_lookup_error(patient_df):
    df = patient_df[['gender', 'birthDate']]
    object_values = df.to_dict('list')
    object = Patient(object_values)
    with pytest.raises(LookupError):
        object.get_id()


def test_assert_type_enum():
    df = pd.DataFrame({"identifier": [0, 1], "gender": ['female', 'F']})  # F should be female
    object_values = df.to_dict('list')
    with pytest.raises(ValueError):
        Patient(object_values)
