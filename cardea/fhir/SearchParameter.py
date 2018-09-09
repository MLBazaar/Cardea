from .fhirbase import fhirbase


class SearchParameter(fhirbase):
    """
    A search parameter that defines a named search item that can be used
    to search/filter on a resource.
    """

    __name__ = 'SearchParameter'

    def __init__(self, dict_values=None):
        self.resourceType = 'SearchParameter'
        """
        This is a SearchParameter resource

        type: string
        possible values: SearchParameter
        """

        self.url = None
        """
        An absolute URI that is used to identify this search parameter when it
        is referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this search parameter is (or will be) published. The URL SHOULD
        include the major version of the search parameter. For more
        information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the search
        parameter when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the search parameter
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the search parameter. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.status = None
        """
        The status of this search parameter. Enables tracking the life-cycle
        of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this search parameter is authored for
        testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the search parameter was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the search parameter
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the search
        parameter.

        type: string
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        publisher.

        type: array
        reference to ContactDetail
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate search parameter instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the search parameter is intended
        to be used.

        type: array
        reference to CodeableConcept
        """

        self.purpose = None
        """
        Explaination of why this search parameter is needed and why it has
        been designed as it has.

        type: string
        """

        self.code = None
        """
        The code used in the URL or the parameter name in a parameters
        resource for this search parameter.

        type: string
        """

        self.base = None
        """
        The base resource type(s) that this search parameter can be used
        against.

        type: array
        """

        self.type = None
        """
        The type of value a search parameter refers to, and how the content is
        interpreted.

        type: string
        possible values: number, date, string, token, reference,
        composite, quantity, uri
        """

        self.derivedFrom = None
        """
        Where this search parameter is originally defined. If a derivedFrom is
        provided, then the details in the search parameter must be consistent
        with the definition from which it is defined. I.e. the parameter
        should have the same meaning, and (usually) the functionality should
        be a proper subset of the underlying search parameter.

        type: string
        """

        self.description = None
        """
        A free text natural language description of the search parameter from
        a consumer's perspective. and how it used.

        type: string
        """

        self.expression = None
        """
        A FHIRPath expression that returns a set of elements for the search
        parameter.

        type: string
        """

        self.xpath = None
        """
        An XPath expression that returns a set of elements for the search
        parameter.

        type: string
        """

        self.xpathUsage = None
        """
        How the search parameter relates to the set of elements returned by
        evaluating the xpath query.

        type: string
        possible values: normal, phonetic, nearby, distance, other
        """

        self.target = None
        """
        Types of resource (if a resource is referenced).

        type: array
        """

        self.comparator = None
        """
        Comparators supported for the search parameter.

        type: array
        possible values: eq, ne, gt, lt, ge, le, sa, eb, ap
        """

        self.modifier = None
        """
        A modifier supported for the search parameter.

        type: array
        possible values: missing, exact, contains, not, text, in,
        not-in, below, above, type
        """

        self.chain = None
        """
        Contains the names of any search parameters which may be chained to
        the containing search parameter. Chained parameters may be added to
        search parameters of type reference, and specify that resources will
        only be returned if they contain a reference to a resource which
        matches the chained parameter value. Values for this field should be
        drawn from SearchParameter.code for a parameter on the target resource
        type.

        type: array
        """

        self.component = None
        """
        Used to define the parts of a composite search parameter.

        type: array
        reference to SearchParameter_Component
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
                        value, 'missing, exact, contains, not, text, in, not-in, below, '
                        'above, type'))

    def get_relationships(self):

        return [
            {'parent_entity': 'SearchParameter_Component',
             'parent_variable': 'object_id',
             'child_entity': 'SearchParameter',
             'child_variable': 'component'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'SearchParameter',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SearchParameter',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'SearchParameter',
             'child_variable': 'useContext'},
        ]


class SearchParameter_Component(fhirbase):
    """
    A search parameter that defines a named search item that can be used
    to search/filter on a resource.
    """

    __name__ = 'SearchParameter_Component'

    def __init__(self, dict_values=None):
        self.definition = None
        """
        The definition of the search parameter that describes this part.

        reference to Reference: identifier
        """

        self.expression = None
        """
        A sub-expression that defines how to extract values for this component
        from the output of the main SearchParameter.expression.

        type: string
        """

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
