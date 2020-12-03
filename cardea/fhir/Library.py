from .fhirbase import fhirbase


class Library(fhirbase):
    """
    The Library resource is a general-purpose container for knowledge
    asset definitions. It can be used to describe and expose existing
    knowledge assets such as logic libraries and information model
    descriptions, as well as to describe a collection of knowledge assets.

    Args:
        resourceType: This is a Library resource
        url: An absolute URI that is used to identify this library when it is
            referenced in a specification, model, design or an instance. This
            SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
            which this library is (or will be) published. The URL SHOULD include
            the major version of the library. For more information see [Technical
            and Business Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this library
            when it is represented in other formats, or referenced in a
            specification, model, design or an instance. e.g. CMS or NQF
            identifiers for a measure artifact. Note that at least one identifier
            is required for non-experimental active artifacts.
        version: The identifier that is used to identify this version of the
            library when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the library author and
            is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There
            is also no expectation that versions can be placed in a
            lexicographical sequence. To provide a version consistent with the
            Decision Support Service specification, use the format
            Major.Minor.Revision (e.g. 1.0.0). For more information on versioning
            knowledge assets, refer to the Decision Support Service specification.
            Note that a version is required for non-experimental active artifacts.
        name: A natural language name identifying the library. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the library.
        status: The status of this library. Enables tracking the life-cycle of
            the content.
        experimental: A boolean value to indicate that this library is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        type: Identifies the type of library such as a Logic Library, Model
            Definition, Asset Collection, or Module Definition.
        date: The date  (and optionally time) when the library was published.
            The date must change if and when the business version changes and it
            must change if the status code changes. In addition, it should change
            when the substantive content of the library changes.
        publisher: The name of the individual or organization that published
            the library.
        description: A free text natural language description of the library
            from a consumer's perspective.
        purpose: Explaination of why this library is needed and why it has
            been designed as it has.
        usage: A detailed description of how the library is used from a
            clinical perspective.
        approvalDate: The date on which the resource content was approved by
            the publisher. Approval happens once when the content is officially
            approved for usage.
        lastReviewDate: The date on which the resource content was last
            reviewed. Review happens periodically after approval, but doesn't
            change the original approval date.
        effectivePeriod: The period during which the library content was or is
            planned to be in active use.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate library instances.
        jurisdiction: A legal or geographic region in which the library is
            intended to be used.
        topic: Descriptive topics related to the content of the library.
            Topics provide a high-level categorization of the library that can be
            useful for filtering and searching.
        contributor: A contributor to the content of the library, including
            authors, editors, reviewers, and endorsers.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        copyright: A copyright statement relating to the library and/or its
            contents. Copyright statements are generally legal restrictions on the
            use and publishing of the library.
        relatedArtifact: Related artifacts such as additional documentation,
            justification, or bibliographic references.
        parameter: The parameter element defines parameters used by the
            library.
        dataRequirement: Describes a set of data that must be provided in
            order to be able to successfully perform the computations defined by
            the library.
        content: The content of the library as an Attachment. The content may
            be a reference to a url, or may be directly embedded as a base-64
            string. Either way, the contentType of the attachment determines how
            to interpret the content.
    """

    __name__ = 'Library'

    def __init__(self, dict_values=None):
        self.resourceType = 'Library'
        # type: str
        # possible values: Library

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

        self.type = None
        # reference to CodeableConcept

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

        self.parameter = None
        # type: list
        # reference to ParameterDefinition

        self.dataRequirement = None
        # type: list
        # reference to DataRequirement

        self.content = None
        # type: list
        # reference to Attachment

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
            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'contributor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'type'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'identifier'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'parameter'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'topic'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'dataRequirement'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'content'},
        ]
