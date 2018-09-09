from .fhirbase import fhirbase


class MessageHeader(fhirbase):
    """
    The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are
    typically transmitted in a bundle in which the MessageHeader resource
    instance is the first resource in the bundle.
    """

    __name__ = 'MessageHeader'

    def __init__(self, dict_values=None):
        self.resourceType = 'MessageHeader'
        """
        This is a MessageHeader resource

        type: string
        possible values: MessageHeader
        """

        self.event = None
        """
        Code that identifies the event this message represents and connects it
        with its definition. Events defined as part of the FHIR specification
        have the system value "http://hl7.org/fhir/message-events".

        reference to Coding
        """

        self.destination = None
        """
        The destination application which the message is intended for.

        type: array
        reference to MessageHeader_Destination
        """

        self.receiver = None
        """
        Allows data conveyed by a message to be addressed to a particular
        person or department when routing to a specific application isn't
        sufficient.

        reference to Reference: identifier
        """

        self.sender = None
        """
        Identifies the sending system to allow the use of a trust
        relationship.

        reference to Reference: identifier
        """

        self.timestamp = None
        """
        The time that the message was sent.

        type: string
        """

        self.enterer = None
        """
        The person or device that performed the data entry leading to this
        message. When there is more than one candidate, pick the most proximal
        to the message. Can provide other enterers in extensions.

        reference to Reference: identifier
        """

        self.author = None
        """
        The logical author of the message - the person or device that decided
        the described event should happen. When there is more than one
        candidate, pick the most proximal to the MessageHeader. Can provide
        other authors in extensions.

        reference to Reference: identifier
        """

        self.source = None
        """
        The source application from which this message originated.

        reference to MessageHeader_Source
        """

        self.responsible = None
        """
        The person or organization that accepts overall responsibility for the
        contents of the message. The implication is that the message event
        happened under the policies of the responsible party.

        reference to Reference: identifier
        """

        self.reason = None
        """
        Coded indication of the cause for the event - indicates  a reason for
        the occurrence of the event that is a focus of this message.

        reference to CodeableConcept
        """

        self.response = None
        """
        Information about the message that this message is a response to.
        Only present if this message is a response.

        reference to MessageHeader_Response: identifier
        """

        self.focus = None
        """
        The actual data of the message - a reference to the root/focus class
        of the event.

        type: array
        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader',
             'child_variable': 'responsible'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader',
             'child_variable': 'receiver'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader',
             'child_variable': 'author'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MessageHeader',
             'child_variable': 'reason'},

            {'parent_entity': 'MessageHeader_Source',
             'parent_variable': 'object_id',
             'child_entity': 'MessageHeader',
             'child_variable': 'source'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader',
             'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader',
             'child_variable': 'focus'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'MessageHeader',
             'child_variable': 'event'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader',
             'child_variable': 'sender'},

            {'parent_entity': 'MessageHeader_Destination',
             'parent_variable': 'object_id',
             'child_entity': 'MessageHeader',
             'child_variable': 'destination'},

            {'parent_entity': 'MessageHeader_Response',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader',
             'child_variable': 'response'},
        ]


class MessageHeader_Destination(fhirbase):
    """
    The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are
    typically transmitted in a bundle in which the MessageHeader resource
    instance is the first resource in the bundle.
    """

    __name__ = 'MessageHeader_Destination'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Human-readable name for the target system.

        type: string
        """

        self.target = None
        """
        Identifies the target end system in situations where the initial
        message transmission is to an intermediary system.

        reference to Reference: identifier
        """

        self.endpoint = None
        """
        Indicates where the message should be routed to.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader_Destination',
             'child_variable': 'target'},
        ]


class MessageHeader_Source(fhirbase):
    """
    The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are
    typically transmitted in a bundle in which the MessageHeader resource
    instance is the first resource in the bundle.
    """

    __name__ = 'MessageHeader_Source'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Human-readable name for the source system.

        type: string
        """

        self.software = None
        """
        May include configuration or other information useful in debugging.

        type: string
        """

        self.version = None
        """
        Can convey versions of multiple systems in situations where a message
        passes through multiple hands.

        type: string
        """

        self.contact = None
        """
        An e-mail, phone, website or other contact point to use to resolve
        issues with message communications.

        reference to ContactPoint
        """

        self.endpoint = None
        """
        Identifies the routing target to send acknowledgements to.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'MessageHeader_Source',
             'child_variable': 'contact'},
        ]


class MessageHeader_Response(fhirbase):
    """
    The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are
    typically transmitted in a bundle in which the MessageHeader resource
    instance is the first resource in the bundle.
    """

    __name__ = 'MessageHeader_Response'

    def __init__(self, dict_values=None):
        self.code = None
        """
        Code that identifies the type of response to the message - whether it
        was successful or not, and whether it should be resent or not.

        type: string
        possible values: ok, transient-error, fatal-error
        """

        self.details = None
        """
        Full details of any issues found in the message.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        The MessageHeader.id of the message to which this message is a
        response.

        type: string
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                        'ok', 'transient-error', 'fatal-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'ok, transient-error, fatal-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageHeader_Response',
             'child_variable': 'details'},
        ]
