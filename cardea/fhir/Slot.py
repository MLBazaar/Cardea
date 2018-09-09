from .fhirbase import fhirbase


class Slot(fhirbase):
    """
    A slot of time on a schedule that may be available for booking
    appointments.
    """

    __name__ = 'Slot'

    def __init__(self, dict_values=None):
        self.resourceType = 'Slot'
        """
        This is a Slot resource

        type: string
        possible values: Slot
        """

        self.serviceCategory = None
        """
        A broad categorisation of the service that is to be performed during
        this appointment.

        reference to CodeableConcept
        """

        self.serviceType = None
        """
        The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location, rather
        than the location itself). If provided then this overrides the value
        provided on the availability resource.

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
        The style of appointment or patient that may be booked in the slot
        (not service type).

        reference to CodeableConcept
        """

        self.schedule = None
        """
        The schedule resource that this slot defines an interval of status
        information.

        reference to Reference: identifier
        """

        self.status = None
        """
        busy | free | busy-unavailable | busy-tentative | entered-in-error.

        type: string
        possible values: busy, free, busy-unavailable, busy-tentative,
        entered-in-error
        """

        self.start = None
        """
        Date/Time that the slot is to begin.

        type: string
        """

        self.end = None
        """
        Date/Time that the slot is to conclude.

        type: string
        """

        self.overbooked = None
        """
        This slot has already been overbooked, appointments are unlikely to be
        accepted for this time.

        type: boolean
        """

        self.comment = None
        """
        Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.

        type: string
        """

        self.identifier = None
        """
        External Ids for this item.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Slot',
             'child_variable': 'schedule'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'serviceType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'appointmentType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Slot',
             'child_variable': 'specialty'},
        ]
