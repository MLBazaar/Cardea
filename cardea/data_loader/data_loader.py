import sys

from cardea import fhir


class DataLoader():

    def create_object(self, df, file_name):
        """Return FHIR representation of pandas dataframe."""

        id_exist = False

        object_values = {}
        for column in df.columns:
            object_values[column] = df[column].values

            if column in ['identifier', 'id', 'object_id']:
                id_exist = True

        if not id_exist:
            raise LookupError('{} is missing an identifier column', file_name)

        object = getattr(sys.modules[fhir.__name__], file_name)(object_values)
        object.assert_type()
        return object
