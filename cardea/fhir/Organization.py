from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Address import Address
from .Reference import Reference
from .ContactPoint import ContactPoint

class Organization(fhirbase):
    """A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """

    def __init__(self, dict_values=None):
        # this is a organization resource
        self.resourceType = 'Organization'
        # type = string
        # possible values = Organization

        # whether the organization's record is still in active use.
        self.active = None
        # type = boolean

        # the kind(s) of organization that this is.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a name associated with the organization.
        self.name = None
        # type = string

        # a list of alternate names that the organization is known as, or was
        # known as in the past.
        self.alias = None
        # type = array

        # a contact detail for the organization.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # an address for the organization.
        self.address = None
        # type = array
        # reference to Address: Address

        # the organization of which this organization forms a part.
        self.partOf = None
        # reference to Reference: identifier

        # contact for the organization for a certain purpose.
        self.contact = None
        # type = array
        # reference to Organization_Contact: Organization_Contact

        # technical endpoints providing access to services operated for the
        # organization.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # identifier for the organization that is used to identify the
        # organization across multiple disparate systems.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Organization',
            'child_variable': 'endpoint'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Organization',
            'child_variable': 'partOf'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Organization',
            'child_variable': 'telecom'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Organization',
            'child_variable': 'identifier'},

            {'parent_entity': 'Organization_Contact',
            'parent_variable': 'object_id',
            'child_entity': 'Organization',
            'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Organization',
            'child_variable': 'type'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Organization',
            'child_variable': 'address'},
        ]

class Organization_Contact(fhirbase):
    """A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """

    def __init__(self, dict_values=None):
        # indicates a purpose for which the contact can be reached.
        self.purpose = None
        # reference to CodeableConcept: CodeableConcept

        # a name associated with the contact.
        self.name = None
        # reference to HumanName: HumanName

        # a contact detail (e.g. a telephone number or an email address) by which
        # the party may be contacted.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # visiting or postal addresses for the contact.
        self.address = None
        # reference to Address: Address


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Organization_Contact',
            'child_variable': 'address'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Organization_Contact',
            'child_variable': 'telecom'},

            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'Organization_Contact',
            'child_variable': 'name'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Organization_Contact',
            'child_variable': 'purpose'},
        ]

