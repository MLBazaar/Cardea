from .fhirbase import fhirbase


class Measure(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.

    Args:
        resourceType: This is a Measure resource
        url: An absolute URI that is used to identify this measure when it is
            referenced in a specification, model, design or an instance. This
            SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
            which this measure is (or will be) published. The URL SHOULD include
            the major version of the measure. For more information see [Technical
            and Business Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this measure
            when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            measure when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the measure author and
            is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There
            is also no expectation that versions can be placed in a
            lexicographical sequence. To provide a version consistent with the
            Decision Support Service specification, use the format
            Major.Minor.Revision (e.g. 1.0.0). For more information on versioning
            knowledge assets, refer to the Decision Support Service specification.
            Note that a version is required for non-experimental active artifacts.
        name: A natural language name identifying the measure. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the measure.
        status: The status of this measure. Enables tracking the life-cycle of
            the content.
        experimental: A boolean value to indicate that this measure is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the measure was published.
            The date must change if and when the business version changes and it
            must change if the status code changes. In addition, it should change
            when the substantive content of the measure changes.
        publisher: The name of the individual or organization that published
            the measure.
        description: A free text natural language description of the measure
            from a consumer's perspective.
        purpose: Explaination of why this measure is needed and why it has
            been designed as it has.
        usage: A detailed description of how the measure is used from a
            clinical perspective.
        approvalDate: The date on which the resource content was approved by
            the publisher. Approval happens once when the content is officially
            approved for usage.
        lastReviewDate: The date on which the resource content was last
            reviewed. Review happens periodically after approval, but doesn't
            change the original approval date.
        effectivePeriod: The period during which the measure content was or is
            planned to be in active use.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate measure instances.
        jurisdiction: A legal or geographic region in which the measure is
            intended to be used.
        topic: Descriptive topics related to the content of the measure.
            Topics provide a high-level categorization of the type of the measure
            that can be useful for filtering and searching.
        contributor: A contributor to the content of the measure, including
            authors, editors, reviewers, and endorsers.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        copyright: A copyright statement relating to the measure and/or its
            contents. Copyright statements are generally legal restrictions on the
            use and publishing of the measure.
        relatedArtifact: Related artifacts such as additional documentation,
            justification, or bibliographic references.
        library: A reference to a Library resource containing the formal logic
            used by the measure.
        disclaimer: Notices and disclaimers regarding the use of the measure,
            or related to intellectual property (such as code systems) referenced
            by the measure.
        scoring: Indicates how the calculation is performed for the measure,
            including proportion, ratio, continuous variable, and cohort. The
            value set is extensible, allowing additional measure scoring types to
            be represented.
        compositeScoring: If this is a composite measure, the scoring method
            used to combine the component measures to determine the composite
            score.
        type: Indicates whether the measure is used to examine a process, an
            outcome over time, a patient-reported outcome, or a structure measure
            such as utilization.
        riskAdjustment: A description of the risk adjustment factors that may
            impact the resulting score for the measure and how they may be
            accounted for when computing and reporting measure results.
        rateAggregation: Describes how to combine the information calculated,
            based on logic in each of several populations, into one summarized
            result.
        rationale: Provides a succint statement of the need for the measure.
            Usually includes statements pertaining to importance criterion:
            impact, gap in care, and evidence.
        clinicalRecommendationStatement: Provides a summary of relevant
            clinical guidelines or other clinical recommendations supporting the
            measure.
        improvementNotation: Information on whether an increase or decrease in
            score is the preferred result (e.g., a higher score indicates better
            quality OR a lower score indicates better quality OR quality is whthin
            a range).
        definition: Provides a description of an individual term used within
            the measure.
        guidance: Additional guidance for the measure including how it can be
            used in a clinical context, and the intent of the measure.
        set: The measure set, e.g. Preventive Care and Screening.
        group: A group of population criteria for the measure.
        supplementalData: The supplemental data criteria for the measure
            report, specified as either the name of a valid CQL expression within
            a referenced library, or a valid FHIR Resource Path.
    """

    __name__ = 'Measure'

    def __init__(self, dict_values=None):
        self.resourceType = 'Measure'
        # type: str
        # possible values: Measure

        self.url = None
        # type: str

        self.version = None
        # type: str

        self.name = None
        # type: str

        self.title = None
        # type: str

        self.status = None
        # type: str
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # type: bool

        self.date = None
        # type: str

        self.publisher = None
        # type: str

        self.description = None
        # type: str

        self.purpose = None
        # type: str

        self.usage = None
        # type: str

        self.approvalDate = None
        # type: str

        self.lastReviewDate = None
        # type: str

        self.effectivePeriod = None
        # reference to Period

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.topic = None
        # type: list
        # reference to CodeableConcept

        self.contributor = None
        # type: list
        # reference to Contributor

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.copyright = None
        # type: str

        self.relatedArtifact = None
        # type: list
        # reference to RelatedArtifact

        self.library = None
        # type: list
        # reference to Reference: identifier

        self.disclaimer = None
        # type: str

        self.scoring = None
        # reference to CodeableConcept

        self.compositeScoring = None
        # reference to CodeableConcept

        self.type = None
        # type: list
        # reference to CodeableConcept

        self.riskAdjustment = None
        # type: str

        self.rateAggregation = None
        # type: str

        self.rationale = None
        # type: str

        self.clinicalRecommendationStatement = None
        # type: str

        self.improvementNotation = None
        # type: str

        self.definition = None
        # type: list

        self.guidance = None
        # type: str

        self.set = None
        # type: str

        self.group = None
        # type: list
        # reference to Measure_Group: identifier

        self.supplementalData = None
        # type: list
        # reference to Measure_SupplementalData: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Measure_SupplementalData',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'supplementalData'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'scoring'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'useContext'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'topic'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'contact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'library'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'contributor'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'compositeScoring'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Measure_Group',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'group'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'relatedArtifact'},
        ]


class Measure_Group(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.

    Args:
        identifier: A unique identifier for the group. This identifier will
            used to report data for the group in the measure report.
        name: Optional name or short description of this group.
        description: The human readable description of this population group.
        population: A population criteria for the measure.
        stratifier: The stratifier criteria for the measure report, specified
            as either the name of a valid CQL expression defined within a
            referenced library, or a valid FHIR Resource Path.
    """

    __name__ = 'Measure_Group'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.description = None
        # type: str

        self.population = None
        # type: list
        # reference to Measure_Population: identifier

        self.stratifier = None
        # type: list
        # reference to Measure_Stratifier: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Measure_Population',
             'parent_variable': 'identifier',
             'child_entity': 'Measure_Group',
             'child_variable': 'population'},

            {'parent_entity': 'Measure_Stratifier',
             'parent_variable': 'identifier',
             'child_entity': 'Measure_Group',
             'child_variable': 'stratifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Group',
             'child_variable': 'identifier'},
        ]


