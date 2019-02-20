from .fhirbase import fhirbase


class Age(fhirbase):
    """
    A duration of time during which an organism (or a process) has
    existed.

    """

    __name__ = 'Age'

    def __init__(self, dict_values=None):
        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
