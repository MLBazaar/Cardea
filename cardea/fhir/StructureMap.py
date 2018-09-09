from .fhirbase import fhirbase


class StructureMap(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap'

    def __init__(self, dict_values=None):
        self.resourceType = 'StructureMap'
        """
        This is a StructureMap resource

        type: string
        possible values: StructureMap
        """

        self.url = None
        """
        An absolute URI that is used to identify this structure map when it is
        referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this structure map is (or will be) published. The URL SHOULD
        include the major version of the structure map. For more information
        see [Technical and Business Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the structure
        map when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the structure map
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the structure map. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the structure map.

        type: string
        """

        self.status = None
        """
        The status of this structure map. Enables tracking the life-cycle of
        the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this structure map is authored for
        testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the structure map was published.
        The date must change if and when the business version changes and it
        must change if the status code changes. In addition, it should change
        when the substantive content of the structure map changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the
        structure map.

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
        A free text natural language description of the structure map from a
        consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate structure map instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the structure map is intended to
        be used.

        type: array
        reference to CodeableConcept
        """

        self.purpose = None
        """
        Explaination of why this structure map is needed and why it has been
        designed as it has.

        type: string
        """

        self.copyright = None
        """
        A copyright statement relating to the structure map and/or its
        contents. Copyright statements are generally legal restrictions on the
        use and publishing of the structure map.

        type: string
        """

        self.structure = None
        """
        A structure definition used by this map. The structure definition may
        describe instances that are converted, or the instances that are
        produced.

        type: array
        reference to StructureMap_Structure
        """

        self._import = None
        """
        Other maps used by this map (canonical URLs).

        type: array
        """

        self.group = None
        """
        Organizes the mapping into managable chunks for human review/ease of
        maintenance.

        type: array
        reference to StructureMap_Group
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this structure map when
        it is represented in other formats, or referenced in a specification,
        model, design or an instance.

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'identifier'},

            {'parent_entity': 'StructureMap_Structure',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'structure'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'StructureMap_Group',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'group'},
        ]


class StructureMap_Structure(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Structure'

    def __init__(self, dict_values=None):
        self.url = None
        """
        The canonical URL that identifies the structure.

        type: string
        """

        self.mode = None
        """
        How the referenced structure is used in this mapping.

        type: string
        possible values: source, queried, target, produced
        """

        self.alias = None
        """
        The name used for this type in the map.

        type: string
        """

        self.documentation = None
        """
        Documentation that describes how the structure is used in the mapping.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'source', 'queried', 'target', 'produced']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'source, queried, target, produced'))


