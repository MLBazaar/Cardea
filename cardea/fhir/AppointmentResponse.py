from .fhirbase import fhirbase


class AppointmentResponse(fhirbase):
    """
    A reply to an appointment request for a patient and/or
    practitioner(s), such as a confirmation or rejection.
    """

    __name__ = 'AppointmentResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'AppointmentResponse'
        """
        This is a AppointmentResponse resource

        type: string
        possible values: AppointmentResponse
        """

        self.appointment = None
        """
        Appointment that this response is replying to.

        reference to Reference: identifier
        """

        self.start = None
        """
        Date/Time that the appointment is to take place, or requested new
        start time.

        type: string
        """

        self.end = None
        """
        This may be either the same as the appointment request to confirm the
        details of the appointment, or alternately a new time to request a
        re-negotiation of the end time.

        type: string
        """

        self.participantType = None
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

        self.participantStatus = None
        """
        Participation status of the participant. When the status is declined
        or tentative if the start/end times are different to the appointment,
        then these times should be interpreted as a requested time change.
        When the status is accepted, the times can either be the time of the
        appointment (as a confirmation of the time) or can be empty.

        type: string
        """

        self.comment = None
        """
        Additional comments about the appointment.

        type: string
        """

        self.identifier = None
        """
        This records identifiers associated with this appointment response
        concern that are defined by business processes and/ or used to refer
        to it when a direct URL reference to the resource itself is not
        appropriate.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'participantType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'actor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'appointment'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'identifier'},
        ]
