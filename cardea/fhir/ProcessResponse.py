from .fhirbase import fhirbase


class ProcessResponse(fhirbase):
    """This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    __name__ = 'ProcessResponse'

    def __init__(self, dict_values=None):
        # this is a processresponse resource
        self.resourceType = 'ProcessResponse'
        # type = string
        # possible values: ProcessResponse

        # the status of the resource instance.
        self.status = None
        # type = string

        # the date when the enclosed suite of services were performed or
        # completed.
        self.created = None
        # type = string

        # the organization who produced this adjudicated response.
        self.organization = None
        # reference to Reference: identifier

        # original request resource reference.
        self.request = None
        # reference to Reference: identifier

        # transaction status: error, complete, held.
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # a description of the status of the adjudication or processing.
        self.disposition = None
        # type = string

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.requestProvider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.requestOrganization = None
        # reference to Reference: identifier

        # the form to be used for printing the content.
        self.form = None
        # reference to CodeableConcept: CodeableConcept

        # suite of processing notes or additional requirements if the processing
        # has been held.
        self.processNote = None
        # type = array
        # reference to ProcessResponse_ProcessNote: ProcessResponse_ProcessNote

        # processing errors.
        self.error = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # request for additional supporting or authorizing information, such as:
        # documents, images or resources.
        self.communicationRequest = None
        # type = array
        # reference to Reference: identifier

        # the response business identifier.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'error'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'communicationRequest'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'form'},

            {'parent_entity': 'ProcessResponse_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse',
             'child_variable': 'processNote'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessResponse',
             'child_variable': 'requestProvider'},
        ]


class ProcessResponse_ProcessNote(fhirbase):
    """This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    __name__ = 'ProcessResponse_ProcessNote'

    def __init__(self, dict_values=None):
        # the note purpose: print/display.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the note text.
        self.text = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessResponse_ProcessNote',
             'child_variable': 'type'},
        ]
