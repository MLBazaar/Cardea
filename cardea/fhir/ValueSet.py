from .fhirbase import fhirbase


class ValueSet(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        resourceType: This is a ValueSet resource
        url: An absolute URI that is used to identify this value set when it
            is referenced in a specification, model, design or an instance. This
            SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
            which this value set is (or will be) published. The URL SHOULD include
            the major version of the value set. For more information see
            [Technical and Business Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this value
            set when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            value set when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the value set author
            and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There
            is also no expectation that versions can be placed in a
            lexicographical sequence.
        name: A natural language name identifying the value set. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the value set.
        status: The status of this value set. Enables tracking the life-cycle
            of the content.
        experimental: A boolean value to indicate that this value set is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the value set was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the value set changes.
            (e.g. the 'content logical definition').
        publisher: The name of the individual or organization that published
            the value set.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the value set
            from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate value set
            instances.
        jurisdiction: A legal or geographic region in which the value set is
            intended to be used.
        immutable: If this is set to 'true', then no new versions of the
            content logical definition can be created.  Note: Other metadata might
            still change.
        purpose: Explaination of why this value set is needed and why it has
            been designed as it has.
        copyright: A copyright statement relating to the value set and/or its
            contents. Copyright statements are generally legal restrictions on the
            use and publishing of the value set.
        extensible: Whether this is intended to be used with an extensible
            binding or not.
        compose: A set of criteria that define the content logical definition
            of the value set by including or excluding codes from outside this
            value set. This I also known as the "Content Logical Definition"
            (CLD).
        expansion: A value set can also be "expanded", where the value set is
            turned into a simple collection of enumerated codes. This element
            holds the expansion, if it has been performed.
    """

    __name__ = 'ValueSet'

    def __init__(self, dict_values=None):
        self.resourceType = 'ValueSet'
        # type: str
        # possible values: ValueSet

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

        self.immutable = None
        # type: bool

        self.purpose = None
        # type: str

        self.copyright = None
        # type: str

        self.extensible = None
        # type: bool

        self.compose = None
        # reference to ValueSet_Compose

        self.expansion = None
        # reference to ValueSet_Expansion: identifier

        self.identifier = None
        # type: list
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

    def get_relationships(self):

        return [
            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'useContext'},

            {'parent_entity': 'ValueSet_Compose',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'compose'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'identifier'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'contact'},

            {'parent_entity': 'ValueSet_Expansion',
             'parent_variable': 'identifier',
             'child_entity': 'ValueSet',
             'child_variable': 'expansion'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'jurisdiction'},
        ]


class ValueSet_Compose(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        lockedDate: If a locked date is defined, then the Content Logical
            Definition must be evaluated using the current version as of the
            locked date for referenced code system(s) and value set instances
            where ValueSet.compose.include.version is not defined.
        inactive: Whether inactive codes - codes that are not approved for
            current use - are in the value set. If inactive = true, inactive codes
            are to be included in the expansion, if inactive = false, the inactive
            codes will not be included in the expansion. If absent, the behavior
            is determined by the implementation, or by the applicable
            ExpansionProfile (but generally, inactive codes would be expected to
            be included).
        include: Include one or more codes from a code system or other value
            set(s).
        exclude: Exclude one or more codes from the value set based on code
            system filters and/or other value sets.
    """

    __name__ = 'ValueSet_Compose'

    def __init__(self, dict_values=None):
        self.lockedDate = None
        # type: str

        self.inactive = None
        # type: bool

        self.include = None
        # type: list
        # reference to ValueSet_Include

        self.exclude = None
        # type: list
        # reference to ValueSet_Include

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Include',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Compose',
             'child_variable': 'include'},

            {'parent_entity': 'ValueSet_Include',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Compose',
             'child_variable': 'exclude'},
        ]


class ValueSet_Include(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        system: An absolute URI which is the code system from which the
            selected codes come from.
        version: The version of the code system that the codes are selected
            from.
        concept: Specifies a concept to be included or excluded.
        filter: Select concepts by specify a matching criteria based on the
            properties (including relationships) defined by the system. If
            multiple filters are specified, they SHALL all be true.
        valueSet: Selects concepts found in this value set. This is an
            absolute URI that is a reference to ValueSet.url.
    """

    __name__ = 'ValueSet_Include'

    def __init__(self, dict_values=None):
        self.system = None
        # type: str

        self.version = None
        # type: str

        self.concept = None
        # type: list
        # reference to ValueSet_Concept

        self.filter = None
        # type: list
        # reference to ValueSet_Filter

        self.valueSet = None
        # type: list

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Concept',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Include',
             'child_variable': 'concept'},

            {'parent_entity': 'ValueSet_Filter',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Include',
             'child_variable': 'filter'},
        ]


class ValueSet_Concept(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        code: Specifies a code for the concept to be included or excluded.
        display: The text to display to the user for this concept in the
            context of this valueset. If no display is provided, then applications
            using the value set use the display specified for the code by the
            system.
        designation: Additional representations for this concept when used in
            this value set - other languages, aliases, specialized purposes, used
            for particular purposes, etc.
    """

    __name__ = 'ValueSet_Concept'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.display = None
        # type: str

        self.designation = None
        # type: list
        # reference to ValueSet_Designation

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Designation',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Concept',
             'child_variable': 'designation'},
        ]


