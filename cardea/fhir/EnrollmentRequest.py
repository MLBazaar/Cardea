from .fhirbase import fhirbase


class EnrollmentRequest(fhirbase):
    """
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    __name__ = 'EnrollmentRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'EnrollmentRequest'
        """
        This is a EnrollmentRequest resource

        type: string
        possible values: EnrollmentRequest
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.created = None
        """
        The date when this resource was created.

        type: string
        """

        self.insurer = None
        """
        The Insurer who is target  of the request.

        reference to Reference: identifier
        """

        self.provider = None
        """
        The practitioner who is responsible for the services rendered to the
        patient.

        reference to Reference: identifier
        """

        self.organization = None
        """
        The organization which is responsible for the services rendered to the
        patient.

        reference to Reference: identifier
        """

        self.subject = None
        """
        Patient Resource.

        reference to Reference: identifier
        """

        self.coverage = None
        """
        Reference to the program or plan identification, underwriter or payor.

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
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'insurer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'coverage'},

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
        ]
