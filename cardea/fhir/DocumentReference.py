from .fhirbase import fhirbase


class DocumentReference(fhirbase):
    """
    A reference to a document.
    """

    __name__ = 'DocumentReference'

    def __init__(self, dict_values=None):
        self.resourceType = 'DocumentReference'
        """
        This is a DocumentReference resource

        type: string
        possible values: DocumentReference
        """

        self.masterIdentifier = None
        """
        Document identifier as assigned by the source of the document. This
        identifier is specific to this version of the document. This unique
        identifier may be used elsewhere to identify this version of the
        document.

        reference to Identifier
        """

        self.status = None
        """
        The status of this document reference.

        type: string
        possible values: current, superseded, entered-in-error
        """

        self.docStatus = None
        """
        The status of the underlying document.

        type: string
        """

        self.type = None
        """
        Specifies the particular kind of document referenced  (e.g. History
        and Physical, Discharge Summary, Progress Note). This usually equates
        to the purpose of making the document referenced.

        reference to CodeableConcept
        """

        self._class = None
        """
        A categorization for the type of document referenced - helps for
        indexing and searching. This may be implied by or derived from the
        code specified in the DocumentReference.type.

        reference to CodeableConcept
        """

        self.subject = None
        """
        Who or what the document is about. The document can be about a person,
        (patient or healthcare practitioner), a device (e.g. a machine) or
        even a group of subjects (such as a document about a herd of farm
        animals, or a set of patients that share a common exposure).

        reference to Reference: identifier
        """

        self.created = None
        """
        When the document was created.

        type: string
        """

        self.indexed = None
        """
        When the document reference was created.

        type: string
        """

        self.author = None
        """
        Identifies who is responsible for adding the information to the
        document.

        type: array
        reference to Reference: identifier
        """

        self.authenticator = None
        """
        Which person or organization authenticates that this document is
        valid.

        reference to Reference: identifier
        """

        self.custodian = None
        """
        Identifies the organization or group who is responsible for ongoing
        maintenance of and access to the document.

        reference to Reference: identifier
        """

        self.relatesTo = None
        """
        Relationships that this document has with other document references
        that already exist.

        type: array
        reference to DocumentReference_RelatesTo
        """

        self.description = None
        """
        Human-readable description of the source document. This is sometimes
        known as the "title".

        type: string
        """

        self.securityLabel = None
        """
        A set of Security-Tag codes specifying the level of privacy/security
        of the Document. Note that DocumentReference.meta.security contains
        the security labels of the "reference" to the document, while
        DocumentReference.securityLabel contains a snapshot of the security
        labels on the document the reference refers to.

        type: array
        reference to CodeableConcept
        """

        self.content = None
        """
        The document and format referenced. There may be multiple content
        element repetitions, each with a different format.

        type: array
        reference to DocumentReference_Content
        """

        self.context = None
        """
        The clinical context in which the document was prepared.

        reference to DocumentReference_Context
        """

        self.identifier = None
        """
        Other identifiers associated with the document, including version
        independent identifiers.

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
             'child_entity': 'DocumentReference',
             'child_variable': 'custodian'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference',
             'child_variable': 'authenticator'},

            {'parent_entity': 'DocumentReference_Content',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'content'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'DocumentReference_RelatesTo',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'relatesTo'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': '_class'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'masterIdentifier'},

            {'parent_entity': 'DocumentReference_Context',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference',
             'child_variable': 'author'},
        ]


class DocumentReference_RelatesTo(fhirbase):
    """
    A reference to a document.
    """

    __name__ = 'DocumentReference_RelatesTo'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The type of relationship that this document has with anther document.

        type: string
        possible values: replaces, transforms, signs, appends
        """

        self.target = None
        """
        The target document of this relationship.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                        'replaces', 'transforms', 'signs', 'appends']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'replaces, transforms, signs, appends'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_RelatesTo',
             'child_variable': 'target'},
        ]


class DocumentReference_Content(fhirbase):
    """
    A reference to a document.
    """

    __name__ = 'DocumentReference_Content'

    def __init__(self, dict_values=None):
        self.attachment = None
        """
        The document or URL of the document along with critical metadata to
        prove content has integrity.

        reference to Attachment
        """

        self.format = None
        """
        An identifier of the document encoding, structure, and template that
        the document conforms to beyond the base format indicated in the
        mimeType.

        reference to Coding
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Content',
             'child_variable': 'attachment'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Content',
             'child_variable': 'format'},
        ]


class DocumentReference_Context(fhirbase):
    """
    A reference to a document.
    """

    __name__ = 'DocumentReference_Context'

    def __init__(self, dict_values=None):
        self.encounter = None
        """
        Describes the clinical encounter or type of care that the document
        content is associated with.

        reference to Reference: identifier
        """

        self.event = None
        """
        This list of codes represents the main clinical acts, such as a
        colonoscopy or an appendectomy, being documented. In some cases, the
        event is inherent in the typeCode, such as a "History and Physical
        Report" in which the procedure being documented is necessarily a
        "History and Physical" act.

        type: array
        reference to CodeableConcept
        """

        self.period = None
        """
        The time period over which the service that is described by the
        document was provided.

        reference to Period
        """

        self.facilityType = None
        """
        The kind of facility where the patient was seen.

        reference to CodeableConcept
        """

        self.practiceSetting = None
        """
        This property may convey specifics about the practice setting where
        the content was created, often reflecting the clinical specialty.

        reference to CodeableConcept
        """

        self.sourcePatientInfo = None
        """
        The Patient Information as known when the document was published. May
        be a reference to a version specific, or contained.

        reference to Reference: identifier
        """

        self.related = None
        """
        Related identifiers or resources associated with the
        DocumentReference.

        type: array
        reference to DocumentReference_Related: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'event'},

            {'parent_entity': 'DocumentReference_Related',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'related'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'facilityType'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'encounter'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'sourcePatientInfo'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'practiceSetting'},
        ]


class DocumentReference_Related(fhirbase):
    """
    A reference to a document.
    """

    __name__ = 'DocumentReference_Related'

    def __init__(self, dict_values=None):
        self.ref = None
        """
        Related Resource to this DocumentReference. If both id and ref are
        present they shall refer to the same thing.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Related identifier to this DocumentReference. If both id and ref are
        present they shall refer to the same thing.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_Related',
             'child_variable': 'ref'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Related',
             'child_variable': 'identifier'},
        ]
