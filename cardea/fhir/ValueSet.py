from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .UsageContext import UsageContext
from .ContactDetail import ContactDetail

class ValueSet(fhirbase):
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # this is a valueset resource
        self.resourceType = 'ValueSet'
        # type = string
        # possible values = ValueSet

        # an absolute uri that is used to identify this value set when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this value set is (or will be) published. the url should include the
        # major version of the value set. for more information see [technical and
        # business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the value set
        # when it is referenced in a specification, model, design or instance.
        # this is an arbitrary value managed by the value set author and is not
        # expected to be globally unique. for example, it might be a timestamp
        # (e.g. yyyymmdd) if a managed version is not available. there is also no
        # expectation that versions can be placed in a lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the value set. this name should be
        # usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the value set.
        self.title = None
        # type = string

        # the status of this value set. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values = draft, active, retired, unknown

        # a boolean value to indicate that this value set is authored for testing
        # purposes (or education/evaluation/marketing), and is not intended to be
        # used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the value set was published. the
        # date must change if and when the business version changes and it must
        # change if the status code changes. in addition, it should change when
        # the substantive content of the value set changes. (e.g. the 'content
        # logical definition').
        self.date = None
        # type = string

        # the name of the individual or organization that published the value set.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the value set from a
        # consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate value set instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the value set is intended to be
        # used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # if this is set to 'true', then no new versions of the content logical
        # definition can be created.  note: other metadata might still change.
        self.immutable = None
        # type = boolean

        # explaination of why this value set is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the value set and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the value set.
        self.copyright = None
        # type = string

        # whether this is intended to be used with an extensible binding or not.
        self.extensible = None
        # type = boolean

        # a set of criteria that define the content logical definition of the
        # value set by including or excluding codes from outside this value set.
        # this i also known as the "content logical definition" (cld).
        self.compose = None
        # reference to ValueSet_Compose: ValueSet_Compose

        # a value set can also be "expanded", where the value set is turned into a
        # simple collection of enumerated codes. this element holds the expansion,
        # if it has been performed.
        self.expansion = None
        # reference to ValueSet_Expansion: identifier

        # a formal identifier that is used to identify this value set when it is
        # represented in other formats, or referenced in a specification, model,
        # design or an instance.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'ValueSet',
            'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'ValueSet',
            'child_variable': 'useContext'},

            {'parent_entity': 'ValueSet_Expansion',
            'parent_variable': 'identifier',
            'child_entity': 'ValueSet',
            'child_variable': 'expansion'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ValueSet',
            'child_variable': 'identifier'},

            {'parent_entity': 'ValueSet_Compose',
            'parent_variable': 'object_id',
            'child_entity': 'ValueSet',
            'child_variable': 'compose'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ValueSet',
            'child_variable': 'jurisdiction'},
        ]

