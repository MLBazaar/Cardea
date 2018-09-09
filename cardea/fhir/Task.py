from .fhirbase import fhirbase


class Task(fhirbase):
    """
    A task to be performed.
    """

    __name__ = 'Task'

    def __init__(self, dict_values=None):
        self.resourceType = 'Task'
        """
        This is a Task resource

        type: string
        possible values: Task
        """

        self.definitionUri = None
        """
        A reference to a formal or informal definition of the task.  For
        example, a protocol, a step within a defined workflow definition, etc.

        type: string
        """

        self.definitionReference = None
        """
        A reference to a formal or informal definition of the task.  For
        example, a protocol, a step within a defined workflow definition, etc.

        reference to Reference: identifier
        """

        self.basedOn = None
        """
        BasedOn refers to a higher-level authorization that triggered the
        creation of the task.  It references a "request" resource such as a
        ProcedureRequest, MedicationRequest, ProcedureRequest, CarePlan, etc.
        which is distinct from the "request" resource the task is seeking to
        fulfil.  This latter resource is referenced by FocusOn.  For example,
        based on a ProcedureRequest (= BasedOn), a task is created to fulfil a
        procedureRequest ( = FocusOn ) to collect a specimen from a patient.

        type: array
        reference to Reference: identifier
        """

        self.groupIdentifier = None
        """
        An identifier that links together multiple tasks and other requests
        that were created in the same context.

        reference to Identifier
        """

        self.partOf = None
        """
        Task that this particular task is part of.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        The current status of the task.

        type: string
        possible values: draft, requested, received, accepted,
        rejected, ready, cancelled, in-progress, on-hold, failed, completed,
        entered-in-error
        """

        self.statusReason = None
        """
        An explanation as to why this task is held, failed, was refused, etc.

        reference to CodeableConcept
        """

        self.businessStatus = None
        """
        Contains business-specific nuances of the business state.

        reference to CodeableConcept
        """

        self.intent = None
        """
        Indicates the "level" of actionability associated with the Task.  I.e.
        Is this a proposed task, a planned task, an actionable task, etc.

        type: string
        """

        self.priority = None
        """
        Indicates how quickly the Task should be addressed with respect to
        other requests.

        type: string
        """

        self.code = None
        """
        A name or code (or both) briefly describing what the task involves.

        reference to CodeableConcept
        """

        self.description = None
        """
        A free-text description of what is to be performed.

        type: string
        """

        self.focus = None
        """
        The request being actioned or the resource being manipulated by this
        task.

        reference to Reference: identifier
        """

        self._for = None
        """
        The entity who benefits from the performance of the service specified
        in the task (e.g., the patient).

        reference to Reference: identifier
        """

        self.context = None
        """
        The healthcare event  (e.g. a patient and healthcare provider
        interaction) during which this task was created.

        reference to Reference: identifier
        """

        self.executionPeriod = None
        """
        Identifies the time action was first taken against the task (start)
        and/or the time final action was taken against the task prior to
        marking it as completed (end).

        reference to Period
        """

        self.authoredOn = None
        """
        The date and time this task was created.

        type: string
        """

        self.lastModified = None
        """
        The date and time of last modification to this task.

        type: string
        """

        self.requester = None
        """
        The creator of the task.

        reference to Task_Requester
        """

        self.performerType = None
        """
        The type of participant that can execute the task.

        type: array
        reference to CodeableConcept
        """

        self.owner = None
        """
        Individual organization or Device currently responsible for task
        execution.

        reference to Reference: identifier
        """

        self.reason = None
        """
        A description or code indicating why this task needs to be performed.

        reference to CodeableConcept
        """

        self.note = None
        """
        Free-text information captured about the task as it progresses.

        type: array
        reference to Annotation
        """

        self.relevantHistory = None
        """
        Links to Provenance records for past versions of this Task that
        identify key state transitions or updates that are likely to be
        relevant to a user looking at the current version of the task.

        type: array
        reference to Reference: identifier
        """

        self.restriction = None
        """
        If the Task.focus is a request resource and the task is seeking
        fulfillment (i.e is asking for the request to be actioned), this
        element identifies any limitations on what parts of the referenced
        request should be actioned.

        reference to Task_Restriction
        """

        self.input = None
        """
        Additional information that may be needed in the execution of the
        task.

        type: array
        reference to Task_Input
        """

        self.output = None
        """
        Outputs produced by the Task.

        type: array
        reference to Task_Output
        """

        self.identifier = None
        """
        The business identifier for this task.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'businessStatus'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'definitionReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'focus'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'owner'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'executionPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'performerType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'partOf'},

            {'parent_entity': 'Task_Input',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'input'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'statusReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': '_for'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'reason'},

            {'parent_entity': 'Task_Output',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'output'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Task_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'requester'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'code'},

            {'parent_entity': 'Task_Restriction',
             'parent_variable': 'object_id',
             'child_entity': 'Task',
             'child_variable': 'restriction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task',
             'child_variable': 'context'},
        ]


class Task_Requester(fhirbase):
    """
    A task to be performed.
    """

    __name__ = 'Task_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        """
        The device, practitioner, etc. who initiated the task.

        reference to Reference: identifier
        """

        self.onBehalfOf = None
        """
        The organization the device or practitioner was acting on behalf of
        when they initiated the task.

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
             'child_entity': 'Task_Requester',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task_Requester',
             'child_variable': 'onBehalfOf'},
        ]


