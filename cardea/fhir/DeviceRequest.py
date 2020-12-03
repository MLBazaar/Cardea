from .fhirbase import fhirbase


class DeviceRequest(fhirbase):
    """
    Represents a request for a patient to employ a medical device. The
    device may be an implantable device, or an external assistive device,
    such as a walker.

    Args:
        resourceType: This is a DeviceRequest resource
        identifier: Identifiers assigned to this order by the orderer or by
            the receiver.
        definition: Protocol or definition followed by this request. For
            example: The proposed act must be performed if the indicated
            conditions occur, e.g.., shortness of breath, SpO2 less than x%.
        basedOn: Plan/proposal/order fulfilled by this request.
        priorRequest: The request takes the place of the referenced completed
            or terminated request(s).
        groupIdentifier: Composite request this is part of.
        status: The status of the request.
        intent: Whether the request is a proposal, plan, an original order or
            a reflex order.
        priority: Indicates how quickly the {{title}} should be addressed with
            respect to other requests.
        codeReference: The details of the device to be used.
        codeCodeableConcept: The details of the device to be used.
        subject: The patient who will use the device.
        context: An encounter that provides additional context in which this
            request is made.
        occurrenceDateTime: The timing schedule for the use of the device. The
            Schedule data type allows many different expressions, for example.
            "Every 8 hours"; "Three times a day"; "1/2 an hour before breakfast
            for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov
            2013".
        occurrencePeriod: The timing schedule for the use of the device. The
            Schedule data type allows many different expressions, for example.
            "Every 8 hours"; "Three times a day"; "1/2 an hour before breakfast
            for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov
            2013".
        occurrenceTiming: The timing schedule for the use of the device. The
            Schedule data type allows many different expressions, for example.
            "Every 8 hours"; "Three times a day"; "1/2 an hour before breakfast
            for 10 days from 23-Dec 2011:"; "15 Oct 2013, 17 Oct 2013 and 1 Nov
            2013".
        authoredOn: When the request transitioned to being actionable.
        requester: The individual who initiated the request and has
            responsibility for its activation.
        performerType: Desired type of performer for doing the diagnostic
            testing.
        performer: The desired perfomer for doing the diagnostic testing.
        reasonCode: Reason or justification for the use of this device.
        reasonReference: Reason or justification for the use of this device.
        supportingInfo: Additional clinical information about the patient that
            may influence the request fulfilment.  For example, this may includes
            body where on the subject's the device will be used ( i.e. the target
            site).
        note: Details about this request that were not represented at all or
            sufficiently in one of the attributes provided in a class. These may
            include for example a comment, an instruction, or a note associated
            with the statement.
        relevantHistory: Key events in the history of the request.
    """

    __name__ = 'DeviceRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'DeviceRequest'
        # type: str
        # possible values: DeviceRequest

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.priorRequest = None
        # type: list
        # reference to Reference: identifier

        self.groupIdentifier = None
        # reference to Identifier

        self.status = None
        # type: str

        self.intent = None
        # reference to CodeableConcept

        self.priority = None
        # type: str

        self.codeReference = None
        # reference to Reference: identifier

        self.codeCodeableConcept = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.occurrenceTiming = None
        # reference to Timing

        self.authoredOn = None
        # type: str

        self.requester = None
        # reference to DeviceRequest_Requester

        self.performerType = None
        # reference to CodeableConcept

        self.performer = None
        # reference to Reference: identifier

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.supportingInfo = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.relevantHistory = None
        # type: list
        # reference to Reference: identifier

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
             'child_entity': 'DeviceRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'performerType'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'definition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'codeCodeableConcept'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'intent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'priorRequest'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'context'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'DeviceRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'codeReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceRequest',
             'child_variable': 'performer'},
        ]


class DeviceRequest_Requester(fhirbase):
    """
    Represents a request for a patient to employ a medical device. The
    device may be an implantable device, or an external assistive device,
    such as a walker.

    Args:
        agent: The device, practitioner, etc. who initiated the request.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'DeviceRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        # reference to Reference: identifier

        self.onBehalfOf = None
        # reference to Reference: identifier

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
