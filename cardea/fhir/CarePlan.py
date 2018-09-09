from .fhirbase import fhirbase


class CarePlan(fhirbase):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient, group or community for a period
    of time, possibly limited to care for a specific condition or set of
    conditions.
    """

    __name__ = 'CarePlan'

    def __init__(self, dict_values=None):
        # this is a careplan resource
        self.resourceType = 'CarePlan'
        # type = string
        # possible values: CarePlan

        # identifies the protocol, questionnaire, guideline or other specification
        # the care plan should be conducted in accordance with.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # a care plan that is fulfilled in whole or in part by this care plan.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # completed or terminated care plan whose function is taken by this new
        # care plan.
        self.replaces = None
        # type = array
        # reference to Reference: identifier

        # a larger care plan of which this particular care plan is a component or
        # step.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # indicates whether the plan is currently being acted upon, represents
        # future intentions or is now a historical record.
        self.status = None
        # type = string
        # possible values: draft, active, suspended, completed, entered-
        # in-error, cancelled, unknown

        # indicates the level of authority/intentionality associated with the care
        # plan and where the care plan fits into the workflow chain.
        self.intent = None
        # type = string
        # possible values: proposal, plan, order, option

        # identifies what "kind" of plan this is to support differentiation
        # between multiple co-existing plans; e.g. "home health", "psychiatric",
        # "asthma", "disease management", "wellness plan", etc.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # human-friendly name for the careplan.
        self.title = None
        # type = string

        # a description of the scope and nature of the plan.
        self.description = None
        # type = string

        # identifies the patient or group whose intended care is described by the
        # plan.
        self.subject = None
        # reference to Reference: identifier

        # identifies the original context in which this particular careplan was
        # created.
        self.context = None
        # reference to Reference: identifier

        # indicates when the plan did (or is intended to) come into effect and
        # end.
        self.period = None
        # reference to Period: Period

        # identifies the individual(s) or ogranization who is responsible for the
        # content of the care plan.
        self.author = None
        # type = array
        # reference to Reference: identifier

        # identifies all people and organizations who are expected to be involved
        # in the care envisioned by this plan.
        self.careTeam = None
        # type = array
        # reference to Reference: identifier

        # identifies the conditions/problems/concerns/diagnoses/etc. whose
        # management and/or mitigation are handled by this plan.
        self.addresses = None
        # type = array
        # reference to Reference: identifier

        # identifies portions of the patient's record that specifically influenced
        # the formation of the plan.  these might include co-morbidities, recent
        # procedures, limitations, recent assessments, etc.
        self.supportingInfo = None
        # type = array
        # reference to Reference: identifier

        # describes the intended objective(s) of carrying out the care plan.
        self.goal = None
        # type = array
        # reference to Reference: identifier

        # identifies a planned action to occur as part of the plan.  for example,
        # a medication to be used, lab tests to perform, self-monitoring,
        # education, etc.
        self.activity = None
        # type = array
        # reference to CarePlan_Activity: CarePlan_Activity

        # general notes about the care plan not covered elsewhere.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # this records identifiers associated with this care plan that are defined
        # by business processes and/or used to refer to it when a direct url
        # reference to the resource itself is not appropriate (e.g. in cda
        # documents, or in written / printed documentation).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'draft', 'active', 'suspended', 'completed', 'entered-in-error',
                        'cancelled', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, suspended, completed, entered-in-error, cancelled,'
                        'unknown'))

        if self.intent is not None:
            for value in self.intent:
                if value is not None and value.lower() not in [
                        'proposal', 'plan', 'order', 'option']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposal, plan, order, option'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'partOf'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'period'},

            {'parent_entity': 'CarePlan_Activity',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'activity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'addresses'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'author'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'goal'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'careTeam'},
        ]


class CarePlan_Activity(fhirbase):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient, group or community for a period
    of time, possibly limited to care for a specific condition or set of
    conditions.
    """

    __name__ = 'CarePlan_Activity'

    def __init__(self, dict_values=None):
        # identifies the outcome at the point when the status of the activity is
        # assessed.  for example, the outcome of an education activity could be
        # patient understands (or not).
        self.outcomeCodeableConcept = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # details of the outcome or action resulting from the activity.  the
        # reference to an "event" resource, such as procedure or encounter or
        # observation, is the result/outcome of the activity itself.  the activity
        # can be conveyed using careplan.activity.detail or using the
        # careplan.activity.reference (a reference to a “request” resource).
        self.outcomeReference = None
        # type = array
        # reference to Reference: identifier

        # notes about the adherence/status/progress of the activity.
        self.progress = None
        # type = array
        # reference to Annotation: Annotation

        # the details of the proposed activity represented in a specific resource.
        self.reference = None
        # reference to Reference: identifier

        # a simple summary of a planned activity suitable for a general care plan
        # system (e.g. form driven) that doesn't know about specific resources
        # such as procedure etc.
        self.detail = None
        # reference to CarePlan_Detail: CarePlan_Detail

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'progress'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'outcomeReference'},

            {'parent_entity': 'CarePlan_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'outcomeCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'reference'},
        ]


