from .fhirbase import fhirbase


class PlanDefinition(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # this is a plandefinition resource
        self.resourceType = 'PlanDefinition'
        # type = string
        # possible values: PlanDefinition

        # an absolute uri that is used to identify this plan definition when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this plan definition is (or will be) published. the url should include
        # the major version of the plan definition. for more information see
        # [technical and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the plan
        # definition when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the plan definition
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence. to provide a version consistent with the
        # decision support service specification, use the format
        # major.minor.revision (e.g. 1.0.0). for more information on versioning
        # knowledge assets, refer to the decision support service specification.
        # note that a version is required for non-experimental active artifacts.
        self.version = None
        # type = string

        # a natural language name identifying the plan definition. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the plan definition.
        self.title = None
        # type = string

        # the type of asset the plan definition represents, e.g. an order set,
        # protocol, or event-condition-action rule.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the status of this plan definition. enables tracking the life-cycle of
        # the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this plan definition is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the plan definition was published.
        # the date must change if and when the business version changes and it
        # must change if the status code changes. in addition, it should change
        # when the substantive content of the plan definition changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the plan
        # definition.
        self.publisher = None
        # type = string

        # a free text natural language description of the plan definition from a
        # consumer's perspective.
        self.description = None
        # type = string

        # explaination of why this plan definition is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # a detailed description of how the asset is used from a clinical
        # perspective.
        self.usage = None
        # type = string

        # the date on which the resource content was approved by the publisher.
        # approval happens once when the content is officially approved for usage.
        self.approvalDate = None
        # type = string

        # the date on which the resource content was last reviewed. review happens
        # periodically after approval, but doesn't change the original approval
        # date.
        self.lastReviewDate = None
        # type = string

        # the period during which the plan definition content was or is planned to
        # be in active use.
        self.effectivePeriod = None
        # reference to Period: Period

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate plan definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the plan definition is intended to
        # be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # descriptive topics related to the content of the plan definition. topics
        # provide a high-level categorization of the definition that can be useful
        # for filtering and searching.
        self.topic = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a contributor to the content of the asset, including authors, editors,
        # reviewers, and endorsers.
        self.contributor = None
        # type = array
        # reference to Contributor: Contributor

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a copyright statement relating to the plan definition and/or its
        # contents. copyright statements are generally legal restrictions on the
        # use and publishing of the plan definition.
        self.copyright = None
        # type = string

        # related artifacts such as additional documentation, justification, or
        # bibliographic references.
        self.relatedArtifact = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # a reference to a library resource containing any formal logic used by
        # the plan definition.
        self.library = None
        # type = array
        # reference to Reference: identifier

        # goals that describe what the activities within the plan are intended to
        # achieve. for example, weight loss, restoring an activity of daily
        # living, obtaining herd immunity via immunization, meeting a process
        # improvement objective, etc.
        self.goal = None
        # type = array
        # reference to PlanDefinition_Goal: PlanDefinition_Goal

        # an action to be taken as part of the plan.
        self.action = None
        # type = array
        # reference to PlanDefinition_Action: PlanDefinition_Action

        # a formal identifier that is used to identify this plan definition when
        # it is represented in other formats, or referenced in a specification,
        # model, design or an instance.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'topic'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition',
             'child_variable': 'library'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'PlanDefinition_Action',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'action'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'type'},

            {'parent_entity': 'PlanDefinition_Goal',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'goal'},
        ]


