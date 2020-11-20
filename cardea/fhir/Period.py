from .fhirbase import fhirbase


class Period(fhirbase):
    """
    A time period defined by a start and end date and optionally time.

    Args:
        start: The start of the period. The boundary is inclusive.
        end: The end of the period. If the end of the period is missing, it
            means that the period is ongoing. The start may be in the past, and
            the end date in the future, which means that period is
            expected/planned to end at that time.
    """

    __name__ = 'Period'

    def __init__(self, dict_values=None):
        self.start = None
        # type: str

        self.end = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
