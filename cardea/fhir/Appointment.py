from .fhirbase import fhirbase


class Appointment(fhirbase):
    """
    A booking of a healthcare event among patient(s), practitioner(s),
    related person(s) and/or device(s) for a specific date/time. This may
    result in one or more Encounter(s).
    """

    __name__ = 'Appointment'

    def __init__(self, dict_values=None):
        self.resourceType = 'Appointment'
        """
        This is a Appointment resource

        type: string
        possible values: Appointment
        """

        self.status = None
        """
        The overall status of the Appointment. Each of the participants has
        their own participation status which indicates their involvement in
        the process, however this status indicates the shared status.

        type: string
        possible values: proposed, pending, booked, arrived,
        fulfilled, cancelled, noshow, entered-in-error
        """

        self.serviceCategory = None
        """
        A broad categorisation of the service that is to be performed during
        this appointment.

        reference to CodeableConcept
        """

        self.serviceType = None
        """
        The specific service that is to be performed during this appointment.

        type: array
        reference to CodeableConcept
        """

        self.specialty = None
        """
        The specialty of a practitioner that would be required to perform the
        service requested in this appointment.

        type: array
        reference to CodeableConcept
        """

        self.appointmentType = None
        """
        The style of appointment or patient that has been booked in the slot
        (not service type).

        reference to CodeableConcept
        """

        self.reason = None
        """
        The reason that this appointment is being scheduled. This is more
        clinical than administrative.

        type: array
        reference to CodeableConcept
        """

        self.indication = None
        """
        Reason the appointment has been scheduled to take place, as specified
        using information from another resource. When the patient arrives and
        the encounter begins it may be used as the admission diagnosis. The
        indication will typically be a Condition (with other resources
        referenced in the evidence.detail), or a Procedure.

        type: array
        reference to Reference: identifier
        """

        self.priority = None
        """
        The priority of the appointment. Can be used to make informed
        decisions if needing to re-prioritize appointments. (The iCal Standard
        specifies 0 as undefined, 1 as highest, 9 as lowest priority).

        type: int
        """

        self.description = None
        """
        The brief description of the appointment as would be shown on a
        subject line in a meeting request, or appointment list. Detailed or
        expanded information should be put in the comment field.

        type: string
        """

        self.supportingInformation = None
        """
        Additional information to support the appointment provided when making
        the appointment.

        type: array
        reference to Reference: identifier
        """

        self.start = None
        """
        Date/Time that the appointment is to take place.

        type: string
        """

        self.end = None
        """
        Date/Time that the appointment is to conclude.

        type: string
        """

        self.minutesDuration = None
        """
        Number of minutes that the appointment is to take. This can be less
        than the duration between the start and end times (where actual time
        of appointment is only an estimate or is a planned appointment
        request).

        type: int
        """

        self.slot = None
        """
        The slots from the participants' schedules that will be filled by the
        appointment.

        type: array
        reference to Reference: identifier
        """

        self.created = None
        """
        The date that this appointment was initially created. This could be
        different to the meta.lastModified value on the initial entry, as this
        could have been before the resource was created on the FHIR server,
        and should remain unchanged over the lifespan of the appointment.

        type: string
        """

        self.comment = None
        """
        Additional comments about the appointment.

        type: string
        """

        self.incomingReferral = None
        """
        The referral request this appointment is allocated to assess (incoming
        referral).

        type: array
        reference to Reference: identifier
        """

        self.participant = None
        """
        List of participants involved in the appointment.

        type: array
        reference to Appointment_Participant
        """

        self.requestedPeriod = None
        """
        A set of date ranges (potentially including times) that the
        appointment is preferred to be scheduled within. When using these
        values, the minutes duration should be provided to indicate the length
        of the appointment to fill and populate the start/end times for the
        actual allocated time.

        type: array
        reference to Period
        """

        self.identifier = None
        """
        This records identifiers associated with this appointment concern that
        are defined by business processes and/or used to refer to it when a
        direct URL reference to the resource itself is not appropriate (e.g.
        in CDA documents, or in written / printed documentation).

        type: array
        reference to Identifier
        """

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'reason'},

            {'parent_entity': 'Appointment_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'participant'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'requestedPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'serviceCategory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'indication'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'slot'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'specialty'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'serviceType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Appointment',
             'child_variable': 'incomingReferral'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Appointment',
             'child_variable': 'appointmentType'},
        ]


class Appointment_Participant(fhirbase):
    """
    A booking of a healthcare event among patient(s), practitioner(s),
    related person(s) and/or device(s) for a specific date/time. This may
    result in one or more Encounter(s).
    """

    __name__ = 'Appointment_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Role of participant in the appointment.

        type: array
        reference to CodeableConcept
        """

        self.actor = None
        """
        A Person, Location/HealthcareService or Device that is participating
        in the appointment.

        reference to Reference: identifier
        """

        self.required = None
        """
        Is this participant required to be present at the meeting. This covers
        a use-case where 2 doctors need to meet to discuss the results for a
        specific patient, and the patient is not required to be present.

        type: string
        possible values: required, optional, information-only
        """

        self.status = None
        """
        Participation status of the actor.

        type: string
        possible values: accepted, declined, tentative, needs-action
        """

        self.object_id = None
        # unique identifier for object class

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
