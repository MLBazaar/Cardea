from .fhirbase import fhirbase


class ResourceList(fhirbase):
    def __init__(self, dict_values=None):
        self.ref = None

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
