from .fhirbase import fhirbase


class Patient(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.

    Args:
        resourceType: This is a Patient resource
        identifier: An identifier for this patient.
        active: Whether this patient record is in active use.
        name: A name associated with the individual.
        telecom: A contact detail (e.g. a telephone number or an email
            address) by which the individual may be contacted.
        gender: Administrative Gender - the gender that the patient is
            considered to have for administration and record keeping purposes.
        birthDate: The date of birth for the individual.
        deceasedBoolean: Indicates if the individual is deceased or not.
        deceasedDateTime: Indicates if the individual is deceased or not.
        address: Addresses for the individual.
        maritalStatus: This field contains a patient's most recent marital
            (civil) status.
        multipleBirthBoolean: Indicates whether the patient is part of a
            multiple (bool) or indicates the actual birth order (integer).
        multipleBirthInteger: Indicates whether the patient is part of a
            multiple (bool) or indicates the actual birth order (integer).
        photo: Image of the patient.
        contact: A contact party (e.g. guardian, partner, friend) for the
            patient.
        animal: This patient is known to be an animal.
        communication: Languages which may be used to communicate with the
            patient about his or her health.
        generalPractitioner: Patient's nominated care provider.
        managingOrganization: Organization that is the custodian of the
            patient record.
        link: Link to another patient resource that concerns the same actual
            patient.
    """

    __name__ = 'Patient'

    def __init__(self, dict_values=None):
        self.resourceType = 'Patient'
        # type: str
        # possible values: Patient

        self.active = None
        # type: bool

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

        self.deceasedBoolean = None
        # type: bool

        self.deceasedDateTime = None
        # type: str

        self.address = None
        # type: list
        # reference to Address

        self.maritalStatus = None
        # reference to CodeableConcept

        self.multipleBirthBoolean = None
        # type: bool

        self.multipleBirthInteger = None
        # type: int

        self.photo = None
        # type: list
        # reference to Attachment

        self.contact = None
        # type: list
        # reference to Patient_Contact

        self.animal = None
        # reference to Patient_Animal

        self.communication = None
        # type: list
        # reference to Patient_Communication

        self.generalPractitioner = None
        # type: list
        # reference to Reference: identifier

        self.managingOrganization = None
        # reference to Reference: identifier

        self.link = None
        # type: list
        # reference to Patient_Link

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
             'child_entity': 'Patient',
             'child_variable': 'address'},

            {'parent_entity': 'Patient_Animal',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'animal'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient',
             'child_variable': 'generalPractitioner'},

            {'parent_entity': 'Patient_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'link'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'maritalStatus'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'telecom'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'identifier'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'photo'},

            {'parent_entity': 'Patient_Communication',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'communication'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'name'},

            {'parent_entity': 'Patient_Contact',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'contact'},
        ]


class Patient_Contact(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.

    Args:
        relationship: The nature of the relationship between the patient and
            the contact person.
        name: A name associated with the contact person.
        telecom: A contact detail for the person, e.g. a telephone number or
            an email address.
        address: Address for the contact person.
        gender: Administrative Gender - the gender that the contact person is
            considered to have for administration and record keeping purposes.
        organization: Organization on behalf of which the contact is acting or
            for which the contact is working.
        period: The period during which this contact person or organization is
            valid to be contacted relating to this patient.
    """

    __name__ = 'Patient_Contact'

    def __init__(self, dict_values=None):
        self.relationship = None
        # type: list
        # reference to CodeableConcept

        self.name = None
        # reference to HumanName

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.address = None
        # reference to Address

        self.gender = None
        # type: str
        # possible values: male, female, other, unknown

        self.organization = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

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
            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'name'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient_Contact',
             'child_variable': 'organization'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'address'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'relationship'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'telecom'},
        ]


class Patient_Animal(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.

    Args:
        species: Identifies the high level taxonomic categorization of the
            kind of animal.
        breed: Identifies the detailed categorization of the kind of animal.
        genderStatus: Indicates the current state of the animal's reproductive
            organs.
    """

    __name__ = 'Patient_Animal'

    def __init__(self, dict_values=None):
        self.species = None
        # reference to CodeableConcept

        self.breed = None
        # reference to CodeableConcept

        self.genderStatus = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'breed'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'species'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'genderStatus'},
        ]


class Patient_Communication(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.

    Args:
        language: The ISO-639-1 alpha 2 code in lower case for the language,
            optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for
            the region in upper case; e.g. "en" for English, or "en-US" for
            American English versus "en-EN" for England English.
        preferred: Indicates whether or not the patient prefers this language
            (over other languages he masters up a certain level).
    """

    __name__ = 'Patient_Communication'

    def __init__(self, dict_values=None):
        self.language = None
        # reference to CodeableConcept

        self.preferred = None
        # type: bool

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Communication',
             'child_variable': 'language'},
        ]


class Patient_Link(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.

    Args:
        other: The other patient resource that the link refers to.
        type: The type of link between this patient resource and another
            patient resource.
    """

    __name__ = 'Patient_Link'

    def __init__(self, dict_values=None):
        self.other = None
        # reference to Reference: identifier

        self.type = None
        # type: str
        # possible values: replaced-by, replaces, refer, seealso

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'replaced-by', 'replaces', 'refer', 'seealso']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'replaced-by, replaces, refer, seealso'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient_Link',
             'child_variable': 'other'},
        ]
