from .fhirbase import fhirbase


class DocumentManifest(fhirbase):
    """A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    def __init__(self, dict_values=None):
        # this is a documentmanifest resource
        self.resourceType = 'DocumentManifest'
        # type = string
        # possible values: DocumentManifest

        # a single identifier that uniquely identifies this manifest. principally
        # used to refer to the manifest in non-fhir contexts.
        self.masterIdentifier = None
        # reference to Identifier: Identifier

        # the status of this document manifest.
        self.status = None
        # type = string
        # possible values: current, superseded, entered-in-error

        # specifies the kind of this set of documents (e.g. patient summary,
        # discharge summary, prescription, etc.). the type of a set of documents
        # may be the same as one of the documents in it - especially if there is
        # only one - but it may be wider.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # who or what the set of documents is about. the documents can be about a
        # person, (patient or healthcare practitioner), a device (i.e. machine) or
        # even a group of subjects (such as a document about a herd of farm
        # animals, or a set of patients that share a common exposure). if the
        # documents cross more than one subject, then more than one subject is
        # allowed here (unusual use case).
        self.subject = None
        # reference to Reference: identifier

        # when the document manifest was created for submission to the server (not
        # necessarily the same thing as the actual resource last modified time,
        # since it may be modified, replicated, etc.).
        self.created = None
        # type = string

        # identifies who is responsible for creating the manifest, and adding
        # documents to it.
        self.author = None
        # type = array
        # reference to Reference: identifier

        # a patient, practitioner, or organization for which this set of documents
        # is intended.
        self.recipient = None
        # type = array
        # reference to Reference: identifier

        # identifies the source system, application, or software that produced the
        # document manifest.
        self.source = None
        # type = string

        # human-readable description of the source document. this is sometimes
        # known as the "title".
        self.description = None
        # type = string

        # the list of documents included in the manifest.
        self.content = None
        # type = array
        # reference to DocumentManifest_Content: DocumentManifest_Content

        # related identifiers or resources associated with the documentmanifest.
        self.related = None
        # type = array
        # reference to DocumentManifest_Related: identifier

        # other identifiers associated with the document manifest, including
        # version independent  identifiers.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'author'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'masterIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'recipient'},

            {'parent_entity': 'DocumentManifest_Related',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentManifest',
             'child_variable': 'related'},

            {'parent_entity': 'DocumentManifest_Content',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'content'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentManifest',
             'child_variable': 'type'},
        ]


class DocumentManifest_Content(fhirbase):
    """A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    def __init__(self, dict_values=None):
        # the list of references to document content, or attachment that consist
        # of the parts of this document manifest. usually, these would be document
        # references, but direct references to media or attachments are also
        # allowed.
        self.pAttachment = None
        # reference to Attachment: Attachment

        # the list of references to document content, or attachment that consist
        # of the parts of this document manifest. usually, these would be document
        # references, but direct references to media or attachments are also
        # allowed.
        self.pReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
    """A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    def __init__(self, dict_values=None):
        # related resource to this documentmanifest. for example, order,
        # procedurerequest,  procedure, eligibilityrequest, etc.
        self.ref = None
        # reference to Reference: identifier

        # related identifier to this documentmanifest.  for example, order
        # numbers, accession numbers, xdw workflow numbers.
        self.identifier = None
        # reference to Identifier: Identifier

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
