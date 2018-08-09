from .fhirbase import * 

class Age(fhirbase):
    """A duration of time during which an organism (or a process) has existed.
    """

    def __init__(self, dict_values=None):

        if dict_values:
              self.set_attributes(dict_values)


