from .fhirbase import fhirbase


class CodeSystem(fhirbase):
    """A code system resource specifies a set of codes drawn from one or more
    code systems.
    """

    __name__ = 'CodeSystem'

    def __init__(self, dict_values=None):
        # this is a codesystem resource
        self.resourceType = 'CodeSystem'
        # type = string
        # possible values: CodeSystem

        # an absolute uri that is used to identify this code system when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this code system is (or will be) published. the url should include the
        # major version of the code system. for more information see [technical
        # and business versions](resource.html#versions). this is used in
        # [coding]{datatypes.html#coding}.system.
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the code system
        # when it is referenced in a specification, model, design or instance.
        # this is an arbitrary value managed by the code system author and is not
        # expected to be globally unique. for example, it might be a timestamp
        # (e.g. yyyymmdd) if a managed version is not available. there is also no
        # expectation that versions can be placed in a lexicographical sequence.
        # this is used in [coding]{datatypes.html#coding}.version.
        self.version = None
        # type = string

        # a natural language name identifying the code system. this name should be
        # usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the code system.
        self.title = None
        # type = string

        # the status of this code system. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this code system is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the code system was published. the
        # date must change if and when the business version changes and it must
        # change if the status code changes. in addition, it should change when
        # the substantive content of the code system changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the code
        # system.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the code system from a
        # consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate code system instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the code system is intended to be
        # used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this code system is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the code system and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the code system.
        self.copyright = None
        # type = string

        # if code comparison is case sensitive when codes within this system are
        # compared to each other.
        self.caseSensitive = None
        # type = boolean

        # canonical url of value set that contains the entire code system.
        self.valueSet = None
        # type = string

        # the meaning of the hierarchy of concepts.
        self.hierarchyMeaning = None
        # type = string
        # possible values: grouped-by, is-a, part-of, classified-with

        # true if code system defines a post-composition grammar.
        self.compositional = None
        # type = boolean

        # this flag is used to signify that the code system has not (or does not)
        # maintain the definitions, and a version must be specified when
        # referencing this code system.
        self.versionNeeded = None
        # type = boolean

        # how much of the content of the code system - the concepts and codes it
        # defines - are represented in this resource.
        self.content = None
        # type = string
        # possible values: not-present, example, fragment, complete

        # the total number of concepts defined by the code system. where the code
        # system has a compositional grammar, the count refers to the number of
        # base (primitive) concepts.
        self.count = None
        # type = int

        # a filter that can be used in a value set compose statement when
        # selecting concepts using a filter.
        self.filter = None
        # type = array
        # reference to CodeSystem_Filter: CodeSystem_Filter

        # a property defines an additional slot through which additional
        # information can be provided about a concept.
        self.property = None
        # type = array
        # reference to CodeSystem_Property: CodeSystem_Property

        # concepts that are in the code system. the concept definitions are
        # inherently hierarchical, but the definitions must be consulted to
        # determine what the meaning of the hierarchical relationships are.
        self.concept = None
        # type = array
        # reference to CodeSystem_Concept: CodeSystem_Concept

        # a formal identifier that is used to identify this code system when it is
        # represented in other formats, or referenced in a specification, model,
        # design or an instance.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

        if self.hierarchyMeaning is not None:
            for value in self.hierarchyMeaning:
                if value is not None and value.lower() not in [
                        'grouped-by', 'is-a', 'part-of', 'classified-with']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'grouped-by, is-a, part-of, classified-with'))

        if self.content is not None:
            for value in self.content:
                if value is not None and value.lower() not in [
                        'not-present', 'example', 'fragment', 'complete']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'not-present, example, fragment, complete'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeSystem_Concept',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'concept'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeSystem_Filter',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'filter'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeSystem_Property',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'property'},
        ]


