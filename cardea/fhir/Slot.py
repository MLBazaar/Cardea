from .fhirbase import fhirbase


class Slot(fhirbase):
    """
    A slot of time on a schedule that may be available for booking
    appointments.

    Args:
        resourceType: This is a Slot resource
        identifier: External Ids for this item.
        serviceCategory: A broad categorisation of the service that is to be
            performed during this appointment.
        serviceType: The type of appointments that can be booked into this
            slot (ideally this would be an identifiable service - which is at a
            location, rather than the location itself). If provided then this
            overrides the value provided on the availability resource.
        specialty: The specialty of a practitioner that would be required to
            perform the service requested in this appointment.
        appointmentType: The style of appointment or patient that may be
            booked in the slot (not service type).
        schedule: The schedule resource that this slot defines an interval of
            status information.
        status: busy | free | busy-unavailable | busy-tentative |
            entered-in-error.
        start: Date/Time that the slot is to begin.
        end: Date/Time that the slot is to conclude.
        overbooked: This slot has already been overbooked, appointments are
            unlikely to be accepted for this time.
        comment: Comments on the slot to describe any extended information.
            Such as custom constraints on the slot.
    """

    __name__ = 'Slot'

    def __init__(self, dict_values=None):
        self.resourceType = 'Slot'
        # type: str
        # possible values: Slot

        self.serviceCategory = None
        # reference to CodeableConcept

        self.serviceType = None
        # type: list
        # reference to CodeableConcept

        self.specialty = None
        # type: list
        # reference to CodeableConcept

        self.appointmentType = None
        # reference to CodeableConcept

        self.schedule = None
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: busy, free, busy-unavailable,
        # busy-tentative, entered-in-error

        self.start = None
        # type: str

        self.end = None
        # type: str

        self.overbooked = None
        # type: bool

        self.comment = None
        # type: str

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
                    'busy', 'free', 'busy-unavailable', 'busy-tentative',
                        'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'busy, free, busy-unavailable, busy-tentative, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'serviceCategory'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'appointmentType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'specialty'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Slot',
             'child_variable': 'schedule'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'serviceType'},
        ]
