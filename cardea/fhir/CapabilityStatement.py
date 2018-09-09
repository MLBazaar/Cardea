from .fhirbase import fhirbase


class CapabilityStatement(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # this is a capabilitystatement resource
        self.resourceType = 'CapabilityStatement'
        # type = string
        # possible values: CapabilityStatement

        # an absolute uri that is used to identify this capability statement when
        # it is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this capability statement is (or will be) published. the url
        # should include the major version of the capability statement. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the capability
        # statement when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the capability statement
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the capability statement. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the capability statement.
        self.title = None
        # type = string

        # the status of this capability statement. enables tracking the life-cycle
        # of the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this capability statement is authored
        # for testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the capability statement was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the capability statement changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the capability
        # statement.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the capability statement
        # from a consumer's perspective. typically, this is used when the
        # capability statement describes a desired rather than an actual solution,
        # for example as a formal expression of requirements as part of an rfp.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate capability statement instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the capability statement is
        # intended to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this capability statement is needed and why it has
        # been designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the capability statement and/or its
        # contents. copyright statements are generally legal restrictions on the
        # use and publishing of the capability statement.
        self.copyright = None
        # type = string

        # the way that this statement is intended to be used, to describe an
        # actual running instance of software, a particular product (kind not
        # instance of software) or a class of implementation (e.g. a desired
        # purchase).
        self.kind = None
        # type = string
        # possible values: instance, capability, requirements

        # reference to a canonical url of another capabilitystatement that this
        # software implements or uses. this capability statement is a published
        # api description that corresponds to a business service. the rest of the
        # capability statement does not need to repeat the details of the
        # referenced resource, but can do so.
        self.instantiates = None
        # type = array

        # software that is covered by this capability statement.  it is used when
        # the capability statement describes the capabilities of a particular
        # software version, independent of an installation.
        self.software = None
        # reference to CapabilityStatement_Software: CapabilityStatement_Software

        # identifies a specific implementation instance that is described by the
        # capability statement - i.e. a particular installation, rather than the
        # capabilities of a software program.
        self.implementation = None
        # reference to CapabilityStatement_Implementation: CapabilityStatement_Implementation

        # the version of the fhir specification on which this capability statement
        # is based.
        self.fhirVersion = None
        # type = string

        # a code that indicates whether the application accepts unknown elements
        # or extensions when reading resources.
        self.acceptUnknown = None
        # type = string
        # possible values: no, extensions, elements, both

        # a list of the formats supported by this implementation using their
        # content types.
        self.format = None
        # type = array

        # a list of the patch formats supported by this implementation using their
        # content types.
        self.patchFormat = None
        # type = array

        # a list of implementation guides that the server does (or should) support
        # in their entirety.
        self.implementationGuide = None
        # type = array

        # a list of profiles that represent different use cases supported by the
        # system. for a server, "supported by the system" means the system
        # hosts/produces a set of resources that are conformant to a particular
        # profile, and allows clients that use its services to search using this
        # profile and to find appropriate data. for a client, it means the system
        # will search by this profile and process data according to the guidance
        # implicit in the profile. see further discussion in [using
        # profiles](profiling.html#profile-uses).
        self.profile = None
        # type = array
        # reference to Reference: identifier

        # a definition of the restful capabilities of the solution, if any.
        self.rest = None
        # type = array
        # reference to CapabilityStatement_Rest: CapabilityStatement_Rest

        # a description of the messaging capabilities of the solution.
        self.messaging = None
        # type = array
        # reference to CapabilityStatement_Messaging: CapabilityStatement_Messaging

        # a document definition.
        self.document = None
        # type = array
        # reference to CapabilityStatement_Document: CapabilityStatement_Document

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

        if self.kind is not None:
            for value in self.kind:
                if value is not None and value.lower() not in [
                        'instance', 'capability', 'requirements']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'instance, capability, requirements'))

        if self.acceptUnknown is not None:
            for value in self.acceptUnknown:
                if value is not None and value.lower() not in [
                        'no', 'extensions', 'elements', 'both']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'no, extensions, elements, both'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'contact'},

            {'parent_entity': 'CapabilityStatement_Rest',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'rest'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CapabilityStatement_Software',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'software'},

            {'parent_entity': 'CapabilityStatement_Document',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'document'},

            {'parent_entity': 'CapabilityStatement_Implementation',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'implementation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'profile'},

            {'parent_entity': 'CapabilityStatement_Messaging',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'messaging'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'useContext'},
        ]


class CapabilityStatement_Software(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # name software is known by.
        self.name = None
        # type = string

        # the version identifier for the software covered by this statement.
        self.version = None
        # type = string

        # date this version of the software was released.
        self.releaseDate = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class CapabilityStatement_Implementation(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # information about the specific installation that this capability
        # statement relates to.
        self.description = None
        # type = string

        # an absolute base url for the implementation.  this forms the base for
        # rest interfaces as well as the mailbox and document interfaces.
        self.url = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class CapabilityStatement_Rest(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # identifies whether this portion of the statement is describing the
        # ability to initiate or receive restful operations.
        self.mode = None
        # type = string
        # possible values: client, server

        # information about the system's restful capabilities that apply across
        # all applications, such as security.
        self.documentation = None
        # type = string

        # information about security implementation from an interface perspective
        # - what a client needs to know.
        self.security = None
        # reference to CapabilityStatement_Security: CapabilityStatement_Security

        # a specification of the restful capabilities of the solution for a
        # specific resource type.
        self.resource = None
        # type = array
        # reference to CapabilityStatement_Resource: CapabilityStatement_Resource

        # a specification of restful operations supported by the system.
        self.interaction = None
        # type = array
        # reference to CapabilityStatement_Interaction1: CapabilityStatement_Interaction1

        # search parameters that are supported for searching all resources for
        # implementations to support and/or make use of - either references to
        # ones defined in the specification, or additional ones defined for/by the
        # implementation.
        self.searchParam = None
        # type = array
        # reference to CapabilityStatement_SearchParam: CapabilityStatement_SearchParam

        # definition of an operation or a named query together with its parameters
        # and their meaning and type.
        self.operation = None
        # type = array
        # reference to CapabilityStatement_Operation: CapabilityStatement_Operation

        # an absolute uri which is a reference to the definition of a compartment
        # that the system supports. the reference is to a compartmentdefinition
        # resource by its canonical url .
        self.compartment = None
        # type = array

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'client', 'server']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'client, server'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CapabilityStatement_Resource',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'resource'},

            {'parent_entity': 'CapabilityStatement_SearchParam',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'searchParam'},

            {'parent_entity': 'CapabilityStatement_Security',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'security'},

            {'parent_entity': 'CapabilityStatement_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'operation'},

            {'parent_entity': 'CapabilityStatement_Interaction1',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'interaction'},
        ]


class CapabilityStatement_Security(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # server adds cors headers when responding to requests - this enables
        # javascript applications to use the server.
        self.cors = None
        # type = boolean

        # types of security services that are supported/required by the system.
        self.service = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # general description of how security works.
        self.description = None
        # type = string

        # certificates associated with security profiles.
        self.certificate = None
        # type = array
        # reference to CapabilityStatement_Certificate: CapabilityStatement_Certificate

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Security',
             'child_variable': 'service'},

            {'parent_entity': 'CapabilityStatement_Certificate',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Security',
             'child_variable': 'certificate'},
        ]


class CapabilityStatement_Certificate(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # mime type for a certificate.
        self.type = None
        # type = string

        # actual certificate.
        self.blob = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class CapabilityStatement_Resource(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # a type of resource exposed via the restful interface.
        self.type = None
        # type = string

        # a specification of the profile that describes the solution's overall
        # support for the resource, including any constraints on cardinality,
        # bindings, lengths or other limitations. see further discussion in [using
        # profiles](profiling.html#profile-uses).
        self.profile = None
        # reference to Reference: identifier

        # additional information about the resource type used by the system.
        self.documentation = None
        # type = string

        # identifies a restful operation supported by the solution.
        self.interaction = None
        # type = array
        # reference to CapabilityStatement_Interaction: CapabilityStatement_Interaction

        # this field is set to no-version to specify that the system does not
        # support (server) or use (client) versioning for this resource type. if
        # this has some other value, the server must at least correctly track and
        # populate the versionid meta-property on resources. if the value is
        # 'versioned-update', then the server supports all the versioning
        # features, including using e-tags for version integrity in the api.
        self.versioning = None
        # type = string
        # possible values: no-version, versioned, versioned-update

        # a flag for whether the server is able to return past versions as part of
        # the vread operation.
        self.readHistory = None
        # type = boolean

        # a flag to indicate that the server allows or needs to allow the client
        # to create new identities on the server (e.g. that is, the client puts to
        # a location where there is no existing resource). allowing this operation
        # means that the server allows the client to create new identities on the
        # server.
        self.updateCreate = None
        # type = boolean

        # a flag that indicates that the server supports conditional create.
        self.conditionalCreate = None
        # type = boolean

        # a code that indicates how the server supports conditional read.
        self.conditionalRead = None
        # type = string
        # possible values: not-supported, modified-since, not-match,
        # full-support

        # a flag that indicates that the server supports conditional update.
        self.conditionalUpdate = None
        # type = boolean

        # a code that indicates how the server supports conditional delete.
        self.conditionalDelete = None
        # type = string
        # possible values: not-supported, single, multiple

        # a set of flags that defines how references are supported.
        self.referencePolicy = None
        # type = array
        # possible values: literal, logical, resolves, enforced, local

        # a list of _include values supported by the server.
        self.searchInclude = None
        # type = array

        # a list of _revinclude (reverse include) values supported by the server.
        self.searchRevInclude = None
        # type = array

        # search parameters for implementations to support and/or make use of -
        # either references to ones defined in the specification, or additional
        # ones defined for/by the implementation.
        self.searchParam = None
        # type = array
        # reference to CapabilityStatement_SearchParam: CapabilityStatement_SearchParam

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.versioning is not None:
            for value in self.versioning:
                if value is not None and value.lower() not in [
                        'no-version', 'versioned', 'versioned-update']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'no-version, versioned, versioned-update'))

        if self.conditionalRead is not None:
            for value in self.conditionalRead:
                if value is not None and value.lower() not in [
                        'not-supported', 'modified-since', 'not-match', 'full-support']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'not-supported, modified-since, not-match, full-support'))

        if self.conditionalDelete is not None:
            for value in self.conditionalDelete:
                if value is not None and value.lower() not in [
                        'not-supported', 'single', 'multiple']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'not-supported, single, multiple'))

        if self.referencePolicy is not None:
            for value in self.referencePolicy:
                if value is not None and value.lower() not in [
                        'literal', 'logical', 'resolves', 'enforced', 'local']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'literal, logical, resolves, enforced, local'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement_Resource',
             'child_variable': 'profile'},

            {'parent_entity': 'CapabilityStatement_Interaction',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Resource',
             'child_variable': 'interaction'},

            {'parent_entity': 'CapabilityStatement_SearchParam',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Resource',
             'child_variable': 'searchParam'},
        ]


