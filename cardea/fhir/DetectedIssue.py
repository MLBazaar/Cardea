from .fhirbase import fhirbase


class DetectedIssue(fhirbase):
    """
    Indicates an actual or potential clinical issue with or between one or
    more active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition
    conflict, etc.
    """

    __name__ = 'DetectedIssue'

    def __init__(self, dict_values=None):
        self.resourceType = 'DetectedIssue'
        """
        This is a DetectedIssue resource

        type: string
        possible values: DetectedIssue
        """

        self.status = None
        """
        Indicates the status of the detected issue.

        type: string
        """

        self.category = None
        """
        Identifies the general type of issue identified.

        reference to CodeableConcept
        """

        self.severity = None
        """
        Indicates the degree of importance associated with the identified
        issue based on the potential impact on the patient.

        type: string
        possible values: high, moderate, low
        """

        self.patient = None
        """
        Indicates the patient whose record the detected issue is associated
        with.

        reference to Reference: identifier
        """

        self.date = None
        """
        The date or date-time when the detected issue was initially
        identified.

        type: string
        """

        self.author = None
        """
        Individual or device responsible for the issue being raised.  For
        example, a decision support application or a pharmacist conducting a
        medication review.

        reference to Reference: identifier
        """

        self.implicated = None
        """
        Indicates the resource representing the current activity or proposed
        activity that is potentially problematic.

        type: array
        reference to Reference: identifier
        """

        self.detail = None
        """
        A textual explanation of the detected issue.

        type: string
        """

        self.reference = None
        """
        The literature, knowledge-base or similar reference that describes the
        propensity for the detected issue identified.

        type: string
        """

        self.mitigation = None
        """
        Indicates an action that has been taken or is committed to to reduce
        or eliminate the likelihood of the risk identified by the detected
        issue from manifesting.  Can also reflect an observation of known
        mitigating factors that may reduce/eliminate the need for any action.

        type: array
        reference to DetectedIssue_Mitigation
        """

        self.identifier = None
        """
        Business identifier associated with the detected issue record.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.severity is not None:
            for value in self.severity:
                if value is not None and value.lower() not in [
                        'high', 'moderate', 'low']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'high, moderate, low'))

    def get_relationships(self):

        return [
            {'parent_entity': 'DetectedIssue_Mitigation',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'mitigation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'implicated'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'category'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'identifier'},
        ]


class DetectedIssue_Mitigation(fhirbase):
    """
    Indicates an actual or potential clinical issue with or between one or
    more active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition
    conflict, etc.
    """

    __name__ = 'DetectedIssue_Mitigation'

    def __init__(self, dict_values=None):
        self.action = None
        """
        Describes the action that was taken or the observation that was made
        that reduces/eliminates the risk associated with the identified issue.

        reference to CodeableConcept
        """

        self.date = None
        """
        Indicates when the mitigating action was documented.

        type: string
        """

        self.author = None
        """
        Identifies the practitioner who determined the mitigation and takes
        responsibility for the mitigation step occurring.

        reference to Reference: identifier
        """

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
