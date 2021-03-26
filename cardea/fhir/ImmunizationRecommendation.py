from .fhirbase import fhirbase


class ImmunizationRecommendation(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.

    Args:
        resourceType: This is a ImmunizationRecommendation resource
        identifier: A unique identifier assigned to this particular
            recommendation record.
        patient: The patient the recommendations are for.
        recommendation: Vaccine administration recommendations.
    """

    __name__ = 'ImmunizationRecommendation'

    def __init__(self, dict_values=None):
        self.resourceType = 'ImmunizationRecommendation'
        # type: str
        # possible values: ImmunizationRecommendation

        self.patient = None
        # reference to Reference: identifier

        self.recommendation = None
        # type: list
        # reference to ImmunizationRecommendation_Recommendation

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImmunizationRecommendation',
             'child_variable': 'patient'},

            {'parent_entity': 'ImmunizationRecommendation_Recommendation',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation',
             'child_variable': 'recommendation'},
        ]


class ImmunizationRecommendation_Recommendation(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.

    Args:
        date: The date the immunization recommendation was created.
        vaccineCode: Vaccine that pertains to the recommendation.
        targetDisease: The targeted disease for the recommendation.
        doseNumber: The next recommended dose number (e.g. dose 2 is the next
            recommended dose).
        forecastStatus: Vaccine administration status.
        dateCriterion: Vaccine date recommendations.  For example, earliest
            date to administer, latest date to administer, etc.
        protocol: Contains information about the protocol under which the
            vaccine was administered.
        supportingImmunization: Immunization event history that supports the
            status and recommendation.
        supportingPatientInformation: Patient Information that supports the
            status and recommendation.  This includes patient observations,
            adverse reactions and allergy/intolerance information.
    """

    __name__ = 'ImmunizationRecommendation_Recommendation'

    def __init__(self, dict_values=None):
        self.date = None
        # type: str

        self.vaccineCode = None
        # reference to CodeableConcept

        self.targetDisease = None
        # reference to CodeableConcept

        self.doseNumber = None
        # type: int

        self.forecastStatus = None
        # reference to CodeableConcept

        self.dateCriterion = None
        # type: list
        # reference to ImmunizationRecommendation_DateCriterion

        self.protocol = None
        # reference to ImmunizationRecommendation_Protocol

        self.supportingImmunization = None
        # type: list
        # reference to Reference: identifier

        self.supportingPatientInformation = None
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
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'forecastStatus'},

            {'parent_entity': 'ImmunizationRecommendation_DateCriterion',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'dateCriterion'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'vaccineCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'targetDisease'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'supportingImmunization'},

            {'parent_entity': 'ImmunizationRecommendation_Protocol',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'protocol'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'supportingPatientInformation'},
        ]


class ImmunizationRecommendation_DateCriterion(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.

    Args:
        code: Date classification of recommendation.  For example, earliest
            date to give, latest date to give, etc.
        value: The date whose meaning is specified by dateCriterion.code.
    """

    __name__ = 'ImmunizationRecommendation_DateCriterion'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_DateCriterion',
             'child_variable': 'code'},
        ]


class ImmunizationRecommendation_Protocol(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.

    Args:
        doseSequence: Indicates the nominal position in a series of the next
            dose.  This is the recommended dose number as per a specified
            protocol.
        description: Contains the description about the protocol under which
            the vaccine was administered.
        authority: Indicates the authority who published the protocol.  For
            example, ACIP.
        series: One possible path to achieve presumed immunity against a
            disease - within the context of an authority.
    """

    __name__ = 'ImmunizationRecommendation_Protocol'

    def __init__(self, dict_values=None):
        self.doseSequence = None
        # type: int

        self.description = None
        # type: str

        self.authority = None
        # reference to Reference: identifier

        self.series = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImmunizationRecommendation_Protocol',
             'child_variable': 'authority'},
        ]
