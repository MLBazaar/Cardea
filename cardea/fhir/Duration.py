from .fhirbase import * 

class Duration(fhirbase):
    """A length of time.
    """

    def __init__(self, dict_values=None):

        if dict_values:
              self.set_attributes(dict_values)


