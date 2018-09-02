from .fhirbase import fhirbase


class Age(fhirbase):
    """A duration of time during which an organism (or a process) has existed.
    """

    def __init__(self, dict_values=None):
        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
