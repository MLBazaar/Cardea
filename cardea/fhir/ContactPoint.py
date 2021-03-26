from .fhirbase import fhirbase


class ContactPoint(fhirbase):
    """
    Details for all kinds of technology mediated contact points for a
    person or organization, including telephone, email, etc.

    Args:
        system: Telecommunications form for contact point - what
            communications system is required to make use of the contact.
        value: The actual contact point details, in a form that is meaningful
            to the designated communication system (i.e. phone number or email
            address).
        use: Identifies the purpose for the contact point.
        rank: Specifies a preferred order in which to use a set of contacts.
            Contacts are ranked with lower values coming before higher values.
        period: Time period when the contact point was/is in use.
    """

    __name__ = 'ContactPoint'

    def __init__(self, dict_values=None):
        self.system = None
        # type: str
        # possible values: phone, fax, email, pager, url, sms, other

        self.value = None
        # type: str

        self.use = None
        # type: str
        # possible values: home, work, temp, old, mobile

        self.rank = None
        # type: int

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
