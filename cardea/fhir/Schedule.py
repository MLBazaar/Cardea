from .fhirbase import fhirbase


class Schedule(fhirbase):
    """A container for slots of time that may be available for booking
    appointments.
    """

    __name__ = 'Schedule'

    def __init__(self, dict_values=None):
        # this is a schedule resource
        self.resourceType = 'Schedule'
        # type = string
        # possible values: Schedule

        # whether this schedule record is in active use, or should not be used
        # (such as was entered in error).
        self.active = None
        # type = boolean

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

        # the resource this schedule resource is providing availability
        # information for. these are expected to usually be one of
        # healthcareservice, location, practitioner, practitionerrole, device,
        # patient or relatedperson.
        self.actor = None
        # type = array
        # reference to Reference: identifier

        # the period of time that the slots that are attached to this schedule
        # resource cover (even if none exist). these  cover the amount of time
        # that an organization's planning horizon; the interval for which they are
        # currently accepting appointments. this does not define a "template" for
        # planning outside these dates.
        self.planningHorizon = None
        # reference to Period: Period

        # comments on the availability to describe any extended information. such
        # as custom constraints on the slots that may be associated.
        self.comment = None
        # type = string

        # external ids for this item.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Schedule',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'specialty'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'planningHorizon'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'serviceCategory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Schedule',
             'child_variable': 'serviceType'},
        ]
