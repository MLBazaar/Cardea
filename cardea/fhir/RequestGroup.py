from .fhirbase import fhirbase


class RequestGroup(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".

    Args:
        resourceType: This is a RequestGroup resource
        identifier: Allows a service to provide a unique, business identifier
            for the request.
        definition: A protocol, guideline, orderset or other definition that
            is adhered to in whole or in part by this request.
        basedOn: A plan, proposal or order that is fulfilled in whole or in
            part by this request.
        replaces: Completed or terminated request(s) whose function is taken
            by this new request.
        groupIdentifier: A shared identifier common to all requests that were
            authorized more or less simultaneously by a single author,
            representing the identifier of the requisition, prescription or
            similar form.
        status: The current state of the request. For request groups, the
            status reflects the status of all the requests in the group.
        intent: Indicates the level of authority/intentionality associated
            with the request and where the request fits into the workflow chain.
        priority: Indicates how quickly the request should be addressed with
            respect to other requests.
        subject: The subject for which the request group was created.
        context: Describes the context of the request group, if any.
        authoredOn: Indicates when the request group was created.
        author: Provides a reference to the author of the request group.
        reasonCodeableConcept: Indicates the reason the request group was
            created. This is typically provided as a parameter to the evaluation
            and echoed by the service, although for some use cases, such as
            subscription- or event-based scenarios, it may provide an indication
            of the cause for the response.
        reasonReference: Indicates the reason the request group was created.
            This is typically provided as a parameter to the evaluation and echoed
            by the service, although for some use cases, such as subscription- or
            event-based scenarios, it may provide an indication of the cause for
            the response.
        note: Provides a mechanism to communicate additional information about
            the response.
        action: The actions, if any, produced by the evaluation of the
            artifact.
    """

    __name__ = 'RequestGroup'

    def __init__(self, dict_values=None):
        self.resourceType = 'RequestGroup'
        # type: str
        # possible values: RequestGroup

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.replaces = None
        # type: list
        # reference to Reference: identifier

        self.groupIdentifier = None
        # reference to Identifier

        self.status = None
        # type: str

        self.intent = None
        # type: str

        self.priority = None
        # type: str

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.authoredOn = None
        # type: str

        self.author = None
        # reference to Reference: identifier

        self.reasonCodeableConcept = None
        # reference to CodeableConcept

        self.reasonReference = None
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.action = None
        # type: list
        # reference to RequestGroup_Action

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
             'child_entity': 'RequestGroup',
             'child_variable': 'basedOn'},

            {'parent_entity': 'RequestGroup_Action',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'action'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'definition'},
        ]


class RequestGroup_Action(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".

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
        documentation: Didactic or other informational resources associated
            with the action that can be provided to the CDS recipient. Information
            resources can include inline text commentary and links to web
            resources.
        condition: An expression that describes applicability criteria, or
            start/stop conditions for the action.
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
        participant: The participant that should perform or be responsible for
            this action.
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
        resource: The resource that is the target of the action (e.g.
            CommunicationRequest).
        action: Sub actions.
    """

    __name__ = 'RequestGroup_Action'

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

        self.documentation = None
        # type: list
        # reference to RelatedArtifact

        self.condition = None
        # type: list
        # reference to RequestGroup_Condition

        self.relatedAction = None
        # type: list
        # reference to RequestGroup_RelatedAction

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
        # reference to Reference: identifier

        self.type = None
        # reference to Coding

        self.groupingBehavior = None
        # type: str

        self.selectionBehavior = None
        # type: str

        self.requiredBehavior = None
        # type: str

        self.precheckBehavior = None
        # type: str

        self.cardinalityBehavior = None
        # type: str

        self.resource = None
        # reference to Reference: identifier

        self.action = None
        # type: list
        # reference to RequestGroup_Action

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'code'},

            {'parent_entity': 'RequestGroup_Action',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'action'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingDuration'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingRange'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'resource'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'documentation'},

            {'parent_entity': 'RequestGroup_RelatedAction',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'relatedAction'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'type'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'RequestGroup_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'condition'},
        ]


class RequestGroup_Condition(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".

    Args:
        kind: The kind of condition.
        description: A brief, natural language description of the condition
            that effectively communicates the intended semantics.
        language: The media type of the language for the expression.
        expression: An expression that returns true or false, indicating
            whether or not the condition is satisfied.
    """

    __name__ = 'RequestGroup_Condition'

    def __init__(self, dict_values=None):
        self.kind = None
        # type: str

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


class RequestGroup_RelatedAction(fhirbase):
    """
    A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".

    Args:
        actionId: The element id of the action this is related to.
        relationship: The relationship of this action to the related action.
        offsetDuration: A duration or range of durations to apply to the
            relationship. For example, 30-60 minutes before.
        offsetRange: A duration or range of durations to apply to the
            relationship. For example, 30-60 minutes before.
    """

    __name__ = 'RequestGroup_RelatedAction'

    def __init__(self, dict_values=None):
        self.actionId = None
        # type: str

        self.relationship = None
        # type: str

        self.offsetDuration = None
        # reference to Duration

        self.offsetRange = None
        # reference to Range

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
