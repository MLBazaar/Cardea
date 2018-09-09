from .fhirbase import fhirbase


class StructureDefinition(fhirbase):
    """A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition'

    def __init__(self, dict_values=None):
        # this is a structuredefinition resource
        self.resourceType = 'StructureDefinition'
        # type = string
        # possible values: StructureDefinition

        # an absolute uri that is used to identify this structure definition when
        # it is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this structure definition is (or will be) published. the url
        # should include the major version of the structure definition. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the structure
        # definition when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the structure definition
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the structure definition. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the structure definition.
        self.title = None
        # type = string

        # the status of this structure definition. enables tracking the life-cycle
        # of the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this structure definition is authored
        # for testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the structure definition was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the structure definition changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the structure
        # definition.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the structure definition
        # from a consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate structure definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the structure definition is
        # intended to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this structure definition is needed and why it has
        # been designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the structure definition and/or its
        # contents. copyright statements are generally legal restrictions on the
        # use and publishing of the structure definition.
        self.copyright = None
        # type = string

        # a set of key words or terms from external terminologies that may be used
        # to assist with indexing and searching of templates.
        self.keyword = None
        # type = array
        # reference to Coding: Coding

        # the version of the fhir specification on which this structuredefinition
        # is based - this is the formal version of the specification, without the
        # revision number, e.g. [publication].[major].[minor], which is 3.0.1 for
        # this version.
        self.fhirVersion = None
        # type = string

        # an external specification that the content is mapped to.
        self.mapping = None
        # type = array
        # reference to StructureDefinition_Mapping: StructureDefinition_Mapping

        # defines the kind of structure that this definition is describing.
        self.kind = None
        # type = string
        # possible values: primitive-type, complex-type, resource,
        # logical

        # whether structure this definition describes is abstract or not  - that
        # is, whether the structure is not intended to be instantiated. for
        # resources and data types, abstract types will never be exchanged
        # between systems.
        self.abstract = None
        # type = boolean

        # if this is an extension, identifies the context within fhir resources
        # where the extension can be used.
        self.contextType = None
        # type = string
        # possible values: resource, datatype, extension

        # identifies the types of resource or data type elements to which the
        # extension can be applied.
        self.context = None
        # type = array

        # a set of rules as fluent invariants about when the extension can be used
        # (e.g. co-occurrence variants for the extension).
        self.contextInvariant = None
        # type = array

        # the type this structure describes. if the derivation kind is
        # 'specialization' then this is the master definition for a type, and
        # there is always one of these (a data type, an extension, a resource,
        # including abstract ones). otherwise the structure definition is a
        # constraint on the stated type (and in this case, the type cannot be an
        # abstract type).
        self.type = None
        # type = string

        # an absolute uri that is the base structure from which this type is
        # derived, either by specialization or constraint.
        self.baseDefinition = None
        # type = string

        # how the type relates to the basedefinition.
        self.derivation = None
        # type = string
        # possible values: specialization, constraint

        # a snapshot view is expressed in a stand alone form that can be used and
        # interpreted without considering the base structuredefinition.
        self.snapshot = None
        # reference to StructureDefinition_Snapshot: StructureDefinition_Snapshot

        # a differential view is expressed relative to the base
        # structuredefinition - a statement of differences that it applies.
        self.differential = None
        # reference to StructureDefinition_Differential: StructureDefinition_Differential

        # a formal identifier that is used to identify this structure definition
        # when it is represented in other formats, or referenced in a
        # specification, model, design or an instance.
        self.identifier = None
        # type = array
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
            {'parent_entity': 'StructureDefinition_Mapping',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'mapping'},

            {'parent_entity': 'StructureDefinition_Snapshot',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'snapshot'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'keyword'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'StructureDefinition_Differential',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'differential'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition',
             'child_variable': 'identifier'},
        ]


class StructureDefinition_Mapping(fhirbase):
    """A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition_Mapping'

    def __init__(self, dict_values=None):
        # an internal id that is used to identify this mapping set when specific
        # mappings are made.
        self.identity = None
        # type = string

        # an absolute uri that identifies the specification that this mapping is
        # expressed to.
        self.uri = None
        # type = string

        # a name for the specification that is being mapped to.
        self.name = None
        # type = string

        # comments about this mapping, including version notes, issues, scope
        # limitations, and other important notes for usage.
        self.comment = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class StructureDefinition_Snapshot(fhirbase):
    """A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition_Snapshot'

    def __init__(self, dict_values=None):
        # captures constraints on each element within the resource.
        self.element = None
        # type = array
        # reference to ElementDefinition: ElementDefinition

        # unique identifier for object class
        self.object_id = None

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
    """A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for
    describing extensions and constraints on resources and data types.
    """

    __name__ = 'StructureDefinition_Differential'

    def __init__(self, dict_values=None):
        # captures constraints on each element within the resource.
        self.element = None
        # type = array
        # reference to ElementDefinition: ElementDefinition

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureDefinition_Differential',
             'child_variable': 'element'},
        ]
