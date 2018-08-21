import pandas as pd
import sys

from classes import *

def create_object(file_path):
    """ this method creates FHIR objects and fills values from .csv formatted tables
    """

    df = pd.read_csv(file_path)

    object_values = {}
    for column in df.columns:
        object_values[column] = df[column].values

    file_name = file_path.split("/")[-1].split(".")[0]
    object = getattr(sys.modules[__name__], file_name)(object_values)
    object.assert_type()
    return object
