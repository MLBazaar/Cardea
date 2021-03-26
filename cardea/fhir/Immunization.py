from .fhirbase import fhirbase


class Immunization(fhirbase):
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.

    Args:
        resourceType: This is a Immunization resource
        identifier: A unique identifier assigned to this immunization record.
        status: Indicates the current status of the vaccination event.
        notGiven: Indicates if the vaccination was or was not given.
        vaccineCode: Vaccine that was administered or was to be administered.
        patient: The patient who either received or did not receive the
            immunization.
        encounter: The visit or admission or other contact between patient and
            health care provider the immunization was performed as part of.
        date: Date vaccine administered or was to be administered.
        primarySource: An indication that the content of the record is based
            on information from the person who administered the vaccine. This
            reflects the context under which the data was originally recorded.
        reportOrigin: The source of the data when the report of the
            immunization event is not based on information from the person who
            administered the vaccine.
        location: The service delivery location where the vaccine
            administration occurred.
        manufacturer: Name of vaccine manufacturer.
        lotNumber: Lot number of the  vaccine product.
        expirationDate: Date vaccine batch expires.
        site: Body site where vaccine was administered.
        route: The path by which the vaccine product is taken into the body.
        doseQuantity: The quantity of vaccine product that was administered.
        practitioner: Indicates who or what performed the event.
        note: Extra information about the immunization that is not conveyed by
            the other attributes.
        explanation: Reasons why a vaccine was or was not administered.
        reaction: Categorical data indicating that an adverse event is
            associated in time to an immunization.
        vaccinationProtocol: Contains information about the protocol(s) under
            which the vaccine was administered.
    """

    __name__ = 'Immunization'

    def __init__(self, dict_values=None):
        self.resourceType = 'Immunization'
        # type: str
        # possible values: Immunization

        self.status = None
        # type: str

        self.notGiven = None
        # type: bool

        self.vaccineCode = None
        # reference to CodeableConcept

        self.patient = None
        # reference to Reference: identifier

        self.encounter = None
        # reference to Reference: identifier

        self.date = None
        # type: str

        self.primarySource = None
        # type: bool

        self.reportOrigin = None
        # reference to CodeableConcept

        self.location = None
        # reference to Reference: identifier

        self.manufacturer = None
        # reference to Reference: identifier

        self.lotNumber = None
        # type: str

        self.expirationDate = None
        # type: str

        self.site = None
        # reference to CodeableConcept

        self.route = None
        # reference to CodeableConcept

        self.doseQuantity = None
        # reference to Quantity

        self.practitioner = None
        # type: list
        # reference to Immunization_Practitioner

        self.note = None
        # type: list
        # reference to Annotation

        self.explanation = None
        # reference to Immunization_Explanation

        self.reaction = None
        # type: list
        # reference to Immunization_Reaction

        self.vaccinationProtocol = None
        # type: list
        # reference to Immunization_VaccinationProtocol

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'patient'},

            {'parent_entity': 'Immunization_Explanation',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'explanation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'encounter'},

            {'parent_entity': 'Immunization_Reaction',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'reaction'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'identifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'doseQuantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'location'},

            {'parent_entity': 'Immunization_Practitioner',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'practitioner'},

            {'parent_entity': 'Immunization_VaccinationProtocol',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'vaccinationProtocol'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'note'},

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
             'child_variable': 'reportOrigin'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'route'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'site'},
        ]


class Immunization_Practitioner(fhirbase):
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.

    Args:
        role: Describes the type of performance (e.g. ordering provider,
            administering provider, etc.).
        actor: The device, practitioner, etc. who performed the action.
    """

    __name__ = 'Immunization_Practitioner'

    def __init__(self, dict_values=None):
        self.role = None
        # reference to CodeableConcept

        self.actor = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization_Practitioner',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_Practitioner',
             'child_variable': 'role'},
        ]


class Immunization_Explanation(fhirbase):
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.

    Args:
        reason: Reasons why a vaccine was administered.
        reasonNotGiven: Reason why a vaccine was not administered.
    """

    __name__ = 'Immunization_Explanation'

    def __init__(self, dict_values=None):
        self.reason = None
        # type: list
        # reference to CodeableConcept

        self.reasonNotGiven = None
        # type: list
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

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
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.

    Args:
        date: Date of reaction to the immunization.
        detail: Details of the reaction.
        reported: Self-reported indicator.
    """

    __name__ = 'Immunization_Reaction'

    def __init__(self, dict_values=None):
        self.date = None
        # type: str

        self.detail = None
        # reference to Reference: identifier

        self.reported = None
        # type: bool

        self.object_id = None
        # unique identifier for object class

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
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.

    Args:
        doseSequence: Nominal position in a series.
        description: Contains the description about the protocol under which
            the vaccine was administered.
        authority: Indicates the authority who published the protocol.  E.g.
            ACIP.
        series: One possible path to achieve presumed immunity against a
            disease - within the context of an authority.
        seriesDoses: The recommended number of doses to achieve immunity.
        targetDisease: The targeted disease.
        doseStatus: Indicates if the immunization event should "count" against
            the protocol.
        doseStatusReason: Provides an explanation as to why an immunization
            event should or should not count against the protocol.
    """

    __name__ = 'Immunization_VaccinationProtocol'

    def __init__(self, dict_values=None):
        self.doseSequence = None
        # type: int

        self.description = None
        # type: str

        self.authority = None
        # reference to Reference: identifier

        self.series = None
        # type: str

        self.seriesDoses = None
        # type: int

        self.targetDisease = None
        # type: list
        # reference to CodeableConcept

        self.doseStatus = None
        # reference to CodeableConcept

        self.doseStatusReason = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'doseStatusReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'doseStatus'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'targetDisease'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'authority'},
        ]
