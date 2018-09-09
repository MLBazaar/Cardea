from .fhirbase import fhirbase


class Communication(fhirbase):
    """
    An occurrence of information being transmitted; e.g. an alert that was
    sent to a responsible provider, a public health agency was notified
    about a reportable condition.
    """

    __name__ = 'Communication'

    def __init__(self, dict_values=None):
        self.resourceType = 'Communication'
        """
        This is a Communication resource

        type: string
        possible values: Communication
        """

        self.definition = None
        """
        A protocol, guideline, or other definition that was adhered to in
        whole or in part by this communication event.

        type: array
        reference to Reference: identifier
        """

        self.basedOn = None
        """
        An order, proposal or plan fulfilled in whole or in part by this
        Communication.

        type: array
        reference to Reference: identifier
        """

        self.partOf = None
        """
        Part of this action.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        The status of the transmission.

        type: string
        """

        self.notDone = None
        """
        If true, indicates that the described communication event did not
        actually occur.

        type: boolean
        """

        self.notDoneReason = None
        """
        Describes why the communication event did not occur in coded and/or
        textual form.

        reference to CodeableConcept
        """

        self.category = None
        """
        The type of message conveyed such as alert, notification, reminder,
        instruction, etc.

        type: array
        reference to CodeableConcept
        """

        self.medium = None
        """
        A channel that was used for this communication (e.g. email, fax).

        type: array
        reference to CodeableConcept
        """

        self.subject = None
        """
        The patient or group that was the focus of this communication.

        reference to Reference: identifier
        """

        self.recipient = None
        """
        The entity (e.g. person, organization, clinical information system, or
        device) which was the target of the communication. If receipts need to
        be tracked by individual, a separate resource instance will need to be
        created for each recipient.  Multiple recipient communications are
        intended where either a receipt(s) is not tracked (e.g. a mass
        mail-out) or is captured in aggregate (all emails confirmed received
        by a particular time).

        type: array
        reference to Reference: identifier
        """

        self.topic = None
        """
        The resources which were responsible for or related to producing this
        communication.

        type: array
        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter within which the communication was sent.

        reference to Reference: identifier
        """

        self.sent = None
        """
        The time when this communication was sent.

        type: string
        """

        self.received = None
        """
        The time when this communication arrived at the destination.

        type: string
        """

        self.sender = None
        """
        The entity (e.g. person, organization, clinical information system, or
        device) which was the source of the communication.

        reference to Reference: identifier
        """

        self.reasonCode = None
        """
        The reason or justification for the communication.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Indicates another resource whose existence justifies this
        communication.

        type: array
        reference to Reference: identifier
        """

        self.payload = None
        """
        Text, attachment(s), or resource(s) that was communicated to the
        recipient.

        type: array
        reference to Communication_Payload
        """

        self.note = None
        """
        Additional notes or commentary about the communication by the sender,
        receiver or other interested parties.

        type: array
        reference to Annotation
        """

        self.identifier = None
        """
        Identifiers associated with this Communication that are defined by
        business processes and/ or used to refer to it when a direct URL
        reference to the resource itself is not appropriate (e.g. in CDA
        documents, or in written / printed documentation).

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'notDoneReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'recipient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'medium'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'sender'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'context'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Communication',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Communication',
             'child_variable': 'topic'},

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
             'child_variable': 'definition'},
        ]


class Communication_Payload(fhirbase):
    """
    An occurrence of information being transmitted; e.g. an alert that was
    sent to a responsible provider, a public health agency was notified
    about a reportable condition.
    """

    __name__ = 'Communication_Payload'

    def __init__(self, dict_values=None):
        self.contentString = None
        """
        A communicated content (or for multi-part communications, one portion
        of the communication).

        type: string
        """

        self.contentAttachment = None
        """
        A communicated content (or for multi-part communications, one portion
        of the communication).

        reference to Attachment
        """

        self.contentReference = None
        """
        A communicated content (or for multi-part communications, one portion
        of the communication).

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
             'child_entity': 'Communication_Payload',
             'child_variable': 'contentReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Communication_Payload',
             'child_variable': 'contentAttachment'},
        ]