class ValueSet_Compose(fhirbase):
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # if a locked date is defined, then the content logical definition must be
        # evaluated using the current version as of the locked date for referenced
        # code system(s) and value set instances where
        # valueset.compose.include.version is not defined.
        self.lockedDate = None
        # type = string

        # whether inactive codes - codes that are not approved for current use -
        # are in the value set. if inactive = true, inactive codes are to be
        # included in the expansion, if inactive = false, the inactive codes will
        # not be included in the expansion. if absent, the behavior is determined
        # by the implementation, or by the applicable expansionprofile (but
        # generally, inactive codes would be expected to be included).
        self.inactive = None
        # type = boolean

        # include one or more codes from a code system or other value set(s).
        self.include = None
        # type = array
        # reference to ValueSet_Include: ValueSet_Include

        # exclude one or more codes from the value set based on code system
        # filters and/or other value sets.
        self.exclude = None
        # type = array
        # reference to ValueSet_Include: ValueSet_Include


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
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # an absolute uri which is the code system from which the selected codes
        # come from.
        # an absolute uri which is the code system from which the selected codes
        # come from.
        self.system = None
        # type = string
        # type = string

        # the version of the code system that the codes are selected from.
        # the version of the code system that the codes are selected from.
        self.version = None
        # type = string
        # type = string

        # specifies a concept to be included or excluded.
        # specifies a concept to be included or excluded.
        self.concept = None
        # type = array
        # type = array
        # reference to ValueSet_Concept: ValueSet_Concept

        # select concepts by specify a matching criteria based on the properties
        # (including relationships) defined by the system. if multiple filters are
        # specified, they shall all be true.
        # select concepts by specify a matching criteria based on the properties
        # (including relationships) defined by the system. if multiple filters are
        # specified, they shall all be true.
        self.filter = None
        # type = array
        # type = array
        # reference to ValueSet_Filter: ValueSet_Filter

        # selects concepts found in this value set. this is an absolute uri that
        # is a reference to valueset.url.
        # selects concepts found in this value set. this is an absolute uri that
        # is a reference to valueset.url.
        self.valueSet = None
        # type = array
        # type = array


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
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # specifies a code for the concept to be included or excluded.
        # specifies a code for the concept to be included or excluded.
        self.code = None
        # type = string
        # type = string

        # the text to display to the user for this concept in the context of this
        # valueset. if no display is provided, then applications using the value
        # set use the display specified for the code by the system.
        # the text to display to the user for this concept in the context of this
        # valueset. if no display is provided, then applications using the value
        # set use the display specified for the code by the system.
        self.display = None
        # type = string
        # type = string

        # additional representations for this concept when used in this value set
        # - other languages, aliases, specialized purposes, used for particular
        # purposes, etc.
        # additional representations for this concept when used in this value set
        # - other languages, aliases, specialized purposes, used for particular
        # purposes, etc.
        self.designation = None
        # type = array
        # type = array
        # reference to ValueSet_Designation: ValueSet_Designation


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
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # the language this designation is defined for.
        # the language this designation is defined for.
        # the language this designation is defined for.
        # the language this designation is defined for.
        self.language = None
        # type = string
        # type = string
        # type = string
        # type = string

        # a code that details how this designation would be used.
        # a code that details how this designation would be used.
        # a code that details how this designation would be used.
        # a code that details how this designation would be used.
        self.use = None
        # reference to Coding: Coding

        # the text value for this designation.
        # the text value for this designation.
        # the text value for this designation.
        # the text value for this designation.
        self.value = None
        # type = string
        # type = string
        # type = string
        # type = string


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
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # a code that identifies a property defined in the code system.
        # a code that identifies a property defined in the code system.
        self.property = None
        # type = string
        # type = string

        # the kind of operation to perform as a part of the filter criteria.
        # the kind of operation to perform as a part of the filter criteria.
        self.op = None
        # type = string
        # type = string
        # possible values = =, is-a, descendent-of, is-not-a, regex, in, not-in, generalizes, exists
        # possible values = =, is-a, descendent-of, is-not-a, regex, in, not-in, generalizes, exists

        # the match value may be either a code defined by the system, or a string
        # value, which is a regex match on the literal string of the property
        # value when the operation is 'regex', or one of the values (true and
        # false), when the operation is 'exists'.
        # the match value may be either a code defined by the system, or a string
        # value, which is a regex match on the literal string of the property
        # value when the operation is 'regex', or one of the values (true and
        # false), when the operation is 'exists'.
        self.value = None
        # type = string
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.op is not None:
            for value in self.op:
                if value != None and value.lower() not in ['=', 'is-a', 'descendent-of', 'is-not-a', 'regex', 'in', 'not-in', 'generalizes', 'exists']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, '=, is-a, descendent-of, is-not-a, regex, in, not-in, generalizes, exists'))

        if self.op is not None:
            for value in self.op:
                if value != None and value.lower() not in ['=', 'is-a', 'descendent-of', 'is-not-a', 'regex', 'in', 'not-in', 'generalizes', 'exists']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, '=, is-a, descendent-of, is-not-a, regex, in, not-in, generalizes, exists'))

