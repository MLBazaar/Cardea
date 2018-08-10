from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Annotation import Annotation
from .Identifier import Identifier
from .Reference import Reference
from .Period import Period

class Task(fhirbase):
    """A task to be performed.
    """

    def __init__(self, dict_values=None):
        # this is a task resource
        self.resourceType = 'Task'
        # type = string
        # possible values = Task

        # a reference to a formal or informal definition of the task.  for
        # example, a protocol, a step within a defined workflow definition, etc.
        self.definitionUri = None
        # type = string

        # a reference to a formal or informal definition of the task.  for
        # example, a protocol, a step within a defined workflow definition, etc.
        self.definitionReference = None
        # reference to Reference: identifier

        # basedon refers to a higher-level authorization that triggered the
        # creation of the task.  it references a "request" resource such as a
        # procedurerequest, medicationrequest, procedurerequest, careplan, etc.
        # which is distinct from the "request" resource the task is seeking to
        # fulfil.  this latter resource is referenced by focuson.  for example,
        # based on a procedurerequest (= basedon), a task is created to fulfil a
        # procedurerequest ( = focuson ) to collect a specimen from a patient.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # an identifier that links together multiple tasks and other requests that
        # were created in the same context.
        self.groupIdentifier = None
        # reference to Identifier: Identifier

        # task that this particular task is part of.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # the current status of the task.
        self.status = None
        # type = string
        # possible values = draft, requested, received, accepted, rejected, ready, cancelled, in-progress, on-hold, failed, completed, entered-in-error

        # an explanation as to why this task is held, failed, was refused, etc.
        self.statusReason = None
        # reference to CodeableConcept: CodeableConcept

        # contains business-specific nuances of the business state.
        self.businessStatus = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the "level" of actionability associated with the task.  i.e.
        # is this a proposed task, a planned task, an actionable task, etc.
        self.intent = None
        # type = string

        # indicates how quickly the task should be addressed with respect to other
        # requests.
        self.priority = None
        # type = string

        # a name or code (or both) briefly describing what the task involves.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a free-text description of what is to be performed.
        self.description = None
        # type = string

        # the request being actioned or the resource being manipulated by this
        # task.
        self.focus = None
        # reference to Reference: identifier

        # the entity who benefits from the performance of the service specified in
        # the task (e.g., the patient).
        self._for = None
        # reference to Reference: identifier

        # the healthcare event  (e.g. a patient and healthcare provider
        # interaction) during which this task was created.
        self.context = None
        # reference to Reference: identifier

        # identifies the time action was first taken against the task (start)
        # and/or the time final action was taken against the task prior to marking
        # it as completed (end).
        self.executionPeriod = None
        # reference to Period: Period

        # the date and time this task was created.
        self.authoredOn = None
        # type = string

        # the date and time of last modification to this task.
        self.lastModified = None
        # type = string

        # the creator of the task.
        self.requester = None
        # reference to Task_Requester: Task_Requester

        # the type of participant that can execute the task.
        self.performerType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # individual organization or device currently responsible for task
        # execution.
        self.owner = None
        # reference to Reference: identifier

        # a description or code indicating why this task needs to be performed.
        self.reason = None
        # reference to CodeableConcept: CodeableConcept

        # free-text information captured about the task as it progresses.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # links to provenance records for past versions of this task that identify
        # key state transitions or updates that are likely to be relevant to a
        # user looking at the current version of the task.
        self.relevantHistory = None
        # type = array
        # reference to Reference: identifier

        # if the task.focus is a request resource and the task is seeking
        # fulfillment (i.e is asking for the request to be actioned), this element
        # identifies any limitations on what parts of the referenced request
        # should be actioned.
        self.restriction = None
        # reference to Task_Restriction: Task_Restriction

        # additional information that may be needed in the execution of the task.
        self.input = None
        # type = array
        # reference to Task_Input: Task_Input

        # outputs produced by the task.
        self.output = None
        # type = array
        # reference to Task_Output: Task_Output

        # the business identifier for this task.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'requested', 'received', 'accepted', 'rejected', 'ready', 'cancelled', 'in-progress', 'on-hold', 'failed', 'completed', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, requested, received, accepted, rejected, ready, cancelled, in-progress, on-hold, failed, completed, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'statusReason'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'basedOn'},

            {'parent_entity': 'Task_Output',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'output'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'performerType'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'code'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'note'},

            {'parent_entity': 'Task_Input',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'input'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'for'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'businessStatus'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'definitionReference'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'relevantHistory'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'reason'},

            {'parent_entity': 'Task_Restriction',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'restriction'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'focus'},

            {'parent_entity': 'Task_Requester',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'requester'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'owner'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'identifier'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Task',
            'child_variable': 'executionPeriod'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task',
            'child_variable': 'context'},
        ]

