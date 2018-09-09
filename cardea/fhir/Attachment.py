from .fhirbase import fhirbase


class Attachment(fhirbase):
    """For referring to data content defined in other formats.
    """

    def __init__(self, dict_values=None):
        # identifies the type of the data in the attachment and allows a method to
        # be chosen to interpret or render the data. includes mime type parameters
        # such as charset where appropriate.
        self.contentType = None
        # type = string

        # the human language of the content. the value can be any valid value
        # according to bcp 47.
        self.language = None
        # type = string

        # the actual data of the attachment - a sequence of bytes. in xml,
        # represented using base64.
        self.data = None
        # type = string

        # an alternative location where the data can be accessed.
        self.url = None
        # type = string

        # the number of bytes of data that make up this attachment (before base64
        # encoding, if that is done).
        self.size = None
        # type = int

        # the calculated hash of the data using sha-1. represented using base64.
        self.hash = None
        # type = string

        # a label or set of text to display in place of the data.
        self.title = None
        # type = string

        # the date that the attachment was first created.
        self.creation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
