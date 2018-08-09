from .fhirbase import * 

class Parameters(fhirbase):
    """This special resource type is used to represent an operation request and
    response (operations.html). It has no other use, and there is no RESTful
    endpoint associated with it.
    """

    def __init__(self, dict_values=None):
        # a parameter passed to or received from the operation.
        self.parameter = None
        # type = array
        # reference to Parameters_Parameter: Parameters_Parameter


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Parameters_Parameter',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters',
            'child_variable': 'parameter'},
        ]

class Parameters_Parameter(fhirbase):
    """This special resource type is used to represent an operation request and
    response (operations.html). It has no other use, and there is no RESTful
    endpoint associated with it.
    """

    def __init__(self, dict_values=None):
        # the name of the parameter (reference to the operation definition).
        # the name of the parameter (reference to the operation definition).
        self.name = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueBoolean = None
        # type = boolean
        # type = boolean

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueInteger = None
        # type = int
        # type = int

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueDecimal = None
        # type = int
        # type = int

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueBase64Binary = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueInstant = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueString = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueUri = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueDate = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueDateTime = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueTime = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueCode = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueOid = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueUuid = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueId = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueUnsignedInt = None
        # type = int
        # type = int

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valuePositiveInt = None
        # type = int
        # type = int

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueMarkdown = None
        # type = string
        # type = string

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueElement = None
        # reference to Element: id

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueExtension = None
        # reference to Extension: Extension

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueBackboneElement = None
        # reference to BackboneElement: BackboneElement

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueNarrative = None
        # reference to Narrative: Narrative

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueAnnotation = None
        # reference to Annotation: Annotation

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueIdentifier = None
        # reference to Identifier: Identifier

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueCoding = None
        # reference to Coding: Coding

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueDuration = None
        # reference to Duration: Duration

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueSimpleQuantity = None
        # reference to Quantity: Quantity

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueDistance = None
        # reference to Distance: Distance

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueCount = None
        # reference to Count: Count

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueMoney = None
        # reference to Money: Money

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueAge = None
        # reference to Age: Age

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueRange = None
        # reference to Range: Range

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valuePeriod = None
        # reference to Period: Period

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueRatio = None
        # reference to Ratio: Ratio

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueReference = None
        # reference to Reference: identifier

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueSampledData = None
        # reference to SampledData: SampledData

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueSignature = None
        # reference to Signature: Signature

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueHumanName = None
        # reference to HumanName: HumanName

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueAddress = None
        # reference to Address: Address

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueContactPoint = None
        # reference to ContactPoint: ContactPoint

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueTiming = None
        # reference to Timing: Timing

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueMeta = None
        # reference to Meta: Meta

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueElementDefinition = None
        # reference to ElementDefinition: ElementDefinition

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueContactDetail = None
        # reference to ContactDetail: ContactDetail

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueContributor = None
        # reference to Contributor: Contributor

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueDosage = None
        # reference to Dosage: Dosage

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueRelatedArtifact = None
        # reference to RelatedArtifact: RelatedArtifact

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueUsageContext = None
        # reference to UsageContext: UsageContext

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueDataRequirement = None
        # reference to DataRequirement: DataRequirement

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueParameterDefinition = None
        # reference to ParameterDefinition: ParameterDefinition

        # if the parameter is a data type.
        # if the parameter is a data type.
        self.valueTriggerDefinition = None
        # reference to TriggerDefinition: TriggerDefinition

        # if the parameter is a whole resource.
        # if the parameter is a whole resource.
        self.resource = None
        # reference to ResourceList: ResourceList

        # a named part of a multi-part parameter.
        # a named part of a multi-part parameter.
        self.part = None
        # type = array
        # type = array
        # reference to Parameters_Parameter: Parameters_Parameter


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueAttachment'},

            {'parent_entity': 'TriggerDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'SampledData',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueSampledData'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueTiming'},

            {'parent_entity': 'Money',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueMoney'},

            {'parent_entity': 'Dosage',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueDosage'},

            {'parent_entity': 'RelatedArtifact',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Range',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueRange'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueAnnotation'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Count',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueCount'},

            {'parent_entity': 'Distance',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueDistance'},

            {'parent_entity': 'BackboneElement',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueAddress'},

            {'parent_entity': 'Narrative',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueNarrative'},

            {'parent_entity': 'Meta',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueMeta'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueIdentifier'},

            {'parent_entity': 'Signature',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueSignature'},

            {'parent_entity': 'ElementDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'Extension',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueExtension'},

            {'parent_entity': 'Duration',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueDuration'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueQuantity'},

            {'parent_entity': 'Contributor',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueContributor'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valuePeriod'},

            {'parent_entity': 'ResourceList',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'resource'},

            {'parent_entity': 'DataRequirement',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'Ratio',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueRatio'},

            {'parent_entity': 'ParameterDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueCoding'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Element',
            'parent_variable': 'id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueElement'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueReference'},

            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueHumanName'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Age',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueAge'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Parameters_Parameter',
            'parent_variable': 'object_id',
            'child_entity': 'Parameters_Parameter',
            'child_variable': 'part'},
        ]

