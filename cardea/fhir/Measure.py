from .fhirbase import fhirbase


class Measure(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.
    """

    __name__ = 'Measure'

    def __init__(self, dict_values=None):
        self.resourceType = 'Measure'
        """
        This is a Measure resource

        type: string
        possible values: Measure
        """

        self.url = None
        """
        An absolute URI that is used to identify this measure when it is
        referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this measure is (or will be) published. The URL SHOULD include
        the major version of the measure. For more information see [Technical
        and Business Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the measure
        when it is referenced in a specification, model, design or instance.
        This is an arbitrary value managed by the measure author and is not
        expected to be globally unique. For example, it might be a timestamp
        (e.g. yyyymmdd) if a managed version is not available. There is also
        no expectation that versions can be placed in a lexicographical
        sequence. To provide a version consistent with the Decision Support
        Service specification, use the format Major.Minor.Revision (e.g.
        1.0.0). For more information on versioning knowledge assets, refer to
        the Decision Support Service specification. Note that a version is
        required for non-experimental active artifacts.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the measure. This name should be
        usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the measure.

        type: string
        """

        self.status = None
        """
        The status of this measure. Enables tracking the life-cycle of the
        content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this measure is authored for testing
        purposes (or education/evaluation/marketing), and is not intended to
        be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the measure was published. The
        date must change if and when the business version changes and it must
        change if the status code changes. In addition, it should change when
        the substantive content of the measure changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the measure.

        type: string
        """

        self.description = None
        """
        A free text natural language description of the measure from a
        consumer's perspective.

        type: string
        """

        self.purpose = None
        """
        Explaination of why this measure is needed and why it has been
        designed as it has.

        type: string
        """

        self.usage = None
        """
        A detailed description of how the measure is used from a clinical
        perspective.

        type: string
        """

        self.approvalDate = None
        """
        The date on which the resource content was approved by the publisher.
        Approval happens once when the content is officially approved for
        usage.

        type: string
        """

        self.lastReviewDate = None
        """
        The date on which the resource content was last reviewed. Review
        happens periodically after approval, but doesn't change the original
        approval date.

        type: string
        """

        self.effectivePeriod = None
        """
        The period during which the measure content was or is planned to be in
        active use.

        reference to Period
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate measure instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the measure is intended to be
        used.

        type: array
        reference to CodeableConcept
        """

        self.topic = None
        """
        Descriptive topics related to the content of the measure. Topics
        provide a high-level categorization of the type of the measure that
        can be useful for filtering and searching.

        type: array
        reference to CodeableConcept
        """

        self.contributor = None
        """
        A contributor to the content of the measure, including authors,
        editors, reviewers, and endorsers.

        type: array
        reference to Contributor
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        publisher.

        type: array
        reference to ContactDetail
        """

        self.copyright = None
        """
        A copyright statement relating to the measure and/or its contents.
        Copyright statements are generally legal restrictions on the use and
        publishing of the measure.

        type: string
        """

        self.relatedArtifact = None
        """
        Related artifacts such as additional documentation, justification, or
        bibliographic references.

        type: array
        reference to RelatedArtifact
        """

        self.library = None
        """
        A reference to a Library resource containing the formal logic used by
        the measure.

        type: array
        reference to Reference: identifier
        """

        self.disclaimer = None
        """
        Notices and disclaimers regarding the use of the measure, or related
        to intellectual property (such as code systems) referenced by the
        measure.

        type: string
        """

        self.scoring = None
        """
        Indicates how the calculation is performed for the measure, including
        proportion, ratio, continuous variable, and cohort. The value set is
        extensible, allowing additional measure scoring types to be
        represented.

        reference to CodeableConcept
        """

        self.compositeScoring = None
        """
        If this is a composite measure, the scoring method used to combine the
        component measures to determine the composite score.

        reference to CodeableConcept
        """

        self.type = None
        """
        Indicates whether the measure is used to examine a process, an outcome
        over time, a patient-reported outcome, or a structure measure such as
        utilization.

        type: array
        reference to CodeableConcept
        """

        self.riskAdjustment = None
        """
        A description of the risk adjustment factors that may impact the
        resulting score for the measure and how they may be accounted for when
        computing and reporting measure results.

        type: string
        """

        self.rateAggregation = None
        """
        Describes how to combine the information calculated, based on logic in
        each of several populations, into one summarized result.

        type: string
        """

        self.rationale = None
        """
        Provides a succint statement of the need for the measure. Usually
        includes statements pertaining to importance criterion: impact, gap in
        care, and evidence.

        type: string
        """

        self.clinicalRecommendationStatement = None
        """
        Provides a summary of relevant clinical guidelines or other clinical
        recommendations supporting the measure.

        type: string
        """

        self.improvementNotation = None
        """
        Information on whether an increase or decrease in score is the
        preferred result (e.g., a higher score indicates better quality OR a
        lower score indicates better quality OR quality is whthin a range).

        type: string
        """

        self.definition = None
        """
        Provides a description of an individual term used within the measure.

        type: array
        """

        self.guidance = None
        """
        Additional guidance for the measure including how it can be used in a
        clinical context, and the intent of the measure.

        type: string
        """

        self.set = None
        """
        The measure set, e.g. Preventive Care and Screening.

        type: string
        """

        self.group = None
        """
        A group of population criteria for the measure.

        type: array
        reference to Measure_Group: identifier
        """

        self.supplementalData = None
        """
        The supplemental data criteria for the measure report, specified as
        either the name of a valid CQL expression within a referenced library,
        or a valid FHIR Resource Path.

        type: array
        reference to Measure_SupplementalData: identifier
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this measure when it is
        represented in other formats, or referenced in a specification, model,
        design or an instance.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'scoring'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'type'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'contributor'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'compositeScoring'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'topic'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'library'},

            {'parent_entity': 'Measure_SupplementalData',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'supplementalData'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'useContext'},

            {'parent_entity': 'Measure_Group',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'group'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'effectivePeriod'},
        ]


