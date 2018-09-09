from .fhirbase import fhirbase


class AuditEvent(fhirbase):
    """A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __name__ = 'AuditEvent'

    def __init__(self, dict_values=None):
        # this is a auditevent resource
        self.resourceType = 'AuditEvent'
        # type = string
        # possible values: AuditEvent

        # identifier for a family of the event.  for example, a menu item,
        # program, rule, policy, function code, application name or url. it
        # identifies the performed function.
        self.type = None
        # reference to Coding: Coding

        # identifier for the category of event.
        self.subtype = None
        # type = array
        # reference to Coding: Coding

        # indicator for type of action performed during the event that generated
        # the audit.
        self.action = None
        # type = string
        # possible values: C, R, U, D, E

        # the time when the event occurred on the source.
        self.recorded = None
        # type = string

        # indicates whether the event succeeded or failed.
        self.outcome = None
        # type = string
        # possible values: 0, 4, 8, 12

        # a free text description of the outcome of the event.
        self.outcomeDesc = None
        # type = string

        # the purposeofuse (reason) that was used during the event being recorded.
        self.purposeOfEvent = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # an actor taking an active role in the event or activity that is logged.
        self.agent = None
        # type = array
        # reference to AuditEvent_Agent: AuditEvent_Agent

        # the system that is reporting the event.
        self.source = None
        # reference to AuditEvent_Source: identifier

        # specific instances of data or objects that have been accessed.
        self.entity = None
        # type = array
        # reference to AuditEvent_Entity: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.action is not None:
            for value in self.action:
                if value is not None and value.lower() not in [
                        'c', 'r', 'u', 'd', 'e']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'C, R, U, D, E'))

        if self.outcome is not None:
            for value in self.outcome:
                if value is not None and value.lower() not in [
                        '0', '4', '8', '12']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, '0, 4, 8, 12'))

    def get_relationships(self):

        return [
            {'parent_entity': 'AuditEvent_Entity',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent',
             'child_variable': 'entity'},

            {'parent_entity': 'AuditEvent_Agent',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'agent'},

            {'parent_entity': 'AuditEvent_Source',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent',
             'child_variable': 'source'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'subtype'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'purposeOfEvent'},
        ]


class AuditEvent_Agent(fhirbase):
    """A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __name__ = 'AuditEvent_Agent'

    def __init__(self, dict_values=None):
        # the security role that the user was acting under, that come from local
        # codes defined by the access control security system (e.g. rbac, abac)
        # used in the local context.
        self.role = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # direct reference to a resource that identifies the agent.
        self.reference = None
        # reference to Reference: identifier

        # unique identifier for the user actively participating in the event.
        self.userId = None
        # reference to Identifier: Identifier

        # alternative agent identifier. for a human, this should be a user
        # identifier text string from authentication system. this identifier would
        # be one known to a common authentication system (e.g. single sign-on), if
        # available.
        self.altId = None
        # type = string

        # human-meaningful name for the agent.
        self.name = None
        # type = string

        # indicator that the user is or is not the requestor, or initiator, for
        # the event being audited.
        self.requestor = None
        # type = boolean

        # where the event occurred.
        self.location = None
        # reference to Reference: identifier

        # the policy or plan that authorized the activity being recorded.
        # typically, a single activity may have multiple applicable policies, such
        # as patient consent, guarantor funding, etc. the policy would also
        # indicate the security token used.
        self.policy = None
        # type = array

        # type of media involved. used when the event is about exporting/importing
        # onto media.
        self.media = None
        # reference to Coding: Coding

        # logical network location for application activity, if the activity has a
        # network location.
        self.network = None
        # reference to AuditEvent_Network: AuditEvent_Network

        # the reason (purpose of use), specific to this agent, that was used
        # during the event being recorded.
        self.purposeOfUse = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'reference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'userId'},

            {'parent_entity': 'AuditEvent_Network',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'network'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'purposeOfUse'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'media'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'location'},
        ]


class AuditEvent_Network(fhirbase):
    """A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __name__ = 'AuditEvent_Network'

    def __init__(self, dict_values=None):
        # an identifier for the network access point of the user device for the
        # audit event.
        self.address = None
        # type = string

        # an identifier for the type of network access point that originated the
        # audit event.
        self.type = None
        # type = string
        # possible values: 1, 2, 3, 4, 5

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        '1', '2', '3', '4', '5']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, '1, 2, 3, 4, 5'))


class AuditEvent_Source(fhirbase):
    """A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __name__ = 'AuditEvent_Source'

    def __init__(self, dict_values=None):
        # logical source location within the healthcare enterprise network.  for
        # example, a hospital or other provider location within a multi-entity
        # provider group.
        self.site = None
        # type = string

        # code specifying the type of source where event originated.
        self.type = None
        # type = array
        # reference to Coding: Coding

        # identifier of the source where the event was detected.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Source',
             'child_variable': 'type'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Source',
             'child_variable': 'identifier'},
        ]


class AuditEvent_Entity(fhirbase):
    """A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __name__ = 'AuditEvent_Entity'

    def __init__(self, dict_values=None):
        # identifies a specific instance of the entity. the reference should be
        # version specific.
        self.reference = None
        # reference to Reference: identifier

        # the type of the object that was involved in this audit event.
        self.type = None
        # reference to Coding: Coding

        # code representing the role the entity played in the event being audited.
        self.role = None
        # reference to Coding: Coding

        # identifier for the data life-cycle stage for the entity.
        self.lifecycle = None
        # reference to Coding: Coding

        # security labels for the identified entity.
        self.securityLabel = None
        # type = array
        # reference to Coding: Coding

        # a name of the entity in the audit event.
        self.name = None
        # type = string

        # text that describes the entity in more detail.
        self.description = None
        # type = string

        # the query parameters for a query-type entities.
        self.query = None
        # type = string

        # tagged value pairs for conveying additional information about the
        # entity.
        self.detail = None
        # type = array
        # reference to AuditEvent_Detail: AuditEvent_Detail

        # identifies a specific instance of the entity. the reference should
        # always be version specific.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'AuditEvent_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'detail'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'type'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'lifecycle'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'reference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'identifier'},
        ]


class AuditEvent_Detail(fhirbase):
    """A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __name__ = 'AuditEvent_Detail'

    def __init__(self, dict_values=None):
        # the type of extra detail provided in the value.
        self.type = None
        # type = string

        # the details, base64 encoded. used to carry bulk information.
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
