from .fhirbase import fhirbase


class Money(fhirbase):
    """An amount of economic utility in some recognized currency.
    """

    def __init__(self, dict_values=None):
        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
