from .fhirbase import fhirbase


class Organization(fhirbase):
    """
    A formally or informally recognized grouping of people or
    organizations formed for the purpose of achieving some form of
    collective action.  Includes companies, institutions, corporations,
    departments, community groups, healthcare practice groups, etc.
    """

    __name__ = 'Organization'

    def __init__(self, dict_values=None):
        self.resourceType = 'Organization'
        """
        This is a Organization resource

        type: string
        possible values: Organization
        """

        self.active = None
        """
        Whether the organization's record is still in active use.

        type: boolean
        """

        self.type = None
        """
        The kind(s) of organization that this is.

        type: array
        reference to CodeableConcept
        """

        self.name = None
        """
        A name associated with the organization.

        type: string
        """

        self.alias = None
        """
        A list of alternate names that the organization is known as, or was
        known as in the past.

        type: array
        """

        self.telecom = None
        """
        A contact detail for the organization.

        type: array
        reference to ContactPoint
        """

        self.address = None
        """
        An address for the organization.

        type: array
        reference to Address
        """

        self.partOf = None
        """
        The organization of which this organization forms a part.

        reference to Reference: identifier
        """

        self.contact = None
        """
        Contact for the organization for a certain purpose.

        type: array
        reference to Organization_Contact
        """

        self.endpoint = None
        """
        Technical endpoints providing access to services operated for the
        organization.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifier for the organization that is used to identify the
        organization across multiple disparate systems.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Organization',
             'child_variable': 'partOf'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'telecom'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Organization',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'identifier'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'address'},

            {'parent_entity': 'Organization_Contact',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'contact'},
        ]


class Organization_Contact(fhirbase):
    """
    A formally or informally recognized grouping of people or
    organizations formed for the purpose of achieving some form of
    collective action.  Includes companies, institutions, corporations,
    departments, community groups, healthcare practice groups, etc.
    """

    __name__ = 'Organization_Contact'

    def __init__(self, dict_values=None):
        self.purpose = None
        """
        Indicates a purpose for which the contact can be reached.

        reference to CodeableConcept
        """

        self.name = None
        """
        A name associated with the contact.

        reference to HumanName
        """

        self.telecom = None
        """
        A contact detail (e.g. a telephone number or an email address) by
        which the party may be contacted.

        type: array
        reference to ContactPoint
        """

        self.address = None
        """
        Visiting or postal addresses for the contact.

        reference to Address
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Organization_Contact',
             'child_variable': 'purpose'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Organization_Contact',
             'child_variable': 'telecom'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Organization_Contact',
             'child_variable': 'name'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Organization_Contact',
             'child_variable': 'address'},
        ]