class PlanDefinition_Goal(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # indicates a category the goal falls within.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # human-readable and/or coded description of a specific desired objective
        # of care, such as "control blood pressure" or "negotiate an obstacle
        # course" or "dance with child at wedding".
        self.description = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the expected level of importance associated with
        # reaching/sustaining the defined goal.
        self.priority = None
        # reference to CodeableConcept: CodeableConcept

        # the event after which the goal should begin being pursued.
        self.start = None
        # reference to CodeableConcept: CodeableConcept

        # identifies problems, conditions, issues, or concerns the goal is
        # intended to address.
        self.addresses = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # didactic or other informational resources associated with the goal that
        # provide further supporting information about the goal. information
        # resources can include inline text commentary and links to web resources.
        self.documentation = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # indicates what should be done and within what timeframe.
        self.target = None
        # type = array
        # reference to PlanDefinition_Target: PlanDefinition_Target

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'priority'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'start'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'addresses'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'documentation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'description'},

            {'parent_entity': 'PlanDefinition_Target',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'target'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'category'},
        ]


class PlanDefinition_Target(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # the parameter whose value is to be tracked, e.g. body weigth, blood
        # pressure, or hemoglobin a1c level.
        self.measure = None
        # reference to CodeableConcept: CodeableConcept

        # the target value of the measure to be achieved to signify fulfillment of
        # the goal, e.g. 150 pounds or 7.0%. either the high or low or both values
        # of the range can be specified. whan a low value is missing, it indicates
        # that the goal is achieved at any value at or below the high value.
        # similarly, if the high value is missing, it indicates that the goal is
        # achieved at any value at or above the low value.
        self.detailQuantity = None
        # reference to Quantity: Quantity

        # the target value of the measure to be achieved to signify fulfillment of
        # the goal, e.g. 150 pounds or 7.0%. either the high or low or both values
        # of the range can be specified. whan a low value is missing, it indicates
        # that the goal is achieved at any value at or below the high value.
        # similarly, if the high value is missing, it indicates that the goal is
        # achieved at any value at or above the low value.
        self.detailRange = None
        # reference to Range: Range

        # the target value of the measure to be achieved to signify fulfillment of
        # the goal, e.g. 150 pounds or 7.0%. either the high or low or both values
        # of the range can be specified. whan a low value is missing, it indicates
        # that the goal is achieved at any value at or below the high value.
        # similarly, if the high value is missing, it indicates that the goal is
        # achieved at any value at or above the low value.
        self.detailCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the timeframe after the start of the goal in which the goal
        # should be met.
        self.due = None
        # reference to Duration: Duration

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailCodeableConcept'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'measure'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'due'},
        ]


