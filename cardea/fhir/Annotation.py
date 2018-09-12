from .fhirbase import fhirbase


class Annotation(fhirbase):
    """
    A  text note which also  contains information about who made the
    statement and when.

    Attributes:
        authorReference: The individual responsible for making the annotation.
        authorString: The individual responsible for making the annotation.
        time: Indicates when this particular annotation was made.
        text: The text of the annotation.
    """

    __name__ = 'Annotation'

    def __init__(self, dict_values=None):
        self.authorReference = None
        # reference to Reference: identifier

        self.authorString = None
        # type: string

        self.time = None
        # type: string

        self.text = None
        # type: string

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Annotation',
             'child_variable': 'authorReference'},
        ]
