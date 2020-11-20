from .fhirbase import fhirbase


class Parameters(fhirbase):
    """
    This special resource type is used to represent an operation request
    and response (operations.html). It has no other use, and there is no
    RESTful endpoint associated with it.

    Args:
        parameter: A parameter passed to or received from the operation.
    """

    __name__ = 'Parameters'

    def __init__(self, dict_values=None):
        self.parameter = None
        # type: list
        # reference to Parameters_Parameter

        self.object_id = None
        # unique identifier for object class

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
    """
    This special resource type is used to represent an operation request
    and response (operations.html). It has no other use, and there is no
    RESTful endpoint associated with it.

    Args:
        name: The name of the parameter (reference to the operation
            definition).
        valueBoolean: If the parameter is a data type.
        valueInteger: If the parameter is a data type.
        valueDecimal: If the parameter is a data type.
        valueBase64Binary: If the parameter is a data type.
        valueInstant: If the parameter is a data type.
        valueString: If the parameter is a data type.
        valueUri: If the parameter is a data type.
        valueDate: If the parameter is a data type.
        valueDateTime: If the parameter is a data type.
        valueTime: If the parameter is a data type.
        valueCode: If the parameter is a data type.
        valueOid: If the parameter is a data type.
        valueUuid: If the parameter is a data type.
        valueId: If the parameter is a data type.
        valueUnsignedInt: If the parameter is a data type.
        valuePositiveInt: If the parameter is a data type.
        valueMarkdown: If the parameter is a data type.
        valueElement: If the parameter is a data type.
        valueExtension: If the parameter is a data type.
        valueBackboneElement: If the parameter is a data type.
        valueNarrative: If the parameter is a data type.
        valueAnnotation: If the parameter is a data type.
        valueAttachment: If the parameter is a data type.
        valueIdentifier: If the parameter is a data type.
        valueCodeableConcept: If the parameter is a data type.
        valueCoding: If the parameter is a data type.
        valueQuantity: If the parameter is a data type.
        valueDuration: If the parameter is a data type.
        valueSimpleQuantity: If the parameter is a data type.
        valueDistance: If the parameter is a data type.
        valueCount: If the parameter is a data type.
        valueMoney: If the parameter is a data type.
        valueAge: If the parameter is a data type.
        valueRange: If the parameter is a data type.
        valuePeriod: If the parameter is a data type.
        valueRatio: If the parameter is a data type.
        valueReference: If the parameter is a data type.
        valueSampledData: If the parameter is a data type.
        valueSignature: If the parameter is a data type.
        valueHumanName: If the parameter is a data type.
        valueAddress: If the parameter is a data type.
        valueContactPoint: If the parameter is a data type.
        valueTiming: If the parameter is a data type.
        valueMeta: If the parameter is a data type.
        valueElementDefinition: If the parameter is a data type.
        valueContactDetail: If the parameter is a data type.
        valueContributor: If the parameter is a data type.
        valueDosage: If the parameter is a data type.
        valueRelatedArtifact: If the parameter is a data type.
        valueUsageContext: If the parameter is a data type.
        valueDataRequirement: If the parameter is a data type.
        valueParameterDefinition: If the parameter is a data type.
        valueTriggerDefinition: If the parameter is a data type.
        resource: If the parameter is a whole resource.
        part: A named part of a multi-part parameter.
    """

    __name__ = 'Parameters_Parameter'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.valueBoolean = None
        # type: bool

        self.valueInteger = None
        # type: int

        self.valueDecimal = None
        # type: int

        self.valueBase64Binary = None
        # type: str

        self.valueInstant = None
        # type: str

        self.valueString = None
        # type: str

        self.valueUri = None
        # type: str

        self.valueDate = None
        # type: str

        self.valueDateTime = None
        # type: str

        self.valueTime = None
        # type: str

        self.valueCode = None
        # type: str

        self.valueOid = None
        # type: str

        self.valueUuid = None
        # type: str

        self.valueId = None
        # type: str

        self.valueUnsignedInt = None
        # type: int

        self.valuePositiveInt = None
        # type: int

        self.valueMarkdown = None
        # type: str

        self.valueElement = None
        # reference to Element: id

        self.valueExtension = None
        # reference to Extension

        self.valueBackboneElement = None
        # reference to BackboneElement

        self.valueNarrative = None
        # reference to Narrative

        self.valueAnnotation = None
        # reference to Annotation

        self.valueAttachment = None
        # reference to Attachment

        self.valueIdentifier = None
        # reference to Identifier

        self.valueCodeableConcept = None
        # reference to CodeableConcept

        self.valueCoding = None
        # reference to Coding

        self.valueQuantity = None
        # reference to Quantity

        self.valueDuration = None
        # reference to Duration

        self.valueSimpleQuantity = None
        # reference to Quantity

        self.valueDistance = None
        # reference to Distance

        self.valueCount = None
        # reference to Count

        self.valueMoney = None
        # reference to Money

        self.valueAge = None
        # reference to Age

        self.valueRange = None
        # reference to Range

        self.valuePeriod = None
        # reference to Period

        self.valueRatio = None
        # reference to Ratio

        self.valueReference = None
        # reference to Reference: identifier

        self.valueSampledData = None
        # reference to SampledData

        self.valueSignature = None
        # reference to Signature

        self.valueHumanName = None
        # reference to HumanName

        self.valueAddress = None
        # reference to Address

        self.valueContactPoint = None
        # reference to ContactPoint

        self.valueTiming = None
        # reference to Timing

        self.valueMeta = None
        # reference to Meta

        self.valueElementDefinition = None
        # reference to ElementDefinition

        self.valueContactDetail = None
        # reference to ContactDetail

        self.valueContributor = None
        # reference to Contributor

        self.valueDosage = None
        # reference to Dosage

        self.valueRelatedArtifact = None
        # reference to RelatedArtifact

        self.valueUsageContext = None
        # reference to UsageContext

        self.valueDataRequirement = None
        # reference to DataRequirement

        self.valueParameterDefinition = None
        # reference to ParameterDefinition

        self.valueTriggerDefinition = None
        # reference to TriggerDefinition

        self.resource = None
        # reference to ResourceList

        self.part = None
        # type: list
        # reference to Parameters_Parameter

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueReference'},

            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'resource'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueContributor'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Parameters_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'part'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAge'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueRange'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueSignature'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDuration'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueCount'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueElement'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueCoding'},
        ]
