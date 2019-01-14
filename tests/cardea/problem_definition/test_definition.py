#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest

from cardea.data_loader import EntitySetLoader
from cardea.problem_definition import ProblemDefinition


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def problem_definition():
    return ProblemDefinition()


@pytest.fixture()
def objects(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "subject": [0, 1, 2],
                                 "period": [120, 121, 122]},)

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['1/1/2000 20:00', '2/1/2000 5:00', '3/1/2000 22:00'],
                              "end": ['1/2/2000 21:10', '2/2/2000 18:00', '3/3/2000 20:00']})

    patient_df = pd.DataFrame({"identifier": [0, 1, 2],
                               "gender": ['female', 'female', 'male'],
                               "birthDate": ['10/21/2000', '7/2/2000', '1/10/2000'],
                               "active": ['True', 'True', 'nan']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    period = es_loader.create_object(period_df, 'Period')
    patient = es_loader.create_object(patient_df, 'Patient')
    return [encounter, period, patient]


@pytest.fixture()
def entityset(objects, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects)

    fhir_dict = es_loader.get_dataframes(objects)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


def test_check_target_label_true(entityset, problem_definition):
    assert problem_definition.check_target_label(entityset, 'Patient', 'gender') is True


def test_check_target_label_false(entityset, problem_definition):

    assert problem_definition.check_target_label(
        entityset, 'Encounter', 'class') is False


def test_check_target_label_values_true(entityset, problem_definition):

    assert problem_definition.check_for_missing_values_in_target_label(
        entityset, 'Patient', 'active') is True


def test_check_target_label_values_false(entityset, problem_definition):
    assert problem_definition.check_for_missing_values_in_target_label(
        entityset, 'Patient', 'gender') is False


def test_check_target_label_values_error(entityset, problem_definition):
    assert problem_definition.check_for_missing_values_in_target_label(
        entityset, 'Encounter', 'class') is False
