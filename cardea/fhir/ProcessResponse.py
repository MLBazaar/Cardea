from .fhirbase import fhirbase


class ProcessResponse(fhirbase):
    """
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    __name__ = 'ProcessResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'ProcessResponse'
        """
        This is a ProcessResponse resource

        type: string
        possible values: ProcessResponse
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.created = None
        """
        The date when the enclosed suite of services were performed or
        completed.

        type: string
        """

        self.organization = None
        """
        The organization who produced this adjudicated response.

        reference to Reference: identifier
        """

        self.request = None
        """
        Original request resource reference.

        reference to Reference: identifier
        """

        self.outcome = None
        """
        Transaction status: error, complete, held.

        reference to CodeableConcept
        """

        self.disposition = None
        """
        A description of the status of the adjudication or processing.

        type: string
        """

        self.requestProvider = None
        """
        The practitioner who is responsible for the services rendered to the
        patient.

        reference to Reference: identifier
        """

        self.requestOrganization = None
        """
        The organization which is responsible for the services rendered to the
        patient.

        reference to Reference: identifier
        """

        self.form = None
        """
        The form to be used for printing the content.

        reference to CodeableConcept
        """

        self.processNote = None
        """
        Suite of processing notes or additional requirements if the processing
        has been held.

        type: array
        reference to ProcessResponse_ProcessNote
        """

        self.error = None
        """
        Processing errors.

        type: array
        reference to CodeableConcept
        """

        self.communicationRequest = None
        """
        Request for additional supporting or authorizing information, such as:
        documents, images or resources.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        The Response business identifier.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'communicationRequest'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'organization'},

            {'parent_entity': 'ProcessResponse_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'processNote'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'error'},
        ]


class ProcessResponse_ProcessNote(fhirbase):
    """
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    __name__ = 'ProcessResponse_ProcessNote'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The note purpose: Print/Display.

        reference to CodeableConcept
        """

        self.text = None
        """
        The note text.

        type: string
        """

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
