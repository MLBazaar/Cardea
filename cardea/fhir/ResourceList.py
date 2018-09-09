from .fhirbase import fhirbase


class ResourceList(fhirbase):
    __name__ = 'ResourceList'

    def __init__(self, dict_values=None):
        self.ref = None

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
