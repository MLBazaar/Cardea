from .fhirbase import fhirbase


class Period(fhirbase):
    """A time period defined by a start and end date and optionally time.
    """

    def __init__(self, dict_values=None):
        # the start of the period. the boundary is inclusive.
        self.start = None
        # type = string

        # the end of the period. if the end of the period is missing, it means
        # that the period is ongoing. the start may be in the past, and the end
        # date in the future, which means that period is expected/planned to end
        # at that time.
        self.end = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
