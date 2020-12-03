from .fhirbase import fhirbase


class OperationDefinition(fhirbase):
    """
    A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).

    Args:
        resourceType: This is a OperationDefinition resource
        url: An absolute URI that is used to identify this operation
            definition when it is referenced in a specification, model, design or
            an instance. This SHALL be a URL, SHOULD be globally unique, and
            SHOULD be an address at which this operation definition is (or will
            be) published. The URL SHOULD include the major version of the
            operation definition. For more information see [Technical and Business
            Versions](resource.html#versions).
        version: The identifier that is used to identify this version of the
            operation definition when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the
            operation definition author and is not expected to be globally unique.
            For example, it might be a timestamp (e.g. yyyymmdd) if a managed
            version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.
        name: A natural language name identifying the operation definition.
            This name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        status: The status of this operation definition. Enables tracking the
            life-cycle of the content.
        kind: Whether this is an operation or a named query.
        experimental: A boolean value to indicate that this operation
            definition is authored for testing purposes (or
            education/evaluation/marketing), and is not intended to be used for
            genuine usage.
        date: The date  (and optionally time) when the operation definition
            was published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the operation definition
            changes.
        publisher: The name of the individual or organization that published
            the operation definition.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the operation
            definition from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate operation
            definition instances.
        jurisdiction: A legal or geographic region in which the operation
            definition is intended to be used.
        purpose: Explaination of why this operation definition is needed and
            why it has been designed as it has.
        idempotent: Operations that are idempotent (see [HTTP specification
            definition of
            idempotent](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html))
            may be invoked by performing an HTTP GET operation instead of a POST.
        code: The name used to invoke the operation.
        comment: Additional information about how to use this operation or
            named query.
        base: Indicates that this operation definition is a constraining
            profile on the base.
        resource: The types on which this operation can be executed.
        system: Indicates whether this operation or named query can be invoked
            at the system level (e.g. without needing to choose a resource type
            for the context).
        type: Indicates whether this operation or named query can be invoked
            at the resource type level for any given resource type level (e.g.
            without needing to choose a specific resource id for the context).
        instance: Indicates whether this operation can be invoked on a
            particular instance of one of the given types.
        parameter: The parameters for the operation/query.
        overload: Defines an appropriate combination of parameters to use when
            invoking this operation, to help code generators when generating
            overloaded parameter sets for this operation.
    """

    __name__ = 'OperationDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'OperationDefinition'
        # type: str
        # possible values: OperationDefinition

        self.url = None
        # type: str

        self.version = None
        # type: str

        self.name = None
        # type: str

        self.status = None
        # type: str
        # possible values: draft, active, retired, unknown

        self.kind = None
        # type: str
        # possible values: operation, query

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

        self.idempotent = None
        # type: bool

        self.code = None
        # type: str

        self.comment = None
        # type: str

        self.base = None
        # reference to Reference: identifier

        self.resource = None
        # type: list

        self.system = None
        # type: bool

        self.type = None
        # type: bool

        self.instance = None
        # type: bool

        self.parameter = None
        # type: list
        # reference to OperationDefinition_Parameter

        self.overload = None
        # type: list
        # reference to OperationDefinition_Overload

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
                        'operation', 'query']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'operation, query'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'OperationDefinition_Overload',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'overload'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'OperationDefinition',
             'child_variable': 'base'},

            {'parent_entity': 'OperationDefinition_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'parameter'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'useContext'},
        ]


class OperationDefinition_Parameter(fhirbase):
    """
    A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).

    Args:
        name: The name of used to identify the parameter.
        use: Whether this is an input or an output parameter.
        min: The minimum number of times this parameter SHALL appear in the
            request or response.
        max: The maximum number of times this element is permitted to appear
            in the request or response.
        documentation: Describes the meaning or use of this parameter.
        type: The type for this parameter.
        searchType: How the parameter is understood as a search parameter.
            This is only used if the parameter type is 'string'.
        profile: A profile the specifies the rules that this parameter must
            conform to.
        binding: Binds to a value set if this parameter is coded (code,
            Coding, CodeableConcept).
        part: The parts of a nested Parameter.
    """

    __name__ = 'OperationDefinition_Parameter'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.use = None
        # type: str
        # possible values: in, out

        self.min = None
        # type: int

        self.max = None
        # type: str

        self.documentation = None
        # type: str

        self.type = None
        # type: str

        self.searchType = None
        # type: str
        # possible values: number, date, string, token, reference,
        # composite, quantity, uri

        self.profile = None
        # reference to Reference: identifier

        self.binding = None
        # reference to OperationDefinition_Binding

        self.part = None
        # type: list
        # reference to OperationDefinition_Parameter

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.use is not None:
            for value in self.use:
                if value is not None and value.lower() not in [
                        'in', 'out']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'in, out'))

        if self.searchType is not None:
            for value in self.searchType:
                if value is not None and value.lower() not in [
                    'number', 'date', 'string', 'token', 'reference', 'composite',
                        'quantity', 'uri']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'number, date, string, token, reference, composite, quantity, uri'))

        if self.use is not None:
            for value in self.use:
                if value is not None and value.lower() not in [
                        'in', 'out']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'in, out'))

        if self.searchType is not None:
            for value in self.searchType:
                if value is not None and value.lower() not in [
                    'number', 'date', 'string', 'token', 'reference', 'composite',
                        'quantity', 'uri']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'number, date, string, token, reference, composite, quantity, uri'))

    def get_relationships(self):

        return [
            {'parent_entity': 'OperationDefinition_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition_Parameter',
             'child_variable': 'part'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'OperationDefinition_Parameter',
             'child_variable': 'profile'},

            {'parent_entity': 'OperationDefinition_Binding',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition_Parameter',
             'child_variable': 'binding'},
        ]


class OperationDefinition_Binding(fhirbase):
    """
    A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).

    Args:
        strength: Indicates the degree of conformance expectations associated
            with this binding - that is, the degree to which the provided value
            set must be adhered to in the instances.
        valueSetUri: Points to the value set or external definition (e.g.
            implicit value set) that identifies the set of codes to be used.
        valueSetReference: Points to the value set or external definition
            (e.g. implicit value set) that identifies the set of codes to be used.
    """

    __name__ = 'OperationDefinition_Binding'

    def __init__(self, dict_values=None):
        self.strength = None
        # type: str
        # possible values: required, extensible, preferred, example

        self.valueSetUri = None
        # type: str

        self.valueSetReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.strength is not None:
            for value in self.strength:
                if value is not None and value.lower() not in [
                        'required', 'extensible', 'preferred', 'example']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'required, extensible, preferred, example'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'OperationDefinition_Binding',
             'child_variable': 'valueSetReference'},
        ]


class OperationDefinition_Overload(fhirbase):
    """
    A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).

    Args:
        parameterName: Name of parameter to include in overload.
        comment: Comments to go on overload.
    """

    __name__ = 'OperationDefinition_Overload'

    def __init__(self, dict_values=None):
        self.parameterName = None
        # type: list

        self.comment = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
