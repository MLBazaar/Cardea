from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Annotation import Annotation
from .Identifier import Identifier
from .Reference import Reference
from .Period import Period
from .RelatedArtifact import RelatedArtifact
from .ContactDetail import ContactDetail

class ResearchStudy(fhirbase):
    """A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices,
    therapies and other interventional and investigative techniques.  A
    ResearchStudy involves the gathering of information about human or
    animal subjects.
    """

    def __init__(self, dict_values=None):
        # this is a researchstudy resource
        self.resourceType = 'ResearchStudy'
        # type = string
        # possible values = ResearchStudy

        # a short, descriptive user-friendly label for the study.
        self.title = None
        # type = string

        # the set of steps expected to be performed as part of the execution of
        # the study.
        self.protocol = None
        # type = array
        # reference to Reference: identifier

        # a larger research study of which this particular study is a component or
        # step.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # the current state of the study.
        self.status = None
        # type = string
        # possible values = draft, in-progress, suspended, stopped, completed, entered-in-error

        # codes categorizing the type of study such as investigational vs.
        # observational, type of blinding, type of randomization, safety vs.
        # efficacy, etc.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the condition(s), medication(s), food(s), therapy(ies), device(s) or
        # other concerns or interventions that the study is seeking to gain more
        # information about.
        self.focus = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # contact details to assist a user in learning more about or engaging with
        # the study.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # citations, references and other related documents.
        self.relatedArtifact = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # key terms to aid in searching for or filtering the study.
        self.keyword = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates a country, state or other region where the study is taking
        # place.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a full description of how the study is being conducted.
        self.description = None
        # type = string

        # reference to a group that defines the criteria for and quantity of
        # subjects participating in the study.  e.g. " 200 female europeans
        # between the ages of 20 and 45 with early onset diabetes".
        self.enrollment = None
        # type = array
        # reference to Reference: identifier

        # identifies the start date and the expected (or actual, depending on
        # status) end date for the study.
        self.period = None
        # reference to Period: Period

        # the organization responsible for the execution of the study.
        self.sponsor = None
        # reference to Reference: identifier

        # indicates the individual who has primary oversite of the execution of
        # the study.
        self.principalInvestigator = None
        # reference to Reference: identifier

        # clinic, hospital or other healthcare location that is participating in
        # the study.
        self.site = None
        # type = array
        # reference to Reference: identifier

        # a description and/or code explaining the premature termination of the
        # study.
        self.reasonStopped = None
        # reference to CodeableConcept: CodeableConcept

        # comments made about the event by the performer, subject or other
        # participants.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # describes an expected sequence of events for one of the participants of
        # a study.  e.g. exposure to drug a, wash-out, exposure to drug b, wash-
        # out, follow-up.
        self.arm = None
        # type = array
        # reference to ResearchStudy_Arm: ResearchStudy_Arm

        # identifiers assigned to this research study by the sponsor or other
        # systems.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'in-progress', 'suspended', 'stopped', 'completed', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, in-progress, suspended, stopped, completed, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'jurisdiction'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'reasonStopped'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ResearchStudy',
            'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'focus'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'keyword'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'note'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ResearchStudy',
            'child_variable': 'principalInvestigator'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ResearchStudy',
            'child_variable': 'site'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ResearchStudy',
            'child_variable': 'enrollment'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ResearchStudy',
            'child_variable': 'sponsor'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ResearchStudy',
            'child_variable': 'protocol'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'category'},

            {'parent_entity': 'ResearchStudy_Arm',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'arm'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'contact'},

            {'parent_entity': 'RelatedArtifact',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy',
            'child_variable': 'relatedArtifact'},
        ]

class ResearchStudy_Arm(fhirbase):
    """A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices,
    therapies and other interventional and investigative techniques.  A
    ResearchStudy involves the gathering of information about human or
    animal subjects.
    """

    def __init__(self, dict_values=None):
        # unique, human-readable label for this arm of the study.
        self.name = None
        # type = string

        # categorization of study arm, e.g. experimental, active comparator,
        # placebo comparater.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a succinct description of the path through the study that would be
        # followed by a subject adhering to this arm.
        self.description = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ResearchStudy_Arm',
            'child_variable': 'code'},
        ]

