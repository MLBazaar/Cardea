from .fhirbase import * 
from .Quantity import Quantity

class Range(fhirbase):
    """A set of ordered Quantities defined by a low and high limit.
    """

    def __init__(self, dict_values=None):
        # the low limit. the boundary is inclusive.
        self.low = None
        # reference to Quantity: Quantity

        # the high limit. the boundary is inclusive.
        self.high = None
        # reference to Quantity: Quantity


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

