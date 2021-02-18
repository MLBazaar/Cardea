import os
import xml.etree.ElementTree as ET
from glob import glob

import featuretools as ft
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
root = ET.parse(path + '/schema.xml').getroot()


def get_table_properties(name):
    """Returns a tuple containing the datatype of each column, the primary key of the table,
        and the time indices.

    Args:
        name: The name of the table in the formal XML file.

    Returns:
        A tuple with three components, a list with the datatypes of each column, the primary key
            of the table, and a list of columns that consider the time indices of the table.
    """

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

        types[column.lower()] = d_type

    return types, prim_key, arr_time


def get_table_relationships(name):
    """Returns a list of the relationships in the table.

    Args:
        name: The name of the table in the formal XML file.

    Returns:
        A list of the relationships in the table, formatted as a dictionary.
    """

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


def load_mimic_data(path=None, subset=None):
    """Returns an entityset loaded with the dataframes in the received path.

    Args:
        path (str):
            The folder path that contains the data.
        subset (str):
            List of tables to include.

    Returns:
        featuretools.EntitySet:
            An entityset with loaded data.
    """
    es = ft.EntitySet(id="mimic")

    relationships = []
    global_tables = []
    files = glob(path + '/*.csv')

    for tag in root.findall('tables/table'):
        table = tag.get('name')
        file = os.path.join(path, table.upper() + '.csv')

        if subset and table not in subset:
            continue

        if file in files:
            # table name
            global_tables.append(table)

            # get table relationships
            relationships = relationships + get_table_relationships(table)

            # get table properties
            prop, key, arr_time = get_table_properties(table)

            # load table into a dataframe
            df = pd.read_csv(file, dtype=prop, date_parser=pd.to_datetime)

            df.columns = [column.lower() for column in df.columns]

            # check if arr_time should be None (no time index)
            arr_time = arr_time[0] if len(arr_time) > 0 else None

            if arr_time and df[arr_time].isnull().all():
                arr_time = None

            # load dataframe into the entityset
            es.entity_from_dataframe(entity_id=table,
                                     dataframe=df,
                                     index=key,
                                     time_index=arr_time)

    for r in relationships:
        if (r['parent'] in global_tables and r['child'] in global_tables):
            new_relationship = ft.Relationship(es[r['parent']][r['primary_key']],
                                               es[r['child']][r['foreign_key']])

            es = es.add_relationship(new_relationship)

    return es
