from .fhirbase import fhirbase


class StructureMap(fhirbase):
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap'

    def __init__(self, dict_values=None):
        # this is a structuremap resource
        self.resourceType = 'StructureMap'
        # type = string
        # possible values: StructureMap

        # an absolute uri that is used to identify this structure map when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this structure map is (or will be) published. the url should include the
        # major version of the structure map. for more information see [technical
        # and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the structure
        # map when it is referenced in a specification, model, design or instance.
        # this is an arbitrary value managed by the structure map author and is
        # not expected to be globally unique. for example, it might be a timestamp
        # (e.g. yyyymmdd) if a managed version is not available. there is also no
        # expectation that versions can be placed in a lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the structure map. this name should
        # be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the structure map.
        self.title = None
        # type = string

        # the status of this structure map. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this structure map is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the structure map was published.
        # the date must change if and when the business version changes and it
        # must change if the status code changes. in addition, it should change
        # when the substantive content of the structure map changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the structure
        # map.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the structure map from a
        # consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate structure map instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the structure map is intended to
        # be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this structure map is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the structure map and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the structure map.
        self.copyright = None
        # type = string

        # a structure definition used by this map. the structure definition may
        # describe instances that are converted, or the instances that are
        # produced.
        self.structure = None
        # type = array
        # reference to StructureMap_Structure: StructureMap_Structure

        # other maps used by this map (canonical urls).
        self._import = None
        # type = array

        # organizes the mapping into managable chunks for human review/ease of
        # maintenance.
        self.group = None
        # type = array
        # reference to StructureMap_Group: StructureMap_Group

        # a formal identifier that is used to identify this structure map when it
        # is represented in other formats, or referenced in a specification,
        # model, design or an instance.
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

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Group',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'group'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'useContext'},

            {'parent_entity': 'StructureMap_Structure',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'structure'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap',
             'child_variable': 'jurisdiction'},
        ]


class StructureMap_Structure(fhirbase):
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Structure'

    def __init__(self, dict_values=None):
        # the canonical url that identifies the structure.
        self.url = None
        # type = string

        # how the referenced structure is used in this mapping.
        self.mode = None
        # type = string
        # possible values: source, queried, target, produced

        # the name used for this type in the map.
        self.alias = None
        # type = string

        # documentation that describes how the structure is used in the mapping.
        self.documentation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

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
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Group'

    def __init__(self, dict_values=None):
        # a unique name for the group for the convenience of human readers.
        self.name = None
        # type = string

        # another group that this group adds rules to.
        self.extends = None
        # type = string

        # if this is the default rule set to apply for thie source type, or this
        # combination of types.
        self.typeMode = None
        # type = string
        # possible values: none, types, type-and-types

        # additional supporting documentation that explains the purpose of the
        # group and the types of mappings within it.
        self.documentation = None
        # type = string

        # a name assigned to an instance of data. the instance must be provided
        # when the mapping is invoked.
        self.input = None
        # type = array
        # reference to StructureMap_Input: StructureMap_Input

        # transform rule from source to target.
        self.rule = None
        # type = array
        # reference to StructureMap_Rule: StructureMap_Rule

        # unique identifier for object class
        self.object_id = None

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
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Input'

    def __init__(self, dict_values=None):
        # name for this instance of data.
        self.name = None
        # type = string

        # type for this instance of data.
        self.type = None
        # type = string

        # mode for this instance of data.
        self.mode = None
        # type = string
        # possible values: source, target

        # documentation for this instance of data.
        self.documentation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

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
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Rule'

    def __init__(self, dict_values=None):
        # name of the rule for internal references.
        self.name = None
        # type = string

        # source inputs to the mapping.
        self.source = None
        # type = array
        # reference to StructureMap_Source: StructureMap_Source

        # content to create because of this mapping rule.
        self.target = None
        # type = array
        # reference to StructureMap_Target: StructureMap_Target

        # rules contained in this rule.
        self.rule = None
        # type = array
        # reference to StructureMap_Rule: StructureMap_Rule

        # which other rules to apply in the context of this rule.
        self.dependent = None
        # type = array
        # reference to StructureMap_Dependent: StructureMap_Dependent

        # documentation for this instance of data.
        self.documentation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'rule'},

            {'parent_entity': 'StructureMap_Target',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'target'},

            {'parent_entity': 'StructureMap_Source',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'source'},

            {'parent_entity': 'StructureMap_Dependent',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Rule',
             'child_variable': 'dependent'},
        ]


