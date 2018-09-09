import inspect
import sys

from cardea import fhir


class DataLoader():

    __name__ = 'DataLoader'

    def create_object(self, df, file_name):
        """Return FHIR representation of pandas dataframe."""

        fhir_classes = [c[0] for c in inspect.getmembers(fhir)]
        if file_name not in fhir_classes:
            raise LookupError('{} file is not part of FHIR schema'.format(file_name))

        object_values = df.to_dict('list')
        id_enum = ['identifier', 'id', 'object_id']

        id_exist = any(i in df.columns for i in id_enum)

        if not id_exist:
            raise LookupError('{} is missing an identifier column'.format(file_name))

        object = getattr(sys.modules[fhir.__name__], file_name)(object_values)
        object.assert_type()
        return object
