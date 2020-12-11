from .fhirbase import fhirbase


class DocumentManifest(fhirbase):
    """
    A collection of documents compiled for a purpose together with
    metadata that applies to the collection.

    Args:
        resourceType: This is a DocumentManifest resource
        masterIdentifier: A single identifier that uniquely identifies this
            manifest. Principally used to refer to the manifest in non-FHIR
            contexts.
        identifier: Other identifiers associated with the document manifest,
            including version independent  identifiers.
        status: The status of this document manifest.
        type: Specifies the kind of this set of documents (e.g. Patient
            Summary, Discharge Summary, Prescription, etc.). The type of a set of
            documents may be the same as one of the documents in it - especially
            if there is only one - but it may be wider.
        subject: Who or what the set of documents is about. The documents can
            be about a person, (patient or healthcare practitioner), a device
            (i.e. machine) or even a group of subjects (such as a document about a
            herd of farm animals, or a set of patients that share a common
            exposure). If the documents cross more than one subject, then more
            than one subject is allowed here (unusual use case).
        created: When the document manifest was created for submission to the
            server (not necessarily the same thing as the actual resource last
            modified time, since it may be modified, replicated, etc.).
        author: Identifies who is responsible for creating the manifest, and
            adding  documents to it.
        recipient: A patient, practitioner, or organization for which this set
            of documents is intended.
        source: Identifies the source system, application, or software that
            produced the document manifest.
        description: Human-readable description of the source document. This
            is sometimes known as the "title".
        content: The list of Documents included in the manifest.
        related: Related identifiers or resources associated with the
            DocumentManifest.
    """

    __name__ = 'DocumentManifest'

    def __init__(self, dict_values=None):
        self.resourceType = 'DocumentManifest'
        # type: str
        # possible values: DocumentManifest

        self.masterIdentifier = None
        # reference to Identifier

        self.status = None
        # type: str
        # possible values: current, superseded, entered-in-error

        self.type = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.created = None
        # type: str

        self.author = None
        # type: list
        # reference to Reference: identifier

        self.recipient = None
        # type: list
        # reference to Reference: identifier

        self.source = None
        # type: str

        self.description = None
        # type: str

        self.content = None
        # type: list
        # reference to DocumentManifest_Content

        self.related = None
        # type: list
        # reference to DocumentManifest_Related: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'current', 'superseded', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'current, superseded, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'masterIdentifier'},

            {'parent_entity': 'DocumentManifest_Related',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'related'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'recipient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'author'},

            {'parent_entity': 'DocumentManifest_Content',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'content'},
        ]


class DocumentManifest_Content(fhirbase):
    """
    A collection of documents compiled for a purpose together with
    metadata that applies to the collection.

    Args:
        pAttachment: The list of references to document content, or Attachment
            that consist of the parts of this document manifest. Usually, these
            would be document references, but direct references to Media or
            Attachments are also allowed.
        pReference: The list of references to document content, or Attachment
            that consist of the parts of this document manifest. Usually, these
            would be document references, but direct references to Media or
            Attachments are also allowed.
    """

    __name__ = 'DocumentManifest_Content'

    def __init__(self, dict_values=None):
        self.pAttachment = None
        # reference to Attachment

        self.pReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest_Content',
             'child_variable': 'pAttachment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest_Content',
             'child_variable': 'pReference'},
        ]


class DocumentManifest_Related(fhirbase):
    """
    A collection of documents compiled for a purpose together with
    metadata that applies to the collection.

    Args:
        identifier: Related identifier to this DocumentManifest.  For example,
            Order numbers, accession numbers, XDW workflow numbers.
        ref: Related Resource to this DocumentManifest. For example, Order,
            ProcedureRequest,  Procedure, EligibilityRequest, etc.
    """

    __name__ = 'DocumentManifest_Related'

    def __init__(self, dict_values=None):
        self.ref = None
        # reference to Reference: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest_Related',
             'child_variable': 'ref'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest_Related',
             'child_variable': 'identifier'},
        ]
