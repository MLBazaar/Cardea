from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Reference import Reference
from .ContactPoint import ContactPoint
from .Attachment import Attachment

class HealthcareService(fhirbase):
    """The details of a healthcare service available at a location.
    """

    def __init__(self, dict_values=None):
        # this is a healthcareservice resource
        self.resourceType = 'HealthcareService'
        # type = string
        # possible values = HealthcareService

        # whether this healthcareservice record is in active use.
        self.active = None
        # type = boolean

        # the organization that provides this healthcare service.
        self.providedBy = None
        # reference to Reference: identifier

        # identifies the broad category of service being performed or delivered.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # the specific type of service that may be delivered or performed.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # collection of specialties handled by the service site. this is more of a
        # medical term.
        self.specialty = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the location(s) where this healthcare service may be provided.
        self.location = None
        # type = array
        # reference to Reference: identifier

        # further description of the service as it would be presented to a
        # consumer while searching.
        self.name = None
        # type = string

        # any additional description of the service and/or any specific issues not
        # covered by the other attributes, which can be displayed as further
        # detail under the servicename.
        self.comment = None
        # type = string

        # extra details about the service that can't be placed in the other
        # fields.
        self.extraDetails = None
        # type = string

        # if there is a photo/symbol associated with this healthcareservice, it
        # may be included here to facilitate quick identification of the service
        # in a list.
        self.photo = None
        # reference to Attachment: Attachment

        # list of contacts related to this specific healthcare service.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # the location(s) that this service is available to (not where the service
        # is provided).
        self.coverageArea = None
        # type = array
        # reference to Reference: identifier

        # the code(s) that detail the conditions under which the healthcare
        # service is available/offered.
        self.serviceProvisionCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # does this service have specific eligibility requirements that need to be
        # met in order to use the service?
        self.eligibility = None
        # reference to CodeableConcept: CodeableConcept

        # describes the eligibility conditions for the service.
        self.eligibilityNote = None
        # type = string

        # program names that can be used to categorize the service.
        self.programName = None
        # type = array

        # collection of characteristics (attributes).
        self.characteristic = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # ways that the service accepts referrals, if this is not provided then it
        # is implied that no referral is required.
        self.referralMethod = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates whether or not a prospective consumer will require an
        # appointment for a particular service at a site to be provided by the
        # organization. indicates if an appointment is required for access to this
        # service.
        self.appointmentRequired = None
        # type = boolean

        # a collection of times that the service site is available.
        self.availableTime = None
        # type = array
        # reference to HealthcareService_AvailableTime: HealthcareService_AvailableTime

        # the healthcareservice is not available during this period of time due to
        # the provided reason.
        self.notAvailable = None
        # type = array
        # reference to HealthcareService_NotAvailable: HealthcareService_NotAvailable

        # a description of site availability exceptions, e.g. public holiday
        # availability. succinctly describing all possible exceptions to normal
        # site availability as details in the available times and not available
        # times.
        self.availabilityExceptions = None
        # type = string

        # technical endpoints providing access to services operated for the
        # specific healthcare services defined at this resource.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # external identifiers for this item.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'HealthcareService_AvailableTime',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'availableTime'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'HealthcareService',
            'child_variable': 'coverageArea'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'HealthcareService',
            'child_variable': 'endpoint'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'serviceProvisionCode'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'eligibility'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'HealthcareService',
            'child_variable': 'location'},

            {'parent_entity': 'HealthcareService_NotAvailable',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'notAvailable'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'characteristic'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'photo'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'identifier'},

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

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'referralMethod'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'telecom'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService',
            'child_variable': 'type'},
        ]

class HealthcareService_AvailableTime(fhirbase):
    """The details of a healthcare service available at a location.
    """

    def __init__(self, dict_values=None):
        # indicates which days of the week are available between the start and end
        # times.
        self.daysOfWeek = None
        # type = array
        # possible values = mon, tue, wed, thu, fri, sat, sun

        # is this always available? (hence times are irrelevant) e.g. 24 hour
        # service.
        self.allDay = None
        # type = boolean

        # the opening time of day. note: if the allday flag is set, then this time
        # is ignored.
        self.availableStartTime = None
        # type = string

        # the closing time of day. note: if the allday flag is set, then this time
        # is ignored.
        self.availableEndTime = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.daysOfWeek is not None:
            for value in self.daysOfWeek:
                if value != None and value.lower() not in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'mon, tue, wed, thu, fri, sat, sun'))

class HealthcareService_NotAvailable(fhirbase):
    """The details of a healthcare service available at a location.
    """

    def __init__(self, dict_values=None):
        # the reason that can be presented to the user as to why this time is not
        # available.
        self.description = None
        # type = string

        # service is not available (seasonally or for a public holiday) from this
        # date.
        self.during = None
        # reference to Period: Period


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'HealthcareService_NotAvailable',
            'child_variable': 'during'},
        ]