class StructureMap_Source(fhirbase):
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Source'

    def __init__(self, dict_values=None):
        # type or variable this rule applies to.
        self.context = None
        # type = string

        # specified minimum cardinality for the element. this is optional; if
        # present, it acts an implicit check on the input content.
        self.min = None
        # type = int

        # specified maximum cardinality for the element - a number or a "*". this
        # is optional; if present, it acts an implicit check on the input content
        # (* just serves as documentation; it's the default value).
        self.max = None
        # type = string

        # specified type for the element. this works as a condition on the mapping
        # - use for polymorphic elements.
        self.type = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueBoolean = None
        # type = boolean

        # a value to use if there is no existing value in the source object.
        self.defaultValueInteger = None
        # type = int

        # a value to use if there is no existing value in the source object.
        self.defaultValueDecimal = None
        # type = int

        # a value to use if there is no existing value in the source object.
        self.defaultValueBase64Binary = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueInstant = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueString = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueUri = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueDate = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueDateTime = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueTime = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueCode = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueOid = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueUuid = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueId = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueUnsignedInt = None
        # type = int

        # a value to use if there is no existing value in the source object.
        self.defaultValuePositiveInt = None
        # type = int

        # a value to use if there is no existing value in the source object.
        self.defaultValueMarkdown = None
        # type = string

        # a value to use if there is no existing value in the source object.
        self.defaultValueElement = None
        # reference to Element: id

        # a value to use if there is no existing value in the source object.
        self.defaultValueExtension = None
        # reference to Extension: Extension

        # a value to use if there is no existing value in the source object.
        self.defaultValueBackboneElement = None
        # reference to BackboneElement: BackboneElement

        # a value to use if there is no existing value in the source object.
        self.defaultValueNarrative = None
        # reference to Narrative: Narrative

        # a value to use if there is no existing value in the source object.
        self.defaultValueAnnotation = None
        # reference to Annotation: Annotation

        # a value to use if there is no existing value in the source object.
        self.defaultValueAttachment = None
        # reference to Attachment: Attachment

        # a value to use if there is no existing value in the source object.
        self.defaultValueIdentifier = None
        # reference to Identifier: Identifier

        # a value to use if there is no existing value in the source object.
        self.defaultValueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # a value to use if there is no existing value in the source object.
        self.defaultValueCoding = None
        # reference to Coding: Coding

        # a value to use if there is no existing value in the source object.
        self.defaultValueQuantity = None
        # reference to Quantity: Quantity

        # a value to use if there is no existing value in the source object.
        self.defaultValueDuration = None
        # reference to Duration: Duration

        # a value to use if there is no existing value in the source object.
        self.defaultValueSimpleQuantity = None
        # reference to Quantity: Quantity

        # a value to use if there is no existing value in the source object.
        self.defaultValueDistance = None
        # reference to Distance: Distance

        # a value to use if there is no existing value in the source object.
        self.defaultValueCount = None
        # reference to Count: Count

        # a value to use if there is no existing value in the source object.
        self.defaultValueMoney = None
        # reference to Money: Money

        # a value to use if there is no existing value in the source object.
        self.defaultValueAge = None
        # reference to Age: Age

        # a value to use if there is no existing value in the source object.
        self.defaultValueRange = None
        # reference to Range: Range

        # a value to use if there is no existing value in the source object.
        self.defaultValuePeriod = None
        # reference to Period: Period

        # a value to use if there is no existing value in the source object.
        self.defaultValueRatio = None
        # reference to Ratio: Ratio

        # a value to use if there is no existing value in the source object.
        self.defaultValueReference = None
        # reference to Reference: identifier

        # a value to use if there is no existing value in the source object.
        self.defaultValueSampledData = None
        # reference to SampledData: SampledData

        # a value to use if there is no existing value in the source object.
        self.defaultValueSignature = None
        # reference to Signature: Signature

        # a value to use if there is no existing value in the source object.
        self.defaultValueHumanName = None
        # reference to HumanName: HumanName

        # a value to use if there is no existing value in the source object.
        self.defaultValueAddress = None
        # reference to Address: Address

        # a value to use if there is no existing value in the source object.
        self.defaultValueContactPoint = None
        # reference to ContactPoint: ContactPoint

        # a value to use if there is no existing value in the source object.
        self.defaultValueTiming = None
        # reference to Timing: Timing

        # a value to use if there is no existing value in the source object.
        self.defaultValueMeta = None
        # reference to Meta: Meta

        # a value to use if there is no existing value in the source object.
        self.defaultValueElementDefinition = None
        # reference to ElementDefinition: ElementDefinition

        # a value to use if there is no existing value in the source object.
        self.defaultValueContactDetail = None
        # reference to ContactDetail: ContactDetail

        # a value to use if there is no existing value in the source object.
        self.defaultValueContributor = None
        # reference to Contributor: Contributor

        # a value to use if there is no existing value in the source object.
        self.defaultValueDosage = None
        # reference to Dosage: Dosage

        # a value to use if there is no existing value in the source object.
        self.defaultValueRelatedArtifact = None
        # reference to RelatedArtifact: RelatedArtifact

        # a value to use if there is no existing value in the source object.
        self.defaultValueUsageContext = None
        # reference to UsageContext: UsageContext

        # a value to use if there is no existing value in the source object.
        self.defaultValueDataRequirement = None
        # reference to DataRequirement: DataRequirement

        # a value to use if there is no existing value in the source object.
        self.defaultValueParameterDefinition = None
        # reference to ParameterDefinition: ParameterDefinition

        # a value to use if there is no existing value in the source object.
        self.defaultValueTriggerDefinition = None
        # reference to TriggerDefinition: TriggerDefinition

        # optional field for this source.
        self.element = None
        # type = string

        # how to handle the list mode for this element.
        self.listMode = None
        # type = string
        # possible values: first, not_first, last, not_last, only_one

        # named context for field, if a field is specified.
        self.variable = None
        # type = string

        # fhirpath expression  - must be true or the rule does not apply.
        self.condition = None
        # type = string

        # fhirpath expression  - must be true or the mapping engine throws an
        # error instead of completing.
        self.check = None
        # type = string

        # unique identifier for object class
        self.object_id = None

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
            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueBackboneElement'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDuration'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueQuantity'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContactDetail'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAnnotation'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValuePeriod'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSignature'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueElementDefinition'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueUsageContext'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCount'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSampledData'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueParameterDefinition'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueHumanName'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueIdentifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueMoney'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueTiming'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRatio'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueExtension'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContactPoint'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueReference'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAddress'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDistance'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueContributor'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDataRequirement'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRelatedArtifact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCodeableConcept'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueElement'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAge'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueNarrative'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueRange'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueAttachment'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueSimpleQuantity'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueCoding'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueMeta'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueDosage'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Source',
             'child_variable': 'defaultValueTriggerDefinition'},
        ]


