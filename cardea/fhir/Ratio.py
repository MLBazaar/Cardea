from .fhirbase import fhirbase


class Ratio(fhirbase):
    """A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    __name__ = 'Ratio'

    def __init__(self, dict_values=None):
        # the value of the numerator.
        self.numerator = None
        # reference to Quantity: Quantity

        # the value of the denominator.
        self.denominator = None
        # reference to Quantity: Quantity

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Ratio',
             'child_variable': 'numerator'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Ratio',
             'child_variable': 'denominator'},
        ]