class CapabilityStatement_Interaction(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # coded identifier of the operation, supported by the system resource.
        self.code = None
        # type = string
        # possible values: read, vread, update, patch, delete, history-
        # instance, history-type, create, search-type

        # guidance specific to the implementation of this operation, such as
        # 'delete is a logical delete' or 'updates are only allowed with version
        # id' or 'creates permitted from pre-authorized certificates only'.
        self.documentation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                    'read', 'vread', 'update', 'patch', 'delete', 'history-instance',
                        'history-type', 'create', 'search-type']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'read, vread, update, patch, delete, history-instance,'
                        'history-type, create, search-type'))


class CapabilityStatement_SearchParam(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # the name of the search parameter used in the interface.
        self.name = None
        # type = string

        # an absolute uri that is a formal reference to where this parameter was
        # first defined, so that a client can be confident of the meaning of the
        # search parameter (a reference to [[[searchparameter.url]]]).
        self.definition = None
        # type = string

        # the type of value a search parameter refers to, and how the content is
        # interpreted.
        self.type = None
        # type = string
        # possible values: number, date, string, token, reference,
        # composite, quantity, uri

        # this allows documentation of any distinct behaviors about how the search
        # parameter is used.  for example, text matching algorithms.
        self.documentation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'number', 'date', 'string', 'token', 'reference', 'composite',
                        'quantity', 'uri']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'number, date, string, token, reference, composite, quantity, uri'))


