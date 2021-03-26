from .fhirbase import fhirbase


class Task(fhirbase):
    """
    A task to be performed.

    Args:
        resourceType: This is a Task resource
        identifier: The business identifier for this task.
        definitionUri: A reference to a formal or informal definition of the
            task.  For example, a protocol, a step within a defined workflow
            definition, etc.
        definitionReference: A reference to a formal or informal definition of
            the task.  For example, a protocol, a step within a defined workflow
            definition, etc.
        basedOn: BasedOn refers to a higher-level authorization that triggered
            the creation of the task.  It references a "request" resource such as
            a ProcedureRequest, MedicationRequest, ProcedureRequest, CarePlan,
            etc. which is distinct from the "request" resource the task is seeking
            to fulfil.  This latter resource is referenced by FocusOn.  For
            example, based on a ProcedureRequest (= BasedOn), a task is created to
            fulfil a procedureRequest ( = FocusOn ) to collect a specimen from a
            patient.
        groupIdentifier: An identifier that links together multiple tasks and
            other requests that were created in the same context.
        partOf: Task that this particular task is part of.
        status: The current status of the task.
        statusReason: An explanation as to why this task is held, failed, was
            refused, etc.
        businessStatus: Contains business-specific nuances of the business
            state.
        intent: Indicates the "level" of actionability associated with the
            Task.  I.e. Is this a proposed task, a planned task, an actionable
            task, etc.
        priority: Indicates how quickly the Task should be addressed with
            respect to other requests.
        code: A name or code (or both) briefly describing what the task
            involves.
        description: A free-text description of what is to be performed.
        focus: The request being actioned or the resource being manipulated by
            this task.
        for: The entity who benefits from the performance of the service
            specified in the task (e.g., the patient).
        context: The healthcare event  (e.g. a patient and healthcare provider
            interaction) during which this task was created.
        executionPeriod: Identifies the time action was first taken against
            the task (start) and/or the time final action was taken against the
            task prior to marking it as completed (end).
        authoredOn: The date and time this task was created.
        lastModified: The date and time of last modification to this task.
        requester: The creator of the task.
        performerType: The type of participant that can execute the task.
        owner: Individual organization or Device currently responsible for
            task execution.
        reason: A description or code indicating why this task needs to be
            performed.
        note: Free-text information captured about the task as it progresses.
        relevantHistory: Links to Provenance records for past versions of this
            Task that identify key state transitions or updates that are likely to
            be relevant to a user looking at the current version of the task.
        restriction: If the Task.focus is a request resource and the task is
            seeking fulfillment (i.e is asking for the request to be actioned),
            this element identifies any limitations on what parts of the
            referenced request should be actioned.
        input: Additional information that may be needed in the execution of
            the task.
        output: Outputs produced by the Task.
    """

    __name__ = 'Task'

    def __init__(self, dict_values=None):
        self.resourceType = 'Task'
        # type: str
        # possible values: Task

        self.definitionUri = None
        # type: str

        self.definitionReference = None
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.groupIdentifier = None
        # reference to Identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: draft, requested, received, accepted,
        # rejected, ready, cancelled, in-progress, on-hold, failed, completed,
        # entered-in-error

        self.statusReason = None
        # reference to CodeableConcept

        self.businessStatus = None
        # reference to CodeableConcept

        self.intent = None
        # type: str

        self.priority = None
        # type: str

        self.code = None
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.focus = None
        # reference to Reference: identifier

        self._for = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.executionPeriod = None
        # reference to Period

        self.authoredOn = None
        # type: str

        self.lastModified = None
        # type: str

        self.requester = None
        # reference to Task_Requester

        self.performerType = None
        # type: list
        # reference to CodeableConcept

        self.owner = None
        # reference to Reference: identifier

        self.reason = None
        # reference to CodeableConcept

        self.note = None
        # type: list
        # reference to Annotation

        self.relevantHistory = None
        # type: list
        # reference to Reference: identifier

        self.restriction = None
        # reference to Task_Restriction

        self.input = None
        # type: list
        # reference to Task_Input

        self.output = None
        # type: list
        # reference to Task_Output

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'draft', 'requested', 'received', 'accepted', 'rejected', 'ready',
                    'cancelled', 'in-progress', 'on-hold', 'failed', 'completed',
                        'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, requested, received, accepted, rejected, ready, cancelled,'
                        'in-progress, on-hold, failed, completed, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'context'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'performerType'},

            {'parent_entity': 'Task_Restriction',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'restriction'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'executionPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'focus'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'reason'},

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
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'Task_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'requester'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'definitionReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'owner'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'statusReason'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': '_for'},

            {'parent_entity': 'Task_Output',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'output'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'businessStatus'},
        ]


