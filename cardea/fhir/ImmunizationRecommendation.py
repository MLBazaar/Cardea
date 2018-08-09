from .fhirbase import * 
from .Reference import Reference
from .Identifier import Identifier

class ImmunizationRecommendation(fhirbase):
    """A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    def __init__(self, dict_values=None):
        # this is a immunizationrecommendation resource
        self.resourceType = 'ImmunizationRecommendation'
        # type = string
        # possible values = ImmunizationRecommendation

        # the patient the recommendations are for.
        self.patient = None
        # reference to Reference: identifier

        # vaccine administration recommendations.
        self.recommendation = None
        # type = array
        # reference to ImmunizationRecommendation_Recommendation: ImmunizationRecommendation_Recommendation

        # a unique identifier assigned to this particular recommendation record.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImmunizationRecommendation',
            'child_variable': 'patient'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ImmunizationRecommendation',
            'child_variable': 'identifier'},

            {'parent_entity': 'ImmunizationRecommendation_Recommendation',
            'parent_variable': 'object_id',
            'child_entity': 'ImmunizationRecommendation',
            'child_variable': 'recommendation'},
        ]

class ImmunizationRecommendation_Recommendation(fhirbase):
    """A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    def __init__(self, dict_values=None):
        # the date the immunization recommendation was created.
        self.date = None
        # type = string

        # vaccine that pertains to the recommendation.
        self.vaccineCode = None
        # reference to CodeableConcept: CodeableConcept

        # the targeted disease for the recommendation.
        self.targetDisease = None
        # reference to CodeableConcept: CodeableConcept

        # the next recommended dose number (e.g. dose 2 is the next recommended
        # dose).
        self.doseNumber = None
        # type = int

        # vaccine administration status.
        self.forecastStatus = None
        # reference to CodeableConcept: CodeableConcept

        # vaccine date recommendations.  for example, earliest date to administer,
        # latest date to administer, etc.
        self.dateCriterion = None
        # type = array
        # reference to ImmunizationRecommendation_DateCriterion: ImmunizationRecommendation_DateCriterion

        # contains information about the protocol under which the vaccine was
        # administered.
        self.protocol = None
        # reference to ImmunizationRecommendation_Protocol: ImmunizationRecommendation_Protocol

        # immunization event history that supports the status and recommendation.
        self.supportingImmunization = None
        # type = array
        # reference to Reference: identifier

        # patient information that supports the status and recommendation.  this
        # includes patient observations, adverse reactions and allergy/intolerance
        # information.
        self.supportingPatientInformation = None
        # type = array
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImmunizationRecommendation_Recommendation',
            'child_variable': 'supportingPatientInformation'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ImmunizationRecommendation_Recommendation',
            'child_variable': 'vaccineCode'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ImmunizationRecommendation_Recommendation',
            'child_variable': 'forecastStatus'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImmunizationRecommendation_Recommendation',
            'child_variable': 'supportingImmunization'},

            {'parent_entity': 'ImmunizationRecommendation_DateCriterion',
            'parent_variable': 'object_id',
            'child_entity': 'ImmunizationRecommendation_Recommendation',
            'child_variable': 'dateCriterion'},

            {'parent_entity': 'ImmunizationRecommendation_Protocol',
            'parent_variable': 'object_id',
            'child_entity': 'ImmunizationRecommendation_Recommendation',
            'child_variable': 'protocol'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ImmunizationRecommendation_Recommendation',
            'child_variable': 'targetDisease'},
        ]

class ImmunizationRecommendation_DateCriterion(fhirbase):
    """A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    def __init__(self, dict_values=None):
        # date classification of recommendation.  for example, earliest date to
        # give, latest date to give, etc.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the date whose meaning is specified by datecriterion.code.
        self.value = None
        # type = string


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
    """A patient's point-in-time immunization and recommendation (i.e.
    forecasting a patient's immunization eligibility according to a
    published schedule) with optional supporting justification.
    """

    def __init__(self, dict_values=None):
        # indicates the nominal position in a series of the next dose.  this is
        # the recommended dose number as per a specified protocol.
        self.doseSequence = None
        # type = int

        # contains the description about the protocol under which the vaccine was
        # administered.
        self.description = None
        # type = string

        # indicates the authority who published the protocol.  for example, acip.
        self.authority = None
        # reference to Reference: identifier

        # one possible path to achieve presumed immunity against a disease -
        # within the context of an authority.
        self.series = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImmunizationRecommendation_Protocol',
            'child_variable': 'authority'},
        ]

