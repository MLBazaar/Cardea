from .fhirbase import fhirbase


class Ratio(fhirbase):
    """
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.

    Args:
        numerator: The value of the numerator.
        denominator: The value of the denominator.
    """

    __name__ = 'Ratio'

    def __init__(self, dict_values=None):
        self.numerator = None
        # reference to Quantity

        self.denominator = None
        # reference to Quantity

        self.object_id = None
        # unique identifier for object class

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
