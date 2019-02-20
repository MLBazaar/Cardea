from .fhirbase import fhirbase


class Duration(fhirbase):
    """
    A length of time.

    """

    __name__ = 'Duration'

    def __init__(self, dict_values=None):
        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
