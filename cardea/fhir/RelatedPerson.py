from .fhirbase import fhirbase


class RelatedPerson(fhirbase):
    """
    Information about a person that is involved in the care for a patient,
    but who is not the target of healthcare, nor has a formal
    responsibility in the care process.
    """

    __name__ = 'RelatedPerson'

    def __init__(self, dict_values=None):
        self.resourceType = 'RelatedPerson'
        """
        This is a RelatedPerson resource

        type: string
        possible values: RelatedPerson
        """

        self.active = None
        """
        Whether this related person record is in active use.

        type: boolean
        """

        self.patient = None
        """
        The patient this person is related to.

        reference to Reference: identifier
        """

        self.relationship = None
        """
        The nature of the relationship between a patient and the related
        person.

        reference to CodeableConcept
        """

        self.name = None
        """
        A name associated with the person.

        type: array
        reference to HumanName
        """

        self.telecom = None
        """
        A contact detail for the person, e.g. a telephone number or an email
        address.

        type: array
        reference to ContactPoint
        """

        self.gender = None
        """
        Administrative Gender - the gender that the person is considered to
        have for administration and record keeping purposes.

        type: string
        possible values: male, female, other, unknown
        """

        self.birthDate = None
        """
        The date on which the related person was born.

        type: string
        """

        self.address = None
        """
        Address where the related person can be contacted or visited.

        type: array
        reference to Address
        """

        self.photo = None
        """
        Image of the person.

        type: array
        reference to Attachment
        """

        self.period = None
        """
        The period of time that this relationship is considered to be valid.
        If there are no dates defined, then the interval is unknown.

        reference to Period
        """

        self.identifier = None
        """
        Identifier for a person within a particular scope.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.gender is not None:
            for value in self.gender:
                if value is not None and value.lower() not in [
                        'male', 'female', 'other', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'male, female, other, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'telecom'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'period'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'photo'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RelatedPerson',
             'child_variable': 'patient'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'address'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'name'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedPerson',
             'child_variable': 'relationship'},
        ]
