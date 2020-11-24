from .fhirbase import fhirbase


class CareTeam(fhirbase):
    """
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.

    Args:
        resourceType: This is a CareTeam resource
        identifier: This records identifiers associated with this care team
            that are defined by business processes and/or used to refer to it when
            a direct URL reference to the resource itself is not appropriate.
        status: Indicates the current state of the care team.
        category: Identifies what kind of team.  This is to support
            differentiation between multiple co-existing teams, such as care plan
            team, episode of care team, longitudinal care team.
        name: A label for human use intended to distinguish like teams.  E.g.
            the "red" vs. "green" trauma teams.
        subject: Identifies the patient or group whose intended care is
            handled by the team.
        context: The encounter or episode of care that establishes the context
            for this care team.
        period: Indicates when the team did (or is intended to) come into
            effect and end.
        participant: Identifies all people and organizations who are expected
            to be involved in the care team.
        reasonCode: Describes why the care team exists.
        reasonReference: Condition(s) that this care team addresses.
        managingOrganization: The organization responsible for the care team.
        note: Comments made about the CareTeam.
    """

    __name__ = 'CareTeam'

    def __init__(self, dict_values=None):
        self.resourceType = 'CareTeam'
        # type: str
        # possible values: CareTeam

        self.status = None
        # type: str
        # possible values: proposed, active, suspended, inactive,
        # entered-in-error

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.name = None
        # type: str

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.participant = None
        # type: list
        # reference to CareTeam_Participant

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.managingOrganization = None
        # type: list
        # reference to Reference: identifier

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
                        'proposed', 'active', 'suspended', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposed, active, suspended, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'CareTeam_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'participant'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'category'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'period'},
        ]


class CareTeam_Participant(fhirbase):
    """
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.

    Args:
        role: Indicates specific responsibility of an individual within the
            care team, such as "Primary care physician", "Trained social worker
            counselor", "Caregiver", etc.
        member: The specific person or organization who is
            participating/expected to participate in the care team.
        onBehalfOf: The organization of the practitioner.
        period: Indicates when the specific member or organization did (or is
            intended to) come into effect and end.
    """

    __name__ = 'CareTeam_Participant'

    def __init__(self, dict_values=None):
        self.role = None
        # reference to CodeableConcept

        self.member = None
        # reference to Reference: identifier

        self.onBehalfOf = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'member'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam_Participant',
             'child_variable': 'period'},
        ]
