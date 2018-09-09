from .fhirbase import fhirbase


class PractitionerRole(fhirbase):
    """A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.
    """

    __name__ = 'PractitionerRole'

    def __init__(self, dict_values=None):
        # this is a practitionerrole resource
        self.resourceType = 'PractitionerRole'
        # type = string
        # possible values: PractitionerRole

        # whether this practitioner's record is in active use.
        self.active = None
        # type = boolean

        # the period during which the person is authorized to act as a
        # practitioner in these role(s) for the organization.
        self.period = None
        # reference to Period: Period

        # practitioner that is able to provide the defined services for the
        # organation.
        self.practitioner = None
        # reference to Reference: identifier

        # the organization where the practitioner performs the roles associated.
        self.organization = None
        # reference to Reference: identifier

        # roles which this practitioner is authorized to perform for the
        # organization.
        self.code = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # specific specialty of the practitioner.
        self.specialty = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the location(s) at which this practitioner provides care.
        self.location = None
        # type = array
        # reference to Reference: identifier

        # the list of healthcare services that this worker provides for this
        # role's organization/location(s).
        self.healthcareService = None
        # type = array
        # reference to Reference: identifier

        # contact details that are specific to the role/location/service.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # a collection of times that the service site is available.
        self.availableTime = None
        # type = array
        # reference to PractitionerRole_AvailableTime: PractitionerRole_AvailableTime

        # the healthcareservice is not available during this period of time due to
        # the provided reason.
        self.notAvailable = None
        # type = array
        # reference to PractitionerRole_NotAvailable: PractitionerRole_NotAvailable

        # a description of site availability exceptions, e.g. public holiday
        # availability. succinctly describing all possible exceptions to normal
        # site availability as details in the available times and not available
        # times.
        self.availabilityExceptions = None
        # type = string

        # technical endpoints providing access to services operated for the
        # practitioner with this role.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # business identifiers that are specific to a role/location.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'period'},

            {'parent_entity': 'PractitionerRole_NotAvailable',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'notAvailable'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'endpoint'},

            {'parent_entity': 'PractitionerRole_AvailableTime',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'availableTime'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'practitioner'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'specialty'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PractitionerRole',
             'child_variable': 'healthcareService'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'telecom'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole',
             'child_variable': 'code'},
        ]


class PractitionerRole_AvailableTime(fhirbase):
    """A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.
    """

    __name__ = 'PractitionerRole_AvailableTime'

    def __init__(self, dict_values=None):
        # indicates which days of the week are available between the start and end
        # times.
        self.daysOfWeek = None
        # type = array

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

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class PractitionerRole_NotAvailable(fhirbase):
    """A specific set of Roles/Locations/specialties/services that a
    practitioner may perform at an organization for a period of time.
    """

    __name__ = 'PractitionerRole_NotAvailable'

    def __init__(self, dict_values=None):
        # the reason that can be presented to the user as to why this time is not
        # available.
        self.description = None
        # type = string

        # service is not available (seasonally or for a public holiday) from this
        # date.
        self.during = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PractitionerRole_NotAvailable',
             'child_variable': 'during'},
        ]
