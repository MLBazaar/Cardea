from .fhirbase import fhirbase


class Measure(fhirbase):
    """The Measure resource provides the definition of a quality measure.
    """

    def __init__(self, dict_values=None):
        # this is a measure resource
        self.resourceType = 'Measure'
        # type = string
        # possible values: Measure

        # an absolute uri that is used to identify this measure when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this measure is (or will be) published. the url should include the major
        # version of the measure. for more information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the measure when
        # it is referenced in a specification, model, design or instance. this is
        # an arbitrary value managed by the measure author and is not expected to
        # be globally unique. for example, it might be a timestamp (e.g. yyyymmdd)
        # if a managed version is not available. there is also no expectation that
        # versions can be placed in a lexicographical sequence. to provide a
        # version consistent with the decision support service specification, use
        # the format major.minor.revision (e.g. 1.0.0). for more information on
        # versioning knowledge assets, refer to the decision support service
        # specification. note that a version is required for non-experimental
        # active artifacts.
        self.version = None
        # type = string

        # a natural language name identifying the measure. this name should be
        # usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the measure.
        self.title = None
        # type = string

        # the status of this measure. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this measure is authored for testing
        # purposes (or education/evaluation/marketing), and is not intended to be
        # used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the measure was published. the date
        # must change if and when the business version changes and it must change
        # if the status code changes. in addition, it should change when the
        # substantive content of the measure changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the measure.
        self.publisher = None
        # type = string

        # a free text natural language description of the measure from a
        # consumer's perspective.
        self.description = None
        # type = string

        # explaination of why this measure is needed and why it has been designed
        # as it has.
        self.purpose = None
        # type = string

        # a detailed description of how the measure is used from a clinical
        # perspective.
        self.usage = None
        # type = string

        # the date on which the resource content was approved by the publisher.
        # approval happens once when the content is officially approved for usage.
        self.approvalDate = None
        # type = string

        # the date on which the resource content was last reviewed. review happens
        # periodically after approval, but doesn't change the original approval
        # date.
        self.lastReviewDate = None
        # type = string

        # the period during which the measure content was or is planned to be in
        # active use.
        self.effectivePeriod = None
        # reference to Period: Period

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate measure instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the measure is intended to be
        # used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # descriptive topics related to the content of the measure. topics provide
        # a high-level categorization of the type of the measure that can be
        # useful for filtering and searching.
        self.topic = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a contributor to the content of the measure, including authors, editors,
        # reviewers, and endorsers.
        self.contributor = None
        # type = array
        # reference to Contributor: Contributor

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a copyright statement relating to the measure and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the measure.
        self.copyright = None
        # type = string

        # related artifacts such as additional documentation, justification, or
        # bibliographic references.
        self.relatedArtifact = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # a reference to a library resource containing the formal logic used by
        # the measure.
        self.library = None
        # type = array
        # reference to Reference: identifier

        # notices and disclaimers regarding the use of the measure, or related to
        # intellectual property (such as code systems) referenced by the measure.
        self.disclaimer = None
        # type = string

        # indicates how the calculation is performed for the measure, including
        # proportion, ratio, continuous variable, and cohort. the value set is
        # extensible, allowing additional measure scoring types to be represented.
        self.scoring = None
        # reference to CodeableConcept: CodeableConcept

        # if this is a composite measure, the scoring method used to combine the
        # component measures to determine the composite score.
        self.compositeScoring = None
        # reference to CodeableConcept: CodeableConcept

        # indicates whether the measure is used to examine a process, an outcome
        # over time, a patient-reported outcome, or a structure measure such as
        # utilization.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a description of the risk adjustment factors that may impact the
        # resulting score for the measure and how they may be accounted for when
        # computing and reporting measure results.
        self.riskAdjustment = None
        # type = string

        # describes how to combine the information calculated, based on logic in
        # each of several populations, into one summarized result.
        self.rateAggregation = None
        # type = string

        # provides a succint statement of the need for the measure. usually
        # includes statements pertaining to importance criterion: impact, gap in
        # care, and evidence.
        self.rationale = None
        # type = string

        # provides a summary of relevant clinical guidelines or other clinical
        # recommendations supporting the measure.
        self.clinicalRecommendationStatement = None
        # type = string

        # information on whether an increase or decrease in score is the preferred
        # result (e.g., a higher score indicates better quality or a lower score
        # indicates better quality or quality is whthin a range).
        self.improvementNotation = None
        # type = string

        # provides a description of an individual term used within the measure.
        self.definition = None
        # type = array

        # additional guidance for the measure including how it can be used in a
        # clinical context, and the intent of the measure.
        self.guidance = None
        # type = string

        # the measure set, e.g. preventive care and screening.
        self.set = None
        # type = string

        # a group of population criteria for the measure.
        self.group = None
        # type = array
        # reference to Measure_Group: identifier

        # the supplemental data criteria for the measure report, specified as
        # either the name of a valid cql expression within a referenced library,
        # or a valid fhir resource path.
        self.supplementalData = None
        # type = array
        # reference to Measure_SupplementalData: identifier

        # a formal identifier that is used to identify this measure when it is
        # represented in other formats, or referenced in a specification, model,
        # design or an instance.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'topic'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'contributor'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'useContext'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'scoring'},

            {'parent_entity': 'Measure_Group',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'group'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'type'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'identifier'},

            {'parent_entity': 'Measure_SupplementalData',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'supplementalData'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'contact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Measure',
             'child_variable': 'library'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Measure',
             'child_variable': 'compositeScoring'},
        ]


