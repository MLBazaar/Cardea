from .fhirbase import fhirbase


class Condition(fhirbase):
    """A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.
    """

    def __init__(self, dict_values=None):
        # this is a condition resource
        self.resourceType = 'Condition'
        # type = string
        # possible values: Condition

        # the clinical status of the condition.
        self.clinicalStatus = None
        # type = string

        # the verification status to support the clinical status of the condition.
        self.verificationStatus = None
        # type = string
        # possible values: provisional, differential, confirmed,
        # refuted, entered-in-error, unknown

        # a category assigned to the condition.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a subjective assessment of the severity of the condition as evaluated by
        # the clinician.
        self.severity = None
        # reference to CodeableConcept: CodeableConcept

        # identification of the condition, problem or diagnosis.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the anatomical location where this condition manifests itself.
        self.bodySite = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates the patient or group who the condition record is associated
        # with.
        self.subject = None
        # reference to Reference: identifier

        # encounter during which the condition was first asserted.
        self.context = None
        # reference to Reference: identifier

        # estimated or actual date or date-time  the condition began, in the
        # opinion of the clinician.
        self.onsetDateTime = None
        # type = string

        # estimated or actual date or date-time  the condition began, in the
        # opinion of the clinician.
        self.onsetAge = None
        # reference to Age: Age

        # estimated or actual date or date-time  the condition began, in the
        # opinion of the clinician.
        self.onsetPeriod = None
        # reference to Period: Period

        # estimated or actual date or date-time  the condition began, in the
        # opinion of the clinician.
        self.onsetRange = None
        # reference to Range: Range

        # estimated or actual date or date-time  the condition began, in the
        # opinion of the clinician.
        self.onsetString = None
        # type = string

        # the date or estimated date that the condition resolved or went into
        # remission. this is called "abatement" because of the many overloaded
        # connotations associated with "remission" or "resolution" - conditions
        # are never really resolved, but they can abate.
        self.abatementDateTime = None
        # type = string

        # the date or estimated date that the condition resolved or went into
        # remission. this is called "abatement" because of the many overloaded
        # connotations associated with "remission" or "resolution" - conditions
        # are never really resolved, but they can abate.
        self.abatementAge = None
        # reference to Age: Age

        # the date or estimated date that the condition resolved or went into
        # remission. this is called "abatement" because of the many overloaded
        # connotations associated with "remission" or "resolution" - conditions
        # are never really resolved, but they can abate.
        self.abatementBoolean = None
        # type = boolean

        # the date or estimated date that the condition resolved or went into
        # remission. this is called "abatement" because of the many overloaded
        # connotations associated with "remission" or "resolution" - conditions
        # are never really resolved, but they can abate.
        self.abatementPeriod = None
        # reference to Period: Period

        # the date or estimated date that the condition resolved or went into
        # remission. this is called "abatement" because of the many overloaded
        # connotations associated with "remission" or "resolution" - conditions
        # are never really resolved, but they can abate.
        self.abatementRange = None
        # reference to Range: Range

        # the date or estimated date that the condition resolved or went into
        # remission. this is called "abatement" because of the many overloaded
        # connotations associated with "remission" or "resolution" - conditions
        # are never really resolved, but they can abate.
        self.abatementString = None
        # type = string

        # the date on which the existance of the condition was first asserted or
        # acknowledged.
        self.assertedDate = None
        # type = string

        # individual who is making the condition statement.
        self.asserter = None
        # reference to Reference: identifier

        # clinical stage or grade of a condition. may include formal severity
        # assessments.
        self.stage = None
        # reference to Condition_Stage: Condition_Stage

        # supporting evidence / manifestations that are the basis on which this
        # condition is suspected or confirmed.
        self.evidence = None
        # type = array
        # reference to Condition_Evidence: Condition_Evidence

        # additional information about the condition. this is a general
        # notes/comments entry  for description of the condition, its diagnosis
        # and prognosis.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # this records identifiers associated with this condition that are defined
        # by business processes and/or used to refer to it when a direct url
        # reference to the resource itself is not appropriate (e.g. in cda
        # documents, or in written / printed documentation).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.verificationStatus is not None:
            for value in self.verificationStatus:
                if value is not None and value.lower() not in [
                    'provisional', 'differential', 'confirmed', 'refuted',
                        'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'provisional, differential, confirmed, refuted,'
                        'entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementAge'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'abatementPeriod'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'severity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'asserter'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'onsetAge'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'category'},

            {'parent_entity': 'Condition_Evidence',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'evidence'},

            {'parent_entity': 'Condition_Stage',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'stage'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition',
             'child_variable': 'bodySite'},
        ]


class Condition_Stage(fhirbase):
    """A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.
    """

    def __init__(self, dict_values=None):
        # a simple summary of the stage such as "stage 3". the determination of
        # the stage is disease-specific.
        self.summary = None
        # reference to CodeableConcept: CodeableConcept

        # reference to a formal record of the evidence on which the staging
        # assessment is based.
        self.assessment = None
        # type = array
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition_Stage',
             'child_variable': 'summary'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition_Stage',
             'child_variable': 'assessment'},
        ]


class Condition_Evidence(fhirbase):
    """A clinical condition, problem, diagnosis, or other event, situation,
    issue, or clinical concept that has risen to a level of concern.
    """

    def __init__(self, dict_values=None):
        # a manifestation or symptom that led to the recording of this condition.
        self.code = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # links to other relevant information, including pathology reports.
        self.detail = None
        # type = array
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Condition_Evidence',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Condition_Evidence',
             'child_variable': 'code'},
        ]
