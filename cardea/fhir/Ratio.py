from .fhirbase import * 
from .Quantity import Quantity

class Ratio(fhirbase):
    """A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    def __init__(self, dict_values=None):
        # the value of the numerator.
        self.numerator = None
        # reference to Quantity: Quantity

        # the value of the denominator.
        self.denominator = None
        # reference to Quantity: Quantity


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Ratio',
            'child_variable': 'denominator'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Ratio',
            'child_variable': 'numerator'},
        ]

