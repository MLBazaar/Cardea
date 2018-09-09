from .fhirbase import fhirbase


class ImmunizationRecommendation(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    __name__ = 'ImmunizationRecommendation'

    def __init__(self, dict_values=None):
        self.resourceType = 'ImmunizationRecommendation'
        """
        This is a ImmunizationRecommendation resource

        type: string
        possible values: ImmunizationRecommendation
        """

        self.patient = None
        """
        The patient the recommendations are for.

        reference to Reference: identifier
        """

        self.recommendation = None
        """
        Vaccine administration recommendations.

        type: array
        reference to ImmunizationRecommendation_Recommendation
        """

        self.identifier = None
        """
        A unique identifier assigned to this particular recommendation record.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ImmunizationRecommendation_Recommendation',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation',
             'child_variable': 'recommendation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImmunizationRecommendation',
             'child_variable': 'patient'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation',
             'child_variable': 'identifier'},
        ]


class ImmunizationRecommendation_Recommendation(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    __name__ = 'ImmunizationRecommendation_Recommendation'

    def __init__(self, dict_values=None):
        self.date = None
        """
        The date the immunization recommendation was created.

        type: string
        """

        self.vaccineCode = None
        """
        Vaccine that pertains to the recommendation.

        reference to CodeableConcept
        """

        self.targetDisease = None
        """
        The targeted disease for the recommendation.

        reference to CodeableConcept
        """

        self.doseNumber = None
        """
        The next recommended dose number (e.g. dose 2 is the next recommended
        dose).

        type: int
        """

        self.forecastStatus = None
        """
        Vaccine administration status.

        reference to CodeableConcept
        """

        self.dateCriterion = None
        """
        Vaccine date recommendations.  For example, earliest date to
        administer, latest date to administer, etc.

        type: array
        reference to ImmunizationRecommendation_DateCriterion
        """

        self.protocol = None
        """
        Contains information about the protocol under which the vaccine was
        administered.

        reference to ImmunizationRecommendation_Protocol
        """

        self.supportingImmunization = None
        """
        Immunization event history that supports the status and
        recommendation.

        type: array
        reference to Reference: identifier
        """

        self.supportingPatientInformation = None
        """
        Patient Information that supports the status and recommendation.  This
        includes patient observations, adverse reactions and
        allergy/intolerance information.

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
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'vaccineCode'},

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

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'targetDisease'},

            {'parent_entity': 'ImmunizationRecommendation_DateCriterion',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'dateCriterion'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImmunizationRecommendation_Recommendation',
             'child_variable': 'forecastStatus'},
        ]


class ImmunizationRecommendation_DateCriterion(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    __name__ = 'ImmunizationRecommendation_DateCriterion'

    def __init__(self, dict_values=None):
        self.code = None
        """
        Date classification of recommendation.  For example, earliest date to
        give, latest date to give, etc.

        reference to CodeableConcept
        """

        self.value = None
        """
        The date whose meaning is specified by dateCriterion.code.

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
             'child_entity': 'ImmunizationRecommendation_DateCriterion',
             'child_variable': 'code'},
        ]


class ImmunizationRecommendation_Protocol(fhirbase):
    """
    A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    __name__ = 'ImmunizationRecommendation_Protocol'

    def __init__(self, dict_values=None):
        self.doseSequence = None
        """
        Indicates the nominal position in a series of the next dose.  This is
        the recommended dose number as per a specified protocol.

        type: int
        """

        self.description = None
        """
        Contains the description about the protocol under which the vaccine
        was administered.

        type: string
        """

        self.authority = None
        """
        Indicates the authority who published the protocol.  For example,
        ACIP.

        reference to Reference: identifier
        """

        self.series = None
        """
        One possible path to achieve presumed immunity against a disease -
        within the context of an authority.

        type: string
        """

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
