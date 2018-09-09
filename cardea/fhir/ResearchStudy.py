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
    """

    __name__ = 'ResearchStudy'

    def __init__(self, dict_values=None):
        self.resourceType = 'ResearchStudy'
        """
        This is a ResearchStudy resource

        type: string
        possible values: ResearchStudy
        """

        self.title = None
        """
        A short, descriptive user-friendly label for the study.

        type: string
        """

        self.protocol = None
        """
        The set of steps expected to be performed as part of the execution of
        the study.

        type: array
        reference to Reference: identifier
        """

        self.partOf = None
        """
        A larger research study of which this particular study is a component
        or step.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        The current state of the study.

        type: string
        possible values: draft, in-progress, suspended, stopped,
        completed, entered-in-error
        """

        self.category = None
        """
        Codes categorizing the type of study such as investigational vs.
        observational, type of blinding, type of randomization, safety vs.
        efficacy, etc.

        type: array
        reference to CodeableConcept
        """

        self.focus = None
        """
        The condition(s), medication(s), food(s), therapy(ies), device(s) or
        other concerns or interventions that the study is seeking to gain more
        information about.

        type: array
        reference to CodeableConcept
        """

        self.contact = None
        """
        Contact details to assist a user in learning more about or engaging
        with the study.

        type: array
        reference to ContactDetail
        """

        self.relatedArtifact = None
        """
        Citations, references and other related documents.

        type: array
        reference to RelatedArtifact
        """

        self.keyword = None
        """
        Key terms to aid in searching for or filtering the study.

        type: array
        reference to CodeableConcept
        """

        self.jurisdiction = None
        """
        Indicates a country, state or other region where the study is taking
        place.

        type: array
        reference to CodeableConcept
        """

        self.description = None
        """
        A full description of how the study is being conducted.

        type: string
        """

        self.enrollment = None
        """
        Reference to a Group that defines the criteria for and quantity of
        subjects participating in the study.  E.g. " 200 female Europeans
        between the ages of 20 and 45 with early onset diabetes".

        type: array
        reference to Reference: identifier
        """

        self.period = None
        """
        Identifies the start date and the expected (or actual, depending on
        status) end date for the study.

        reference to Period
        """

        self.sponsor = None
        """
        The organization responsible for the execution of the study.

        reference to Reference: identifier
        """

        self.principalInvestigator = None
        """
        Indicates the individual who has primary oversite of the execution of
        the study.

        reference to Reference: identifier
        """

        self.site = None
        """
        Clinic, hospital or other healthcare location that is participating in
        the study.

        type: array
        reference to Reference: identifier
        """

        self.reasonStopped = None
        """
        A description and/or code explaining the premature termination of the
        study.

        reference to CodeableConcept
        """

        self.note = None
        """
        Comments made about the event by the performer, subject or other
        participants.

        type: array
        reference to Annotation
        """

        self.arm = None
        """
        Describes an expected sequence of events for one of the participants
        of a study.  E.g. Exposure to drug A, wash-out, exposure to drug B,
        wash-out, follow-up.

        type: array
        reference to ResearchStudy_Arm
        """

        self.identifier = None
        """
        Identifiers assigned to this research study by the sponsor or other
        systems.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'category'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'sponsor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'protocol'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'contact'},

            {'parent_entity': 'ResearchStudy_Arm',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'arm'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'enrollment'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'reasonStopped'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'focus'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'keyword'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'principalInvestigator'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchStudy',
             'child_variable': 'site'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchStudy',
             'child_variable': 'identifier'},
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
    """

    __name__ = 'ResearchStudy_Arm'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Unique, human-readable label for this arm of the study.

        type: string
        """

        self.code = None
        """
        Categorization of study arm, e.g. experimental, active comparator,
        placebo comparater.

        reference to CodeableConcept
        """

        self.description = None
        """
        A succinct description of the path through the study that would be
        followed by a subject adhering to this arm.

        type: string
        """

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
