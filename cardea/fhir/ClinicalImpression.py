from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Annotation import Annotation
from .Reference import Reference
from .Period import Period

class ClinicalImpression(fhirbase):
    """A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments
    are often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """

    def __init__(self, dict_values=None):
        # this is a clinicalimpression resource
        self.resourceType = 'ClinicalImpression'
        # type = string
        # possible values = ClinicalImpression

        # identifies the workflow status of the assessment.
        self.status = None
        # type = string
        # possible values = draft, completed, entered-in-error

        # categorizes the type of clinical assessment performed.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a summary of the context and/or cause of the assessment - why / where
        # was it performed, and what patient events/status prompted it.
        self.description = None
        # type = string

        # the patient or group of individuals assessed as part of this record.
        self.subject = None
        # reference to Reference: identifier

        # the encounter or episode of care this impression was created as part of.
        self.context = None
        # reference to Reference: identifier

        # the point in time or period over which the subject was assessed.
        self.effectiveDateTime = None
        # type = string

        # the point in time or period over which the subject was assessed.
        self.effectivePeriod = None
        # reference to Period: Period

        # indicates when the documentation of the assessment was complete.
        self.date = None
        # type = string

        # the clinician performing the assessment.
        self.assessor = None
        # reference to Reference: identifier

        # a reference to the last assesment that was conducted bon this patient.
        # assessments are often/usually ongoing in nature; a care provider
        # (practitioner or team) will make new assessments on an ongoing basis as
        # new data arises or the patient's conditions changes.
        self.previous = None
        # reference to Reference: identifier

        # this a list of the relevant problems/conditions for a patient.
        self.problem = None
        # type = array
        # reference to Reference: identifier

        # one or more sets of investigations (signs, symptions, etc.). the actual
        # grouping of investigations vary greatly depending on the type and
        # context of the assessment. these investigations may include data
        # generated during the assessment process, or data previously generated
        # and recorded that is pertinent to the outcomes.
        self.investigation = None
        # type = array
        # reference to ClinicalImpression_Investigation: ClinicalImpression_Investigation

        # reference to a specific published clinical protocol that was followed
        # during this assessment, and/or that provides evidence in support of the
        # diagnosis.
        self.protocol = None
        # type = array

        # a text summary of the investigations and the diagnosis.
        self.summary = None
        # type = string

        # specific findings or diagnoses that was considered likely or relevant to
        # ongoing treatment.
        self.finding = None
        # type = array
        # reference to ClinicalImpression_Finding: ClinicalImpression_Finding

        # estimate of likely outcome.
        self.prognosisCodeableConcept = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # riskassessment expressing likely outcome.
        self.prognosisReference = None
        # type = array
        # reference to Reference: identifier

        # action taken as part of assessment procedure.
        self.action = None
        # type = array
        # reference to Reference: identifier

        # commentary about the impression, typically recorded after the impression
        # itself was made, though supplemental notes by the original author could
        # also appear.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # a unique identifier assigned to the clinical impression that remains
        # consistent regardless of what server the impression is stored on.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'completed', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, completed, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ClinicalImpression_Finding',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'finding'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'assessor'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'prognosisCodeableConcept'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'identifier'},

            {'parent_entity': 'ClinicalImpression_Investigation',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'investigation'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'action'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'subject'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'problem'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'previous'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'note'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'prognosisReference'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression',
            'child_variable': 'code'},
        ]

class ClinicalImpression_Investigation(fhirbase):
    """A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments
    are often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """

    def __init__(self, dict_values=None):
        # a name/code for the group ("set") of investigations. typically, this
        # will be something like "signs", "symptoms", "clinical", "diagnostic",
        # but the list is not constrained, and others such groups such as
        # (exposure|family|travel|nutitirional) history may be used.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a record of a specific investigation that was undertaken.
        self.item = None
        # type = array
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression_Investigation',
            'child_variable': 'item'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression_Investigation',
            'child_variable': 'code'},
        ]

class ClinicalImpression_Finding(fhirbase):
    """A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments
    are often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """

    def __init__(self, dict_values=None):
        # specific text, code or reference for finding or diagnosis, which may
        # include ruled-out or resolved conditions.
        self.itemCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # specific text, code or reference for finding or diagnosis, which may
        # include ruled-out or resolved conditions.
        self.itemReference = None
        # reference to Reference: identifier

        # which investigations support finding or diagnosis.
        self.basis = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ClinicalImpression_Finding',
            'child_variable': 'itemCodeableConcept'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ClinicalImpression_Finding',
            'child_variable': 'itemReference'},
        ]