class Task_Restriction(fhirbase):
    """
    A task to be performed.
    """

    __name__ = 'Task_Restriction'

    def __init__(self, dict_values=None):
        self.repetitions = None
        """
        Indicates the number of times the requested action should occur.

        type: int
        """

        self.period = None
        """
        Over what time-period is fulfillment sought.

        reference to Period
        """

        self.recipient = None
        """
        For requests that are targeted to more than on potential
        recipient/target, for whom is fulfillment sought?

        type: array
        reference to Reference: identifier
        """

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
    """

    __name__ = 'Task_Input'

    def __init__(self, dict_values=None):
        self.type = None
        """
        A code or description indicating how the input is intended to be used
        as part of the task execution.

        reference to CodeableConcept
        """

        self.valueBoolean = None
        """
        The value of the input parameter as a basic type.

        type: boolean
        """

        self.valueInteger = None
        """
        The value of the input parameter as a basic type.

        type: int
        """

        self.valueDecimal = None
        """
        The value of the input parameter as a basic type.

        type: int
        """

        self.valueBase64Binary = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueInstant = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueString = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueUri = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueDate = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueDateTime = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueTime = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueCode = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueOid = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueUuid = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueId = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueUnsignedInt = None
        """
        The value of the input parameter as a basic type.

        type: int
        """

        self.valuePositiveInt = None
        """
        The value of the input parameter as a basic type.

        type: int
        """

        self.valueMarkdown = None
        """
        The value of the input parameter as a basic type.

        type: string
        """

        self.valueElement = None
        """
        The value of the input parameter as a basic type.

        reference to Element: id
        """

        self.valueExtension = None
        """
        The value of the input parameter as a basic type.

        reference to Extension
        """

        self.valueBackboneElement = None
        """
        The value of the input parameter as a basic type.

        reference to BackboneElement
        """

        self.valueNarrative = None
        """
        The value of the input parameter as a basic type.

        reference to Narrative
        """

        self.valueAnnotation = None
        """
        The value of the input parameter as a basic type.

        reference to Annotation
        """

        self.valueAttachment = None
        """
        The value of the input parameter as a basic type.

        reference to Attachment
        """

        self.valueIdentifier = None
        """
        The value of the input parameter as a basic type.

        reference to Identifier
        """

        self.valueCodeableConcept = None
        """
        The value of the input parameter as a basic type.

        reference to CodeableConcept
        """

        self.valueCoding = None
        """
        The value of the input parameter as a basic type.

        reference to Coding
        """

        self.valueQuantity = None
        """
        The value of the input parameter as a basic type.

        reference to Quantity
        """

        self.valueDuration = None
        """
        The value of the input parameter as a basic type.

        reference to Duration
        """

        self.valueSimpleQuantity = None
        """
        The value of the input parameter as a basic type.

        reference to Quantity
        """

        self.valueDistance = None
        """
        The value of the input parameter as a basic type.

        reference to Distance
        """

        self.valueCount = None
        """
        The value of the input parameter as a basic type.

        reference to Count
        """

        self.valueMoney = None
        """
        The value of the input parameter as a basic type.

        reference to Money
        """

        self.valueAge = None
        """
        The value of the input parameter as a basic type.

        reference to Age
        """

        self.valueRange = None
        """
        The value of the input parameter as a basic type.

        reference to Range
        """

        self.valuePeriod = None
        """
        The value of the input parameter as a basic type.

        reference to Period
        """

        self.valueRatio = None
        """
        The value of the input parameter as a basic type.

        reference to Ratio
        """

        self.valueReference = None
        """
        The value of the input parameter as a basic type.

        reference to Reference: identifier
        """

        self.valueSampledData = None
        """
        The value of the input parameter as a basic type.

        reference to SampledData
        """

        self.valueSignature = None
        """
        The value of the input parameter as a basic type.

        reference to Signature
        """

        self.valueHumanName = None
        """
        The value of the input parameter as a basic type.

        reference to HumanName
        """

        self.valueAddress = None
        """
        The value of the input parameter as a basic type.

        reference to Address
        """

        self.valueContactPoint = None
        """
        The value of the input parameter as a basic type.

        reference to ContactPoint
        """

        self.valueTiming = None
        """
        The value of the input parameter as a basic type.

        reference to Timing
        """

        self.valueMeta = None
        """
        The value of the input parameter as a basic type.

        reference to Meta
        """

        self.valueElementDefinition = None
        """
        The value of the input parameter as a basic type.

        reference to ElementDefinition
        """

        self.valueContactDetail = None
        """
        The value of the input parameter as a basic type.

        reference to ContactDetail
        """

        self.valueContributor = None
        """
        The value of the input parameter as a basic type.

        reference to Contributor
        """

        self.valueDosage = None
        """
        The value of the input parameter as a basic type.

        reference to Dosage
        """

        self.valueRelatedArtifact = None
        """
        The value of the input parameter as a basic type.

        reference to RelatedArtifact
        """

        self.valueUsageContext = None
        """
        The value of the input parameter as a basic type.

        reference to UsageContext
        """

        self.valueDataRequirement = None
        """
        The value of the input parameter as a basic type.

        reference to DataRequirement
        """

        self.valueParameterDefinition = None
        """
        The value of the input parameter as a basic type.

        reference to ParameterDefinition
        """

        self.valueTriggerDefinition = None
        """
        The value of the input parameter as a basic type.

        reference to TriggerDefinition
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueElement'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task_Input',
             'child_variable': 'valueReference'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueContributor'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDuration'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'type'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAge'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueCount'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueRange'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Input',
             'child_variable': 'valueSignature'},
        ]