class StructureMap_Target(fhirbase):
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Target'

    def __init__(self, dict_values=None):
        # type or variable this rule applies to.
        self.context = None
        # type = string

        # how to interpret the context.
        self.contextType = None
        # type = string
        # possible values: type, variable

        # field to create in the context.
        self.element = None
        # type = string

        # named context for field, if desired, and a field is specified.
        self.variable = None
        # type = string

        # if field is a list, how to manage the list.
        self.listMode = None
        # type = array
        # possible values: first, share, last, collate

        # internal rule reference for shared list items.
        self.listRuleId = None
        # type = string

        # how the data is copied / created.
        self.transform = None
        # type = string
        # possible values: create, copy, truncate, escape, cast, append,
        # translate, reference, dateOp, uuid, pointer, evaluate, cc, c, qty, id,
        # cp

        # parameters to the transform.
        self.parameter = None
        # type = array
        # reference to StructureMap_Parameter: StructureMap_Parameter

        # unique identifier for object class
        self.object_id = None

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
                    'reference', 'dateop', 'uuid', 'pointer', 'evaluate', 'cc', 'c', 'qty',
                        'id', 'cp']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'create, copy, truncate, escape, cast, append, translate,'
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
                    'reference', 'dateop', 'uuid', 'pointer', 'evaluate', 'cc', 'c', 'qty',
                        'id', 'cp']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'create, copy, truncate, escape, cast, append, translate,'
                        'reference, dateOp, uuid, pointer, evaluate, cc, c, qty, id, cp'))

    def get_relationships(self):

        return [
            {'parent_entity': 'StructureMap_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'StructureMap_Target',
             'child_variable': 'parameter'},
        ]


class StructureMap_Parameter(fhirbase):
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Parameter'

    def __init__(self, dict_values=None):
        # parameter value - variable or literal.
        self.valueId = None
        # type = string

        # parameter value - variable or literal.
        self.valueString = None
        # type = string

        # parameter value - variable or literal.
        self.valueBoolean = None
        # type = boolean

        # parameter value - variable or literal.
        self.valueInteger = None
        # type = int

        # parameter value - variable or literal.
        self.valueDecimal = None
        # type = int

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class StructureMap_Dependent(fhirbase):
    """A Map of relationships between 2 structures that can be used to
    transform data.
    """

    __name__ = 'StructureMap_Dependent'

    def __init__(self, dict_values=None):
        # name of a rule or group to apply.
        self.name = None
        # type = string

        # variable to pass to the rule or group.
        self.variable = None
        # type = array

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
