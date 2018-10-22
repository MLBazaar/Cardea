#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

from cardea.data_loader import DataLoader, Diamond


@pytest.fixture()
def patient_df():
    return pd.DataFrame({"identifier": [0, 1, 2, 3],
                         "gender": ['female', 'female', 'male', 'female'],
                         "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000', '9/16/2000'],
                         "active": ['True', 'True', 'False', 'False']})


@pytest.fixture()
def reference_df(patient_df):
    return pd.DataFrame({"identifier": patient_df["identifier"].values})


@pytest.fixture()
def encounter_df():
    return pd.DataFrame({"identifier": [10, 11, 12],
                         "period": [120, 121, 122],
                         "subject": [0, 1, 2]})


@pytest.fixture()
def loader():
    return DataLoader()


@pytest.fixture()
def patient(loader, patient_df):
    object = loader.create_object(patient_df, 'Patient')
    return object


@pytest.fixture()
def encounter(loader, encounter_df):
    object = loader.create_object(encounter_df, 'Encounter')
    return object


@pytest.fixture()
def reference(loader, reference_df):
    object = loader.create_object(reference_df, 'Reference')
    return object


@pytest.fixture()
def objects(loader):
    patient_df = pd.DataFrame({"identifier": [0, 1, 2, 3],
                               "gender": ['female', 'female', 'male', 'female'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000', '9/16/2000'],
                               "active": ['True', 'True', 'False', 'False']})

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "period": [120, 121, 122],
                                 "subject": [1, 2, 3],
                                 "diagnosis": [91, 92, 91]})

    encounter_diagnosis_df = pd.DataFrame({"object_id": [91, 92],
                                           "condition": [1000, 3000]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['1/1/2000 20:00', '2/1/2000 5:00', '3/1/2000 22:00'],
                              "end": ['1/2/2000 21:10', '2/2/2000 18:00', '3/3/2000 20:00']})

    condition_df = pd.DataFrame({"identifier": [1000, 2000, 3000],
                                 "subject": [2, 2, 1]})

    reference_df = pd.DataFrame({"identifier": [0, 1, 2, 3, 10, 11, 12, 1000, 2000, 3000]})
    identifier_df = pd.DataFrame({"object_id": [0, 1, 2, 3, 10, 11, 12, 1000, 2000, 3000]})

    patient = loader.create_object(patient_df, 'Patient')
    encounter = loader.create_object(encounter_df, 'Encounter')
    encounter_diagnosis = loader.create_object(encounter_diagnosis_df, 'Encounter_Diagnosis')
    period = loader.create_object(period_df, 'Period')
    condition = loader.create_object(condition_df, 'Condition')
    reference = loader.create_object(reference_df, 'Reference')
    identifier = loader.create_object(identifier_df, 'Identifier')

    return [patient, encounter, encounter_diagnosis, period, condition, reference, identifier]


@pytest.fixture()
def diamond(objects):
    return Diamond(objects)


@pytest.fixture()
def edge():
    return ('Condition', 'Patient')


@pytest.fixture()
def diamond_witout_ref(diamond):
    diamond.resolve_reference()
    return diamond


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


def test_get_object_ids(loader, patient):
    id = loader.get_object_ids([patient])
    assert len(id) == 1 and id['Patient'] == "identifier"


def test_get_relationships_single(loader, patient):
    relationships = loader.get_relationships([patient], ['Patient'])
    assert len(relationships) == 0


def test_get_relationships_multiple(loader, patient, encounter, reference):
    relationships = loader.get_relationships([patient, encounter, reference],
                                             ['Patient', 'Encounter', 'Reference'])
    assert len(relationships) == 1


def test_get_dataframes(loader, patient):
    dfs = loader.get_dataframes([patient])
    assert len(dfs) == 1


def test_get_dataframes_names(loader, patient, encounter):
    dfs = loader.get_dataframes([patient, encounter])
    names = list(dfs.keys())
    assert len(names) == len(['Patient', 'Encounter']) and \
        sorted(names) == sorted(['Patient', 'Encounter'])


def test_merge_cost(diamond):
    cost = diamond.merge_cost()
    assert sum(cost) == sum([26, 22, 22, 16, 21, 14, 16, 16, 20])


def test_resolve_reference(diamond):
    diamond.resolve_reference()
    relationships = diamond.get_fhir_relationships()
    assert len(relationships) == 5


def test_resolve_reference_lookuperror(objects):
    objects = objects[:-1]
    diamond = Diamond(objects)
    with pytest.raises(LookupError):
        diamond.resolve_reference()


def test_merge_entities(diamond_witout_ref, edge):
    fhir = diamond_witout_ref.get_fhir_dataframes()
    previous = len(fhir['Condition'].columns)
    diamond_witout_ref.merge(edge)
    fhir = diamond_witout_ref.get_fhir_dataframes()
    after = len(fhir['Condition'].columns)
    assert previous + 3 == after


def test_merge_relationships_without_drop(diamond_witout_ref, edge):
    previous = len(diamond_witout_ref.get_fhir_relationships())
    diamond_witout_ref.merge(edge, False)
    after = len(diamond_witout_ref.get_fhir_relationships())
    assert previous == after


def test_merge_relationships_with_drop(diamond_witout_ref, edge):
    previous = len(diamond_witout_ref.get_fhir_relationships())
    diamond_witout_ref.merge(edge, True)
    after = len(diamond_witout_ref.get_fhir_relationships())
    assert previous == after + 1


def test_resolve_diamond(diamond):
    diamond.resolve_diamond()
    relationships = diamond.get_fhir_relationships()
    fhir = diamond.get_fhir_dataframes()
    assert len(relationships) == 4 and len(fhir) == 7
