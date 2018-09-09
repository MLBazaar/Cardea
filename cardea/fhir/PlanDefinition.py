from .fhirbase import fhirbase


class PlanDefinition(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'PlanDefinition'
        """
        This is a PlanDefinition resource

        type: string
        possible values: PlanDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this plan definition when it
        is referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this plan definition is (or will be) published. The URL SHOULD
        include the major version of the plan definition. For more information
        see [Technical and Business Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the plan
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the plan definition
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence. To provide a version consistent with the
        Decision Support Service specification, use the format
        Major.Minor.Revision (e.g. 1.0.0). For more information on versioning
        knowledge assets, refer to the Decision Support Service specification.
        Note that a version is required for non-experimental active artifacts.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the plan definition. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the plan definition.

        type: string
        """

        self.type = None
        """
        The type of asset the plan definition represents, e.g. an order set,
        protocol, or event-condition-action rule.

        reference to CodeableConcept
        """

        self.status = None
        """
        The status of this plan definition. Enables tracking the life-cycle of
        the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this plan definition is authored for
        testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the plan definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the plan definition
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the plan
        definition.

        type: string
        """

        self.description = None
        """
        A free text natural language description of the plan definition from a
        consumer's perspective.

        type: string
        """

        self.purpose = None
        """
        Explaination of why this plan definition is needed and why it has been
        designed as it has.

        type: string
        """

        self.usage = None
        """
        A detailed description of how the asset is used from a clinical
        perspective.

        type: string
        """

        self.approvalDate = None
        """
        The date on which the resource content was approved by the publisher.
        Approval happens once when the content is officially approved for
        usage.

        type: string
        """

        self.lastReviewDate = None
        """
        The date on which the resource content was last reviewed. Review
        happens periodically after approval, but doesn't change the original
        approval date.

        type: string
        """

        self.effectivePeriod = None
        """
        The period during which the plan definition content was or is planned
        to be in active use.

        reference to Period
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate plan definition instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the plan definition is intended
        to be used.

        type: array
        reference to CodeableConcept
        """

        self.topic = None
        """
        Descriptive topics related to the content of the plan definition.
        Topics provide a high-level categorization of the definition that can
        be useful for filtering and searching.

        type: array
        reference to CodeableConcept
        """

        self.contributor = None
        """
        A contributor to the content of the asset, including authors, editors,
        reviewers, and endorsers.

        type: array
        reference to Contributor
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        publisher.

        type: array
        reference to ContactDetail
        """

        self.copyright = None
        """
        A copyright statement relating to the plan definition and/or its
        contents. Copyright statements are generally legal restrictions on the
        use and publishing of the plan definition.

        type: string
        """

        self.relatedArtifact = None
        """
        Related artifacts such as additional documentation, justification, or
        bibliographic references.

        type: array
        reference to RelatedArtifact
        """

        self.library = None
        """
        A reference to a Library resource containing any formal logic used by
        the plan definition.

        type: array
        reference to Reference: identifier
        """

        self.goal = None
        """
        Goals that describe what the activities within the plan are intended
        to achieve. For example, weight loss, restoring an activity of daily
        living, obtaining herd immunity via immunization, meeting a process
        improvement objective, etc.

        type: array
        reference to PlanDefinition_Goal
        """

        self.action = None
        """
        An action to be taken as part of the plan.

        type: array
        reference to PlanDefinition_Action
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this plan definition when
        it is represented in other formats, or referenced in a specification,
        model, design or an instance.

        type: array
        reference to Identifier
        """

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'PlanDefinition_Action',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'action'},

            {'parent_entity': 'PlanDefinition_Goal',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'goal'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'type'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'topic'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition',
             'child_variable': 'library'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'contact'},
        ]


