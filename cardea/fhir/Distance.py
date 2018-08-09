from .fhirbase import * 

class Distance(fhirbase):
    """A length - a value with a unit that is a physical distance.
    """

    def __init__(self, dict_values=None):

        if dict_values:
              self.set_attributes(dict_values)