class CodeSystem_Filter(fhirbase):
    """A code system resource specifies a set of codes drawn from one or more
    code systems.
    """

    __name__ = 'CodeSystem_Filter'

    def __init__(self, dict_values=None):
        # the code that identifies this filter when it is used in the instance.
        self.code = None
        # type = string

        # a description of how or why the filter is used.
        self.description = None
        # type = string

        # a list of operators that can be used with the filter.
        self.operator = None
        # type = array

        # a description of what the value for the filter should be.
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class CodeSystem_Property(fhirbase):
    """A code system resource specifies a set of codes drawn from one or more
    code systems.
    """

    __name__ = 'CodeSystem_Property'

    def __init__(self, dict_values=None):
        # a code that is used to identify the property. the code is used
        # internally (in codesystem.concept.property.code) and also externally,
        # such as in property filters.
        self.code = None
        # type = string

        # reference to the formal meaning of the property. one possible source of
        # meaning is the [concept properties](codesystem-concept-properties.html)
        # code system.
        self.uri = None
        # type = string

        # a description of the property- why it is defined, and how its value
        # might be used.
        self.description = None
        # type = string

        # the type of the property value. properties of type "code" contain a code
        # defined by the code system (e.g. a reference to anotherr defined
        # concept).
        self.type = None
        # type = string
        # possible values: code, Coding, string, integer, boolean,
        # dateTime

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'code', 'coding', 'string', 'integer', 'boolean', 'datetime']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'code, Coding, string, integer, boolean, dateTime'))


class CodeSystem_Concept(fhirbase):
    """A code system resource specifies a set of codes drawn from one or more
    code systems.
    """

    __name__ = 'CodeSystem_Concept'

    def __init__(self, dict_values=None):
        # a code - a text symbol - that uniquely identifies the concept within the
        # code system.
        self.code = None
        # type = string

        # a human readable string that is the recommended default way to present
        # this concept to a user.
        self.display = None
        # type = string

        # the formal definition of the concept. the code system resource does not
        # make formal definitions required, because of the prevalence of legacy
        # systems. however, they are highly recommended, as without them there is
        # no formal meaning associated with the concept.
        self.definition = None
        # type = string

        # additional representations for the concept - other languages, aliases,
        # specialized purposes, used for particular purposes, etc.
        self.designation = None
        # type = array
        # reference to CodeSystem_Designation: CodeSystem_Designation

        # a property value for this concept.
        self.property = None
        # type = array
        # reference to CodeSystem_Property1: CodeSystem_Property1

        # defines children of a concept to produce a hierarchy of concepts. the
        # nature of the relationships is variable (is-a/contains/categorizes) -
        # see hierarchymeaning.
        self.concept = None
        # type = array
        # reference to CodeSystem_Concept: CodeSystem_Concept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeSystem_Concept',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem_Concept',
             'child_variable': 'concept'},

            {'parent_entity': 'CodeSystem_Designation',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem_Concept',
             'child_variable': 'designation'},

            {'parent_entity': 'CodeSystem_Property1',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem_Concept',
             'child_variable': 'property'},
        ]


class CodeSystem_Designation(fhirbase):
    """A code system resource specifies a set of codes drawn from one or more
    code systems.
    """

    __name__ = 'CodeSystem_Designation'

    def __init__(self, dict_values=None):
        # the language this designation is defined for.
        self.language = None
        # type = string

        # a code that details how this designation would be used.
        self.use = None
        # reference to Coding: Coding

        # the text value for this designation.
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem_Designation',
             'child_variable': 'use'},
        ]


class CodeSystem_Property1(fhirbase):
    """A code system resource specifies a set of codes drawn from one or more
    code systems.
    """

    __name__ = 'CodeSystem_Property1'

    def __init__(self, dict_values=None):
        # a code that is a reference to codesystem.property.code.
        self.code = None
        # type = string

        # the value of this property.
        self.valueCode = None
        # type = string

        # the value of this property.
        self.valueCoding = None
        # reference to Coding: Coding

        # the value of this property.
        self.valueString = None
        # type = string

        # the value of this property.
        self.valueInteger = None
        # type = int

        # the value of this property.
        self.valueBoolean = None
        # type = boolean

        # the value of this property.
        self.valueDateTime = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem_Property1',
             'child_variable': 'valueCoding'},
        ]
