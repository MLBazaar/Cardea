from .fhirbase import fhirbase


class Binary(fhirbase):
    """A binary resource can contain any content, whether text, image, pdf, zip
    archive, etc.
    """

    __name__ = 'Binary'

    def __init__(self, dict_values=None):
        # this is a binary resource
        self.resourceType = 'Binary'
        # type = string
        # possible values: Binary

        # mimetype of the binary content represented as a standard mimetype (bcp
        # 13).
        self.contentType = None
        # type = string

        # treat this binary as if it was this other resource for access control
        # purposes.
        self.securityContext = None
        # reference to Reference: identifier

        # the actual content, base64 encoded.
        self.content = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Binary',
             'child_variable': 'securityContext'},
        ]
