from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Annotation import Annotation
from .Timing import Timing
from .Reference import Reference
from .Period import Period

class ProcedureRequest(fhirbase):
    """A record of a request for diagnostic investigations, treatments, or
    operations to be performed.
    """

    def __init__(self, dict_values=None):
        # this is a procedurerequest resource
        self.resourceType = 'ProcedureRequest'
        # type = string
        # possible values = ProcedureRequest

        # protocol or definition followed by this request.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # plan/proposal/order fulfilled by this request.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # the request takes the place of the referenced completed or terminated
        # request(s).
        self.replaces = None
        # type = array
        # reference to Reference: identifier

        # a shared identifier common to all procedure or diagnostic requests that
        # were authorized more or less simultaneously by a single author,
        # representing the composite or group identifier.
        self.requisition = None
        # reference to Identifier: Identifier

        # the status of the order.
        self.status = None
        # type = string

        # whether the request is a proposal, plan, an original order or a reflex
        # order.
        self.intent = None
        # type = string

        # indicates how quickly the procedurerequest should be addressed with
        # respect to other requests.
        self.priority = None
        # type = string

        # set this to true if the record is saying that the procedure should not
        # be performed.
        self.doNotPerform = None
        # type = boolean

        # a code that classifies the procedure for searching, sorting and display
        # purposes (e.g. "surgical procedure").
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a code that identifies a particular procedure, diagnostic investigation,
        # or panel of investigations, that have been requested.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # on whom or what the procedure or diagnostic is to be performed. this is
        # usually a human patient, but can also be requested on animals, groups of
        # humans or animals, devices such as dialysis machines, or even locations
        # (typically for environmental scans).
        self.subject = None
        # reference to Reference: identifier

        # an encounter or episode of care that provides additional information
        # about the healthcare context in which this request is made.
        self.context = None
        # reference to Reference: identifier

        # the date/time at which the diagnostic testing should occur.
        self.occurrenceDateTime = None
        # type = string

        # the date/time at which the diagnostic testing should occur.
        self.occurrencePeriod = None
        # reference to Period: Period

        # the date/time at which the diagnostic testing should occur.
        self.occurrenceTiming = None
        # reference to Timing: Timing

        # if a codeableconcept is present, it indicates the pre-condition for
        # performing the procedure.  for example "pain", "on flare-up", etc.
        self.asNeededBoolean = None
        # type = boolean

        # if a codeableconcept is present, it indicates the pre-condition for
        # performing the procedure.  for example "pain", "on flare-up", etc.
        self.asNeededCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # when the request transitioned to being actionable.
        self.authoredOn = None
        # type = string

        # the individual who initiated the request and has responsibility for its
        # activation.
        self.requester = None
        # reference to ProcedureRequest_Requester: ProcedureRequest_Requester

        # desired type of performer for doing the diagnostic testing.
        self.performerType = None
        # reference to CodeableConcept: CodeableConcept

        # the desired perfomer for doing the diagnostic testing.  for example, the
        # surgeon, dermatopathologist, endoscopist, etc.
        self.performer = None
        # reference to Reference: identifier

        # an explanation or justification for why this diagnostic investigation is
        # being requested in coded or textual form.   this is often for billing
        # purposes.  may relate to the resources referred to in
        # supportinginformation.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates another resource that provides a justification for why this
        # diagnostic investigation is being requested.   may relate to the
        # resources referred to in supportinginformation.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # additional clinical information about the patient or specimen that may
        # influence the procedure or diagnostics or their interpretations.
        # this information includes diagnosis, clinical findings and other
        # observations.  in laboratory ordering these are typically referred to as
        # "ask at order entry questions (aoes)".  this includes observations
        # explicitly requested by the producer (filler) to provide context or
        # supporting information needed to complete the order. for example,
        # reporting the amount of inspired oxygen for blood gas measurements.
        self.supportingInfo = None
        # type = array
        # reference to Reference: identifier

        # one or more specimens that the laboratory procedure will use.
        self.specimen = None
        # type = array
        # reference to Reference: identifier

        # anatomic location where the procedure should be performed. this is the
        # target site.
        self.bodySite = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # any other notes and comments made about the service request. for
        # example, letting provider know that "patient hates needles" or other
        # provider instructions.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # key events in the history of the request.
        self.relevantHistory = None
        # type = array
        # reference to Reference: identifier

        # identifiers assigned to this order instance by the orderer and/or the
        # receiver and/or order fulfiller.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'performer'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'category'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'context'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'asNeededCodeableConcept'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'relevantHistory'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'supportingInfo'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'performerType'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'specimen'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'requisition'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'bodySite'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'note'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'definition'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'subject'},

            {'parent_entity': 'ProcedureRequest_Requester',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'requester'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'ProcedureRequest',
            'child_variable': 'occurrenceTiming'},
        ]

class ProcedureRequest_Requester(fhirbase):
    """A record of a request for diagnostic investigations, treatments, or
    operations to be performed.
    """

    def __init__(self, dict_values=None):
        # the device, practitioner or organization who initiated the request.
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
            'child_entity': 'ProcedureRequest_Requester',
            'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcedureRequest_Requester',
            'child_variable': 'agent'},
        ]