class PlanDefinition_Action(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # a user-visible label for the action.
        self.label = None
        # type = string

        # the title of the action displayed to a user.
        self.title = None
        # type = string

        # a short description of the action used to provide a summary to display
        # to the user.
        self.description = None
        # type = string

        # a text equivalent of the action to be performed. this provides a human-
        # interpretable description of the action when the definition is consumed
        # by a system that may not be capable of interpreting it dynamically.
        self.textEquivalent = None
        # type = string

        # a code that provides meaning for the action or action group. for
        # example, a section may have a loinc code for a the section of a
        # documentation template.
        self.code = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a description of why this action is necessary or appropriate.
        self.reason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # didactic or other informational resources associated with the action
        # that can be provided to the cds recipient. information resources can
        # include inline text commentary and links to web resources.
        self.documentation = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # identifies goals that this action supports. the reference must be to a
        # goal element defined within this plan definition.
        self.goalId = None
        # type = array

        # a description of when the action should be triggered.
        self.triggerDefinition = None
        # type = array
        # reference to TriggerDefinition: TriggerDefinition

        # an expression that describes applicability criteria, or start/stop
        # conditions for the action.
        self.condition = None
        # type = array
        # reference to PlanDefinition_Condition: PlanDefinition_Condition

        # defines input data requirements for the action.
        self.input = None
        # type = array
        # reference to DataRequirement: DataRequirement

        # defines the outputs of the action, if any.
        self.output = None
        # type = array
        # reference to DataRequirement: DataRequirement

        # a relationship to another action such as "before" or "30-60 minutes
        # after start of".
        self.relatedAction = None
        # type = array
        # reference to PlanDefinition_RelatedAction: PlanDefinition_RelatedAction

        # an optional value describing when the action should be performed.
        self.timingDateTime = None
        # type = string

        # an optional value describing when the action should be performed.
        self.timingPeriod = None
        # reference to Period: Period

        # an optional value describing when the action should be performed.
        self.timingDuration = None
        # reference to Duration: Duration

        # an optional value describing when the action should be performed.
        self.timingRange = None
        # reference to Range: Range

        # an optional value describing when the action should be performed.
        self.timingTiming = None
        # reference to Timing: Timing

        # indicates who should participate in performing the action described.
        self.participant = None
        # type = array
        # reference to PlanDefinition_Participant: PlanDefinition_Participant

        # the type of action to perform (create, update, remove).
        self.type = None
        # reference to Coding: Coding

        # defines the grouping behavior for the action and its children.
        self.groupingBehavior = None
        # type = string
        # possible values: visual-group, logical-group, sentence-group

        # defines the selection behavior for the action and its children.
        self.selectionBehavior = None
        # type = string
        # possible values: any, all, all-or-none, exactly-one, at-most-
        # one, one-or-more

        # defines the requiredness behavior for the action.
        self.requiredBehavior = None
        # type = string
        # possible values: must, could, must-unless-documented

        # defines whether the action should usually be preselected.
        self.precheckBehavior = None
        # type = string
        # possible values: yes, no

        # defines whether the action can be selected multiple times.
        self.cardinalityBehavior = None
        # type = string
        # possible values: single, multiple

        # a reference to an activitydefinition that describes the action to be
        # taken in detail, or a plandefinition that describes a series of actions
        # to be taken.
        self.definition = None
        # reference to Reference: identifier

        # a reference to a structuremap resource that defines a transform that can
        # be executed to produce the intent resource using the activitydefinition
        # instance as the input.
        self.transform = None
        # reference to Reference: identifier

        # customizations that should be applied to the statically defined
        # resource. for example, if the dosage of a medication must be computed
        # based on the patient's weight, a customization would be used to specify
        # an expression that calculated the weight, and the path on the resource
        # that would contain the result.
        self.dynamicValue = None
        # type = array
        # reference to PlanDefinition_DynamicValue: PlanDefinition_DynamicValue

        # sub actions that are contained within the action. the behavior of this
        # action determines the functionality of the sub-actions. for example, a
        # selection behavior of at-most-one indicates that of the sub-actions, at
        # most one may be chosen as part of realizing the action definition.
        self.action = None
        # type = array
        # reference to PlanDefinition_Action: PlanDefinition_Action

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.groupingBehavior is not None:
            for value in self.groupingBehavior:
                if value is not None and value.lower() not in [
                        'visual-group', 'logical-group', 'sentence-group']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'visual-group, logical-group, sentence-group'))

        if self.selectionBehavior is not None:
            for value in self.selectionBehavior:
                if value is not None and value.lower() not in [
                    'any', 'all', 'all-or-none', 'exactly-one', 'at-most-one',
                        'one-or-more']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'any, all, all-or-none, exactly-one, at-most-one, one-or-more'))

        if self.requiredBehavior is not None:
            for value in self.requiredBehavior:
                if value is not None and value.lower() not in [
                        'must', 'could', 'must-unless-documented']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'must, could, must-unless-documented'))

        if self.precheckBehavior is not None:
            for value in self.precheckBehavior:
                if value is not None and value.lower() not in [
                        'yes', 'no']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'yes, no'))

        if self.cardinalityBehavior is not None:
            for value in self.cardinalityBehavior:
                if value is not None and value.lower() not in [
                        'single', 'multiple']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'single, multiple'))

        if self.groupingBehavior is not None:
            for value in self.groupingBehavior:
                if value is not None and value.lower() not in [
                        'visual-group', 'logical-group', 'sentence-group']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'visual-group, logical-group, sentence-group'))

        if self.selectionBehavior is not None:
            for value in self.selectionBehavior:
                if value is not None and value.lower() not in [
                    'any', 'all', 'all-or-none', 'exactly-one', 'at-most-one',
                        'one-or-more']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'any, all, all-or-none, exactly-one, at-most-one, one-or-more'))

        if self.requiredBehavior is not None:
            for value in self.requiredBehavior:
                if value is not None and value.lower() not in [
                        'must', 'could', 'must-unless-documented']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'must, could, must-unless-documented'))

        if self.precheckBehavior is not None:
            for value in self.precheckBehavior:
                if value is not None and value.lower() not in [
                        'yes', 'no']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'yes, no'))

        if self.cardinalityBehavior is not None:
            for value in self.cardinalityBehavior:
                if value is not None and value.lower() not in [
                        'single', 'multiple']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'single, multiple'))

    def get_relationships(self):

        return [
            {'parent_entity': 'PlanDefinition_Action',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'action'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'type'},

            {'parent_entity': 'PlanDefinition_RelatedAction',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'relatedAction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'transform'},

            {'parent_entity': 'PlanDefinition_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'participant'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'input'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'triggerDefinition'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'output'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'reason'},

            {'parent_entity': 'PlanDefinition_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'condition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'definition'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingRange'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'code'},

            {'parent_entity': 'PlanDefinition_DynamicValue',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'dynamicValue'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingDuration'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'documentation'},
        ]


class PlanDefinition_Condition(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # the kind of condition.
        self.kind = None
        # type = string
        # possible values: applicability, start, stop

        # a brief, natural language description of the condition that effectively
        # communicates the intended semantics.
        self.description = None
        # type = string

        # the media type of the language for the expression.
        self.language = None
        # type = string

        # an expression that returns true or false, indicating whether or not the
        # condition is satisfied.
        self.expression = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.kind is not None:
            for value in self.kind:
                if value is not None and value.lower() not in [
                        'applicability', 'start', 'stop']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'applicability, start, stop'))


class PlanDefinition_RelatedAction(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # the element id of the related action.
        self.actionId = None
        # type = string

        # the relationship of this action to the related action.
        self.relationship = None
        # type = string
        # possible values: before-start, before, before-end, concurrent-
        # with-start, concurrent, concurrent-with-end, after-start, after, after-
        # end

        # a duration or range of durations to apply to the relationship. for
        # example, 30-60 minutes before.
        self.offsetDuration = None
        # reference to Duration: Duration

        # a duration or range of durations to apply to the relationship. for
        # example, 30-60 minutes before.
        self.offsetRange = None
        # reference to Range: Range

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.relationship is not None:
            for value in self.relationship:
                if value is not None and value.lower() not in [
                    'before-start', 'before', 'before-end', 'concurrent-with-start',
                    'concurrent', 'concurrent-with-end', 'after-start', 'after',
                        'after-end']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'before-start, before, before-end, concurrent-with-start,'
                        'concurrent,'
                        'concurrent-with-end, after-start, after, after-end'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_RelatedAction',
             'child_variable': 'offsetDuration'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_RelatedAction',
             'child_variable': 'offsetRange'},
        ]


class PlanDefinition_Participant(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # the type of participant in the action.
        self.type = None
        # type = string
        # possible values: patient, practitioner, related-person

        # the role the participant should play in performing the described action.
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'patient', 'practitioner', 'related-person']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'patient, practitioner, related-person'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Participant',
             'child_variable': 'role'},
        ]


class PlanDefinition_DynamicValue(fhirbase):
    """This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """

    def __init__(self, dict_values=None):
        # a brief, natural language description of the intended semantics of the
        # dynamic value.
        self.description = None
        # type = string

        # the path to the element to be customized. this is the path on the
        # resource that will hold the result of the calculation defined by the
        # expression.
        self.path = None
        # type = string

        # the media type of the language for the expression.
        self.language = None
        # type = string

        # an expression specifying the value of the customized element.
        self.expression = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
