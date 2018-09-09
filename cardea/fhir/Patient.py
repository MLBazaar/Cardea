from .fhirbase import fhirbase


class Patient(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.
    """

    __name__ = 'Patient'

    def __init__(self, dict_values=None):
        self.resourceType = 'Patient'
        """
        This is a Patient resource

        type: string
        possible values: Patient
        """

        self.active = None
        """
        Whether this patient record is in active use.

        type: boolean
        """

        self.name = None
        """
        A name associated with the individual.

        type: array
        reference to HumanName
        """

        self.telecom = None
        """
        A contact detail (e.g. a telephone number or an email address) by
        which the individual may be contacted.

        type: array
        reference to ContactPoint
        """

        self.gender = None
        """
        Administrative Gender - the gender that the patient is considered to
        have for administration and record keeping purposes.

        type: string
        possible values: male, female, other, unknown
        """

        self.birthDate = None
        """
        The date of birth for the individual.

        type: string
        """

        self.deceasedBoolean = None
        """
        Indicates if the individual is deceased or not.

        type: boolean
        """

        self.deceasedDateTime = None
        """
        Indicates if the individual is deceased or not.

        type: string
        """

        self.address = None
        """
        Addresses for the individual.

        type: array
        reference to Address
        """

        self.maritalStatus = None
        """
        This field contains a patient's most recent marital (civil) status.

        reference to CodeableConcept
        """

        self.multipleBirthBoolean = None
        """
        Indicates whether the patient is part of a multiple (bool) or
        indicates the actual birth order (integer).

        type: boolean
        """

        self.multipleBirthInteger = None
        """
        Indicates whether the patient is part of a multiple (bool) or
        indicates the actual birth order (integer).

        type: int
        """

        self.photo = None
        """
        Image of the patient.

        type: array
        reference to Attachment
        """

        self.contact = None
        """
        A contact party (e.g. guardian, partner, friend) for the patient.

        type: array
        reference to Patient_Contact
        """

        self.animal = None
        """
        This patient is known to be an animal.

        reference to Patient_Animal
        """

        self.communication = None
        """
        Languages which may be used to communicate with the patient about his
        or her health.

        type: array
        reference to Patient_Communication
        """

        self.generalPractitioner = None
        """
        Patient's nominated care provider.

        type: array
        reference to Reference: identifier
        """

        self.managingOrganization = None
        """
        Organization that is the custodian of the patient record.

        reference to Reference: identifier
        """

        self.link = None
        """
        Link to another patient resource that concerns the same actual
        patient.

        type: array
        reference to Patient_Link
        """

        self.identifier = None
        """
        An identifier for this patient.

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'maritalStatus'},

            {'parent_entity': 'Patient_Animal',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'animal'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Patient_Contact',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'contact'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'name'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient',
             'child_variable': 'generalPractitioner'},

            {'parent_entity': 'Patient_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'link'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'telecom'},

            {'parent_entity': 'Patient_Communication',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'communication'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'identifier'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'address'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'photo'},
        ]


class Patient_Contact(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.
    """

    __name__ = 'Patient_Contact'

    def __init__(self, dict_values=None):
        self.relationship = None
        """
        The nature of the relationship between the patient and the contact
        person.

        type: array
        reference to CodeableConcept
        """

        self.name = None
        """
        A name associated with the contact person.

        reference to HumanName
        """

        self.telecom = None
        """
        A contact detail for the person, e.g. a telephone number or an email
        address.

        type: array
        reference to ContactPoint
        """

        self.address = None
        """
        Address for the contact person.

        reference to Address
        """

        self.gender = None
        """
        Administrative Gender - the gender that the contact person is
        considered to have for administration and record keeping purposes.

        type: string
        possible values: male, female, other, unknown
        """

        self.organization = None
        """
        Organization on behalf of which the contact is acting or for which the
        contact is working.

        reference to Reference: identifier
        """

        self.period = None
        """
        The period during which this contact person or organization is valid
        to be contacted relating to this patient.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient_Contact',
             'child_variable': 'organization'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'address'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'telecom'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'name'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'relationship'},
        ]


class Patient_Animal(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.
    """

    __name__ = 'Patient_Animal'

    def __init__(self, dict_values=None):
        self.species = None
        """
        Identifies the high level taxonomic categorization of the kind of
        animal.

        reference to CodeableConcept
        """

        self.breed = None
        """
        Identifies the detailed categorization of the kind of animal.

        reference to CodeableConcept
        """

        self.genderStatus = None
        """
        Indicates the current state of the animal's reproductive organs.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'genderStatus'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'species'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'breed'},
        ]


class Patient_Communication(fhirbase):
    """
    Demographics and other administrative information about an individual
    or animal receiving care or other health-related services.
    """

    __name__ = 'Patient_Communication'

    def __init__(self, dict_values=None):
        self.language = None
        """
        The ISO-639-1 alpha 2 code in lower case for the language, optionally
        followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in
        upper case; e.g. "en" for English, or "en-US" for American English
        versus "en-EN" for England English.

        reference to CodeableConcept
        """

        self.preferred = None
        """
        Indicates whether or not the patient prefers this language (over other
        languages he masters up a certain level).

        type: boolean
        """

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
    """

    __name__ = 'Patient_Link'

    def __init__(self, dict_values=None):
        self.other = None
        """
        The other patient resource that the link refers to.

        reference to Reference: identifier
        """

        self.type = None
        """
        The type of link between this patient resource and another patient
        resource.

        type: string
        possible values: replaced-by, replaces, refer, seealso
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
