from .fhirbase import fhirbase


class ProcessResponse(fhirbase):
    """
    This resource provides processing status, errors and notes from the
    processing of a resource.

    Args:
        resourceType: This is a ProcessResponse resource
        identifier: The Response business identifier.
        status: The status of the resource instance.
        created: The date when the enclosed suite of services were performed
            or completed.
        organization: The organization who produced this adjudicated response.
        request: Original request resource reference.
        outcome: Transaction status: error, complete, held.
        disposition: A description of the status of the adjudication or
            processing.
        requestProvider: The practitioner who is responsible for the services
            rendered to the patient.
        requestOrganization: The organization which is responsible for the
            services rendered to the patient.
        form: The form to be used for printing the content.
        processNote: Suite of processing notes or additional requirements if
            the processing has been held.
        error: Processing errors.
        communicationRequest: Request for additional supporting or authorizing
            information, such as: documents, images or resources.
    """

    __name__ = 'ProcessResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'ProcessResponse'
        # type: str
        # possible values: ProcessResponse

        self.status = None
        # type: str

        self.created = None
        # type: str

        self.organization = None
        # reference to Reference: identifier

        self.request = None
        # reference to Reference: identifier

        self.outcome = None
        # reference to CodeableConcept

        self.disposition = None
        # type: str

        self.requestProvider = None
        # reference to Reference: identifier

        self.requestOrganization = None
        # reference to Reference: identifier

        self.form = None
        # reference to CodeableConcept

        self.processNote = None
        # type: list
        # reference to ProcessResponse_ProcessNote

        self.error = None
        # type: list
        # reference to CodeableConcept

        self.communicationRequest = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'error'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'communicationRequest'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'ProcessResponse_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'processNote'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'organization'},
        ]


class ProcessResponse_ProcessNote(fhirbase):
    """
    This resource provides processing status, errors and notes from the
    processing of a resource.

    Args:
        type: The note purpose: Print/Display.
        text: The note text.
    """

    __name__ = 'ProcessResponse_ProcessNote'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.text = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse_ProcessNote',
             'child_variable': 'type'},
        ]
