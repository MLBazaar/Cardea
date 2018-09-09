from .fhirbase import fhirbase


class Signature(fhirbase):
    """
    A digital signature along with supporting context. The signature may
    be electronic/cryptographic in nature, or a graphical image
    representing a hand-written signature, or a signature process.
    Different signature approaches have different utilities.
    """

    __name__ = 'Signature'

    def __init__(self, dict_values=None):
        self.type = None
        """
        An indication of the reason that the entity signed this document. This
        may be explicitly included as part of the signature information and
        can be used when determining accountability for various actions
        concerning the document.

        type: array
        reference to Coding
        """

        self.when = None
        """
        When the digital signature was signed.

        type: string
        """

        self.whoUri = None
        """
        A reference to an application-usable description of the identity that
        signed  (e.g. the signature used their private key).

        type: string
        """

        self.whoReference = None
        """
        A reference to an application-usable description of the identity that
        signed  (e.g. the signature used their private key).

        reference to Reference: identifier
        """

        self.onBehalfOfUri = None
        """
        A reference to an application-usable description of the identity that
        is represented by the signature.

        type: string
        """

        self.onBehalfOfReference = None
        """
        A reference to an application-usable description of the identity that
        is represented by the signature.

        reference to Reference: identifier
        """

        self.contentType = None
        """
        A mime type that indicates the technical format of the signature.
        Important mime types are application/signature+xml for X ML DigSig,
        application/jwt for JWT, and image/* for a graphical image of a
        signature, etc.

        type: string
        """

        self.blob = None
        """
        The base64 encoding of the Signature content. When signature is not
        recorded electronically this element would be empty.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Signature',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Signature',
             'child_variable': 'whoReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Signature',
             'child_variable': 'onBehalfOfReference'},
        ]
