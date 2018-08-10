from .fhirbase import * 
from .Extension import Extension

class Element(fhirbase):
    """Base definition for all elements in a resource.
    """

    def __init__(self, dict_values=None):
        # may be used to represent additional information that is not part of the
        # basic definition of the element. in order to make the use of extensions
        # safe and manageable, there is a strict set of governance  applied to the
        # definition and use of extensions. though any implementer is allowed to
        # define an extension, there is a set of requirements that shall be met as
        # part of the definition of the extension.
        self.extension = None
        # type = array
        # reference to Extension: Extension

        # unique id for the element within a resource (for internal references).
        # this may be any string value that does not contain spaces.
        self.id = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Extension',
            'parent_variable': 'object_id',
            'child_entity': 'Element',
            'child_variable': 'extension'},
        ]