class CapabilityStatement_Interaction1(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # a coded identifier of the operation, supported by the system.
        self.code = None
        # type = string
        # possible values: transaction, batch, search-system, history-
        # system

        # guidance specific to the implementation of this operation, such as
        # limitations on the kind of transactions allowed, or information about
        # system wide search is implemented.
        self.documentation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                        'transaction', 'batch', 'search-system', 'history-system']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'transaction, batch, search-system, history-system'))


class CapabilityStatement_Operation(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # the name of the operation or query. for an operation, this is the name
        # prefixed with $ and used in the url. for a query, this is the name used
        # in the _query parameter when the query is called.
        self.name = None
        # type = string

        # where the formal definition can be found.
        self.definition = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement_Operation',
             'child_variable': 'definition'},
        ]


class CapabilityStatement_Messaging(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # an endpoint (network accessible address) to which messages and/or
        # replies are to be sent.
        self.endpoint = None
        # type = array
        # reference to CapabilityStatement_Endpoint: CapabilityStatement_Endpoint

        # length if the receiver's reliable messaging cache in minutes (if a
        # receiver) or how long the cache length on the receiver should be (if a
        # sender).
        self.reliableCache = None
        # type = int

        # documentation about the system's messaging capabilities for this
        # endpoint not otherwise documented by the capability statement.  for
        # example, the process for becoming an authorized messaging exchange
        # partner.
        self.documentation = None
        # type = string

        # references to message definitions for messages this system can send or
        # receive.
        self.supportedMessage = None
        # type = array
        # reference to CapabilityStatement_SupportedMessage: CapabilityStatement_SupportedMessage

        # a description of the solution's support for an event at this end-point.
        self.event = None
        # type = array
        # reference to CapabilityStatement_Event: CapabilityStatement_Event

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CapabilityStatement_Endpoint',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Messaging',
             'child_variable': 'endpoint'},

            {'parent_entity': 'CapabilityStatement_SupportedMessage',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Messaging',
             'child_variable': 'supportedMessage'},

            {'parent_entity': 'CapabilityStatement_Event',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Messaging',
             'child_variable': 'event'},
        ]


