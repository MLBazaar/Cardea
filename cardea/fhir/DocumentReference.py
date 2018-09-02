from .fhirbase import fhirbase


class DocumentReference(fhirbase):
    """A reference to a document.
    """

    def __init__(self, dict_values=None):
        # this is a documentreference resource
        self.resourceType = 'DocumentReference'
        # type = string
        # possible values: DocumentReference

        # document identifier as assigned by the source of the document. this
        # identifier is specific to this version of the document. this unique
        # identifier may be used elsewhere to identify this version of the
        # document.
        self.masterIdentifier = None
        # reference to Identifier: Identifier

        # the status of this document reference.
        self.status = None
        # type = string
        # possible values: current, superseded, entered-in-error

        # the status of the underlying document.
        self.docStatus = None
        # type = string

        # specifies the particular kind of document referenced  (e.g. history and
        # physical, discharge summary, progress note). this usually equates to the
        # purpose of making the document referenced.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # a categorization for the type of document referenced - helps for
        # indexing and searching. this may be implied by or derived from the code
        # specified in the documentreference.type.
        self._class = None
        # reference to CodeableConcept: CodeableConcept

        # who or what the document is about. the document can be about a person,
        # (patient or healthcare practitioner), a device (e.g. a machine) or even
        # a group of subjects (such as a document about a herd of farm animals, or
        # a set of patients that share a common exposure).
        self.subject = None
        # reference to Reference: identifier

        # when the document was created.
        self.created = None
        # type = string

        # when the document reference was created.
        self.indexed = None
        # type = string

        # identifies who is responsible for adding the information to the
        # document.
        self.author = None
        # type = array
        # reference to Reference: identifier

        # which person or organization authenticates that this document is valid.
        self.authenticator = None
        # reference to Reference: identifier

        # identifies the organization or group who is responsible for ongoing
        # maintenance of and access to the document.
        self.custodian = None
        # reference to Reference: identifier

        # relationships that this document has with other document references that
        # already exist.
        self.relatesTo = None
        # type = array
        # reference to DocumentReference_RelatesTo: DocumentReference_RelatesTo

        # human-readable description of the source document. this is sometimes
        # known as the "title".
        self.description = None
        # type = string

        # a set of security-tag codes specifying the level of privacy/security of
        # the document. note that documentreference.meta.security contains the
        # security labels of the "reference" to the document, while
        # documentreference.securitylabel contains a snapshot of the security
        # labels on the document the reference refers to.
        self.securityLabel = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the document and format referenced. there may be multiple content
        # element repetitions, each with a different format.
        self.content = None
        # type = array
        # reference to DocumentReference_Content: DocumentReference_Content

        # the clinical context in which the document was prepared.
        self.context = None
        # reference to DocumentReference_Context: DocumentReference_Context

        # other identifiers associated with the document, including version
        # independent identifiers.
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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference',
             'child_variable': 'custodian'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference',
             'child_variable': 'authenticator'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference',
             'child_variable': 'author'},

            {'parent_entity': 'DocumentReference_Context',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'context'},

            {'parent_entity': 'DocumentReference_Content',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'content'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': '_class'},

            {'parent_entity': 'DocumentReference_RelatesTo',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'relatesTo'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'masterIdentifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference',
             'child_variable': 'identifier'},
        ]


class DocumentReference_RelatesTo(fhirbase):
    """A reference to a document.
    """

    def __init__(self, dict_values=None):
        # the type of relationship that this document has with anther document.
        self.code = None
        # type = string
        # possible values: replaces, transforms, signs, appends

        # the target document of this relationship.
        self.target = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
    """A reference to a document.
    """

    def __init__(self, dict_values=None):
        # the document or url of the document along with critical metadata to
        # prove content has integrity.
        self.attachment = None
        # reference to Attachment: Attachment

        # an identifier of the document encoding, structure, and template that the
        # document conforms to beyond the base format indicated in the mimetype.
        self.format = None
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Content',
             'child_variable': 'format'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Content',
             'child_variable': 'attachment'},
        ]


class DocumentReference_Context(fhirbase):
    """A reference to a document.
    """

    def __init__(self, dict_values=None):
        # describes the clinical encounter or type of care that the document
        # content is associated with.
        self.encounter = None
        # reference to Reference: identifier

        # this list of codes represents the main clinical acts, such as a
        # colonoscopy or an appendectomy, being documented. in some cases, the
        # event is inherent in the typecode, such as a "history and physical
        # report" in which the procedure being documented is necessarily a
        # "history and physical" act.
        self.event = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the time period over which the service that is described by the document
        # was provided.
        self.period = None
        # reference to Period: Period

        # the kind of facility where the patient was seen.
        self.facilityType = None
        # reference to CodeableConcept: CodeableConcept

        # this property may convey specifics about the practice setting where the
        # content was created, often reflecting the clinical specialty.
        self.practiceSetting = None
        # reference to CodeableConcept: CodeableConcept

        # the patient information as known when the document was published. may be
        # a reference to a version specific, or contained.
        self.sourcePatientInfo = None
        # reference to Reference: identifier

        # related identifiers or resources associated with the documentreference.
        self.related = None
        # type = array
        # reference to DocumentReference_Related: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'practiceSetting'},

            {'parent_entity': 'DocumentReference_Related',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'related'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'event'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'facilityType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'sourcePatientInfo'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DocumentReference_Context',
             'child_variable': 'encounter'},
        ]


class DocumentReference_Related(fhirbase):
    """A reference to a document.
    """

    def __init__(self, dict_values=None):
        # related resource to this documentreference. if both id and ref are
        # present they shall refer to the same thing.
        self.ref = None
        # reference to Reference: identifier

        # related identifier to this documentreference. if both id and ref are
        # present they shall refer to the same thing.
        self.identifier = None
        # reference to Identifier: Identifier

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
