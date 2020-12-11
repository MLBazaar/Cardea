from .fhirbase import fhirbase


class StructureDefinition(fhirbase):
    """
    A definition of a FHIR structure. This resource is used to describe
    the underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.

    Args:
        resourceType: This is a StructureDefinition resource
        url: An absolute URI that is used to identify this structure
            definition when it is referenced in a specification, model, design or
            an instance. This SHALL be a URL, SHOULD be globally unique, and
            SHOULD be an address at which this structure definition is (or will
            be) published. The URL SHOULD include the major version of the
            structure definition. For more information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this
            structure definition when it is represented in other formats, or
            referenced in a specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            structure definition when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the
            structure definition author and is not expected to be globally unique.
            For example, it might be a timestamp (e.g. yyyymmdd) if a managed
            version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.
        name: A natural language name identifying the structure definition.
            This name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        title: A short, descriptive, user-friendly title for the structure
            definition.
        status: The status of this structure definition. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this structure
            definition is authored for testing purposes (or
            education/evaluation/marketing), and is not intended to be used for
            genuine usage.
        date: The date  (and optionally time) when the structure definition
            was published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the structure definition
            changes.
        publisher: The name of the individual or organization that published
            the structure definition.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the structure
            definition from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate structure
            definition instances.
        jurisdiction: A legal or geographic region in which the structure
            definition is intended to be used.
        purpose: Explaination of why this structure definition is needed and
            why it has been designed as it has.
        copyright: A copyright statement relating to the structure definition
            and/or its contents. Copyright statements are generally legal
            restrictions on the use and publishing of the structure definition.
        keyword: A set of key words or terms from external terminologies that
            may be used to assist with indexing and searching of templates.
        fhirVersion: The version of the FHIR specification on which this
            StructureDefinition is based - this is the formal version of the
            specification, without the revision number, e.g.
            [publication].[major].[minor], which is 3.0.1 for this version.
        mapping: An external specification that the content is mapped to.
        kind: Defines the kind of structure that this definition is
            describing.
        abstract: Whether structure this definition describes is abstract or
            not  - that is, whether the structure is not intended to be
            instantiated. For Resources and Data types, abstract types will never
            be exchanged  between systems.
        contextType: If this is an extension, Identifies the context within
            FHIR resources where the extension can be used.
        context: Identifies the types of resource or data type elements to
            which the extension can be applied.
        contextInvariant: A set of rules as Fluent Invariants about when the
            extension can be used (e.g. co-occurrence variants for the extension).
        type: The type this structure describes. If the derivation kind is
            'specialization' then this is the master definition for a type, and
            there is always one of these (a data type, an extension, a resource,
            including abstract ones). Otherwise the structure definition is a
            constraint on the stated type (and in this case, the type cannot be an
            abstract type).
        baseDefinition: An absolute URI that is the base structure from which
            this type is derived, either by specialization or constraint.
        derivation: How the type relates to the baseDefinition.
        snapshot: A snapshot view is expressed in a stand alone form that can
            be used and interpreted without considering the base
            StructureDefinition.
        differential: A differential view is expressed relative to the base
            StructureDefinition - a statement of differences that it applies.
    """

    __name__ = 'StructureDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'StructureDefinition'
        # type: str
        # possible values: StructureDefinition

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

        self.keyword = None
        # type: list
        # reference to Coding

        self.fhirVersion = None
        # type: str

        self.mapping = None
        # type: list
        # reference to StructureDefinition_Mapping

        self.kind = None
        # type: str
        # possible values: primitive-type, complex-type, resource,
        # logical

        self.abstract = None
        # type: bool

        self.contextType = None
        # type: str
        # possible values: resource, datatype, extension

        self.context = None
        # type: list

        self.contextInvariant = None
        # type: list

        self.type = None
        # type: str

        self.baseDefinition = None
        # type: str

        self.derivation = None
        # type: str
        # possible values: specialization, constraint

        self.snapshot = None
        # reference to StructureDefinition_Snapshot

        self.differential = None
        # reference to StructureDefinition_Differential

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
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'keyword'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'StructureDefinition_Differential',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'differential'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'StructureDefinition_Mapping',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'mapping'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'StructureDefinition_Snapshot',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'snapshot'},
        ]


class StructureDefinition_Mapping(fhirbase):
    """
    A definition of a FHIR structure. This resource is used to describe
    the underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.

    Args:
        identity: An Internal id that is used to identify this mapping set
            when specific mappings are made.
        uri: An absolute URI that identifies the specification that this
            mapping is expressed to.
        name: A name for the specification that is being mapped to.
        comment: Comments about this mapping, including version notes, issues,
            scope limitations, and other important notes for usage.
    """

    __name__ = 'StructureDefinition_Mapping'

    def __init__(self, dict_values=None):
        self.identity = None
        # type: str

        self.uri = None
        # type: str

        self.name = None
        # type: str

        self.comment = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class StructureDefinition_Snapshot(fhirbase):
    """
    A definition of a FHIR structure. This resource is used to describe
    the underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.

    Args:
        element: Captures constraints on each element within the resource.
    """

    __name__ = 'StructureDefinition_Snapshot'

    def __init__(self, dict_values=None):
        self.element = None
        # type: list
        # reference to ElementDefinition

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

    Args:
        element: Captures constraints on each element within the resource.
    """

    __name__ = 'StructureDefinition_Differential'

    def __init__(self, dict_values=None):
        self.element = None
        # type: list
        # reference to ElementDefinition

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
