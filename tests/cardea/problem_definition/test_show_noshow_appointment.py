#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest
from numpy import nan

from cardea.data_loader import EntitySetLoader
from cardea.problem_definition import MissedAppointment


@pytest.fixture()
def missed_appointment():
    return MissedAppointment()


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def cutoff_times():
    return pd.DataFrame(
        {"instance_id": [10, 11, 12],
         "time": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018],
         "label": ['noshow', 'noshow', 'fulfilled']
         })


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
def es_success(objects, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects)

    fhir_dict = es_loader.get_dataframes(objects)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


@pytest.fixture()
def object_error_missing_label(es_loader):

    appointment_df = pd.DataFrame({"identifier": [10, 11, 12],
                                   "start": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018],
                                   "participant": [120, 121, 122],
                                   "created": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018]})

    appointment = es_loader.create_object(appointment_df, 'Appointment')

    return appointment


@pytest.fixture()
def objects_error_missing_cutoff_label(es_loader):

    appointment_df = pd.DataFrame({"identifier": [10, 11, 12],
                                   "start": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018],
                                   "status": ['noshow', 'noshow', 'fulfilled'],
                                   "participant": [120, 121, 122]})

    appointment = es_loader.create_object(appointment_df, 'Appointment')
    return appointment


@pytest.fixture()
def entityset_error_missing_label(objects, object_error_missing_label, es_loader):
    es = ft.EntitySet(id="test")

    objects.extend([object_error_missing_label])

    identifiers = es_loader.get_object_ids(objects)

    fhir_dict = es_loader.get_dataframes(objects)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


@pytest.fixture()
def entityset_error_missing_cutoff_label(objects, objects_error_missing_cutoff_label, es_loader):
    es = ft.EntitySet(id="test")

    for object in objects:
        es_loader.create_entity(object, entity_set=es)

    for object in objects:
        es_loader.create_relationships(object, entity_set=es)

    es_loader.create_entity(objects_error_missing_cutoff_label, entity_set=es)
    es_loader.create_relationships(objects_error_missing_cutoff_label, entity_set=es)
    return es


def test_generate_cutoff_times_success(
        es_success, missed_appointment, cutoff_times):
    _, _, generated_df = missed_appointment.generate_cutoff_times(es_success)
    generated_df.index = cutoff_times.index  # both should have the same index
    generated_df = generated_df[cutoff_times.columns]  # same columns order
    assert generated_df.equals(cutoff_times)


def test_generate_cutoff_times_error(
        entityset_error_missing_label, missed_appointment):
    with pytest.raises(ValueError):
        missed_appointment.generate_cutoff_times(
            entityset_error_missing_label)


def test_generate_cutoff_times_error_value(es_success, missed_appointment):
    es_success['Appointment'].df.loc[len(es_success['Appointment'].df)] = [
        nan, nan, nan, nan, nan]
    with pytest.raises(ValueError):
        missed_appointment.generate_cutoff_times(
            es_success)


def test_generate_cutoff_times_missing_cutoff_time(
        es_success, missed_appointment):
    es_success['Appointment'].delete_variables(['created'])
    with pytest.raises(ValueError):
        missed_appointment.generate_cutoff_times(
            es_success)
