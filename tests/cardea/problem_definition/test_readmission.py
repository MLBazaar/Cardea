#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest
from numpy import nan

from cardea.data_loader import EntitySetLoader
from cardea.problem_definition import Readmission


@pytest.fixture()
def readmission():
    return Readmission()


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def cutoff_times():
    temp = pd.DataFrame({"instance_id": [10, 11, 12, 13, 14, 15],
                         "time": ['9/22/2018', '9/21/2018', '10/4/2018',
                                  '9/28/2018', '10/30/2018', '11/18/2018'],
                         "label": [False, False, False, True, False, True]
                         })
    temp['time'] = pd.to_datetime(temp['time'])
    return temp


@pytest.fixture()
def objects(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12, 13, 14, 15],
                                 "subject": [0, 1, 2, 0, 0, 0],
                                 "period": [120, 121, 122, 125, 123, 124],
                                 "length": [2, 1, 7, 0, 0, 0]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122, 125, 123, 124],
                              "start": ['9/20/2018', '9/20/2018', '9/27/2018',
                                        '9/28/2018', '10/30/2018', '11/18/2018'],
                              "end": ['9/22/2018', '9/21/2018', '10/4/2018',
                                      '9/28/2018', '10/30/2018', '11/18/2018']
                              })

    duration_df = pd.DataFrame({"object_id": [0, 2, 1, 7]})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    period = es_loader.create_object(period_df, 'Period')
    patient = es_loader.create_object(patient_df, 'Patient')
    duration = es_loader.create_object(duration_df, 'Duration')

    return [encounter, period, patient, duration]


@pytest.fixture()
def objects_fail(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/18/2018', '9/19/2018', '9/20/2018'],
                              "end": ['9/20/2018', '9/20/2018', '9/27/2018']})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    period = es_loader.create_object(period_df, 'Period')
    patient = es_loader.create_object(patient_df, 'Patient')

    return [encounter, period, patient]


@pytest.fixture()
def objects_missing_generation_table(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12, 13, 14, 15],
                                 "subject": [0, 1, 2, 0, 0, 0],
                                 "length": [2, 1, 7, 0, 0, 0]})

    duration_df = pd.DataFrame({"object_id": [0, 2, 1, 7]})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    patient = es_loader.create_object(patient_df, 'Patient')
    duration = es_loader.create_object(duration_df, 'Duration')

    return [encounter, patient, duration]


@pytest.fixture()
def objects_missing_generation_value(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/18/2018', '9/19/2018', '9/20/2018'],
                              "end": ['9/18/2018', '9/19/2018', nan]})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    patient = es_loader.create_object(patient_df, 'Patient')
    period = es_loader.create_object(period_df, 'Period')

    return [encounter, patient, period]


@pytest.fixture()
def relationships():
    return[('Encounter', 'period', 'Period', 'object_id'),
           ('Encounter', 'subject', 'Patient', 'identifier'),
           ('Encounter', 'length', 'Duration', 'object_id')]


@pytest.fixture()
def entityset_success(objects, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects)

    fhir_dict = es_loader.get_dataframes(objects)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


@pytest.fixture()
def entityset_fail_missing_generation_value(objects_missing_generation_value, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects_missing_generation_value)

    fhir_dict = es_loader.get_dataframes(objects_missing_generation_value)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(
        objects_missing_generation_value, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


@pytest.fixture()
def entityset_fail_missing_generation_table(objects_missing_generation_table, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects_missing_generation_table)

    fhir_dict = es_loader.get_dataframes(objects_missing_generation_table)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(
        objects_missing_generation_table, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)
    return es


@pytest.fixture()
def entityset_fail(objects_fail, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects_fail)

    fhir_dict = es_loader.get_dataframes(objects_fail)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects_fail, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)
    return es


def test_generate_cutoff_times_success(entityset_success, readmission, cutoff_times):
    _, _, generated_df = readmission.generate_cutoff_times(
        entityset_success)
    generated_df.index = cutoff_times.index  # both should have the same index
    generated_df = generated_df[cutoff_times.columns]  # same columns order
    assert generated_df.equals(cutoff_times)


def test_generate_labels_success(entityset_success, readmission, cutoff_times):
    es, _, generated_df = readmission.generate_cutoff_times(
        entityset_success)
    generated_df.index = cutoff_times.index  # both should have the same index

    labels = list(generated_df['label'])

    assert labels == [False, False, False, True, False, True]


def test_generate_labels_success_threshold(entityset_success, cutoff_times):

    es, _, generated_df = Readmission(6).generate_cutoff_times(
        entityset_success)
    generated_df.index = cutoff_times.index  # both should have the same index

    labels = list(generated_df['label'])
    assert labels == [False, False, False, True, False, False]


def test_generate_cutoff_times_missing_generation_label(entityset_success, readmission):
    entityset_success['Period'].delete_variables(['end'])
    with pytest.raises(ValueError):
        readmission.generate_cutoff_times(
            entityset_success)


def test_generate_label_with_missing_values(entityset_fail_missing_generation_value, readmission):
    with pytest.raises(ValueError):
        readmission.generate_cutoff_times(entityset_fail_missing_generation_value)
