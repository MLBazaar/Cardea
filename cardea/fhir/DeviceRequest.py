from .fhirbase import fhirbase


class DeviceRequest(fhirbase):
    """
    Represents a request for a patient to employ a medical device. The
    device may be an implantable device, or an external assistive device,
    such as a walker.
    """

    __name__ = 'DeviceRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'DeviceRequest'
        """
        This is a DeviceRequest resource

        type: string
        possible values: DeviceRequest
        """

        self.definition = None
        """
        Protocol or definition followed by this request. For example: The
        proposed act must be performed if the indicated conditions occur,
        e.g.., shortness of breath, SpO2 less than x%.

        type: array
        reference to Reference: identifier
        """

        self.basedOn = None
        """
        Plan/proposal/order fulfilled by this request.

        type: array
        reference to Reference: identifier
        """

        self.priorRequest = None
        """
        The request takes the place of the referenced completed or terminated
        request(s).

        type: array
        reference to Reference: identifier
        """

        self.groupIdentifier = None
        """
        Composite request this is part of.

        reference to Identifier
        """

        self.status = None
        """
        The status of the request.

        type: string
        """

        self.intent = None
        """
        Whether the request is a proposal, plan, an original order or a reflex
        order.

        reference to CodeableConcept
        """

        self.priority = None
        """
        Indicates how quickly the {{title}} should be addressed with respect
        to other requests.

        type: string
        """

        self.codeReference = None
        """
        The details of the device to be used.

        reference to Reference: identifier
        """

        self.codeCodeableConcept = None
        """
        The details of the device to be used.

        reference to CodeableConcept
        """

        self.subject = None
        """
        The patient who will use the device.

        reference to Reference: identifier
        """

        self.context = None
        """
        An encounter that provides additional context in which this request is
        made.

        reference to Reference: identifier
        """

        self.occurrenceDateTime = None
        """
        The timing schedule for the use of the device. The Schedule data type
        allows many different expressions, for example. "Every 8 hours";
        "Three times a day"; "1/2 an hour before breakfast for 10 days from
        23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".

        type: string
        """

        self.occurrencePeriod = None
        """
        The timing schedule for the use of the device. The Schedule data type
        allows many different expressions, for example. "Every 8 hours";
        "Three times a day"; "1/2 an hour before breakfast for 10 days from
        23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".

        reference to Period
        """

        self.occurrenceTiming = None
        """
        The timing schedule for the use of the device. The Schedule data type
        allows many different expressions, for example. "Every 8 hours";
        "Three times a day"; "1/2 an hour before breakfast for 10 days from
        23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov 2013".

        reference to Timing
        """

        self.authoredOn = None
        """
        When the request transitioned to being actionable.

        type: string
        """

        self.requester = None
        """
        The individual who initiated the request and has responsibility for
        its activation.

        reference to DeviceRequest_Requester
        """

        self.performerType = None
        """
        Desired type of performer for doing the diagnostic testing.

        reference to CodeableConcept
        """

        self.performer = None
        """
        The desired perfomer for doing the diagnostic testing.

        reference to Reference: identifier
        """

        self.reasonCode = None
        """
        Reason or justification for the use of this device.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Reason or justification for the use of this device.

        type: array
        reference to Reference: identifier
        """

        self.supportingInfo = None
        """
        Additional clinical information about the patient that may influence
        the request fulfilment.  For example, this may includes body where on
        the subject's the device will be used ( i.e. the target site).

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Details about this request that were not represented at all or
        sufficiently in one of the attributes provided in a class. These may
        include for example a comment, an instruction, or a note associated
        with the statement.

        type: array
        reference to Annotation
        """

        self.relevantHistory = None
        """
        Key events in the history of the request.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifiers assigned to this order by the orderer or by the receiver.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'codeReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'priorRequest'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'definition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'intent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'performerType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'codeCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'DeviceRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'context'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'groupIdentifier'},
        ]


class DeviceRequest_Requester(fhirbase):
    """
    Represents a request for a patient to employ a medical device. The
    device may be an implantable device, or an external assistive device,
    such as a walker.
    """

    __name__ = 'DeviceRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        """
        The device, practitioner, etc. who initiated the request.

        reference to Reference: identifier
        """

        self.onBehalfOf = None
        """
        The organization the device or practitioner was acting on behalf of.

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
             'child_entity': 'DeviceRequest_Requester',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest_Requester',
             'child_variable': 'agent'},
        ]