class Measure_Group(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.
    """

    __name__ = 'Measure_Group'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Optional name or short description of this group.

        type: string
        """

        self.description = None
        """
        The human readable description of this population group.

        type: string
        """

        self.population = None
        """
        A population criteria for the measure.

        type: array
        reference to Measure_Population: identifier
        """

        self.stratifier = None
        """
        The stratifier criteria for the measure report, specified as either
        the name of a valid CQL expression defined within a referenced
        library, or a valid FHIR Resource Path.

        type: array
        reference to Measure_Stratifier: identifier
        """

        self.identifier = None
        """
        A unique identifier for the group. This identifier will used to report
        data for the group in the measure report.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Group',
             'child_variable': 'identifier'},

            {'parent_entity': 'Measure_Stratifier',
             'parent_variable': 'identifier',
             'child_entity': 'Measure_Group',
             'child_variable': 'stratifier'},

            {'parent_entity': 'Measure_Population',
             'parent_variable': 'identifier',
             'child_entity': 'Measure_Group',
             'child_variable': 'population'},
        ]


class Measure_Population(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.
    """

    __name__ = 'Measure_Population'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The type of population criteria.

        reference to CodeableConcept
        """

        self.name = None
        """
        Optional name or short description of this population.

        type: string
        """

        self.description = None
        """
        The human readable description of this population criteria.

        type: string
        """

        self.criteria = None
        """
        The name of a valid referenced CQL expression (may be namespaced) that
        defines this population criteria.

        type: string
        """

        self.identifier = None
        """
        A unique identifier for the population criteria. This identifier is
        used to report data against this criteria within the measure report.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Population',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Population',
             'child_variable': 'code'},
        ]


class Measure_Stratifier(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.
    """

    __name__ = 'Measure_Stratifier'

    def __init__(self, dict_values=None):
        self.criteria = None
        """
        The criteria for the stratifier. This must be the name of an
        expression defined within a referenced library.

        type: string
        """

        self.path = None
        """
        The path to an element that defines the stratifier, specified as a
        valid FHIR resource path.

        type: string
        """

        self.identifier = None
        """
        The identifier for the stratifier used to coordinate the reported data
        back to this stratifier.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Stratifier',
             'child_variable': 'identifier'},
        ]


class Measure_SupplementalData(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.
    """

    __name__ = 'Measure_SupplementalData'

    def __init__(self, dict_values=None):
        self.usage = None
        """
        An indicator of the intended usage for the supplemental data element.
        Supplemental data indicates the data is additional information
        requested to augment the measure information. Risk adjustment factor
        indicates the data is additional information used to calculate risk
        adjustment factors when applying a risk model to the measure
        calculation.

        type: array
        reference to CodeableConcept
        """

        self.criteria = None
        """
        The criteria for the supplemental data. This must be the name of a
        valid expression defined within a referenced library, and defines the
        data to be returned for this element.

        type: string
        """

        self.path = None
        """
        The supplemental data to be supplied as part of the measure response,
        specified as a valid FHIR Resource Path.

        type: string
        """

        self.identifier = None
        """
        An identifier for the supplemental data.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_SupplementalData',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_SupplementalData',
             'child_variable': 'usage'},
        ]
