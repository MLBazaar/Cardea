from .fhirbase import fhirbase


class CarePlan(fhirbase):
    """
    Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient, group or community for a period
    of time, possibly limited to care for a specific condition or set of
    conditions.

    Args:
        resourceType: This is a CarePlan resource
        identifier: This records identifiers associated with this care plan
            that are defined by business processes and/or used to refer to it when
            a direct URL reference to the resource itself is not appropriate (e.g.
            in CDA documents, or in written / printed documentation).
        definition: Identifies the protocol, questionnaire, guideline or other
            specification the care plan should be conducted in accordance with.
        basedOn: A care plan that is fulfilled in whole or in part by this
            care plan.
        replaces: Completed or terminated care plan whose function is taken by
            this new care plan.
        partOf: A larger care plan of which this particular care plan is a
            component or step.
        status: Indicates whether the plan is currently being acted upon,
            represents future intentions or is now a historical record.
        intent: Indicates the level of authority/intentionality associated
            with the care plan and where the care plan fits into the workflow
            chain.
        category: Identifies what "kind" of plan this is to support
            differentiation between multiple co-existing plans; e.g. "Home
            health", "psychiatric", "asthma", "disease management", "wellness
            plan", etc.
        title: Human-friendly name for the CarePlan.
        description: A description of the scope and nature of the plan.
        subject: Identifies the patient or group whose intended care is
            described by the plan.
        context: Identifies the original context in which this particular
            CarePlan was created.
        period: Indicates when the plan did (or is intended to) come into
            effect and end.
        author: Identifies the individual(s) or ogranization who is
            responsible for the content of the care plan.
        careTeam: Identifies all people and organizations who are expected to
            be involved in the care envisioned by this plan.
        addresses: Identifies the conditions/problems/concerns/diagnoses/etc.
            whose management and/or mitigation are handled by this plan.
        supportingInfo: Identifies portions of the patient's record that
            specifically influenced the formation of the plan.  These might
            include co-morbidities, recent procedures, limitations, recent
            assessments, etc.
        goal: Describes the intended objective(s) of carrying out the care
            plan.
        activity: Identifies a planned action to occur as part of the plan.
            For example, a medication to be used, lab tests to perform,
            self-monitoring, education, etc.
        note: General notes about the care plan not covered elsewhere.
    """

    __name__ = 'CarePlan'

    def __init__(self, dict_values=None):
        self.resourceType = 'CarePlan'
        # type: str
        # possible values: CarePlan

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.replaces = None
        # type: list
        # reference to Reference: identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: draft, active, suspended, completed,
        # entered-in-error, cancelled, unknown

        self.intent = None
        # type: str
        # possible values: proposal, plan, order, option

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.title = None
        # type: str

        self.description = None
        # type: str

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.author = None
        # type: list
        # reference to Reference: identifier

        self.careTeam = None
        # type: list
        # reference to Reference: identifier

        self.addresses = None
        # type: list
        # reference to Reference: identifier

        self.supportingInfo = None
        # type: list
        # reference to Reference: identifier

        self.goal = None
        # type: list
        # reference to Reference: identifier

        self.activity = None
        # type: list
        # reference to CarePlan_Activity

        self.note = None
        # type: list
        # reference to Annotation

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'careTeam'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'context'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'note'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'goal'},

            {'parent_entity': 'CarePlan_Activity',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'activity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'addresses'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan',
             'child_variable': 'partOf'},
        ]


class CarePlan_Activity(fhirbase):
    """
    Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient, group or community for a period
    of time, possibly limited to care for a specific condition or set of
    conditions.

    Args:
        outcomeCodeableConcept: Identifies the outcome at the point when the
            status of the activity is assessed.  For example, the outcome of an
            education activity could be patient understands (or not).
        outcomeReference: Details of the outcome or action resulting from the
            activity.  The reference to an "event" resource, such as Procedure or
            Encounter or Observation, is the result/outcome of the activity
            itself.  The activity can be conveyed using CarePlan.activity.detail
            OR using the CarePlan.activity.reference (a reference to a “request”
            resource).
        progress: Notes about the adherence/status/progress of the activity.
        reference: The details of the proposed activity represented in a
            specific resource.
        detail: A simple summary of a planned activity suitable for a general
            care plan system (e.g. form driven) that doesn't know about specific
            resources such as procedure etc.
    """

    __name__ = 'CarePlan_Activity'

    def __init__(self, dict_values=None):
        self.outcomeCodeableConcept = None
        # type: list
        # reference to CodeableConcept

        self.outcomeReference = None
        # type: list
        # reference to Reference: identifier

        self.progress = None
        # type: list
        # reference to Annotation

        self.reference = None
        # reference to Reference: identifier

        self.detail = None
        # reference to CarePlan_Detail

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CarePlan_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'detail'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'progress'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'outcomeReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'reference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Activity',
             'child_variable': 'outcomeCodeableConcept'},
        ]


