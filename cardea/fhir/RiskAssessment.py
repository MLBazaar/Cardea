from .fhirbase import fhirbase


class RiskAssessment(fhirbase):
    """
    An assessment of the likely outcome(s) for a patient or other subject
    as well as the likelihood of each outcome.

    Args:
        resourceType: This is a RiskAssessment resource
        identifier: Business identifier assigned to the risk assessment.
        basedOn: A reference to the request that is fulfilled by this risk
            assessment.
        parent: A reference to a resource that this risk assessment is part
            of, such as a Procedure.
        status: The status of the RiskAssessment, using the same statuses as
            an Observation.
        method: The algorithm, process or mechanism used to evaluate the risk.
        code: The type of the risk assessment performed.
        subject: The patient or group the risk assessment applies to.
        context: The encounter where the assessment was performed.
        occurrenceDateTime: The date (and possibly time) the risk assessment
            was performed.
        occurrencePeriod: The date (and possibly time) the risk assessment was
            performed.
        condition: For assessments or prognosis specific to a particular
            condition, indicates the condition being assessed.
        performer: The provider or software application that performed the
            assessment.
        reasonCodeableConcept: The reason the risk assessment was performed.
        reasonReference: The reason the risk assessment was performed.
        basis: Indicates the source data considered as part of the assessment
            (FamilyHistory, Observations, Procedures, Conditions, etc.).
        prediction: Describes the expected outcome for the subject.
        mitigation: A description of the steps that might be taken to reduce
            the identified risk(s).
        comment: Additional comments about the risk assessment.
    """

    __name__ = 'RiskAssessment'

    def __init__(self, dict_values=None):
        self.resourceType = 'RiskAssessment'
        # type: str
        # possible values: RiskAssessment

        self.basedOn = None
        # reference to Reference: identifier

        self.parent = None
        # reference to Reference: identifier

        self.status = None
        # type: str

        self.method = None
        # reference to CodeableConcept

        self.code = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.condition = None
        # reference to Reference: identifier

        self.performer = None
        # reference to Reference: identifier

        self.reasonCodeableConcept = None
        # reference to CodeableConcept

        self.reasonReference = None
        # reference to Reference: identifier

        self.basis = None
        # type: list
        # reference to Reference: identifier

        self.prediction = None
        # type: list
        # reference to RiskAssessment_Prediction

        self.mitigation = None
        # type: str

        self.comment = None
        # type: str

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'code'},

            {'parent_entity': 'RiskAssessment_Prediction',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'prediction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'condition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'parent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'subject'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'method'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'basis'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'identifier'},
        ]


class RiskAssessment_Prediction(fhirbase):
    """
    An assessment of the likely outcome(s) for a patient or other subject
    as well as the likelihood of each outcome.

    Args:
        outcome: One of the potential outcomes for the patient (e.g.
            remission, death,  a particular condition).
        probabilityDecimal: How likely is the outcome (in the specified
            timeframe).
        probabilityRange: How likely is the outcome (in the specified
            timeframe).
        qualitativeRisk: How likely is the outcome (in the specified
            timeframe), expressed as a qualitative value (e.g. low, medium, high).
        relativeRisk: Indicates the risk for this particular subject (with
            their specific characteristics) divided by the risk of the population
            in general.  (Numbers greater than 1 = higher risk than the
            population, numbers less than 1 = lower risk.).
        whenPeriod: Indicates the period of time or age range of the subject
            to which the specified probability applies.
        whenRange: Indicates the period of time or age range of the subject to
            which the specified probability applies.
        rationale: Additional information explaining the basis for the
            prediction.
    """

    __name__ = 'RiskAssessment_Prediction'

    def __init__(self, dict_values=None):
        self.outcome = None
        # reference to CodeableConcept

        self.probabilityDecimal = None
        # type: int

        self.probabilityRange = None
        # reference to Range

        self.qualitativeRisk = None
        # reference to CodeableConcept

        self.relativeRisk = None
        # type: int

        self.whenPeriod = None
        # reference to Period

        self.whenRange = None
        # reference to Range

        self.rationale = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
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
             'child_variable': 'whenRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'outcome'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'probabilityRange'},
        ]
