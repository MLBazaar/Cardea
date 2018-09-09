from .fhirbase import fhirbase


class Appointment(fhirbase):
    """A booking of a healthcare event among patient(s), practitioner(s),
    related person(s) and/or device(s) for a specific date/time. This may
    result in one or more Encounter(s).
    """

    __name__ = 'Appointment'

    def __init__(self, dict_values=None):
        # this is a appointment resource
        self.resourceType = 'Appointment'
        # type = string
        # possible values: Appointment

        # the overall status of the appointment. each of the participants has
        # their own participation status which indicates their involvement in the
        # process, however this status indicates the shared status.
        self.status = None
        # type = string
        # possible values: proposed, pending, booked, arrived,
        # fulfilled, cancelled, noshow, entered-in-error

        # a broad categorisation of the service that is to be performed during
        # this appointment.
        self.serviceCategory = None
        # reference to CodeableConcept: CodeableConcept

        # the specific service that is to be performed during this appointment.
        self.serviceType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the specialty of a practitioner that would be required to perform the
        # service requested in this appointment.
        self.specialty = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the style of appointment or patient that has been booked in the slot
        # (not service type).
        self.appointmentType = None
        # reference to CodeableConcept: CodeableConcept

        # the reason that this appointment is being scheduled. this is more
        # clinical than administrative.
        self.reason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # reason the appointment has been scheduled to take place, as specified
        # using information from another resource. when the patient arrives and
        # the encounter begins it may be used as the admission diagnosis. the
        # indication will typically be a condition (with other resources
        # referenced in the evidence.detail), or a procedure.
        self.indication = None
        # type = array
        # reference to Reference: identifier

        # the priority of the appointment. can be used to make informed decisions
        # if needing to re-prioritize appointments. (the ical standard specifies 0
        # as undefined, 1 as highest, 9 as lowest priority).
        self.priority = None
        # type = int

        # the brief description of the appointment as would be shown on a subject
        # line in a meeting request, or appointment list. detailed or expanded
        # information should be put in the comment field.
        self.description = None
        # type = string

        # additional information to support the appointment provided when making
        # the appointment.
        self.supportingInformation = None
        # type = array
        # reference to Reference: identifier

        # date/time that the appointment is to take place.
        self.start = None
        # type = string

        # date/time that the appointment is to conclude.
        self.end = None
        # type = string

        # number of minutes that the appointment is to take. this can be less than
        # the duration between the start and end times (where actual time of
        # appointment is only an estimate or is a planned appointment request).
        self.minutesDuration = None
        # type = int

        # the slots from the participants' schedules that will be filled by the
        # appointment.
        self.slot = None
        # type = array
        # reference to Reference: identifier

        # the date that this appointment was initially created. this could be
        # different to the meta.lastmodified value on the initial entry, as this
        # could have been before the resource was created on the fhir server, and
        # should remain unchanged over the lifespan of the appointment.
        self.created = None
        # type = string

        # additional comments about the appointment.
        self.comment = None
        # type = string

        # the referral request this appointment is allocated to assess (incoming
        # referral).
        self.incomingReferral = None
        # type = array
        # reference to Reference: identifier

        # list of participants involved in the appointment.
        self.participant = None
        # type = array
        # reference to Appointment_Participant: Appointment_Participant

        # a set of date ranges (potentially including times) that the appointment
        # is preferred to be scheduled within. when using these values, the
        # minutes duration should be provided to indicate the length of the
        # appointment to fill and populate the start/end times for the actual
        # allocated time.
        self.requestedPeriod = None
        # type = array
        # reference to Period: Period

        # this records identifiers associated with this appointment concern that
        # are defined by business processes and/or used to refer to it when a
        # direct url reference to the resource itself is not appropriate (e.g. in
        # cda documents, or in written / printed documentation).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'proposed', 'pending', 'booked', 'arrived', 'fulfilled', 'cancelled',
                        'noshow', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposed, pending, booked, arrived, fulfilled, cancelled, noshow,'
                        'entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'slot'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'requestedPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'specialty'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'reason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'appointmentType'},

            {'parent_entity': 'Appointment_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'participant'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'serviceCategory'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'incomingReferral'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'serviceType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'indication'},
        ]


class Appointment_Participant(fhirbase):
    """A booking of a healthcare event among patient(s), practitioner(s),
    related person(s) and/or device(s) for a specific date/time. This may
    result in one or more Encounter(s).
    """

    __name__ = 'Appointment_Participant'

    def __init__(self, dict_values=None):
        # role of participant in the appointment.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a person, location/healthcareservice or device that is participating in
        # the appointment.
        self.actor = None
        # reference to Reference: identifier

        # is this participant required to be present at the meeting. this covers a
        # use-case where 2 doctors need to meet to discuss the results for a
        # specific patient, and the patient is not required to be present.
        self.required = None
        # type = string
        # possible values: required, optional, information-only

        # participation status of the actor.
        self.status = None
        # type = string
        # possible values: accepted, declined, tentative, needs-action

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.required is not None:
            for value in self.required:
                if value is not None and value.lower() not in [
                        'required', 'optional', 'information-only']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'required, optional, information-only'))

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'accepted', 'declined', 'tentative', 'needs-action']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'accepted, declined, tentative, needs-action'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment_Participant',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment_Participant',
             'child_variable': 'type'},
        ]
