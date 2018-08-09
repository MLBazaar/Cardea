from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .HumanName import HumanName
from .Address import Address
from .Reference import Reference
from .ContactPoint import ContactPoint
from .Period import Period
from .Attachment import Attachment

class RelatedPerson(fhirbase):
    """Information about a person that is involved in the care for a patient,
    but who is not the target of healthcare, nor has a formal responsibility
    in the care process.
    """

    def __init__(self, dict_values=None):
        # this is a relatedperson resource
        self.resourceType = 'RelatedPerson'
        # type = string
        # possible values = RelatedPerson

        # whether this related person record is in active use.
        self.active = None
        # type = boolean

        # the patient this person is related to.
        self.patient = None
        # reference to Reference: identifier

        # the nature of the relationship between a patient and the related person.
        self.relationship = None
        # reference to CodeableConcept: CodeableConcept

        # a name associated with the person.
        self.name = None
        # type = array
        # reference to HumanName: HumanName

        # a contact detail for the person, e.g. a telephone number or an email
        # address.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # administrative gender - the gender that the person is considered to have
        # for administration and record keeping purposes.
        self.gender = None
        # type = string
        # possible values = male, female, other, unknown

        # the date on which the related person was born.
        self.birthDate = None
        # type = string

        # address where the related person can be contacted or visited.
        self.address = None
        # type = array
        # reference to Address: Address

        # image of the person.
        self.photo = None
        # type = array
        # reference to Attachment: Attachment

        # the period of time that this relationship is considered to be valid. if
        # there are no dates defined, then the interval is unknown.
        self.period = None
        # reference to Period: Period

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
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'RelatedPerson',
            'child_variable': 'patient'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'RelatedPerson',
            'child_variable': 'photo'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'RelatedPerson',
            'child_variable': 'relationship'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'RelatedPerson',
            'child_variable': 'period'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'RelatedPerson',
            'child_variable': 'telecom'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'RelatedPerson',
            'child_variable': 'identifier'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'RelatedPerson',
            'child_variable': 'address'},

            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'RelatedPerson',
            'child_variable': 'name'},
        ]