class CapabilityStatement_Endpoint(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # a list of the messaging transport protocol(s) identifiers, supported by
        # this endpoint.
        self.protocol = None
        # reference to Coding: Coding

        # the network address of the end-point. for solutions that do not use
        # network addresses for routing, it can be just an identifier.
        self.address = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Endpoint',
             'child_variable': 'protocol'},
        ]


class CapabilityStatement_SupportedMessage(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # the mode of this event declaration - whether application is sender or
        # receiver.
        self.mode = None
        # type = string
        # possible values: sender, receiver

        # points to a message definition that identifies the messaging event,
        # message structure, allowed responses, etc.
        self.definition = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'sender', 'receiver']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'sender, receiver'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement_SupportedMessage',
             'child_variable': 'definition'},
        ]


class CapabilityStatement_Event(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # a coded identifier of a supported messaging event.
        self.code = None
        # reference to Coding: Coding

        # the impact of the content of the message.
        self.category = None
        # type = string
        # possible values: Consequence, Currency, Notification

        # the mode of this event declaration - whether an application is a sender
        # or receiver.
        self.mode = None
        # type = string
        # possible values: sender, receiver

        # a resource associated with the event.  this is the resource that defines
        # the event.
        self.focus = None
        # type = string

        # information about the request for this event.
        self.request = None
        # reference to Reference: identifier

        # information about the response for this event.
        self.response = None
        # reference to Reference: identifier

        # guidance on how this event is handled, such as internal system trigger
        # points, business rules, etc.
        self.documentation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.category is not None:
            for value in self.category:
                if value is not None and value.lower() not in [
                        'consequence', 'currency', 'notification']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'Consequence, Currency, Notification'))

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'sender', 'receiver']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'sender, receiver'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement_Event',
             'child_variable': 'response'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Event',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement_Event',
             'child_variable': 'request'},
        ]


class CapabilityStatement_Document(fhirbase):
    """A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.
    """

    def __init__(self, dict_values=None):
        # mode of this document declaration - whether an application is a producer
        # or consumer.
        self.mode = None
        # type = string
        # possible values: producer, consumer

        # a description of how the application supports or uses the specified
        # document profile.  for example, when documents are created, what action
        # is taken with consumed documents, etc.
        self.documentation = None
        # type = string

        # a constraint on a resource used in the document.
        self.profile = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'producer', 'consumer']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'producer, consumer'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement_Document',
             'child_variable': 'profile'},
        ]
