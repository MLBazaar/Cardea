from .fhirbase import fhirbase


class CapabilityStatement(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        resourceType: This is a CapabilityStatement resource
        url: An absolute URI that is used to identify this capability
            statement when it is referenced in a specification, model, design or
            an instance. This SHALL be a URL, SHOULD be globally unique, and
            SHOULD be an address at which this capability statement is (or will
            be) published. The URL SHOULD include the major version of the
            capability statement. For more information see [Technical and Business
            Versions](resource.html#versions).
        version: The identifier that is used to identify this version of the
            capability statement when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the
            capability statement author and is not expected to be globally unique.
            For example, it might be a timestamp (e.g. yyyymmdd) if a managed
            version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.
        name: A natural language name identifying the capability statement.
            This name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        title: A short, descriptive, user-friendly title for the capability
            statement.
        status: The status of this capability statement. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this capability
            statement is authored for testing purposes (or
            education/evaluation/marketing), and is not intended to be used for
            genuine usage.
        date: The date  (and optionally time) when the capability statement
            was published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the capability statement
            changes.
        publisher: The name of the individual or organization that published
            the capability statement.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the
            capability statement from a consumer's perspective. Typically, this is
            used when the capability statement describes a desired rather than an
            actual solution, for example as a formal expression of requirements as
            part of an RFP.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate capability
            statement instances.
        jurisdiction: A legal or geographic region in which the capability
            statement is intended to be used.
        purpose: Explaination of why this capability statement is needed and
            why it has been designed as it has.
        copyright: A copyright statement relating to the capability statement
            and/or its contents. Copyright statements are generally legal
            restrictions on the use and publishing of the capability statement.
        kind: The way that this statement is intended to be used, to describe
            an actual running instance of software, a particular product (kind not
            instance of software) or a class of implementation (e.g. a desired
            purchase).
        instantiates: Reference to a canonical URL of another
            CapabilityStatement that this software implements or uses. This
            capability statement is a published API description that corresponds
            to a business service. The rest of the capability statement does not
            need to repeat the details of the referenced resource, but can do so.
        software: Software that is covered by this capability statement.  It
            is used when the capability statement describes the capabilities of a
            particular software version, independent of an installation.
        implementation: Identifies a specific implementation instance that is
            described by the capability statement - i.e. a particular
            installation, rather than the capabilities of a software program.
        fhirVersion: The version of the FHIR specification on which this
            capability statement is based.
        acceptUnknown: A code that indicates whether the application accepts
            unknown elements or extensions when reading resources.
        format: A list of the formats supported by this implementation using
            their content types.
        patchFormat: A list of the patch formats supported by this
            implementation using their content types.
        implementationGuide: A list of implementation guides that the server
            does (or should) support in their entirety.
        profile: A list of profiles that represent different use cases
            supported by the system. For a server, "supported by the system" means
            the system hosts/produces a set of resources that are conformant to a
            particular profile, and allows clients that use its services to search
            using this profile and to find appropriate data. For a client, it
            means the system will search by this profile and process data
            according to the guidance implicit in the profile. See further
            discussion in [Using Profiles](profiling.html#profile-uses).
        rest: A definition of the restful capabilities of the solution, if
            any.
        messaging: A description of the messaging capabilities of the
            solution.
        document: A document definition.
    """

    __name__ = 'CapabilityStatement'

    def __init__(self, dict_values=None):
        self.resourceType = 'CapabilityStatement'
        # type: str
        # possible values: CapabilityStatement

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

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.description = None
        # type: str

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.purpose = None
        # type: str

        self.copyright = None
        # type: str

        self.kind = None
        # type: str
        # possible values: instance, capability, requirements

        self.instantiates = None
        # type: list

        self.software = None
        # reference to CapabilityStatement_Software

        self.implementation = None
        # reference to CapabilityStatement_Implementation

        self.fhirVersion = None
        # type: str

        self.acceptUnknown = None
        # type: str
        # possible values: no, extensions, elements, both

        self.format = None
        # type: list

        self.patchFormat = None
        # type: list

        self.implementationGuide = None
        # type: list

        self.profile = None
        # type: list
        # reference to Reference: identifier

        self.rest = None
        # type: list
        # reference to CapabilityStatement_Rest

        self.messaging = None
        # type: list
        # reference to CapabilityStatement_Messaging

        self.document = None
        # type: list
        # reference to CapabilityStatement_Document

        self.object_id = None
        # unique identifier for object class

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
            {'parent_entity': 'CapabilityStatement_Rest',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'rest'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'contact'},

            {'parent_entity': 'CapabilityStatement_Software',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'software'},

            {'parent_entity': 'CapabilityStatement_Implementation',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'implementation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'profile'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CapabilityStatement_Document',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement',
             'child_variable': 'document'},

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
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        name: Name software is known by.
        version: The version identifier for the software covered by this
            statement.
        releaseDate: Date this version of the software was released.
    """

    __name__ = 'CapabilityStatement_Software'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.version = None
        # type: str

        self.releaseDate = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class CapabilityStatement_Implementation(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        description: Information about the specific installation that this
            capability statement relates to.
        url: An absolute base URL for the implementation.  This forms the base
            for REST interfaces as well as the mailbox and document interfaces.
    """

    __name__ = 'CapabilityStatement_Implementation'

    def __init__(self, dict_values=None):
        self.description = None
        # type: str

        self.url = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class CapabilityStatement_Rest(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        mode: Identifies whether this portion of the statement is describing
            the ability to initiate or receive restful operations.
        documentation: Information about the system's restful capabilities
            that apply across all applications, such as security.
        security: Information about security implementation from an interface
            perspective - what a client needs to know.
        resource: A specification of the restful capabilities of the solution
            for a specific resource type.
        interaction: A specification of restful operations supported by the
            system.
        searchParam: Search parameters that are supported for searching all
            resources for implementations to support and/or make use of - either
            references to ones defined in the specification, or additional ones
            defined for/by the implementation.
        operation: Definition of an operation or a named query together with
            its parameters and their meaning and type.
        compartment: An absolute URI which is a reference to the definition of
            a compartment that the system supports. The reference is to a
            CompartmentDefinition resource by its canonical URL .
    """

    __name__ = 'CapabilityStatement_Rest'

    def __init__(self, dict_values=None):
        self.mode = None
        # type: str
        # possible values: client, server

        self.documentation = None
        # type: str

        self.security = None
        # reference to CapabilityStatement_Security

        self.resource = None
        # type: list
        # reference to CapabilityStatement_Resource

        self.interaction = None
        # type: list
        # reference to CapabilityStatement_Interaction1

        self.searchParam = None
        # type: list
        # reference to CapabilityStatement_SearchParam

        self.operation = None
        # type: list
        # reference to CapabilityStatement_Operation

        self.compartment = None
        # type: list

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'client', 'server']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'client, server'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CapabilityStatement_SearchParam',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'searchParam'},

            {'parent_entity': 'CapabilityStatement_Interaction1',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'interaction'},

            {'parent_entity': 'CapabilityStatement_Security',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'security'},

            {'parent_entity': 'CapabilityStatement_Resource',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'resource'},

            {'parent_entity': 'CapabilityStatement_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Rest',
             'child_variable': 'operation'},
        ]


class CapabilityStatement_Security(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        cors: Server adds CORS headers when responding to requests - this
            enables javascript applications to use the server.
        service: Types of security services that are supported/required by the
            system.
        description: General description of how security works.
        certificate: Certificates associated with security profiles.
    """

    __name__ = 'CapabilityStatement_Security'

    def __init__(self, dict_values=None):
        self.cors = None
        # type: bool

        self.service = None
        # type: list
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.certificate = None
        # type: list
        # reference to CapabilityStatement_Certificate

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CapabilityStatement_Certificate',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Security',
             'child_variable': 'certificate'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Security',
             'child_variable': 'service'},
        ]


class CapabilityStatement_Certificate(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        type: Mime type for a certificate.
        blob: Actual certificate.
    """

    __name__ = 'CapabilityStatement_Certificate'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str

        self.blob = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class CapabilityStatement_Resource(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        type: A type of resource exposed via the restful interface.
        profile: A specification of the profile that describes the solution's
            overall support for the resource, including any constraints on
            cardinality, bindings, lengths or other limitations. See further
            discussion in [Using Profiles](profiling.html#profile-uses).
        documentation: Additional information about the resource type used by
            the system.
        interaction: Identifies a restful operation supported by the solution.
        versioning: This field is set to no-version to specify that the system
            does not support (server) or use (client) versioning for this resource
            type. If this has some other value, the server must at least correctly
            track and populate the versionId meta-property on resources. If the
            value is 'versioned-update', then the server supports all the
            versioning features, including using e-tags for version integrity in
            the API.
        readHistory: A flag for whether the server is able to return past
            versions as part of the vRead operation.
        updateCreate: A flag to indicate that the server allows or needs to
            allow the client to create new identities on the server (e.g. that is,
            the client PUTs to a location where there is no existing resource).
            Allowing this operation means that the server allows the client to
            create new identities on the server.
        conditionalCreate: A flag that indicates that the server supports
            conditional create.
        conditionalRead: A code that indicates how the server supports
            conditional read.
        conditionalUpdate: A flag that indicates that the server supports
            conditional update.
        conditionalDelete: A code that indicates how the server supports
            conditional delete.
        referencePolicy: A set of flags that defines how references are
            supported.
        searchInclude: A list of _include values supported by the server.
        searchRevInclude: A list of _revinclude (reverse include) values
            supported by the server.
        searchParam: Search parameters for implementations to support and/or
            make use of - either references to ones defined in the specification,
            or additional ones defined for/by the implementation.
    """

    __name__ = 'CapabilityStatement_Resource'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str

        self.profile = None
        # reference to Reference: identifier

        self.documentation = None
        # type: str

        self.interaction = None
        # type: list
        # reference to CapabilityStatement_Interaction

        self.versioning = None
        # type: str
        # possible values: no-version, versioned, versioned-update

        self.readHistory = None
        # type: bool

        self.updateCreate = None
        # type: bool

        self.conditionalCreate = None
        # type: bool

        self.conditionalRead = None
        # type: str
        # possible values: not-supported, modified-since, not-match,
        # full-support

        self.conditionalUpdate = None
        # type: bool

        self.conditionalDelete = None
        # type: str
        # possible values: not-supported, single, multiple

        self.referencePolicy = None
        # type: list
        # possible values: literal, logical, resolves, enforced, local

        self.searchInclude = None
        # type: list

        self.searchRevInclude = None
        # type: list

        self.searchParam = None
        # type: list
        # reference to CapabilityStatement_SearchParam

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

            {'parent_entity': 'CapabilityStatement_SearchParam',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Resource',
             'child_variable': 'searchParam'},

            {'parent_entity': 'CapabilityStatement_Interaction',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Resource',
             'child_variable': 'interaction'},
        ]


class CapabilityStatement_Interaction(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        code: Coded identifier of the operation, supported by the system
            resource.
        documentation: Guidance specific to the implementation of this
            operation, such as 'delete is a logical delete' or 'updates are only
            allowed with version id' or 'creates permitted from pre-authorized
            certificates only'.
    """

    __name__ = 'CapabilityStatement_Interaction'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str
        # possible values: read, vread, update, patch, delete,
        # history-instance, history-type, create, search-type

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                    'read', 'vread', 'update', 'patch', 'delete', 'history-instance',
                        'history-type', 'create', 'search-type']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'read, vread, update, patch, delete, history-instance, '
                        'history-type, create, search-type'))


class CapabilityStatement_SearchParam(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        name: The name of the search parameter used in the interface.
        definition: An absolute URI that is a formal reference to where this
            parameter was first defined, so that a client can be confident of the
            meaning of the search parameter (a reference to
            [[[SearchParameter.url]]]).
        type: The type of value a search parameter refers to, and how the
            content is interpreted.
        documentation: This allows documentation of any distinct behaviors
            about how the search parameter is used.  For example, text matching
            algorithms.
    """

    __name__ = 'CapabilityStatement_SearchParam'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.definition = None
        # type: str

        self.type = None
        # type: str
        # possible values: number, date, string, token, reference,
        # composite, quantity, uri

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'number', 'date', 'string', 'token', 'reference', 'composite',
                        'quantity', 'uri']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'number, date, string, token, reference, composite, quantity, uri'))


class CapabilityStatement_Interaction1(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        code: A coded identifier of the operation, supported by the system.
        documentation: Guidance specific to the implementation of this
            operation, such as limitations on the kind of transactions allowed, or
            information about system wide search is implemented.
    """

    __name__ = 'CapabilityStatement_Interaction1'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str
        # possible values: transaction, batch, search-system,
        # history-system

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                        'transaction', 'batch', 'search-system', 'history-system']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'transaction, batch, search-system, history-system'))


