from .fhirbase import fhirbase


class DetectedIssue(fhirbase):
    """
    Indicates an actual or potential clinical issue with or between one or
    more active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition
    conflict, etc.

    Args:
        resourceType: This is a DetectedIssue resource
        identifier: Business identifier associated with the detected issue
            record.
        status: Indicates the status of the detected issue.
        category: Identifies the general type of issue identified.
        severity: Indicates the degree of importance associated with the
            identified issue based on the potential impact on the patient.
        patient: Indicates the patient whose record the detected issue is
            associated with.
        date: The date or date-time when the detected issue was initially
            identified.
        author: Individual or device responsible for the issue being raised.
            For example, a decision support application or a pharmacist conducting
            a medication review.
        implicated: Indicates the resource representing the current activity
            or proposed activity that is potentially problematic.
        detail: A textual explanation of the detected issue.
        reference: The literature, knowledge-base or similar reference that
            describes the propensity for the detected issue identified.
        mitigation: Indicates an action that has been taken or is committed to
            to reduce or eliminate the likelihood of the risk identified by the
            detected issue from manifesting.  Can also reflect an observation of
            known mitigating factors that may reduce/eliminate the need for any
            action.
    """

    __name__ = 'DetectedIssue'

    def __init__(self, dict_values=None):
        self.resourceType = 'DetectedIssue'
        # type: str
        # possible values: DetectedIssue

        self.status = None
        # type: str

        self.category = None
        # reference to CodeableConcept

        self.severity = None
        # type: str
        # possible values: high, moderate, low

        self.patient = None
        # reference to Reference: identifier

        self.date = None
        # type: str

        self.author = None
        # reference to Reference: identifier

        self.implicated = None
        # type: list
        # reference to Reference: identifier

        self.detail = None
        # type: str

        self.reference = None
        # type: str

        self.mitigation = None
        # type: list
        # reference to DetectedIssue_Mitigation

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.severity is not None:
            for value in self.severity:
                if value is not None and value.lower() not in [
                        'high', 'moderate', 'low']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'high, moderate, low'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'author'},

            {'parent_entity': 'DetectedIssue_Mitigation',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'mitigation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'patient'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'implicated'},
        ]


class DetectedIssue_Mitigation(fhirbase):
    """
    Indicates an actual or potential clinical issue with or between one or
    more active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition
    conflict, etc.

    Args:
        action: Describes the action that was taken or the observation that
            was made that reduces/eliminates the risk associated with the
            identified issue.
        date: Indicates when the mitigating action was documented.
        author: Identifies the practitioner who determined the mitigation and
            takes responsibility for the mitigation step occurring.
    """

    __name__ = 'DetectedIssue_Mitigation'

    def __init__(self, dict_values=None):
        self.action = None
        # reference to CodeableConcept

        self.date = None
        # type: str

        self.author = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue_Mitigation',
             'child_variable': 'action'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue_Mitigation',
             'child_variable': 'author'},
        ]
