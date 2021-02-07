#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest
from numpy import nan

from cardea.data_loader import EntitySetLoader
from cardea.problem_definition import ProlongedLengthOfStay


@pytest.fixture()
def length_of_stay():
    return ProlongedLengthOfStay()


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def cutoff_times():
    temp = pd.DataFrame({"instance_id": [10, 11, 12],
                         "time": ['9/19/2018 00:00', '9/19/2018 00:00', '9/20/2018 11:23'],
                         "label": [0, 0, 1]
                         })
    temp['time'] = pd.to_datetime(temp['time'])
    return temp


@pytest.fixture()
def objects(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122],
                                 "length": [2, 1, 7]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/18/2018 00:00', '9/19/2018 00:00', '9/20/2018 11:23'],
                              "end": ['9/20/2018 00:12', '9/20/2018 00:20', '9/27/2018 11:23']})

    duration_df = pd.DataFrame({"object_id": [2, 1, 7]})

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
                              "start": ['9/18/2018 00:00', '9/19/2018 00:00', '9/20/2018 11:23'],
                              "end": ['9/20/2018 00:12', '9/20/2018 00:20', '9/27/2018 11:23']})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    period = es_loader.create_object(period_df, 'Period')
    patient = es_loader.create_object(patient_df, 'Patient')

    return [encounter, period, patient]


@pytest.fixture()
def objects_missing_generation_label(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/18/2018', '9/19/2018', '9/20/2018']})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    patient = es_loader.create_object(patient_df, 'Patient')
    period = es_loader.create_object(period_df, 'Period')

    return [encounter, patient, period]


@pytest.fixture()
def objects_missing_generation_table(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2]})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    patient = es_loader.create_object(patient_df, 'Patient')

    return [encounter, patient]


@pytest.fixture()
def objects_missing_generation_value(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/18/2018 00:00', '9/19/2018 00:00', '9/20/2018 11:23'],
                              "end": ['9/20/2018 00:12', '9/20/2018 00:20', nan]})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    patient = es_loader.create_object(patient_df, 'Patient')
    period = es_loader.create_object(period_df, 'Period')

    return [encounter, patient, period]


@pytest.fixture()
def objects_missing_cutoff_label(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122],
                                 "length": [2, 1, 7]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/18/2018 00:00', '9/19/2018 00:00', '9/20/2018 11:23'],
                              "end": ['9/20/2018 00:12', '9/20/2018 00:20', '9/27/2018 11:23']})

    duration_df = pd.DataFrame({"object_id": [2, 1, 7]})

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


@pytest.fixture()
def entityset_fail_missing_generation_label(objects_missing_generation_label, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects_missing_generation_label)

    fhir_dict = es_loader.get_dataframes(objects_missing_generation_label)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(
        objects_missing_generation_label, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)
    return es


@pytest.fixture()
def entityset_error_missing_cutoff_label(objects_missing_cutoff_label, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects_missing_cutoff_label)

    fhir_dict = es_loader.get_dataframes(objects_missing_cutoff_label)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(
        objects_missing_cutoff_label, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)
    return es


def test_generate_cutoff_times_success(entityset_success, length_of_stay, cutoff_times):
    _, _, generated_df = length_of_stay.generate_cutoff_times(
        entityset_success)
    generated_df.index = cutoff_times.index  # both should have the same index
    generated_df = generated_df[cutoff_times.columns]  # same columns order
    assert generated_df.equals(cutoff_times)


def test_generate_cutoff_times_missing_target_label(entityset_fail, length_of_stay, cutoff_times):
    _, _, generated_df = length_of_stay.generate_cutoff_times(
        entityset_fail)
    generated_df.index = cutoff_times.index  # both should have the same index
    generated_df = generated_df[cutoff_times.columns]  # same columns order
    assert generated_df.equals(cutoff_times)


def test_generate_cutoff_times_missing_generation_label(
        entityset_fail_missing_generation_label, length_of_stay):
    with pytest.raises(ValueError):
        length_of_stay.generate_cutoff_times(
            entityset_fail_missing_generation_label)


def test_generate_cutoff_times_with_missing_cutoff_label(
        entityset_error_missing_cutoff_label, length_of_stay):
    entityset_error_missing_cutoff_label['Period'].delete_variables(['start'])
    with pytest.raises(ValueError):
        length_of_stay.generate_cutoff_times(
            entityset_error_missing_cutoff_label)


def test_generate_label_with_missing_values(
        entityset_fail_missing_generation_value, length_of_stay):
    with pytest.raises(ValueError):
        length_of_stay.generate_cutoff_times(entityset_fail_missing_generation_value)


def test_generate_cutoff_times_with_threshold(entityset_success):
    los = ProlongedLengthOfStay(t=2)
    values_should_be = [1, 0, 1]
    es, _, generated_df = los.generate_cutoff_times(
        entityset_success)
    generated_labels = list(generated_df['label'])
    assert values_should_be == generated_labels
