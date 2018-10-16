#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest
from numpy import nan

from cardea.data_loader import EntitySetLoader
from cardea.problem_definition import MissedAppointmentProblemDefinition, ProblemDefinition


@pytest.fixture()
def missed_appointment_droblem_definition():
    return MissedAppointmentProblemDefinition()


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def problem_definition():
    return ProblemDefinition()


@pytest.fixture()
def cutoff_times():
    return pd.DataFrame({"cutoff_time": [7 / 22 / 2018, 8 / 21 / 2018, 9 / 16 / 2018]})


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
def entityset_success(objects, es_loader):
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
def entityset_error_missing_label(objects, object_error_missing_label, es_loader):
    es = ft.EntitySet(id="test")

    objects.extend([object_error_missing_label])

    identifiers = es_loader.get_object_ids(objects)

    fhir_dict = es_loader.get_dataframes(objects)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


def test_generate_cutoff_times_success(entityset_success):
    _, _, _, generated_df = MissedAppointmentProblemDefinition.generate_cutoff_times(
        MissedAppointmentProblemDefinition, entityset_success)
    generated_df.index = cutoff_times().index  # both should have the same index
    assert generated_df.equals(cutoff_times())


def test_generate_cutoff_times_error(entityset_error_missing_label):
    with pytest.raises(ValueError):
        MissedAppointmentProblemDefinition.generate_cutoff_times(
            MissedAppointmentProblemDefinition, entityset_error_missing_label)


def test_generate_cutoff_times_error_value(entityset_success):
    entityset_success['Appointment'].df.loc[len(entityset_success['Appointment'].df)] = [
        nan, nan, nan, nan, nan]
    with pytest.raises(ValueError):
        MissedAppointmentProblemDefinition.generate_cutoff_times(
            MissedAppointmentProblemDefinition, entityset_success)


def test_generate_cutoff_times_missing_cutoff_time(entityset_success):
    entityset_success['Appointment'].delete_variable('created')
    with pytest.raises(ValueError):
        MissedAppointmentProblemDefinition.generate_cutoff_times(
            MissedAppointmentProblemDefinition, entityset_success)
