from .fhirbase import fhirbase


class Address(fhirbase):
    """
    An address expressed using postal conventions (as opposed to GPS or
    other location definition formats).  This data type may be used to
    convey addresses for use in delivering mail as well as for visiting
    locations which might not be valid for mail delivery.  There are a
    variety of postal address formats defined around the world.
    """

    __name__ = 'Address'

    def __init__(self, dict_values=None):
        self.use = None
        """
        The purpose of this address.

        type: string
        possible values: home, work, temp, old
        """

        self.type = None
        """
        Distinguishes between physical addresses (those you can visit) and
        mailing addresses (e.g. PO Boxes and care-of addresses). Most
        addresses are both.

        type: string
        possible values: postal, physical, both
        """

        self.text = None
        """
        A full text representation of the address.

        type: string
        """

        self.line = None
        """
        This component contains the house number, apartment number, street
        name, street direction,  P.O. Box number, delivery hints, and similar
        address information.

        type: array
        """

        self.city = None
        """
        The name of the city, town, village or other community or delivery
        center.

        type: string
        """

        self.district = None
        """
        The name of the administrative area (county).

        type: string
        """

        self.state = None
        """
        Sub-unit of a country with limited sovereignty in a federally
        organized country. A code may be used if codes are in common use (i.e.
        US 2 letter state codes).

        type: string
        """

        self.postalCode = None
        """
        A postal code designating a region defined by the postal service.

        type: string
        """

        self.country = None
        """
        Country - a nation as commonly understood or generally accepted.

        type: string
        """

        self.period = None
        """
        Time period when address was/is in use.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.use is not None:
            for value in self.use:
                if value is not None and value.lower() not in [
                        'home', 'work', 'temp', 'old']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'home, work, temp, old'))

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'postal', 'physical', 'both']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'postal, physical, both'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Address',
             'child_variable': 'period'},
        ]
