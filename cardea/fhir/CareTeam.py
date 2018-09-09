from .fhirbase import fhirbase


class CareTeam(fhirbase):
    """
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """

    __name__ = 'CareTeam'

    def __init__(self, dict_values=None):
        self.resourceType = 'CareTeam'
        """
        This is a CareTeam resource

        type: string
        possible values: CareTeam
        """

        self.status = None
        """
        Indicates the current state of the care team.

        type: string
        possible values: proposed, active, suspended, inactive,
        entered-in-error
        """

        self.category = None
        """
        Identifies what kind of team.  This is to support differentiation
        between multiple co-existing teams, such as care plan team, episode of
        care team, longitudinal care team.

        type: array
        reference to CodeableConcept
        """

        self.name = None
        """
        A label for human use intended to distinguish like teams.  E.g. the
        "red" vs. "green" trauma teams.

        type: string
        """

        self.subject = None
        """
        Identifies the patient or group whose intended care is handled by the
        team.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter or episode of care that establishes the context for this
        care team.

        reference to Reference: identifier
        """

        self.period = None
        """
        Indicates when the team did (or is intended to) come into effect and
        end.

        reference to Period
        """

        self.participant = None
        """
        Identifies all people and organizations who are expected to be
        involved in the care team.

        type: array
        reference to CareTeam_Participant
        """

        self.reasonCode = None
        """
        Describes why the care team exists.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Condition(s) that this care team addresses.

        type: array
        reference to Reference: identifier
        """

        self.managingOrganization = None
        """
        The organization responsible for the care team.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Comments made about the CareTeam.

        type: array
        reference to Annotation
        """

        self.identifier = None
        """
        This records identifiers associated with this care team that are
        defined by business processes and/or used to refer to it when a direct
        URL reference to the resource itself is not appropriate.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'proposed', 'active', 'suspended', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposed, active, suspended, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'context'},

            {'parent_entity': 'CareTeam_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'subject'},
        ]


class CareTeam_Participant(fhirbase):
    """
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """

    __name__ = 'CareTeam_Participant'

    def __init__(self, dict_values=None):
        self.role = None
        """
        Indicates specific responsibility of an individual within the care
        team, such as "Primary care physician", "Trained social worker
        counselor", "Caregiver", etc.

        reference to CodeableConcept
        """

        self.member = None
        """
        The specific person or organization who is participating/expected to
        participate in the care team.

        reference to Reference: identifier
        """

        self.onBehalfOf = None
        """
        The organization of the practitioner.

        reference to Reference: identifier
        """

        self.period = None
        """
        Indicates when the specific member or organization did (or is intended
        to) come into effect and end.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'member'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'role'},
        ]
