from .fhirbase import fhirbase


class Condition(fhirbase):
    """
    A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.

    Args:
        resourceType: This is a Condition resource
        identifier: This records identifiers associated with this condition
            that are defined by business processes and/or used to refer to it when
            a direct URL reference to the resource itself is not appropriate (e.g.
            in CDA documents, or in written / printed documentation).
        clinicalStatus: The clinical status of the condition.
        verificationStatus: The verification status to support the clinical
            status of the condition.
        category: A category assigned to the condition.
        severity: A subjective assessment of the severity of the condition as
            evaluated by the clinician.
        code: Identification of the condition, problem or diagnosis.
        bodySite: The anatomical location where this condition manifests
            itself.
        subject: Indicates the patient or group who the condition record is
            associated with.
        context: Encounter during which the condition was first asserted.
        onsetDateTime: Estimated or actual date or date-time  the condition
            began, in the opinion of the clinician.
        onsetAge: Estimated or actual date or date-time  the condition began,
            in the opinion of the clinician.
        onsetPeriod: Estimated or actual date or date-time  the condition
            began, in the opinion of the clinician.
        onsetRange: Estimated or actual date or date-time  the condition
            began, in the opinion of the clinician.
        onsetString: Estimated or actual date or date-time  the condition
            began, in the opinion of the clinician.
        abatementDateTime: The date or estimated date that the condition
            resolved or went into remission. This is called "abatement" because of
            the many overloaded connotations associated with "remission" or
            "resolution" - Conditions are never really resolved, but they can
            abate.
        abatementAge: The date or estimated date that the condition resolved
            or went into remission. This is called "abatement" because of the many
            overloaded connotations associated with "remission" or "resolution" -
            Conditions are never really resolved, but they can abate.
        abatementBoolean: The date or estimated date that the condition
            resolved or went into remission. This is called "abatement" because of
            the many overloaded connotations associated with "remission" or
            "resolution" - Conditions are never really resolved, but they can
            abate.
        abatementPeriod: The date or estimated date that the condition
            resolved or went into remission. This is called "abatement" because of
            the many overloaded connotations associated with "remission" or
            "resolution" - Conditions are never really resolved, but they can
            abate.
        abatementRange: The date or estimated date that the condition resolved
            or went into remission. This is called "abatement" because of the many
            overloaded connotations associated with "remission" or "resolution" -
            Conditions are never really resolved, but they can abate.
        abatementString: The date or estimated date that the condition
            resolved or went into remission. This is called "abatement" because of
            the many overloaded connotations associated with "remission" or
            "resolution" - Conditions are never really resolved, but they can
            abate.
        assertedDate: The date on which the existance of the Condition was
            first asserted or acknowledged.
        asserter: Individual who is making the condition statement.
        stage: Clinical stage or grade of a condition. May include formal
            severity assessments.
        evidence: Supporting Evidence / manifestations that are the basis on
            which this condition is suspected or confirmed.
        note: Additional information about the Condition. This is a general
            notes/comments entry  for description of the Condition, its diagnosis
            and prognosis.
    """

    __name__ = 'Condition'

    def __init__(self, dict_values=None):
        self.resourceType = 'Condition'
        # type: str
        # possible values: Condition

        self.clinicalStatus = None
        # type: str

        self.verificationStatus = None
        # type: str
        # possible values: provisional, differential, confirmed,
        # refuted, entered-in-error, unknown

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.severity = None
        # reference to CodeableConcept

        self.code = None
        # reference to CodeableConcept

        self.bodySite = None
        # type: list
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.onsetDateTime = None
        # type: str

        self.onsetAge = None
        # reference to Age

        self.onsetPeriod = None
        # reference to Period

        self.onsetRange = None
        # reference to Range

        self.onsetString = None
        # type: str

        self.abatementDateTime = None
        # type: str

        self.abatementAge = None
        # reference to Age

        self.abatementBoolean = None
        # type: bool

        self.abatementPeriod = None
        # reference to Period

        self.abatementRange = None
        # reference to Range

        self.abatementString = None
        # type: str

        self.assertedDate = None
        # type: str

        self.asserter = None
        # reference to Reference: identifier

        self.stage = None
        # reference to Condition_Stage

        self.evidence = None
        # type: list
        # reference to Condition_Evidence

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

        if self.verificationStatus is not None:
            for value in self.verificationStatus:
                if value is not None and value.lower() not in [
                    'provisional', 'differential', 'confirmed', 'refuted',
                        'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'provisional, differential, confirmed, refuted, entered-in-error,'
                        'unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'subject'},

            {'parent_entity': 'Condition_Evidence',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'evidence'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'code'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'asserter'},

            {'parent_entity': 'Condition_Stage',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'stage'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetAge'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementPeriod'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementRange'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'note'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementAge'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'severity'},
        ]


class Condition_Stage(fhirbase):
    """
    A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.

    Args:
        summary: A simple summary of the stage such as "Stage 3". The
            determination of the stage is disease-specific.
        assessment: Reference to a formal record of the evidence on which the
            staging assessment is based.
    """

    __name__ = 'Condition_Stage'

    def __init__(self, dict_values=None):
        self.summary = None
        # reference to CodeableConcept

        self.assessment = None
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
             'child_entity': 'Condition_Stage',
             'child_variable': 'assessment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition_Stage',
             'child_variable': 'summary'},
        ]


class Condition_Evidence(fhirbase):
    """
    A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.

    Args:
        code: A manifestation or symptom that led to the recording of this
            condition.
        detail: Links to other relevant information, including pathology
            reports.
    """

    __name__ = 'Condition_Evidence'

    def __init__(self, dict_values=None):
        self.code = None
        # type: list
        # reference to CodeableConcept

        self.detail = None
        # type: list
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition_Evidence',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition_Evidence',
             'child_variable': 'detail'},
        ]
