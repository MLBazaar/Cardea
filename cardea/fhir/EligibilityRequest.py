from .fhirbase import fhirbase


class EligibilityRequest(fhirbase):
    """
    The EligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    EligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """

    __name__ = 'EligibilityRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'EligibilityRequest'
        """
        This is a EligibilityRequest resource

        type: string
        possible values: EligibilityRequest
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.priority = None
        """
        Immediate (STAT), best effort (NORMAL), deferred (DEFER).

        reference to CodeableConcept
        """

        self.patient = None
        """
        Patient Resource.

        reference to Reference: identifier
        """

        self.servicedDate = None
        """
        The date or dates when the enclosed suite of services were performed
        or completed.

        type: string
        """

        self.servicedPeriod = None
        """
        The date or dates when the enclosed suite of services were performed
        or completed.

        reference to Period
        """

        self.created = None
        """
        The date when this resource was created.

        type: string
        """

        self.enterer = None
        """
        Person who created the invoice/claim/pre-determination or
        pre-authorization.

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

        self.insurer = None
        """
        The Insurer who is target  of the request.

        reference to Reference: identifier
        """

        self.facility = None
        """
        Facility where the services were provided.

        reference to Reference: identifier
        """

        self.coverage = None
        """
        Financial instrument by which payment information for health care.

        reference to Reference: identifier
        """

        self.businessArrangement = None
        """
        The contract number of a business agreement which describes the terms
        and conditions.

        type: string
        """

        self.benefitCategory = None
        """
        Dental, Vision, Medical, Pharmacy, Rehab etc.

        reference to CodeableConcept
        """

        self.benefitSubCategory = None
        """
        Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.

        reference to CodeableConcept
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
             'child_entity': 'EligibilityRequest',
             'child_variable': 'coverage'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'priority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'enterer'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'provider'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'benefitSubCategory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'facility'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'benefitCategory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'insurer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'patient'},
        ]
