from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .HumanName import HumanName
from .Identifier import Identifier
from .Address import Address
from .ContactPoint import ContactPoint
from .Attachment import Attachment

class Practitioner(fhirbase):
    """A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    def __init__(self, dict_values=None):
        # this is a practitioner resource
        self.resourceType = 'Practitioner'
        # type = string
        # possible values = Practitioner

        # whether this practitioner's record is in active use.
        self.active = None
        # type = boolean

        # the name(s) associated with the practitioner.
        self.name = None
        # type = array
        # reference to HumanName: HumanName

        # a contact detail for the practitioner, e.g. a telephone number or an
        # email address.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # address(es) of the practitioner that are not role specific (typically
        # home address).  work addresses are not typically entered in this
        # property as they are usually role dependent.
        self.address = None
        # type = array
        # reference to Address: Address

        # administrative gender - the gender that the person is considered to have
        # for administration and record keeping purposes.
        self.gender = None
        # type = string
        # possible values = male, female, other, unknown

        # the date of birth for the practitioner.
        self.birthDate = None
        # type = string

        # image of the person.
        self.photo = None
        # type = array
        # reference to Attachment: Attachment

        # qualifications obtained by training and certification.
        self.qualification = None
        # type = array
        # reference to Practitioner_Qualification: identifier

        # a language the practitioner is able to use in patient communication.
        self.communication = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # an identifier that applies to this person in this role.
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
            {'parent_entity': 'Practitioner_Qualification',
            'parent_variable': 'identifier',
            'child_entity': 'Practitioner',
            'child_variable': 'qualification'},

            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner',
            'child_variable': 'name'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner',
            'child_variable': 'photo'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner',
            'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner',
            'child_variable': 'communication'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner',
            'child_variable': 'address'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner',
            'child_variable': 'telecom'},
        ]

class Practitioner_Qualification(fhirbase):
    """A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    def __init__(self, dict_values=None):
        # coded representation of the qualification.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # period during which the qualification is valid.
        self.period = None
        # reference to Period: Period

        # organization that regulates and issues the qualification.
        self.issuer = None
        # reference to Reference: identifier

        # an identifier that applies to this person's qualification in this role.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner_Qualification',
            'child_variable': 'period'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Practitioner_Qualification',
            'child_variable': 'issuer'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner_Qualification',
            'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Practitioner_Qualification',
            'child_variable': 'code'},
        ]

