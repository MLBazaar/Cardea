from .fhirbase import fhirbase


class Encounter(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    __name__ = 'Encounter'

    def __init__(self, dict_values=None):
        self.resourceType = 'Encounter'
        """
        This is a Encounter resource

        type: string
        possible values: Encounter
        """

        self.status = None
        """
        planned | arrived | triaged | in-progress | onleave | finished |
        cancelled +.

        type: string
        possible values: planned, arrived, triaged, in-progress,
        onleave, finished, cancelled, entered-in-error, unknown
        """

        self.statusHistory = None
        """
        The status history permits the encounter resource to contain the
        status history without needing to read through the historical versions
        of the resource, or even have the server store them.

        type: array
        reference to Encounter_StatusHistory
        """

        self._class = None
        """
        inpatient | outpatient | ambulatory | emergency +.

        reference to Coding
        """

        self.classHistory = None
        """
        The class history permits the tracking of the encounters transitions
        without needing to go  through the resource history.  This would be
        used for a case where an admission starts of as an emergency
        encounter, then transisions into an inpatient scenario. Doing this and
        not restarting a new encounter ensures that any lab/diagnostic results
        can more easily follow the patient and not require re-processing and
        not get lost or cancelled during a kindof discharge from emergency to
        inpatient.

        type: array
        reference to Encounter_ClassHistory
        """

        self.type = None
        """
        Specific type of encounter (e.g. e-mail consultation, surgical
        day-care, skilled nursing, rehabilitation).

        type: array
        reference to CodeableConcept
        """

        self.priority = None
        """
        Indicates the urgency of the encounter.

        reference to CodeableConcept
        """

        self.subject = None
        """
        The patient ro group present at the encounter.

        reference to Reference: identifier
        """

        self.episodeOfCare = None
        """
        Where a specific encounter should be classified as a part of a
        specific episode(s) of care this field should be used. This
        association can facilitate grouping of related encounters together for
        a specific purpose, such as government reporting, issue tracking,
        association via a common problem.  The association is recorded on the
        encounter as these are typically created after the episode of care,
        and grouped on entry rather than editing the episode of care to append
        another encounter to it (the episode of care could span years).

        type: array
        reference to Reference: identifier
        """

        self.incomingReferral = None
        """
        The referral request this encounter satisfies (incoming referral).

        type: array
        reference to Reference: identifier
        """

        self.participant = None
        """
        The list of people responsible for providing the service.

        type: array
        reference to Encounter_Participant
        """

        self.appointment = None
        """
        The appointment that scheduled this encounter.

        reference to Reference: identifier
        """

        self.period = None
        """
        The start and end time of the encounter.

        reference to Period
        """

        self.length = None
        """
        Quantity of time the encounter lasted. This excludes the time during
        leaves of absence.

        reference to Duration
        """

        self.reason = None
        """
        Reason the encounter takes place, expressed as a code. For admissions,
        this can be used for a coded admission diagnosis.

        type: array
        reference to CodeableConcept
        """

        self.diagnosis = None
        """
        The list of diagnosis relevant to this encounter.

        type: array
        reference to Encounter_Diagnosis
        """

        self.account = None
        """
        The set of accounts that may be used for billing for this Encounter.

        type: array
        reference to Reference: identifier
        """

        self.hospitalization = None
        """
        Details about the admission to a healthcare service.

        reference to Encounter_Hospitalization
        """

        self.location = None
        """
        List of locations where  the patient has been during this encounter.

        type: array
        reference to Encounter_Location
        """

        self.serviceProvider = None
        """
        An organization that is in charge of maintaining the information of
        this Encounter (e.g. who maintains the report or the master service
        catalog item, etc.). This MAY be the same as the organization on the
        Patient record, however it could be different. This MAY not be not the
        Service Delivery Location's Organization.

        reference to Reference: identifier
        """

        self.partOf = None
        """
        Another Encounter of which this encounter is a part of
        (administratively or in time).

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifier(s) by which this encounter is known.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'partOf'},

            {'parent_entity': 'Encounter_Hospitalization',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'length'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': '_class'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'priority'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'type'},

            {'parent_entity': 'Encounter_ClassHistory',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'classHistory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'reason'},

            {'parent_entity': 'Encounter_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'account'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'period'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'identifier'},

            {'parent_entity': 'Encounter_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'episodeOfCare'},

            {'parent_entity': 'Encounter_Location',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'location'},

            {'parent_entity': 'Encounter_StatusHistory',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'statusHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'appointment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'incomingReferral'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'serviceProvider'},
        ]


class Encounter_StatusHistory(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    __name__ = 'Encounter_StatusHistory'

    def __init__(self, dict_values=None):
        self.status = None
        """
        planned | arrived | triaged | in-progress | onleave | finished |
        cancelled +.

        type: string
        possible values: planned, arrived, triaged, in-progress,
        onleave, finished, cancelled, entered-in-error, unknown
        """

        self.period = None
        """
        The time that the episode was in the specified status.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
    """

    __name__ = 'Encounter_ClassHistory'

    def __init__(self, dict_values=None):
        self._class = None
        """
        inpatient | outpatient | ambulatory | emergency +.

        reference to Coding
        """

        self.period = None
        """
        The time that the episode was in the specified class.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_ClassHistory',
             'child_variable': 'period'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_ClassHistory',
             'child_variable': '_class'},
        ]


