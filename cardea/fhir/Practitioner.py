from .fhirbase import fhirbase


class Practitioner(fhirbase):
    """
    A person who is directly or indirectly involved in the provisioning of
    healthcare.

    Args:
        resourceType: This is a Practitioner resource
        identifier: An identifier that applies to this person in this role.
        active: Whether this practitioner's record is in active use.
        name: The name(s) associated with the practitioner.
        telecom: A contact detail for the practitioner, e.g. a telephone
            number or an email address.
        address: Address(es) of the practitioner that are not role specific
            (typically home address).  Work addresses are not typically entered in
            this property as they are usually role dependent.
        gender: Administrative Gender - the gender that the person is
            considered to have for administration and record keeping purposes.
        birthDate: The date of birth for the practitioner.
        photo: Image of the person.
        qualification: Qualifications obtained by training and certification.
        communication: A language the practitioner is able to use in patient
            communication.
    """

    __name__ = 'Practitioner'

    def __init__(self, dict_values=None):
        self.resourceType = 'Practitioner'
        # type: str
        # possible values: Practitioner

        self.active = None
        # type: bool

        self.name = None
        # type: list
        # reference to HumanName

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.address = None
        # type: list
        # reference to Address

        self.gender = None
        # type: str
        # possible values: male, female, other, unknown

        self.birthDate = None
        # type: str

        self.photo = None
        # type: list
        # reference to Attachment

        self.qualification = None
        # type: list
        # reference to Practitioner_Qualification: identifier

        self.communication = None
        # type: list
        # reference to CodeableConcept

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
            {'parent_entity': 'Practitioner_Qualification',
             'parent_variable': 'identifier',
             'child_entity': 'Practitioner',
             'child_variable': 'qualification'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'name'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'communication'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'address'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'photo'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'identifier'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'telecom'},
        ]


class Practitioner_Qualification(fhirbase):
    """
    A person who is directly or indirectly involved in the provisioning of
    healthcare.

    Args:
        identifier: An identifier that applies to this person's qualification
            in this role.
        code: Coded representation of the qualification.
        period: Period during which the qualification is valid.
        issuer: Organization that regulates and issues the qualification.
    """

    __name__ = 'Practitioner_Qualification'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.period = None
        # reference to Period

        self.issuer = None
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner_Qualification',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Practitioner_Qualification',
             'child_variable': 'issuer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner_Qualification',
             'child_variable': 'code'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner_Qualification',
             'child_variable': 'period'},
        ]
