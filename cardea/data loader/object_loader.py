import sys

from fhir.classes import *

def create_object(df, file_name):
    """ this method creates FHIR objects and fills values from pandas dataframes
    """
    
    id_exist = False

    object_values = {}
    for column in df.columns:
        object_values[column] = df[column].values

        if column in ['identifier', 'id', 'object_id']:
            id_exist = True

    if not id_exist:
        raise LookupError('{} is missing an identifier column', file_name)

    object = getattr(sys.modules[__name__], file_name)(object_values)
    object.assert_type()
    return object
