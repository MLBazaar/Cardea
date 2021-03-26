from .fhirbase import fhirbase


class Goal(fhirbase):
    """
    Describes the intended objective(s) for a patient, group or
    organization care, for example, weight loss, restoring an activity of
    daily living, obtaining herd immunity via immunization, meeting a
    process improvement objective, etc.

    Args:
        resourceType: This is a Goal resource
        identifier: This records identifiers associated with this care plan
            that are defined by business processes and/or used to refer to it when
            a direct URL reference to the resource itself is not appropriate (e.g.
            in CDA documents, or in written / printed documentation).
        status: Indicates whether the goal has been reached and is still
            considered relevant.
        category: Indicates a category the goal falls within.
        priority: Identifies the mutually agreed level of importance
            associated with reaching/sustaining the goal.
        description: Human-readable and/or coded description of a specific
            desired objective of care, such as "control blood pressure" or
            "negotiate an obstacle course" or "dance with child at wedding".
        subject: Identifies the patient, group or organization for whom the
            goal is being established.
        startDate: The date or event after which the goal should begin being
            pursued.
        startCodeableConcept: The date or event after which the goal should
            begin being pursued.
        target: Indicates what should be done by when.
        statusDate: Identifies when the current status.  I.e. When initially
            created, when achieved, when cancelled, etc.
        statusReason: Captures the reason for the current status.
        expressedBy: Indicates whose goal this is - patient goal, practitioner
            goal, etc.
        addresses: The identified conditions and other health record elements
            that are intended to be addressed by the goal.
        note: Any comments related to the goal.
        outcomeCode: Identifies the change (or lack of change) at the point
            when the status of the goal is assessed.
        outcomeReference: Details of what's changed (or not changed).
    """

    __name__ = 'Goal'

    def __init__(self, dict_values=None):
        self.resourceType = 'Goal'
        # type: str
        # possible values: Goal

        self.status = None
        # type: str
        # possible values: proposed, accepted, planned, in-progress,
        # on-target, ahead-of-target, behind-target, sustaining, achieved,
        # on-hold, cancelled, entered-in-error, rejected

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.priority = None
        # reference to CodeableConcept

        self.description = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.startDate = None
        # type: str

        self.startCodeableConcept = None
        # reference to CodeableConcept

        self.target = None
        # reference to Goal_Target

        self.statusDate = None
        # type: str

        self.statusReason = None
        # type: str

        self.expressedBy = None
        # reference to Reference: identifier

        self.addresses = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.outcomeCode = None
        # type: list
        # reference to CodeableConcept

        self.outcomeReference = None
        # type: list
        # reference to Reference: identifier

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
                    'proposed', 'accepted', 'planned', 'in-progress', 'on-target',
                    'ahead-of-target', 'behind-target', 'sustaining', 'achieved',
                        'on-hold', 'cancelled', 'entered-in-error', 'rejected']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposed, accepted, planned, in-progress, on-target, '
                        'ahead-of-target, behind-target, sustaining, achieved, on-hold, '
                        'cancelled, entered-in-error, rejected'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'addresses'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'outcomeReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'identifier'},

            {'parent_entity': 'Goal_Target',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'target'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'outcomeCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'priority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'expressedBy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'startCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'description'},
        ]


class Goal_Target(fhirbase):
    """
    Describes the intended objective(s) for a patient, group or
    organization care, for example, weight loss, restoring an activity of
    daily living, obtaining herd immunity via immunization, meeting a
    process improvement objective, etc.

    Args:
        measure: The parameter whose value is being tracked, e.g. body weight,
            blood pressure, or hemoglobin A1c level.
        detailQuantity: The target value of the focus to be achieved to
            signify the fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the
            high or low or both values of the range can be specified. When a low
            value is missing, it indicates that the goal is achieved at any focus
            value at or below the high value. Similarly, if the high value is
            missing, it indicates that the goal is achieved at any focus value at
            or above the low value.
        detailRange: The target value of the focus to be achieved to signify
            the fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or
            low or both values of the range can be specified. When a low value is
            missing, it indicates that the goal is achieved at any focus value at
            or below the high value. Similarly, if the high value is missing, it
            indicates that the goal is achieved at any focus value at or above the
            low value.
        detailCodeableConcept: The target value of the focus to be achieved to
            signify the fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the
            high or low or both values of the range can be specified. When a low
            value is missing, it indicates that the goal is achieved at any focus
            value at or below the high value. Similarly, if the high value is
            missing, it indicates that the goal is achieved at any focus value at
            or above the low value.
        dueDate: Indicates either the date or the duration after start by
            which the goal should be met.
        dueDuration: Indicates either the date or the duration after start by
            which the goal should be met.
    """

    __name__ = 'Goal_Target'

    def __init__(self, dict_values=None):
        self.measure = None
        # reference to CodeableConcept

        self.detailQuantity = None
        # reference to Quantity

        self.detailRange = None
        # reference to Range

        self.detailCodeableConcept = None
        # reference to CodeableConcept

        self.dueDate = None
        # type: str

        self.dueDuration = None
        # reference to Duration

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'measure'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'dueDuration'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailCodeableConcept'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailQuantity'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailRange'},
        ]
