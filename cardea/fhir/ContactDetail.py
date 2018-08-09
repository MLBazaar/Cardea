from .fhirbase import * 
from .ContactPoint import ContactPoint

class ContactDetail(fhirbase):
    """Specifies contact information for a person or organization.
    """

    def __init__(self, dict_values=None):
        # the name of an individual to contact.
        self.name = None
        # type = string

        # the contact details for the individual (if a name was provided) or the
        # organization.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'ContactDetail',
            'child_variable': 'telecom'},
        ]

