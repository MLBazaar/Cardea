from .fhirbase import fhirbase


class Annotation(fhirbase):
    """A  text note which also  contains information about who made the
    statement and when.
    """

    __name__ = 'Annotation'

    def __init__(self, dict_values=None):
        # the individual responsible for making the annotation.
        self.authorReference = None
        # reference to Reference: identifier

        # the individual responsible for making the annotation.
        self.authorString = None
        # type = string

        # indicates when this particular annotation was made.
        self.time = None
        # type = string

        # the text of the annotation.
        self.text = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Annotation',
             'child_variable': 'authorReference'},
        ]
