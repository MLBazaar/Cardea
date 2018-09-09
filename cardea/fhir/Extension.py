from .fhirbase import fhirbase


class Extension(fhirbase):
    """
    Optional Extension Element - found in all resources.
    """

    __name__ = 'Extension'

    def __init__(self, dict_values=None):
        self.url = None
        """
        Source of the definition for the extension code - a logical name or a
        URL.

        type: string
        """

        self.valueBoolean = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: boolean
        """

        self.valueInteger = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: int
        """

        self.valueDecimal = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: int
        """

        self.valueBase64Binary = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueInstant = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueString = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueUri = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueDate = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueDateTime = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueTime = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueCode = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueOid = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueUuid = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueId = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueUnsignedInt = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: int
        """

        self.valuePositiveInt = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: int
        """

        self.valueMarkdown = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        type: string
        """

        self.valueElement = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        """

        self.valueExtension = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Extension
        """

        self.valueBackboneElement = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        """

        self.valueNarrative = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Narrative
        """

        self.valueAnnotation = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Annotation
        """

        self.valueAttachment = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Attachment
        """

        self.valueIdentifier = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Identifier
        """

        self.valueCodeableConcept = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to CodeableConcept
        """

        self.valueCoding = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Coding
        """

        self.valueQuantity = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Quantity
        """

        self.valueDuration = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Duration
        """

        self.valueSimpleQuantity = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Quantity
        """

        self.valueDistance = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Distance
        """

        self.valueCount = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Count
        """

        self.valueMoney = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Money
        """

        self.valueAge = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Age
        """

        self.valueRange = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Range
        """

        self.valuePeriod = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Period
        """

        self.valueRatio = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Ratio
        """

        self.valueReference = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Reference: identifier
        """

        self.valueSampledData = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to SampledData
        """

        self.valueSignature = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Signature
        """

        self.valueHumanName = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to HumanName
        """

        self.valueAddress = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Address
        """

        self.valueContactPoint = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to ContactPoint
        """

        self.valueTiming = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Timing
        """

        self.valueMeta = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Meta
        """

        self.valueElementDefinition = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        """

        self.valueContactDetail = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to ContactDetail
        """

        self.valueContributor = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Contributor
        """

        self.valueDosage = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to Dosage
        """

        self.valueRelatedArtifact = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to RelatedArtifact
        """

        self.valueUsageContext = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to UsageContext
        """

        self.valueDataRequirement = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to DataRequirement
        """

        self.valueParameterDefinition = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to ParameterDefinition
        """

        self.valueTriggerDefinition = None
        """
        Value of extension - may be a resource or one of a constrained set of
        the data types (see Extensibility in the spec for list).

        reference to TriggerDefinition
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAge'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Extension',
             'child_variable': 'valueReference'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueCount'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueContributor'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueSignature'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDuration'},
        ]
