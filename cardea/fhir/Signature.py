from .fhirbase import * 
from .Reference import Reference
from .Coding import Coding

class Signature(fhirbase):
    """A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different signature
    approaches have different utilities.
    """

    def __init__(self, dict_values=None):
        # an indication of the reason that the entity signed this document. this
        # may be explicitly included as part of the signature information and can
        # be used when determining accountability for various actions concerning
        # the document.
        self.type = None
        # type = array
        # reference to Coding: Coding

        # when the digital signature was signed.
        self.when = None
        # type = string

        # a reference to an application-usable description of the identity that
        # signed  (e.g. the signature used their private key).
        self.whoUri = None
        # type = string

        # a reference to an application-usable description of the identity that
        # signed  (e.g. the signature used their private key).
        self.whoReference = None
        # reference to Reference: identifier

        # a reference to an application-usable description of the identity that is
        # represented by the signature.
        self.onBehalfOfUri = None
        # type = string

        # a reference to an application-usable description of the identity that is
        # represented by the signature.
        self.onBehalfOfReference = None
        # reference to Reference: identifier

        # a mime type that indicates the technical format of the signature.
        # important mime types are application/signature+xml for x ml digsig,
        # application/jwt for jwt, and image/* for a graphical image of a
        # signature, etc.
        self.contentType = None
        # type = string

        # the base64 encoding of the signature content. when signature is not
        # recorded electronically this element would be empty.
        self.blob = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Signature',
            'child_variable': 'whoReference'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Signature',
            'child_variable': 'type'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Signature',
            'child_variable': 'onBehalfOfReference'},
        ]

