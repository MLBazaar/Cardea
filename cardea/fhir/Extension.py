from .fhirbase import fhirbase


class Extension(fhirbase):
    """
    Optional Extension Element - found in all resources.

    Args:
        url: Source of the definition for the extension code - a logical name
            or a URL.
        valueBoolean: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueInteger: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueDecimal: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueBase64Binary: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueInstant: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueString: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueUri: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueDate: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueDateTime: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueTime: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueCode: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueOid: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueUuid: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueId: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueUnsignedInt: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valuePositiveInt: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueMarkdown: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueElement: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueExtension: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueBackboneElement: Value of extension - may be a resource or one of
            a constrained set of the data types (see Extensibility in the spec for
            list).
        valueNarrative: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueAnnotation: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueAttachment: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueIdentifier: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueCodeableConcept: Value of extension - may be a resource or one of
            a constrained set of the data types (see Extensibility in the spec for
            list).
        valueCoding: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueQuantity: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueDuration: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueSimpleQuantity: Value of extension - may be a resource or one of
            a constrained set of the data types (see Extensibility in the spec for
            list).
        valueDistance: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueCount: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueMoney: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueAge: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueRange: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valuePeriod: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueRatio: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueReference: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueSampledData: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueSignature: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueHumanName: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueAddress: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueContactPoint: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueTiming: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueMeta: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueElementDefinition: Value of extension - may be a resource or one
            of a constrained set of the data types (see Extensibility in the spec
            for list).
        valueContactDetail: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueContributor: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueDosage: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueRelatedArtifact: Value of extension - may be a resource or one of
            a constrained set of the data types (see Extensibility in the spec for
            list).
        valueUsageContext: Value of extension - may be a resource or one of a
            constrained set of the data types (see Extensibility in the spec for
            list).
        valueDataRequirement: Value of extension - may be a resource or one of
            a constrained set of the data types (see Extensibility in the spec for
            list).
        valueParameterDefinition: Value of extension - may be a resource or
            one of a constrained set of the data types (see Extensibility in the
            spec for list).
        valueTriggerDefinition: Value of extension - may be a resource or one
            of a constrained set of the data types (see Extensibility in the spec
            for list).
    """

    __name__ = 'Extension'

    def __init__(self, dict_values=None):
        self.url = None
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

        self.valueExtension = None
        # reference to Extension

        self.valueBackboneElement = None

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

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueMoney'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Extension',
             'child_variable': 'valueReference'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAge'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueRange'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueContactDetail'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueMeta'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDuration'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueContributor'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueSignature'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'ParameterDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAddress'},

            {'parent_entity': 'Distance',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDistance'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueTiming'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAnnotation'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueHumanName'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueIdentifier'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'TriggerDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueNarrative'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueExtension'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueDosage'},

            {'parent_entity': 'Count',
             'parent_variable': 'object_id',
             'child_entity': 'Extension',
             'child_variable': 'valueCount'},
        ]
