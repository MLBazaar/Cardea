from .fhirbase import fhirbase


class Schedule(fhirbase):
    """
    A container for slots of time that may be available for booking
    appointments.
    """

    __name__ = 'Schedule'

    def __init__(self, dict_values=None):
        self.resourceType = 'Schedule'
        """
        This is a Schedule resource

        type: string
        possible values: Schedule
        """

        self.active = None
        """
        Whether this schedule record is in active use, or should not be used
        (such as was entered in error).

        type: boolean
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

        self.actor = None
        """
        The resource this Schedule resource is providing availability
        information for. These are expected to usually be one of
        HealthcareService, Location, Practitioner, PractitionerRole, Device,
        Patient or RelatedPerson.

        type: array
        reference to Reference: identifier
        """

        self.planningHorizon = None
        """
        The period of time that the slots that are attached to this Schedule
        resource cover (even if none exist). These  cover the amount of time
        that an organization's planning horizon; the interval for which they
        are currently accepting appointments. This does not define a
        "template" for planning outside these dates.

        reference to Period
        """

        self.comment = None
        """
        Comments on the availability to describe any extended information.
        Such as custom constraints on the slots that may be associated.

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

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'planningHorizon'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'serviceCategory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Schedule',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'specialty'},
        ]
