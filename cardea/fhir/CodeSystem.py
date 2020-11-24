from .fhirbase import fhirbase


class CodeSystem(fhirbase):
    """
    A code system resource specifies a set of codes drawn from one or more
    code systems.

    Args:
        resourceType: This is a CodeSystem resource
        url: An absolute URI that is used to identify this code system when it
            is referenced in a specification, model, design or an instance. This
            SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
            which this code system is (or will be) published. The URL SHOULD
            include the major version of the code system. For more information see
            [Technical and Business Versions](resource.html#versions). This is
            used in [Coding]{datatypes.html#Coding}.system.
        identifier: A formal identifier that is used to identify this code
            system when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            code system when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the code system author
            and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There
            is also no expectation that versions can be placed in a
            lexicographical sequence. This is used in
            [Coding]{datatypes.html#Coding}.version.
        name: A natural language name identifying the code system. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the code system.
        status: The status of this code system. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this code system is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the code system was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the code system changes.
        publisher: The name of the individual or organization that published
            the code system.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the code
            system from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate code system
            instances.
        jurisdiction: A legal or geographic region in which the code system is
            intended to be used.
        purpose: Explaination of why this code system is needed and why it has
            been designed as it has.
        copyright: A copyright statement relating to the code system and/or
            its contents. Copyright statements are generally legal restrictions on
            the use and publishing of the code system.
        caseSensitive: If code comparison is case sensitive when codes within
            this system are compared to each other.
        valueSet: Canonical URL of value set that contains the entire code
            system.
        hierarchyMeaning: The meaning of the hierarchy of concepts.
        compositional: True If code system defines a post-composition grammar.
        versionNeeded: This flag is used to signify that the code system has
            not (or does not) maintain the definitions, and a version must be
            specified when referencing this code system.
        content: How much of the content of the code system - the concepts and
            codes it defines - are represented in this resource.
        count: The total number of concepts defined by the code system. Where
            the code system has a compositional grammar, the count refers to the
            number of base (primitive) concepts.
        filter: A filter that can be used in a value set compose statement
            when selecting concepts using a filter.
        property: A property defines an additional slot through which
            additional information can be provided about a concept.
        concept: Concepts that are in the code system. The concept definitions
            are inherently hierarchical, but the definitions must be consulted to
            determine what the meaning of the hierarchical relationships are.
    """

    __name__ = 'CodeSystem'

    def __init__(self, dict_values=None):
        self.resourceType = 'CodeSystem'
        # type: str
        # possible values: CodeSystem

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

        self.caseSensitive = None
        # type: bool

        self.valueSet = None
        # type: str

        self.hierarchyMeaning = None
        # type: str
        # possible values: grouped-by, is-a, part-of, classified-with

        self.compositional = None
        # type: bool

        self.versionNeeded = None
        # type: bool

        self.content = None
        # type: str
        # possible values: not-present, example, fragment, complete

        self.count = None
        # type: int

        self.filter = None
        # type: list
        # reference to CodeSystem_Filter

        self.property = None
        # type: list
        # reference to CodeSystem_Property

        self.concept = None
        # type: list
        # reference to CodeSystem_Concept

        self.identifier = None
        # reference to Identifier

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

            {'parent_entity': 'CodeSystem_Concept',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'concept'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'identifier'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem',
             'child_variable': 'contact'},
        ]


class CodeSystem_Filter(fhirbase):
    """
    A code system resource specifies a set of codes drawn from one or more
    code systems.

    Args:
        code: The code that identifies this filter when it is used in the
            instance.
        description: A description of how or why the filter is used.
        operator: A list of operators that can be used with the filter.
        value: A description of what the value for the filter should be.
    """

    __name__ = 'CodeSystem_Filter'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.description = None
        # type: str

        self.operator = None
        # type: list

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class CodeSystem_Property(fhirbase):
    """
    A code system resource specifies a set of codes drawn from one or more
    code systems.

    Args:
        code: A code that is used to identify the property. The code is used
            internally (in CodeSystem.concept.property.code) and also externally,
            such as in property filters.
        uri: Reference to the formal meaning of the property. One possible
            source of meaning is the [Concept
            Properties](codesystem-concept-properties.html) code system.
        description: A description of the property- why it is defined, and how
            its value might be used.
        type: The type of the property value. Properties of type "code"
            contain a code defined by the code system (e.g. a reference to
            anotherr defined concept).
    """

    __name__ = 'CodeSystem_Property'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.uri = None
        # type: str

        self.description = None
        # type: str

        self.type = None
        # type: str
        # possible values: code, Coding, string, integer, boolean,
        # dateTime

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'code', 'coding', 'string', 'integer', 'boolean', 'datetime']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'code, Coding, string, integer, boolean, dateTime'))


class CodeSystem_Concept(fhirbase):
    """
    A code system resource specifies a set of codes drawn from one or more
    code systems.

    Args:
        code: A code - a text symbol - that uniquely identifies the concept
            within the code system.
        display: A human readable string that is the recommended default way
            to present this concept to a user.
        definition: The formal definition of the concept. The code system
            resource does not make formal definitions required, because of the
            prevalence of legacy systems. However, they are highly recommended, as
            without them there is no formal meaning associated with the concept.
        designation: Additional representations for the concept - other
            languages, aliases, specialized purposes, used for particular
            purposes, etc.
        property: A property value for this concept.
        concept: Defines children of a concept to produce a hierarchy of
            concepts. The nature of the relationships is variable
            (is-a/contains/categorizes) - see hierarchyMeaning.
    """

    __name__ = 'CodeSystem_Concept'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.display = None
        # type: str

        self.definition = None
        # type: str

        self.designation = None
        # type: list
        # reference to CodeSystem_Designation

        self.property = None
        # type: list
        # reference to CodeSystem_Property1

        self.concept = None
        # type: list
        # reference to CodeSystem_Concept

        self.object_id = None
        # unique identifier for object class

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
    """
    A code system resource specifies a set of codes drawn from one or more
    code systems.

    Args:
        language: The language this designation is defined for.
        use: A code that details how this designation would be used.
        value: The text value for this designation.
    """

    __name__ = 'CodeSystem_Designation'

    def __init__(self, dict_values=None):
        self.language = None
        # type: str

        self.use = None
        # reference to Coding

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

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
    """
    A code system resource specifies a set of codes drawn from one or more
    code systems.

    Args:
        code: A code that is a reference to CodeSystem.property.code.
        valueCode: The value of this property.
        valueCoding: The value of this property.
        valueString: The value of this property.
        valueInteger: The value of this property.
        valueBoolean: The value of this property.
        valueDateTime: The value of this property.
    """

    __name__ = 'CodeSystem_Property1'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.valueCode = None
        # type: str

        self.valueCoding = None
        # reference to Coding

        self.valueString = None
        # type: str

        self.valueInteger = None
        # type: int

        self.valueBoolean = None
        # type: bool

        self.valueDateTime = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'CodeSystem_Property1',
             'child_variable': 'valueCoding'},
        ]
