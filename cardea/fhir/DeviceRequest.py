from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Annotation import Annotation
from .Timing import Timing
from .Reference import Reference
from .Period import Period

class DeviceRequest(fhirbase):
    """Represents a request for a patient to employ a medical device. The
    device may be an implantable device, or an external assistive device,
    such as a walker.
    """

    def __init__(self, dict_values=None):
        # this is a devicerequest resource
        self.resourceType = 'DeviceRequest'
        # type = string
        # possible values = DeviceRequest

        # protocol or definition followed by this request. for example: the
        # proposed act must be performed if the indicated conditions occur, e.g..,
        # shortness of breath, spo2 less than x%.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # plan/proposal/order fulfilled by this request.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # the request takes the place of the referenced completed or terminated
        # request(s).
        self.priorRequest = None
        # type = array
        # reference to Reference: identifier

        # composite request this is part of.
        self.groupIdentifier = None
        # reference to Identifier: Identifier

        # the status of the request.
        self.status = None
        # type = string

        # whether the request is a proposal, plan, an original order or a reflex
        # order.
        self.intent = None
        # reference to CodeableConcept: CodeableConcept

        # indicates how quickly the {{title}} should be addressed with respect to
        # other requests.
        self.priority = None
        # type = string

        # the details of the device to be used.
        self.codeReference = None
        # reference to Reference: identifier

        # the details of the device to be used.
        self.codeCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the patient who will use the device.
        self.subject = None
        # reference to Reference: identifier

        # an encounter that provides additional context in which this request is
        # made.
        self.context = None
        # reference to Reference: identifier

        # the timing schedule for the use of the device. the schedule data type
        # allows many different expressions, for example. "every 8 hours"; "three
        # times a day"; "1/2 an hour before breakfast for 10 days from 23-dec
        # 2011:"; "15 oct 2013, 17 oct 2013 and 1 nov 2013".
        self.occurrenceDateTime = None
        # type = string

        # the timing schedule for the use of the device. the schedule data type
        # allows many different expressions, for example. "every 8 hours"; "three
        # times a day"; "1/2 an hour before breakfast for 10 days from 23-dec
        # 2011:"; "15 oct 2013, 17 oct 2013 and 1 nov 2013".
        self.occurrencePeriod = None
        # reference to Period: Period

        # the timing schedule for the use of the device. the schedule data type
        # allows many different expressions, for example. "every 8 hours"; "three
        # times a day"; "1/2 an hour before breakfast for 10 days from 23-dec
        # 2011:"; "15 oct 2013, 17 oct 2013 and 1 nov 2013".
        self.occurrenceTiming = None
        # reference to Timing: Timing

        # when the request transitioned to being actionable.
        self.authoredOn = None
        # type = string

        # the individual who initiated the request and has responsibility for its
        # activation.
        self.requester = None
        # reference to DeviceRequest_Requester: DeviceRequest_Requester

        # desired type of performer for doing the diagnostic testing.
        self.performerType = None
        # reference to CodeableConcept: CodeableConcept

        # the desired perfomer for doing the diagnostic testing.
        self.performer = None
        # reference to Reference: identifier

        # reason or justification for the use of this device.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # reason or justification for the use of this device.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # additional clinical information about the patient that may influence the
        # request fulfilment.  for example, this may includes body where on the
        # subject's the device will be used ( i.e. the target site).
        self.supportingInfo = None
        # type = array
        # reference to Reference: identifier

        # details about this request that were not represented at all or
        # sufficiently in one of the attributes provided in a class. these may
        # include for example a comment, an instruction, or a note associated with
        # the statement.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # key events in the history of the request.
        self.relevantHistory = None
        # type = array
        # reference to Reference: identifier

        # identifiers assigned to this order by the orderer or by the receiver.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'context'},

            {'parent_entity': 'DeviceRequest_Requester',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'requester'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'performerType'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'intent'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'basedOn'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'performer'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'priorRequest'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'note'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'subject'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'definition'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'supportingInfo'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'codeReference'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest',
            'child_variable': 'relevantHistory'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'codeCodeableConcept'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceRequest',
            'child_variable': 'groupIdentifier'},
        ]

class DeviceRequest_Requester(fhirbase):
    """Represents a request for a patient to employ a medical device. The
    device may be an implantable device, or an external assistive device,
    such as a walker.
    """

    def __init__(self, dict_values=None):
        # the device, practitioner, etc. who initiated the request.
        self.agent = None
        # reference to Reference: identifier

        # the organization the device or practitioner was acting on behalf of.
        self.onBehalfOf = None
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest_Requester',
            'child_variable': 'agent'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceRequest_Requester',
            'child_variable': 'onBehalfOf'},
        ]

