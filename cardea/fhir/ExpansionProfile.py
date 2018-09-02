from .fhirbase import fhirbase


class ExpansionProfile(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # this is a expansionprofile resource
        self.resourceType = 'ExpansionProfile'
        # type = string
        # possible values: ExpansionProfile

        # an absolute uri that is used to identify this expansion profile when it
        # is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this expansion profile is (or will be) published. the url should
        # include the major version of the expansion profile. for more information
        # see [technical and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the expansion
        # profile when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the expansion profile
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the expansion profile. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # the status of this expansion profile. enables tracking the life-cycle of
        # the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this expansion profile is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the expansion profile was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the expansion profile changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the expansion
        # profile.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the expansion profile from a
        # consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate expansion profile instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the expansion profile is intended
        # to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # fix use of a particular code system to a particular version.
        self.fixedVersion = None
        # type = array
        # reference to ExpansionProfile_FixedVersion: ExpansionProfile_FixedVersion

        # code system, or a particular version of a code system to be excluded
        # from value set expansions.
        self.excludedSystem = None
        # reference to ExpansionProfile_ExcludedSystem: ExpansionProfile_ExcludedSystem

        # controls whether concept designations are to be included or excluded in
        # value set expansions.
        self.includeDesignations = None
        # type = boolean

        # a set of criteria that provide the constraints imposed on the value set
        # expansion by including or excluding designations.
        self.designation = None
        # reference to ExpansionProfile_Designation: ExpansionProfile_Designation

        # controls whether the value set definition is included or excluded in
        # value set expansions.
        self.includeDefinition = None
        # type = boolean

        # controls whether inactive concepts are included or excluded in value set
        # expansions.
        self.activeOnly = None
        # type = boolean

        # controls whether or not the value set expansion nests codes or not (i.e.
        # valueset.expansion.contains.contains).
        self.excludeNested = None
        # type = boolean

        # controls whether or not the value set expansion includes codes which
        # cannot be displayed in user interfaces.
        self.excludeNotForUI = None
        # type = boolean

        # controls whether or not the value set expansion includes post
        # coordinated codes.
        self.excludePostCoordinated = None
        # type = boolean

        # specifies the language to be used for description in the expansions i.e.
        # the language to be used for valueset.expansion.contains.display.
        self.displayLanguage = None
        # type = string

        # if the value set being expanded is incomplete (because it is too big to
        # expand), return a limited expansion (a subset) with an indicator that
        # expansion is incomplete, using the extension
        # [http://hl7.org/fhir/structuredefinition/valueset-toocostly](extension-
        # valueset-toocostly.html).
        self.limitedExpansion = None
        # type = boolean

        # a formal identifier that is used to identify this expansion profile when
        # it is represented in other formats, or referenced in a specification,
        # model, design or an instance.
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

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'useContext'},

            {'parent_entity': 'ExpansionProfile_FixedVersion',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'fixedVersion'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'identifier'},

            {'parent_entity': 'ExpansionProfile_Designation',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'designation'},

            {'parent_entity': 'ExpansionProfile_ExcludedSystem',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'excludedSystem'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'jurisdiction'},
        ]


class ExpansionProfile_FixedVersion(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # the specific system for which to fix the version.
        self.system = None
        # type = string

        # the version of the code system from which codes in the expansion should
        # be included.
        self.version = None
        # type = string

        # how to manage the intersection between a fixed version in a value set,
        # and this fixed version of the system in the expansion profile.
        self.mode = None
        # type = string
        # possible values: default, check, override

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'default', 'check', 'override']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'default, check, override'))


class ExpansionProfile_ExcludedSystem(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # an absolute uri which is the code system to be excluded.
        self.system = None
        # type = string

        # the version of the code system from which codes in the expansion should
        # be excluded.
        self.version = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class ExpansionProfile_Designation(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # designations to be included.
        self.include = None
        # reference to ExpansionProfile_Include: ExpansionProfile_Include

        # designations to be excluded.
        self.exclude = None
        # reference to ExpansionProfile_Exclude: ExpansionProfile_Exclude

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ExpansionProfile_Include',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile_Designation',
             'child_variable': 'include'},

            {'parent_entity': 'ExpansionProfile_Exclude',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile_Designation',
             'child_variable': 'exclude'},
        ]


class ExpansionProfile_Include(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # a data group for each designation to be included.
        self.designation = None
        # type = array
        # reference to ExpansionProfile_Designation1: ExpansionProfile_Designation1

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ExpansionProfile_Designation1',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile_Include',
             'child_variable': 'designation'},
        ]


class ExpansionProfile_Designation1(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # the language this designation is defined for.
        self.language = None
        # type = string

        # which kinds of designation to include in the expansion.
        self.use = None
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile_Designation1',
             'child_variable': 'use'},
        ]


class ExpansionProfile_Exclude(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # a data group for each designation to be excluded.
        self.designation = None
        # type = array
        # reference to ExpansionProfile_Designation2: ExpansionProfile_Designation2

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ExpansionProfile_Designation2',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile_Exclude',
             'child_variable': 'designation'},
        ]


class ExpansionProfile_Designation2(fhirbase):
    """Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    def __init__(self, dict_values=None):
        # the language this designation is defined for.
        self.language = None
        # type = string

        # which kinds of designation to exclude from the expansion.
        self.use = None
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile_Designation2',
             'child_variable': 'use'},
        ]
