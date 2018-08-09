from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .ContactDetail import ContactDetail
from .UsageContext import UsageContext

class GraphDefinition(fhirbase):
    """A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """

    def __init__(self, dict_values=None):
        # this is a graphdefinition resource
        self.resourceType = 'GraphDefinition'
        # type = string
        # possible values = GraphDefinition

        # an absolute uri that is used to identify this graph definition when it
        # is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this graph definition is (or will be) published. the url should
        # include the major version of the graph definition. for more information
        # see [technical and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the graph
        # definition when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the graph definition
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the graph definition. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # the status of this graph definition. enables tracking the life-cycle of
        # the content.
        self.status = None
        # type = string
        # possible values = draft, active, retired, unknown

        # a boolean value to indicate that this graph definition is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the graph definition was published.
        # the date must change if and when the business version changes and it
        # must change if the status code changes. in addition, it should change
        # when the substantive content of the graph definition changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the graph
        # definition.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the graph definition from a
        # consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate graph definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the graph definition is intended
        # to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this graph definition is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # the type of fhir resource at which instances of this graph start.
        self.start = None
        # type = string

        # the profile that describes the use of the base resource.
        self.profile = None
        # type = string

        # links this graph makes rules about.
        self.link = None
        # type = array
        # reference to GraphDefinition_Link: GraphDefinition_Link


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'GraphDefinition_Link',
            'parent_variable': 'object_id',
            'child_entity': 'GraphDefinition',
            'child_variable': 'link'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'GraphDefinition',
            'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'GraphDefinition',
            'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'GraphDefinition',
            'child_variable': 'useContext'},
        ]

class GraphDefinition_Link(fhirbase):
    """A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """

    def __init__(self, dict_values=None):
        # path in the resource that contains the link.
        self.path = None
        # type = string

        # which slice (if profiled).
        self.sliceName = None
        # type = string

        # minimum occurrences for this link.
        self.min = None
        # type = int

        # maximum occurrences for this link.
        self.max = None
        # type = string

        # information about why this link is of interest in this graph definition.
        self.description = None
        # type = string

        # potential target for the link.
        self.target = None
        # type = array


        if dict_values:
              self.set_attributes(dict_values)


class GraphDefinition_Target(fhirbase):
    """A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """

    def __init__(self, dict_values=None):
        # type of resource this link refers to.
        self.type = None
        # type = string

        # profile for the target resource.
        self.profile = None
        # type = string

        # compartment consistency rules.
        self.compartment = None
        # type = array
        # reference to GraphDefinition_Compartment: GraphDefinition_Compartment

        # additional links from target resource.
        self.link = None
        # type = array
        # reference to GraphDefinition_Link: GraphDefinition_Link


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'GraphDefinition_Link',
            'parent_variable': 'object_id',
            'child_entity': 'GraphDefinition_Target',
            'child_variable': 'link'},

            {'parent_entity': 'GraphDefinition_Compartment',
            'parent_variable': 'object_id',
            'child_entity': 'GraphDefinition_Target',
            'child_variable': 'compartment'},
        ]

class GraphDefinition_Compartment(fhirbase):
    """A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """

    def __init__(self, dict_values=None):
        # identifies the compartment.
        self.code = None
        # type = string

        # identical | matching | different | no-rule | custom.
        self.rule = None
        # type = string
        # possible values = identical, matching, different, custom

        # custom rule, as a fhirpath expression.
        self.expression = None
        # type = string

        # documentation for fhirpath expression.
        self.description = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.rule is not None:
            for value in self.rule:
                if value != None and value.lower() not in ['identical', 'matching', 'different', 'custom']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'identical, matching, different, custom'))