class Task_Output(fhirbase):
    """
    A task to be performed.
    """

    __name__ = 'Task_Output'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The name of the Output parameter.

        reference to CodeableConcept
        """

        self.valueBoolean = None
        """
        The value of the Output parameter as a basic type.

        type: boolean
        """

        self.valueInteger = None
        """
        The value of the Output parameter as a basic type.

        type: int
        """

        self.valueDecimal = None
        """
        The value of the Output parameter as a basic type.

        type: int
        """

        self.valueBase64Binary = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueInstant = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueString = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueUri = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueDate = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueDateTime = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueTime = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueCode = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueOid = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueUuid = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueId = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueUnsignedInt = None
        """
        The value of the Output parameter as a basic type.

        type: int
        """

        self.valuePositiveInt = None
        """
        The value of the Output parameter as a basic type.

        type: int
        """

        self.valueMarkdown = None
        """
        The value of the Output parameter as a basic type.

        type: string
        """

        self.valueElement = None
        """
        The value of the Output parameter as a basic type.

        reference to Element: id
        """

        self.valueExtension = None
        """
        The value of the Output parameter as a basic type.

        reference to Extension
        """

        self.valueBackboneElement = None
        """
        The value of the Output parameter as a basic type.

        reference to BackboneElement
        """

        self.valueNarrative = None
        """
        The value of the Output parameter as a basic type.

        reference to Narrative
        """

        self.valueAnnotation = None
        """
        The value of the Output parameter as a basic type.

        reference to Annotation
        """

        self.valueAttachment = None
        """
        The value of the Output parameter as a basic type.

        reference to Attachment
        """

        self.valueIdentifier = None
        """
        The value of the Output parameter as a basic type.

        reference to Identifier
        """

        self.valueCodeableConcept = None
        """
        The value of the Output parameter as a basic type.

        reference to CodeableConcept
        """

        self.valueCoding = None
        """
        The value of the Output parameter as a basic type.

        reference to Coding
        """

        self.valueQuantity = None
        """
        The value of the Output parameter as a basic type.

        reference to Quantity
        """

        self.valueDuration = None
        """
        The value of the Output parameter as a basic type.

        reference to Duration
        """

        self.valueSimpleQuantity = None
        """
        The value of the Output parameter as a basic type.

        reference to Quantity
        """

        self.valueDistance = None
        """
        The value of the Output parameter as a basic type.

        reference to Distance
        """

        self.valueCount = None
        """
        The value of the Output parameter as a basic type.

        reference to Count
        """

        self.valueMoney = None
        """
        The value of the Output parameter as a basic type.

        reference to Money
        """

        self.valueAge = None
        """
        The value of the Output parameter as a basic type.

        reference to Age
        """

        self.valueRange = None
        """
        The value of the Output parameter as a basic type.

        reference to Range
        """

        self.valuePeriod = None
        """
        The value of the Output parameter as a basic type.

        reference to Period
        """

        self.valueRatio = None
        """
        The value of the Output parameter as a basic type.

        reference to Ratio
        """

        self.valueReference = None
        """
        The value of the Output parameter as a basic type.

        reference to Reference: identifier
        """

        self.valueSampledData = None
        """
        The value of the Output parameter as a basic type.

        reference to SampledData
        """

        self.valueSignature = None
        """
        The value of the Output parameter as a basic type.

        reference to Signature
        """

        self.valueHumanName = None
        """
        The value of the Output parameter as a basic type.

        reference to HumanName
        """

        self.valueAddress = None
        """
        The value of the Output parameter as a basic type.

        reference to Address
        """

        self.valueContactPoint = None
        """
        The value of the Output parameter as a basic type.

        reference to ContactPoint
        """

        self.valueTiming = None
        """
        The value of the Output parameter as a basic type.

        reference to Timing
        """

        self.valueMeta = None
        """
        The value of the Output parameter as a basic type.

        reference to Meta
        """

        self.valueElementDefinition = None
        """
        The value of the Output parameter as a basic type.

        reference to ElementDefinition
        """

        self.valueContactDetail = None
        """
        The value of the Output parameter as a basic type.

        reference to ContactDetail
        """

        self.valueContributor = None
        """
        The value of the Output parameter as a basic type.

        reference to Contributor
        """

        self.valueDosage = None
        """
        The value of the Output parameter as a basic type.

        reference to Dosage
        """

        self.valueRelatedArtifact = None
        """
        The value of the Output parameter as a basic type.

        reference to RelatedArtifact
        """

        self.valueUsageContext = None
        """
        The value of the Output parameter as a basic type.

        reference to UsageContext
        """

        self.valueDataRequirement = None
        """
        The value of the Output parameter as a basic type.

        reference to DataRequirement
        """

        self.valueParameterDefinition = None
        """
        The value of the Output parameter as a basic type.

        reference to ParameterDefinition
        """

        self.valueTriggerDefinition = None
        """
        The value of the Output parameter as a basic type.

        reference to TriggerDefinition
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueRange'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Task_Output',
             'child_variable': 'valueReference'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueElement'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDuration'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAge'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueSignature'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueContributor'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueCount'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'type'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Task_Output',
             'child_variable': 'valueSampledData'},
        ]
