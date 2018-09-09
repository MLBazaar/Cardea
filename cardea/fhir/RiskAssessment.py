from .fhirbase import fhirbase


class RiskAssessment(fhirbase):
    """
    An assessment of the likely outcome(s) for a patient or other subject
    as well as the likelihood of each outcome.
    """

    __name__ = 'RiskAssessment'

    def __init__(self, dict_values=None):
        self.resourceType = 'RiskAssessment'
        """
        This is a RiskAssessment resource

        type: string
        possible values: RiskAssessment
        """

        self.basedOn = None
        """
        A reference to the request that is fulfilled by this risk assessment.

        reference to Reference: identifier
        """

        self.parent = None
        """
        A reference to a resource that this risk assessment is part of, such
        as a Procedure.

        reference to Reference: identifier
        """

        self.status = None
        """
        The status of the RiskAssessment, using the same statuses as an
        Observation.

        type: string
        """

        self.method = None
        """
        The algorithm, process or mechanism used to evaluate the risk.

        reference to CodeableConcept
        """

        self.code = None
        """
        The type of the risk assessment performed.

        reference to CodeableConcept
        """

        self.subject = None
        """
        The patient or group the risk assessment applies to.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter where the assessment was performed.

        reference to Reference: identifier
        """

        self.occurrenceDateTime = None
        """
        The date (and possibly time) the risk assessment was performed.

        type: string
        """

        self.occurrencePeriod = None
        """
        The date (and possibly time) the risk assessment was performed.

        reference to Period
        """

        self.condition = None
        """
        For assessments or prognosis specific to a particular condition,
        indicates the condition being assessed.

        reference to Reference: identifier
        """

        self.performer = None
        """
        The provider or software application that performed the assessment.

        reference to Reference: identifier
        """

        self.reasonCodeableConcept = None
        """
        The reason the risk assessment was performed.

        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        The reason the risk assessment was performed.

        reference to Reference: identifier
        """

        self.basis = None
        """
        Indicates the source data considered as part of the assessment
        (FamilyHistory, Observations, Procedures, Conditions, etc.).

        type: array
        reference to Reference: identifier
        """

        self.prediction = None
        """
        Describes the expected outcome for the subject.

        type: array
        reference to RiskAssessment_Prediction
        """

        self.mitigation = None
        """
        A description of the steps that might be taken to reduce the
        identified risk(s).

        type: string
        """

        self.comment = None
        """
        Additional comments about the risk assessment.

        type: string
        """

        self.identifier = None
        """
        Business identifier assigned to the risk assessment.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'RiskAssessment_Prediction',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'prediction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'method'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'parent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'basis'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'condition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RiskAssessment',
             'child_variable': 'basedOn'},
        ]


class RiskAssessment_Prediction(fhirbase):
    """
    An assessment of the likely outcome(s) for a patient or other subject
    as well as the likelihood of each outcome.
    """

    __name__ = 'RiskAssessment_Prediction'

    def __init__(self, dict_values=None):
        self.outcome = None
        """
        One of the potential outcomes for the patient (e.g. remission, death,
        a particular condition).

        reference to CodeableConcept
        """

        self.probabilityDecimal = None
        """
        How likely is the outcome (in the specified timeframe).

        type: int
        """

        self.probabilityRange = None
        """
        How likely is the outcome (in the specified timeframe).

        reference to Range
        """

        self.qualitativeRisk = None
        """
        How likely is the outcome (in the specified timeframe), expressed as a
        qualitative value (e.g. low, medium, high).

        reference to CodeableConcept
        """

        self.relativeRisk = None
        """
        Indicates the risk for this particular subject (with their specific
        characteristics) divided by the risk of the population in general.
        (Numbers greater than 1 = higher risk than the population, numbers
        less than 1 = lower risk.).

        type: int
        """

        self.whenPeriod = None
        """
        Indicates the period of time or age range of the subject to which the
        specified probability applies.

        reference to Period
        """

        self.whenRange = None
        """
        Indicates the period of time or age range of the subject to which the
        specified probability applies.

        reference to Range
        """

        self.rationale = None
        """
        Additional information explaining the basis for the prediction.

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
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'qualitativeRisk'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'probabilityRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'whenPeriod'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'whenRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'RiskAssessment_Prediction',
             'child_variable': 'outcome'},
        ]