class CapabilityStatement_Operation(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        name: The name of the operation or query. For an operation, this is
            the name  prefixed with $ and used in the URL. For a query, this is
            the name used in the _query parameter when the query is called.
        definition: Where the formal definition can be found.
    """

    __name__ = 'CapabilityStatement_Operation'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.definition = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        endpoint: An endpoint (network accessible address) to which messages
            and/or replies are to be sent.
        reliableCache: Length if the receiver's reliable messaging cache in
            minutes (if a receiver) or how long the cache length on the receiver
            should be (if a sender).
        documentation: Documentation about the system's messaging capabilities
            for this endpoint not otherwise documented by the capability
            statement.  For example, the process for becoming an authorized
            messaging exchange partner.
        supportedMessage: References to message definitions for messages this
            system can send or receive.
        event: A description of the solution's support for an event at this
            end-point.
    """

    __name__ = 'CapabilityStatement_Messaging'

    def __init__(self, dict_values=None):
        self.endpoint = None
        # type: list
        # reference to CapabilityStatement_Endpoint

        self.reliableCache = None
        # type: int

        self.documentation = None
        # type: str

        self.supportedMessage = None
        # type: list
        # reference to CapabilityStatement_SupportedMessage

        self.event = None
        # type: list
        # reference to CapabilityStatement_Event

        self.object_id = None
        # unique identifier for object class

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
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        protocol: A list of the messaging transport protocol(s) identifiers,
            supported by this endpoint.
        address: The network address of the end-point. For solutions that do
            not use network addresses for routing, it can be just an identifier.
    """

    __name__ = 'CapabilityStatement_Endpoint'

    def __init__(self, dict_values=None):
        self.protocol = None
        # reference to Coding

        self.address = None
        # type: str

        self.object_id = None
        # unique identifier for object class

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
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        mode: The mode of this event declaration - whether application is
            sender or receiver.
        definition: Points to a message definition that identifies the
            messaging event, message structure, allowed responses, etc.
    """

    __name__ = 'CapabilityStatement_SupportedMessage'

    def __init__(self, dict_values=None):
        self.mode = None
        # type: str
        # possible values: sender, receiver

        self.definition = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        code: A coded identifier of a supported messaging event.
        category: The impact of the content of the message.
        mode: The mode of this event declaration - whether an application is a
            sender or receiver.
        focus: A resource associated with the event.  This is the resource
            that defines the event.
        request: Information about the request for this event.
        response: Information about the response for this event.
        documentation: Guidance on how this event is handled, such as internal
            system trigger points, business rules, etc.
    """

    __name__ = 'CapabilityStatement_Event'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to Coding

        self.category = None
        # type: str
        # possible values: Consequence, Currency, Notification

        self.mode = None
        # type: str
        # possible values: sender, receiver

        self.focus = None
        # type: str

        self.request = None
        # reference to Reference: identifier

        self.response = None
        # reference to Reference: identifier

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CapabilityStatement_Event',
             'child_variable': 'response'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'CapabilityStatement_Event',
             'child_variable': 'code'},
        ]


class CapabilityStatement_Document(fhirbase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of
    a FHIR Server that may be used as a statement of actual server
    functionality or a statement of required or desired server
    implementation.

    Args:
        mode: Mode of this document declaration - whether an application is a
            producer or consumer.
        documentation: A description of how the application supports or uses
            the specified document profile.  For example, when documents are
            created, what action is taken with consumed documents, etc.
        profile: A constraint on a resource used in the document.
    """

    __name__ = 'CapabilityStatement_Document'

    def __init__(self, dict_values=None):
        self.mode = None
        # type: str
        # possible values: producer, consumer

        self.documentation = None
        # type: str

        self.profile = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
