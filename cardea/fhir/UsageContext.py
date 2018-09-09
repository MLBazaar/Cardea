from .fhirbase import fhirbase


class UsageContext(fhirbase):
    """Specifies clinical/business/etc metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be
    specific to the applicable population (e.g., age category, DRG) or the
    specific context of care (e.g., venue, care setting, provider of care).
    """

    __name__ = 'UsageContext'

    def __init__(self, dict_values=None):
        # a code that identifies the type of context being specified by this usage
        # context.
        self.code = None
        # reference to Coding: Coding

        # a value that defines the context specified in this context of use. the
        # interpretation of the value is defined by the code.
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # a value that defines the context specified in this context of use. the
        # interpretation of the value is defined by the code.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # a value that defines the context specified in this context of use. the
        # interpretation of the value is defined by the code.
        self.valueRange = None
        # reference to Range: Range

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'valueCodeableConcept'},
        ]
