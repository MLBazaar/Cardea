from glob import glob
import pandas as pd
import sys

import featuretools as ft

from classes import *

def create_object(file):
    df = pd.read_csv(file)

    entity_values = {}
    for column in df.columns:

        entity_values[column] = df[column].values

    file = file.split("/")[-1].split(".")[0]
    object = getattr(sys.modules[__name__], file)(entity_values)
    object.assert_type()
    all_objects.append(object)
    create_entity(object)

def create_entity(object):
    df = object.get_dataframe()

    # get ID if exists
    if 'identifier' in df.columns:
        id = 'identifier'
    elif 'id' in df.columns:
        id = 'id'
    else:
        id = 'object_id'

    if object.__class__.__name__ == 'Period':
        entity_set.entity_from_dataframe(entity_id=str(object.__class__.__name__),
                                 dataframe=df,
                                 index=id,
                                 time_index="start")
    else:
        entity_set.entity_from_dataframe(entity_id=str(object.__class__.__name__),
                                 dataframe=df,
                                 index=id)


def create_relationships(entity):
    for relation in entity.get_relationships():
        # parent table: 0, field: 1
        # child table: 2, field: 3

        if relation['parent_entity'] in entity_set.entity_names and getattr(entity, relation['child_variable']) is not None:
            new_relationship = ft.Relationship(entity_set[relation['parent_entity']][relation['parent_variable']],
                                               entity_set[relation['child_entity']][relation['child_variable']])

            entity_set.add_relationship(new_relationship)




all_objects = []
all_files = glob("data/*.csv")
entity_set = ft.EntitySet(id="fhir")

for file in all_files:
    entity = create_object(file)

for entity in all_objects:
    create_relationships(entity)
