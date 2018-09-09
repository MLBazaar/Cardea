from .fhirbase import fhirbase


class EpisodeOfCare(fhirbase):
    """An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.
    """

    __name__ = 'EpisodeOfCare'

    def __init__(self, dict_values=None):
        # this is a episodeofcare resource
        self.resourceType = 'EpisodeOfCare'
        # type = string
        # possible values: EpisodeOfCare

        # planned | waitlist | active | onhold | finished | cancelled.
        self.status = None
        # type = string
        # possible values: planned, waitlist, active, onhold, finished,
        # cancelled, entered-in-error

        # the history of statuses that the episodeofcare has been through (without
        # requiring processing the history of the resource).
        self.statusHistory = None
        # type = array
        # reference to EpisodeOfCare_StatusHistory: EpisodeOfCare_StatusHistory

        # a classification of the type of episode of care; e.g. specialist
        # referral, disease management, type of funded care.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the list of diagnosis relevant to this episode of care.
        self.diagnosis = None
        # type = array
        # reference to EpisodeOfCare_Diagnosis: EpisodeOfCare_Diagnosis

        # the patient who is the focus of this episode of care.
        self.patient = None
        # reference to Reference: identifier

        # the organization that has assumed the specific responsibilities for the
        # specified duration.
        self.managingOrganization = None
        # reference to Reference: identifier

        # the interval during which the managing organization assumes the defined
        # responsibility.
        self.period = None
        # reference to Period: Period

        # referral request(s) that are fulfilled by this episodeofcare, incoming
        # referrals.
        self.referralRequest = None
        # type = array
        # reference to Reference: identifier

        # the practitioner that is the care manager/care co-ordinator for this
        # patient.
        self.careManager = None
        # reference to Reference: identifier

        # the list of practitioners that may be facilitating this episode of care
        # for specific purposes.
        self.team = None
        # type = array
        # reference to Reference: identifier

        # the set of accounts that may be used for billing for this episodeofcare.
        self.account = None
        # type = array
        # reference to Reference: identifier

        # the episodeofcare may be known by different identifiers for different
        # contexts of use, such as when an external agency is tracking the episode
        # for funding purposes.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'referralRequest'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'period'},

            {'parent_entity': 'EpisodeOfCare_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'careManager'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'account'},

            {'parent_entity': 'EpisodeOfCare_StatusHistory',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'statusHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'team'},

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
             'child_variable': 'managingOrganization'},
        ]


class EpisodeOfCare_StatusHistory(fhirbase):
    """An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.
    """

    __name__ = 'EpisodeOfCare_StatusHistory'

    def __init__(self, dict_values=None):
        # planned | waitlist | active | onhold | finished | cancelled.
        self.status = None
        # type = string
        # possible values: planned, waitlist, active, onhold, finished,
        # cancelled, entered-in-error

        # the period during this episodeofcare that the specific status applied.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

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
    """An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.
    """

    __name__ = 'EpisodeOfCare_Diagnosis'

    def __init__(self, dict_values=None):
        # a list of conditions/problems/diagnoses that this episode of care is
        # intended to be providing care for.
        self.condition = None
        # reference to Reference: identifier

        # role that this diagnosis has within the episode of care (e.g. admission,
        # billing, discharge …).
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # ranking of the diagnosis (for each role type).
        self.rank = None
        # type = int

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare_Diagnosis',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare_Diagnosis',
             'child_variable': 'condition'},
        ]
