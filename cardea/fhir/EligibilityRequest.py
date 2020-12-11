from .fhirbase import fhirbase


class EligibilityRequest(fhirbase):
    """
    The EligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    EligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.

    Args:
        resourceType: This is a EligibilityRequest resource
        identifier: The Response business identifier.
        status: The status of the resource instance.
        priority: Immediate (STAT), best effort (NORMAL), deferred (DEFER).
        patient: Patient Resource.
        servicedDate: The date or dates when the enclosed suite of services
            were performed or completed.
        servicedPeriod: The date or dates when the enclosed suite of services
            were performed or completed.
        created: The date when this resource was created.
        enterer: Person who created the invoice/claim/pre-determination or
            pre-authorization.
        provider: The practitioner who is responsible for the services
            rendered to the patient.
        organization: The organization which is responsible for the services
            rendered to the patient.
        insurer: The Insurer who is target  of the request.
        facility: Facility where the services were provided.
        coverage: Financial instrument by which payment information for health
            care.
        businessArrangement: The contract number of a business agreement which
            describes the terms and conditions.
        benefitCategory: Dental, Vision, Medical, Pharmacy, Rehab etc.
        benefitSubCategory: Dental: basic, major, ortho; Vision exam, glasses,
            contacts; etc.
    """

    __name__ = 'EligibilityRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'EligibilityRequest'
        # type: str
        # possible values: EligibilityRequest

        self.status = None
        # type: str

        self.priority = None
        # reference to CodeableConcept

        self.patient = None
        # reference to Reference: identifier

        self.servicedDate = None
        # type: str

        self.servicedPeriod = None
        # reference to Period

        self.created = None
        # type: str

        self.enterer = None
        # reference to Reference: identifier

        self.provider = None
        # reference to Reference: identifier

        self.organization = None
        # reference to Reference: identifier

        self.insurer = None
        # reference to Reference: identifier

        self.facility = None
        # reference to Reference: identifier

        self.coverage = None
        # reference to Reference: identifier

        self.businessArrangement = None
        # type: str

        self.benefitCategory = None
        # reference to CodeableConcept

        self.benefitSubCategory = None
        # reference to CodeableConcept

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
             'child_entity': 'EligibilityRequest',
             'child_variable': 'provider'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'coverage'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'benefitCategory'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'insurer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'benefitSubCategory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'facility'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'priority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityRequest',
             'child_variable': 'organization'},
        ]
