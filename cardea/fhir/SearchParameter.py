from .fhirbase import fhirbase


class SearchParameter(fhirbase):
    """
    A search parameter that defines a named search item that can be used
    to search/filter on a resource.

    Args:
        resourceType: This is a SearchParameter resource
        url: An absolute URI that is used to identify this search parameter
            when it is referenced in a specification, model, design or an
            instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
            be an address at which this search parameter is (or will be)
            published. The URL SHOULD include the major version of the search
            parameter. For more information see [Technical and Business
            Versions](resource.html#versions).
        version: The identifier that is used to identify this version of the
            search parameter when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the search
            parameter author and is not expected to be globally unique. For
            example, it might be a timestamp (e.g. yyyymmdd) if a managed version
            is not available. There is also no expectation that versions can be
            placed in a lexicographical sequence.
        name: A natural language name identifying the search parameter. This
            name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        status: The status of this search parameter. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this search parameter
            is authored for testing purposes (or education/evaluation/marketing),
            and is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the search parameter was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the search parameter
            changes.
        publisher: The name of the individual or organization that published
            the search parameter.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate search parameter
            instances.
        jurisdiction: A legal or geographic region in which the search
            parameter is intended to be used.
        purpose: Explaination of why this search parameter is needed and why
            it has been designed as it has.
        code: The code used in the URL or the parameter name in a parameters
            resource for this search parameter.
        base: The base resource type(s) that this search parameter can be used
            against.
        type: The type of value a search parameter refers to, and how the
            content is interpreted.
        derivedFrom: Where this search parameter is originally defined. If a
            derivedFrom is provided, then the details in the search parameter must
            be consistent with the definition from which it is defined. I.e. the
            parameter should have the same meaning, and (usually) the
            functionality should be a proper subset of the underlying search
            parameter.
        description: A free text natural language description of the search
            parameter from a consumer's perspective. and how it used.
        expression: A FHIRPath expression that returns a set of elements for
            the search parameter.
        xpath: An XPath expression that returns a set of elements for the
            search parameter.
        xpathUsage: How the search parameter relates to the set of elements
            returned by evaluating the xpath query.
        target: Types of resource (if a resource is referenced).
        comparator: Comparators supported for the search parameter.
        modifier: A modifier supported for the search parameter.
        chain: Contains the names of any search parameters which may be
            chained to the containing search parameter. Chained parameters may be
            added to search parameters of type reference, and specify that
            resources will only be returned if they contain a reference to a
            resource which matches the chained parameter value. Values for this
            field should be drawn from SearchParameter.code for a parameter on the
            target resource type.
        component: Used to define the parts of a composite search parameter.
    """

    __name__ = 'SearchParameter'

    def __init__(self, dict_values=None):
        self.resourceType = 'SearchParameter'
        # type: str
        # possible values: SearchParameter

        self.url = None
        # type: str

        self.version = None
        # type: str

        self.name = None
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

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.purpose = None
        # type: str

        self.code = None
        # type: str

        self.base = None
        # type: list

        self.type = None
        # type: str
        # possible values: number, date, string, token, reference,
        # composite, quantity, uri

        self.derivedFrom = None
        # type: str

        self.description = None
        # type: str

        self.expression = None
        # type: str

        self.xpath = None
        # type: str

        self.xpathUsage = None
        # type: str
        # possible values: normal, phonetic, nearby, distance, other

        self.target = None
        # type: list

        self.comparator = None
        # type: list
        # possible values: eq, ne, gt, lt, ge, le, sa, eb, ap

        self.modifier = None
        # type: list
        # possible values: missing, exact, contains, not, text, in,
        # not-in, below, above, type

        self.chain = None
        # type: list

        self.component = None
        # type: list
        # reference to SearchParameter_Component

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

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'number', 'date', 'string', 'token', 'reference', 'composite',
                        'quantity', 'uri']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'number, date, string, token, reference, composite, quantity, uri'))

        if self.xpathUsage is not None:
            for value in self.xpathUsage:
                if value is not None and value.lower() not in [
                        'normal', 'phonetic', 'nearby', 'distance', 'other']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'normal, phonetic, nearby, distance, other'))

        if self.comparator is not None:
            for value in self.comparator:
                if value is not None and value.lower() not in [
                        'eq', 'ne', 'gt', 'lt', 'ge', 'le', 'sa', 'eb', 'ap']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'eq, ne, gt, lt, ge, le, sa, eb, ap'))

        if self.modifier is not None:
            for value in self.modifier:
                if value is not None and value.lower() not in [
                    'missing', 'exact', 'contains', 'not', 'text', 'in', 'not-in',
                        'below', 'above', 'type']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'missing, exact, contains, not, text, in, not-in, below, above, '
                        'type'))

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

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'SearchParameter',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'SearchParameter',
             'child_variable': 'useContext'},
        ]


class SearchParameter_Component(fhirbase):
    """
    A search parameter that defines a named search item that can be used
    to search/filter on a resource.

    Args:
        definition: The definition of the search parameter that describes this
            part.
        expression: A sub-expression that defines how to extract values for
            this component from the output of the main SearchParameter.expression.
    """

    __name__ = 'SearchParameter_Component'

    def __init__(self, dict_values=None):
        self.definition = None
        # reference to Reference: identifier

        self.expression = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SearchParameter_Component',
             'child_variable': 'definition'},
        ]
