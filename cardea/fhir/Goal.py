from .fhirbase import fhirbase


class Goal(fhirbase):
    """Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    def __init__(self, dict_values=None):
        # this is a goal resource
        self.resourceType = 'Goal'
        # type = string
        # possible values: Goal

        # indicates whether the goal has been reached and is still considered
        # relevant.
        self.status = None
        # type = string
        # possible values: proposed, accepted, planned, in-progress, on-
        # target, ahead-of-target, behind-target, sustaining, achieved, on-hold,
        # cancelled, entered-in-error, rejected

        # indicates a category the goal falls within.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # identifies the mutually agreed level of importance associated with
        # reaching/sustaining the goal.
        self.priority = None
        # reference to CodeableConcept: CodeableConcept

        # human-readable and/or coded description of a specific desired objective
        # of care, such as "control blood pressure" or "negotiate an obstacle
        # course" or "dance with child at wedding".
        self.description = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the patient, group or organization for whom the goal is being
        # established.
        self.subject = None
        # reference to Reference: identifier

        # the date or event after which the goal should begin being pursued.
        self.startDate = None
        # type = string

        # the date or event after which the goal should begin being pursued.
        self.startCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # indicates what should be done by when.
        self.target = None
        # reference to Goal_Target: Goal_Target

        # identifies when the current status.  i.e. when initially created, when
        # achieved, when cancelled, etc.
        self.statusDate = None
        # type = string

        # captures the reason for the current status.
        self.statusReason = None
        # type = string

        # indicates whose goal this is - patient goal, practitioner goal, etc.
        self.expressedBy = None
        # reference to Reference: identifier

        # the identified conditions and other health record elements that are
        # intended to be addressed by the goal.
        self.addresses = None
        # type = array
        # reference to Reference: identifier

        # any comments related to the goal.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # identifies the change (or lack of change) at the point when the status
        # of the goal is assessed.
        self.outcomeCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # details of what's changed (or not changed).
        self.outcomeReference = None
        # type = array
        # reference to Reference: identifier

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
                        'proposed', 'accepted', 'planned', 'in-progress', 'on-target',
                        'ahead-of-target', 'behind-target', 'sustaining', 'achieved',
                        'on-hold', 'cancelled', 'entered-in-error', 'rejected']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposed, accepted, planned, in-progress, on-target,'
                        'ahead-of-target, behind-target, sustaining, achieved, on-hold,'
                        'cancelled, entered-in-error, rejected'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'outcomeCode'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'identifier'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'note'},

            {'parent_entity': 'Goal_Target',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'target'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'expressedBy'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'addresses'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'description'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'startCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'priority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'outcomeReference'},
        ]


class Goal_Target(fhirbase):
    """Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """

    def __init__(self, dict_values=None):
        # the parameter whose value is being tracked, e.g. body weight, blood
        # pressure, or hemoglobin a1c level.
        self.measure = None
        # reference to CodeableConcept: CodeableConcept

        # the target value of the focus to be achieved to signify the fulfillment
        # of the goal, e.g. 150 pounds, 7.0%. either the high or low or both
        # values of the range can be specified. when a low value is missing, it
        # indicates that the goal is achieved at any focus value at or below the
        # high value. similarly, if the high value is missing, it indicates that
        # the goal is achieved at any focus value at or above the low value.
        self.detailQuantity = None
        # reference to Quantity: Quantity

        # the target value of the focus to be achieved to signify the fulfillment
        # of the goal, e.g. 150 pounds, 7.0%. either the high or low or both
        # values of the range can be specified. when a low value is missing, it
        # indicates that the goal is achieved at any focus value at or below the
        # high value. similarly, if the high value is missing, it indicates that
        # the goal is achieved at any focus value at or above the low value.
        self.detailRange = None
        # reference to Range: Range

        # the target value of the focus to be achieved to signify the fulfillment
        # of the goal, e.g. 150 pounds, 7.0%. either the high or low or both
        # values of the range can be specified. when a low value is missing, it
        # indicates that the goal is achieved at any focus value at or below the
        # high value. similarly, if the high value is missing, it indicates that
        # the goal is achieved at any focus value at or above the low value.
        self.detailCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # indicates either the date or the duration after start by which the goal
        # should be met.
        self.dueDate = None
        # type = string

        # indicates either the date or the duration after start by which the goal
        # should be met.
        self.dueDuration = None
        # reference to Duration: Duration

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'dueDuration'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'measure'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailCodeableConcept'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailRange'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailQuantity'},
        ]
