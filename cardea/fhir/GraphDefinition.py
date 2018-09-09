from .fhirbase import fhirbase


class GraphDefinition(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.
    """

    __name__ = 'GraphDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'GraphDefinition'
        """
        This is a GraphDefinition resource

        type: string
        possible values: GraphDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this graph definition when it
        is referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this graph definition is (or will be) published. The URL SHOULD
        include the major version of the graph definition. For more
        information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the graph
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the graph definition
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the graph definition. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.status = None
        """
        The status of this graph definition. Enables tracking the life-cycle
        of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this graph definition is authored for
        testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the graph definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the graph definition
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the graph
        definition.

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
        A free text natural language description of the graph definition from
        a consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate graph definition instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the graph definition is intended
        to be used.

        type: array
        reference to CodeableConcept
        """

        self.purpose = None
        """
        Explaination of why this graph definition is needed and why it has
        been designed as it has.

        type: string
        """

        self.start = None
        """
        The type of FHIR resource at which instances of this graph start.

        type: string
        """

        self.profile = None
        """
        The profile that describes the use of the base resource.

        type: string
        """

        self.link = None
        """
        Links this graph makes rules about.

        type: array
        reference to GraphDefinition_Link
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

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'GraphDefinition_Link',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'link'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition',
             'child_variable': 'useContext'},
        ]


class GraphDefinition_Link(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.
    """

    __name__ = 'GraphDefinition_Link'

    def __init__(self, dict_values=None):
        self.path = None
        """
        Path in the resource that contains the link.

        type: string
        """

        self.sliceName = None
        """
        Which slice (if profiled).

        type: string
        """

        self.min = None
        """
        Minimum occurrences for this link.

        type: int
        """

        self.max = None
        """
        Maximum occurrences for this link.

        type: string
        """

        self.description = None
        """
        Information about why this link is of interest in this graph
        definition.

        type: string
        """

        self.target = None
        """
        Potential target for the link.

        type: array
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class GraphDefinition_Target(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.
    """

    __name__ = 'GraphDefinition_Target'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Type of resource this link refers to.

        type: string
        """

        self.profile = None
        """
        Profile for the target resource.

        type: string
        """

        self.compartment = None
        """
        Compartment Consistency Rules.

        type: array
        reference to GraphDefinition_Compartment
        """

        self.link = None
        """
        Additional links from target resource.

        type: array
        reference to GraphDefinition_Link
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'GraphDefinition_Compartment',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition_Target',
             'child_variable': 'compartment'},

            {'parent_entity': 'GraphDefinition_Link',
             'parent_variable': 'object_id',
             'child_entity': 'GraphDefinition_Target',
             'child_variable': 'link'},
        ]


class GraphDefinition_Compartment(fhirbase):
    """
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references.
    The Graph Definition resource defines a set and makes rules about the
    set.
    """

    __name__ = 'GraphDefinition_Compartment'

    def __init__(self, dict_values=None):
        self.code = None
        """
        Identifies the compartment.

        type: string
        """

        self.rule = None
        """
        identical | matching | different | no-rule | custom.

        type: string
        possible values: identical, matching, different, custom
        """

        self.expression = None
        """
        Custom rule, as a FHIRPath expression.

        type: string
        """

        self.description = None
        """
        Documentation for FHIRPath expression.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.rule is not None:
            for value in self.rule:
                if value is not None and value.lower() not in [
                        'identical', 'matching', 'different', 'custom']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'identical, matching, different, custom'))