class Task_Requester(fhirbase):
    """
    A task to be performed.

    Args:
        agent: The device, practitioner, etc. who initiated the task.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of when they initiated the task.
    """

    __name__ = 'Task_Requester'

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
             'child_entity': 'Task_Requester',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task_Requester',
             'child_variable': 'agent'},
        ]


class Task_Restriction(fhirbase):
    """
    A task to be performed.

    Args:
        repetitions: Indicates the number of times the requested action should
            occur.
        period: Over what time-period is fulfillment sought.
        recipient: For requests that are targeted to more than on potential
            recipient/target, for whom is fulfillment sought?
    """

    __name__ = 'Task_Restriction'

    def __init__(self, dict_values=None):
        self.repetitions = None
        # type: int

        self.period = None
        # reference to Period

        self.recipient = None
        # type: list
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Restriction',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task_Restriction',
             'child_variable': 'recipient'},
        ]


class Task_Input(fhirbase):
    """
    A task to be performed.

    Args:
        type: A code or description indicating how the input is intended to be
            used as part of the task execution.
        valueBoolean: The value of the input parameter as a basic type.
        valueInteger: The value of the input parameter as a basic type.
        valueDecimal: The value of the input parameter as a basic type.
        valueBase64Binary: The value of the input parameter as a basic type.
        valueInstant: The value of the input parameter as a basic type.
        valueString: The value of the input parameter as a basic type.
        valueUri: The value of the input parameter as a basic type.
        valueDate: The value of the input parameter as a basic type.
        valueDateTime: The value of the input parameter as a basic type.
        valueTime: The value of the input parameter as a basic type.
        valueCode: The value of the input parameter as a basic type.
        valueOid: The value of the input parameter as a basic type.
        valueUuid: The value of the input parameter as a basic type.
        valueId: The value of the input parameter as a basic type.
        valueUnsignedInt: The value of the input parameter as a basic type.
        valuePositiveInt: The value of the input parameter as a basic type.
        valueMarkdown: The value of the input parameter as a basic type.
        valueElement: The value of the input parameter as a basic type.
        valueExtension: The value of the input parameter as a basic type.
        valueBackboneElement: The value of the input parameter as a basic
            type.
        valueNarrative: The value of the input parameter as a basic type.
        valueAnnotation: The value of the input parameter as a basic type.
        valueAttachment: The value of the input parameter as a basic type.
        valueIdentifier: The value of the input parameter as a basic type.
        valueCodeableConcept: The value of the input parameter as a basic
            type.
        valueCoding: The value of the input parameter as a basic type.
        valueQuantity: The value of the input parameter as a basic type.
        valueDuration: The value of the input parameter as a basic type.
        valueSimpleQuantity: The value of the input parameter as a basic type.
        valueDistance: The value of the input parameter as a basic type.
        valueCount: The value of the input parameter as a basic type.
        valueMoney: The value of the input parameter as a basic type.
        valueAge: The value of the input parameter as a basic type.
        valueRange: The value of the input parameter as a basic type.
        valuePeriod: The value of the input parameter as a basic type.
        valueRatio: The value of the input parameter as a basic type.
        valueReference: The value of the input parameter as a basic type.
        valueSampledData: The value of the input parameter as a basic type.
        valueSignature: The value of the input parameter as a basic type.
        valueHumanName: The value of the input parameter as a basic type.
        valueAddress: The value of the input parameter as a basic type.
        valueContactPoint: The value of the input parameter as a basic type.
        valueTiming: The value of the input parameter as a basic type.
        valueMeta: The value of the input parameter as a basic type.
        valueElementDefinition: The value of the input parameter as a basic
            type.
        valueContactDetail: The value of the input parameter as a basic type.
        valueContributor: The value of the input parameter as a basic type.
        valueDosage: The value of the input parameter as a basic type.
        valueRelatedArtifact: The value of the input parameter as a basic
            type.
        valueUsageContext: The value of the input parameter as a basic type.
        valueDataRequirement: The value of the input parameter as a basic
            type.
        valueParameterDefinition: The value of the input parameter as a basic
            type.
        valueTriggerDefinition: The value of the input parameter as a basic
            type.
    """

    __name__ = 'Task_Input'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.valueBoolean = None
        # type: bool

        self.valueInteger = None
        # type: int

        self.valueDecimal = None
        # type: int

        self.valueBase64Binary = None
        # type: str

        self.valueInstant = None
        # type: str

        self.valueString = None
        # type: str

        self.valueUri = None
        # type: str

        self.valueDate = None
        # type: str

        self.valueDateTime = None
        # type: str

        self.valueTime = None
        # type: str

        self.valueCode = None
        # type: str

        self.valueOid = None
        # type: str

        self.valueUuid = None
        # type: str

        self.valueId = None
        # type: str

        self.valueUnsignedInt = None
        # type: int

        self.valuePositiveInt = None
        # type: int

        self.valueMarkdown = None
        # type: str

        self.valueElement = None
        # reference to Element: id

        self.valueExtension = None
        # reference to Extension

        self.valueBackboneElement = None
        # reference to BackboneElement

        self.valueNarrative = None
        # reference to Narrative

        self.valueAnnotation = None
        # reference to Annotation

        self.valueAttachment = None
        # reference to Attachment

        self.valueIdentifier = None
        # reference to Identifier

        self.valueCodeableConcept = None
        # reference to CodeableConcept

        self.valueCoding = None
        # reference to Coding

        self.valueQuantity = None
        # reference to Quantity

        self.valueDuration = None
        # reference to Duration

        self.valueSimpleQuantity = None
        # reference to Quantity

        self.valueDistance = None
        # reference to Distance

        self.valueCount = None
        # reference to Count

        self.valueMoney = None
        # reference to Money

        self.valueAge = None
        # reference to Age

        self.valueRange = None
        # reference to Range

        self.valuePeriod = None
        # reference to Period

        self.valueRatio = None
        # reference to Ratio

        self.valueReference = None
        # reference to Reference: identifier

        self.valueSampledData = None
        # reference to SampledData

        self.valueSignature = None
        # reference to Signature

        self.valueHumanName = None
        # reference to HumanName

        self.valueAddress = None
        # reference to Address

        self.valueContactPoint = None
        # reference to ContactPoint

        self.valueTiming = None
        # reference to Timing

        self.valueMeta = None
        # reference to Meta

        self.valueElementDefinition = None
        # reference to ElementDefinition

        self.valueContactDetail = None
        # reference to ContactDetail

        self.valueContributor = None
        # reference to Contributor

        self.valueDosage = None
        # reference to Dosage

        self.valueRelatedArtifact = None
        # reference to RelatedArtifact

        self.valueUsageContext = None
        # reference to UsageContext

        self.valueDataRequirement = None
        # reference to DataRequirement

        self.valueParameterDefinition = None
        # reference to ParameterDefinition

        self.valueTriggerDefinition = None
        # reference to TriggerDefinition

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueContributor'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task_Input',
             'child_variable': 'valueReference'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDuration'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueSignature'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueElement'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'type'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueCount'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAge'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueSampledData'},
        ]