class Task_Requester(fhirbase):
    """A task to be performed.
    """

    def __init__(self, dict_values=None):
        # the device, practitioner, etc. who initiated the task.
        self.agent = None
        # reference to Reference: identifier

        # the organization the device or practitioner was acting on behalf of when
        # they initiated the task.
        self.onBehalfOf = None
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task_Requester',
            'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task_Requester',
            'child_variable': 'agent'},
        ]

class Task_Restriction(fhirbase):
    """A task to be performed.
    """

    def __init__(self, dict_values=None):
        # indicates the number of times the requested action should occur.
        self.repetitions = None
        # type = int

        # over what time-period is fulfillment sought.
        self.period = None
        # reference to Period: Period

        # for requests that are targeted to more than on potential
        # recipient/target, for whom is fulfillment sought?
        self.recipient = None
        # type = array
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task_Restriction',
            'child_variable': 'recipient'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Restriction',
            'child_variable': 'period'},
        ]

class Task_Input(fhirbase):
    """A task to be performed.
    """

    def __init__(self, dict_values=None):
        # a code or description indicating how the input is intended to be used as
        # part of the task execution.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the value of the input parameter as a basic type.
        self.valueBoolean = None
        # type = boolean

        # the value of the input parameter as a basic type.
        self.valueInteger = None
        # type = int

        # the value of the input parameter as a basic type.
        self.valueDecimal = None
        # type = int

        # the value of the input parameter as a basic type.
        self.valueBase64Binary = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueInstant = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueString = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueUri = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueDate = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueDateTime = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueTime = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueCode = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueOid = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueUuid = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueId = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueUnsignedInt = None
        # type = int

        # the value of the input parameter as a basic type.
        self.valuePositiveInt = None
        # type = int

        # the value of the input parameter as a basic type.
        self.valueMarkdown = None
        # type = string

        # the value of the input parameter as a basic type.
        self.valueElement = None
        # reference to Element: id

        # the value of the input parameter as a basic type.
        self.valueExtension = None
        # reference to Extension: Extension

        # the value of the input parameter as a basic type.
        self.valueBackboneElement = None
        # reference to BackboneElement: BackboneElement

        # the value of the input parameter as a basic type.
        self.valueNarrative = None
        # reference to Narrative: Narrative

        # the value of the input parameter as a basic type.
        self.valueAnnotation = None
        # reference to Annotation: Annotation

        # the value of the input parameter as a basic type.
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # the value of the input parameter as a basic type.
        self.valueIdentifier = None
        # reference to Identifier: Identifier

        # the value of the input parameter as a basic type.
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the value of the input parameter as a basic type.
        self.valueCoding = None
        # reference to Coding: Coding

        # the value of the input parameter as a basic type.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # the value of the input parameter as a basic type.
        self.valueDuration = None
        # reference to Duration: Duration

        # the value of the input parameter as a basic type.
        self.valueSimpleQuantity = None
        # reference to Quantity: Quantity

        # the value of the input parameter as a basic type.
        self.valueDistance = None
        # reference to Distance: Distance

        # the value of the input parameter as a basic type.
        self.valueCount = None
        # reference to Count: Count

        # the value of the input parameter as a basic type.
        self.valueMoney = None
        # reference to Money: Money

        # the value of the input parameter as a basic type.
        self.valueAge = None
        # reference to Age: Age

        # the value of the input parameter as a basic type.
        self.valueRange = None
        # reference to Range: Range

        # the value of the input parameter as a basic type.
        self.valuePeriod = None
        # reference to Period: Period

        # the value of the input parameter as a basic type.
        self.valueRatio = None
        # reference to Ratio: Ratio

        # the value of the input parameter as a basic type.
        self.valueReference = None
        # reference to Reference: identifier

        # the value of the input parameter as a basic type.
        self.valueSampledData = None
        # reference to SampledData: SampledData

        # the value of the input parameter as a basic type.
        self.valueSignature = None
        # reference to Signature: Signature

        # the value of the input parameter as a basic type.
        self.valueHumanName = None
        # reference to HumanName: HumanName

        # the value of the input parameter as a basic type.
        self.valueAddress = None
        # reference to Address: Address

        # the value of the input parameter as a basic type.
        self.valueContactPoint = None
        # reference to ContactPoint: ContactPoint

        # the value of the input parameter as a basic type.
        self.valueTiming = None
        # reference to Timing: Timing

        # the value of the input parameter as a basic type.
        self.valueMeta = None
        # reference to Meta: Meta

        # the value of the input parameter as a basic type.
        self.valueElementDefinition = None
        # reference to ElementDefinition: ElementDefinition

        # the value of the input parameter as a basic type.
        self.valueContactDetail = None
        # reference to ContactDetail: ContactDetail

        # the value of the input parameter as a basic type.
        self.valueContributor = None
        # reference to Contributor: Contributor

        # the value of the input parameter as a basic type.
        self.valueDosage = None
        # reference to Dosage: Dosage

        # the value of the input parameter as a basic type.
        self.valueRelatedArtifact = None
        # reference to RelatedArtifact: RelatedArtifact

        # the value of the input parameter as a basic type.
        self.valueUsageContext = None
        # reference to UsageContext: UsageContext

        # the value of the input parameter as a basic type.
        self.valueDataRequirement = None
        # reference to DataRequirement: DataRequirement

        # the value of the input parameter as a basic type.
        self.valueParameterDefinition = None
        # reference to ParameterDefinition: ParameterDefinition

        # the value of the input parameter as a basic type.
        self.valueTriggerDefinition = None
        # reference to TriggerDefinition: TriggerDefinition


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Element',
            'parent_variable': 'id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueElement'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueQuantity'},

            {'parent_entity': 'ElementDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueHumanName'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Dosage',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueDosage'},

            {'parent_entity': 'Signature',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueSignature'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueTiming'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Range',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueRange'},

            {'parent_entity': 'Extension',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueExtension'},

            {'parent_entity': 'RelatedArtifact',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'ParameterDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'Narrative',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueNarrative'},

            {'parent_entity': 'DataRequirement',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'Money',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueMoney'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueAttachment'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueAddress'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task_Input',
            'child_variable': 'valueReference'},

            {'parent_entity': 'Contributor',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueContributor'},

            {'parent_entity': 'Duration',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueDuration'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueCoding'},

            {'parent_entity': 'Distance',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueDistance'},

            {'parent_entity': 'BackboneElement',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'Meta',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueMeta'},

            {'parent_entity': 'TriggerDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueContactPoint'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Count',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueCount'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueIdentifier'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'type'},

            {'parent_entity': 'SampledData',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueSampledData'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valuePeriod'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Ratio',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueRatio'},

            {'parent_entity': 'Age',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueAge'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Input',
            'child_variable': 'valueUsageContext'},
        ]

class Task_Output(fhirbase):
    """A task to be performed.
    """

    def __init__(self, dict_values=None):
        # the name of the output parameter.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the value of the output parameter as a basic type.
        self.valueBoolean = None
        # type = boolean

        # the value of the output parameter as a basic type.
        self.valueInteger = None
        # type = int

        # the value of the output parameter as a basic type.
        self.valueDecimal = None
        # type = int

        # the value of the output parameter as a basic type.
        self.valueBase64Binary = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueInstant = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueString = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueUri = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueDate = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueDateTime = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueTime = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueCode = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueOid = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueUuid = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueId = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueUnsignedInt = None
        # type = int

        # the value of the output parameter as a basic type.
        self.valuePositiveInt = None
        # type = int

        # the value of the output parameter as a basic type.
        self.valueMarkdown = None
        # type = string

        # the value of the output parameter as a basic type.
        self.valueElement = None
        # reference to Element: id

        # the value of the output parameter as a basic type.
        self.valueExtension = None
        # reference to Extension: Extension

        # the value of the output parameter as a basic type.
        self.valueBackboneElement = None
        # reference to BackboneElement: BackboneElement

        # the value of the output parameter as a basic type.
        self.valueNarrative = None
        # reference to Narrative: Narrative

        # the value of the output parameter as a basic type.
        self.valueAnnotation = None
        # reference to Annotation: Annotation

        # the value of the output parameter as a basic type.
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # the value of the output parameter as a basic type.
        self.valueIdentifier = None
        # reference to Identifier: Identifier

        # the value of the output parameter as a basic type.
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the value of the output parameter as a basic type.
        self.valueCoding = None
        # reference to Coding: Coding

        # the value of the output parameter as a basic type.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # the value of the output parameter as a basic type.
        self.valueDuration = None
        # reference to Duration: Duration

        # the value of the output parameter as a basic type.
        self.valueSimpleQuantity = None
        # reference to Quantity: Quantity

        # the value of the output parameter as a basic type.
        self.valueDistance = None
        # reference to Distance: Distance

        # the value of the output parameter as a basic type.
        self.valueCount = None
        # reference to Count: Count

        # the value of the output parameter as a basic type.
        self.valueMoney = None
        # reference to Money: Money

        # the value of the output parameter as a basic type.
        self.valueAge = None
        # reference to Age: Age

        # the value of the output parameter as a basic type.
        self.valueRange = None
        # reference to Range: Range

        # the value of the output parameter as a basic type.
        self.valuePeriod = None
        # reference to Period: Period

        # the value of the output parameter as a basic type.
        self.valueRatio = None
        # reference to Ratio: Ratio

        # the value of the output parameter as a basic type.
        self.valueReference = None
        # reference to Reference: identifier

        # the value of the output parameter as a basic type.
        self.valueSampledData = None
        # reference to SampledData: SampledData

        # the value of the output parameter as a basic type.
        self.valueSignature = None
        # reference to Signature: Signature

        # the value of the output parameter as a basic type.
        self.valueHumanName = None
        # reference to HumanName: HumanName

        # the value of the output parameter as a basic type.
        self.valueAddress = None
        # reference to Address: Address

        # the value of the output parameter as a basic type.
        self.valueContactPoint = None
        # reference to ContactPoint: ContactPoint

        # the value of the output parameter as a basic type.
        self.valueTiming = None
        # reference to Timing: Timing

        # the value of the output parameter as a basic type.
        self.valueMeta = None
        # reference to Meta: Meta

        # the value of the output parameter as a basic type.
        self.valueElementDefinition = None
        # reference to ElementDefinition: ElementDefinition

        # the value of the output parameter as a basic type.
        self.valueContactDetail = None
        # reference to ContactDetail: ContactDetail

        # the value of the output parameter as a basic type.
        self.valueContributor = None
        # reference to Contributor: Contributor

        # the value of the output parameter as a basic type.
        self.valueDosage = None
        # reference to Dosage: Dosage

        # the value of the output parameter as a basic type.
        self.valueRelatedArtifact = None
        # reference to RelatedArtifact: RelatedArtifact

        # the value of the output parameter as a basic type.
        self.valueUsageContext = None
        # reference to UsageContext: UsageContext

        # the value of the output parameter as a basic type.
        self.valueDataRequirement = None
        # reference to DataRequirement: DataRequirement

        # the value of the output parameter as a basic type.
        self.valueParameterDefinition = None
        # reference to ParameterDefinition: ParameterDefinition

        # the value of the output parameter as a basic type.
        self.valueTriggerDefinition = None
        # reference to TriggerDefinition: TriggerDefinition


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Distance',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueDistance'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueContactPoint'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'type'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueCoding'},

            {'parent_entity': 'Range',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueRange'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Extension',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueExtension'},

            {'parent_entity': 'SampledData',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueSampledData'},

            {'parent_entity': 'Duration',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueDuration'},

            {'parent_entity': 'ParameterDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'Narrative',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueNarrative'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valuePeriod'},

            {'parent_entity': 'Signature',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueSignature'},

            {'parent_entity': 'Count',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueCount'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueIdentifier'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueQuantity'},

            {'parent_entity': 'Money',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueMoney'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueAttachment'},

            {'parent_entity': 'DataRequirement',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'BackboneElement',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'Contributor',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueContributor'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Element',
            'parent_variable': 'id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueElement'},

            {'parent_entity': 'TriggerDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Meta',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueMeta'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Task_Output',
            'child_variable': 'valueReference'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Dosage',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueDosage'},

            {'parent_entity': 'Age',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueAge'},

            {'parent_entity': 'RelatedArtifact',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'ElementDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueAddress'},

            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueHumanName'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueTiming'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Ratio',
            'parent_variable': 'object_id',
            'child_entity': 'Task_Output',
            'child_variable': 'valueRatio'},
        ]

