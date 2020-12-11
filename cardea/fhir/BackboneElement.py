from .fhirbase import fhirbase


class BackboneElement(fhirbase):
    """
    Base definition for all elements that are defined inside a resource -
    but not those in a data type.

    Args:
        modifierExtension: May be used to represent additional information
            that is not part of the basic definition of the element, and that
            modifies the understanding of the element that contains it. Usually
            modifier elements provide negation or qualification. In order to make
            the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the
            extension. Applications processing a resource are required to check
            for modifier extensions.
    """

    __name__ = 'BackboneElement'

    def __init__(self, dict_values=None):
        self.modifierExtension = None
        # type: list
        # reference to Extension

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'BackboneElement',
             'child_variable': 'modifierExtension'},
        ]
