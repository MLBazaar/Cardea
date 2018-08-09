from .fhirbase import * 

class Money(fhirbase):
    """An amount of economic utility in some recognized currency.
    """

    def __init__(self, dict_values=None):

        if dict_values:
              self.set_attributes(dict_values)


