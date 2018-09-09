from .fhirbase import fhirbase


class ContactDetail(fhirbase):
    """
    Specifies contact information for a person or organization.
    """

    __name__ = 'ContactDetail'

    def __init__(self, dict_values=None):
        self.name = None
        """
        The name of an individual to contact.

        type: string
        """

        self.telecom = None
        """
        The contact details for the individual (if a name was provided) or the
        organization.

        type: array
        reference to ContactPoint
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'ContactDetail',
             'child_variable': 'telecom'},
        ]
