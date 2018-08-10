from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .ContactDetail import ContactDetail
from .UsageContext import UsageContext

class SearchParameter(fhirbase):
    """A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    def __init__(self, dict_values=None):
        # this is a searchparameter resource
        self.resourceType = 'SearchParameter'
        # type = string
        # possible values = SearchParameter

        # an absolute uri that is used to identify this search parameter when it
        # is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this search parameter is (or will be) published. the url should
        # include the major version of the search parameter. for more information
        # see [technical and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the search
        # parameter when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the search parameter
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the search parameter. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # the status of this search parameter. enables tracking the life-cycle of
        # the content.
        self.status = None
        # type = string
        # possible values = draft, active, retired, unknown

        # a boolean value to indicate that this search parameter is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the search parameter was published.
        # the date must change if and when the business version changes and it
        # must change if the status code changes. in addition, it should change
        # when the substantive content of the search parameter changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the search
        # parameter.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate search parameter instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the search parameter is intended
        # to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this search parameter is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # the code used in the url or the parameter name in a parameters resource
        # for this search parameter.
        self.code = None
        # type = string

        # the base resource type(s) that this search parameter can be used
        # against.
        self.base = None
        # type = array

        # the type of value a search parameter refers to, and how the content is
        # interpreted.
        self.type = None
        # type = string
        # possible values = number, date, string, token, reference, composite, quantity, uri

        # where this search parameter is originally defined. if a derivedfrom is
        # provided, then the details in the search parameter must be consistent
        # with the definition from which it is defined. i.e. the parameter should
        # have the same meaning, and (usually) the functionality should be a
        # proper subset of the underlying search parameter.
        self.derivedFrom = None
        # type = string

        # a free text natural language description of the search parameter from a
        # consumer's perspective. and how it used.
        self.description = None
        # type = string

        # a fhirpath expression that returns a set of elements for the search
        # parameter.
        self.expression = None
        # type = string

        # an xpath expression that returns a set of elements for the search
        # parameter.
        self.xpath = None
        # type = string

        # how the search parameter relates to the set of elements returned by
        # evaluating the xpath query.
        self.xpathUsage = None
        # type = string
        # possible values = normal, phonetic, nearby, distance, other

        # types of resource (if a resource is referenced).
        self.target = None
        # type = array

        # comparators supported for the search parameter.
        self.comparator = None
        # type = array
        # possible values = eq, ne, gt, lt, ge, le, sa, eb, ap

        # a modifier supported for the search parameter.
        self.modifier = None
        # type = array
        # possible values = missing, exact, contains, not, text, in, not-in, below, above, type

        # contains the names of any search parameters which may be chained to the
        # containing search parameter. chained parameters may be added to search
        # parameters of type reference, and specify that resources will only be
        # returned if they contain a reference to a resource which matches the
        # chained parameter value. values for this field should be drawn from
        # searchparameter.code for a parameter on the target resource type.
        self.chain = None
        # type = array

        # used to define the parts of a composite search parameter.
        self.component = None
        # type = array
        # reference to SearchParameter_Component: SearchParameter_Component


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, active, retired, unknown'))

        if self.type is not None:
            for value in self.type:
                if value != None and value.lower() not in ['number', 'date', 'string', 'token', 'reference', 'composite', 'quantity', 'uri']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'number, date, string, token, reference, composite, quantity, uri'))

        if self.xpathUsage is not None:
            for value in self.xpathUsage:
                if value != None and value.lower() not in ['normal', 'phonetic', 'nearby', 'distance', 'other']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'normal, phonetic, nearby, distance, other'))

        if self.comparator is not None:
            for value in self.comparator:
                if value != None and value.lower() not in ['eq', 'ne', 'gt', 'lt', 'ge', 'le', 'sa', 'eb', 'ap']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'eq, ne, gt, lt, ge, le, sa, eb, ap'))

        if self.modifier is not None:
            for value in self.modifier:
                if value != None and value.lower() not in ['missing', 'exact', 'contains', 'not', 'text', 'in', 'not-in', 'below', 'above', 'type']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'missing, exact, contains, not, text, in, not-in, below, above, type'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'SearchParameter',
            'child_variable': 'jurisdiction'},

            {'parent_entity': 'SearchParameter_Component',
            'parent_variable': 'object_id',
            'child_entity': 'SearchParameter',
            'child_variable': 'component'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'SearchParameter',
            'child_variable': 'useContext'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'SearchParameter',
            'child_variable': 'contact'},
        ]

class SearchParameter_Component(fhirbase):
    """A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    def __init__(self, dict_values=None):
        # the definition of the search parameter that describes this part.
        self.definition = None
        # reference to Reference: identifier

        # a sub-expression that defines how to extract values for this component
        # from the output of the main searchparameter.expression.
        self.expression = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'SearchParameter_Component',
            'child_variable': 'definition'},
        ]