class StructureMap_Group(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Group'

    def __init__(self, dict_values=None):
        self.name = None
        """
        A unique name for the group for the convenience of human readers.

        type: string
        """

        self.extends = None
        """
        Another group that this group adds rules to.

        type: string
        """

        self.typeMode = None
        """
        If this is the default rule set to apply for thie source type, or this
        combination of types.

        type: string
        possible values: none, types, type-and-types
        """

        self.documentation = None
        """
        Additional supporting documentation that explains the purpose of the
        group and the types of mappings within it.

        type: string
        """

        self.input = None
        """
        A name assigned to an instance of data. The instance must be provided
        when the mapping is invoked.

        type: array
        reference to StructureMap_Input
        """

        self.rule = None
        """
        Transform Rule from source to target.

        type: array
        reference to StructureMap_Rule
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.typeMode is not None:
            for value in self.typeMode:
                if value is not None and value.lower() not in [
                        'none', 'types', 'type-and-types']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'none, types, type-and-types'))

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Group',
             'child_variable': 'rule'},

            {'parent_entity': 'StructureMap_Input',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Group',
             'child_variable': 'input'},
        ]


class StructureMap_Input(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Input'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Name for this instance of data.

        type: string
        """

        self.type = None
        """
        Type for this instance of data.

        type: string
        """

        self.mode = None
        """
        Mode for this instance of data.

        type: string
        possible values: source, target
        """

        self.documentation = None
        """
        Documentation for this instance of data.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'source', 'target']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'source, target'))


class StructureMap_Rule(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Rule'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Name of the rule for internal references.

        type: string
        """

        self.source = None
        """
        Source inputs to the mapping.

        type: array
        reference to StructureMap_Source
        """

        self.target = None
        """
        Content to create because of this mapping rule.

        type: array
        reference to StructureMap_Target
        """

        self.rule = None
        """
        Rules contained in this rule.

        type: array
        reference to StructureMap_Rule
        """

        self.dependent = None
        """
        Which other rules to apply in the context of this rule.

        type: array
        reference to StructureMap_Dependent
        """

        self.documentation = None
        """
        Documentation for this instance of data.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Dependent',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'dependent'},

            {'parent_entity': 'StructureMap_Source',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'source'},

            {'parent_entity': 'StructureMap_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'rule'},

            {'parent_entity': 'StructureMap_Target',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'target'},
        ]


class StructureMap_Source(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Source'

    def __init__(self, dict_values=None):
        self.context = None
        """
        Type or variable this rule applies to.

        type: string
        """

        self.min = None
        """
        Specified minimum cardinality for the element. This is optional; if
        present, it acts an implicit check on the input content.

        type: int
        """

        self.max = None
        """
        Specified maximum cardinality for the element - a number or a "*".
        This is optional; if present, it acts an implicit check on the input
        content (* just serves as documentation; it's the default value).

        type: string
        """

        self.type = None
        """
        Specified type for the element. This works as a condition on the
        mapping - use for polymorphic elements.

        type: string
        """

        self.defaultValueBoolean = None
        """
        A value to use if there is no existing value in the source object.

        type: boolean
        """

        self.defaultValueInteger = None
        """
        A value to use if there is no existing value in the source object.

        type: int
        """

        self.defaultValueDecimal = None
        """
        A value to use if there is no existing value in the source object.

        type: int
        """

        self.defaultValueBase64Binary = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueInstant = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueString = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueUri = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueDate = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueDateTime = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueTime = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueCode = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueOid = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueUuid = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueId = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueUnsignedInt = None
        """
        A value to use if there is no existing value in the source object.

        type: int
        """

        self.defaultValuePositiveInt = None
        """
        A value to use if there is no existing value in the source object.

        type: int
        """

        self.defaultValueMarkdown = None
        """
        A value to use if there is no existing value in the source object.

        type: string
        """

        self.defaultValueElement = None
        """
        A value to use if there is no existing value in the source object.

        reference to Element: id
        """

        self.defaultValueExtension = None
        """
        A value to use if there is no existing value in the source object.

        reference to Extension
        """

        self.defaultValueBackboneElement = None
        """
        A value to use if there is no existing value in the source object.

        reference to BackboneElement
        """

        self.defaultValueNarrative = None
        """
        A value to use if there is no existing value in the source object.

        reference to Narrative
        """

        self.defaultValueAnnotation = None
        """
        A value to use if there is no existing value in the source object.

        reference to Annotation
        """

        self.defaultValueAttachment = None
        """
        A value to use if there is no existing value in the source object.

        reference to Attachment
        """

        self.defaultValueIdentifier = None
        """
        A value to use if there is no existing value in the source object.

        reference to Identifier
        """

        self.defaultValueCodeableConcept = None
        """
        A value to use if there is no existing value in the source object.

        reference to CodeableConcept
        """

        self.defaultValueCoding = None
        """
        A value to use if there is no existing value in the source object.

        reference to Coding
        """

        self.defaultValueQuantity = None
        """
        A value to use if there is no existing value in the source object.

        reference to Quantity
        """

        self.defaultValueDuration = None
        """
        A value to use if there is no existing value in the source object.

        reference to Duration
        """

        self.defaultValueSimpleQuantity = None
        """
        A value to use if there is no existing value in the source object.

        reference to Quantity
        """

        self.defaultValueDistance = None
        """
        A value to use if there is no existing value in the source object.

        reference to Distance
        """

        self.defaultValueCount = None
        """
        A value to use if there is no existing value in the source object.

        reference to Count
        """

        self.defaultValueMoney = None
        """
        A value to use if there is no existing value in the source object.

        reference to Money
        """

        self.defaultValueAge = None
        """
        A value to use if there is no existing value in the source object.

        reference to Age
        """

        self.defaultValueRange = None
        """
        A value to use if there is no existing value in the source object.

        reference to Range
        """

        self.defaultValuePeriod = None
        """
        A value to use if there is no existing value in the source object.

        reference to Period
        """

        self.defaultValueRatio = None
        """
        A value to use if there is no existing value in the source object.

        reference to Ratio
        """

        self.defaultValueReference = None
        """
        A value to use if there is no existing value in the source object.

        reference to Reference: identifier
        """

        self.defaultValueSampledData = None
        """
        A value to use if there is no existing value in the source object.

        reference to SampledData
        """

        self.defaultValueSignature = None
        """
        A value to use if there is no existing value in the source object.

        reference to Signature
        """

        self.defaultValueHumanName = None
        """
        A value to use if there is no existing value in the source object.

        reference to HumanName
        """

        self.defaultValueAddress = None
        """
        A value to use if there is no existing value in the source object.

        reference to Address
        """

        self.defaultValueContactPoint = None
        """
        A value to use if there is no existing value in the source object.

        reference to ContactPoint
        """

        self.defaultValueTiming = None
        """
        A value to use if there is no existing value in the source object.

        reference to Timing
        """

        self.defaultValueMeta = None
        """
        A value to use if there is no existing value in the source object.

        reference to Meta
        """

        self.defaultValueElementDefinition = None
        """
        A value to use if there is no existing value in the source object.

        reference to ElementDefinition
        """

        self.defaultValueContactDetail = None
        """
        A value to use if there is no existing value in the source object.

        reference to ContactDetail
        """

        self.defaultValueContributor = None
        """
        A value to use if there is no existing value in the source object.

        reference to Contributor
        """

        self.defaultValueDosage = None
        """
        A value to use if there is no existing value in the source object.

        reference to Dosage
        """

        self.defaultValueRelatedArtifact = None
        """
        A value to use if there is no existing value in the source object.

        reference to RelatedArtifact
        """

        self.defaultValueUsageContext = None
        """
        A value to use if there is no existing value in the source object.

        reference to UsageContext
        """

        self.defaultValueDataRequirement = None
        """
        A value to use if there is no existing value in the source object.

        reference to DataRequirement
        """

        self.defaultValueParameterDefinition = None
        """
        A value to use if there is no existing value in the source object.

        reference to ParameterDefinition
        """

        self.defaultValueTriggerDefinition = None
        """
        A value to use if there is no existing value in the source object.

        reference to TriggerDefinition
        """

        self.element = None
        """
        Optional field for this source.

        type: string
        """

        self.listMode = None
        """
        How to handle the list mode for this element.

        type: string
        possible values: first, not_first, last, not_last, only_one
        """

        self.variable = None
        """
        Named context for field, if a field is specified.

        type: string
        """

        self.condition = None
        """
        FHIRPath expression  - must be true or the rule does not apply.

        type: string
        """

        self.check = None
        """
        FHIRPath expression  - must be true or the mapping engine throws an
        error instead of completing.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.listMode is not None:
            for value in self.listMode:
                if value is not None and value.lower() not in [
                        'first', 'not_first', 'last', 'not_last', 'only_one']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'first, not_first, last, not_last, only_one'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRatio'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueHumanName'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRange'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDuration'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDosage'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueIdentifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValuePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCodeableConcept'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContactPoint'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueMeta'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAttachment'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRelatedArtifact'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCoding'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCount'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSimpleQuantity'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueElement'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAge'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAnnotation'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueParameterDefinition'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueTriggerDefinition'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSampledData'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSignature'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueTiming'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDataRequirement'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueUsageContext'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueElementDefinition'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueExtension'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueMoney'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDistance'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueBackboneElement'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContributor'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueQuantity'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContactDetail'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAddress'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueNarrative'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueReference'},
        ]


