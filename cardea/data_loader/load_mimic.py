import os
import xml.etree.ElementTree as ET
from glob import glob

import featuretools as ft
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
root = ET.parse(path + '/schema.xml').getroot()


def get_table_properties(name):

    types = {}
    arr_time = []
    prim_key = 'row_id'

    x = root.find('.//table[@name="' + name + '"]')
    for t in x.findall('column'):

        column = t.get('name')
        a_type = t.get('type')
        d_type = get_type(a_type)
        prim_key = column if 'Primary key' in t.get('remarks') else prim_key

        if a_type == 'timestamp':
            arr_time.append(column)

        types[column.upper()] = d_type

    arr_time = arr_time[0] if len(arr_time) > 0 else None

    return types, prim_key, arr_time


def get_table_relationships(name):

    relations = []
    x = root.find('.//table[@name="' + name + '"]')

    for c in x.findall('column/child'):
        target_table = c.get('table')
        target_handle = c.get('column')

        handle = x.find('.//column/child/...').get('name')

        relations.append({'parent': name, 'primary_key': handle,
                          'child': target_table, 'foreign_key': target_handle})

    return relations


def get_type(x):
    return {
        'int4': float,
        'int2': float,
        'varchar': str,
        'float8': float,
        'text': str
    }.get(x, str)


def load_mimic_data(path=None):

    es = ft.EntitySet(id="mimic")

    relationships = []
    files = glob(path + '*.csv')

    for tag in root.findall('tables/table'):
        table = tag.get('name')
        file = table.upper() + '.csv'

        if (path + file) in files:
            # get table relationships
            relationships = relationships + get_table_relationships(table)

            # get table properties
            prop, key, arr_time = get_table_properties(table)

            # load table into a dataframe
            df = pd.read_csv(path + file, dtype=prop, date_parser=pd.to_datetime)
            df.columns = [column.lower() for column in df.columns]

            # load dataframe into the entityset
            es.entity_from_dataframe(entity_id=table,
                                     dataframe=df,
                                     index=key,
                                     time_index=arr_time)

    for r in relationships:
        new_relationship = ft.Relationship(es[r['parent']][r['primary_key']],
                                           es[r['child']][r['foreign_key']])

        es = es.add_relationship(new_relationship)

    return es