class Measure_Group(fhirbase):
    """The Measure resource provides the definition of a quality measure.
    """

    def __init__(self, dict_values=None):
        # optional name or short description of this group.
        self.name = None
        # type = string

        # the human readable description of this population group.
        self.description = None
        # type = string

        # a population criteria for the measure.
        self.population = None
        # type = array
        # reference to Measure_Population: identifier

        # the stratifier criteria for the measure report, specified as either the
        # name of a valid cql expression defined within a referenced library, or a
        # valid fhir resource path.
        self.stratifier = None
        # type = array
        # reference to Measure_Stratifier: identifier

        # a unique identifier for the group. this identifier will used to report
        # data for the group in the measure report.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Measure_Stratifier',
             'parent_variable': 'identifier',
             'child_entity': 'Measure_Group',
             'child_variable': 'stratifier'},

            {'parent_entity': 'Measure_Population',
             'parent_variable': 'identifier',
             'child_entity': 'Measure_Group',
             'child_variable': 'population'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Measure_Group',
             'child_variable': 'identifier'},
        ]


class Measure_Population(fhirbase):
    """The Measure resource provides the definition of a quality measure.
    """

    def __init__(self, dict_values=None):
        # the type of population criteria.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # optional name or short description of this population.
        self.name = None
        # type = string

        # the human readable description of this population criteria.
        self.description = None
        # type = string

        # the name of a valid referenced cql expression (may be namespaced) that
        # defines this population criteria.
        self.criteria = None
        # type = string

        # a unique identifier for the population criteria. this identifier is used
        # to report data against this criteria within the measure report.
        self.identifier = None
        # reference to Identifier: Identifier

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
    """The Measure resource provides the definition of a quality measure.
    """

    def __init__(self, dict_values=None):
        # the criteria for the stratifier. this must be the name of an expression
        # defined within a referenced library.
        self.criteria = None
        # type = string

        # the path to an element that defines the stratifier, specified as a valid
        # fhir resource path.
        self.path = None
        # type = string

        # the identifier for the stratifier used to coordinate the reported data
        # back to this stratifier.
        self.identifier = None
        # reference to Identifier: Identifier

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
    """The Measure resource provides the definition of a quality measure.
    """

    def __init__(self, dict_values=None):
        # an indicator of the intended usage for the supplemental data element.
        # supplemental data indicates the data is additional information requested
        # to augment the measure information. risk adjustment factor indicates the
        # data is additional information used to calculate risk adjustment factors
        # when applying a risk model to the measure calculation.
        self.usage = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the criteria for the supplemental data. this must be the name of a valid
        # expression defined within a referenced library, and defines the data to
        # be returned for this element.
        self.criteria = None
        # type = string

        # the supplemental data to be supplied as part of the measure response,
        # specified as a valid fhir resource path.
        self.path = None
        # type = string

        # an identifier for the supplemental data.
        self.identifier = None
        # reference to Identifier: Identifier

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
