from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Annotation import Annotation
from .Identifier import Identifier
from .Reference import Reference

class Communication(fhirbase):
    """An occurrence of information being transmitted; e.g. an alert that was
    sent to a responsible provider, a public health agency was notified
    about a reportable condition.
    """

    def __init__(self, dict_values=None):
        # this is a communication resource
        self.resourceType = 'Communication'
        # type = string
        # possible values = Communication

        # a protocol, guideline, or other definition that was adhered to in whole
        # or in part by this communication event.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # an order, proposal or plan fulfilled in whole or in part by this
        # communication.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # part of this action.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # the status of the transmission.
        self.status = None
        # type = string

        # if true, indicates that the described communication event did not
        # actually occur.
        self.notDone = None
        # type = boolean

        # describes why the communication event did not occur in coded and/or
        # textual form.
        self.notDoneReason = None
        # reference to CodeableConcept: CodeableConcept

        # the type of message conveyed such as alert, notification, reminder,
        # instruction, etc.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a channel that was used for this communication (e.g. email, fax).
        self.medium = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the patient or group that was the focus of this communication.
        self.subject = None
        # reference to Reference: identifier

        # the entity (e.g. person, organization, clinical information system, or
        # device) which was the target of the communication. if receipts need to
        # be tracked by individual, a separate resource instance will need to be
        # created for each recipient.  multiple recipient communications are
        # intended where either a receipt(s) is not tracked (e.g. a mass mail-out)
        # or is captured in aggregate (all emails confirmed received by a
        # particular time).
        self.recipient = None
        # type = array
        # reference to Reference: identifier

        # the resources which were responsible for or related to producing this
        # communication.
        self.topic = None
        # type = array
        # reference to Reference: identifier

        # the encounter within which the communication was sent.
        self.context = None
        # reference to Reference: identifier

        # the time when this communication was sent.
        self.sent = None
        # type = string

        # the time when this communication arrived at the destination.
        self.received = None
        # type = string

        # the entity (e.g. person, organization, clinical information system, or
        # device) which was the source of the communication.
        self.sender = None
        # reference to Reference: identifier

        # the reason or justification for the communication.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates another resource whose existence justifies this communication.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # text, attachment(s), or resource(s) that was communicated to the
        # recipient.
        self.payload = None
        # type = array
        # reference to Communication_Payload: Communication_Payload

        # additional notes or commentary about the communication by the sender,
        # receiver or other interested parties.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # identifiers associated with this communication that are defined by
        # business processes and/ or used to refer to it when a direct url
        # reference to the resource itself is not appropriate (e.g. in cda
        # documents, or in written / printed documentation).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'definition'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Communication',
            'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Communication',
            'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Communication',
            'child_variable': 'notDoneReason'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'sender'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'topic'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'context'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'basedOn'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'Communication',
            'child_variable': 'note'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Communication',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'recipient'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Communication',
            'child_variable': 'medium'},

            {'parent_entity': 'Communication_Payload',
            'parent_variable': 'object_id',
            'child_entity': 'Communication',
            'child_variable': 'payload'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'subject'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication',
            'child_variable': 'reasonReference'},
        ]

class Communication_Payload(fhirbase):
    """An occurrence of information being transmitted; e.g. an alert that was
    sent to a responsible provider, a public health agency was notified
    about a reportable condition.
    """

    def __init__(self, dict_values=None):
        # a communicated content (or for multi-part communications, one portion of
        # the communication).
        self.contentString = None
        # type = string

        # a communicated content (or for multi-part communications, one portion of
        # the communication).
        self.contentAttachment = None
        # reference to Attachment: Attachment

        # a communicated content (or for multi-part communications, one portion of
        # the communication).
        self.contentReference = None
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Communication_Payload',
            'child_variable': 'contentAttachment'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Communication_Payload',
            'child_variable': 'contentReference'},
        ]

