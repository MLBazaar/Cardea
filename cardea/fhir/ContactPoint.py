from .fhirbase import fhirbase


class ContactPoint(fhirbase):
    """Details for all kinds of technology mediated contact points for a person
    or organization, including telephone, email, etc.
    """

    def __init__(self, dict_values=None):
        # telecommunications form for contact point - what communications system
        # is required to make use of the contact.
        self.system = None
        # type = string
        # possible values: phone, fax, email, pager, url, sms, other

        # the actual contact point details, in a form that is meaningful to the
        # designated communication system (i.e. phone number or email address).
        self.value = None
        # type = string

        # identifies the purpose for the contact point.
        self.use = None
        # type = string
        # possible values: home, work, temp, old, mobile

        # specifies a preferred order in which to use a set of contacts. contacts
        # are ranked with lower values coming before higher values.
        self.rank = None
        # type = int

        # time period when the contact point was/is in use.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.system is not None:
            for value in self.system:
                if value is not None and value.lower() not in [
                        'phone', 'fax', 'email', 'pager', 'url', 'sms', 'other']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'phone, fax, email, pager, url, sms, other'))

        if self.use is not None:
            for value in self.use:
                if value is not None and value.lower() not in [
                        'home', 'work', 'temp', 'old', 'mobile']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'home, work, temp, old, mobile'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ContactPoint',
             'child_variable': 'period'},
        ]
