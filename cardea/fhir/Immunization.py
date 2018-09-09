from .fhirbase import fhirbase


class Immunization(fhirbase):
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.
    """

    __name__ = 'Immunization'

    def __init__(self, dict_values=None):
        self.resourceType = 'Immunization'
        """
        This is a Immunization resource

        type: string
        possible values: Immunization
        """

        self.status = None
        """
        Indicates the current status of the vaccination event.

        type: string
        """

        self.notGiven = None
        """
        Indicates if the vaccination was or was not given.

        type: boolean
        """

        self.vaccineCode = None
        """
        Vaccine that was administered or was to be administered.

        reference to CodeableConcept
        """

        self.patient = None
        """
        The patient who either received or did not receive the immunization.

        reference to Reference: identifier
        """

        self.encounter = None
        """
        The visit or admission or other contact between patient and health
        care provider the immunization was performed as part of.

        reference to Reference: identifier
        """

        self.date = None
        """
        Date vaccine administered or was to be administered.

        type: string
        """

        self.primarySource = None
        """
        An indication that the content of the record is based on information
        from the person who administered the vaccine. This reflects the
        context under which the data was originally recorded.

        type: boolean
        """

        self.reportOrigin = None
        """
        The source of the data when the report of the immunization event is
        not based on information from the person who administered the vaccine.

        reference to CodeableConcept
        """

        self.location = None
        """
        The service delivery location where the vaccine administration
        occurred.

        reference to Reference: identifier
        """

        self.manufacturer = None
        """
        Name of vaccine manufacturer.

        reference to Reference: identifier
        """

        self.lotNumber = None
        """
        Lot number of the  vaccine product.

        type: string
        """

        self.expirationDate = None
        """
        Date vaccine batch expires.

        type: string
        """

        self.site = None
        """
        Body site where vaccine was administered.

        reference to CodeableConcept
        """

        self.route = None
        """
        The path by which the vaccine product is taken into the body.

        reference to CodeableConcept
        """

        self.doseQuantity = None
        """
        The quantity of vaccine product that was administered.

        reference to Quantity
        """

        self.practitioner = None
        """
        Indicates who or what performed the event.

        type: array
        reference to Immunization_Practitioner
        """

        self.note = None
        """
        Extra information about the immunization that is not conveyed by the
        other attributes.

        type: array
        reference to Annotation
        """

        self.explanation = None
        """
        Reasons why a vaccine was or was not administered.

        reference to Immunization_Explanation
        """

        self.reaction = None
        """
        Categorical data indicating that an adverse event is associated in
        time to an immunization.

        type: array
        reference to Immunization_Reaction
        """

        self.vaccinationProtocol = None
        """
        Contains information about the protocol(s) under which the vaccine was
        administered.

        type: array
        reference to Immunization_VaccinationProtocol
        """

        self.identifier = None
        """
        A unique identifier assigned to this immunization record.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'vaccineCode'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'doseQuantity'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'site'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'identifier'},

            {'parent_entity': 'Immunization_Practitioner',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'practitioner'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'manufacturer'},

            {'parent_entity': 'Immunization_Explanation',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'explanation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'route'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'reportOrigin'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'patient'},

            {'parent_entity': 'Immunization_VaccinationProtocol',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'vaccinationProtocol'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'encounter'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Immunization',
             'child_variable': 'location'},

            {'parent_entity': 'Immunization_Reaction',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization',
             'child_variable': 'reaction'},
        ]


class Immunization_Practitioner(fhirbase):
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.
    """

    __name__ = 'Immunization_Practitioner'

    def __init__(self, dict_values=None):
        self.role = None
        """
        Describes the type of performance (e.g. ordering provider,
        administering provider, etc.).

        reference to CodeableConcept
        """

        self.actor = None
        """
        The device, practitioner, etc. who performed the action.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.
    """

    __name__ = 'Immunization_Explanation'

    def __init__(self, dict_values=None):
        self.reason = None
        """
        Reasons why a vaccine was administered.

        type: array
        reference to CodeableConcept
        """

        self.reasonNotGiven = None
        """
        Reason why a vaccine was not administered.

        type: array
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
             'child_entity': 'Immunization_Explanation',
             'child_variable': 'reason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_Explanation',
             'child_variable': 'reasonNotGiven'},
        ]


class Immunization_Reaction(fhirbase):
    """
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or
    another party and may include vaccine reaction information and what
    vaccination protocol was followed.
    """

    __name__ = 'Immunization_Reaction'

    def __init__(self, dict_values=None):
        self.date = None
        """
        Date of reaction to the immunization.

        type: string
        """

        self.detail = None
        """
        Details of the reaction.

        reference to Reference: identifier
        """

        self.reported = None
        """
        Self-reported indicator.

        type: boolean
        """

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
    """

    __name__ = 'Immunization_VaccinationProtocol'

    def __init__(self, dict_values=None):
        self.doseSequence = None
        """
        Nominal position in a series.

        type: int
        """

        self.description = None
        """
        Contains the description about the protocol under which the vaccine
        was administered.

        type: string
        """

        self.authority = None
        """
        Indicates the authority who published the protocol.  E.g. ACIP.

        reference to Reference: identifier
        """

        self.series = None
        """
        One possible path to achieve presumed immunity against a disease -
        within the context of an authority.

        type: string
        """

        self.seriesDoses = None
        """
        The recommended number of doses to achieve immunity.

        type: int
        """

        self.targetDisease = None
        """
        The targeted disease.

        type: array
        reference to CodeableConcept
        """

        self.doseStatus = None
        """
        Indicates if the immunization event should "count" against  the
        protocol.

        reference to CodeableConcept
        """

        self.doseStatusReason = None
        """
        Provides an explanation as to why an immunization event should or
        should not count against the protocol.

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

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Immunization_VaccinationProtocol',
             'child_variable': 'targetDisease'},
        ]
