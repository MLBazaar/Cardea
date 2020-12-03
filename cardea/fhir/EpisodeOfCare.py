from .fhirbase import fhirbase


class EpisodeOfCare(fhirbase):
    """
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.

    Args:
        resourceType: This is a EpisodeOfCare resource
        identifier: The EpisodeOfCare may be known by different identifiers
            for different contexts of use, such as when an external agency is
            tracking the Episode for funding purposes.
        status: planned | waitlist | active | onhold | finished | cancelled.
        statusHistory: The history of statuses that the EpisodeOfCare has been
            through (without requiring processing the history of the resource).
        type: A classification of the type of episode of care; e.g. specialist
            referral, disease management, type of funded care.
        diagnosis: The list of diagnosis relevant to this episode of care.
        patient: The patient who is the focus of this episode of care.
        managingOrganization: The organization that has assumed the specific
            responsibilities for the specified duration.
        period: The interval during which the managing organization assumes
            the defined responsibility.
        referralRequest: Referral Request(s) that are fulfilled by this
            EpisodeOfCare, incoming referrals.
        careManager: The practitioner that is the care manager/care
            co-ordinator for this patient.
        team: The list of practitioners that may be facilitating this episode
            of care for specific purposes.
        account: The set of accounts that may be used for billing for this
            EpisodeOfCare.
    """

    __name__ = 'EpisodeOfCare'

    def __init__(self, dict_values=None):
        self.resourceType = 'EpisodeOfCare'
        # type: str
        # possible values: EpisodeOfCare

        self.status = None
        # type: str
        # possible values: planned, waitlist, active, onhold,
        # finished, cancelled, entered-in-error

        self.statusHistory = None
        # type: list
        # reference to EpisodeOfCare_StatusHistory

        self.type = None
        # type: list
        # reference to CodeableConcept

        self.diagnosis = None
        # type: list
        # reference to EpisodeOfCare_Diagnosis

        self.patient = None
        # reference to Reference: identifier

        self.managingOrganization = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.referralRequest = None
        # type: list
        # reference to Reference: identifier

        self.careManager = None
        # reference to Reference: identifier

        self.team = None
        # type: list
        # reference to Reference: identifier

        self.account = None
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
                    'planned', 'waitlist', 'active', 'onhold', 'finished', 'cancelled',
                        'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, waitlist, active, onhold, finished, cancelled,'
                        'entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'EpisodeOfCare_StatusHistory',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'statusHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'account'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'team'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'referralRequest'},

            {'parent_entity': 'EpisodeOfCare_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'careManager'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'type'},
        ]


class EpisodeOfCare_StatusHistory(fhirbase):
    """
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.

    Args:
        status: planned | waitlist | active | onhold | finished | cancelled.
        period: The period during this EpisodeOfCare that the specific status
            applied.
    """

    __name__ = 'EpisodeOfCare_StatusHistory'

    def __init__(self, dict_values=None):
        self.status = None
        # type: str
        # possible values: planned, waitlist, active, onhold,
        # finished, cancelled, entered-in-error

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'planned', 'waitlist', 'active', 'onhold', 'finished', 'cancelled',
                        'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, waitlist, active, onhold, finished, cancelled,'
                        'entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare_StatusHistory',
             'child_variable': 'period'},
        ]


class EpisodeOfCare_Diagnosis(fhirbase):
    """
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.

    Args:
        condition: A list of conditions/problems/diagnoses that this episode
            of care is intended to be providing care for.
        role: Role that this diagnosis has within the episode of care (e.g.
            admission, billing, discharge …).
        rank: Ranking of the diagnosis (for each role type).
    """

    __name__ = 'EpisodeOfCare_Diagnosis'

    def __init__(self, dict_values=None):
        self.condition = None
        # reference to Reference: identifier

        self.role = None
        # reference to CodeableConcept

        self.rank = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare_Diagnosis',
             'child_variable': 'condition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare_Diagnosis',
             'child_variable': 'role'},
        ]
