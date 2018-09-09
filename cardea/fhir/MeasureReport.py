from .fhirbase import fhirbase


class MeasureReport(fhirbase):
    """The MeasureReport resource contains the results of evaluating a measure.
    """

    def __init__(self, dict_values=None):
        # this is a measurereport resource
        self.resourceType = 'MeasureReport'
        # type = string
        # possible values: MeasureReport

        # the report status. no data will be available until the report status is
        # complete.
        self.status = None
        # type = string
        # possible values: complete, pending, error

        # the type of measure report. this may be an individual report, which
        # provides a single patient's score for the measure; a patient listing,
        # which returns the list of patients that meet the various criteria in the
        # measure; or a summary report, which returns a population count for each
        # of the criteria in the measure.
        self.type = None
        # type = string
        # possible values: individual, patient-list, summary

        # a reference to the measure that was evaluated to produce this report.
        self.measure = None
        # reference to Reference: identifier

        # optional patient if the report was requested for a single patient.
        self.patient = None
        # reference to Reference: identifier

        # the date this measure report was generated.
        self.date = None
        # type = string

        # reporting organization.
        self.reportingOrganization = None
        # reference to Reference: identifier

        # the reporting period for which the report was calculated.
        self.period = None
        # reference to Period: Period

        # the results of the calculation, one for each population group in the
        # measure.
        self.group = None
        # type = array
        # reference to MeasureReport_Group: identifier

        # a reference to a bundle containing the resources that were used in the
        # evaluation of this report.
        self.evaluatedResources = None
        # reference to Reference: identifier

        # a formal identifier that is used to identify this report when it is
        # represented in other formats, or referenced in a specification, model,
        # design or an instance.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'complete', 'pending', 'error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'complete, pending, error'))

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'individual', 'patient-list', 'summary']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'individual, patient-list, summary'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'patient'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'evaluatedResources'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'measure'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'reportingOrganization'},

            {'parent_entity': 'MeasureReport_Group',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'group'},
        ]


class MeasureReport_Group(fhirbase):
    """The MeasureReport resource contains the results of evaluating a measure.
    """

    def __init__(self, dict_values=None):
        # the populations that make up the population group, one for each type of
        # population appropriate for the measure.
        self.population = None
        # type = array
        # reference to MeasureReport_Population: identifier

        # the measure score for this population group, calculated as appropriate
        # for the measure type and scoring method, and based on the contents of
        # the populations defined in the group.
        self.measureScore = None
        # type = int

        # when a measure includes multiple stratifiers, there will be a stratifier
        # group for each stratifier defined by the measure.
        self.stratifier = None
        # type = array
        # reference to MeasureReport_Stratifier: identifier

        # the identifier of the population group as defined in the measure
        # definition.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'MeasureReport_Population',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'population'},

            {'parent_entity': 'MeasureReport_Stratifier',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'stratifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'identifier'},
        ]


class MeasureReport_Population(fhirbase):
    """The MeasureReport resource contains the results of evaluating a measure.
    """

    def __init__(self, dict_values=None):
        # the type of the population.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the number of members of the population.
        self.count = None
        # type = int

        # this element refers to a list of patient level measurereport resources,
        # one for each patient in this population.
        self.patients = None
        # reference to Reference: identifier

        # the identifier of the population being reported, as defined by the
        # population element of the measure.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'patients'},
        ]


class MeasureReport_Stratifier(fhirbase):
    """The MeasureReport resource contains the results of evaluating a measure.
    """

    def __init__(self, dict_values=None):
        # this element contains the results for a single stratum within the
        # stratifier. for example, when stratifying on administrative gender,
        # there will be four strata, one for each possible gender value.
        self.stratum = None
        # type = array
        # reference to MeasureReport_Stratum: MeasureReport_Stratum

        # the identifier of this stratifier, as defined in the measure definition.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Stratifier',
             'child_variable': 'identifier'},

            {'parent_entity': 'MeasureReport_Stratum',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Stratifier',
             'child_variable': 'stratum'},
        ]


class MeasureReport_Stratum(fhirbase):
    """The MeasureReport resource contains the results of evaluating a measure.
    """

    def __init__(self, dict_values=None):
        # the value for this stratum, expressed as a string. when defining
        # stratifiers on complex values, the value must be rendered such that the
        # value for each stratum within the stratifier is unique.
        self.value = None
        # type = string

        # the populations that make up the stratum, one for each type of
        # population appropriate to the measure.
        self.population = None
        # type = array
        # reference to MeasureReport_Population1: identifier

        # the measure score for this stratum, calculated as appropriate for the
        # measure type and scoring method, and based on only the members of this
        # stratum.
        self.measureScore = None
        # type = int

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'MeasureReport_Population1',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Stratum',
             'child_variable': 'population'},
        ]


class MeasureReport_Population1(fhirbase):
    """The MeasureReport resource contains the results of evaluating a measure.
    """

    def __init__(self, dict_values=None):
        # the type of the population.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the number of members of the population in this stratum.
        self.count = None
        # type = int

        # this element refers to a list of patient level measurereport resources,
        # one for each patient in this population in this stratum.
        self.patients = None
        # reference to Reference: identifier

        # the identifier of the population being reported, as defined by the
        # population element of the measure.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population1',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Population1',
             'child_variable': 'patients'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population1',
             'child_variable': 'identifier'},
        ]
