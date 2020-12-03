from .fhirbase import fhirbase


class PractitionerRole(fhirbase):
    """
    A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.

    Args:
        resourceType: This is a PractitionerRole resource
        identifier: Business Identifiers that are specific to a role/location.
        active: Whether this practitioner's record is in active use.
        period: The period during which the person is authorized to act as a
            practitioner in these role(s) for the organization.
        practitioner: Practitioner that is able to provide the defined
            services for the organation.
        organization: The organization where the Practitioner performs the
            roles associated.
        code: Roles which this practitioner is authorized to perform for the
            organization.
        specialty: Specific specialty of the practitioner.
        location: The location(s) at which this practitioner provides care.
        healthcareService: The list of healthcare services that this worker
            provides for this role's Organization/Location(s).
        telecom: Contact details that are specific to the
            role/location/service.
        availableTime: A collection of times that the Service Site is
            available.
        notAvailable: The HealthcareService is not available during this
            period of time due to the provided reason.
        availabilityExceptions: A description of site availability exceptions,
            e.g. public holiday availability. Succinctly describing all possible
            exceptions to normal site availability as details in the available
            Times and not available Times.
        endpoint: Technical endpoints providing access to services operated
            for the practitioner with this role.
    """

    __name__ = 'PractitionerRole'

    def __init__(self, dict_values=None):
        self.resourceType = 'PractitionerRole'
        # type: str
        # possible values: PractitionerRole

        self.active = None
        # type: bool

        self.period = None
        # reference to Period

        self.practitioner = None
        # reference to Reference: identifier

        self.organization = None
        # reference to Reference: identifier

        self.code = None
        # type: list
        # reference to CodeableConcept

        self.specialty = None
        # type: list
        # reference to CodeableConcept

        self.location = None
        # type: list
        # reference to Reference: identifier

        self.healthcareService = None
        # type: list
        # reference to Reference: identifier

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.availableTime = None
        # type: list
        # reference to PractitionerRole_AvailableTime

        self.notAvailable = None
        # type: list
        # reference to PractitionerRole_NotAvailable

        self.availabilityExceptions = None
        # type: str

        self.endpoint = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'healthcareService'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'practitioner'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'specialty'},

            {'parent_entity': 'PractitionerRole_NotAvailable',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'notAvailable'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'endpoint'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'telecom'},

            {'parent_entity': 'PractitionerRole_AvailableTime',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'availableTime'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'location'},
        ]


class PractitionerRole_AvailableTime(fhirbase):
    """
    A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.

    Args:
        daysOfWeek: Indicates which days of the week are available between the
            start and end Times.
        allDay: Is this always available? (hence times are irrelevant) e.g. 24
            hour service.
        availableStartTime: The opening time of day. Note: If the AllDay flag
            is set, then this time is ignored.
        availableEndTime: The closing time of day. Note: If the AllDay flag is
            set, then this time is ignored.
    """

    __name__ = 'PractitionerRole_AvailableTime'

    def __init__(self, dict_values=None):
        self.daysOfWeek = None
        # type: list

        self.allDay = None
        # type: bool

        self.availableStartTime = None
        # type: str

        self.availableEndTime = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class PractitionerRole_NotAvailable(fhirbase):
    """
    A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.

    Args:
        description: The reason that can be presented to the user as to why
            this time is not available.
        during: Service is not available (seasonally or for a public holiday)
            from this date.
    """

    __name__ = 'PractitionerRole_NotAvailable'

    def __init__(self, dict_values=None):
        self.description = None
        # type: str

        self.during = None
        # reference to Period

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
