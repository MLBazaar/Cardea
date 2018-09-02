from .fhirbase import fhirbase


class Patient(fhirbase):
    """Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    def __init__(self, dict_values=None):
        # this is a patient resource
        self.resourceType = 'Patient'
        # type = string
        # possible values: Patient

        # whether this patient record is in active use.
        self.active = None
        # type = boolean

        # a name associated with the individual.
        self.name = None
        # type = array
        # reference to HumanName: HumanName

        # a contact detail (e.g. a telephone number or an email address) by which
        # the individual may be contacted.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # administrative gender - the gender that the patient is considered to
        # have for administration and record keeping purposes.
        self.gender = None
        # type = string
        # possible values: male, female, other, unknown

        # the date of birth for the individual.
        self.birthDate = None
        # type = string

        # indicates if the individual is deceased or not.
        self.deceasedBoolean = None
        # type = boolean

        # indicates if the individual is deceased or not.
        self.deceasedDateTime = None
        # type = string

        # addresses for the individual.
        self.address = None
        # type = array
        # reference to Address: Address

        # this field contains a patient's most recent marital (civil) status.
        self.maritalStatus = None
        # reference to CodeableConcept: CodeableConcept

        # indicates whether the patient is part of a multiple (bool) or indicates
        # the actual birth order (integer).
        self.multipleBirthBoolean = None
        # type = boolean

        # indicates whether the patient is part of a multiple (bool) or indicates
        # the actual birth order (integer).
        self.multipleBirthInteger = None
        # type = int

        # image of the patient.
        self.photo = None
        # type = array
        # reference to Attachment: Attachment

        # a contact party (e.g. guardian, partner, friend) for the patient.
        self.contact = None
        # type = array
        # reference to Patient_Contact: Patient_Contact

        # this patient is known to be an animal.
        self.animal = None
        # reference to Patient_Animal: Patient_Animal

        # languages which may be used to communicate with the patient about his or
        # her health.
        self.communication = None
        # type = array
        # reference to Patient_Communication: Patient_Communication

        # patient's nominated care provider.
        self.generalPractitioner = None
        # type = array
        # reference to Reference: identifier

        # organization that is the custodian of the patient record.
        self.managingOrganization = None
        # reference to Reference: identifier

        # link to another patient resource that concerns the same actual patient.
        self.link = None
        # type = array
        # reference to Patient_Link: Patient_Link

        # an identifier for this patient.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Patient_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'link'},

            {'parent_entity': 'Patient_Animal',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'animal'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient',
             'child_variable': 'generalPractitioner'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'photo'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'maritalStatus'},

            {'parent_entity': 'Patient_Communication',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'communication'},

            {'parent_entity': 'Patient_Contact',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'contact'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'telecom'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'address'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Patient',
             'child_variable': 'name'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient',
             'child_variable': 'managingOrganization'},
        ]


class Patient_Contact(fhirbase):
    """Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    def __init__(self, dict_values=None):
        # the nature of the relationship between the patient and the contact
        # person.
        self.relationship = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a name associated with the contact person.
        self.name = None
        # reference to HumanName: HumanName

        # a contact detail for the person, e.g. a telephone number or an email
        # address.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # address for the contact person.
        self.address = None
        # reference to Address: Address

        # administrative gender - the gender that the contact person is considered
        # to have for administration and record keeping purposes.
        self.gender = None
        # type = string
        # possible values: male, female, other, unknown

        # organization on behalf of which the contact is acting or for which the
        # contact is working.
        self.organization = None
        # reference to Reference: identifier

        # the period during which this contact person or organization is valid to
        # be contacted relating to this patient.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

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
             'child_entity': 'Patient_Contact',
             'child_variable': 'relationship'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'telecom'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'address'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Patient_Contact',
             'child_variable': 'organization'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'period'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Contact',
             'child_variable': 'name'},
        ]


class Patient_Animal(fhirbase):
    """Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    def __init__(self, dict_values=None):
        # identifies the high level taxonomic categorization of the kind of
        # animal.
        self.species = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the detailed categorization of the kind of animal.
        self.breed = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the current state of the animal's reproductive organs.
        self.genderStatus = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'species'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'breed'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Patient_Animal',
             'child_variable': 'genderStatus'},
        ]


class Patient_Communication(fhirbase):
    """Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    def __init__(self, dict_values=None):
        # the iso-639-1 alpha 2 code in lower case for the language, optionally
        # followed by a hyphen and the iso-3166-1 alpha 2 code for the region in
        # upper case; e.g. "en" for english, or "en-us" for american english
        # versus "en-en" for england english.
        self.language = None
        # reference to CodeableConcept: CodeableConcept

        # indicates whether or not the patient prefers this language (over other
        # languages he masters up a certain level).
        self.preferred = None
        # type = boolean

        # unique identifier for object class
        self.object_id = None

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
    """Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    def __init__(self, dict_values=None):
        # the other patient resource that the link refers to.
        self.other = None
        # reference to Reference: identifier

        # the type of link between this patient resource and another patient
        # resource.
        self.type = None
        # type = string
        # possible values: replaced-by, replaces, refer, seealso

        # unique identifier for object class
        self.object_id = None

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
