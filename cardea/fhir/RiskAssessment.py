from .fhirbase import fhirbase


class RiskAssessment(fhirbase):
    """An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    __name__ = 'RiskAssessment'

    def __init__(self, dict_values=None):
        # this is a riskassessment resource
        self.resourceType = 'RiskAssessment'
        # type = string
        # possible values: RiskAssessment

        # a reference to the request that is fulfilled by this risk assessment.
        self.basedOn = None
        # reference to Reference: identifier

        # a reference to a resource that this risk assessment is part of, such as
        # a procedure.
        self.parent = None
        # reference to Reference: identifier

        # the status of the riskassessment, using the same statuses as an
        # observation.
        self.status = None
        # type = string

        # the algorithm, process or mechanism used to evaluate the risk.
        self.method = None
        # reference to CodeableConcept: CodeableConcept

        # the type of the risk assessment performed.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the patient or group the risk assessment applies to.
        self.subject = None
        # reference to Reference: identifier

        # the encounter where the assessment was performed.
        self.context = None
        # reference to Reference: identifier

        # the date (and possibly time) the risk assessment was performed.
        self.occurrenceDateTime = None
        # type = string

        # the date (and possibly time) the risk assessment was performed.
        self.occurrencePeriod = None
        # reference to Period: Period

        # for assessments or prognosis specific to a particular condition,
        # indicates the condition being assessed.
        self.condition = None
        # reference to Reference: identifier

        # the provider or software application that performed the assessment.
        self.performer = None
        # reference to Reference: identifier

        # the reason the risk assessment was performed.
        self.reasonCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the reason the risk assessment was performed.
        self.reasonReference = None
        # reference to Reference: identifier

        # indicates the source data considered as part of the assessment
        # (familyhistory, observations, procedures, conditions, etc.).
        self.basis = None
        # type = array
        # reference to Reference: identifier

        # describes the expected outcome for the subject.
        self.prediction = None
        # type = array
        # reference to RiskAssessment_Prediction: RiskAssessment_Prediction

        # a description of the steps that might be taken to reduce the identified
        # risk(s).
        self.mitigation = None
        # type = string

        # additional comments about the risk assessment.
        self.comment = None
        # type = string

        # business identifier assigned to the risk assessment.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'condition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'RiskAssessment_Prediction',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'prediction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'basis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'parent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'method'},
        ]


class RiskAssessment_Prediction(fhirbase):
    """An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    __name__ = 'RiskAssessment_Prediction'

    def __init__(self, dict_values=None):
        # one of the potential outcomes for the patient (e.g. remission, death,  a
        # particular condition).
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # how likely is the outcome (in the specified timeframe).
        self.probabilityDecimal = None
        # type = int

        # how likely is the outcome (in the specified timeframe).
        self.probabilityRange = None
        # reference to Range: Range

        # how likely is the outcome (in the specified timeframe), expressed as a
        # qualitative value (e.g. low, medium, high).
        self.qualitativeRisk = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the risk for this particular subject (with their specific
        # characteristics) divided by the risk of the population in general.
        # (numbers greater than 1 = higher risk than the population, numbers less
        # than 1 = lower risk.).
        self.relativeRisk = None
        # type = int

        # indicates the period of time or age range of the subject to which the
        # specified probability applies.
        self.whenPeriod = None
        # reference to Period: Period

        # indicates the period of time or age range of the subject to which the
        # specified probability applies.
        self.whenRange = None
        # reference to Range: Range

        # additional information explaining the basis for the prediction.
        self.rationale = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'outcome'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'whenPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'qualitativeRisk'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'probabilityRange'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'whenRange'},
        ]
