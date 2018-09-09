from .fhirbase import fhirbase


class OperationDefinition(fhirbase):
    """
    A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).
    """

    __name__ = 'OperationDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'OperationDefinition'
        """
        This is a OperationDefinition resource

        type: string
        possible values: OperationDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this operation definition
        when it is referenced in a specification, model, design or an
        instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
        be an address at which this operation definition is (or will be)
        published. The URL SHOULD include the major version of the operation
        definition. For more information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the operation
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the operation
        definition author and is not expected to be globally unique. For
        example, it might be a timestamp (e.g. yyyymmdd) if a managed version
        is not available. There is also no expectation that versions can be
        placed in a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the operation definition. This
        name should be usable as an identifier for the module by machine
        processing applications such as code generation.

        type: string
        """

        self.status = None
        """
        The status of this operation definition. Enables tracking the
        life-cycle of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.kind = None
        """
        Whether this is an operation or a named query.

        type: string
        possible values: operation, query
        """

        self.experimental = None
        """
        A boolean value to indicate that this operation definition is authored
        for testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the operation definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the operation definition
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the
        operation definition.

        type: string
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        publisher.

        type: array
        reference to ContactDetail
        """

        self.description = None
        """
        A free text natural language description of the operation definition
        from a consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate operation definition instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the operation definition is
        intended to be used.

        type: array
        reference to CodeableConcept
        """

        self.purpose = None
        """
        Explaination of why this operation definition is needed and why it has
        been designed as it has.

        type: string
        """

        self.idempotent = None
        """
        Operations that are idempotent (see [HTTP specification definition of
        idempotent](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html))
        may be invoked by performing an HTTP GET operation instead of a POST.

        type: boolean
        """

        self.code = None
        """
        The name used to invoke the operation.

        type: string
        """

        self.comment = None
        """
        Additional information about how to use this operation or named query.

        type: string
        """

        self.base = None
        """
        Indicates that this operation definition is a constraining profile on
        the base.

        reference to Reference: identifier
        """

        self.resource = None
        """
        The types on which this operation can be executed.

        type: array
        """

        self.system = None
        """
        Indicates whether this operation or named query can be invoked at the
        system level (e.g. without needing to choose a resource type for the
        context).

        type: boolean
        """

        self.type = None
        """
        Indicates whether this operation or named query can be invoked at the
        resource type level for any given resource type level (e.g. without
        needing to choose a specific resource id for the context).

        type: boolean
        """

        self.instance = None
        """
        Indicates whether this operation can be invoked on a particular
        instance of one of the given types.

        type: boolean
        """

        self.parameter = None
        """
        The parameters for the operation/query.

        type: array
        reference to OperationDefinition_Parameter
        """

        self.overload = None
        """
        Defines an appropriate combination of parameters to use when invoking
        this operation, to help code generators when generating overloaded
        parameter sets for this operation.

        type: array
        reference to OperationDefinition_Overload
        """

        self.object_id = None
        # unique identifier for object class

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
                        'operation', 'query']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'operation, query'))

    def get_relationships(self):

        return [
            {'parent_entity': 'OperationDefinition_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'parameter'},

            {'parent_entity': 'OperationDefinition_Overload',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'overload'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'OperationDefinition',
             'child_variable': 'base'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'jurisdiction'},
        ]


class OperationDefinition_Parameter(fhirbase):
    """
    A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).
    """

    __name__ = 'OperationDefinition_Parameter'

    def __init__(self, dict_values=None):
        self.name = None
        """
        The name of used to identify the parameter.

        type: string
        """

        self.use = None
        """
        Whether this is an input or an output parameter.

        type: string
        possible values: in, out
        """

        self.min = None
        """
        The minimum number of times this parameter SHALL appear in the request
        or response.

        type: int
        """

        self.max = None
        """
        The maximum number of times this element is permitted to appear in the
        request or response.

        type: string
        """

        self.documentation = None
        """
        Describes the meaning or use of this parameter.

        type: string
        """

        self.type = None
        """
        The type for this parameter.

        type: string
        """

        self.searchType = None
        """
        How the parameter is understood as a search parameter. This is only
        used if the parameter type is 'string'.

        type: string
        possible values: number, date, string, token, reference,
        composite, quantity, uri
        """

        self.profile = None
        """
        A profile the specifies the rules that this parameter must conform to.

        reference to Reference: identifier
        """

        self.binding = None
        """
        Binds to a value set if this parameter is coded (code, Coding,
        CodeableConcept).

        reference to OperationDefinition_Binding
        """

        self.part = None
        """
        The parts of a nested Parameter.

        type: array
        reference to OperationDefinition_Parameter
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'OperationDefinition_Parameter',
             'child_variable': 'profile'},

            {'parent_entity': 'OperationDefinition_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition_Parameter',
             'child_variable': 'part'},

            {'parent_entity': 'OperationDefinition_Binding',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition_Parameter',
             'child_variable': 'binding'},
        ]


class OperationDefinition_Binding(fhirbase):
    """
    A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).
    """

    __name__ = 'OperationDefinition_Binding'

    def __init__(self, dict_values=None):
        self.strength = None
        """
        Indicates the degree of conformance expectations associated with this
        binding - that is, the degree to which the provided value set must be
        adhered to in the instances.

        type: string
        possible values: required, extensible, preferred, example
        """

        self.valueSetUri = None
        """
        Points to the value set or external definition (e.g. implicit value
        set) that identifies the set of codes to be used.

        type: string
        """

        self.valueSetReference = None
        """
        Points to the value set or external definition (e.g. implicit value
        set) that identifies the set of codes to be used.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
    """

    __name__ = 'OperationDefinition_Overload'

    def __init__(self, dict_values=None):
        self.parameterName = None
        """
        Name of parameter to include in overload.

        type: array
        """

        self.comment = None
        """
        Comments to go on overload.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
