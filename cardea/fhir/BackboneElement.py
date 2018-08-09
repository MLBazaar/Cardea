from .fhirbase import * 
from .Extension import Extension

class BackboneElement(fhirbase):
    """Base definition for all elements that are defined inside a resource -
    but not those in a data type.
    """

    def __init__(self, dict_values=None):
        # may be used to represent additional information that is not part of the
        # basic definition of the element, and that modifies the understanding of
        # the element that contains it. usually modifier elements provide negation
        # or qualification. in order to make the use of extensions safe and
        # manageable, there is a strict set of governance applied to the
        # definition and use of extensions. though any implementer is allowed to
        # define an extension, there is a set of requirements that shall be met as
        # part of the definition of the extension. applications processing a
        # resource are required to check for modifier extensions.
        self.modifierExtension = None
        # type = array
        # reference to Extension: Extension


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Extension',
            'parent_variable': 'object_id',
            'child_entity': 'BackboneElement',
            'child_variable': 'modifierExtension'},
        ]

