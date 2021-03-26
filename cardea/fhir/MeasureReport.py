from .fhirbase import fhirbase


class MeasureReport(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.

    Args:
        resourceType: This is a MeasureReport resource
        identifier: A formal identifier that is used to identify this report
            when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        status: The report status. No data will be available until the report
            status is complete.
        type: The type of measure report. This may be an individual report,
            which provides a single patient's score for the measure; a patient
            listing, which returns the list of patients that meet the various
            criteria in the measure; or a summary report, which returns a
            population count for each of the criteria in the measure.
        measure: A reference to the Measure that was evaluated to produce this
            report.
        patient: Optional Patient if the report was requested for a single
            patient.
        date: The date this measure report was generated.
        reportingOrganization: Reporting Organization.
        period: The reporting period for which the report was calculated.
        group: The results of the calculation, one for each population group
            in the measure.
        evaluatedResources: A reference to a Bundle containing the Resources
            that were used in the evaluation of this report.
    """

    __name__ = 'MeasureReport'

    def __init__(self, dict_values=None):
        self.resourceType = 'MeasureReport'
        # type: str
        # possible values: MeasureReport

        self.status = None
        # type: str
        # possible values: complete, pending, error

        self.type = None
        # type: str
        # possible values: individual, patient-list, summary

        self.measure = None
        # reference to Reference: identifier

        self.patient = None
        # reference to Reference: identifier

        self.date = None
        # type: str

        self.reportingOrganization = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.group = None
        # type: list
        # reference to MeasureReport_Group: identifier

        self.evaluatedResources = None
        # reference to Reference: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'reportingOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'measure'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'patient'},

            {'parent_entity': 'MeasureReport_Group',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'group'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'evaluatedResources'},
        ]


class MeasureReport_Group(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.

    Args:
        identifier: The identifier of the population group as defined in the
            measure definition.
        population: The populations that make up the population group, one for
            each type of population appropriate for the measure.
        measureScore: The measure score for this population group, calculated
            as appropriate for the measure type and scoring method, and based on
            the contents of the populations defined in the group.
        stratifier: When a measure includes multiple stratifiers, there will
            be a stratifier group for each stratifier defined by the measure.
    """

    __name__ = 'MeasureReport_Group'

    def __init__(self, dict_values=None):
        self.population = None
        # type: list
        # reference to MeasureReport_Population: identifier

        self.measureScore = None
        # type: int

        self.stratifier = None
        # type: list
        # reference to MeasureReport_Stratifier: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'MeasureReport_Stratifier',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'stratifier'},

            {'parent_entity': 'MeasureReport_Population',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'population'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'identifier'},
        ]


class MeasureReport_Population(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.

    Args:
        identifier: The identifier of the population being reported, as
            defined by the population element of the measure.
        code: The type of the population.
        count: The number of members of the population.
        patients: This element refers to a List of patient level MeasureReport
            resources, one for each patient in this population.
    """

    __name__ = 'MeasureReport_Population'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.count = None
        # type: int

        self.patients = None
        # reference to Reference: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'patients'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'code'},
        ]


class MeasureReport_Stratifier(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.

    Args:
        identifier: The identifier of this stratifier, as defined in the
            measure definition.
        stratum: This element contains the results for a single stratum within
            the stratifier. For example, when stratifying on administrative
            gender, there will be four strata, one for each possible gender value.
    """

    __name__ = 'MeasureReport_Stratifier'

    def __init__(self, dict_values=None):
        self.stratum = None
        # type: list
        # reference to MeasureReport_Stratum

        self.identifier = None
        # reference to Identifier

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
    """
    The MeasureReport resource contains the results of evaluating a
    measure.

    Args:
        value: The value for this stratum, expressed as a string. When
            defining stratifiers on complex values, the value must be rendered
            such that the value for each stratum within the stratifier is unique.
        population: The populations that make up the stratum, one for each
            type of population appropriate to the measure.
        measureScore: The measure score for this stratum, calculated as
            appropriate for the measure type and scoring method, and based on only
            the members of this stratum.
    """

    __name__ = 'MeasureReport_Stratum'

    def __init__(self, dict_values=None):
        self.value = None
        # type: str

        self.population = None
        # type: list
        # reference to MeasureReport_Population1: identifier

        self.measureScore = None
        # type: int

        self.object_id = None
        # unique identifier for object class

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
    """
    The MeasureReport resource contains the results of evaluating a
    measure.

    Args:
        identifier: The identifier of the population being reported, as
            defined by the population element of the measure.
        code: The type of the population.
        count: The number of members of the population in this stratum.
        patients: This element refers to a List of patient level MeasureReport
            resources, one for each patient in this population in this stratum.
    """

    __name__ = 'MeasureReport_Population1'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.count = None
        # type: int

        self.patients = None
        # reference to Reference: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Population1',
             'child_variable': 'patients'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population1',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population1',
             'child_variable': 'code'},
        ]
