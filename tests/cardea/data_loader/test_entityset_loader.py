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
def objects(es_loader):

    encounter_df = pd.DataFrame({"identifier": [10, 11, 12],
                                 "period": [120, 121, 122]})

    period_df = pd.DataFrame({"object_id": [120, 121, 122],
                              "start": ['1/1/2000 20:00', '2/1/2000 5:00', '3/1/2000 22:00'],
                              "end": ['1/2/2000 21:10', '2/2/2000 18:00', '3/3/2000 20:00']})

    encounter = es_loader.create_object(encounter_df, 'Encounter')
    period = es_loader.create_object(period_df, 'Period')

    return [encounter, period]


@pytest.fixture()
def relationships():
    return [('Encounter', 'period', 'Period', 'object_id')]


@pytest.fixture()
def entityset(objects, es_loader):
    es = ft.EntitySet(id="test")

    for object in objects:
        es_loader.create_entity(object, entity_set=es)

    for object in objects:
        es_loader.create_relationships(object, entity_set=es)

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
