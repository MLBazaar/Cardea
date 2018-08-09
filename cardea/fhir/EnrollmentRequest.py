from .fhirbase import * 
from .Reference import Reference
from .Identifier import Identifier

class EnrollmentRequest(fhirbase):
    """This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    def __init__(self, dict_values=None):
        # this is a enrollmentrequest resource
        self.resourceType = 'EnrollmentRequest'
        # type = string
        # possible values = EnrollmentRequest

        # the status of the resource instance.
        self.status = None
        # type = string

        # the date when this resource was created.
        self.created = None
        # type = string

        # the insurer who is target  of the request.
        self.insurer = None
        # reference to Reference: identifier

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.provider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.organization = None
        # reference to Reference: identifier

        # patient resource.
        self.subject = None
        # reference to Reference: identifier

        # reference to the program or plan identification, underwriter or payor.
        self.coverage = None
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
            'child_entity': 'EnrollmentRequest',
            'child_variable': 'provider'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'EnrollmentRequest',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EnrollmentRequest',
            'child_variable': 'subject'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EnrollmentRequest',
            'child_variable': 'organization'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EnrollmentRequest',
            'child_variable': 'coverage'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EnrollmentRequest',
            'child_variable': 'insurer'},
        ]

