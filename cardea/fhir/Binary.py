from .fhirbase import fhirbase


class Binary(fhirbase):
    """
    A binary resource can contain any content, whether text, image, pdf,
    zip archive, etc.
    """

    __name__ = 'Binary'

    def __init__(self, dict_values=None):
        self.resourceType = 'Binary'
        """
        This is a Binary resource

        type: string
        possible values: Binary
        """

        self.contentType = None
        """
        MimeType of the binary content represented as a standard MimeType (BCP
        13).

        type: string
        """

        self.securityContext = None
        """
        Treat this binary as if it was this other resource for access control
        purposes.

        reference to Reference: identifier
        """

        self.content = None
        """
        The actual content, base64 encoded.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Binary',
             'child_variable': 'securityContext'},
        ]