class Encounter_Participant(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    __name__ = 'Encounter_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Role of participant in encounter.

        type: array
        reference to CodeableConcept
        """

        self.period = None
        """
        The period of time that the specified participant participated in the
        encounter. These can overlap or be sub-sets of the overall encounter's
        period.

        reference to Period
        """

        self.individual = None
        """
        Persons involved in the encounter other than the patient.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'individual'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'type'},

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
    """

    __name__ = 'Encounter_Diagnosis'

    def __init__(self, dict_values=None):
        self.condition = None
        """
        Reason the encounter takes place, as specified using information from
        another resource. For admissions, this is the admission diagnosis. The
        indication will typically be a Condition (with other resources
        referenced in the evidence.detail), or a Procedure.

        reference to Reference: identifier
        """

        self.role = None
        """
        Role that this diagnosis has within the encounter (e.g. admission,
        billing, discharge …).

        reference to CodeableConcept
        """

        self.rank = None
        """
        Ranking of the diagnosis (for each role type).

        type: int
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Diagnosis',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Diagnosis',
             'child_variable': 'condition'},
        ]


class Encounter_Hospitalization(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    __name__ = 'Encounter_Hospitalization'

    def __init__(self, dict_values=None):
        self.preAdmissionIdentifier = None
        """
        Pre-admission identifier.

        reference to Identifier
        """

        self.origin = None
        """
        The location from which the patient came before admission.

        reference to Reference: identifier
        """

        self.admitSource = None
        """
        From where patient was admitted (physician referral, transfer).

        reference to CodeableConcept
        """

        self.reAdmission = None
        """
        Whether this hospitalization is a readmission and why if known.

        reference to CodeableConcept
        """

        self.dietPreference = None
        """
        Diet preferences reported by the patient.

        type: array
        reference to CodeableConcept
        """

        self.specialCourtesy = None
        """
        Special courtesies (VIP, board member).

        type: array
        reference to CodeableConcept
        """

        self.specialArrangement = None
        """
        Any special requests that have been made for this hospitalization
        encounter, such as the provision of specific equipment or other
        things.

        type: array
        reference to CodeableConcept
        """

        self.destination = None
        """
        Location to which the patient is discharged.

        reference to Reference: identifier
        """

        self.dischargeDisposition = None
        """
        Category or kind of location after discharge.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
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
             'child_variable': 'reAdmission'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'dietPreference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'origin'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'destination'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'specialArrangement'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'dischargeDisposition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'admitSource'},
        ]


class Encounter_Location(fhirbase):
    """
    An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    __name__ = 'Encounter_Location'

    def __init__(self, dict_values=None):
        self.location = None
        """
        The location where the encounter takes place.

        reference to Reference: identifier
        """

        self.status = None
        """
        The status of the participants' presence at the specified location
        during the period specified. If the participant is is no longer at the
        location, then the period will have an end date/time.

        type: string
        possible values: planned, active, reserved, completed
        """

        self.period = None
        """
        Time period during which the patient was present at the location.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'planned', 'active', 'reserved', 'completed']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, active, reserved, completed'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Location',
             'child_variable': 'location'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Location',
             'child_variable': 'period'},
        ]
