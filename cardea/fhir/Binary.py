from .fhirbase import fhirbase


class Binary(fhirbase):
    """
    A binary resource can contain any content, whether text, image, pdf,
    zip archive, etc.

    Args:
        resourceType: This is a Binary resource
        contentType: MimeType of the binary content represented as a standard
            MimeType (BCP 13).
        securityContext: Treat this binary as if it was this other resource
            for access control purposes.
        content: The actual content, base64 encoded.
    """

    __name__ = 'Binary'

    def __init__(self, dict_values=None):
        self.resourceType = 'Binary'
        # type: str
        # possible values: Binary

        self.contentType = None
        # type: str

        self.securityContext = None
        # reference to Reference: identifier

        self.content = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Binary',
             'child_variable': 'securityContext'},
        ]
