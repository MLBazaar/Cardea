#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest
from numpy import nan

from cardea.data_loader import EntitySetLoader
from cardea.problem_definition import PredictingMissedAppointmet, ProblemDefinition


@pytest.fixture()
def predicting_missed_appointmet():
    return PredictingMissedAppointmet()


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def problem_definition():
    return ProblemDefinition()


@pytest.fixture()
def cutoff_times():
    return pd.DataFrame({"identifier": [10, 11, 12],
                         "cutoff_time": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018],
                         "label": ['noshow', 'noshow', 'fulfilled']},
                        index=[10, 11, 12])


@pytest.fixture()
def objects(es_loader):

    appointment_df = pd.DataFrame({"identifier": [10, 11, 12],
                                   "status": ['noshow', 'noshow', 'fulfilled'],
                                   "start": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018],
                                   "participant": [120, 121, 122],
                                   "created": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018]})

    participant_df = pd.DataFrame({"object_id": [120, 121, 122],
                                   "actor": [0, 1, 2]})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    appointment = es_loader.create_object(appointment_df, 'Appointment')
    participant = es_loader.create_object(participant_df, 'Appointment_Participant')
    patient = es_loader.create_object(patient_df, 'Patient')

    return [appointment, participant, patient]


@pytest.fixture()
def relationships():
    return [('Appointment', 'participant', 'Appointment_Participant', 'object_id'),
            ('Patient', 'identifier', 'Appointment_Participant', 'actor')]


@pytest.fixture()
def entityset_success(objects, es_loader):
    es = ft.EntitySet(id="test")

    for object in objects:
        es_loader.create_entity(object, entity_set=es)

    for object in objects:
        es_loader.create_relationships(object, entity_set=es)

    return es


@pytest.fixture()
def objects_error_missing_label(es_loader):

    appointment_df = pd.DataFrame({"identifier": [10, 11, 12],
                                   "start": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018],
                                   "participant": [120, 121, 122],
                                   "created": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018]})

    appointment = es_loader.create_object(appointment_df, 'Appointment')
    return appointment


@pytest.fixture()
def entityset_error_missing_label(objects, objects_error_missing_label, es_loader):
    es = ft.EntitySet(id="test")

    for object in objects:
        es_loader.create_entity(object, entity_set=es)

    for object in objects:
        es_loader.create_relationships(object, entity_set=es)

    es_loader.create_entity(objects_error_missing_label, entity_set=es)
    es_loader.create_relationships(objects_error_missing_label, entity_set=es)
    return es


def test_generate_cutoff_times_success(entityset_success):
    assert PredictingMissedAppointmet.generate_cutoff_times(
        PredictingMissedAppointmet, entityset_success).equals(cutoff_times())


def test_generate_cutoff_times_error(entityset_error_missing_label):
    with pytest.raises(ValueError):
        PredictingMissedAppointmet.generate_cutoff_times(
            PredictingMissedAppointmet, entityset_error_missing_label)


def test_generate_cutoff_times_error_value(entityset_success):
    entityset_success['Appointment'].df.loc[len(entityset_success['Appointment'].df)] = [
        nan, nan, nan, nan, nan]
    print(entityset_success['Appointment'])
    with pytest.raises(ValueError):
        PredictingMissedAppointmet.generate_cutoff_times(
            PredictingMissedAppointmet, entityset_success)


def test_generate_cutoff_times_missing_cutoff_time(entityset_success):
    entityset_success['Appointment'].delete_variable('created')
    with pytest.raises(ValueError):
        PredictingMissedAppointmet.generate_cutoff_times(
            PredictingMissedAppointmet, entityset_success)
