from .fhirbase import * 
from .Reference import Reference
from .Identifier import Identifier
from .Period import Period
from .CodeableConcept import CodeableConcept

class EligibilityRequest(fhirbase):
    """The EligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    EligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """

    def __init__(self, dict_values=None):
        # this is a eligibilityrequest resource
        self.resourceType = 'EligibilityRequest'
        # type = string
        # possible values = EligibilityRequest

        # the status of the resource instance.
        self.status = None
        # type = string

        # immediate (stat), best effort (normal), deferred (defer).
        self.priority = None
        # reference to CodeableConcept: CodeableConcept

        # patient resource.
        self.patient = None
        # reference to Reference: identifier

        # the date or dates when the enclosed suite of services were performed or
        # completed.
        self.servicedDate = None
        # type = string

        # the date or dates when the enclosed suite of services were performed or
        # completed.
        self.servicedPeriod = None
        # reference to Period: Period

        # the date when this resource was created.
        self.created = None
        # type = string

        # person who created the invoice/claim/pre-determination or pre-
        # authorization.
        self.enterer = None
        # reference to Reference: identifier

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.provider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.organization = None
        # reference to Reference: identifier

        # the insurer who is target  of the request.
        self.insurer = None
        # reference to Reference: identifier

        # facility where the services were provided.
        self.facility = None
        # reference to Reference: identifier

        # financial instrument by which payment information for health care.
        self.coverage = None
        # reference to Reference: identifier

        # the contract number of a business agreement which describes the terms
        # and conditions.
        self.businessArrangement = None
        # type = string

        # dental, vision, medical, pharmacy, rehab etc.
        self.benefitCategory = None
        # reference to CodeableConcept: CodeableConcept

        # dental: basic, major, ortho; vision exam, glasses, contacts; etc.
        self.benefitSubCategory = None
        # reference to CodeableConcept: CodeableConcept

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
            'child_entity': 'EligibilityRequest',
            'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'patient'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'insurer'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'coverage'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'benefitCategory'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'organization'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'priority'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'facility'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'benefitSubCategory'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'provider'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityRequest',
            'child_variable': 'servicedPeriod'},
        ]

