#!/usr/bin/env python
# -*- coding: utf-8 -*-

import featuretools as ft
import pandas as pd
import pytest

from cardea.data_loader import EntitySetLoader
from cardea.featurization import Featurization


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
def entityset(objects, es_loader):
    es = ft.EntitySet(id="test")

    identifiers = es_loader.get_object_ids(objects)

    fhir_dict = es_loader.get_dataframes(objects)
    es_loader.create_entity(fhir_dict, identifiers, entity_set=es)

    relationships = es_loader.get_relationships(objects, list(fhir_dict.keys()))
    es_loader.create_relationships(relationships, entity_set=es)

    return es


@pytest.fixture()
def cutoff():
    cutoff = pd.DataFrame({"instance_id": [10, 11, 12],
                           "time": ['1/1/2000 20:00', '2/1/2000 5:00', '3/1/2000 22:00']})

    cutoff['time'] = pd.to_datetime(cutoff['time'])
    return cutoff


@pytest.fixture()
def featurization():
    return Featurization()


def test_generate_feature_matrix(featurization, entityset, cutoff):
    fm_encoded, features_encoded = featurization.generate_feature_matrix(
        entityset, "Encounter", cutoff)
    assert len(fm_encoded) == 3 and len(fm_encoded.columns) == 32
