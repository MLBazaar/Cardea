from .fhirbase import fhirbase


class Encounter(fhirbase):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    def __init__(self, dict_values=None):
        # this is a encounter resource
        self.resourceType = 'Encounter'
        # type = string
        # possible values: Encounter

        # planned | arrived | triaged | in-progress | onleave | finished |
        # cancelled +.
        self.status = None
        # type = string
        # possible values: planned, arrived, triaged, in-progress,
        # onleave, finished, cancelled, entered-in-error, unknown

        # the status history permits the encounter resource to contain the status
        # history without needing to read through the historical versions of the
        # resource, or even have the server store them.
        self.statusHistory = None
        # type = array
        # reference to Encounter_StatusHistory: Encounter_StatusHistory

        # inpatient | outpatient | ambulatory | emergency +.
        self._class = None
        # reference to Coding: Coding

        # the class history permits the tracking of the encounters transitions
        # without needing to go  through the resource history.  this would be used
        # for a case where an admission starts of as an emergency encounter, then
        # transisions into an inpatient scenario. doing this and not restarting a
        # new encounter ensures that any lab/diagnostic results can more easily
        # follow the patient and not require re-processing and not get lost or
        # cancelled during a kindof discharge from emergency to inpatient.
        self.classHistory = None
        # type = array
        # reference to Encounter_ClassHistory: Encounter_ClassHistory

        # specific type of encounter (e.g. e-mail consultation, surgical day-care,
        # skilled nursing, rehabilitation).
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates the urgency of the encounter.
        self.priority = None
        # reference to CodeableConcept: CodeableConcept

        # the patient ro group present at the encounter.
        self.subject = None
        # reference to Reference: identifier

        # where a specific encounter should be classified as a part of a specific
        # episode(s) of care this field should be used. this association can
        # facilitate grouping of related encounters together for a specific
        # purpose, such as government reporting, issue tracking, association via a
        # common problem.  the association is recorded on the encounter as these
        # are typically created after the episode of care, and grouped on entry
        # rather than editing the episode of care to append another encounter to
        # it (the episode of care could span years).
        self.episodeOfCare = None
        # type = array
        # reference to Reference: identifier

        # the referral request this encounter satisfies (incoming referral).
        self.incomingReferral = None
        # type = array
        # reference to Reference: identifier

        # the list of people responsible for providing the service.
        self.participant = None
        # type = array
        # reference to Encounter_Participant: Encounter_Participant

        # the appointment that scheduled this encounter.
        self.appointment = None
        # reference to Reference: identifier

        # the start and end time of the encounter.
        self.period = None
        # reference to Period: Period

        # quantity of time the encounter lasted. this excludes the time during
        # leaves of absence.
        self.length = None
        # reference to Duration: Duration

        # reason the encounter takes place, expressed as a code. for admissions,
        # this can be used for a coded admission diagnosis.
        self.reason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the list of diagnosis relevant to this encounter.
        self.diagnosis = None
        # type = array
        # reference to Encounter_Diagnosis: Encounter_Diagnosis

        # the set of accounts that may be used for billing for this encounter.
        self.account = None
        # type = array
        # reference to Reference: identifier

        # details about the admission to a healthcare service.
        self.hospitalization = None
        # reference to Encounter_Hospitalization: Encounter_Hospitalization

        # list of locations where  the patient has been during this encounter.
        self.location = None
        # type = array
        # reference to Encounter_Location: Encounter_Location

        # an organization that is in charge of maintaining the information of this
        # encounter (e.g. who maintains the report or the master service catalog
        # item, etc.). this may be the same as the organization on the patient
        # record, however it could be different. this may not be not the service
        # delivery location's organization.
        self.serviceProvider = None
        # reference to Reference: identifier

        # another encounter of which this encounter is a part of (administratively
        # or in time).
        self.partOf = None
        # reference to Reference: identifier

        # identifier(s) by which this encounter is known.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'planned', 'arrived', 'triaged', 'in-progress', 'onleave', 'finished',
                        'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, arrived, triaged, in-progress, onleave,'
                        'finished, cancelled, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Encounter_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'account'},

            {'parent_entity': 'Encounter_Location',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'location'},

            {'parent_entity': 'Encounter_ClassHistory',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'classHistory'},

            {'parent_entity': 'Encounter_StatusHistory',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'statusHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'appointment'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': '_class'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'episodeOfCare'},

            {'parent_entity': 'Encounter_Hospitalization',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'serviceProvider'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'partOf'},

            {'parent_entity': 'Encounter_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter',
             'child_variable': 'incomingReferral'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'priority'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'type'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'length'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter',
             'child_variable': 'reason'},
        ]


