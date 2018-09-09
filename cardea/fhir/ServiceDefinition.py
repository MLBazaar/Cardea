from .fhirbase import fhirbase


class ServiceDefinition(fhirbase):
    """
    The ServiceDefinition describes a unit of decision support
    functionality that is made available as a service, such as
    immunization modules or drug-drug interaction checking.
    """

    __name__ = 'ServiceDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'ServiceDefinition'
        """
        This is a ServiceDefinition resource

        type: string
        possible values: ServiceDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this service definition when
        it is referenced in a specification, model, design or an instance.
        This SHALL be a URL, SHOULD be globally unique, and SHOULD be an
        address at which this service definition is (or will be) published.
        The URL SHOULD include the major version of the service definition.
        For more information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the service
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the service definition
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the service definition. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the service definition.

        type: string
        """

        self.status = None
        """
        The status of this service definition. Enables tracking the life-cycle
        of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this service definition is authored
        for testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the service definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the service definition
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the service
        definition.

        type: string
        """

        self.description = None
        """
        A free text natural language description of the service definition
        from a consumer's perspective.

        type: string
        """

        self.purpose = None
        """
        Explaination of why this service definition is needed and why it has
        been designed as it has.

        type: string
        """

        self.usage = None
        """
        A detailed description of how the module is used from a clinical
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
        The period during which the service definition content was or is
        planned to be in active use.

        reference to Period
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate service definition instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the service definition is
        intended to be used.

        type: array
        reference to CodeableConcept
        """

        self.topic = None
        """
        Descriptive topics related to the module. Topics provide a high-level
        categorization of the module that can be useful for filtering and
        searching.

        type: array
        reference to CodeableConcept
        """

        self.contributor = None
        """
        A contributor to the content of the module, including authors,
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
        A copyright statement relating to the service definition and/or its
        contents. Copyright statements are generally legal restrictions on the
        use and publishing of the service definition.

        type: string
        """

        self.relatedArtifact = None
        """
        Related resources such as additional documentation, justification, or
        bibliographic references.

        type: array
        reference to RelatedArtifact
        """

        self.trigger = None
        """
        The trigger element defines when the rule should be invoked. This
        information is used by consumers of the rule to determine how to
        integrate the rule into a specific workflow.

        type: array
        reference to TriggerDefinition
        """

        self.dataRequirement = None
        """
        Data requirements are a machine processable description of the data
        required by the module in order to perform a successful evaluation.

        type: array
        reference to DataRequirement
        """

        self.operationDefinition = None
        """
        A reference to the operation that is used to invoke this service.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this service definition
        when it is represented in other formats, or referenced in a
        specification, model, design or an instance. This is used for CMS or
        NQF identifiers for a measure artifact. Note that at least one
        identifier is required for non-experimental active artifacts.

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
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'trigger'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'operationDefinition'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'dataRequirement'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'topic'},
        ]
