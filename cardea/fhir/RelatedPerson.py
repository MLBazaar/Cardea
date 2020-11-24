from .fhirbase import fhirbase


class RelatedPerson(fhirbase):
    """
    Information about a person that is involved in the care for a patient,
    but who is not the target of healthcare, nor has a formal
    responsibility in the care process.

    Args:
        resourceType: This is a RelatedPerson resource
        identifier: Identifier for a person within a particular scope.
        active: Whether this related person record is in active use.
        patient: The patient this person is related to.
        relationship: The nature of the relationship between a patient and the
            related person.
        name: A name associated with the person.
        telecom: A contact detail for the person, e.g. a telephone number or
            an email address.
        gender: Administrative Gender - the gender that the person is
            considered to have for administration and record keeping purposes.
        birthDate: The date on which the related person was born.
        address: Address where the related person can be contacted or visited.
        photo: Image of the person.
        period: The period of time that this relationship is considered to be
            valid. If there are no dates defined, then the interval is unknown.
    """

    __name__ = 'RelatedPerson'

    def __init__(self, dict_values=None):
        self.resourceType = 'RelatedPerson'
        # type: str
        # possible values: RelatedPerson

        self.active = None
        # type: bool

        self.patient = None
        # reference to Reference: identifier

        self.relationship = None
        # reference to CodeableConcept

        self.name = None
        # type: list
        # reference to HumanName

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.gender = None
        # type: str
        # possible values: male, female, other, unknown

        self.birthDate = None
        # type: str

        self.address = None
        # type: list
        # reference to Address

        self.photo = None
        # type: list
        # reference to Attachment

        self.period = None
        # reference to Period

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.gender is not None:
            for value in self.gender:
                if value is not None and value.lower() not in [
                        'male', 'female', 'other', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'male, female, other, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'address'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'photo'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'relationship'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RelatedPerson',
             'child_variable': 'patient'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'name'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'telecom'},
        ]