class Encounter_StatusHistory(fhirbase):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    def __init__(self, dict_values=None):
        # planned | arrived | triaged | in-progress | onleave | finished |
        # cancelled +.
        self.status = None
        # type = string
        # possible values: planned, arrived, triaged, in-progress,
        # onleave, finished, cancelled, entered-in-error, unknown

        # the time that the episode was in the specified status.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'planned', 'arrived', 'triaged', 'in-progress', 'onleave', 'finished',
                        'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, arrived, triaged, in-progress, onleave, finished,'
                        'cancelled, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_StatusHistory',
             'child_variable': 'period'},
        ]


class Encounter_ClassHistory(fhirbase):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    def __init__(self, dict_values=None):
        # inpatient | outpatient | ambulatory | emergency +.
        self._class = None
        # reference to Coding: Coding

        # the time that the episode was in the specified class.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

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
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    def __init__(self, dict_values=None):
        # role of participant in encounter.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the period of time that the specified participant participated in the
        # encounter. these can overlap or be sub-sets of the overall encounter's
        # period.
        self.period = None
        # reference to Period: Period

        # persons involved in the encounter other than the patient.
        self.individual = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Participant',
             'child_variable': 'individual'},
        ]


class Encounter_Diagnosis(fhirbase):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    def __init__(self, dict_values=None):
        # reason the encounter takes place, as specified using information from
        # another resource. for admissions, this is the admission diagnosis. the
        # indication will typically be a condition (with other resources
        # referenced in the evidence.detail), or a procedure.
        self.condition = None
        # reference to Reference: identifier

        # role that this diagnosis has within the encounter (e.g. admission,
        # billing, discharge …).
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # ranking of the diagnosis (for each role type).
        self.rank = None
        # type = int

        # unique identifier for object class
        self.object_id = None

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
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    def __init__(self, dict_values=None):
        # pre-admission identifier.
        self.preAdmissionIdentifier = None
        # reference to Identifier: Identifier

        # the location from which the patient came before admission.
        self.origin = None
        # reference to Reference: identifier

        # from where patient was admitted (physician referral, transfer).
        self.admitSource = None
        # reference to CodeableConcept: CodeableConcept

        # whether this hospitalization is a readmission and why if known.
        self.reAdmission = None
        # reference to CodeableConcept: CodeableConcept

        # diet preferences reported by the patient.
        self.dietPreference = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # special courtesies (vip, board member).
        self.specialCourtesy = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # any special requests that have been made for this hospitalization
        # encounter, such as the provision of specific equipment or other things.
        self.specialArrangement = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # location to which the patient is discharged.
        self.destination = None
        # reference to Reference: identifier

        # category or kind of location after discharge.
        self.dischargeDisposition = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'specialArrangement'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'dischargeDisposition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'origin'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'reAdmission'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'specialCourtesy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'admitSource'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'dietPreference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'preAdmissionIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Hospitalization',
             'child_variable': 'destination'},
        ]


class Encounter_Location(fhirbase):
    """An interaction between a patient and healthcare provider(s) for the
    purpose of providing healthcare service(s) or assessing the health
    status of a patient.
    """

    def __init__(self, dict_values=None):
        # the location where the encounter takes place.
        self.location = None
        # reference to Reference: identifier

        # the status of the participants' presence at the specified location
        # during the period specified. if the participant is is no longer at the
        # location, then the period will have an end date/time.
        self.status = None
        # type = string
        # possible values: planned, active, reserved, completed

        # time period during which the patient was present at the location.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

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
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Encounter_Location',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Encounter_Location',
             'child_variable': 'location'},
        ]
