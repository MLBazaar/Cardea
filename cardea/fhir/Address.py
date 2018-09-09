from .fhirbase import fhirbase


class Address(fhirbase):
    """An address expressed using postal conventions (as opposed to GPS or
    other location definition formats).  This data type may be used to
    convey addresses for use in delivering mail as well as for visiting
    locations which might not be valid for mail delivery.  There are a
    variety of postal address formats defined around the world.
    """

    def __init__(self, dict_values=None):
        # the purpose of this address.
        self.use = None
        # type = string
        # possible values: home, work, temp, old

        # distinguishes between physical addresses (those you can visit) and
        # mailing addresses (e.g. po boxes and care-of addresses). most addresses
        # are both.
        self.type = None
        # type = string
        # possible values: postal, physical, both

        # a full text representation of the address.
        self.text = None
        # type = string

        # this component contains the house number, apartment number, street name,
        # street direction,  p.o. box number, delivery hints, and similar address
        # information.
        self.line = None
        # type = array

        # the name of the city, town, village or other community or delivery
        # center.
        self.city = None
        # type = string

        # the name of the administrative area (county).
        self.district = None
        # type = string

        # sub-unit of a country with limited sovereignty in a federally organized
        # country. a code may be used if codes are in common use (i.e. us 2 letter
        # state codes).
        self.state = None
        # type = string

        # a postal code designating a region defined by the postal service.
        self.postalCode = None
        # type = string

        # country - a nation as commonly understood or generally accepted.
        self.country = None
        # type = string

        # time period when address was/is in use.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

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
