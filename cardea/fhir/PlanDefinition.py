from .fhirbase import fhirbase


class PlanDefinition(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.

    Args:
        resourceType: This is a PlanDefinition resource
        url: An absolute URI that is used to identify this plan definition
            when it is referenced in a specification, model, design or an
            instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
            be an address at which this plan definition is (or will be) published.
            The URL SHOULD include the major version of the plan definition. For
            more information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this plan
            definition when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            plan definition when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the plan
            definition author and is not expected to be globally unique. For
            example, it might be a timestamp (e.g. yyyymmdd) if a managed version
            is not available. There is also no expectation that versions can be
            placed in a lexicographical sequence. To provide a version consistent
            with the Decision Support Service specification, use the format
            Major.Minor.Revision (e.g. 1.0.0). For more information on versioning
            knowledge assets, refer to the Decision Support Service specification.
            Note that a version is required for non-experimental active artifacts.
        name: A natural language name identifying the plan definition. This
            name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        title: A short, descriptive, user-friendly title for the plan
            definition.
        type: The type of asset the plan definition represents, e.g. an order
            set, protocol, or event-condition-action rule.
        status: The status of this plan definition. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this plan definition is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the plan definition was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the plan definition
            changes.
        publisher: The name of the individual or organization that published
            the plan definition.
        description: A free text natural language description of the plan
            definition from a consumer's perspective.
        purpose: Explaination of why this plan definition is needed and why it
            has been designed as it has.
        usage: A detailed description of how the asset is used from a clinical
            perspective.
        approvalDate: The date on which the resource content was approved by
            the publisher. Approval happens once when the content is officially
            approved for usage.
        lastReviewDate: The date on which the resource content was last
            reviewed. Review happens periodically after approval, but doesn't
            change the original approval date.
        effectivePeriod: The period during which the plan definition content
            was or is planned to be in active use.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate plan definition
            instances.
        jurisdiction: A legal or geographic region in which the plan
            definition is intended to be used.
        topic: Descriptive topics related to the content of the plan
            definition. Topics provide a high-level categorization of the
            definition that can be useful for filtering and searching.
        contributor: A contributor to the content of the asset, including
            authors, editors, reviewers, and endorsers.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        copyright: A copyright statement relating to the plan definition
            and/or its contents. Copyright statements are generally legal
            restrictions on the use and publishing of the plan definition.
        relatedArtifact: Related artifacts such as additional documentation,
            justification, or bibliographic references.
        library: A reference to a Library resource containing any formal logic
            used by the plan definition.
        goal: Goals that describe what the activities within the plan are
            intended to achieve. For example, weight loss, restoring an activity
            of daily living, obtaining herd immunity via immunization, meeting a
            process improvement objective, etc.
        action: An action to be taken as part of the plan.
    """

    __name__ = 'PlanDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'PlanDefinition'
        # type: str
        # possible values: PlanDefinition

        self.url = None
        # type: str

        self.version = None
        # type: str

        self.name = None
        # type: str

        self.title = None
        # type: str

        self.type = None
        # reference to CodeableConcept

        self.status = None
        # type: str
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # type: bool

        self.date = None
        # type: str

        self.publisher = None
        # type: str

        self.description = None
        # type: str

        self.purpose = None
        # type: str

        self.usage = None
        # type: str

        self.approvalDate = None
        # type: str

        self.lastReviewDate = None
        # type: str

        self.effectivePeriod = None
        # reference to Period

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.topic = None
        # type: list
        # reference to CodeableConcept

        self.contributor = None
        # type: list
        # reference to Contributor

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.copyright = None
        # type: str

        self.relatedArtifact = None
        # type: list
        # reference to RelatedArtifact

        self.library = None
        # type: list
        # reference to Reference: identifier

        self.goal = None
        # type: list
        # reference to PlanDefinition_Goal

        self.action = None
        # type: list
        # reference to PlanDefinition_Action

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
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'PlanDefinition_Action',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'action'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'type'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'useContext'},

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

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'PlanDefinition_Goal',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition',
             'child_variable': 'goal'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition',
             'child_variable': 'library'},
        ]


class PlanDefinition_Goal(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.

    Args:
        category: Indicates a category the goal falls within.
        description: Human-readable and/or coded description of a specific
            desired objective of care, such as "control blood pressure" or
            "negotiate an obstacle course" or "dance with child at wedding".
        priority: Identifies the expected level of importance associated with
            reaching/sustaining the defined goal.
        start: The event after which the goal should begin being pursued.
        addresses: Identifies problems, conditions, issues, or concerns the
            goal is intended to address.
        documentation: Didactic or other informational resources associated
            with the goal that provide further supporting information about the
            goal. Information resources can include inline text commentary and
            links to web resources.
        target: Indicates what should be done and within what timeframe.
    """

    __name__ = 'PlanDefinition_Goal'

    def __init__(self, dict_values=None):
        self.category = None
        # reference to CodeableConcept

        self.description = None
        # reference to CodeableConcept

        self.priority = None
        # reference to CodeableConcept

        self.start = None
        # reference to CodeableConcept

        self.addresses = None
        # type: list
        # reference to CodeableConcept

        self.documentation = None
        # type: list
        # reference to RelatedArtifact

        self.target = None
        # type: list
        # reference to PlanDefinition_Target

        self.object_id = None
        # unique identifier for object class

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
             'child_variable': 'description'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'documentation'},

            {'parent_entity': 'PlanDefinition_Target',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Goal',
             'child_variable': 'target'},

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

    Args:
        measure: The parameter whose value is to be tracked, e.g. body weigth,
            blood pressure, or hemoglobin A1c level.
        detailQuantity: The target value of the measure to be achieved to
            signify fulfillment of the goal, e.g. 150 pounds or 7.0%. Either the
            high or low or both values of the range can be specified. Whan a low
            value is missing, it indicates that the goal is achieved at any value
            at or below the high value. Similarly, if the high value is missing,
            it indicates that the goal is achieved at any value at or above the
            low value.
        detailRange: The target value of the measure to be achieved to signify
            fulfillment of the goal, e.g. 150 pounds or 7.0%. Either the high or
            low or both values of the range can be specified. Whan a low value is
            missing, it indicates that the goal is achieved at any value at or
            below the high value. Similarly, if the high value is missing, it
            indicates that the goal is achieved at any value at or above the low
            value.
        detailCodeableConcept: The target value of the measure to be achieved
            to signify fulfillment of the goal, e.g. 150 pounds or 7.0%. Either
            the high or low or both values of the range can be specified. Whan a
            low value is missing, it indicates that the goal is achieved at any
            value at or below the high value. Similarly, if the high value is
            missing, it indicates that the goal is achieved at any value at or
            above the low value.
        due: Indicates the timeframe after the start of the goal in which the
            goal should be met.
    """

    __name__ = 'PlanDefinition_Target'

    def __init__(self, dict_values=None):
        self.measure = None
        # reference to CodeableConcept

        self.detailQuantity = None
        # reference to Quantity

        self.detailRange = None
        # reference to Range

        self.detailCodeableConcept = None
        # reference to CodeableConcept

        self.due = None
        # reference to Duration

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailQuantity'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'measure'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'detailCodeableConcept'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Target',
             'child_variable': 'due'},
        ]


class PlanDefinition_Action(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.

    Args:
        label: A user-visible label for the action.
        title: The title of the action displayed to a user.
        description: A short description of the action used to provide a
            summary to display to the user.
        textEquivalent: A text equivalent of the action to be performed. This
            provides a human-interpretable description of the action when the
            definition is consumed by a system that may not be capable of
            interpreting it dynamically.
        code: A code that provides meaning for the action or action group. For
            example, a section may have a LOINC code for a the section of a
            documentation template.
        reason: A description of why this action is necessary or appropriate.
        documentation: Didactic or other informational resources associated
            with the action that can be provided to the CDS recipient. Information
            resources can include inline text commentary and links to web
            resources.
        goalId: Identifies goals that this action supports. The reference must
            be to a goal element defined within this plan definition.
        triggerDefinition: A description of when the action should be
            triggered.
        condition: An expression that describes applicability criteria, or
            start/stop conditions for the action.
        input: Defines input data requirements for the action.
        output: Defines the outputs of the action, if any.
        relatedAction: A relationship to another action such as "before" or
            "30-60 minutes after start of".
        timingDateTime: An optional value describing when the action should be
            performed.
        timingPeriod: An optional value describing when the action should be
            performed.
        timingDuration: An optional value describing when the action should be
            performed.
        timingRange: An optional value describing when the action should be
            performed.
        timingTiming: An optional value describing when the action should be
            performed.
        participant: Indicates who should participate in performing the action
            described.
        type: The type of action to perform (create, update, remove).
        groupingBehavior: Defines the grouping behavior for the action and its
            children.
        selectionBehavior: Defines the selection behavior for the action and
            its children.
        requiredBehavior: Defines the requiredness behavior for the action.
        precheckBehavior: Defines whether the action should usually be
            preselected.
        cardinalityBehavior: Defines whether the action can be selected
            multiple times.
        definition: A reference to an ActivityDefinition that describes the
            action to be taken in detail, or a PlanDefinition that describes a
            series of actions to be taken.
        transform: A reference to a StructureMap resource that defines a
            transform that can be executed to produce the intent resource using
            the ActivityDefinition instance as the input.
        dynamicValue: Customizations that should be applied to the statically
            defined resource. For example, if the dosage of a medication must be
            computed based on the patient's weight, a customization would be used
            to specify an expression that calculated the weight, and the path on
            the resource that would contain the result.
        action: Sub actions that are contained within the action. The behavior
            of this action determines the functionality of the sub-actions. For
            example, a selection behavior of at-most-one indicates that of the
            sub-actions, at most one may be chosen as part of realizing the action
            definition.
    """

    __name__ = 'PlanDefinition_Action'

    def __init__(self, dict_values=None):
        self.label = None
        # type: str

        self.title = None
        # type: str

        self.description = None
        # type: str

        self.textEquivalent = None
        # type: str

        self.code = None
        # type: list
        # reference to CodeableConcept

        self.reason = None
        # type: list
        # reference to CodeableConcept

        self.documentation = None
        # type: list
        # reference to RelatedArtifact

        self.goalId = None
        # type: list

        self.triggerDefinition = None
        # type: list
        # reference to TriggerDefinition

        self.condition = None
        # type: list
        # reference to PlanDefinition_Condition

        self.input = None
        # type: list
        # reference to DataRequirement

        self.output = None
        # type: list
        # reference to DataRequirement

        self.relatedAction = None
        # type: list
        # reference to PlanDefinition_RelatedAction

        self.timingDateTime = None
        # type: str

        self.timingPeriod = None
        # reference to Period

        self.timingDuration = None
        # reference to Duration

        self.timingRange = None
        # reference to Range

        self.timingTiming = None
        # reference to Timing

        self.participant = None
        # type: list
        # reference to PlanDefinition_Participant

        self.type = None
        # reference to Coding

        self.groupingBehavior = None
        # type: str
        # possible values: visual-group, logical-group, sentence-group

        self.selectionBehavior = None
        # type: str
        # possible values: any, all, all-or-none, exactly-one,
        # at-most-one, one-or-more

        self.requiredBehavior = None
        # type: str
        # possible values: must, could, must-unless-documented

        self.precheckBehavior = None
        # type: str
        # possible values: yes, no

        self.cardinalityBehavior = None
        # type: str
        # possible values: single, multiple

        self.definition = None
        # reference to Reference: identifier

        self.transform = None
        # reference to Reference: identifier

        self.dynamicValue = None
        # type: list
        # reference to PlanDefinition_DynamicValue

        self.action = None
        # type: list
        # reference to PlanDefinition_Action

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'PlanDefinition_RelatedAction',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'relatedAction'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingRange'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'documentation'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'PlanDefinition_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'participant'},

            {'parent_entity': 'PlanDefinition_Action',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'action'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'definition'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'input'},

            {'parent_entity': 'PlanDefinition_DynamicValue',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'dynamicValue'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'timingDuration'},

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

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'transform'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_Action',
             'child_variable': 'reason'},

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

    Args:
        kind: The kind of condition.
        description: A brief, natural language description of the condition
            that effectively communicates the intended semantics.
        language: The media type of the language for the expression.
        expression: An expression that returns true or false, indicating
            whether or not the condition is satisfied.
    """

    __name__ = 'PlanDefinition_Condition'

    def __init__(self, dict_values=None):
        self.kind = None
        # type: str
        # possible values: applicability, start, stop

        self.description = None
        # type: str

        self.language = None
        # type: str

        self.expression = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        actionId: The element id of the related action.
        relationship: The relationship of this action to the related action.
        offsetDuration: A duration or range of durations to apply to the
            relationship. For example, 30-60 minutes before.
        offsetRange: A duration or range of durations to apply to the
            relationship. For example, 30-60 minutes before.
    """

    __name__ = 'PlanDefinition_RelatedAction'

    def __init__(self, dict_values=None):
        self.actionId = None
        # type: str

        self.relationship = None
        # type: str
        # possible values: before-start, before, before-end,
        # concurrent-with-start, concurrent, concurrent-with-end, after-start,
        # after, after-end

        self.offsetDuration = None
        # reference to Duration

        self.offsetRange = None
        # reference to Range

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_RelatedAction',
             'child_variable': 'offsetRange'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'PlanDefinition_RelatedAction',
             'child_variable': 'offsetDuration'},
        ]


class PlanDefinition_Participant(fhirbase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical
    artifacts such as clinical decision support rules, order sets and
    protocols.

    Args:
        type: The type of participant in the action.
        role: The role the participant should play in performing the described
            action.
    """

    __name__ = 'PlanDefinition_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: patient, practitioner, related-person

        self.role = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        description: A brief, natural language description of the intended
            semantics of the dynamic value.
        path: The path to the element to be customized. This is the path on
            the resource that will hold the result of the calculation defined by
            the expression.
        language: The media type of the language for the expression.
        expression: An expression specifying the value of the customized
            element.
    """

    __name__ = 'PlanDefinition_DynamicValue'

    def __init__(self, dict_values=None):
        self.description = None
        # type: str

        self.path = None
        # type: str

        self.language = None
        # type: str

        self.expression = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
