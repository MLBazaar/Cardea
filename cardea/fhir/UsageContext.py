from .fhirbase import fhirbase


class UsageContext(fhirbase):
    """
    Specifies clinical/business/etc metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be
    specific to the applicable population (e.g., age category, DRG) or the
    specific context of care (e.g., venue, care setting, provider of
    care).

    Args:
        code: A code that identifies the type of context being specified by
            this usage context.
        valueCodeableConcept: A value that defines the context specified in
            this context of use. The interpretation of the value is defined by the
            code.
        valueQuantity: A value that defines the context specified in this
            context of use. The interpretation of the value is defined by the
            code.
        valueRange: A value that defines the context specified in this context
            of use. The interpretation of the value is defined by the code.
    """

    __name__ = 'UsageContext'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to Coding

        self.valueCodeableConcept = None
        # reference to CodeableConcept

        self.valueQuantity = None
        # reference to Quantity

        self.valueRange = None
        # reference to Range

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'code'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'UsageContext',
             'child_variable': 'valueRange'},
        ]
