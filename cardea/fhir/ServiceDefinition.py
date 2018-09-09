from .fhirbase import fhirbase


class ServiceDefinition(fhirbase):
    """The ServiceDefinition describes a unit of decision support functionality
    that is made available as a service, such as immunization modules or
    drug-drug interaction checking.
    """

    def __init__(self, dict_values=None):
        # this is a servicedefinition resource
        self.resourceType = 'ServiceDefinition'
        # type = string
        # possible values: ServiceDefinition

        # an absolute uri that is used to identify this service definition when it
        # is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this service definition is (or will be) published. the url should
        # include the major version of the service definition. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the service
        # definition when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the service definition
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the service definition. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the service definition.
        self.title = None
        # type = string

        # the status of this service definition. enables tracking the life-cycle
        # of the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this service definition is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the service definition was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the service definition changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the service
        # definition.
        self.publisher = None
        # type = string

        # a free text natural language description of the service definition from
        # a consumer's perspective.
        self.description = None
        # type = string

        # explaination of why this service definition is needed and why it has
        # been designed as it has.
        self.purpose = None
        # type = string

        # a detailed description of how the module is used from a clinical
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

        # the period during which the service definition content was or is planned
        # to be in active use.
        self.effectivePeriod = None
        # reference to Period: Period

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate service definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the service definition is intended
        # to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # descriptive topics related to the module. topics provide a high-level
        # categorization of the module that can be useful for filtering and
        # searching.
        self.topic = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a contributor to the content of the module, including authors, editors,
        # reviewers, and endorsers.
        self.contributor = None
        # type = array
        # reference to Contributor: Contributor

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a copyright statement relating to the service definition and/or its
        # contents. copyright statements are generally legal restrictions on the
        # use and publishing of the service definition.
        self.copyright = None
        # type = string

        # related resources such as additional documentation, justification, or
        # bibliographic references.
        self.relatedArtifact = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # the trigger element defines when the rule should be invoked. this
        # information is used by consumers of the rule to determine how to
        # integrate the rule into a specific workflow.
        self.trigger = None
        # type = array
        # reference to TriggerDefinition: TriggerDefinition

        # data requirements are a machine processable description of the data
        # required by the module in order to perform a successful evaluation.
        self.dataRequirement = None
        # type = array
        # reference to DataRequirement: DataRequirement

        # a reference to the operation that is used to invoke this service.
        self.operationDefinition = None
        # reference to Reference: identifier

        # a formal identifier that is used to identify this service definition
        # when it is represented in other formats, or referenced in a
        # specification, model, design or an instance. this is used for cms or nqf
        # identifiers for a measure artifact. note that at least one identifier is
        # required for non-experimental active artifacts.
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
            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'trigger'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'operationDefinition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'dataRequirement'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'topic'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'contributor'},
        ]