class Task_Output(fhirbase):
    """
    A task to be performed.

    Args:
        type: The name of the Output parameter.
        valueBoolean: The value of the Output parameter as a basic type.
        valueInteger: The value of the Output parameter as a basic type.
        valueDecimal: The value of the Output parameter as a basic type.
        valueBase64Binary: The value of the Output parameter as a basic type.
        valueInstant: The value of the Output parameter as a basic type.
        valueString: The value of the Output parameter as a basic type.
        valueUri: The value of the Output parameter as a basic type.
        valueDate: The value of the Output parameter as a basic type.
        valueDateTime: The value of the Output parameter as a basic type.
        valueTime: The value of the Output parameter as a basic type.
        valueCode: The value of the Output parameter as a basic type.
        valueOid: The value of the Output parameter as a basic type.
        valueUuid: The value of the Output parameter as a basic type.
        valueId: The value of the Output parameter as a basic type.
        valueUnsignedInt: The value of the Output parameter as a basic type.
        valuePositiveInt: The value of the Output parameter as a basic type.
        valueMarkdown: The value of the Output parameter as a basic type.
        valueElement: The value of the Output parameter as a basic type.
        valueExtension: The value of the Output parameter as a basic type.
        valueBackboneElement: The value of the Output parameter as a basic
            type.
        valueNarrative: The value of the Output parameter as a basic type.
        valueAnnotation: The value of the Output parameter as a basic type.
        valueAttachment: The value of the Output parameter as a basic type.
        valueIdentifier: The value of the Output parameter as a basic type.
        valueCodeableConcept: The value of the Output parameter as a basic
            type.
        valueCoding: The value of the Output parameter as a basic type.
        valueQuantity: The value of the Output parameter as a basic type.
        valueDuration: The value of the Output parameter as a basic type.
        valueSimpleQuantity: The value of the Output parameter as a basic
            type.
        valueDistance: The value of the Output parameter as a basic type.
        valueCount: The value of the Output parameter as a basic type.
        valueMoney: The value of the Output parameter as a basic type.
        valueAge: The value of the Output parameter as a basic type.
        valueRange: The value of the Output parameter as a basic type.
        valuePeriod: The value of the Output parameter as a basic type.
        valueRatio: The value of the Output parameter as a basic type.
        valueReference: The value of the Output parameter as a basic type.
        valueSampledData: The value of the Output parameter as a basic type.
        valueSignature: The value of the Output parameter as a basic type.
        valueHumanName: The value of the Output parameter as a basic type.
        valueAddress: The value of the Output parameter as a basic type.
        valueContactPoint: The value of the Output parameter as a basic type.
        valueTiming: The value of the Output parameter as a basic type.
        valueMeta: The value of the Output parameter as a basic type.
        valueElementDefinition: The value of the Output parameter as a basic
            type.
        valueContactDetail: The value of the Output parameter as a basic type.
        valueContributor: The value of the Output parameter as a basic type.
        valueDosage: The value of the Output parameter as a basic type.
        valueRelatedArtifact: The value of the Output parameter as a basic
            type.
        valueUsageContext: The value of the Output parameter as a basic type.
        valueDataRequirement: The value of the Output parameter as a basic
            type.
        valueParameterDefinition: The value of the Output parameter as a basic
            type.
        valueTriggerDefinition: The value of the Output parameter as a basic
            type.
    """

    __name__ = 'Task_Output'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.valueBoolean = None
        # type: bool

        self.valueInteger = None
        # type: int

        self.valueDecimal = None
        # type: int

        self.valueBase64Binary = None
        # type: str

        self.valueInstant = None
        # type: str

        self.valueString = None
        # type: str

        self.valueUri = None
        # type: str

        self.valueDate = None
        # type: str

        self.valueDateTime = None
        # type: str

        self.valueTime = None
        # type: str

        self.valueCode = None
        # type: str

        self.valueOid = None
        # type: str

        self.valueUuid = None
        # type: str

        self.valueId = None
        # type: str

        self.valueUnsignedInt = None
        # type: int

        self.valuePositiveInt = None
        # type: int

        self.valueMarkdown = None
        # type: str

        self.valueElement = None
        # reference to Element: id

        self.valueExtension = None
        # reference to Extension

        self.valueBackboneElement = None
        # reference to BackboneElement

        self.valueNarrative = None
        # reference to Narrative

        self.valueAnnotation = None
        # reference to Annotation

        self.valueAttachment = None
        # reference to Attachment

        self.valueIdentifier = None
        # reference to Identifier

        self.valueCodeableConcept = None
        # reference to CodeableConcept

        self.valueCoding = None
        # reference to Coding

        self.valueQuantity = None
        # reference to Quantity

        self.valueDuration = None
        # reference to Duration

        self.valueSimpleQuantity = None
        # reference to Quantity

        self.valueDistance = None
        # reference to Distance

        self.valueCount = None
        # reference to Count

        self.valueMoney = None
        # reference to Money

        self.valueAge = None
        # reference to Age

        self.valueRange = None
        # reference to Range

        self.valuePeriod = None
        # reference to Period

        self.valueRatio = None
        # reference to Ratio

        self.valueReference = None
        # reference to Reference: identifier

        self.valueSampledData = None
        # reference to SampledData

        self.valueSignature = None
        # reference to Signature

        self.valueHumanName = None
        # reference to HumanName

        self.valueAddress = None
        # reference to Address

        self.valueContactPoint = None
        # reference to ContactPoint

        self.valueTiming = None
        # reference to Timing

        self.valueMeta = None
        # reference to Meta

        self.valueElementDefinition = None
        # reference to ElementDefinition

        self.valueContactDetail = None
        # reference to ContactDetail

        self.valueContributor = None
        # reference to Contributor

        self.valueDosage = None
        # reference to Dosage

        self.valueRelatedArtifact = None
        # reference to RelatedArtifact

        self.valueUsageContext = None
        # reference to UsageContext

        self.valueDataRequirement = None
        # reference to DataRequirement

        self.valueParameterDefinition = None
        # reference to ParameterDefinition

        self.valueTriggerDefinition = None
        # reference to TriggerDefinition

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueSignature'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task_Output',
             'child_variable': 'valueReference'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAge'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueElement'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueCount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'type'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDuration'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueContributor'},
        ]