class StructureMap_Target(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Target'

    def __init__(self, dict_values=None):
        self.context = None
        """
        Type or variable this rule applies to.

        type: string
        """

        self.contextType = None
        """
        How to interpret the context.

        type: string
        possible values: type, variable
        """

        self.element = None
        """
        Field to create in the context.

        type: string
        """

        self.variable = None
        """
        Named context for field, if desired, and a field is specified.

        type: string
        """

        self.listMode = None
        """
        If field is a list, how to manage the list.

        type: array
        possible values: first, share, last, collate
        """

        self.listRuleId = None
        """
        Internal rule reference for shared list items.

        type: string
        """

        self.transform = None
        """
        How the data is copied / created.

        type: string
        possible values: create, copy, truncate, escape, cast, append,
        translate, reference, dateOp, uuid, pointer, evaluate, cc, c, qty, id,
        cp
        """

        self.parameter = None
        """
        Parameters to the transform.

        type: array
        reference to StructureMap_Parameter
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.contextType is not None:
            for value in self.contextType:
                if value is not None and value.lower() not in [
                        'type', 'variable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'type, variable'))

        if self.listMode is not None:
            for value in self.listMode:
                if value is not None and value.lower() not in [
                        'first', 'share', 'last', 'collate']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'first, share, last, collate'))

        if self.transform is not None:
            for value in self.transform:
                if value is not None and value.lower() not in [
                    'create', 'copy', 'truncate', 'escape', 'cast', 'append', 'translate',
                    'reference', 'dateop', 'uuid', 'pointer', 'evaluate', 'cc', 'c',
                        'qty', 'id', 'cp']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'create, copy, truncate, escape, cast, append, translate, '
                        'reference, dateOp, uuid, pointer, evaluate, cc, c, qty, id, cp'))

        if self.contextType is not None:
            for value in self.contextType:
                if value is not None and value.lower() not in [
                        'type', 'variable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'type, variable'))

        if self.listMode is not None:
            for value in self.listMode:
                if value is not None and value.lower() not in [
                        'first', 'share', 'last', 'collate']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'first, share, last, collate'))

        if self.transform is not None:
            for value in self.transform:
                if value is not None and value.lower() not in [
                    'create', 'copy', 'truncate', 'escape', 'cast', 'append', 'translate',
                    'reference', 'dateop', 'uuid', 'pointer', 'evaluate', 'cc', 'c',
                        'qty', 'id', 'cp']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'create, copy, truncate, escape, cast, append, translate, '
                        'reference, dateOp, uuid, pointer, evaluate, cc, c, qty, id, cp'))

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Target',
             'child_variable': 'parameter'},
        ]


class StructureMap_Parameter(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Parameter'

    def __init__(self, dict_values=None):
        self.valueId = None
        """
        Parameter value - variable or literal.

        type: string
        """

        self.valueString = None
        """
        Parameter value - variable or literal.

        type: string
        """

        self.valueBoolean = None
        """
        Parameter value - variable or literal.

        type: boolean
        """

        self.valueInteger = None
        """
        Parameter value - variable or literal.

        type: int
        """

        self.valueDecimal = None
        """
        Parameter value - variable or literal.

        type: int
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class StructureMap_Dependent(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Dependent'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Name of a rule or group to apply.

        type: string
        """

        self.variable = None
        """
        Variable to pass to the rule or group.

        type: array
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
