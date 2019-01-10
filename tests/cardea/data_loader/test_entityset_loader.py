#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest

from cardea.data_loader import EntitySetLoader


@pytest.fixture()
def es_loader():
    return EntitySetLoader()


@pytest.fixture()
def encounter_df():
    return pd.DataFrame({"identifier": [10, 11, 12],
                         "period": [120, 121, 122]})


@pytest.fixture()
def period_df():
    return pd.DataFrame({"object_id": [120, 121, 122],
                         "start": ['1/1/2000 20:00', '2/1/2000 5:00', '3/1/2000 22:00'],
                         "end": ['1/2/2000 21:10', '2/2/2000 18:00', '3/3/2000 20:00']})


@pytest.fixture()
def objects(es_loader, encounter_df, period_df):

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    period = es_loader.create_object(period_df, 'Period')

    return [encounter, period]


@pytest.fixture()
def entityset(objects, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects)

    fhir_dict = es_loader.get_dataframes(objects)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


def test_create_entity_addition_to_entityset(entityset):
    assert len(entityset.entities) == 2


def test_create_entity_index(entityset):
    ids = {entity.id: entity.index for entity in entityset.entities}
    assert ids['Encounter'] == 'identifier' and ids['Period'] == 'object_id'


def test_create_entity_setting_time_index(entityset):
    assert entityset['Period'].time_index == 'start' and entityset['Encounter'].time_index is None


def test_number_relations_in_create_relationships(entityset):
    assert len(entityset.relationships) == 1


def test_load_df_entityset(es_loader, encounter_df, period_df):
    fhir = {"Encounter": encounter_df, "Period": period_df}
    es = es_loader.load_df_entityset(fhir)
    assert len(es.relationships) == 1 and len(es.entities) == 2
