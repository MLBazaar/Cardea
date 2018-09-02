from .fhirbase import fhirbase


class AppointmentResponse(fhirbase):
    """A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """

    def __init__(self, dict_values=None):
        # this is a appointmentresponse resource
        self.resourceType = 'AppointmentResponse'
        # type = string
        # possible values: AppointmentResponse

        # appointment that this response is replying to.
        self.appointment = None
        # reference to Reference: identifier

        # date/time that the appointment is to take place, or requested new start
        # time.
        self.start = None
        # type = string

        # this may be either the same as the appointment request to confirm the
        # details of the appointment, or alternately a new time to request a re-
        # negotiation of the end time.
        self.end = None
        # type = string

        # role of participant in the appointment.
        self.participantType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a person, location/healthcareservice or device that is participating in
        # the appointment.
        self.actor = None
        # reference to Reference: identifier

        # participation status of the participant. when the status is declined or
        # tentative if the start/end times are different to the appointment, then
        # these times should be interpreted as a requested time change. when the
        # status is accepted, the times can either be the time of the appointment
        # (as a confirmation of the time) or can be empty.
        self.participantStatus = None
        # type = string

        # additional comments about the appointment.
        self.comment = None
        # type = string

        # this records identifiers associated with this appointment response
        # concern that are defined by business processes and/ or used to refer to
        # it when a direct url reference to the resource itself is not
        # appropriate.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'participantType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AppointmentResponse',
             'child_variable': 'appointment'},
        ]