class ValueSet_Expansion(fhirbase):
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # the time at which the expansion was produced by the expanding system.
        self.timestamp = None
        # type = string

        # the total number of concepts in the expansion. if the number of concept
        # nodes in this resource is less than the stated number, then the server
        # can return more using the offset parameter.
        self.total = None
        # type = int

        # if paging is being used, the offset at which this resource starts.  i.e.
        # this resource is a partial view into the expansion. if paging is not
        # being used, this element shall not be present.
        self.offset = None
        # type = int

        # a parameter that controlled the expansion process. these parameters may
        # be used by users of expanded value sets to check whether the expansion
        # is suitable for a particular purpose, or to pick the correct expansion.
        self.parameter = None
        # type = array
        # reference to ValueSet_Parameter: ValueSet_Parameter

        # the codes that are contained in the value set expansion.
        self.contains = None
        # type = array
        # reference to ValueSet_Contains: ValueSet_Contains

        # an identifier that uniquely identifies this expansion of the valueset.
        # systems may re-use the same identifier as long as the expansion and the
        # definition remain the same, but are not required to do so.
        self.identifier = None
        # type = string


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
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # the name of the parameter.
        self.name = None
        # type = string

        # the value of the parameter.
        self.valueString = None
        # type = string

        # the value of the parameter.
        self.valueBoolean = None
        # type = boolean

        # the value of the parameter.
        self.valueInteger = None
        # type = int

        # the value of the parameter.
        self.valueDecimal = None
        # type = int

        # the value of the parameter.
        self.valueUri = None
        # type = string

        # the value of the parameter.
        self.valueCode = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


class ValueSet_Contains(fhirbase):
    """A value set specifies a set of codes drawn from one or more code
    systems.
    """

    def __init__(self, dict_values=None):
        # an absolute uri which is the code system in which the code for this item
        # in the expansion is defined.
        # an absolute uri which is the code system in which the code for this item
        # in the expansion is defined.
        self.system = None
        # type = string
        # type = string

        # if true, this entry is included in the expansion for navigational
        # purposes, and the user cannot select the code directly as a proper
        # value.
        # if true, this entry is included in the expansion for navigational
        # purposes, and the user cannot select the code directly as a proper
        # value.
        self.abstract = None
        # type = boolean
        # type = boolean

        # if the concept is inactive in the code system that defines it. inactive
        # codes are those that are no longer to be used, but are maintained by the
        # code system for understanding legacy data.
        # if the concept is inactive in the code system that defines it. inactive
        # codes are those that are no longer to be used, but are maintained by the
        # code system for understanding legacy data.
        self.inactive = None
        # type = boolean
        # type = boolean

        # the version of this code system that defined this code and/or display.
        # this should only be used with code systems that do not enforce concept
        # permanence.
        # the version of this code system that defined this code and/or display.
        # this should only be used with code systems that do not enforce concept
        # permanence.
        self.version = None
        # type = string
        # type = string

        # the code for this item in the expansion hierarchy. if this code is
        # missing the entry in the hierarchy is a place holder (abstract) and does
        # not represent a valid code in the value set.
        # the code for this item in the expansion hierarchy. if this code is
        # missing the entry in the hierarchy is a place holder (abstract) and does
        # not represent a valid code in the value set.
        self.code = None
        # type = string
        # type = string

        # the recommended display for this item in the expansion.
        # the recommended display for this item in the expansion.
        self.display = None
        # type = string
        # type = string

        # additional representations for this item - other languages, aliases,
        # specialized purposes, used for particular purposes, etc. these are
        # relevant when the conditions of the expansion do not fix to a single
        # correct representation.
        # additional representations for this item - other languages, aliases,
        # specialized purposes, used for particular purposes, etc. these are
        # relevant when the conditions of the expansion do not fix to a single
        # correct representation.
        self.designation = None
        # type = array
        # type = array
        # reference to ValueSet_Designation: ValueSet_Designation

        # other codes and entries contained under this entry in the hierarchy.
        # other codes and entries contained under this entry in the hierarchy.
        self.contains = None
        # type = array
        # type = array
        # reference to ValueSet_Contains: ValueSet_Contains


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'ValueSet_Designation',
            'parent_variable': 'object_id',
            'child_entity': 'ValueSet_Contains',
            'child_variable': 'designation'},

            {'parent_entity': 'ValueSet_Contains',
            'parent_variable': 'object_id',
            'child_entity': 'ValueSet_Contains',
            'child_variable': 'contains'},
        ]

