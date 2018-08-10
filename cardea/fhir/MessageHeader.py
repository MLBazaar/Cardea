from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Reference import Reference
from .Coding import Coding

class MessageHeader(fhirbase):
    """The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are typically
    transmitted in a bundle in which the MessageHeader resource instance is
    the first resource in the bundle.
    """

    def __init__(self, dict_values=None):
        # this is a messageheader resource
        self.resourceType = 'MessageHeader'
        # type = string
        # possible values = MessageHeader

        # code that identifies the event this message represents and connects it
        # with its definition. events defined as part of the fhir specification
        # have the system value "http://hl7.org/fhir/message-events".
        self.event = None
        # reference to Coding: Coding

        # the destination application which the message is intended for.
        self.destination = None
        # type = array
        # reference to MessageHeader_Destination: MessageHeader_Destination

        # allows data conveyed by a message to be addressed to a particular person
        # or department when routing to a specific application isn't sufficient.
        self.receiver = None
        # reference to Reference: identifier

        # identifies the sending system to allow the use of a trust relationship.
        self.sender = None
        # reference to Reference: identifier

        # the time that the message was sent.
        self.timestamp = None
        # type = string

        # the person or device that performed the data entry leading to this
        # message. when there is more than one candidate, pick the most proximal
        # to the message. can provide other enterers in extensions.
        self.enterer = None
        # reference to Reference: identifier

        # the logical author of the message - the person or device that decided
        # the described event should happen. when there is more than one
        # candidate, pick the most proximal to the messageheader. can provide
        # other authors in extensions.
        self.author = None
        # reference to Reference: identifier

        # the source application from which this message originated.
        self.source = None
        # reference to MessageHeader_Source: MessageHeader_Source

        # the person or organization that accepts overall responsibility for the
        # contents of the message. the implication is that the message event
        # happened under the policies of the responsible party.
        self.responsible = None
        # reference to Reference: identifier

        # coded indication of the cause for the event - indicates  a reason for
        # the occurrence of the event that is a focus of this message.
        self.reason = None
        # reference to CodeableConcept: CodeableConcept

        # information about the message that this message is a response to.  only
        # present if this message is a response.
        self.response = None
        # reference to MessageHeader_Response: identifier

        # the actual data of the message - a reference to the root/focus class of
        # the event.
        self.focus = None
        # type = array
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MessageHeader',
            'child_variable': 'responsible'},

            {'parent_entity': 'MessageHeader_Destination',
            'parent_variable': 'object_id',
            'child_entity': 'MessageHeader',
            'child_variable': 'destination'},

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
            'child_variable': 'author'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MessageHeader',
            'child_variable': 'reason'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MessageHeader',
            'child_variable': 'sender'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MessageHeader',
            'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MessageHeader',
            'child_variable': 'receiver'},

            {'parent_entity': 'MessageHeader_Response',
            'parent_variable': 'identifier',
            'child_entity': 'MessageHeader',
            'child_variable': 'response'},

            {'parent_entity': 'MessageHeader_Source',
            'parent_variable': 'object_id',
            'child_entity': 'MessageHeader',
            'child_variable': 'source'},
        ]

class MessageHeader_Destination(fhirbase):
    """The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are typically
    transmitted in a bundle in which the MessageHeader resource instance is
    the first resource in the bundle.
    """

    def __init__(self, dict_values=None):
        # human-readable name for the target system.
        self.name = None
        # type = string

        # identifies the target end system in situations where the initial message
        # transmission is to an intermediary system.
        self.target = None
        # reference to Reference: identifier

        # indicates where the message should be routed to.
        self.endpoint = None
        # type = string


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
    """The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are typically
    transmitted in a bundle in which the MessageHeader resource instance is
    the first resource in the bundle.
    """

    def __init__(self, dict_values=None):
        # human-readable name for the source system.
        self.name = None
        # type = string

        # may include configuration or other information useful in debugging.
        self.software = None
        # type = string

        # can convey versions of multiple systems in situations where a message
        # passes through multiple hands.
        self.version = None
        # type = string

        # an e-mail, phone, website or other contact point to use to resolve
        # issues with message communications.
        self.contact = None
        # reference to ContactPoint: ContactPoint

        # identifies the routing target to send acknowledgements to.
        self.endpoint = None
        # type = string


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
    """The header for a message exchange that is either requesting or
    responding to an action.  The reference(s) that are the subject of the
    action as well as other information related to the action are typically
    transmitted in a bundle in which the MessageHeader resource instance is
    the first resource in the bundle.
    """

    def __init__(self, dict_values=None):
        # code that identifies the type of response to the message - whether it
        # was successful or not, and whether it should be resent or not.
        self.code = None
        # type = string
        # possible values = ok, transient-error, fatal-error

        # full details of any issues found in the message.
        self.details = None
        # reference to Reference: identifier

        # the messageheader.id of the message to which this message is a response.
        self.identifier = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.code is not None:
            for value in self.code:
                if value != None and value.lower() not in ['ok', 'transient-error', 'fatal-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'ok, transient-error, fatal-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MessageHeader_Response',
            'child_variable': 'details'},
        ]

