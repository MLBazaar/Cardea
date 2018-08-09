from .fhirbase import * 
from .HumanName import HumanName
from .Identifier import Identifier
from .Address import Address
from .Reference import Reference
from .ContactPoint import ContactPoint
from .Attachment import Attachment

class Person(fhirbase):
    """Demographics and administrative information about a person independent
    of a specific health-related context.
    """

    def __init__(self, dict_values=None):
        # this is a person resource
        self.resourceType = 'Person'
        # type = string
        # possible values = Person

        # a name associated with the person.
        self.name = None
        # type = array
        # reference to HumanName: HumanName

        # a contact detail for the person, e.g. a telephone number or an email
        # address.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # administrative gender.
        self.gender = None
        # type = string
        # possible values = male, female, other, unknown

        # the birth date for the person.
        self.birthDate = None
        # type = string

        # one or more addresses for the person.
        self.address = None
        # type = array
        # reference to Address: Address

        # an image that can be displayed as a thumbnail of the person to enhance
        # the identification of the individual.
        self.photo = None
        # reference to Attachment: Attachment

        # the organization that is the custodian of the person record.
        self.managingOrganization = None
        # reference to Reference: identifier

        # whether this person's record is in active use.
        self.active = None
        # type = boolean

        # link to a resource that concerns the same actual person.
        self.link = None
        # type = array
        # reference to Person_Link: Person_Link

        # identifier for a person within a particular scope.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.gender is not None:
            for value in self.gender:
                if value != None and value.lower() not in ['male', 'female', 'other', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'male, female, other, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'Person',
            'child_variable': 'name'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Person',
            'child_variable': 'photo'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Person',
            'child_variable': 'telecom'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Person',
            'child_variable': 'managingOrganization'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Person',
            'child_variable': 'address'},

            {'parent_entity': 'Person_Link',
            'parent_variable': 'object_id',
            'child_entity': 'Person',
            'child_variable': 'link'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Person',
            'child_variable': 'identifier'},
        ]

class Person_Link(fhirbase):
    """Demographics and administrative information about a person independent
    of a specific health-related context.
    """

    def __init__(self, dict_values=None):
        # the resource to which this actual person is associated.
        self.target = None
        # reference to Reference: identifier

        # level of assurance that this link is actually associated with the target
        # resource.
        self.assurance = None
        # type = string
        # possible values = level1, level2, level3, level4


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.assurance is not None:
            for value in self.assurance:
                if value != None and value.lower() not in ['level1', 'level2', 'level3', 'level4']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'level1, level2, level3, level4'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Person_Link',
            'child_variable': 'target'},
        ]

