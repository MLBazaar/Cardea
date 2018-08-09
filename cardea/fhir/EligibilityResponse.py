from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Reference import Reference

class EligibilityResponse(fhirbase):
    """This resource provides eligibility and plan details from the processing
    of an Eligibility resource.
    """

    def __init__(self, dict_values=None):
        # this is a eligibilityresponse resource
        self.resourceType = 'EligibilityResponse'
        # type = string
        # possible values = EligibilityResponse

        # the status of the resource instance.
        self.status = None
        # type = string

        # the date when the enclosed suite of services were performed or
        # completed.
        self.created = None
        # type = string

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.requestProvider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.requestOrganization = None
        # reference to Reference: identifier

        # original request resource reference.
        self.request = None
        # reference to Reference: identifier

        # transaction status: error, complete.
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # a description of the status of the adjudication.
        self.disposition = None
        # type = string

        # the insurer who produced this adjudicated response.
        self.insurer = None
        # reference to Reference: identifier

        # flag indicating if the coverage provided is inforce currently  if no
        # service date(s) specified or for the whole duration of the service
        # dates.
        self.inforce = None
        # type = boolean

        # the insurer may provide both the details for the requested coverage as
        # well as details for additional coverages known to the insurer.
        self.insurance = None
        # type = array
        # reference to EligibilityResponse_Insurance: EligibilityResponse_Insurance

        # the form to be used for printing the content.
        self.form = None
        # reference to CodeableConcept: CodeableConcept

        # mutually exclusive with services provided (item).
        self.error = None
        # type = array
        # reference to EligibilityResponse_Error: EligibilityResponse_Error

        # the response business identifier.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'form'},

            {'parent_entity': 'EligibilityResponse_Insurance',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'insurance'},

            {'parent_entity': 'EligibilityResponse_Error',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'error'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'outcome'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'requestProvider'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'request'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityResponse',
            'child_variable': 'insurer'},
        ]

class EligibilityResponse_Insurance(fhirbase):
    """This resource provides eligibility and plan details from the processing
    of an Eligibility resource.
    """

    def __init__(self, dict_values=None):
        # a suite of updated or additional coverages from the insurer.
        self.coverage = None
        # reference to Reference: identifier

        # the contract resource which may provide more detailed information.
        self.contract = None
        # reference to Reference: identifier

        # benefits and optionally current balances by category.
        self.benefitBalance = None
        # type = array
        # reference to EligibilityResponse_BenefitBalance: EligibilityResponse_BenefitBalance


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'EligibilityResponse_BenefitBalance',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_Insurance',
            'child_variable': 'benefitBalance'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityResponse_Insurance',
            'child_variable': 'contract'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'EligibilityResponse_Insurance',
            'child_variable': 'coverage'},
        ]

class EligibilityResponse_BenefitBalance(fhirbase):
    """This resource provides eligibility and plan details from the processing
    of an Eligibility resource.
    """

    def __init__(self, dict_values=None):
        # dental, vision, medical, pharmacy, rehab etc.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # dental: basic, major, ortho; vision exam, glasses, contacts; etc.
        self.subCategory = None
        # reference to CodeableConcept: CodeableConcept

        # true if the indicated class of service is excluded from the plan,
        # missing or false indicated the service is included in the coverage.
        self.excluded = None
        # type = boolean

        # a short name or tag for the benefit, for example med01, or dent2.
        self.name = None
        # type = string

        # a richer description of the benefit, for example 'dent2 covers 100% of
        # basic, 50% of major but exclused ortho, implants and costmetic
        # services'.
        self.description = None
        # type = string

        # network designation.
        self.network = None
        # reference to CodeableConcept: CodeableConcept

        # unit designation: individual or family.
        self.unit = None
        # reference to CodeableConcept: CodeableConcept

        # the term or period of the values such as 'maximum lifetime benefit' or
        # 'maximum annual vistis'.
        self.term = None
        # reference to CodeableConcept: CodeableConcept

        # benefits used to date.
        self.financial = None
        # type = array
        # reference to EligibilityResponse_Financial: EligibilityResponse_Financial


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'EligibilityResponse_Financial',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_BenefitBalance',
            'child_variable': 'financial'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_BenefitBalance',
            'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_BenefitBalance',
            'child_variable': 'unit'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_BenefitBalance',
            'child_variable': 'term'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_BenefitBalance',
            'child_variable': 'network'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_BenefitBalance',
            'child_variable': 'subCategory'},
        ]

class EligibilityResponse_Financial(fhirbase):
    """This resource provides eligibility and plan details from the processing
    of an Eligibility resource.
    """

    def __init__(self, dict_values=None):
        # deductable, visits, benefit amount.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # benefits allowed.
        self.allowedUnsignedInt = None
        # type = int

        # benefits allowed.
        self.allowedString = None
        # type = string

        # benefits allowed.
        self.allowedMoney = None
        # reference to Money: Money

        # benefits used.
        self.usedUnsignedInt = None
        # type = int

        # benefits used.
        self.usedMoney = None
        # reference to Money: Money


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_Financial',
            'child_variable': 'allowedMoney'},

            {'parent_entity': 'Money',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_Financial',
            'child_variable': 'usedMoney'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_Financial',
            'child_variable': 'type'},
        ]

class EligibilityResponse_Error(fhirbase):
    """This resource provides eligibility and plan details from the processing
    of an Eligibility resource.
    """

    def __init__(self, dict_values=None):
        # an error code,from a specified code system, which details why the
        # eligibility check could not be performed.
        self.code = None
        # reference to CodeableConcept: CodeableConcept


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'EligibilityResponse_Error',
            'child_variable': 'code'},
        ]

