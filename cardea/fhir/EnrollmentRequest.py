from .fhirbase import fhirbase


class EnrollmentRequest(fhirbase):
    """
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.

    Args:
        resourceType: This is a EnrollmentRequest resource
        identifier: The Response business identifier.
        status: The status of the resource instance.
        created: The date when this resource was created.
        insurer: The Insurer who is target  of the request.
        provider: The practitioner who is responsible for the services
            rendered to the patient.
        organization: The organization which is responsible for the services
            rendered to the patient.
        subject: Patient Resource.
        coverage: Reference to the program or plan identification, underwriter
            or payor.
    """

    __name__ = 'EnrollmentRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'EnrollmentRequest'
        # type: str
        # possible values: EnrollmentRequest

        self.status = None
        # type: str

        self.created = None
        # type: str

        self.insurer = None
        # reference to Reference: identifier

        self.provider = None
        # reference to Reference: identifier

        self.organization = None
        # reference to Reference: identifier

        self.subject = None
        # reference to Reference: identifier

        self.coverage = None
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'coverage'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'insurer'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EnrollmentRequest',
             'child_variable': 'provider'},
        ]
