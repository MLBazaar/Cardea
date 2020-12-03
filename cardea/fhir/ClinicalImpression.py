from .fhirbase import fhirbase


class ClinicalImpression(fhirbase):
    """
    A record of a clinical assessment performed to determine what
    problem(s) may affect the patient and before planning the treatments
    or management strategies that are best to manage a patient's
    condition. Assessments are often 1:1 with a clinical consultation /
    encounter,  but this varies greatly depending on the clinical
    workflow. This resource is called "ClinicalImpression" rather than
    "ClinicalAssessment" to avoid confusion with the recording of
    assessment tools such as Apgar score.

    Args:
        resourceType: This is a ClinicalImpression resource
        identifier: A unique identifier assigned to the clinical impression
            that remains consistent regardless of what server the impression is
            stored on.
        status: Identifies the workflow status of the assessment.
        code: Categorizes the type of clinical assessment performed.
        description: A summary of the context and/or cause of the assessment -
            why / where was it performed, and what patient events/status prompted
            it.
        subject: The patient or group of individuals assessed as part of this
            record.
        context: The encounter or episode of care this impression was created
            as part of.
        effectiveDateTime: The point in time or period over which the subject
            was assessed.
        effectivePeriod: The point in time or period over which the subject
            was assessed.
        date: Indicates when the documentation of the assessment was complete.
        assessor: The clinician performing the assessment.
        previous: A reference to the last assesment that was conducted bon
            this patient. Assessments are often/usually ongoing in nature; a care
            provider (practitioner or team) will make new assessments on an
            ongoing basis as new data arises or the patient's conditions changes.
        problem: This a list of the relevant problems/conditions for a
            patient.
        investigation: One or more sets of investigations (signs, symptions,
            etc.). The actual grouping of investigations vary greatly depending on
            the type and context of the assessment. These investigations may
            include data generated during the assessment process, or data
            previously generated and recorded that is pertinent to the outcomes.
        protocol: Reference to a specific published clinical protocol that was
            followed during this assessment, and/or that provides evidence in
            support of the diagnosis.
        summary: A text summary of the investigations and the diagnosis.
        finding: Specific findings or diagnoses that was considered likely or
            relevant to ongoing treatment.
        prognosisCodeableConcept: Estimate of likely outcome.
        prognosisReference: RiskAssessment expressing likely outcome.
        action: Action taken as part of assessment procedure.
        note: Commentary about the impression, typically recorded after the
            impression itself was made, though supplemental notes by the original
            author could also appear.
    """

    __name__ = 'ClinicalImpression'

    def __init__(self, dict_values=None):
        self.resourceType = 'ClinicalImpression'
        # type: str
        # possible values: ClinicalImpression

        self.status = None
        # type: str
        # possible values: draft, completed, entered-in-error

        self.code = None
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.effectiveDateTime = None
        # type: str

        self.effectivePeriod = None
        # reference to Period

        self.date = None
        # type: str

        self.assessor = None
        # reference to Reference: identifier

        self.previous = None
        # reference to Reference: identifier

        self.problem = None
        # type: list
        # reference to Reference: identifier

        self.investigation = None
        # type: list
        # reference to ClinicalImpression_Investigation

        self.protocol = None
        # type: list

        self.summary = None
        # type: str

        self.finding = None
        # type: list
        # reference to ClinicalImpression_Finding

        self.prognosisCodeableConcept = None
        # type: list
        # reference to CodeableConcept

        self.prognosisReference = None
        # type: list
        # reference to Reference: identifier

        self.action = None
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
                        'draft', 'completed', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, completed, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'ClinicalImpression_Finding',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'finding'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'assessor'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'identifier'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'action'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'prognosisReference'},

            {'parent_entity': 'ClinicalImpression_Investigation',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'investigation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'prognosisCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'problem'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'previous'},
        ]


class ClinicalImpression_Investigation(fhirbase):
    """
    A record of a clinical assessment performed to determine what
    problem(s) may affect the patient and before planning the treatments
    or management strategies that are best to manage a patient's
    condition. Assessments are often 1:1 with a clinical consultation /
    encounter,  but this varies greatly depending on the clinical
    workflow. This resource is called "ClinicalImpression" rather than
    "ClinicalAssessment" to avoid confusion with the recording of
    assessment tools such as Apgar score.

    Args:
        code: A name/code for the group ("set") of investigations. Typically,
            this will be something like "signs", "symptoms", "clinical",
            "diagnostic", but the list is not constrained, and others such groups
            such as (exposure|family|travel|nutitirional) history may be used.
        item: A record of a specific investigation that was undertaken.
    """

    __name__ = 'ClinicalImpression_Investigation'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.item = None
        # type: list
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
    """
    A record of a clinical assessment performed to determine what
    problem(s) may affect the patient and before planning the treatments
    or management strategies that are best to manage a patient's
    condition. Assessments are often 1:1 with a clinical consultation /
    encounter,  but this varies greatly depending on the clinical
    workflow. This resource is called "ClinicalImpression" rather than
    "ClinicalAssessment" to avoid confusion with the recording of
    assessment tools such as Apgar score.

    Args:
        itemCodeableConcept: Specific text, code or reference for finding or
            diagnosis, which may include ruled-out or resolved conditions.
        itemReference: Specific text, code or reference for finding or
            diagnosis, which may include ruled-out or resolved conditions.
        basis: Which investigations support finding or diagnosis.
    """

    __name__ = 'ClinicalImpression_Finding'

    def __init__(self, dict_values=None):
        self.itemCodeableConcept = None
        # reference to CodeableConcept

        self.itemReference = None
        # reference to Reference: identifier

        self.basis = None
        # type: str

        self.object_id = None
        # unique identifier for object class

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
