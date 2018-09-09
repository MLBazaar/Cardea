from .fhirbase import fhirbase


class Goal(fhirbase):
    """
    Describes the intended objective(s) for a patient, group or
    organization care, for example, weight loss, restoring an activity of
    daily living, obtaining herd immunity via immunization, meeting a
    process improvement objective, etc.
    """

    __name__ = 'Goal'

    def __init__(self, dict_values=None):
        self.resourceType = 'Goal'
        """
        This is a Goal resource

        type: string
        possible values: Goal
        """

        self.status = None
        """
        Indicates whether the goal has been reached and is still considered
        relevant.

        type: string
        possible values: proposed, accepted, planned, in-progress,
        on-target, ahead-of-target, behind-target, sustaining, achieved,
        on-hold, cancelled, entered-in-error, rejected
        """

        self.category = None
        """
        Indicates a category the goal falls within.

        type: array
        reference to CodeableConcept
        """

        self.priority = None
        """
        Identifies the mutually agreed level of importance associated with
        reaching/sustaining the goal.

        reference to CodeableConcept
        """

        self.description = None
        """
        Human-readable and/or coded description of a specific desired
        objective of care, such as "control blood pressure" or "negotiate an
        obstacle course" or "dance with child at wedding".

        reference to CodeableConcept
        """

        self.subject = None
        """
        Identifies the patient, group or organization for whom the goal is
        being established.

        reference to Reference: identifier
        """

        self.startDate = None
        """
        The date or event after which the goal should begin being pursued.

        type: string
        """

        self.startCodeableConcept = None
        """
        The date or event after which the goal should begin being pursued.

        reference to CodeableConcept
        """

        self.target = None
        """
        Indicates what should be done by when.

        reference to Goal_Target
        """

        self.statusDate = None
        """
        Identifies when the current status.  I.e. When initially created, when
        achieved, when cancelled, etc.

        type: string
        """

        self.statusReason = None
        """
        Captures the reason for the current status.

        type: string
        """

        self.expressedBy = None
        """
        Indicates whose goal this is - patient goal, practitioner goal, etc.

        reference to Reference: identifier
        """

        self.addresses = None
        """
        The identified conditions and other health record elements that are
        intended to be addressed by the goal.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Any comments related to the goal.

        type: array
        reference to Annotation
        """

        self.outcomeCode = None
        """
        Identifies the change (or lack of change) at the point when the status
        of the goal is assessed.

        type: array
        reference to CodeableConcept
        """

        self.outcomeReference = None
        """
        Details of what's changed (or not changed).

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        This records identifiers associated with this care plan that are
        defined by business processes and/or used to refer to it when a direct
        URL reference to the resource itself is not appropriate (e.g. in CDA
        documents, or in written / printed documentation).

        type: array
        reference to Identifier
        """

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
                        value, 'proposed, accepted, planned, in-progress, on-target, '
                        'ahead-of-target, behind-target, sustaining, achieved, on-hold, '
                        'cancelled, entered-in-error, rejected'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'description'},

            {'parent_entity': 'Goal_Target',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'target'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'expressedBy'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'outcomeReference'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'outcomeCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'priority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Goal',
             'child_variable': 'addresses'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'startCodeableConcept'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Goal',
             'child_variable': 'identifier'},
        ]


class Goal_Target(fhirbase):
    """
    Describes the intended objective(s) for a patient, group or
    organization care, for example, weight loss, restoring an activity of
    daily living, obtaining herd immunity via immunization, meeting a
    process improvement objective, etc.
    """

    __name__ = 'Goal_Target'

    def __init__(self, dict_values=None):
        self.measure = None
        """
        The parameter whose value is being tracked, e.g. body weight, blood
        pressure, or hemoglobin A1c level.

        reference to CodeableConcept
        """

        self.detailQuantity = None
        """
        The target value of the focus to be achieved to signify the
        fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low
        or both values of the range can be specified. When a low value is
        missing, it indicates that the goal is achieved at any focus value at
        or below the high value. Similarly, if the high value is missing, it
        indicates that the goal is achieved at any focus value at or above the
        low value.

        reference to Quantity
        """

        self.detailRange = None
        """
        The target value of the focus to be achieved to signify the
        fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low
        or both values of the range can be specified. When a low value is
        missing, it indicates that the goal is achieved at any focus value at
        or below the high value. Similarly, if the high value is missing, it
        indicates that the goal is achieved at any focus value at or above the
        low value.

        reference to Range
        """

        self.detailCodeableConcept = None
        """
        The target value of the focus to be achieved to signify the
        fulfillment of the goal, e.g. 150 pounds, 7.0%. Either the high or low
        or both values of the range can be specified. When a low value is
        missing, it indicates that the goal is achieved at any focus value at
        or below the high value. Similarly, if the high value is missing, it
        indicates that the goal is achieved at any focus value at or above the
        low value.

        reference to CodeableConcept
        """

        self.dueDate = None
        """
        Indicates either the date or the duration after start by which the
        goal should be met.

        type: string
        """

        self.dueDuration = None
        """
        Indicates either the date or the duration after start by which the
        goal should be met.

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
             'child_entity': 'Goal_Target',
             'child_variable': 'detailCodeableConcept'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'dueDuration'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'measure'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Goal_Target',
             'child_variable': 'detailQuantity'},
        ]
