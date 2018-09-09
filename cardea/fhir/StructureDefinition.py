from .fhirbase import fhirbase


class StructureDefinition(fhirbase):
    """
    A definition of a FHIR structure. This resource is used to describe
    the underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'StructureDefinition'
        """
        This is a StructureDefinition resource

        type: string
        possible values: StructureDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this structure definition
        when it is referenced in a specification, model, design or an
        instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
        be an address at which this structure definition is (or will be)
        published. The URL SHOULD include the major version of the structure
        definition. For more information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the structure
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the structure
        definition author and is not expected to be globally unique. For
        example, it might be a timestamp (e.g. yyyymmdd) if a managed version
        is not available. There is also no expectation that versions can be
        placed in a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the structure definition. This
        name should be usable as an identifier for the module by machine
        processing applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the structure
        definition.

        type: string
        """

        self.status = None
        """
        The status of this structure definition. Enables tracking the
        life-cycle of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this structure definition is authored
        for testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the structure definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the structure definition
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the
        structure definition.

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
        A free text natural language description of the structure definition
        from a consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate structure definition instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the structure definition is
        intended to be used.

        type: array
        reference to CodeableConcept
        """

        self.purpose = None
        """
        Explaination of why this structure definition is needed and why it has
        been designed as it has.

        type: string
        """

        self.copyright = None
        """
        A copyright statement relating to the structure definition and/or its
        contents. Copyright statements are generally legal restrictions on the
        use and publishing of the structure definition.

        type: string
        """

        self.keyword = None
        """
        A set of key words or terms from external terminologies that may be
        used to assist with indexing and searching of templates.

        type: array
        reference to Coding
        """

        self.fhirVersion = None
        """
        The version of the FHIR specification on which this
        StructureDefinition is based - this is the formal version of the
        specification, without the revision number, e.g.
        [publication].[major].[minor], which is 3.0.1 for this version.

        type: string
        """

        self.mapping = None
        """
        An external specification that the content is mapped to.

        type: array
        reference to StructureDefinition_Mapping
        """

        self.kind = None
        """
        Defines the kind of structure that this definition is describing.

        type: string
        possible values: primitive-type, complex-type, resource,
        logical
        """

        self.abstract = None
        """
        Whether structure this definition describes is abstract or not  - that
        is, whether the structure is not intended to be instantiated. For
        Resources and Data types, abstract types will never be exchanged
        between systems.

        type: boolean
        """

        self.contextType = None
        """
        If this is an extension, Identifies the context within FHIR resources
        where the extension can be used.

        type: string
        possible values: resource, datatype, extension
        """

        self.context = None
        """
        Identifies the types of resource or data type elements to which the
        extension can be applied.

        type: array
        """

        self.contextInvariant = None
        """
        A set of rules as Fluent Invariants about when the extension can be
        used (e.g. co-occurrence variants for the extension).

        type: array
        """

        self.type = None
        """
        The type this structure describes. If the derivation kind is
        'specialization' then this is the master definition for a type, and
        there is always one of these (a data type, an extension, a resource,
        including abstract ones). Otherwise the structure definition is a
        constraint on the stated type (and in this case, the type cannot be an
        abstract type).

        type: string
        """

        self.baseDefinition = None
        """
        An absolute URI that is the base structure from which this type is
        derived, either by specialization or constraint.

        type: string
        """

        self.derivation = None
        """
        How the type relates to the baseDefinition.

        type: string
        possible values: specialization, constraint
        """

        self.snapshot = None
        """
        A snapshot view is expressed in a stand alone form that can be used
        and interpreted without considering the base StructureDefinition.

        reference to StructureDefinition_Snapshot
        """

        self.differential = None
        """
        A differential view is expressed relative to the base
        StructureDefinition - a statement of differences that it applies.

        reference to StructureDefinition_Differential
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this structure definition
        when it is represented in other formats, or referenced in a
        specification, model, design or an instance.

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

        if self.kind is not None:
            for value in self.kind:
                if value is not None and value.lower() not in [
                        'primitive-type', 'complex-type', 'resource', 'logical']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'primitive-type, complex-type, resource, logical'))

        if self.contextType is not None:
            for value in self.contextType:
                if value is not None and value.lower() not in [
                        'resource', 'datatype', 'extension']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'resource, datatype, extension'))

        if self.derivation is not None:
            for value in self.derivation:
                if value is not None and value.lower() not in [
                        'specialization', 'constraint']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'specialization, constraint'))

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureDefinition_Snapshot',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'snapshot'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'keyword'},

            {'parent_entity': 'StructureDefinition_Mapping',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'mapping'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'StructureDefinition_Differential',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'differential'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'contact'},
        ]


class StructureDefinition_Mapping(fhirbase):
    """
    A definition of a FHIR structure. This resource is used to describe
    the underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition_Mapping'

    def __init__(self, dict_values=None):
        self.identity = None
        """
        An Internal id that is used to identify this mapping set when specific
        mappings are made.

        type: string
        """

        self.uri = None
        """
        An absolute URI that identifies the specification that this mapping is
        expressed to.

        type: string
        """

        self.name = None
        """
        A name for the specification that is being mapped to.

        type: string
        """

        self.comment = None
        """
        Comments about this mapping, including version notes, issues, scope
        limitations, and other important notes for usage.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class StructureDefinition_Snapshot(fhirbase):
    """
    A definition of a FHIR structure. This resource is used to describe
    the underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition_Snapshot'

    def __init__(self, dict_values=None):
        self.element = None
        """
        Captures constraints on each element within the resource.

        type: array
        reference to ElementDefinition
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition_Snapshot',
             'child_variable': 'element'},
        ]


class StructureDefinition_Differential(fhirbase):
    """
    A definition of a FHIR structure. This resource is used to describe
    the underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition_Differential'

    def __init__(self, dict_values=None):
        self.element = None
        """
        Captures constraints on each element within the resource.

        type: array
        reference to ElementDefinition
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition_Differential',
             'child_variable': 'element'},
        ]
