from .fhirbase import fhirbase


class Element(fhirbase):
    """
    Base definition for all elements in a resource.

    Args:
        id: unique id for the element within a resource (for internal
            references). This may be any string value that does not contain
            spaces.
        extension: May be used to represent additional information that is not
            part of the basic definition of the element. In order to make the use
            of extensions safe and manageable, there is a strict set of governance
            applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the
            extension.
    """

    __name__ = 'Element'

    def __init__(self, dict_values=None):
        self.extension = None
        # type: list
        # reference to Extension

        self.id = None
        # type: str

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'Element',
             'child_variable': 'extension'},
        ]
