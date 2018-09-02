from .fhirbase import fhirbase


class Library(fhirbase):
    """The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as
    well as to describe a collection of knowledge assets.
    """

    def __init__(self, dict_values=None):
        # this is a library resource
        self.resourceType = 'Library'
        # type = string
        # possible values: Library

        # an absolute uri that is used to identify this library when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this library is (or will be) published. the url should include the major
        # version of the library. for more information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the library when
        # it is referenced in a specification, model, design or instance. this is
        # an arbitrary value managed by the library author and is not expected to
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

        # a natural language name identifying the library. this name should be
        # usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the library.
        self.title = None
        # type = string

        # the status of this library. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this library is authored for testing
        # purposes (or education/evaluation/marketing), and is not intended to be
        # used for genuine usage.
        self.experimental = None
        # type = boolean

        # identifies the type of library such as a logic library, model
        # definition, asset collection, or module definition.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the date  (and optionally time) when the library was published. the date
        # must change if and when the business version changes and it must change
        # if the status code changes. in addition, it should change when the
        # substantive content of the library changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the library.
        self.publisher = None
        # type = string

        # a free text natural language description of the library from a
        # consumer's perspective.
        self.description = None
        # type = string

        # explaination of why this library is needed and why it has been designed
        # as it has.
        self.purpose = None
        # type = string

        # a detailed description of how the library is used from a clinical
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

        # the period during which the library content was or is planned to be in
        # active use.
        self.effectivePeriod = None
        # reference to Period: Period

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate library instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the library is intended to be
        # used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # descriptive topics related to the content of the library. topics provide
        # a high-level categorization of the library that can be useful for
        # filtering and searching.
        self.topic = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a contributor to the content of the library, including authors, editors,
        # reviewers, and endorsers.
        self.contributor = None
        # type = array
        # reference to Contributor: Contributor

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a copyright statement relating to the library and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the library.
        self.copyright = None
        # type = string

        # related artifacts such as additional documentation, justification, or
        # bibliographic references.
        self.relatedArtifact = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # the parameter element defines parameters used by the library.
        self.parameter = None
        # type = array
        # reference to ParameterDefinition: ParameterDefinition

        # describes a set of data that must be provided in order to be able to
        # successfully perform the computations defined by the library.
        self.dataRequirement = None
        # type = array
        # reference to DataRequirement: DataRequirement

        # the content of the library as an attachment. the content may be a
        # reference to a url, or may be directly embedded as a base-64 string.
        # either way, the contenttype of the attachment determines how to
        # interpret the content.
        self.content = None
        # type = array
        # reference to Attachment: Attachment

        # a formal identifier that is used to identify this library when it is
        # represented in other formats, or referenced in a specification, model,
        # design or an instance. e.g. cms or nqf identifiers for a measure
        # artifact. note that at least one identifier is required for non-
        # experimental active artifacts.
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
            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'content'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'topic'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'parameter'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'useContext'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'dataRequirement'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'contact'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'contributor'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Library',
             'child_variable': 'jurisdiction'},
        ]
