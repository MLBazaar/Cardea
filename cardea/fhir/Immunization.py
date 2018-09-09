from .fhirbase import fhirbase


class Immunization(fhirbase):
    """Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    def __init__(self, dict_values=None):
        # this is a immunization resource
        self.resourceType = 'Immunization'
        # type = string
        # possible values: Immunization

        # indicates the current status of the vaccination event.
        self.status = None
        # type = string

        # indicates if the vaccination was or was not given.
        self.notGiven = None
        # type = boolean

        # vaccine that was administered or was to be administered.
        self.vaccineCode = None
        # reference to CodeableConcept: CodeableConcept

        # the patient who either received or did not receive the immunization.
        self.patient = None
        # reference to Reference: identifier

        # the visit or admission or other contact between patient and health care
        # provider the immunization was performed as part of.
        self.encounter = None
        # reference to Reference: identifier

        # date vaccine administered or was to be administered.
        self.date = None
        # type = string

        # an indication that the content of the record is based on information
        # from the person who administered the vaccine. this reflects the context
        # under which the data was originally recorded.
        self.primarySource = None
        # type = boolean

        # the source of the data when the report of the immunization event is not
        # based on information from the person who administered the vaccine.
        self.reportOrigin = None
        # reference to CodeableConcept: CodeableConcept

        # the service delivery location where the vaccine administration occurred.
        self.location = None
        # reference to Reference: identifier

        # name of vaccine manufacturer.
        self.manufacturer = None
        # reference to Reference: identifier

        # lot number of the  vaccine product.
        self.lotNumber = None
        # type = string

        # date vaccine batch expires.
        self.expirationDate = None
        # type = string

        # body site where vaccine was administered.
        self.site = None
        # reference to CodeableConcept: CodeableConcept

        # the path by which the vaccine product is taken into the body.
        self.route = None
        # reference to CodeableConcept: CodeableConcept

        # the quantity of vaccine product that was administered.
        self.doseQuantity = None
        # reference to Quantity: Quantity

        # indicates who or what performed the event.
        self.practitioner = None
        # type = array
        # reference to Immunization_Practitioner: Immunization_Practitioner

        # extra information about the immunization that is not conveyed by the
        # other attributes.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # reasons why a vaccine was or was not administered.
        self.explanation = None
        # reference to Immunization_Explanation: Immunization_Explanation

        # categorical data indicating that an adverse event is associated in time
        # to an immunization.
        self.reaction = None
        # type = array
        # reference to Immunization_Reaction: Immunization_Reaction

        # contains information about the protocol(s) under which the vaccine was
        # administered.
        self.vaccinationProtocol = None
        # type = array
        # reference to Immunization_VaccinationProtocol: Immunization_VaccinationProtocol

        # a unique identifier assigned to this immunization record.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'reportOrigin'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'note'},

            {'parent_entity': 'Immunization_VaccinationProtocol',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'vaccinationProtocol'},

            {'parent_entity': 'Immunization_Reaction',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'reaction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'patient'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'doseQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'site'},

            {'parent_entity': 'Immunization_Practitioner',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'practitioner'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'encounter'},

            {'parent_entity': 'Immunization_Explanation',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'explanation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'manufacturer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'vaccineCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'route'},
        ]


class Immunization_Practitioner(fhirbase):
    """Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    def __init__(self, dict_values=None):
        # describes the type of performance (e.g. ordering provider, administering
        # provider, etc.).
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the device, practitioner, etc. who performed the action.
        self.actor = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_Practitioner',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization_Practitioner',
             'child_variable': 'actor'},
        ]


class Immunization_Explanation(fhirbase):
    """Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    def __init__(self, dict_values=None):
        # reasons why a vaccine was administered.
        self.reason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # reason why a vaccine was not administered.
        self.reasonNotGiven = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_Explanation',
             'child_variable': 'reasonNotGiven'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_Explanation',
             'child_variable': 'reason'},
        ]


class Immunization_Reaction(fhirbase):
    """Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    def __init__(self, dict_values=None):
        # date of reaction to the immunization.
        self.date = None
        # type = string

        # details of the reaction.
        self.detail = None
        # reference to Reference: identifier

        # self-reported indicator.
        self.reported = None
        # type = boolean

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization_Reaction',
             'child_variable': 'detail'},
        ]


class Immunization_VaccinationProtocol(fhirbase):
    """Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """

    def __init__(self, dict_values=None):
        # nominal position in a series.
        self.doseSequence = None
        # type = int

        # contains the description about the protocol under which the vaccine was
        # administered.
        self.description = None
        # type = string

        # indicates the authority who published the protocol.  e.g. acip.
        self.authority = None
        # reference to Reference: identifier

        # one possible path to achieve presumed immunity against a disease -
        # within the context of an authority.
        self.series = None
        # type = string

        # the recommended number of doses to achieve immunity.
        self.seriesDoses = None
        # type = int

        # the targeted disease.
        self.targetDisease = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates if the immunization event should "count" against  the
        # protocol.
        self.doseStatus = None
        # reference to CodeableConcept: CodeableConcept

        # provides an explanation as to why an immunization event should or should
        # not count against the protocol.
        self.doseStatusReason = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'targetDisease'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'doseStatusReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'doseStatus'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'authority'},
        ]
