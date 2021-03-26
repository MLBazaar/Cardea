from .fhirbase import fhirbase


class Schedule(fhirbase):
    """
    A container for slots of time that may be available for booking
    appointments.

    Args:
        resourceType: This is a Schedule resource
        identifier: External Ids for this item.
        active: Whether this schedule record is in active use, or should not
            be used (such as was entered in error).
        serviceCategory: A broad categorisation of the service that is to be
            performed during this appointment.
        serviceType: The specific service that is to be performed during this
            appointment.
        specialty: The specialty of a practitioner that would be required to
            perform the service requested in this appointment.
        actor: The resource this Schedule resource is providing availability
            information for. These are expected to usually be one of
            HealthcareService, Location, Practitioner, PractitionerRole, Device,
            Patient or RelatedPerson.
        planningHorizon: The period of time that the slots that are attached
            to this Schedule resource cover (even if none exist). These  cover the
            amount of time that an organization's planning horizon; the interval
            for which they are currently accepting appointments. This does not
            define a "template" for planning outside these dates.
        comment: Comments on the availability to describe any extended
            information. Such as custom constraints on the slots that may be
            associated.
    """

    __name__ = 'Schedule'

    def __init__(self, dict_values=None):
        self.resourceType = 'Schedule'
        # type: str
        # possible values: Schedule

        self.active = None
        # type: bool

        self.serviceCategory = None
        # reference to CodeableConcept

        self.serviceType = None
        # type: list
        # reference to CodeableConcept

        self.specialty = None
        # type: list
        # reference to CodeableConcept

        self.actor = None
        # type: list
        # reference to Reference: identifier

        self.planningHorizon = None
        # reference to Period

        self.comment = None
        # type: str

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'serviceType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'specialty'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'serviceCategory'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'planningHorizon'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Schedule',
             'child_variable': 'actor'},
        ]
