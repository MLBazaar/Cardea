from .fhirbase import fhirbase


class Organization(fhirbase):
    """
    A formally or informally recognized grouping of people or
    organizations formed for the purpose of achieving some form of
    collective action.  Includes companies, institutions, corporations,
    departments, community groups, healthcare practice groups, etc.

    Args:
        resourceType: This is a Organization resource
        identifier: Identifier for the organization that is used to identify
            the organization across multiple disparate systems.
        active: Whether the organization's record is still in active use.
        type: The kind(s) of organization that this is.
        name: A name associated with the organization.
        alias: A list of alternate names that the organization is known as, or
            was known as in the past.
        telecom: A contact detail for the organization.
        address: An address for the organization.
        partOf: The organization of which this organization forms a part.
        contact: Contact for the organization for a certain purpose.
        endpoint: Technical endpoints providing access to services operated
            for the organization.
    """

    __name__ = 'Organization'

    def __init__(self, dict_values=None):
        self.resourceType = 'Organization'
        # type: str
        # possible values: Organization

        self.active = None
        # type: bool

        self.type = None
        # type: list
        # reference to CodeableConcept

        self.name = None
        # type: str

        self.alias = None
        # type: list

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.address = None
        # type: list
        # reference to Address

        self.partOf = None
        # reference to Reference: identifier

        self.contact = None
        # type: list
        # reference to Organization_Contact

        self.endpoint = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Organization_Contact',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'contact'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'telecom'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Organization',
             'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Organization',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Organization',
             'child_variable': 'address'},
        ]


class Organization_Contact(fhirbase):
    """
    A formally or informally recognized grouping of people or
    organizations formed for the purpose of achieving some form of
    collective action.  Includes companies, institutions, corporations,
    departments, community groups, healthcare practice groups, etc.

    Args:
        purpose: Indicates a purpose for which the contact can be reached.
        name: A name associated with the contact.
        telecom: A contact detail (e.g. a telephone number or an email
            address) by which the party may be contacted.
        address: Visiting or postal addresses for the contact.
    """

    __name__ = 'Organization_Contact'

    def __init__(self, dict_values=None):
        self.purpose = None
        # reference to CodeableConcept

        self.name = None
        # reference to HumanName

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.address = None
        # reference to Address

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

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Organization_Contact',
             'child_variable': 'address'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Organization_Contact',
             'child_variable': 'name'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Organization_Contact',
             'child_variable': 'telecom'},
        ]
