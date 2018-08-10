from .fhirbase import * 

class ResourceList(fhirbase):
    def __init__(self, dict_values=None):
        self.ref = None


        if dict_values:
              self.set_attributes(dict_values)


