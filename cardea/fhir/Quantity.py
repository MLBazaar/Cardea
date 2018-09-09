from .fhirbase import fhirbase


class Quantity(fhirbase):
    """
    A measured amount (or an amount that can potentially be measured).
    Note that measured amounts include amounts that are not precisely
    quantified, including amounts involving arbitrary units and floating
    currencies.
    """

    __name__ = 'Quantity'

    def __init__(self, dict_values=None):
        self.value = None
        """
        The value of the measured amount. The value includes an implicit
        precision in the presentation of the value.

        type: int
        """

        self.comparator = None
        """
        How the value should be understood and represented - whether the
        actual value is greater or less than the stated value due to
        measurement issues; e.g. if the comparator is "<" , then the real
        value is < stated value.

        type: string
        possible values: <, <=, >=, >
        """

        self.unit = None
        """
        A human-readable form of the unit.

        type: string
        """

        self.system = None
        """
        The identification of the system that provides the coded form of the
        unit.

        type: string
        """

        self.code = None
        """
        A computer processable form of the unit in some unit representation
        system.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.comparator is not None:
            for value in self.comparator:
                if value is not None and value.lower() not in [
                        '<', '<=', '>=', '>']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, '<, <=, >=, >'))