class CarePlan_Detail(fhirbase):
    """Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient, group or community for a period
    of time, possibly limited to care for a specific condition or set of
    conditions.
    """

    __name__ = 'CarePlan_Detail'

    def __init__(self, dict_values=None):
        # high-level categorization of the type of activity in a care plan.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the protocol, questionnaire, guideline or other specification
        # the planned activity should be conducted in accordance with.
        self.definition = None
        # reference to Reference: identifier

        # detailed description of the type of planned activity; e.g. what lab
        # test, what procedure, what kind of encounter.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # provides the rationale that drove the inclusion of this particular
        # activity as part of the plan or the reason why the activity was
        # prohibited.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # provides the health condition(s) that drove the inclusion of this
        # particular activity as part of the plan.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # internal reference that identifies the goals that this activity is
        # intended to contribute towards meeting.
        self.goal = None
        # type = array
        # reference to Reference: identifier

        # identifies what progress is being made for the specific activity.
        self.status = None
        # type = string
        # possible values: not-started, scheduled, in-progress, on-hold,
        # completed, cancelled, unknown

        # provides reason why the activity isn't yet started, is on hold, was
        # cancelled, etc.
        self.statusReason = None
        # type = string

        # if true, indicates that the described activity is one that must not be
        # engaged in when following the plan.  if false, indicates that the
        # described activity is one that should be engaged in when following the
        # plan.
        self.prohibited = None
        # type = boolean

        # the period, timing or frequency upon which the described activity is to
        # occur.
        self.scheduledTiming = None
        # reference to Timing: Timing

        # the period, timing or frequency upon which the described activity is to
        # occur.
        self.scheduledPeriod = None
        # reference to Period: Period

        # the period, timing or frequency upon which the described activity is to
        # occur.
        self.scheduledString = None
        # type = string

        # identifies the facility where the activity will occur; e.g. home,
        # hospital, specific clinic, etc.
        self.location = None
        # reference to Reference: identifier

        # identifies who's expected to be involved in the activity.
        self.performer = None
        # type = array
        # reference to Reference: identifier

        # identifies the food, drug or other product to be consumed or supplied in
        # the activity.
        self.productCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the food, drug or other product to be consumed or supplied in
        # the activity.
        self.productReference = None
        # reference to Reference: identifier

        # identifies the quantity expected to be consumed in a given day.
        self.dailyAmount = None
        # reference to Quantity: Quantity

        # identifies the quantity expected to be supplied, administered or
        # consumed by the subject.
        self.quantity = None
        # reference to Quantity: Quantity

        # this provides a textual description of constraints on the intended
        # activity occurrence, including relation to other activities.  it may
        # also include objectives, pre-conditions and end-conditions.  finally, it
        # may convey specifics about the activity such as body site, method,
        # route, etc.
        self.description = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'not-started', 'scheduled', 'in-progress', 'on-hold', 'completed',
                        'cancelled', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'not-started, scheduled, in-progress, on-hold, completed,'
                        'cancelled, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'code'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'scheduledPeriod'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'productReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'goal'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'dailyAmount'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'scheduledTiming'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'productCodeableConcept'},
        ]
