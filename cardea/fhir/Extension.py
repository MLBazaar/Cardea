from .fhirbase import * 
from .HumanName import HumanName
from .Timing import Timing
from .Address import Address
from .SampledData import SampledData
from .TriggerDefinition import TriggerDefinition
from .Period import Period
from .Quantity import Quantity
from .UsageContext import UsageContext
from .Duration import Duration
from .CodeableConcept import CodeableConcept
from .DataRequirement import DataRequirement
from .Count import Count
from .ContactPoint import ContactPoint
from .Money import Money
from .Contributor import Contributor
from .ContactDetail import ContactDetail
from .ParameterDefinition import ParameterDefinition
from .Annotation import Annotation
from .Ratio import Ratio
from .Age import Age
from .Attachment import Attachment
from .Meta import Meta
from .Signature import Signature
from .Coding import Coding
from .Identifier import Identifier
from .Narrative import Narrative
from .Reference import Reference
from .Dosage import Dosage
from .Range import Range
from .RelatedArtifact import RelatedArtifact
from .Distance import Distance

class Extension(fhirbase):
    """Optional Extension Element - found in all resources.
    """

    def __init__(self, dict_values=None):
        # source of the definition for the extension code - a logical name or a
        # url.
        self.url = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueBoolean = None
        # type = boolean

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueInteger = None
        # type = int

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueDecimal = None
        # type = int

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueBase64Binary = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueInstant = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueString = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueUri = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueDate = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueDateTime = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueTime = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueCode = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueOid = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueUuid = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueId = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueUnsignedInt = None
        # type = int

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valuePositiveInt = None
        # type = int

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueMarkdown = None
        # type = string

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueElement = None

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueExtension = None
        # reference to Extension: Extension

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueBackboneElement = None

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueNarrative = None
        # reference to Narrative: Narrative

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueAnnotation = None
        # reference to Annotation: Annotation

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueIdentifier = None
        # reference to Identifier: Identifier

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueCoding = None
        # reference to Coding: Coding

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueDuration = None
        # reference to Duration: Duration

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueSimpleQuantity = None
        # reference to Quantity: Quantity

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueDistance = None
        # reference to Distance: Distance

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueCount = None
        # reference to Count: Count

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueMoney = None
        # reference to Money: Money

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueAge = None
        # reference to Age: Age

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueRange = None
        # reference to Range: Range

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valuePeriod = None
        # reference to Period: Period

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueRatio = None
        # reference to Ratio: Ratio

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueReference = None
        # reference to Reference: identifier

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueSampledData = None
        # reference to SampledData: SampledData

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueSignature = None
        # reference to Signature: Signature

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueHumanName = None
        # reference to HumanName: HumanName

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueAddress = None
        # reference to Address: Address

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueContactPoint = None
        # reference to ContactPoint: ContactPoint

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueTiming = None
        # reference to Timing: Timing

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueMeta = None
        # reference to Meta: Meta

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueElementDefinition = None

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueContactDetail = None
        # reference to ContactDetail: ContactDetail

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueContributor = None
        # reference to Contributor: Contributor

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueDosage = None
        # reference to Dosage: Dosage

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueRelatedArtifact = None
        # reference to RelatedArtifact: RelatedArtifact

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueUsageContext = None
        # reference to UsageContext: UsageContext

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueDataRequirement = None
        # reference to DataRequirement: DataRequirement

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueParameterDefinition = None
        # reference to ParameterDefinition: ParameterDefinition

        # value of extension - may be a resource or one of a constrained set of
        # the data types (see extensibility in the spec for list).
        self.valueTriggerDefinition = None
        # reference to TriggerDefinition: TriggerDefinition


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Dosage',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueDosage'},

            {'parent_entity': 'Money',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueMoney'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Extension',
            'child_variable': 'valueReference'},

            {'parent_entity': 'Distance',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueDistance'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueAttachment'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueSimpleQuantity'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueContactDetail'},

            {'parent_entity': 'SampledData',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueSampledData'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Signature',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueSignature'},

            {'parent_entity': 'Count',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueCount'},

            {'parent_entity': 'HumanName',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueHumanName'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueUsageContext'},

            {'parent_entity': 'Narrative',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueNarrative'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueQuantity'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueIdentifier'},

            {'parent_entity': 'ParameterDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueParameterDefinition'},

            {'parent_entity': 'TriggerDefinition',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueTriggerDefinition'},

            {'parent_entity': 'Contributor',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueContributor'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueTiming'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueCoding'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueAnnotation'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valuePeriod'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueAddress'},

            {'parent_entity': 'Age',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueAge'},

            {'parent_entity': 'Range',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueRange'},

            {'parent_entity': 'RelatedArtifact',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueRelatedArtifact'},

            {'parent_entity': 'DataRequirement',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueDataRequirement'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueContactPoint'},

            {'parent_entity': 'Meta',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueMeta'},

            {'parent_entity': 'Ratio',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueRatio'},

            {'parent_entity': 'Extension',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueExtension'},

            {'parent_entity': 'Duration',
            'parent_variable': 'object_id',
            'child_entity': 'Extension',
            'child_variable': 'valueDuration'},
        ]