class PlanDefinition_Goal(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition_Goal'

    def __init__(self, dict_values=None):
        self.category = None
        """
        Indicates a category the goal falls within.

        reference to CodeableConcept
        """

        self.description = None
        """
        Human-readable and/or coded description of a specific desired
        objective of care, such as "control blood pressure" or "negotiate an
        obstacle course" or "dance with child at wedding".

        reference to CodeableConcept
        """

        self.priority = None
        """
        Identifies the expected level of importance associated with
        reaching/sustaining the defined goal.

        reference to CodeableConcept
        """

        self.start = None
        """
        The event after which the goal should begin being pursued.

        reference to CodeableConcept
        """

        self.addresses = None
        """
        Identifies problems, conditions, issues, or concerns the goal is
        intended to address.

        type: array
        reference to CodeableConcept
        """

        self.documentation = None
        """
        Didactic or other informational resources associated with the goal
        that provide further supporting information about the goal.
        Information resources can include inline text commentary and links to
        web resources.

        type: array
        reference to RelatedArtifact
        """

        self.target = None
        """
        Indicates what should be done and within what timeframe.

        type: array
        reference to PlanDefinition_Target
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'start'},

            {'parent_entity': 'PlanDefinition_Target',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'target'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'priority'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'description'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'documentation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'addresses'},
        ]


class PlanDefinition_Target(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition_Target'

    def __init__(self, dict_values=None):
        self.measure = None
        """
        The parameter whose value is to be tracked, e.g. body weigth, blood
        pressure, or hemoglobin A1c level.

        reference to CodeableConcept
        """

        self.detailQuantity = None
        """
        The target value of the measure to be achieved to signify fulfillment
        of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both
        values of the range can be specified. Whan a low value is missing, it
        indicates that the goal is achieved at any value at or below the high
        value. Similarly, if the high value is missing, it indicates that the
        goal is achieved at any value at or above the low value.

        reference to Quantity
        """

        self.detailRange = None
        """
        The target value of the measure to be achieved to signify fulfillment
        of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both
        values of the range can be specified. Whan a low value is missing, it
        indicates that the goal is achieved at any value at or below the high
        value. Similarly, if the high value is missing, it indicates that the
        goal is achieved at any value at or above the low value.

        reference to Range
        """

        self.detailCodeableConcept = None
        """
        The target value of the measure to be achieved to signify fulfillment
        of the goal, e.g. 150 pounds or 7.0%. Either the high or low or both
        values of the range can be specified. Whan a low value is missing, it
        indicates that the goal is achieved at any value at or below the high
        value. Similarly, if the high value is missing, it indicates that the
        goal is achieved at any value at or above the low value.

        reference to CodeableConcept
        """

        self.due = None
        """
        Indicates the timeframe after the start of the goal in which the goal
        should be met.

        reference to Duration
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'measure'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailQuantity'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailRange'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'due'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailCodeableConcept'},
        ]


