from .fhirbase import fhirbase


class Encounter(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.

    Args:
        resourceType: This is a Encounter resource
        identifier: Identifier(s) by which this encounter is known.
        status: planned | arrived | triaged | in-progress | onleave | finished
            | cancelled +.
        statusHistory: The status history permits the encounter resource to
            contain the status history without needing to read through the
            historical versions of the resource, or even have the server store
            them.
        class: inpatient | outpatient | ambulatory | emergency +.
        classHistory: The class history permits the tracking of the encounters
            transitions without needing to go  through the resource history.  This
            would be used for a case where an admission starts of as an emergency
            encounter, then transisions into an inpatient scenario. Doing this and
            not restarting a new encounter ensures that any lab/diagnostic results
            can more easily follow the patient and not require re-processing and
            not get lost or cancelled during a kindof discharge from emergency to
            inpatient.
        type: Specific type of encounter (e.g. e-mail consultation, surgical
            day-care, skilled nursing, rehabilitation).
        priority: Indicates the urgency of the encounter.
        subject: The patient ro group present at the encounter.
        episodeOfCare: Where a specific encounter should be classified as a
            part of a specific episode(s) of care this field should be used. This
            association can facilitate grouping of related encounters together for
            a specific purpose, such as government reporting, issue tracking,
            association via a common problem.  The association is recorded on the
            encounter as these are typically created after the episode of care,
            and grouped on entry rather than editing the episode of care to append
            another encounter to it (the episode of care could span years).
        incomingReferral: The referral request this encounter satisfies
            (incoming referral).
        participant: The list of people responsible for providing the service.
        appointment: The appointment that scheduled this encounter.
        period: The start and end time of the encounter.
        length: Quantity of time the encounter lasted. This excludes the time
            during leaves of absence.
        reason: Reason the encounter takes place, expressed as a code. For
            admissions, this can be used for a coded admission diagnosis.
        diagnosis: The list of diagnosis relevant to this encounter.
        account: The set of accounts that may be used for billing for this
            Encounter.
        hospitalization: Details about the admission to a healthcare service.
        location: List of locations where  the patient has been during this
            encounter.
        serviceProvider: An organization that is in charge of maintaining the
            information of this Encounter (e.g. who maintains the report or the
            master service catalog item, etc.). This MAY be the same as the
            organization on the Patient record, however it could be different.
            This MAY not be not the Service Delivery Location's Organization.
        partOf: Another Encounter of which this encounter is a part of
            (administratively or in time).
    """

    __name__ = 'Encounter'

    def __init__(self, dict_values=None):
        self.resourceType = 'Encounter'
        # type: str
        # possible values: Encounter

        self.status = None
        # type: str
        # possible values: planned, arrived, triaged, in-progress,
        # onleave, finished, cancelled, entered-in-error, unknown

        self.statusHistory = None
        # type: list
        # reference to Encounter_StatusHistory

        self._class = None
        # reference to Coding

        self.classHistory = None
        # type: list
        # reference to Encounter_ClassHistory

        self.type = None
        # type: list
        # reference to CodeableConcept

        self.priority = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.episodeOfCare = None
        # type: list
        # reference to Reference: identifier

        self.incomingReferral = None
        # type: list
        # reference to Reference: identifier

        self.participant = None
        # type: list
        # reference to Encounter_Participant

        self.appointment = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.length = None
        # reference to Duration

        self.reason = None
        # type: list
        # reference to CodeableConcept

        self.diagnosis = None
        # type: list
        # reference to Encounter_Diagnosis

        self.account = None
        # type: list
        # reference to Reference: identifier

        self.hospitalization = None
        # reference to Encounter_Hospitalization

        self.location = None
        # type: list
        # reference to Encounter_Location

        self.serviceProvider = None
        # reference to Reference: identifier

        self.partOf = None
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'planned', 'arrived', 'triaged', 'in-progress', 'onleave', 'finished',
                        'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, arrived, triaged, in-progress, onleave, finished, '
                        'cancelled, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'incomingReferral'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'episodeOfCare'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': '_class'},

            {'parent_entity': 'Encounter_ClassHistory',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'classHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'reason'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'length'},

            {'parent_entity': 'Encounter_StatusHistory',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'statusHistory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'type'},

            {'parent_entity': 'Encounter_Location',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'subject'},

            {'parent_entity': 'Encounter_Hospitalization',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'priority'},

            {'parent_entity': 'Encounter_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'serviceProvider'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'account'},

            {'parent_entity': 'Encounter_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'appointment'},
        ]


class Encounter_StatusHistory(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.

    Args:
        status: planned | arrived | triaged | in-progress | onleave | finished
            | cancelled +.
        period: The time that the episode was in the specified status.
    """

    __name__ = 'Encounter_StatusHistory'

    def __init__(self, dict_values=None):
        self.status = None
        # type: str
        # possible values: planned, arrived, triaged, in-progress,
        # onleave, finished, cancelled, entered-in-error, unknown

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'planned', 'arrived', 'triaged', 'in-progress', 'onleave', 'finished',
                        'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, arrived, triaged, in-progress, onleave, finished, '
                        'cancelled, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_StatusHistory',
             'child_variable': 'period'},
        ]


