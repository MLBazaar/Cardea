from .fhirbase import fhirbase


class Parameters(fhirbase):
    """
    This special resource type is used to represent an operation request
    and response (operations.html). It has no other use, and there is no
    RESTful endpoint associated with it.
    """

    __name__ = 'Parameters'

    def __init__(self, dict_values=None):
        self.parameter = None
        """
        A parameter passed to or received from the operation.

        type: array
        reference to Parameters_Parameter
        """

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
    """

    __name__ = 'Parameters_Parameter'

    def __init__(self, dict_values=None):
        self.name = None
        """
        The name of the parameter (reference to the operation definition).

        type: string
        """

        self.valueBoolean = None
        """
        If the parameter is a data type.

        type: boolean
        """

        self.valueInteger = None
        """
        If the parameter is a data type.

        type: int
        """

        self.valueDecimal = None
        """
        If the parameter is a data type.

        type: int
        """

        self.valueBase64Binary = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueInstant = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueString = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueUri = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueDate = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueDateTime = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueTime = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueCode = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueOid = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueUuid = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueId = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueUnsignedInt = None
        """
        If the parameter is a data type.

        type: int
        """

        self.valuePositiveInt = None
        """
        If the parameter is a data type.

        type: int
        """

        self.valueMarkdown = None
        """
        If the parameter is a data type.

        type: string
        """

        self.valueElement = None
        """
        If the parameter is a data type.

        reference to Element: id
        """

        self.valueExtension = None
        """
        If the parameter is a data type.

        reference to Extension
        """

        self.valueBackboneElement = None
        """
        If the parameter is a data type.

        reference to BackboneElement
        """

        self.valueNarrative = None
        """
        If the parameter is a data type.

        reference to Narrative
        """

        self.valueAnnotation = None
        """
        If the parameter is a data type.

        reference to Annotation
        """

        self.valueAttachment = None
        """
        If the parameter is a data type.

        reference to Attachment
        """

        self.valueIdentifier = None
        """
        If the parameter is a data type.

        reference to Identifier
        """

        self.valueCodeableConcept = None
        """
        If the parameter is a data type.

        reference to CodeableConcept
        """

        self.valueCoding = None
        """
        If the parameter is a data type.

        reference to Coding
        """

        self.valueQuantity = None
        """
        If the parameter is a data type.

        reference to Quantity
        """

        self.valueDuration = None
        """
        If the parameter is a data type.

        reference to Duration
        """

        self.valueSimpleQuantity = None
        """
        If the parameter is a data type.

        reference to Quantity
        """

        self.valueDistance = None
        """
        If the parameter is a data type.

        reference to Distance
        """

        self.valueCount = None
        """
        If the parameter is a data type.

        reference to Count
        """

        self.valueMoney = None
        """
        If the parameter is a data type.

        reference to Money
        """

        self.valueAge = None
        """
        If the parameter is a data type.

        reference to Age
        """

        self.valueRange = None
        """
        If the parameter is a data type.

        reference to Range
        """

        self.valuePeriod = None
        """
        If the parameter is a data type.

        reference to Period
        """

        self.valueRatio = None
        """
        If the parameter is a data type.

        reference to Ratio
        """

        self.valueReference = None
        """
        If the parameter is a data type.

        reference to Reference: identifier
        """

        self.valueSampledData = None
        """
        If the parameter is a data type.

        reference to SampledData
        """

        self.valueSignature = None
        """
        If the parameter is a data type.

        reference to Signature
        """

        self.valueHumanName = None
        """
        If the parameter is a data type.

        reference to HumanName
        """

        self.valueAddress = None
        """
        If the parameter is a data type.

        reference to Address
        """

        self.valueContactPoint = None
        """
        If the parameter is a data type.

        reference to ContactPoint
        """

        self.valueTiming = None
        """
        If the parameter is a data type.

        reference to Timing
        """

        self.valueMeta = None
        """
        If the parameter is a data type.

        reference to Meta
        """

        self.valueElementDefinition = None
        """
        If the parameter is a data type.

        reference to ElementDefinition
        """

        self.valueContactDetail = None
        """
        If the parameter is a data type.

        reference to ContactDetail
        """

        self.valueContributor = None
        """
        If the parameter is a data type.

        reference to Contributor
        """

        self.valueDosage = None
        """
        If the parameter is a data type.

        reference to Dosage
        """

        self.valueRelatedArtifact = None
        """
        If the parameter is a data type.

        reference to RelatedArtifact
        """

        self.valueUsageContext = None
        """
        If the parameter is a data type.

        reference to UsageContext
        """

        self.valueDataRequirement = None
        """
        If the parameter is a data type.

        reference to DataRequirement
        """

        self.valueParameterDefinition = None
        """
        If the parameter is a data type.

        reference to ParameterDefinition
        """

        self.valueTriggerDefinition = None
        """
        If the parameter is a data type.

        reference to TriggerDefinition
        """

        self.resource = None
        """
        If the parameter is a whole resource.

        reference to ResourceList
        """

        self.part = None
        """
        A named part of a multi-part parameter.

        type: array
        reference to Parameters_Parameter
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'resource'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueElementDefinition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'Parameters_Parameter',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'part'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueRange'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueSignature'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueContributor'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAge'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueCount'},

            {'parent_entity': 'BackboneElement',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueBackboneElement'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Element',
             'parent_variable': 'id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueElement'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Parameters_Parameter',
             'child_variable': 'valueDuration'},
        ]
