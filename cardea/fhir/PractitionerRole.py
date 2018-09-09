from .fhirbase import fhirbase


class PractitionerRole(fhirbase):
    """
    A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.
    """

    __name__ = 'PractitionerRole'

    def __init__(self, dict_values=None):
        self.resourceType = 'PractitionerRole'
        """
        This is a PractitionerRole resource

        type: string
        possible values: PractitionerRole
        """

        self.active = None
        """
        Whether this practitioner's record is in active use.

        type: boolean
        """

        self.period = None
        """
        The period during which the person is authorized to act as a
        practitioner in these role(s) for the organization.

        reference to Period
        """

        self.practitioner = None
        """
        Practitioner that is able to provide the defined services for the
        organation.

        reference to Reference: identifier
        """

        self.organization = None
        """
        The organization where the Practitioner performs the roles associated.

        reference to Reference: identifier
        """

        self.code = None
        """
        Roles which this practitioner is authorized to perform for the
        organization.

        type: array
        reference to CodeableConcept
        """

        self.specialty = None
        """
        Specific specialty of the practitioner.

        type: array
        reference to CodeableConcept
        """

        self.location = None
        """
        The location(s) at which this practitioner provides care.

        type: array
        reference to Reference: identifier
        """

        self.healthcareService = None
        """
        The list of healthcare services that this worker provides for this
        role's Organization/Location(s).

        type: array
        reference to Reference: identifier
        """

        self.telecom = None
        """
        Contact details that are specific to the role/location/service.

        type: array
        reference to ContactPoint
        """

        self.availableTime = None
        """
        A collection of times that the Service Site is available.

        type: array
        reference to PractitionerRole_AvailableTime
        """

        self.notAvailable = None
        """
        The HealthcareService is not available during this period of time due
        to the provided reason.

        type: array
        reference to PractitionerRole_NotAvailable
        """

        self.availabilityExceptions = None
        """
        A description of site availability exceptions, e.g. public holiday
        availability. Succinctly describing all possible exceptions to normal
        site availability as details in the available Times and not available
        Times.

        type: string
        """

        self.endpoint = None
        """
        Technical endpoints providing access to services operated for the
        practitioner with this role.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Business Identifiers that are specific to a role/location.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'practitioner'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'healthcareService'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'location'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'specialty'},

            {'parent_entity': 'PractitionerRole_AvailableTime',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'availableTime'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'organization'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'identifier'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'telecom'},

            {'parent_entity': 'PractitionerRole_NotAvailable',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'notAvailable'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'endpoint'},
        ]


class PractitionerRole_AvailableTime(fhirbase):
    """
    A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.
    """

    __name__ = 'PractitionerRole_AvailableTime'

    def __init__(self, dict_values=None):
        self.daysOfWeek = None
        """
        Indicates which days of the week are available between the start and
        end Times.

        type: array
        """

        self.allDay = None
        """
        Is this always available? (hence times are irrelevant) e.g. 24 hour
        service.

        type: boolean
        """

        self.availableStartTime = None
        """
        The opening time of day. Note: If the AllDay flag is set, then this
        time is ignored.

        type: string
        """

        self.availableEndTime = None
        """
        The closing time of day. Note: If the AllDay flag is set, then this
        time is ignored.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class PractitionerRole_NotAvailable(fhirbase):
    """
    A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.
    """

    __name__ = 'PractitionerRole_NotAvailable'

    def __init__(self, dict_values=None):
        self.description = None
        """
        The reason that can be presented to the user as to why this time is
        not available.

        type: string
        """

        self.during = None
        """
        Service is not available (seasonally or for a public holiday) from
        this date.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole_NotAvailable',
             'child_variable': 'during'},
        ]
