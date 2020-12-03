from .fhirbase import fhirbase


class HealthcareService(fhirbase):
    """
    The details of a healthcare service available at a location.

    Args:
        resourceType: This is a HealthcareService resource
        identifier: External identifiers for this item.
        active: Whether this healthcareservice record is in active use.
        providedBy: The organization that provides this healthcare service.
        category: Identifies the broad category of service being performed or
            delivered.
        type: The specific type of service that may be delivered or performed.
        specialty: Collection of specialties handled by the service site. This
            is more of a medical term.
        location: The location(s) where this healthcare service may be
            provided.
        name: Further description of the service as it would be presented to a
            consumer while searching.
        comment: Any additional description of the service and/or any specific
            issues not covered by the other attributes, which can be displayed as
            further detail under the serviceName.
        extraDetails: Extra details about the service that can't be placed in
            the other fields.
        photo: If there is a photo/symbol associated with this
            HealthcareService, it may be included here to facilitate quick
            identification of the service in a list.
        telecom: List of contacts related to this specific healthcare service.
        coverageArea: The location(s) that this service is available to (not
            where the service is provided).
        serviceProvisionCode: The code(s) that detail the conditions under
            which the healthcare service is available/offered.
        eligibility: Does this service have specific eligibility requirements
            that need to be met in order to use the service?
        eligibilityNote: Describes the eligibility conditions for the service.
        programName: Program Names that can be used to categorize the service.
        characteristic: Collection of characteristics (attributes).
        referralMethod: Ways that the service accepts referrals, if this is
            not provided then it is implied that no referral is required.
        appointmentRequired: Indicates whether or not a prospective consumer
            will require an appointment for a particular service at a site to be
            provided by the Organization. Indicates if an appointment is required
            for access to this service.
        availableTime: A collection of times that the Service Site is
            available.
        notAvailable: The HealthcareService is not available during this
            period of time due to the provided reason.
        availabilityExceptions: A description of site availability exceptions,
            e.g. public holiday availability. Succinctly describing all possible
            exceptions to normal site availability as details in the available
            Times and not available Times.
        endpoint: Technical endpoints providing access to services operated
            for the specific healthcare services defined at this resource.
    """

    __name__ = 'HealthcareService'

    def __init__(self, dict_values=None):
        self.resourceType = 'HealthcareService'
        # type: str
        # possible values: HealthcareService

        self.active = None
        # type: bool

        self.providedBy = None
        # reference to Reference: identifier

        self.category = None
        # reference to CodeableConcept

        self.type = None
        # type: list
        # reference to CodeableConcept

        self.specialty = None
        # type: list
        # reference to CodeableConcept

        self.location = None
        # type: list
        # reference to Reference: identifier

        self.name = None
        # type: str

        self.comment = None
        # type: str

        self.extraDetails = None
        # type: str

        self.photo = None
        # reference to Attachment

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.coverageArea = None
        # type: list
        # reference to Reference: identifier

        self.serviceProvisionCode = None
        # type: list
        # reference to CodeableConcept

        self.eligibility = None
        # reference to CodeableConcept

        self.eligibilityNote = None
        # type: str

        self.programName = None
        # type: list

        self.characteristic = None
        # type: list
        # reference to CodeableConcept

        self.referralMethod = None
        # type: list
        # reference to CodeableConcept

        self.appointmentRequired = None
        # type: bool

        self.availableTime = None
        # type: list
        # reference to HealthcareService_AvailableTime

        self.notAvailable = None
        # type: list
        # reference to HealthcareService_NotAvailable

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
            {'parent_entity': 'HealthcareService_NotAvailable',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'notAvailable'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'photo'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'telecom'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'characteristic'},

            {'parent_entity': 'HealthcareService_AvailableTime',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'availableTime'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'referralMethod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'providedBy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'specialty'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'eligibility'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'serviceProvisionCode'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'coverageArea'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'HealthcareService',
             'child_variable': 'endpoint'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'HealthcareService',
             'child_variable': 'category'},
        ]


class HealthcareService_AvailableTime(fhirbase):
    """
    The details of a healthcare service available at a location.

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

    __name__ = 'HealthcareService_AvailableTime'

    def __init__(self, dict_values=None):
        self.daysOfWeek = None
        # type: list
        # possible values: mon, tue, wed, thu, fri, sat, sun

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
            self.assert_type()

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

    Args:
        description: The reason that can be presented to the user as to why
            this time is not available.
        during: Service is not available (seasonally or for a public holiday)
            from this date.
    """

    __name__ = 'HealthcareService_NotAvailable'

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
             'child_entity': 'HealthcareService_NotAvailable',
             'child_variable': 'during'},
        ]
