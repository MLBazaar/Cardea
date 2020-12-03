from .fhirbase import fhirbase


class Attachment(fhirbase):
    """
    For referring to data content defined in other formats.

    Args:
        contentType: Identifies the type of the data in the attachment and
            allows a method to be chosen to interpret or render the data. Includes
            mime type parameters such as charset where appropriate.
        language: The human language of the content. The value can be any
            valid value according to BCP 47.
        data: The actual data of the attachment - a sequence of bytes. In XML,
            represented using base64.
        url: An alternative location where the data can be accessed.
        size: The number of bytes of data that make up this attachment (before
            base64 encoding, if that is done).
        hash: The calculated hash of the data using SHA-1. Represented using
            base64.
        title: A label or set of text to display in place of the data.
        creation: The date that the attachment was first created.
    """

    __name__ = 'Attachment'

    def __init__(self, dict_values=None):
        self.contentType = None
        # type: str

        self.language = None
        # type: str

        self.data = None
        # type: str

        self.url = None
        # type: str

        self.size = None
        # type: int

        self.hash = None
        # type: str

        self.title = None
        # type: str

        self.creation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
