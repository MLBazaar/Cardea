from .fhirbase import fhirbase


class StructureMap(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.

    Args:
        resourceType: This is a StructureMap resource
        url: An absolute URI that is used to identify this structure map when
            it is referenced in a specification, model, design or an instance.
            This SHALL be a URL, SHOULD be globally unique, and SHOULD be an
            address at which this structure map is (or will be) published. The URL
            SHOULD include the major version of the structure map. For more
            information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this
            structure map when it is represented in other formats, or referenced
            in a specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            structure map when it is referenced in a specification, model, design
            or instance. This is an arbitrary value managed by the structure map
            author and is not expected to be globally unique. For example, it
            might be a timestamp (e.g. yyyymmdd) if a managed version is not
            available. There is also no expectation that versions can be placed in
            a lexicographical sequence.
        name: A natural language name identifying the structure map. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the structure
            map.
        status: The status of this structure map. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this structure map is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the structure map was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the structure map
            changes.
        publisher: The name of the individual or organization that published
            the structure map.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the structure
            map from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate structure map
            instances.
        jurisdiction: A legal or geographic region in which the structure map
            is intended to be used.
        purpose: Explaination of why this structure map is needed and why it
            has been designed as it has.
        copyright: A copyright statement relating to the structure map and/or
            its contents. Copyright statements are generally legal restrictions on
            the use and publishing of the structure map.
        structure: A structure definition used by this map. The structure
            definition may describe instances that are converted, or the instances
            that are produced.
        import: Other maps used by this map (canonical URLs).
        group: Organizes the mapping into managable chunks for human
            review/ease of maintenance.
    """

    __name__ = 'StructureMap'

    def __init__(self, dict_values=None):
        self.resourceType = 'StructureMap'
        # type: str
        # possible values: StructureMap

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

        self.structure = None
        # type: list
        # reference to StructureMap_Structure

        self._import = None
        # type: list

        self.group = None
        # type: list
        # reference to StructureMap_Group

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'useContext'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'contact'},

            {'parent_entity': 'StructureMap_Group',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'group'},

            {'parent_entity': 'StructureMap_Structure',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'structure'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'identifier'},
        ]


class StructureMap_Structure(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.

    Args:
        url: The canonical URL that identifies the structure.
        mode: How the referenced structure is used in this mapping.
        alias: The name used for this type in the map.
        documentation: Documentation that describes how the structure is used
            in the mapping.
    """

    __name__ = 'StructureMap_Structure'

    def __init__(self, dict_values=None):
        self.url = None
        # type: str

        self.mode = None
        # type: str
        # possible values: source, queried, target, produced

        self.alias = None
        # type: str

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        name: A unique name for the group for the convenience of human
            readers.
        extends: Another group that this group adds rules to.
        typeMode: If this is the default rule set to apply for thie source
            type, or this combination of types.
        documentation: Additional supporting documentation that explains the
            purpose of the group and the types of mappings within it.
        input: A name assigned to an instance of data. The instance must be
            provided when the mapping is invoked.
        rule: Transform Rule from source to target.
    """

    __name__ = 'StructureMap_Group'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.extends = None
        # type: str

        self.typeMode = None
        # type: str
        # possible values: none, types, type-and-types

        self.documentation = None
        # type: str

        self.input = None
        # type: list
        # reference to StructureMap_Input

        self.rule = None
        # type: list
        # reference to StructureMap_Rule

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.typeMode is not None:
            for value in self.typeMode:
                if value is not None and value.lower() not in [
                        'none', 'types', 'type-and-types']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'none, types, type-and-types'))

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Input',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Group',
             'child_variable': 'input'},

            {'parent_entity': 'StructureMap_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Group',
             'child_variable': 'rule'},
        ]


class StructureMap_Input(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.

    Args:
        name: Name for this instance of data.
        type: Type for this instance of data.
        mode: Mode for this instance of data.
        documentation: Documentation for this instance of data.
    """

    __name__ = 'StructureMap_Input'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.type = None
        # type: str

        self.mode = None
        # type: str
        # possible values: source, target

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        name: Name of the rule for internal references.
        source: Source inputs to the mapping.
        target: Content to create because of this mapping rule.
        rule: Rules contained in this rule.
        dependent: Which other rules to apply in the context of this rule.
        documentation: Documentation for this instance of data.
    """

    __name__ = 'StructureMap_Rule'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.source = None
        # type: list
        # reference to StructureMap_Source

        self.target = None
        # type: list
        # reference to StructureMap_Target

        self.rule = None
        # type: list
        # reference to StructureMap_Rule

        self.dependent = None
        # type: list
        # reference to StructureMap_Dependent

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Source',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'source'},

            {'parent_entity': 'StructureMap_Dependent',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'dependent'},

            {'parent_entity': 'StructureMap_Target',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'target'},

            {'parent_entity': 'StructureMap_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'rule'},
        ]


class StructureMap_Source(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.

    Args:
        context: Type or variable this rule applies to.
        min: Specified minimum cardinality for the element. This is optional;
            if present, it acts an implicit check on the input content.
        max: Specified maximum cardinality for the element - a number or a
            "*". This is optional; if present, it acts an implicit check on the
            input content (* just serves as documentation; it's the default
            value).
        type: Specified type for the element. This works as a condition on the
            mapping - use for polymorphic elements.
        defaultValueBoolean: A value to use if there is no existing value in
            the source object.
        defaultValueInteger: A value to use if there is no existing value in
            the source object.
        defaultValueDecimal: A value to use if there is no existing value in
            the source object.
        defaultValueBase64Binary: A value to use if there is no existing value
            in the source object.
        defaultValueInstant: A value to use if there is no existing value in
            the source object.
        defaultValueString: A value to use if there is no existing value in
            the source object.
        defaultValueUri: A value to use if there is no existing value in the
            source object.
        defaultValueDate: A value to use if there is no existing value in the
            source object.
        defaultValueDateTime: A value to use if there is no existing value in
            the source object.
        defaultValueTime: A value to use if there is no existing value in the
            source object.
        defaultValueCode: A value to use if there is no existing value in the
            source object.
        defaultValueOid: A value to use if there is no existing value in the
            source object.
        defaultValueUuid: A value to use if there is no existing value in the
            source object.
        defaultValueId: A value to use if there is no existing value in the
            source object.
        defaultValueUnsignedInt: A value to use if there is no existing value
            in the source object.
        defaultValuePositiveInt: A value to use if there is no existing value
            in the source object.
        defaultValueMarkdown: A value to use if there is no existing value in
            the source object.
        defaultValueElement: A value to use if there is no existing value in
            the source object.
        defaultValueExtension: A value to use if there is no existing value in
            the source object.
        defaultValueBackboneElement: A value to use if there is no existing
            value in the source object.
        defaultValueNarrative: A value to use if there is no existing value in
            the source object.
        defaultValueAnnotation: A value to use if there is no existing value
            in the source object.
        defaultValueAttachment: A value to use if there is no existing value
            in the source object.
        defaultValueIdentifier: A value to use if there is no existing value
            in the source object.
        defaultValueCodeableConcept: A value to use if there is no existing
            value in the source object.
        defaultValueCoding: A value to use if there is no existing value in
            the source object.
        defaultValueQuantity: A value to use if there is no existing value in
            the source object.
        defaultValueDuration: A value to use if there is no existing value in
            the source object.
        defaultValueSimpleQuantity: A value to use if there is no existing
            value in the source object.
        defaultValueDistance: A value to use if there is no existing value in
            the source object.
        defaultValueCount: A value to use if there is no existing value in the
            source object.
        defaultValueMoney: A value to use if there is no existing value in the
            source object.
        defaultValueAge: A value to use if there is no existing value in the
            source object.
        defaultValueRange: A value to use if there is no existing value in the
            source object.
        defaultValuePeriod: A value to use if there is no existing value in
            the source object.
        defaultValueRatio: A value to use if there is no existing value in the
            source object.
        defaultValueReference: A value to use if there is no existing value in
            the source object.
        defaultValueSampledData: A value to use if there is no existing value
            in the source object.
        defaultValueSignature: A value to use if there is no existing value in
            the source object.
        defaultValueHumanName: A value to use if there is no existing value in
            the source object.
        defaultValueAddress: A value to use if there is no existing value in
            the source object.
        defaultValueContactPoint: A value to use if there is no existing value
            in the source object.
        defaultValueTiming: A value to use if there is no existing value in
            the source object.
        defaultValueMeta: A value to use if there is no existing value in the
            source object.
        defaultValueElementDefinition: A value to use if there is no existing
            value in the source object.
        defaultValueContactDetail: A value to use if there is no existing
            value in the source object.
        defaultValueContributor: A value to use if there is no existing value
            in the source object.
        defaultValueDosage: A value to use if there is no existing value in
            the source object.
        defaultValueRelatedArtifact: A value to use if there is no existing
            value in the source object.
        defaultValueUsageContext: A value to use if there is no existing value
            in the source object.
        defaultValueDataRequirement: A value to use if there is no existing
            value in the source object.
        defaultValueParameterDefinition: A value to use if there is no
            existing value in the source object.
        defaultValueTriggerDefinition: A value to use if there is no existing
            value in the source object.
        element: Optional field for this source.
        listMode: How to handle the list mode for this element.
        variable: Named context for field, if a field is specified.
        condition: FHIRPath expression  - must be true or the rule does not
            apply.
        check: FHIRPath expression  - must be true or the mapping engine
            throws an error instead of completing.
    """

    __name__ = 'StructureMap_Source'

    def __init__(self, dict_values=None):
        self.context = None
        # type: str

        self.min = None
        # type: int

        self.max = None
        # type: str

        self.type = None
        # type: str

        self.defaultValueBoolean = None
        # type: bool

        self.defaultValueInteger = None
        # type: int

        self.defaultValueDecimal = None
        # type: int

        self.defaultValueBase64Binary = None
        # type: str

        self.defaultValueInstant = None
        # type: str

        self.defaultValueString = None
        # type: str

        self.defaultValueUri = None
        # type: str

        self.defaultValueDate = None
        # type: str

        self.defaultValueDateTime = None
        # type: str

        self.defaultValueTime = None
        # type: str

        self.defaultValueCode = None
        # type: str

        self.defaultValueOid = None
        # type: str

        self.defaultValueUuid = None
        # type: str

        self.defaultValueId = None
        # type: str

        self.defaultValueUnsignedInt = None
        # type: int

        self.defaultValuePositiveInt = None
        # type: int

        self.defaultValueMarkdown = None
        # type: str

        self.defaultValueElement = None
        # reference to Element: id

        self.defaultValueExtension = None
        # reference to Extension

        self.defaultValueBackboneElement = None
        # reference to BackboneElement

        self.defaultValueNarrative = None
        # reference to Narrative

        self.defaultValueAnnotation = None
        # reference to Annotation

        self.defaultValueAttachment = None
        # reference to Attachment

        self.defaultValueIdentifier = None
        # reference to Identifier

        self.defaultValueCodeableConcept = None
        # reference to CodeableConcept

        self.defaultValueCoding = None
        # reference to Coding

        self.defaultValueQuantity = None
        # reference to Quantity

        self.defaultValueDuration = None
        # reference to Duration

        self.defaultValueSimpleQuantity = None
        # reference to Quantity

        self.defaultValueDistance = None
        # reference to Distance

        self.defaultValueCount = None
        # reference to Count

        self.defaultValueMoney = None
        # reference to Money

        self.defaultValueAge = None
        # reference to Age

        self.defaultValueRange = None
        # reference to Range

        self.defaultValuePeriod = None
        # reference to Period

        self.defaultValueRatio = None
        # reference to Ratio

        self.defaultValueReference = None
        # reference to Reference: identifier

        self.defaultValueSampledData = None
        # reference to SampledData

        self.defaultValueSignature = None
        # reference to Signature

        self.defaultValueHumanName = None
        # reference to HumanName

        self.defaultValueAddress = None
        # reference to Address

        self.defaultValueContactPoint = None
        # reference to ContactPoint

        self.defaultValueTiming = None
        # reference to Timing

        self.defaultValueMeta = None
        # reference to Meta

        self.defaultValueElementDefinition = None
        # reference to ElementDefinition

        self.defaultValueContactDetail = None
        # reference to ContactDetail

        self.defaultValueContributor = None
        # reference to Contributor

        self.defaultValueDosage = None
        # reference to Dosage

        self.defaultValueRelatedArtifact = None
        # reference to RelatedArtifact

        self.defaultValueUsageContext = None
        # reference to UsageContext

        self.defaultValueDataRequirement = None
        # reference to DataRequirement

        self.defaultValueParameterDefinition = None
        # reference to ParameterDefinition

        self.defaultValueTriggerDefinition = None
        # reference to TriggerDefinition

        self.element = None
        # type: str

        self.listMode = None
        # type: str
        # possible values: first, not_first, last, not_last, only_one

        self.variable = None
        # type: str

        self.condition = None
        # type: str

        self.check = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.listMode is not None:
            for value in self.listMode:
                if value is not None and value.lower() not in [
                        'first', 'not_first', 'last', 'not_last', 'only_one']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'first, not_first, last, not_last, only_one'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueMoney'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDuration'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContactPoint'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueIdentifier'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContributor'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueHumanName'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueBackboneElement'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueTriggerDefinition'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueTiming'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDosage'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSampledData'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueExtension'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSimpleQuantity'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAge'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAttachment'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAddress'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRatio'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValuePeriod'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueMeta'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCount'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRelatedArtifact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueUsageContext'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueParameterDefinition'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueElementDefinition'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueElement'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCodeableConcept'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContactDetail'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAnnotation'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCoding'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSignature'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueReference'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDistance'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDataRequirement'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRange'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueNarrative'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueQuantity'},
        ]


