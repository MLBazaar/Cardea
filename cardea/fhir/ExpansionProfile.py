from .fhirbase import fhirbase


class ExpansionProfile(fhirbase):
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile'

    def __init__(self, dict_values=None):
        self.resourceType = 'ExpansionProfile'
        """
        This is a ExpansionProfile resource

        type: string
        possible values: ExpansionProfile
        """

        self.url = None
        """
        An absolute URI that is used to identify this expansion profile when
        it is referenced in a specification, model, design or an instance.
        This SHALL be a URL, SHOULD be globally unique, and SHOULD be an
        address at which this expansion profile is (or will be) published. The
        URL SHOULD include the major version of the expansion profile. For
        more information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the expansion
        profile when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the expansion profile
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the expansion profile. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.status = None
        """
        The status of this expansion profile. Enables tracking the life-cycle
        of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this expansion profile is authored
        for testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the expansion profile was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the expansion profile
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the
        expansion profile.

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
        A free text natural language description of the expansion profile from
        a consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate expansion profile instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the expansion profile is
        intended to be used.

        type: array
        reference to CodeableConcept
        """

        self.fixedVersion = None
        """
        Fix use of a particular code system to a particular version.

        type: array
        reference to ExpansionProfile_FixedVersion
        """

        self.excludedSystem = None
        """
        Code system, or a particular version of a code system to be excluded
        from value set expansions.

        reference to ExpansionProfile_ExcludedSystem
        """

        self.includeDesignations = None
        """
        Controls whether concept designations are to be included or excluded
        in value set expansions.

        type: boolean
        """

        self.designation = None
        """
        A set of criteria that provide the constraints imposed on the value
        set expansion by including or excluding designations.

        reference to ExpansionProfile_Designation
        """

        self.includeDefinition = None
        """
        Controls whether the value set definition is included or excluded in
        value set expansions.

        type: boolean
        """

        self.activeOnly = None
        """
        Controls whether inactive concepts are included or excluded in value
        set expansions.

        type: boolean
        """

        self.excludeNested = None
        """
        Controls whether or not the value set expansion nests codes or not
        (i.e. ValueSet.expansion.contains.contains).

        type: boolean
        """

        self.excludeNotForUI = None
        """
        Controls whether or not the value set expansion includes codes which
        cannot be displayed in user interfaces.

        type: boolean
        """

        self.excludePostCoordinated = None
        """
        Controls whether or not the value set expansion includes post
        coordinated codes.

        type: boolean
        """

        self.displayLanguage = None
        """
        Specifies the language to be used for description in the expansions
        i.e. the language to be used for ValueSet.expansion.contains.display.

        type: string
        """

        self.limitedExpansion = None
        """
        If the value set being expanded is incomplete (because it is too big
        to expand), return a limited expansion (a subset) with an indicator
        that expansion is incomplete, using the extension
        [http://hl7.org/fhir/StructureDefinition/valueset-toocostly](extension-valueset-toocostly.html).

        type: boolean
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this expansion profile
        when it is represented in other formats, or referenced in a
        specification, model, design or an instance.

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'identifier'},

            {'parent_entity': 'ExpansionProfile_Designation',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'designation'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'useContext'},

            {'parent_entity': 'ExpansionProfile_ExcludedSystem',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'excludedSystem'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'contact'},

            {'parent_entity': 'ExpansionProfile_FixedVersion',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile',
             'child_variable': 'fixedVersion'},
        ]


class ExpansionProfile_FixedVersion(fhirbase):
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile_FixedVersion'

    def __init__(self, dict_values=None):
        self.system = None
        """
        The specific system for which to fix the version.

        type: string
        """

        self.version = None
        """
        The version of the code system from which codes in the expansion
        should be included.

        type: string
        """

        self.mode = None
        """
        How to manage the intersection between a fixed version in a value set,
        and this fixed version of the system in the expansion profile.

        type: string
        possible values: default, check, override
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile_ExcludedSystem'

    def __init__(self, dict_values=None):
        self.system = None
        """
        An absolute URI which is the code system to be excluded.

        type: string
        """

        self.version = None
        """
        The version of the code system from which codes in the expansion
        should be excluded.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class ExpansionProfile_Designation(fhirbase):
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile_Designation'

    def __init__(self, dict_values=None):
        self.include = None
        """
        Designations to be included.

        reference to ExpansionProfile_Include
        """

        self.exclude = None
        """
        Designations to be excluded.

        reference to ExpansionProfile_Exclude
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile_Include'

    def __init__(self, dict_values=None):
        self.designation = None
        """
        A data group for each designation to be included.

        type: array
        reference to ExpansionProfile_Designation1
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile_Designation1'

    def __init__(self, dict_values=None):
        self.language = None
        """
        The language this designation is defined for.

        type: string
        """

        self.use = None
        """
        Which kinds of designation to include in the expansion.

        reference to Coding
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile_Exclude'

    def __init__(self, dict_values=None):
        self.designation = None
        """
        A data group for each designation to be excluded.

        type: array
        reference to ExpansionProfile_Designation2
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """

    __name__ = 'ExpansionProfile_Designation2'

    def __init__(self, dict_values=None):
        self.language = None
        """
        The language this designation is defined for.

        type: string
        """

        self.use = None
        """
        Which kinds of designation to exclude from the expansion.

        reference to Coding
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ExpansionProfile_Designation2',
             'child_variable': 'use'},
        ]
