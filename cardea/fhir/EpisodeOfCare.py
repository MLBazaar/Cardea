from .fhirbase import fhirbase


class EpisodeOfCare(fhirbase):
    """
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.
    """

    __name__ = 'EpisodeOfCare'

    def __init__(self, dict_values=None):
        self.resourceType = 'EpisodeOfCare'
        """
        This is a EpisodeOfCare resource

        type: string
        possible values: EpisodeOfCare
        """

        self.status = None
        """
        planned | waitlist | active | onhold | finished | cancelled.

        type: string
        possible values: planned, waitlist, active, onhold, finished,
        cancelled, entered-in-error
        """

        self.statusHistory = None
        """
        The history of statuses that the EpisodeOfCare has been through
        (without requiring processing the history of the resource).

        type: array
        reference to EpisodeOfCare_StatusHistory
        """

        self.type = None
        """
        A classification of the type of episode of care; e.g. specialist
        referral, disease management, type of funded care.

        type: array
        reference to CodeableConcept
        """

        self.diagnosis = None
        """
        The list of diagnosis relevant to this episode of care.

        type: array
        reference to EpisodeOfCare_Diagnosis
        """

        self.patient = None
        """
        The patient who is the focus of this episode of care.

        reference to Reference: identifier
        """

        self.managingOrganization = None
        """
        The organization that has assumed the specific responsibilities for
        the specified duration.

        reference to Reference: identifier
        """

        self.period = None
        """
        The interval during which the managing organization assumes the
        defined responsibility.

        reference to Period
        """

        self.referralRequest = None
        """
        Referral Request(s) that are fulfilled by this EpisodeOfCare, incoming
        referrals.

        type: array
        reference to Reference: identifier
        """

        self.careManager = None
        """
        The practitioner that is the care manager/care co-ordinator for this
        patient.

        reference to Reference: identifier
        """

        self.team = None
        """
        The list of practitioners that may be facilitating this episode of
        care for specific purposes.

        type: array
        reference to Reference: identifier
        """

        self.account = None
        """
        The set of accounts that may be used for billing for this
        EpisodeOfCare.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        The EpisodeOfCare may be known by different identifiers for different
        contexts of use, such as when an external agency is tracking the
        Episode for funding purposes.

        type: array
        reference to Identifier
        """

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
             'child_variable': 'account'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'referralRequest'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'identifier'},

            {'parent_entity': 'EpisodeOfCare_StatusHistory',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'statusHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'careManager'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'patient'},

            {'parent_entity': 'EpisodeOfCare_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EpisodeOfCare',
             'child_variable': 'team'},

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
    """

    __name__ = 'EpisodeOfCare_StatusHistory'

    def __init__(self, dict_values=None):
        self.status = None
        """
        planned | waitlist | active | onhold | finished | cancelled.

        type: string
        possible values: planned, waitlist, active, onhold, finished,
        cancelled, entered-in-error
        """

        self.period = None
        """
        The period during this EpisodeOfCare that the specific status applied.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during
    this time.
    """

    __name__ = 'EpisodeOfCare_Diagnosis'

    def __init__(self, dict_values=None):
        self.condition = None
        """
        A list of conditions/problems/diagnoses that this episode of care is
        intended to be providing care for.

        reference to Reference: identifier
        """

        self.role = None
        """
        Role that this diagnosis has within the episode of care (e.g.
        admission, billing, discharge …).

        reference to CodeableConcept
        """

        self.rank = None
        """
        Ranking of the diagnosis (for each role type).

        type: int
        """

        self.object_id = None
        # unique identifier for object class

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
