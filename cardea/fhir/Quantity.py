from .fhirbase import fhirbase


class Quantity(fhirbase):
    """A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """

    __name__ = 'Quantity'

    def __init__(self, dict_values=None):
        # the value of the measured amount. the value includes an implicit
        # precision in the presentation of the value.
        self.value = None
        # type = int

        # how the value should be understood and represented - whether the actual
        # value is greater or less than the stated value due to measurement
        # issues; e.g. if the comparator is "<" , then the real value is < stated
        # value.
        self.comparator = None
        # type = string
        # possible values: <, <=, >=, >

        # a human-readable form of the unit.
        self.unit = None
        # type = string

        # the identification of the system that provides the coded form of the
        # unit.
        self.system = None
        # type = string

        # a computer processable form of the unit in some unit representation
        # system.
        self.code = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.comparator is not None:
            for value in self.comparator:
                if value is not None and value.lower() not in [
                        '<', '<=', '>=', '>']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, '<, <=, >=, >'))
