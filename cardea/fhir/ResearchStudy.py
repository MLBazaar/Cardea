from .fhirbase import fhirbase


class ResearchStudy(fhirbase):
    """
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices,
    therapies and other interventional and investigative techniques.  A
    ResearchStudy involves the gathering of information about human or
    animal subjects.

    Args:
        resourceType: This is a ResearchStudy resource
        identifier: Identifiers assigned to this research study by the sponsor
            or other systems.
        title: A short, descriptive user-friendly label for the study.
        protocol: The set of steps expected to be performed as part of the
            execution of the study.
        partOf: A larger research study of which this particular study is a
            component or step.
        status: The current state of the study.
        category: Codes categorizing the type of study such as investigational
            vs. observational, type of blinding, type of randomization, safety vs.
            efficacy, etc.
        focus: The condition(s), medication(s), food(s), therapy(ies),
            device(s) or other concerns or interventions that the study is seeking
            to gain more information about.
        contact: Contact details to assist a user in learning more about or
            engaging with the study.
        relatedArtifact: Citations, references and other related documents.
        keyword: Key terms to aid in searching for or filtering the study.
        jurisdiction: Indicates a country, state or other region where the
            study is taking place.
        description: A full description of how the study is being conducted.
        enrollment: Reference to a Group that defines the criteria for and
            quantity of subjects participating in the study.  E.g. " 200 female
            Europeans between the ages of 20 and 45 with early onset diabetes".
        period: Identifies the start date and the expected (or actual,
            depending on status) end date for the study.
        sponsor: The organization responsible for the execution of the study.
        principalInvestigator: Indicates the individual who has primary
            oversite of the execution of the study.
        site: Clinic, hospital or other healthcare location that is
            participating in the study.
        reasonStopped: A description and/or code explaining the premature
            termination of the study.
        note: Comments made about the event by the performer, subject or other
            participants.
        arm: Describes an expected sequence of events for one of the
            participants of a study.  E.g. Exposure to drug A, wash-out, exposure
            to drug B, wash-out, follow-up.
    """

    __name__ = 'ResearchStudy'

    def __init__(self, dict_values=None):
        self.resourceType = 'ResearchStudy'
        # type: str
        # possible values: ResearchStudy

        self.title = None
        # type: str

        self.protocol = None
        # type: list
        # reference to Reference: identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: draft, in-progress, suspended, stopped,
        # completed, entered-in-error

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.focus = None
        # type: list
        # reference to CodeableConcept

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.relatedArtifact = None
        # type: list
        # reference to RelatedArtifact

        self.keyword = None
        # type: list
        # reference to CodeableConcept

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.enrollment = None
        # type: list
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.sponsor = None
        # reference to Reference: identifier

        self.principalInvestigator = None
        # reference to Reference: identifier

        self.site = None
        # type: list
        # reference to Reference: identifier

        self.reasonStopped = None
        # reference to CodeableConcept

        self.note = None
        # type: list
        # reference to Annotation

        self.arm = None
        # type: list
        # reference to ResearchStudy_Arm

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
                    'draft', 'in-progress', 'suspended', 'stopped', 'completed',
                        'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, in-progress, suspended, stopped, completed, '
                        'entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'reasonStopped'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'sponsor'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'partOf'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'contact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'site'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'focus'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'protocol'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'period'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'principalInvestigator'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'keyword'},

            {'parent_entity': 'ResearchStudy_Arm',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'arm'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'enrollment'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'note'},
        ]


class ResearchStudy_Arm(fhirbase):
    """
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices,
    therapies and other interventional and investigative techniques.  A
    ResearchStudy involves the gathering of information about human or
    animal subjects.

    Args:
        name: Unique, human-readable label for this arm of the study.
        code: Categorization of study arm, e.g. experimental, active
            comparator, placebo comparater.
        description: A succinct description of the path through the study that
            would be followed by a subject adhering to this arm.
    """

    __name__ = 'ResearchStudy_Arm'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.code = None
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy_Arm',
             'child_variable': 'code'},
        ]
