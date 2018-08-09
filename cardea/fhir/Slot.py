from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Reference import Reference

class Slot(fhirbase):
    """A slot of time on a schedule that may be available for booking
    appointments.
    """

    def __init__(self, dict_values=None):
        # this is a slot resource
        self.resourceType = 'Slot'
        # type = string
        # possible values = Slot

        # a broad categorisation of the service that is to be performed during
        # this appointment.
        self.serviceCategory = None
        # reference to CodeableConcept: CodeableConcept

        # the type of appointments that can be booked into this slot (ideally this
        # would be an identifiable service - which is at a location, rather than
        # the location itself). if provided then this overrides the value provided
        # on the availability resource.
        self.serviceType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the specialty of a practitioner that would be required to perform the
        # service requested in this appointment.
        self.specialty = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the style of appointment or patient that may be booked in the slot (not
        # service type).
        self.appointmentType = None
        # reference to CodeableConcept: CodeableConcept

        # the schedule resource that this slot defines an interval of status
        # information.
        self.schedule = None
        # reference to Reference: identifier

        # busy | free | busy-unavailable | busy-tentative | entered-in-error.
        self.status = None
        # type = string
        # possible values = busy, free, busy-unavailable, busy-tentative, entered-in-error

        # date/time that the slot is to begin.
        self.start = None
        # type = string

        # date/time that the slot is to conclude.
        self.end = None
        # type = string

        # this slot has already been overbooked, appointments are unlikely to be
        # accepted for this time.
        self.overbooked = None
        # type = boolean

        # comments on the slot to describe any extended information. such as
        # custom constraints on the slot.
        self.comment = None
        # type = string

        # external ids for this item.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['busy', 'free', 'busy-unavailable', 'busy-tentative', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'busy, free, busy-unavailable, busy-tentative, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Slot',
            'child_variable': 'serviceType'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Slot',
            'child_variable': 'schedule'},

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
            'child_variable': 'serviceCategory'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Slot',
            'child_variable': 'specialty'},
        ]

