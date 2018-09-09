from .fhirbase import fhirbase


class DetectedIssue(fhirbase):
    """Indicates an actual or potential clinical issue with or between one or
    more active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition
    conflict, etc.
    """

    __name__ = 'DetectedIssue'

    def __init__(self, dict_values=None):
        # this is a detectedissue resource
        self.resourceType = 'DetectedIssue'
        # type = string
        # possible values: DetectedIssue

        # indicates the status of the detected issue.
        self.status = None
        # type = string

        # identifies the general type of issue identified.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the degree of importance associated with the identified issue
        # based on the potential impact on the patient.
        self.severity = None
        # type = string
        # possible values: high, moderate, low

        # indicates the patient whose record the detected issue is associated
        # with.
        self.patient = None
        # reference to Reference: identifier

        # the date or date-time when the detected issue was initially identified.
        self.date = None
        # type = string

        # individual or device responsible for the issue being raised.  for
        # example, a decision support application or a pharmacist conducting a
        # medication review.
        self.author = None
        # reference to Reference: identifier

        # indicates the resource representing the current activity or proposed
        # activity that is potentially problematic.
        self.implicated = None
        # type = array
        # reference to Reference: identifier

        # a textual explanation of the detected issue.
        self.detail = None
        # type = string

        # the literature, knowledge-base or similar reference that describes the
        # propensity for the detected issue identified.
        self.reference = None
        # type = string

        # indicates an action that has been taken or is committed to to reduce or
        # eliminate the likelihood of the risk identified by the detected issue
        # from manifesting.  can also reflect an observation of known mitigating
        # factors that may reduce/eliminate the need for any action.
        self.mitigation = None
        # type = array
        # reference to DetectedIssue_Mitigation: DetectedIssue_Mitigation

        # business identifier associated with the detected issue record.
        self.identifier = None
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'implicated'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DetectedIssue',
             'child_variable': 'patient'},

            {'parent_entity': 'DetectedIssue_Mitigation',
             'parent_variable': 'object_id',
             'child_entity': 'DetectedIssue',
             'child_variable': 'mitigation'},
        ]


class DetectedIssue_Mitigation(fhirbase):
    """Indicates an actual or potential clinical issue with or between one or
    more active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition
    conflict, etc.
    """

    __name__ = 'DetectedIssue_Mitigation'

    def __init__(self, dict_values=None):
        # describes the action that was taken or the observation that was made
        # that reduces/eliminates the risk associated with the identified issue.
        self.action = None
        # reference to CodeableConcept: CodeableConcept

        # indicates when the mitigating action was documented.
        self.date = None
        # type = string

        # identifies the practitioner who determined the mitigation and takes
        # responsibility for the mitigation step occurring.
        self.author = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
