from .fhirbase import fhirbase


class Distance(fhirbase):
    """
    A length - a value with a unit that is a physical distance.

    """

    __name__ = 'Distance'

    def __init__(self, dict_values=None):
        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
