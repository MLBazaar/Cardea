from .fhirbase import fhirbase


class HealthcareService(fhirbase):
    """
    The details of a healthcare service available at a location.
    """

    __name__ = 'HealthcareService'

    def __init__(self, dict_values=None):
        self.resourceType = 'HealthcareService'
        """
        This is a HealthcareService resource

        type: string
        possible values: HealthcareService
        """

        self.active = None
        """
        Whether this healthcareservice record is in active use.

        type: boolean
        """

        self.providedBy = None
        """
        The organization that provides this healthcare service.

        reference to Reference: identifier
        """

        self.category = None
        """
        Identifies the broad category of service being performed or delivered.

        reference to CodeableConcept
        """

        self.type = None
        """
        The specific type of service that may be delivered or performed.

        type: array
        reference to CodeableConcept
        """

        self.specialty = None
        """
        Collection of specialties handled by the service site. This is more of
        a medical term.

        type: array
        reference to CodeableConcept
        """

        self.location = None
        """
        The location(s) where this healthcare service may be provided.

        type: array
        reference to Reference: identifier
        """

        self.name = None
        """
        Further description of the service as it would be presented to a
        consumer while searching.

        type: string
        """

        self.comment = None
        """
        Any additional description of the service and/or any specific issues
        not covered by the other attributes, which can be displayed as further
        detail under the serviceName.

        type: string
        """

        self.extraDetails = None
        """
        Extra details about the service that can't be placed in the other
        fields.

        type: string
        """

        self.photo = None
        """
        If there is a photo/symbol associated with this HealthcareService, it
        may be included here to facilitate quick identification of the service
        in a list.

        reference to Attachment
        """

        self.telecom = None
        """
        List of contacts related to this specific healthcare service.

        type: array
        reference to ContactPoint
        """

        self.coverageArea = None
        """
        The location(s) that this service is available to (not where the
        service is provided).

        type: array
        reference to Reference: identifier
        """

        self.serviceProvisionCode = None
        """
        The code(s) that detail the conditions under which the healthcare
        service is available/offered.

        type: array
        reference to CodeableConcept
        """

        self.eligibility = None
        """
        Does this service have specific eligibility requirements that need to
        be met in order to use the service?

        reference to CodeableConcept
        """

        self.eligibilityNote = None
        """
        Describes the eligibility conditions for the service.

        type: string
        """

        self.programName = None
        """
        Program Names that can be used to categorize the service.

        type: array
        """

        self.characteristic = None
        """
        Collection of characteristics (attributes).

        type: array
        reference to CodeableConcept
        """

        self.referralMethod = None
        """
        Ways that the service accepts referrals, if this is not provided then
        it is implied that no referral is required.

        type: array
        reference to CodeableConcept
        """

        self.appointmentRequired = None
        """
        Indicates whether or not a prospective consumer will require an
        appointment for a particular service at a site to be provided by the
        Organization. Indicates if an appointment is required for access to
        this service.

        type: boolean
        """

        self.availableTime = None
        """
        A collection of times that the Service Site is available.

        type: array
        reference to HealthcareService_AvailableTime
        """

        self.notAvailable = None
        """
        The HealthcareService is not available during this period of time due
        to the provided reason.

        type: array
        reference to HealthcareService_NotAvailable
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
        specific healthcare services defined at this resource.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        External identifiers for this item.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'type'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'telecom'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'coverageArea'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'serviceProvisionCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'location'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'referralMethod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'providedBy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'specialty'},

            {'parent_entity': 'HealthcareService_NotAvailable',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'notAvailable'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'eligibility'},

            {'parent_entity': 'HealthcareService_AvailableTime',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'availableTime'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'characteristic'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'photo'},
        ]


class HealthcareService_AvailableTime(fhirbase):
    """
    The details of a healthcare service available at a location.
    """

    __name__ = 'HealthcareService_AvailableTime'

    def __init__(self, dict_values=None):
        self.daysOfWeek = None
        """
        Indicates which days of the week are available between the start and
        end Times.

        type: array
        possible values: mon, tue, wed, thu, fri, sat, sun
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

    def assert_type(self):

        if self.daysOfWeek is not None:
            for value in self.daysOfWeek:
                if value is not None and value.lower() not in [
                        'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'mon, tue, wed, thu, fri, sat, sun'))


class HealthcareService_NotAvailable(fhirbase):
    """
    The details of a healthcare service available at a location.
    """

    __name__ = 'HealthcareService_NotAvailable'

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
             'child_entity': 'HealthcareService_NotAvailable',
             'child_variable': 'during'},
        ]
