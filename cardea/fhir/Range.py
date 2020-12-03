from .fhirbase import fhirbase


class Range(fhirbase):
    """
    A set of ordered Quantities defined by a low and high limit.

    Args:
        low: The low limit. The boundary is inclusive.
        high: The high limit. The boundary is inclusive.
    """

    __name__ = 'Range'

    def __init__(self, dict_values=None):
        self.low = None
        # reference to Quantity

        self.high = None
        # reference to Quantity

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Range',
             'child_variable': 'low'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Range',
             'child_variable': 'high'},
        ]
