from .fhirbase import fhirbase


class OperationDefinition(fhirbase):
    """A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).
    """

    def __init__(self, dict_values=None):
        # this is a operationdefinition resource
        self.resourceType = 'OperationDefinition'
        # type = string
        # possible values: OperationDefinition

        # an absolute uri that is used to identify this operation definition when
        # it is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this operation definition is (or will be) published. the url
        # should include the major version of the operation definition. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the operation
        # definition when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the operation definition
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the operation definition. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # the status of this operation definition. enables tracking the life-cycle
        # of the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # whether this is an operation or a named query.
        self.kind = None
        # type = string
        # possible values: operation, query

        # a boolean value to indicate that this operation definition is authored
        # for testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the operation definition was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the operation definition changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the operation
        # definition.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the operation definition
        # from a consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate operation definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the operation definition is
        # intended to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this operation definition is needed and why it has
        # been designed as it has.
        self.purpose = None
        # type = string

        # operations that are idempotent (see [http specification definition of
        # idempotent](http://www.w3.org/protocols/rfc2616/rfc2616-sec9.html)) may
        # be invoked by performing an http get operation instead of a post.
        self.idempotent = None
        # type = boolean

        # the name used to invoke the operation.
        self.code = None
        # type = string

        # additional information about how to use this operation or named query.
        self.comment = None
        # type = string

        # indicates that this operation definition is a constraining profile on
        # the base.
        self.base = None
        # reference to Reference: identifier

        # the types on which this operation can be executed.
        self.resource = None
        # type = array

        # indicates whether this operation or named query can be invoked at the
        # system level (e.g. without needing to choose a resource type for the
        # context).
        self.system = None
        # type = boolean

        # indicates whether this operation or named query can be invoked at the
        # resource type level for any given resource type level (e.g. without
        # needing to choose a specific resource id for the context).
        self.type = None
        # type = boolean

        # indicates whether this operation can be invoked on a particular instance
        # of one of the given types.
        self.instance = None
        # type = boolean

        # the parameters for the operation/query.
        self.parameter = None
        # type = array
        # reference to OperationDefinition_Parameter: OperationDefinition_Parameter

        # defines an appropriate combination of parameters to use when invoking
        # this operation, to help code generators when generating overloaded
        # parameter sets for this operation.
        self.overload = None
        # type = array
        # reference to OperationDefinition_Overload: OperationDefinition_Overload

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
                        'operation', 'query']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'operation, query'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'OperationDefinition',
             'child_variable': 'jurisdiction'},

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
        ]


class OperationDefinition_Parameter(fhirbase):
    """A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).
    """

    def __init__(self, dict_values=None):
        # the name of used to identify the parameter.
        self.name = None
        # type = string

        # whether this is an input or an output parameter.
        self.use = None
        # type = string
        # possible values: in, out

        # the minimum number of times this parameter shall appear in the request
        # or response.
        self.min = None
        # type = int

        # the maximum number of times this element is permitted to appear in the
        # request or response.
        self.max = None
        # type = string

        # describes the meaning or use of this parameter.
        self.documentation = None
        # type = string

        # the type for this parameter.
        self.type = None
        # type = string

        # how the parameter is understood as a search parameter. this is only used
        # if the parameter type is 'string'.
        self.searchType = None
        # type = string
        # possible values: number, date, string, token, reference,
        # composite, quantity, uri

        # a profile the specifies the rules that this parameter must conform to.
        self.profile = None
        # reference to Reference: identifier

        # binds to a value set if this parameter is coded (code, coding,
        # codeableconcept).
        self.binding = None
        # reference to OperationDefinition_Binding: OperationDefinition_Binding

        # the parts of a nested parameter.
        self.part = None
        # type = array
        # reference to OperationDefinition_Parameter: OperationDefinition_Parameter

        # unique identifier for object class
        self.object_id = None

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
    """A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).
    """

    def __init__(self, dict_values=None):
        # indicates the degree of conformance expectations associated with this
        # binding - that is, the degree to which the provided value set must be
        # adhered to in the instances.
        self.strength = None
        # type = string
        # possible values: required, extensible, preferred, example

        # points to the value set or external definition (e.g. implicit value set)
        # that identifies the set of codes to be used.
        self.valueSetUri = None
        # type = string

        # points to the value set or external definition (e.g. implicit value set)
        # that identifies the set of codes to be used.
        self.valueSetReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
    """A formal computable definition of an operation (on the RESTful
    interface) or a named query (using the search interaction).
    """

    def __init__(self, dict_values=None):
        # name of parameter to include in overload.
        self.parameterName = None
        # type = array

        # comments to go on overload.
        self.comment = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