class Encounter_ClassHistory(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.

    Args:
        class: inpatient | outpatient | ambulatory | emergency +.
        period: The time that the episode was in the specified class.
    """

    __name__ = 'Encounter_ClassHistory'

    def __init__(self, dict_values=None):
        self._class = None
        # reference to Coding

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_ClassHistory',
             'child_variable': '_class'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_ClassHistory',
             'child_variable': 'period'},
        ]


class Encounter_Participant(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.

    Args:
        type: Role of participant in encounter.
        period: The period of time that the specified participant participated
            in the encounter. These can overlap or be sub-sets of the overall
            encounter's period.
        individual: Persons involved in the encounter other than the patient.
    """

    __name__ = 'Encounter_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        # type: list
        # reference to CodeableConcept

        self.period = None
        # reference to Period

        self.individual = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'individual'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'period'},
        ]


class Encounter_Diagnosis(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.

    Args:
        condition: Reason the encounter takes place, as specified using
            information from another resource. For admissions, this is the
            admission diagnosis. The indication will typically be a Condition
            (with other resources referenced in the evidence.detail), or a
            Procedure.
        role: Role that this diagnosis has within the encounter (e.g.
            admission, billing, discharge …).
        rank: Ranking of the diagnosis (for each role type).
    """

    __name__ = 'Encounter_Diagnosis'

    def __init__(self, dict_values=None):
        self.condition = None
        # reference to Reference: identifier

        self.role = None
        # reference to CodeableConcept

        self.rank = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Diagnosis',
             'child_variable': 'condition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Diagnosis',
             'child_variable': 'role'},
        ]


class Encounter_Hospitalization(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.

    Args:
        preAdmissionIdentifier: Pre-admission identifier.
        origin: The location from which the patient came before admission.
        admitSource: From where patient was admitted (physician referral,
            transfer).
        reAdmission: Whether this hospitalization is a readmission and why if
            known.
        dietPreference: Diet preferences reported by the patient.
        specialCourtesy: Special courtesies (VIP, board member).
        specialArrangement: Any special requests that have been made for this
            hospitalization encounter, such as the provision of specific equipment
            or other things.
        destination: Location to which the patient is discharged.
        dischargeDisposition: Category or kind of location after discharge.
    """

    __name__ = 'Encounter_Hospitalization'

    def __init__(self, dict_values=None):
        self.preAdmissionIdentifier = None
        # reference to Identifier

        self.origin = None
        # reference to Reference: identifier

        self.admitSource = None
        # reference to CodeableConcept

        self.reAdmission = None
        # reference to CodeableConcept

        self.dietPreference = None
        # type: list
        # reference to CodeableConcept

        self.specialCourtesy = None
        # type: list
        # reference to CodeableConcept

        self.specialArrangement = None
        # type: list
        # reference to CodeableConcept

        self.destination = None
        # reference to Reference: identifier

        self.dischargeDisposition = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'admitSource'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'preAdmissionIdentifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'specialCourtesy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'specialArrangement'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'reAdmission'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'destination'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'dietPreference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'dischargeDisposition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'origin'},
        ]


class Encounter_Location(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.

    Args:
        location: The location where the encounter takes place.
        status: The status of the participants' presence at the specified
            location during the period specified. If the participant is is no
            longer at the location, then the period will have an end date/time.
        period: Time period during which the patient was present at the
            location.
    """

    __name__ = 'Encounter_Location'

    def __init__(self, dict_values=None):
        self.location = None
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: planned, active, reserved, completed

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'planned', 'active', 'reserved', 'completed']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, active, reserved, completed'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Location',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Location',
             'child_variable': 'location'},
        ]
