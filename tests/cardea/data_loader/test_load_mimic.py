#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from cardea.data_loader.load_mimic import get_table_properties, get_table_relationships


@pytest.fixture()
def admission():
    return "admissions"


@pytest.fixture()
def properties(admission):
    types, prim_key, arr_time = get_table_properties(admission)
    return types, prim_key, arr_time


@pytest.fixture()
def relationships(admission):
    relations = get_table_relationships(admission)
    return relations


def test_get_table_properties_types(properties):
    types = properties[0]
    assert len(types) == 19 and types['language'] == str


def test_get_table_properties_primkey(properties):
    primkey = properties[1]
    assert primkey == 'hadm_id'


def test_get_table_properties_arrtime(properties):
    arrtime = properties[2]
    assert len(arrtime) == 5


def test_get_table_relatopnships(relationships):
    assert len(relationships) == 18
