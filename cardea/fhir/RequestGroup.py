from .fhirbase import fhirbase


class RequestGroup(fhirbase):
    """A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
    """

    def __init__(self, dict_values=None):
        # this is a requestgroup resource
        self.resourceType = 'RequestGroup'
        # type = string
        # possible values: RequestGroup

        # a protocol, guideline, orderset or other definition that is adhered to
        # in whole or in part by this request.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # a plan, proposal or order that is fulfilled in whole or in part by this
        # request.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # completed or terminated request(s) whose function is taken by this new
        # request.
        self.replaces = None
        # type = array
        # reference to Reference: identifier

        # a shared identifier common to all requests that were authorized more or
        # less simultaneously by a single author, representing the identifier of
        # the requisition, prescription or similar form.
        self.groupIdentifier = None
        # reference to Identifier: Identifier

        # the current state of the request. for request groups, the status
        # reflects the status of all the requests in the group.
        self.status = None
        # type = string

        # indicates the level of authority/intentionality associated with the
        # request and where the request fits into the workflow chain.
        self.intent = None
        # type = string

        # indicates how quickly the request should be addressed with respect to
        # other requests.
        self.priority = None
        # type = string

        # the subject for which the request group was created.
        self.subject = None
        # reference to Reference: identifier

        # describes the context of the request group, if any.
        self.context = None
        # reference to Reference: identifier

        # indicates when the request group was created.
        self.authoredOn = None
        # type = string

        # provides a reference to the author of the request group.
        self.author = None
        # reference to Reference: identifier

        # indicates the reason the request group was created. this is typically
        # provided as a parameter to the evaluation and echoed by the service,
        # although for some use cases, such as subscription- or event-based
        # scenarios, it may provide an indication of the cause for the response.
        self.reasonCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the reason the request group was created. this is typically
        # provided as a parameter to the evaluation and echoed by the service,
        # although for some use cases, such as subscription- or event-based
        # scenarios, it may provide an indication of the cause for the response.
        self.reasonReference = None
        # reference to Reference: identifier

        # provides a mechanism to communicate additional information about the
        # response.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # the actions, if any, produced by the evaluation of the artifact.
        self.action = None
        # type = array
        # reference to RequestGroup_Action: RequestGroup_Action

        # allows a service to provide a unique, business identifier for the
        # request.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'definition'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'author'},

            {'parent_entity': 'RequestGroup_Action',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'action'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup',
             'child_variable': 'subject'},
        ]


class RequestGroup_Action(fhirbase):
    """A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
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

        # didactic or other informational resources associated with the action
        # that can be provided to the cds recipient. information resources can
        # include inline text commentary and links to web resources.
        self.documentation = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # an expression that describes applicability criteria, or start/stop
        # conditions for the action.
        self.condition = None
        # type = array
        # reference to RequestGroup_Condition: RequestGroup_Condition

        # a relationship to another action such as "before" or "30-60 minutes
        # after start of".
        self.relatedAction = None
        # type = array
        # reference to RequestGroup_RelatedAction: RequestGroup_RelatedAction

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

        # the participant that should perform or be responsible for this action.
        self.participant = None
        # type = array
        # reference to Reference: identifier

        # the type of action to perform (create, update, remove).
        self.type = None
        # reference to Coding: Coding

        # defines the grouping behavior for the action and its children.
        self.groupingBehavior = None
        # type = string

        # defines the selection behavior for the action and its children.
        self.selectionBehavior = None
        # type = string

        # defines the requiredness behavior for the action.
        self.requiredBehavior = None
        # type = string

        # defines whether the action should usually be preselected.
        self.precheckBehavior = None
        # type = string

        # defines whether the action can be selected multiple times.
        self.cardinalityBehavior = None
        # type = string

        # the resource that is the target of the action (e.g.
        # communicationrequest).
        self.resource = None
        # reference to Reference: identifier

        # sub actions.
        self.action = None
        # type = array
        # reference to RequestGroup_Action: RequestGroup_Action

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'resource'},

            {'parent_entity': 'RequestGroup_RelatedAction',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'relatedAction'},

            {'parent_entity': 'RequestGroup_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'condition'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'type'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'documentation'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'code'},

            {'parent_entity': 'RequestGroup_Action',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'action'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingDuration'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'participant'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'RequestGroup_Action',
             'child_variable': 'timingTiming'},
        ]


class RequestGroup_Condition(fhirbase):
    """A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
    """

    def __init__(self, dict_values=None):
        # the kind of condition.
        self.kind = None
        # type = string

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


class RequestGroup_RelatedAction(fhirbase):
    """A group of related requests that can be used to capture intended
    activities that have inter-dependencies such as "give this medication
    after that one".
    """

    def __init__(self, dict_values=None):
        # the element id of the action this is related to.
        self.actionId = None
        # type = string

        # the relationship of this action to the related action.
        self.relationship = None
        # type = string

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
