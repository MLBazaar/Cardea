from .fhirbase import fhirbase


class Money(fhirbase):
    """
    An amount of economic utility in some recognized currency.

    """

    __name__ = 'Money'

    def __init__(self, dict_values=None):
        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
