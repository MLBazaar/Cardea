from .fhirbase import fhirbase


class MeasureReport(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.
    """

    __name__ = 'MeasureReport'

    def __init__(self, dict_values=None):
        self.resourceType = 'MeasureReport'
        """
        This is a MeasureReport resource

        type: string
        possible values: MeasureReport
        """

        self.status = None
        """
        The report status. No data will be available until the report status
        is complete.

        type: string
        possible values: complete, pending, error
        """

        self.type = None
        """
        The type of measure report. This may be an individual report, which
        provides a single patient's score for the measure; a patient listing,
        which returns the list of patients that meet the various criteria in
        the measure; or a summary report, which returns a population count for
        each of the criteria in the measure.

        type: string
        possible values: individual, patient-list, summary
        """

        self.measure = None
        """
        A reference to the Measure that was evaluated to produce this report.

        reference to Reference: identifier
        """

        self.patient = None
        """
        Optional Patient if the report was requested for a single patient.

        reference to Reference: identifier
        """

        self.date = None
        """
        The date this measure report was generated.

        type: string
        """

        self.reportingOrganization = None
        """
        Reporting Organization.

        reference to Reference: identifier
        """

        self.period = None
        """
        The reporting period for which the report was calculated.

        reference to Period
        """

        self.group = None
        """
        The results of the calculation, one for each population group in the
        measure.

        type: array
        reference to MeasureReport_Group: identifier
        """

        self.evaluatedResources = None
        """
        A reference to a Bundle containing the Resources that were used in the
        evaluation of this report.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this report when it is
        represented in other formats, or referenced in a specification, model,
        design or an instance.

        reference to Identifier
        """

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
            {'parent_entity': 'MeasureReport_Group',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'group'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'measure'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'reportingOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport',
             'child_variable': 'evaluatedResources'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport',
             'child_variable': 'period'},
        ]


class MeasureReport_Group(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.
    """

    __name__ = 'MeasureReport_Group'

    def __init__(self, dict_values=None):
        self.population = None
        """
        The populations that make up the population group, one for each type
        of population appropriate for the measure.

        type: array
        reference to MeasureReport_Population: identifier
        """

        self.measureScore = None
        """
        The measure score for this population group, calculated as appropriate
        for the measure type and scoring method, and based on the contents of
        the populations defined in the group.

        type: int
        """

        self.stratifier = None
        """
        When a measure includes multiple stratifiers, there will be a
        stratifier group for each stratifier defined by the measure.

        type: array
        reference to MeasureReport_Stratifier: identifier
        """

        self.identifier = None
        """
        The identifier of the population group as defined in the measure
        definition.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'MeasureReport_Stratifier',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'stratifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'identifier'},

            {'parent_entity': 'MeasureReport_Population',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Group',
             'child_variable': 'population'},
        ]


class MeasureReport_Population(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.
    """

    __name__ = 'MeasureReport_Population'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The type of the population.

        reference to CodeableConcept
        """

        self.count = None
        """
        The number of members of the population.

        type: int
        """

        self.patients = None
        """
        This element refers to a List of patient level MeasureReport
        resources, one for each patient in this population.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        The identifier of the population being reported, as defined by the
        population element of the measure.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'code'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MeasureReport_Population',
             'child_variable': 'patients'},
        ]


class MeasureReport_Stratifier(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.
    """

    __name__ = 'MeasureReport_Stratifier'

    def __init__(self, dict_values=None):
        self.stratum = None
        """
        This element contains the results for a single stratum within the
        stratifier. For example, when stratifying on administrative gender,
        there will be four strata, one for each possible gender value.

        type: array
        reference to MeasureReport_Stratum
        """

        self.identifier = None
        """
        The identifier of this stratifier, as defined in the measure
        definition.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'MeasureReport_Stratum',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Stratifier',
             'child_variable': 'stratum'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MeasureReport_Stratifier',
             'child_variable': 'identifier'},
        ]


class MeasureReport_Stratum(fhirbase):
    """
    The MeasureReport resource contains the results of evaluating a
    measure.
    """

    __name__ = 'MeasureReport_Stratum'

    def __init__(self, dict_values=None):
        self.value = None
        """
        The value for this stratum, expressed as a string. When defining
        stratifiers on complex values, the value must be rendered such that
        the value for each stratum within the stratifier is unique.

        type: string
        """

        self.population = None
        """
        The populations that make up the stratum, one for each type of
        population appropriate to the measure.

        type: array
        reference to MeasureReport_Population1: identifier
        """

        self.measureScore = None
        """
        The measure score for this stratum, calculated as appropriate for the
        measure type and scoring method, and based on only the members of this
        stratum.

        type: int
        """

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
    """

    __name__ = 'MeasureReport_Population1'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The type of the population.

        reference to CodeableConcept
        """

        self.count = None
        """
        The number of members of the population in this stratum.

        type: int
        """

        self.patients = None
        """
        This element refers to a List of patient level MeasureReport
        resources, one for each patient in this population in this stratum.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        The identifier of the population being reported, as defined by the
        population element of the measure.

        reference to Identifier
        """

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
