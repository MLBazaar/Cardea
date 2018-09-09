from .fhirbase import fhirbase


class ValueSet(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.
    """

    __name__ = 'ValueSet'

    def __init__(self, dict_values=None):
        self.resourceType = 'ValueSet'
        """
        This is a ValueSet resource

        type: string
        possible values: ValueSet
        """

        self.url = None
        """
        An absolute URI that is used to identify this value set when it is
        referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this value set is (or will be) published. The URL SHOULD include
        the major version of the value set. For more information see
        [Technical and Business Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the value set
        when it is referenced in a specification, model, design or instance.
        This is an arbitrary value managed by the value set author and is not
        expected to be globally unique. For example, it might be a timestamp
        (e.g. yyyymmdd) if a managed version is not available. There is also
        no expectation that versions can be placed in a lexicographical
        sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the value set. This name should be
        usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the value set.

        type: string
        """

        self.status = None
        """
        The status of this value set. Enables tracking the life-cycle of the
        content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this value set is authored for
        testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the value set was published. The
        date must change if and when the business version changes and it must
        change if the status code changes. In addition, it should change when
        the substantive content of the value set changes. (e.g. the 'content
        logical definition').

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the value
        set.

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
        A free text natural language description of the value set from a
        consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate value set instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the value set is intended to be
        used.

        type: array
        reference to CodeableConcept
        """

        self.immutable = None
        """
        If this is set to 'true', then no new versions of the content logical
        definition can be created.  Note: Other metadata might still change.

        type: boolean
        """

        self.purpose = None
        """
        Explaination of why this value set is needed and why it has been
        designed as it has.

        type: string
        """

        self.copyright = None
        """
        A copyright statement relating to the value set and/or its contents.
        Copyright statements are generally legal restrictions on the use and
        publishing of the value set.

        type: string
        """

        self.extensible = None
        """
        Whether this is intended to be used with an extensible binding or not.

        type: boolean
        """

        self.compose = None
        """
        A set of criteria that define the content logical definition of the
        value set by including or excluding codes from outside this value set.
        This I also known as the "Content Logical Definition" (CLD).

        reference to ValueSet_Compose
        """

        self.expansion = None
        """
        A value set can also be "expanded", where the value set is turned into
        a simple collection of enumerated codes. This element holds the
        expansion, if it has been performed.

        reference to ValueSet_Expansion: identifier
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this value set when it is
        represented in other formats, or referenced in a specification, model,
        design or an instance.

        type: array
        reference to Identifier
        """

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
            {'parent_entity': 'ValueSet_Compose',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'compose'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'identifier'},

            {'parent_entity': 'ValueSet_Expansion',
             'parent_variable': 'identifier',
             'child_entity': 'ValueSet',
             'child_variable': 'expansion'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet',
             'child_variable': 'jurisdiction'},
        ]


class ValueSet_Compose(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.
    """

    __name__ = 'ValueSet_Compose'

    def __init__(self, dict_values=None):
        self.lockedDate = None
        """
        If a locked date is defined, then the Content Logical Definition must
        be evaluated using the current version as of the locked date for
        referenced code system(s) and value set instances where
        ValueSet.compose.include.version is not defined.

        type: string
        """

        self.inactive = None
        """
        Whether inactive codes - codes that are not approved for current use -
        are in the value set. If inactive = true, inactive codes are to be
        included in the expansion, if inactive = false, the inactive codes
        will not be included in the expansion. If absent, the behavior is
        determined by the implementation, or by the applicable
        ExpansionProfile (but generally, inactive codes would be expected to
        be included).

        type: boolean
        """

        self.include = None
        """
        Include one or more codes from a code system or other value set(s).

        type: array
        reference to ValueSet_Include
        """

        self.exclude = None
        """
        Exclude one or more codes from the value set based on code system
        filters and/or other value sets.

        type: array
        reference to ValueSet_Include
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Include',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Compose',
             'child_variable': 'exclude'},

            {'parent_entity': 'ValueSet_Include',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Compose',
             'child_variable': 'include'},
        ]


class ValueSet_Include(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.
    """

    __name__ = 'ValueSet_Include'

    def __init__(self, dict_values=None):
        self.system = None
        """
        An absolute URI which is the code system from which the selected codes
        come from.

        type: string
        """

        self.version = None
        """
        The version of the code system that the codes are selected from.

        type: string
        """

        self.concept = None
        """
        Specifies a concept to be included or excluded.

        type: array
        reference to ValueSet_Concept
        """

        self.filter = None
        """
        Select concepts by specify a matching criteria based on the properties
        (including relationships) defined by the system. If multiple filters
        are specified, they SHALL all be true.

        type: array
        reference to ValueSet_Filter
        """

        self.valueSet = None
        """
        Selects concepts found in this value set. This is an absolute URI that
        is a reference to ValueSet.url.

        type: array
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Filter',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Include',
             'child_variable': 'filter'},

            {'parent_entity': 'ValueSet_Concept',
             'parent_variable': 'object_id',
             'child_entity': 'ValueSet_Include',
             'child_variable': 'concept'},
        ]


class ValueSet_Concept(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.
    """

    __name__ = 'ValueSet_Concept'

    def __init__(self, dict_values=None):
        self.code = None
        """
        Specifies a code for the concept to be included or excluded.

        type: string
        """

        self.display = None
        """
        The text to display to the user for this concept in the context of
        this valueset. If no display is provided, then applications using the
        value set use the display specified for the code by the system.

        type: string
        """

        self.designation = None
        """
        Additional representations for this concept when used in this value
        set - other languages, aliases, specialized purposes, used for
        particular purposes, etc.

        type: array
        reference to ValueSet_Designation
        """

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
    """

    __name__ = 'ValueSet_Designation'

    def __init__(self, dict_values=None):
        self.language = None
        """
        The language this designation is defined for.

        type: string
        """

        self.use = None
        """
        A code that details how this designation would be used.

        reference to Coding
        """

        self.value = None
        """
        The text value for this designation.

        type: string
        """

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
    """

    __name__ = 'ValueSet_Filter'

    def __init__(self, dict_values=None):
        self.property = None
        """
        A code that identifies a property defined in the code system.

        type: string
        """

        self.op = None
        """
        The kind of operation to perform as a part of the filter criteria.

        type: string
        possible values: =, is-a, descendent-of, is-not-a, regex, in,
        not-in, generalizes, exists
        """

        self.value = None
        """
        The match value may be either a code defined by the system, or a
        string value, which is a regex match on the literal string of the
        property value when the operation is 'regex', or one of the values
        (true and false), when the operation is 'exists'.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
    """

    __name__ = 'ValueSet_Expansion'

    def __init__(self, dict_values=None):
        self.timestamp = None
        """
        The time at which the expansion was produced by the expanding system.

        type: string
        """

        self.total = None
        """
        The total number of concepts in the expansion. If the number of
        concept nodes in this resource is less than the stated number, then
        the server can return more using the offset parameter.

        type: int
        """

        self.offset = None
        """
        If paging is being used, the offset at which this resource starts.
        I.e. this resource is a partial view into the expansion. If paging is
        not being used, this element SHALL not be present.

        type: int
        """

        self.parameter = None
        """
        A parameter that controlled the expansion process. These parameters
        may be used by users of expanded value sets to check whether the
        expansion is suitable for a particular purpose, or to pick the correct
        expansion.

        type: array
        reference to ValueSet_Parameter
        """

        self.contains = None
        """
        The codes that are contained in the value set expansion.

        type: array
        reference to ValueSet_Contains
        """

        self.identifier = None
        """
        An identifier that uniquely identifies this expansion of the valueset.
        Systems may re-use the same identifier as long as the expansion and
        the definition remain the same, but are not required to do so.

        type: string
        """

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
    """

    __name__ = 'ValueSet_Parameter'

    def __init__(self, dict_values=None):
        self.name = None
        """
        The name of the parameter.

        type: string
        """

        self.valueString = None
        """
        The value of the parameter.

        type: string
        """

        self.valueBoolean = None
        """
        The value of the parameter.

        type: boolean
        """

        self.valueInteger = None
        """
        The value of the parameter.

        type: int
        """

        self.valueDecimal = None
        """
        The value of the parameter.

        type: int
        """

        self.valueUri = None
        """
        The value of the parameter.

        type: string
        """

        self.valueCode = None
        """
        The value of the parameter.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class ValueSet_Contains(fhirbase):
    """
    A value set specifies a set of codes drawn from one or more code
    systems.
    """

    __name__ = 'ValueSet_Contains'

    def __init__(self, dict_values=None):
        self.system = None
        """
        An absolute URI which is the code system in which the code for this
        item in the expansion is defined.

        type: string
        """

        self.abstract = None
        """
        If true, this entry is included in the expansion for navigational
        purposes, and the user cannot select the code directly as a proper
        value.

        type: boolean
        """

        self.inactive = None
        """
        If the concept is inactive in the code system that defines it.
        Inactive codes are those that are no longer to be used, but are
        maintained by the code system for understanding legacy data.

        type: boolean
        """

        self.version = None
        """
        The version of this code system that defined this code and/or display.
        This should only be used with code systems that do not enforce concept
        permanence.

        type: string
        """

        self.code = None
        """
        The code for this item in the expansion hierarchy. If this code is
        missing the entry in the hierarchy is a place holder (abstract) and
        does not represent a valid code in the value set.

        type: string
        """

        self.display = None
        """
        The recommended display for this item in the expansion.

        type: string
        """

        self.designation = None
        """
        Additional representations for this item - other languages, aliases,
        specialized purposes, used for particular purposes, etc. These are
        relevant when the conditions of the expansion do not fix to a single
        correct representation.

        type: array
        reference to ValueSet_Designation
        """

        self.contains = None
        """
        Other codes and entries contained under this entry in the hierarchy.

        type: array
        reference to ValueSet_Contains
        """

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
