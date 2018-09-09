from .fhirbase import fhirbase


class DocumentManifest(fhirbase):
    """
    A collection of documents compiled for a purpose together with
    metadata that applies to the collection.
    """

    __name__ = 'DocumentManifest'

    def __init__(self, dict_values=None):
        self.resourceType = 'DocumentManifest'
        """
        This is a DocumentManifest resource

        type: string
        possible values: DocumentManifest
        """

        self.masterIdentifier = None
        """
        A single identifier that uniquely identifies this manifest.
        Principally used to refer to the manifest in non-FHIR contexts.

        reference to Identifier
        """

        self.status = None
        """
        The status of this document manifest.

        type: string
        possible values: current, superseded, entered-in-error
        """

        self.type = None
        """
        Specifies the kind of this set of documents (e.g. Patient Summary,
        Discharge Summary, Prescription, etc.). The type of a set of documents
        may be the same as one of the documents in it - especially if there is
        only one - but it may be wider.

        reference to CodeableConcept
        """

        self.subject = None
        """
        Who or what the set of documents is about. The documents can be about
        a person, (patient or healthcare practitioner), a device (i.e.
        machine) or even a group of subjects (such as a document about a herd
        of farm animals, or a set of patients that share a common exposure).
        If the documents cross more than one subject, then more than one
        subject is allowed here (unusual use case).

        reference to Reference: identifier
        """

        self.created = None
        """
        When the document manifest was created for submission to the server
        (not necessarily the same thing as the actual resource last modified
        time, since it may be modified, replicated, etc.).

        type: string
        """

        self.author = None
        """
        Identifies who is responsible for creating the manifest, and adding
        documents to it.

        type: array
        reference to Reference: identifier
        """

        self.recipient = None
        """
        A patient, practitioner, or organization for which this set of
        documents is intended.

        type: array
        reference to Reference: identifier
        """

        self.source = None
        """
        Identifies the source system, application, or software that produced
        the document manifest.

        type: string
        """

        self.description = None
        """
        Human-readable description of the source document. This is sometimes
        known as the "title".

        type: string
        """

        self.content = None
        """
        The list of Documents included in the manifest.

        type: array
        reference to DocumentManifest_Content
        """

        self.related = None
        """
        Related identifiers or resources associated with the DocumentManifest.

        type: array
        reference to DocumentManifest_Related: identifier
        """

        self.identifier = None
        """
        Other identifiers associated with the document manifest, including
        version independent  identifiers.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'current', 'superseded', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'current, superseded, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'recipient'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'author'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'type'},

            {'parent_entity': 'DocumentManifest_Related',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'related'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'masterIdentifier'},

            {'parent_entity': 'DocumentManifest_Content',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'content'},
        ]


class DocumentManifest_Content(fhirbase):
    """
    A collection of documents compiled for a purpose together with
    metadata that applies to the collection.
    """

    __name__ = 'DocumentManifest_Content'

    def __init__(self, dict_values=None):
        self.pAttachment = None
        """
        The list of references to document content, or Attachment that consist
        of the parts of this document manifest. Usually, these would be
        document references, but direct references to Media or Attachments are
        also allowed.

        reference to Attachment
        """

        self.pReference = None
        """
        The list of references to document content, or Attachment that consist
        of the parts of this document manifest. Usually, these would be
        document references, but direct references to Media or Attachments are
        also allowed.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest_Content',
             'child_variable': 'pReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest_Content',
             'child_variable': 'pAttachment'},
        ]


class DocumentManifest_Related(fhirbase):
    """
    A collection of documents compiled for a purpose together with
    metadata that applies to the collection.
    """

    __name__ = 'DocumentManifest_Related'

    def __init__(self, dict_values=None):
        self.ref = None
        """
        Related Resource to this DocumentManifest. For example, Order,
        ProcedureRequest,  Procedure, EligibilityRequest, etc.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Related identifier to this DocumentManifest.  For example, Order
        numbers, accession numbers, XDW workflow numbers.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest_Related',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest_Related',
             'child_variable': 'ref'},
        ]
