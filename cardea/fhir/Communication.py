from .fhirbase import fhirbase


class Communication(fhirbase):
    """
    An occurrence of information being transmitted; e.g. an alert that was
    sent to a responsible provider, a public health agency was notified
    about a reportable condition.

    Args:
        resourceType: This is a Communication resource
        identifier: Identifiers associated with this Communication that are
            defined by business processes and/ or used to refer to it when a
            direct URL reference to the resource itself is not appropriate (e.g.
            in CDA documents, or in written / printed documentation).
        definition: A protocol, guideline, or other definition that was
            adhered to in whole or in part by this communication event.
        basedOn: An order, proposal or plan fulfilled in whole or in part by
            this Communication.
        partOf: Part of this action.
        status: The status of the transmission.
        notDone: If true, indicates that the described communication event did
            not actually occur.
        notDoneReason: Describes why the communication event did not occur in
            coded and/or textual form.
        category: The type of message conveyed such as alert, notification,
            reminder, instruction, etc.
        medium: A channel that was used for this communication (e.g. email,
            fax).
        subject: The patient or group that was the focus of this
            communication.
        recipient: The entity (e.g. person, organization, clinical information
            system, or device) which was the target of the communication. If
            receipts need to be tracked by individual, a separate resource
            instance will need to be created for each recipient.  Multiple
            recipient communications are intended where either a receipt(s) is not
            tracked (e.g. a mass mail-out) or is captured in aggregate (all emails
            confirmed received by a particular time).
        topic: The resources which were responsible for or related to
            producing this communication.
        context: The encounter within which the communication was sent.
        sent: The time when this communication was sent.
        received: The time when this communication arrived at the destination.
        sender: The entity (e.g. person, organization, clinical information
            system, or device) which was the source of the communication.
        reasonCode: The reason or justification for the communication.
        reasonReference: Indicates another resource whose existence justifies
            this communication.
        payload: Text, attachment(s), or resource(s) that was communicated to
            the recipient.
        note: Additional notes or commentary about the communication by the
            sender, receiver or other interested parties.
    """

    __name__ = 'Communication'

    def __init__(self, dict_values=None):
        self.resourceType = 'Communication'
        # type: str
        # possible values: Communication

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str

        self.notDone = None
        # type: bool

        self.notDoneReason = None
        # reference to CodeableConcept

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.medium = None
        # type: list
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.recipient = None
        # type: list
        # reference to Reference: identifier

        self.topic = None
        # type: list
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.sent = None
        # type: str

        self.received = None
        # type: str

        self.sender = None
        # reference to Reference: identifier

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.payload = None
        # type: list
        # reference to Communication_Payload

        self.note = None
        # type: list
        # reference to Annotation

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
             'child_entity': 'Communication',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'medium'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'sender'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'context'},

            {'parent_entity': 'Communication_Payload',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'payload'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'recipient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'notDoneReason'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'subject'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'topic'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'basedOn'},
        ]


class Communication_Payload(fhirbase):
    """
    An occurrence of information being transmitted; e.g. an alert that was
    sent to a responsible provider, a public health agency was notified
    about a reportable condition.

    Args:
        contentString: A communicated content (or for multi-part
            communications, one portion of the communication).
        contentAttachment: A communicated content (or for multi-part
            communications, one portion of the communication).
        contentReference: A communicated content (or for multi-part
            communications, one portion of the communication).
    """

    __name__ = 'Communication_Payload'

    def __init__(self, dict_values=None):
        self.contentString = None
        # type: str

        self.contentAttachment = None
        # reference to Attachment

        self.contentReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