class ValueSet_Designation(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        language: The language this designation is defined for.
        use: A code that details how this designation would be used.
        value: The text value for this designation.
    """

    __name__ = 'ValueSet_Designation'

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
             'child_entity': 'ValueSet_Designation',
             'child_variable': 'use'},
        ]


class ValueSet_Filter(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        property: A code that identifies a property defined in the code
            system.
        op: The kind of operation to perform as a part of the filter criteria.
        value: The match value may be either a code defined by the system, or
            a string value, which is a regex match on the literal string of the
            property value when the operation is 'regex', or one of the values
            (true and false), when the operation is 'exists'.
    """

    __name__ = 'ValueSet_Filter'

    def __init__(self, dict_values=None):
        self.property = None
        # type: str

        self.op = None
        # type: str
        # possible values: =, is-a, descendent-of, is-not-a, regex,
        # in, not-in, generalizes, exists

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.op is not None:
            for value in self.op:
                if value is not None and value.lower() not in [
                    '=', 'is-a', 'descendent-of', 'is-not-a', 'regex', 'in', 'not-in',
                        'generalizes', 'exists']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, '=, is-a, descendent-of, is-not-a, regex, in, not-in, generalizes,'
                        'exists'))


class ValueSet_Expansion(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        identifier: An identifier that uniquely identifies this expansion of
            the valueset. Systems may re-use the same identifier as long as the
            expansion and the definition remain the same, but are not required to
            do so.
        timestamp: The time at which the expansion was produced by the
            expanding system.
        total: The total number of concepts in the expansion. If the number of
            concept nodes in this resource is less than the stated number, then
            the server can return more using the offset parameter.
        offset: If paging is being used, the offset at which this resource
            starts.  I.e. this resource is a partial view into the expansion. If
            paging is not being used, this element SHALL not be present.
        parameter: A parameter that controlled the expansion process. These
            parameters may be used by users of expanded value sets to check
            whether the expansion is suitable for a particular purpose, or to pick
            the correct expansion.
        contains: The codes that are contained in the value set expansion.
    """

    __name__ = 'ValueSet_Expansion'

    def __init__(self, dict_values=None):
        self.timestamp = None
        # type: str

        self.total = None
        # type: int

        self.offset = None
        # type: int

        self.parameter = None
        # type: list
        # reference to ValueSet_Parameter

        self.contains = None
        # type: list
        # reference to ValueSet_Contains

        self.identifier = None
        # type: str

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Expansion',
             'child_variable': 'parameter'},

            {'parent_entity': 'ValueSet_Contains',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Expansion',
             'child_variable': 'contains'},
        ]


class ValueSet_Parameter(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        name: The name of the parameter.
        valueString: The value of the parameter.
        valueBoolean: The value of the parameter.
        valueInteger: The value of the parameter.
        valueDecimal: The value of the parameter.
        valueUri: The value of the parameter.
        valueCode: The value of the parameter.
    """

    __name__ = 'ValueSet_Parameter'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.valueString = None
        # type: str

        self.valueBoolean = None
        # type: bool

        self.valueInteger = None
        # type: int

        self.valueDecimal = None
        # type: int

        self.valueUri = None
        # type: str

        self.valueCode = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class ValueSet_Contains(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.

    Args:
        system: An absolute URI which is the code system in which the code for
            this item in the expansion is defined.
        abstract: If true, this entry is included in the expansion for
            navigational purposes, and the user cannot select the code directly as
            a proper value.
        inactive: If the concept is inactive in the code system that defines
            it. Inactive codes are those that are no longer to be used, but are
            maintained by the code system for understanding legacy data.
        version: The version of this code system that defined this code and/or
            display. This should only be used with code systems that do not
            enforce concept permanence.
        code: The code for this item in the expansion hierarchy. If this code
            is missing the entry in the hierarchy is a place holder (abstract) and
            does not represent a valid code in the value set.
        display: The recommended display for this item in the expansion.
        designation: Additional representations for this item - other
            languages, aliases, specialized purposes, used for particular
            purposes, etc. These are relevant when the conditions of the expansion
            do not fix to a single correct representation.
        contains: Other codes and entries contained under this entry in the
            hierarchy.
    """

    __name__ = 'ValueSet_Contains'

    def __init__(self, dict_values=None):
        self.system = None
        # type: str

        self.abstract = None
        # type: bool

        self.inactive = None
        # type: bool

        self.version = None
        # type: str

        self.code = None
        # type: str

        self.display = None
        # type: str

        self.designation = None
        # type: list
        # reference to ValueSet_Designation

        self.contains = None
        # type: list
        # reference to ValueSet_Contains

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Contains',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Contains',
             'child_variable': 'contains'},

            {'parent_entity': 'ValueSet_Designation',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Contains',
             'child_variable': 'designation'},
        ]
