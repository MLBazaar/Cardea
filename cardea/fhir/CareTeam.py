from .fhirbase import fhirbase


class CareTeam(fhirbase):
    """The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """

    def __init__(self, dict_values=None):
        # this is a careteam resource
        self.resourceType = 'CareTeam'
        # type = string
        # possible values: CareTeam

        # indicates the current state of the care team.
        self.status = None
        # type = string
        # possible values: proposed, active, suspended, inactive,
        # entered-in-error

        # identifies what kind of team.  this is to support differentiation
        # between multiple co-existing teams, such as care plan team, episode of
        # care team, longitudinal care team.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a label for human use intended to distinguish like teams.  e.g. the
        # "red" vs. "green" trauma teams.
        self.name = None
        # type = string

        # identifies the patient or group whose intended care is handled by the
        # team.
        self.subject = None
        # reference to Reference: identifier

        # the encounter or episode of care that establishes the context for this
        # care team.
        self.context = None
        # reference to Reference: identifier

        # indicates when the team did (or is intended to) come into effect and
        # end.
        self.period = None
        # reference to Period: Period

        # identifies all people and organizations who are expected to be involved
        # in the care team.
        self.participant = None
        # type = array
        # reference to CareTeam_Participant: CareTeam_Participant

        # describes why the care team exists.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # condition(s) that this care team addresses.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # the organization responsible for the care team.
        self.managingOrganization = None
        # type = array
        # reference to Reference: identifier

        # comments made about the careteam.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # this records identifiers associated with this care team that are defined
        # by business processes and/or used to refer to it when a direct url
        # reference to the resource itself is not appropriate.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CareTeam',
             'child_variable': 'subject'},

            {'parent_entity': 'CareTeam_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'participant'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CareTeam',
             'child_variable': 'category'},
        ]


class CareTeam_Participant(fhirbase):
    """The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """

    def __init__(self, dict_values=None):
        # indicates specific responsibility of an individual within the care team,
        # such as "primary care physician", "trained social worker counselor",
        # "caregiver", etc.
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the specific person or organization who is participating/expected to
        # participate in the care team.
        self.member = None
        # reference to Reference: identifier

        # the organization of the practitioner.
        self.onBehalfOf = None
        # reference to Reference: identifier

        # indicates when the specific member or organization did (or is intended
        # to) come into effect and end.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

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