class Measure_Population(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.

    Args:
        identifier: A unique identifier for the population criteria. This
            identifier is used to report data against this criteria within the
            measure report.
        code: The type of population criteria.
        name: Optional name or short description of this population.
        description: The human readable description of this population
            criteria.
        criteria: The name of a valid referenced CQL expression (may be
            namespaced) that defines this population criteria.
    """

    __name__ = 'Measure_Population'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.name = None
        # type: str

        self.description = None
        # type: str

        self.criteria = None
        # type: str

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Population',
             'child_variable': 'code'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Population',
             'child_variable': 'identifier'},
        ]


class Measure_Stratifier(fhirbase):
    """
    The Measure resource provides the definition of a quality measure.

    Args:
        identifier: The identifier for the stratifier used to coordinate the
            reported data back to this stratifier.
        criteria: The criteria for the stratifier. This must be the name of an
            expression defined within a referenced library.
        path: The path to an element that defines the stratifier, specified as
            a valid FHIR resource path.
    """

    __name__ = 'Measure_Stratifier'

    def __init__(self, dict_values=None):
        self.criteria = None
        # type: str

        self.path = None
        # type: str

        self.identifier = None
        # reference to Identifier

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

    Args:
        identifier: An identifier for the supplemental data.
        usage: An indicator of the intended usage for the supplemental data
            element. Supplemental data indicates the data is additional
            information requested to augment the measure information. Risk
            adjustment factor indicates the data is additional information used to
            calculate risk adjustment factors when applying a risk model to the
            measure calculation.
        criteria: The criteria for the supplemental data. This must be the
            name of a valid expression defined within a referenced library, and
            defines the data to be returned for this element.
        path: The supplemental data to be supplied as part of the measure
            response, specified as a valid FHIR Resource Path.
    """

    __name__ = 'Measure_SupplementalData'

    def __init__(self, dict_values=None):
        self.usage = None
        # type: list
        # reference to CodeableConcept

        self.criteria = None
        # type: str

        self.path = None
        # type: str

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_SupplementalData',
             'child_variable': 'usage'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_SupplementalData',
             'child_variable': 'identifier'},
        ]