class StructureMap_Target(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.

    Args:
        context: Type or variable this rule applies to.
        contextType: How to interpret the context.
        element: Field to create in the context.
        variable: Named context for field, if desired, and a field is
            specified.
        listMode: If field is a list, how to manage the list.
        listRuleId: Internal rule reference for shared list items.
        transform: How the data is copied / created.
        parameter: Parameters to the transform.
    """

    __name__ = 'StructureMap_Target'

    def __init__(self, dict_values=None):
        self.context = None
        # type: str

        self.contextType = None
        # type: str
        # possible values: type, variable

        self.element = None
        # type: str

        self.variable = None
        # type: str

        self.listMode = None
        # type: list
        # possible values: first, share, last, collate

        self.listRuleId = None
        # type: str

        self.transform = None
        # type: str
        # possible values: create, copy, truncate, escape, cast,
        # append, translate, reference, dateOp, uuid, pointer, evaluate, cc, c,
        # qty, id, cp

        self.parameter = None
        # type: list
        # reference to StructureMap_Parameter

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        valueId: Parameter value - variable or literal.
        valueString: Parameter value - variable or literal.
        valueBoolean: Parameter value - variable or literal.
        valueInteger: Parameter value - variable or literal.
        valueDecimal: Parameter value - variable or literal.
    """

    __name__ = 'StructureMap_Parameter'

    def __init__(self, dict_values=None):
        self.valueId = None
        # type: str

        self.valueString = None
        # type: str

        self.valueBoolean = None
        # type: bool

        self.valueInteger = None
        # type: int

        self.valueDecimal = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class StructureMap_Dependent(fhirbase):
    """
    A Map of relationships between 2 structures that can be used to
    transform data.

    Args:
        name: Name of a rule or group to apply.
        variable: Variable to pass to the rule or group.
    """

    __name__ = 'StructureMap_Dependent'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.variable = None
        # type: list

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