class CarePlan_Detail(fhirbase):
    """
    Describes the intention of how one or more practitioners intend to
    deliver care for a particular patient, group or community for a period
    of time, possibly limited to care for a specific condition or set of
    conditions.

    Args:
        category: High-level categorization of the type of activity in a care
            plan.
        definition: Identifies the protocol, questionnaire, guideline or other
            specification the planned activity should be conducted in accordance
            with.
        code: Detailed description of the type of planned activity; e.g. What
            lab test, what procedure, what kind of encounter.
        reasonCode: Provides the rationale that drove the inclusion of this
            particular activity as part of the plan or the reason why the activity
            was prohibited.
        reasonReference: Provides the health condition(s) that drove the
            inclusion of this particular activity as part of the plan.
        goal: Internal reference that identifies the goals that this activity
            is intended to contribute towards meeting.
        status: Identifies what progress is being made for the specific
            activity.
        statusReason: Provides reason why the activity isn't yet started, is
            on hold, was cancelled, etc.
        prohibited: If true, indicates that the described activity is one that
            must NOT be engaged in when following the plan.  If false, indicates
            that the described activity is one that should be engaged in when
            following the plan.
        scheduledTiming: The period, timing or frequency upon which the
            described activity is to occur.
        scheduledPeriod: The period, timing or frequency upon which the
            described activity is to occur.
        scheduledString: The period, timing or frequency upon which the
            described activity is to occur.
        location: Identifies the facility where the activity will occur; e.g.
            home, hospital, specific clinic, etc.
        performer: Identifies who's expected to be involved in the activity.
        productCodeableConcept: Identifies the food, drug or other product to
            be consumed or supplied in the activity.
        productReference: Identifies the food, drug or other product to be
            consumed or supplied in the activity.
        dailyAmount: Identifies the quantity expected to be consumed in a
            given day.
        quantity: Identifies the quantity expected to be supplied,
            administered or consumed by the subject.
        description: This provides a textual description of constraints on the
            intended activity occurrence, including relation to other activities.
            It may also include objectives, pre-conditions and end-conditions.
            Finally, it may convey specifics about the activity such as body site,
            method, route, etc.
    """

    __name__ = 'CarePlan_Detail'

    def __init__(self, dict_values=None):
        self.category = None
        # reference to CodeableConcept

        self.definition = None
        # reference to Reference: identifier

        self.code = None
        # reference to CodeableConcept

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.goal = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: not-started, scheduled, in-progress,
        # on-hold, completed, cancelled, unknown

        self.statusReason = None
        # type: str

        self.prohibited = None
        # type: bool

        self.scheduledTiming = None
        # reference to Timing

        self.scheduledPeriod = None
        # reference to Period

        self.scheduledString = None
        # type: str

        self.location = None
        # reference to Reference: identifier

        self.performer = None
        # type: list
        # reference to Reference: identifier

        self.productCodeableConcept = None
        # reference to CodeableConcept

        self.productReference = None
        # reference to Reference: identifier

        self.dailyAmount = None
        # reference to Quantity

        self.quantity = None
        # reference to Quantity

        self.description = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'not-started', 'scheduled', 'in-progress', 'on-hold', 'completed',
                        'cancelled', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'not-started, scheduled, in-progress, on-hold, completed, '
                        'cancelled, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'scheduledPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'productReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'dailyAmount'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'performer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'scheduledTiming'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'goal'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'location'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'productCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CarePlan_Detail',
             'child_variable': 'definition'},
        ]
