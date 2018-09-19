from .fhirbase import fhirbase


class Count(fhirbase):
    """
    A measured amount (or an amount that can potentially be measured).
    Note that measured amounts include amounts that are not precisely
    quantified, including amounts involving arbitrary units and floating
    currencies.

    """

    __name__ = 'Count'

    def __init__(self, dict_values=None):
        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
