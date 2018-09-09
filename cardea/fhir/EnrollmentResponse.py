from .fhirbase import fhirbase


class EnrollmentResponse(fhirbase):
    """
    This resource provides enrollment and plan details from the processing
    of an Enrollment resource.
    """

    __name__ = 'EnrollmentResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'EnrollmentResponse'
        """
        This is a EnrollmentResponse resource

        type: string
        possible values: EnrollmentResponse
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.request = None
        """
        Original request resource reference.

        reference to Reference: identifier
        """

        self.outcome = None
        """
        Processing status: error, complete.

        reference to CodeableConcept
        """

        self.disposition = None
        """
        A description of the status of the adjudication.

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
        The Insurer who produced this adjudicated response.

        reference to Reference: identifier
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
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'requestProvider'},

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

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EnrollmentResponse',
             'child_variable': 'outcome'},
        ]
