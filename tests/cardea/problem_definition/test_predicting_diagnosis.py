#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest
from numpy import nan

from cardea.data_loader import EntitySetLoader
from cardea.problem_definition.predicting_diagnosis import DiagnosisPrediction


@pytest.fixture()
def diagnosis_prediction():
    return DiagnosisPrediction("Z10")


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def cutoff_times():
    temp = pd.DataFrame({"instance_id": [10, 11, 12],
                         "time": ['9/22/2018 00:00', '9/21/2018 00:00', '10/4/2018 00:00'],
                         "label": [True, False, False]})
    temp['time'] = pd.to_datetime(temp['time'])
    return temp


@pytest.fixture()
def objects(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122],
                                 "length": [2, 1, 7],
                                 "diagnosis": [1, 2, 3]})

    encounter_diagnosis_df = pd.DataFrame({"object_id": [1, 2, 3],
                                           "condition": [10, 11, 12]})

    condition_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "code": [1, 2, 3],
                                 "subject": [10, 11, 12]})

    cc_df = pd.DataFrame({"object_id": [1, 2, 3],
                          "coding": [100, 111, 112],
                          "subject": [10, 11, 12]})

    coding_df = pd.DataFrame({"object_id": [100, 111, 112],
                              "code": ["Z10", "C12", "A10"]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/22/2018 00:00', '9/21/2018 00:00', '10/4/2018 00:00'],
                              "end": ['9/22/2018 00:10', '9/21/2018 00:10', '10/4/2018 00:10']})

    duration_df = pd.DataFrame({"object_id": [0, 2, 1, 7]})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    period = es_loader.create_object(period_df, 'Period')
    patient = es_loader.create_object(patient_df, 'Patient')
    duration = es_loader.create_object(duration_df, 'Duration')
    encounter_diagnosis = es_loader.create_object(encounter_diagnosis_df, 'Encounter_Diagnosis')
    condition = es_loader.create_object(condition_df, 'Condition')
    cc = es_loader.create_object(cc_df, 'CodeableConcept')
    coding = es_loader.create_object(coding_df, 'Coding')

    objects = [encounter, period, patient, duration, encounter_diagnosis, condition, cc, coding]
    return objects


@pytest.fixture()
def objects_fail(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/18/2018 00:00', '9/19/2018 00:00', '9/20/2018 11:00'],
                              "end": ['9/20/2018 00:00', '9/20/2018 00:10', '9/27/2018 00:10']})

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
                                 "period": [120, 121, 122],
                                 "length": [2, 1, 7],
                                 "diagnosis": [1, 2, 3]})

    encounter_diagnosis_df = pd.DataFrame({"object_id": [1, 2, 3],
                                           "condition": [10, 11, 12]})

    condition_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "code": [1, 2, 3],
                                 "subject": [10, 11, 12]})

    cc_df = pd.DataFrame({"object_id": [1, 2, 3],
                          "coding": [100, 111, 112],
                          "subject": [10, 11, 12]})

    coding_df = pd.DataFrame({"object_id": [100, 111, 112],
                              "code": ["Z10", "C12", "A10"]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['9/20/2018 21:10', '9/20/2018 18:00', '9/27/2018 20:00'],
                              "end": ['9/22/2018 20:00', '9/21/2018 5:00', '10/4/2018 22:00']
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
    encounter_diagnosis = es_loader.create_object(encounter_diagnosis_df, 'Encounter_Diagnosis')
    condition = es_loader.create_object(condition_df, 'Condition')
    cc = es_loader.create_object(cc_df, 'CodeableConcept')
    coding = es_loader.create_object(coding_df, 'Coding')

    objects = [encounter, period, patient, duration, encounter_diagnosis, condition, cc, coding]
    return objects


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


def test_generate_cutoff_times_success(entityset_success, diagnosis_prediction, cutoff_times):
    _, _, generated_df = diagnosis_prediction.generate_cutoff_times(
        entityset_success)
    generated_df.index = cutoff_times.index  # both should have the same index
    generated_df = generated_df[cutoff_times.columns]  # same columns order
    assert generated_df.equals(cutoff_times)


def test_generate_cutoff_times_missing_generation_label(entityset_success, diagnosis_prediction):
    entityset_success['Period'].delete_variables(['start'])
    with pytest.raises(ValueError):
        diagnosis_prediction.generate_cutoff_times(
            entityset_success)


def test_generate_label_with_missing_label(entityset_success, diagnosis_prediction):
    entityset_success['Encounter'].delete_variables(['diagnosis'])
    with pytest.raises(ValueError):
        diagnosis_prediction.generate_cutoff_times(entityset_success)


def test_generate_label_with_missing_values(
        entityset_fail_missing_generation_value, diagnosis_prediction):
    es_fail = entityset_fail_missing_generation_value
    temp = es_fail['Encounter'].df
    temp['diagnosis'] = [nan, nan, nan]
    es = es_fail.entity_from_dataframe(entity_id='Encounter',
                                       dataframe=temp,
                                       index='identifier')
    with pytest.raises(ValueError):
        diagnosis_prediction.generate_cutoff_times(es)
