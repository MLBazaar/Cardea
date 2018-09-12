from .fhirbase import fhirbase


class ServiceDefinition(fhirbase):
    """
    The ServiceDefinition describes a unit of decision support
    functionality that is made available as a service, such as
    immunization modules or drug-drug interaction checking.

    Attributes:
        resourceType: This is a ServiceDefinition resource
        url: An absolute URI that is used to identify this service definition
            when it is referenced in a specification, model, design or an
            instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
            be an address at which this service definition is (or will be)
            published. The URL SHOULD include the major version of the service
            definition. For more information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this service
            definition when it is represented in other formats, or referenced in a
            specification, model, design or an instance. This is used for CMS or
            NQF identifiers for a measure artifact. Note that at least one
            identifier is required for non-experimental active artifacts.
        version: The identifier that is used to identify this version of the
            service definition when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the service
            definition author and is not expected to be globally unique. For
            example, it might be a timestamp (e.g. yyyymmdd) if a managed version
            is not available. There is also no expectation that versions can be
            placed in a lexicographical sequence.
        name: A natural language name identifying the service definition. This
            name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        title: A short, descriptive, user-friendly title for the service
            definition.
        status: The status of this service definition. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this service definition
            is authored for testing purposes (or education/evaluation/marketing),
            and is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the service definition was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the service definition
            changes.
        publisher: The name of the individual or organization that published
            the service definition.
        description: A free text natural language description of the service
            definition from a consumer's perspective.
        purpose: Explaination of why this service definition is needed and why
            it has been designed as it has.
        usage: A detailed description of how the module is used from a
            clinical perspective.
        approvalDate: The date on which the resource content was approved by
            the publisher. Approval happens once when the content is officially
            approved for usage.
        lastReviewDate: The date on which the resource content was last
            reviewed. Review happens periodically after approval, but doesn't
            change the original approval date.
        effectivePeriod: The period during which the service definition
            content was or is planned to be in active use.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate service definition
            instances.
        jurisdiction: A legal or geographic region in which the service
            definition is intended to be used.
        topic: Descriptive topics related to the module. Topics provide a
            high-level categorization of the module that can be useful for
            filtering and searching.
        contributor: A contributor to the content of the module, including
            authors, editors, reviewers, and endorsers.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        copyright: A copyright statement relating to the service definition
            and/or its contents. Copyright statements are generally legal
            restrictions on the use and publishing of the service definition.
        relatedArtifact: Related resources such as additional documentation,
            justification, or bibliographic references.
        trigger: The trigger element defines when the rule should be invoked.
            This information is used by consumers of the rule to determine how to
            integrate the rule into a specific workflow.
        dataRequirement: Data requirements are a machine processable
            description of the data required by the module in order to perform a
            successful evaluation.
        operationDefinition: A reference to the operation that is used to
            invoke this service.
    """

    __name__ = 'ServiceDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'ServiceDefinition'
        # type: string
        # possible values: ServiceDefinition

        self.url = None
        # type: string

        self.version = None
        # type: string

        self.name = None
        # type: string

        self.title = None
        # type: string

        self.status = None
        # type: string
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # type: boolean

        self.date = None
        # type: string

        self.publisher = None
        # type: string

        self.description = None
        # type: string

        self.purpose = None
        # type: string

        self.usage = None
        # type: string

        self.approvalDate = None
        # type: string

        self.lastReviewDate = None
        # type: string

        self.effectivePeriod = None
        # reference to Period

        self.useContext = None
        # type: array
        # reference to UsageContext

        self.jurisdiction = None
        # type: array
        # reference to CodeableConcept

        self.topic = None
        # type: array
        # reference to CodeableConcept

        self.contributor = None
        # type: array
        # reference to Contributor

        self.contact = None
        # type: array
        # reference to ContactDetail

        self.copyright = None
        # type: string

        self.relatedArtifact = None
        # type: array
        # reference to RelatedArtifact

        self.trigger = None
        # type: array
        # reference to TriggerDefinition

        self.dataRequirement = None
        # type: array
        # reference to DataRequirement

        self.operationDefinition = None
        # reference to Reference: identifier

        self.identifier = None
        # type: array
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
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'trigger'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'topic'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'dataRequirement'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ServiceDefinition',
             'child_variable': 'operationDefinition'},
        ]
