from .fhirbase import fhirbase


class Practitioner(fhirbase):
    """
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    __name__ = 'Practitioner'

    def __init__(self, dict_values=None):
        self.resourceType = 'Practitioner'
        """
        This is a Practitioner resource

        type: string
        possible values: Practitioner
        """

        self.active = None
        """
        Whether this practitioner's record is in active use.

        type: boolean
        """

        self.name = None
        """
        The name(s) associated with the practitioner.

        type: array
        reference to HumanName
        """

        self.telecom = None
        """
        A contact detail for the practitioner, e.g. a telephone number or an
        email address.

        type: array
        reference to ContactPoint
        """

        self.address = None
        """
        Address(es) of the practitioner that are not role specific (typically
        home address).  Work addresses are not typically entered in this
        property as they are usually role dependent.

        type: array
        reference to Address
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
        The date of birth for the practitioner.

        type: string
        """

        self.photo = None
        """
        Image of the person.

        type: array
        reference to Attachment
        """

        self.qualification = None
        """
        Qualifications obtained by training and certification.

        type: array
        reference to Practitioner_Qualification: identifier
        """

        self.communication = None
        """
        A language the practitioner is able to use in patient communication.

        type: array
        reference to CodeableConcept
        """

        self.identifier = None
        """
        An identifier that applies to this person in this role.

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'identifier'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'name'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'communication'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'telecom'},

            {'parent_entity': 'Practitioner_Qualification',
             'parent_variable': 'identifier',
             'child_entity': 'Practitioner',
             'child_variable': 'qualification'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'photo'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Practitioner',
             'child_variable': 'address'},
        ]


class Practitioner_Qualification(fhirbase):
    """
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """

    __name__ = 'Practitioner_Qualification'

    def __init__(self, dict_values=None):
        self.code = None
        """
        Coded representation of the qualification.

        reference to CodeableConcept
        """

        self.period = None
        """
        Period during which the qualification is valid.

        reference to Period
        """

        self.issuer = None
        """
        Organization that regulates and issues the qualification.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        An identifier that applies to this person's qualification in this
        role.

        type: array
        reference to Identifier
        """

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
