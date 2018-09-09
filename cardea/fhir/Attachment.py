from .fhirbase import fhirbase


class Attachment(fhirbase):
    """
    For referring to data content defined in other formats.
    """

    __name__ = 'Attachment'

    def __init__(self, dict_values=None):
        self.contentType = None
        """
        Identifies the type of the data in the attachment and allows a method
        to be chosen to interpret or render the data. Includes mime type
        parameters such as charset where appropriate.

        type: string
        """

        self.language = None
        """
        The human language of the content. The value can be any valid value
        according to BCP 47.

        type: string
        """

        self.data = None
        """
        The actual data of the attachment - a sequence of bytes. In XML,
        represented using base64.

        type: string
        """

        self.url = None
        """
        An alternative location where the data can be accessed.

        type: string
        """

        self.size = None
        """
        The number of bytes of data that make up this attachment (before
        base64 encoding, if that is done).

        type: int
        """

        self.hash = None
        """
        The calculated hash of the data using SHA-1. Represented using base64.

        type: string
        """

        self.title = None
        """
        A label or set of text to display in place of the data.

        type: string
        """

        self.creation = None
        """
        The date that the attachment was first created.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
