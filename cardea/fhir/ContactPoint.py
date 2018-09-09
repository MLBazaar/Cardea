from .fhirbase import fhirbase


class ContactPoint(fhirbase):
    """
    Details for all kinds of technology mediated contact points for a
    person or organization, including telephone, email, etc.
    """

    __name__ = 'ContactPoint'

    def __init__(self, dict_values=None):
        self.system = None
        """
        Telecommunications form for contact point - what communications system
        is required to make use of the contact.

        type: string
        possible values: phone, fax, email, pager, url, sms, other
        """

        self.value = None
        """
        The actual contact point details, in a form that is meaningful to the
        designated communication system (i.e. phone number or email address).

        type: string
        """

        self.use = None
        """
        Identifies the purpose for the contact point.

        type: string
        possible values: home, work, temp, old, mobile
        """

        self.rank = None
        """
        Specifies a preferred order in which to use a set of contacts.
        Contacts are ranked with lower values coming before higher values.

        type: int
        """

        self.period = None
        """
        Time period when the contact point was/is in use.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

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