class PlanDefinition_Action(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition_Action'

    def __init__(self, dict_values=None):
        self.label = None
        """
        A user-visible label for the action.

        type: string
        """

        self.title = None
        """
        The title of the action displayed to a user.

        type: string
        """

        self.description = None
        """
        A short description of the action used to provide a summary to display
        to the user.

        type: string
        """

        self.textEquivalent = None
        """
        A text equivalent of the action to be performed. This provides a
        human-interpretable description of the action when the definition is
        consumed by a system that may not be capable of interpreting it
        dynamically.

        type: string
        """

        self.code = None
        """
        A code that provides meaning for the action or action group. For
        example, a section may have a LOINC code for a the section of a
        documentation template.

        type: array
        reference to CodeableConcept
        """

        self.reason = None
        """
        A description of why this action is necessary or appropriate.

        type: array
        reference to CodeableConcept
        """

        self.documentation = None
        """
        Didactic or other informational resources associated with the action
        that can be provided to the CDS recipient. Information resources can
        include inline text commentary and links to web resources.

        type: array
        reference to RelatedArtifact
        """

        self.goalId = None
        """
        Identifies goals that this action supports. The reference must be to a
        goal element defined within this plan definition.

        type: array
        """

        self.triggerDefinition = None
        """
        A description of when the action should be triggered.

        type: array
        reference to TriggerDefinition
        """

        self.condition = None
        """
        An expression that describes applicability criteria, or start/stop
        conditions for the action.

        type: array
        reference to PlanDefinition_Condition
        """

        self.input = None
        """
        Defines input data requirements for the action.

        type: array
        reference to DataRequirement
        """

        self.output = None
        """
        Defines the outputs of the action, if any.

        type: array
        reference to DataRequirement
        """

        self.relatedAction = None
        """
        A relationship to another action such as "before" or "30-60 minutes
        after start of".

        type: array
        reference to PlanDefinition_RelatedAction
        """

        self.timingDateTime = None
        """
        An optional value describing when the action should be performed.

        type: string
        """

        self.timingPeriod = None
        """
        An optional value describing when the action should be performed.

        reference to Period
        """

        self.timingDuration = None
        """
        An optional value describing when the action should be performed.

        reference to Duration
        """

        self.timingRange = None
        """
        An optional value describing when the action should be performed.

        reference to Range
        """

        self.timingTiming = None
        """
        An optional value describing when the action should be performed.

        reference to Timing
        """

        self.participant = None
        """
        Indicates who should participate in performing the action described.

        type: array
        reference to PlanDefinition_Participant
        """

        self.type = None
        """
        The type of action to perform (create, update, remove).

        reference to Coding
        """

        self.groupingBehavior = None
        """
        Defines the grouping behavior for the action and its children.

        type: string
        possible values: visual-group, logical-group, sentence-group
        """

        self.selectionBehavior = None
        """
        Defines the selection behavior for the action and its children.

        type: string
        possible values: any, all, all-or-none, exactly-one,
        at-most-one, one-or-more
        """

        self.requiredBehavior = None
        """
        Defines the requiredness behavior for the action.

        type: string
        possible values: must, could, must-unless-documented
        """

        self.precheckBehavior = None
        """
        Defines whether the action should usually be preselected.

        type: string
        possible values: yes, no
        """

        self.cardinalityBehavior = None
        """
        Defines whether the action can be selected multiple times.

        type: string
        possible values: single, multiple
        """

        self.definition = None
        """
        A reference to an ActivityDefinition that describes the action to be
        taken in detail, or a PlanDefinition that describes a series of
        actions to be taken.

        reference to Reference: identifier
        """

        self.transform = None
        """
        A reference to a StructureMap resource that defines a transform that
        can be executed to produce the intent resource using the
        ActivityDefinition instance as the input.

        reference to Reference: identifier
        """

        self.dynamicValue = None
        """
        Customizations that should be applied to the statically defined
        resource. For example, if the dosage of a medication must be computed
        based on the patient's weight, a customization would be used to
        specify an expression that calculated the weight, and the path on the
        resource that would contain the result.

        type: array
        reference to PlanDefinition_DynamicValue
        """

        self.action = None
        """
        Sub actions that are contained within the action. The behavior of this
        action determines the functionality of the sub-actions. For example, a
        selection behavior of at-most-one indicates that of the sub-actions,
        at most one may be chosen as part of realizing the action definition.

        type: array
        reference to PlanDefinition_Action
        """

        self.object_id = None
        # unique identifier for object class

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
            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingDuration'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'transform'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'definition'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'triggerDefinition'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingRange'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'type'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'input'},

            {'parent_entity': 'PlanDefinition_RelatedAction',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'relatedAction'},

            {'parent_entity': 'PlanDefinition_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'participant'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'documentation'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'output'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'reason'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'PlanDefinition_Action',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'action'},

            {'parent_entity': 'PlanDefinition_DynamicValue',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'dynamicValue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'code'},

            {'parent_entity': 'PlanDefinition_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'condition'},
        ]


class PlanDefinition_Condition(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition_Condition'

    def __init__(self, dict_values=None):
        self.kind = None
        """
        The kind of condition.

        type: string
        possible values: applicability, start, stop
        """

        self.description = None
        """
        A brief, natural language description of the condition that
        effectively communicates the intended semantics.

        type: string
        """

        self.language = None
        """
        The media type of the language for the expression.

        type: string
        """

        self.expression = None
        """
        An expression that returns true or false, indicating whether or not
        the condition is satisfied.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition_RelatedAction'

    def __init__(self, dict_values=None):
        self.actionId = None
        """
        The element id of the related action.

        type: string
        """

        self.relationship = None
        """
        The relationship of this action to the related action.

        type: string
        possible values: before-start, before, before-end,
        concurrent-with-start, concurrent, concurrent-with-end, after-start,
        after, after-end
        """

        self.offsetDuration = None
        """
        A duration or range of durations to apply to the relationship. For
        example, 30-60 minutes before.

        reference to Duration
        """

        self.offsetRange = None
        """
        A duration or range of durations to apply to the relationship. For
        example, 30-60 minutes before.

        reference to Range
        """

        self.object_id = None
        # unique identifier for object class

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
                        value, 'before-start, before, before-end, concurrent-with-start, '
                        'concurrent, concurrent-with-end, after-start, after, after-end'))

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
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The type of participant in the action.

        type: string
        possible values: patient, practitioner, related-person
        """

        self.role = None
        """
        The role the participant should play in performing the described
        action.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.
    """

    __name__ = 'PlanDefinition_DynamicValue'

    def __init__(self, dict_values=None):
        self.description = None
        """
        A brief, natural language description of the intended semantics of the
        dynamic value.

        type: string
        """

        self.path = None
        """
        The path to the element to be customized. This is the path on the
        resource that will hold the result of the calculation defined by the
        expression.

        type: string
        """

        self.language = None
        """
        The media type of the language for the expression.

        type: string
        """

        self.expression = None
        """
        An expression specifying the value of the customized element.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
