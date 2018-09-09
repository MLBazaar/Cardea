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
    """

    __name__ = 'ClinicalImpression'

    def __init__(self, dict_values=None):
        self.resourceType = 'ClinicalImpression'
        """
        This is a ClinicalImpression resource

        type: string
        possible values: ClinicalImpression
        """

        self.status = None
        """
        Identifies the workflow status of the assessment.

        type: string
        possible values: draft, completed, entered-in-error
        """

        self.code = None
        """
        Categorizes the type of clinical assessment performed.

        reference to CodeableConcept
        """

        self.description = None
        """
        A summary of the context and/or cause of the assessment - why / where
        was it performed, and what patient events/status prompted it.

        type: string
        """

        self.subject = None
        """
        The patient or group of individuals assessed as part of this record.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter or episode of care this impression was created as part
        of.

        reference to Reference: identifier
        """

        self.effectiveDateTime = None
        """
        The point in time or period over which the subject was assessed.

        type: string
        """

        self.effectivePeriod = None
        """
        The point in time or period over which the subject was assessed.

        reference to Period
        """

        self.date = None
        """
        Indicates when the documentation of the assessment was complete.

        type: string
        """

        self.assessor = None
        """
        The clinician performing the assessment.

        reference to Reference: identifier
        """

        self.previous = None
        """
        A reference to the last assesment that was conducted bon this patient.
        Assessments are often/usually ongoing in nature; a care provider
        (practitioner or team) will make new assessments on an ongoing basis
        as new data arises or the patient's conditions changes.

        reference to Reference: identifier
        """

        self.problem = None
        """
        This a list of the relevant problems/conditions for a patient.

        type: array
        reference to Reference: identifier
        """

        self.investigation = None
        """
        One or more sets of investigations (signs, symptions, etc.). The
        actual grouping of investigations vary greatly depending on the type
        and context of the assessment. These investigations may include data
        generated during the assessment process, or data previously generated
        and recorded that is pertinent to the outcomes.

        type: array
        reference to ClinicalImpression_Investigation
        """

        self.protocol = None
        """
        Reference to a specific published clinical protocol that was followed
        during this assessment, and/or that provides evidence in support of
        the diagnosis.

        type: array
        """

        self.summary = None
        """
        A text summary of the investigations and the diagnosis.

        type: string
        """

        self.finding = None
        """
        Specific findings or diagnoses that was considered likely or relevant
        to ongoing treatment.

        type: array
        reference to ClinicalImpression_Finding
        """

        self.prognosisCodeableConcept = None
        """
        Estimate of likely outcome.

        type: array
        reference to CodeableConcept
        """

        self.prognosisReference = None
        """
        RiskAssessment expressing likely outcome.

        type: array
        reference to Reference: identifier
        """

        self.action = None
        """
        Action taken as part of assessment procedure.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Commentary about the impression, typically recorded after the
        impression itself was made, though supplemental notes by the original
        author could also appear.

        type: array
        reference to Annotation
        """

        self.identifier = None
        """
        A unique identifier assigned to the clinical impression that remains
        consistent regardless of what server the impression is stored on.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'completed', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, completed, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'action'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'prognosisCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'previous'},

            {'parent_entity': 'ClinicalImpression_Finding',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'finding'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'identifier'},

            {'parent_entity': 'ClinicalImpression_Investigation',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'investigation'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'prognosisReference'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'problem'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression',
             'child_variable': 'assessor'},
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
    """

    __name__ = 'ClinicalImpression_Investigation'

    def __init__(self, dict_values=None):
        self.code = None
        """
        A name/code for the group ("set") of investigations. Typically, this
        will be something like "signs", "symptoms", "clinical", "diagnostic",
        but the list is not constrained, and others such groups such as
        (exposure|family|travel|nutitirional) history may be used.

        reference to CodeableConcept
        """

        self.item = None
        """
        A record of a specific investigation that was undertaken.

        type: array
        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClinicalImpression_Investigation',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression_Investigation',
             'child_variable': 'item'},
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
    """

    __name__ = 'ClinicalImpression_Finding'

    def __init__(self, dict_values=None):
        self.itemCodeableConcept = None
        """
        Specific text, code or reference for finding or diagnosis, which may
        include ruled-out or resolved conditions.

        reference to CodeableConcept
        """

        self.itemReference = None
        """
        Specific text, code or reference for finding or diagnosis, which may
        include ruled-out or resolved conditions.

        reference to Reference: identifier
        """

        self.basis = None
        """
        Which investigations support finding or diagnosis.

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
             'child_entity': 'ClinicalImpression_Finding',
             'child_variable': 'itemCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClinicalImpression_Finding',
             'child_variable': 'itemReference'},
        ]
