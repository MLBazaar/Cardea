from .fhirbase import fhirbase


class RequestGroup(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
    """

    __name__ = 'RequestGroup'

    def __init__(self, dict_values=None):
        self.resourceType = 'RequestGroup'
        """
        This is a RequestGroup resource

        type: string
        possible values: RequestGroup
        """

        self.definition = None
        """
        A protocol, guideline, orderset or other definition that is adhered to
        in whole or in part by this request.

        type: array
        reference to Reference: identifier
        """

        self.basedOn = None
        """
        A plan, proposal or order that is fulfilled in whole or in part by
        this request.

        type: array
        reference to Reference: identifier
        """

        self.replaces = None
        """
        Completed or terminated request(s) whose function is taken by this new
        request.

        type: array
        reference to Reference: identifier
        """

        self.groupIdentifier = None
        """
        A shared identifier common to all requests that were authorized more
        or less simultaneously by a single author, representing the identifier
        of the requisition, prescription or similar form.

        reference to Identifier
        """

        self.status = None
        """
        The current state of the request. For request groups, the status
        reflects the status of all the requests in the group.

        type: string
        """

        self.intent = None
        """
        Indicates the level of authority/intentionality associated with the
        request and where the request fits into the workflow chain.

        type: string
        """

        self.priority = None
        """
        Indicates how quickly the request should be addressed with respect to
        other requests.

        type: string
        """

        self.subject = None
        """
        The subject for which the request group was created.

        reference to Reference: identifier
        """

        self.context = None
        """
        Describes the context of the request group, if any.

        reference to Reference: identifier
        """

        self.authoredOn = None
        """
        Indicates when the request group was created.

        type: string
        """

        self.author = None
        """
        Provides a reference to the author of the request group.

        reference to Reference: identifier
        """

        self.reasonCodeableConcept = None
        """
        Indicates the reason the request group was created. This is typically
        provided as a parameter to the evaluation and echoed by the service,
        although for some use cases, such as subscription- or event-based
        scenarios, it may provide an indication of the cause for the response.

        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Indicates the reason the request group was created. This is typically
        provided as a parameter to the evaluation and echoed by the service,
        although for some use cases, such as subscription- or event-based
        scenarios, it may provide an indication of the cause for the response.

        reference to Reference: identifier
        """

        self.note = None
        """
        Provides a mechanism to communicate additional information about the
        response.

        type: array
        reference to Annotation
        """

        self.action = None
        """
        The actions, if any, produced by the evaluation of the artifact.

        type: array
        reference to RequestGroup_Action
        """

        self.identifier = None
        """
        Allows a service to provide a unique, business identifier for the
        request.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'context'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'identifier'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'definition'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'author'},

            {'parent_entity': 'RequestGroup_Action',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'action'},
        ]


class RequestGroup_Action(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
    """

    __name__ = 'RequestGroup_Action'

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

        self.documentation = None
        """
        Didactic or other informational resources associated with the action
        that can be provided to the CDS recipient. Information resources can
        include inline text commentary and links to web resources.

        type: array
        reference to RelatedArtifact
        """

        self.condition = None
        """
        An expression that describes applicability criteria, or start/stop
        conditions for the action.

        type: array
        reference to RequestGroup_Condition
        """

        self.relatedAction = None
        """
        A relationship to another action such as "before" or "30-60 minutes
        after start of".

        type: array
        reference to RequestGroup_RelatedAction
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
        The participant that should perform or be responsible for this action.

        type: array
        reference to Reference: identifier
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
        """

        self.selectionBehavior = None
        """
        Defines the selection behavior for the action and its children.

        type: string
        """

        self.requiredBehavior = None
        """
        Defines the requiredness behavior for the action.

        type: string
        """

        self.precheckBehavior = None
        """
        Defines whether the action should usually be preselected.

        type: string
        """

        self.cardinalityBehavior = None
        """
        Defines whether the action can be selected multiple times.

        type: string
        """

        self.resource = None
        """
        The resource that is the target of the action (e.g.
        CommunicationRequest).

        reference to Reference: identifier
        """

        self.action = None
        """
        Sub actions.

        type: array
        reference to RequestGroup_Action
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'RequestGroup_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'condition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'resource'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'type'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingDuration'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'participant'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'documentation'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'RequestGroup_RelatedAction',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'relatedAction'},

            {'parent_entity': 'RequestGroup_Action',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'action'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingRange'},
        ]


class RequestGroup_Condition(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
    """

    __name__ = 'RequestGroup_Condition'

    def __init__(self, dict_values=None):
        self.kind = None
        """
        The kind of condition.

        type: string
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


class RequestGroup_RelatedAction(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
    """

    __name__ = 'RequestGroup_RelatedAction'

    def __init__(self, dict_values=None):
        self.actionId = None
        """
        The element id of the action this is related to.

        type: string
        """

        self.relationship = None
        """
        The relationship of this action to the related action.

        type: string
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

    def get_relationships(self):

        return [
            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_RelatedAction',
             'child_variable': 'offsetDuration'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_RelatedAction',
             'child_variable': 'offsetRange'},
        ]
