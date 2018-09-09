from .fhirbase import fhirbase


class EnrollmentResponse(fhirbase):
    """This resource provides enrollment and plan details from the processing
    of an Enrollment resource.
    """

    __name__ = 'EnrollmentResponse'

    def __init__(self, dict_values=None):
        # this is a enrollmentresponse resource
        self.resourceType = 'EnrollmentResponse'
        # type = string
        # possible values: EnrollmentResponse

        # the status of the resource instance.
        self.status = None
        # type = string

        # original request resource reference.
        self.request = None
        # reference to Reference: identifier

        # processing status: error, complete.
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # a description of the status of the adjudication.
        self.disposition = None
        # type = string

        # the date when the enclosed suite of services were performed or
        # completed.
        self.created = None
        # type = string

        # the insurer who produced this adjudicated response.
        self.organization = None
        # reference to Reference: identifier

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.requestProvider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.requestOrganization = None
        # reference to Reference: identifier

        # the response business identifier.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'organization'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'identifier'},
        ]
