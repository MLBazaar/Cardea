from .fhirbase import fhirbase


class AuditEvent(fhirbase):
    """
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring
    for inappropriate usage.

    Args:
        resourceType: This is a AuditEvent resource
        type: Identifier for a family of the event.  For example, a menu item,
            program, rule, policy, function code, application name or URL. It
            identifies the performed function.
        subtype: Identifier for the category of event.
        action: Indicator for type of action performed during the event that
            generated the audit.
        recorded: The time when the event occurred on the source.
        outcome: Indicates whether the event succeeded or failed.
        outcomeDesc: A free text description of the outcome of the event.
        purposeOfEvent: The purposeOfUse (reason) that was used during the
            event being recorded.
        agent: An actor taking an active role in the event or activity that is
            logged.
        source: The system that is reporting the event.
        entity: Specific instances of data or objects that have been accessed.
    """

    __name__ = 'AuditEvent'

    def __init__(self, dict_values=None):
        self.resourceType = 'AuditEvent'
        # type: str
        # possible values: AuditEvent

        self.type = None
        # reference to Coding

        self.subtype = None
        # type: list
        # reference to Coding

        self.action = None
        # type: str
        # possible values: C, R, U, D, E

        self.recorded = None
        # type: str

        self.outcome = None
        # type: str
        # possible values: 0, 4, 8, 12

        self.outcomeDesc = None
        # type: str

        self.purposeOfEvent = None
        # type: list
        # reference to CodeableConcept

        self.agent = None
        # type: list
        # reference to AuditEvent_Agent

        self.source = None
        # reference to AuditEvent_Source: identifier

        self.entity = None
        # type: list
        # reference to AuditEvent_Entity: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'type'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'subtype'},

            {'parent_entity': 'AuditEvent_Source',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent',
             'child_variable': 'source'},

            {'parent_entity': 'AuditEvent_Agent',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'agent'},

            {'parent_entity': 'AuditEvent_Entity',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent',
             'child_variable': 'entity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent',
             'child_variable': 'purposeOfEvent'},
        ]


class AuditEvent_Agent(fhirbase):
    """
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring
    for inappropriate usage.

    Args:
        role: The security role that the user was acting under, that come from
            local codes defined by the access control security system (e.g. RBAC,
            ABAC) used in the local context.
        reference: Direct reference to a resource that identifies the agent.
        userId: Unique identifier for the user actively participating in the
            event.
        altId: Alternative agent Identifier. For a human, this should be a
            user identifier text string from authentication system. This
            identifier would be one known to a common authentication system (e.g.
            single sign-on), if available.
        name: Human-meaningful name for the agent.
        requestor: Indicator that the user is or is not the requestor, or
            initiator, for the event being audited.
        location: Where the event occurred.
        policy: The policy or plan that authorized the activity being
            recorded. Typically, a single activity may have multiple applicable
            policies, such as patient consent, guarantor funding, etc. The policy
            would also indicate the security token used.
        media: Type of media involved. Used when the event is about
            exporting/importing onto media.
        network: Logical network location for application activity, if the
            activity has a network location.
        purposeOfUse: The reason (purpose of use), specific to this agent,
            that was used during the event being recorded.
    """

    __name__ = 'AuditEvent_Agent'

    def __init__(self, dict_values=None):
        self.role = None
        # type: list
        # reference to CodeableConcept

        self.reference = None
        # reference to Reference: identifier

        self.userId = None
        # reference to Identifier

        self.altId = None
        # type: str

        self.name = None
        # type: str

        self.requestor = None
        # type: bool

        self.location = None
        # reference to Reference: identifier

        self.policy = None
        # type: list

        self.media = None
        # reference to Coding

        self.network = None
        # reference to AuditEvent_Network

        self.purposeOfUse = None
        # type: list
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'purposeOfUse'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'reference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'userId'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'location'},

            {'parent_entity': 'AuditEvent_Network',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'network'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'media'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Agent',
             'child_variable': 'role'},
        ]


class AuditEvent_Network(fhirbase):
    """
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring
    for inappropriate usage.

    Args:
        address: An identifier for the network access point of the user device
            for the audit event.
        type: An identifier for the type of network access point that
            originated the audit event.
    """

    __name__ = 'AuditEvent_Network'

    def __init__(self, dict_values=None):
        self.address = None
        # type: str

        self.type = None
        # type: str
        # possible values: 1, 2, 3, 4, 5

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        '1', '2', '3', '4', '5']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, '1, 2, 3, 4, 5'))


class AuditEvent_Source(fhirbase):
    """
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring
    for inappropriate usage.

    Args:
        site: Logical source location within the healthcare enterprise
            network.  For example, a hospital or other provider location within a
            multi-entity provider group.
        identifier: Identifier of the source where the event was detected.
        type: Code specifying the type of source where event originated.
    """

    __name__ = 'AuditEvent_Source'

    def __init__(self, dict_values=None):
        self.site = None
        # type: str

        self.type = None
        # type: list
        # reference to Coding

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Source',
             'child_variable': 'identifier'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Source',
             'child_variable': 'type'},
        ]


class AuditEvent_Entity(fhirbase):
    """
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring
    for inappropriate usage.

    Args:
        identifier: Identifies a specific instance of the entity. The
            reference should always be version specific.
        reference: Identifies a specific instance of the entity. The reference
            should be version specific.
        type: The type of the object that was involved in this audit event.
        role: Code representing the role the entity played in the event being
            audited.
        lifecycle: Identifier for the data life-cycle stage for the entity.
        securityLabel: Security labels for the identified entity.
        name: A name of the entity in the audit event.
        description: Text that describes the entity in more detail.
        query: The query parameters for a query-type entities.
        detail: Tagged value pairs for conveying additional information about
            the entity.
    """

    __name__ = 'AuditEvent_Entity'

    def __init__(self, dict_values=None):
        self.reference = None
        # reference to Reference: identifier

        self.type = None
        # reference to Coding

        self.role = None
        # reference to Coding

        self.lifecycle = None
        # reference to Coding

        self.securityLabel = None
        # type: list
        # reference to Coding

        self.name = None
        # type: str

        self.description = None
        # type: str

        self.query = None
        # type: str

        self.detail = None
        # type: list
        # reference to AuditEvent_Detail

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'type'},

            {'parent_entity': 'AuditEvent_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'detail'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'role'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'reference'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'AuditEvent_Entity',
             'child_variable': 'lifecycle'},
        ]


class AuditEvent_Detail(fhirbase):
    """
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring
    for inappropriate usage.

    Args:
        type: The type of extra detail provided in the value.
        value: The details, base64 encoded. Used to carry bulk information.
    """

    __name__ = 'AuditEvent_Detail'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
