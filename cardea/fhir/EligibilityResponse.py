from .fhirbase import fhirbase


class EligibilityResponse(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.

    Args:
        resourceType: This is a EligibilityResponse resource
        identifier: The Response business identifier.
        status: The status of the resource instance.
        created: The date when the enclosed suite of services were performed
            or completed.
        requestProvider: The practitioner who is responsible for the services
            rendered to the patient.
        requestOrganization: The organization which is responsible for the
            services rendered to the patient.
        request: Original request resource reference.
        outcome: Transaction status: error, complete.
        disposition: A description of the status of the adjudication.
        insurer: The Insurer who produced this adjudicated response.
        inforce: Flag indicating if the coverage provided is inforce currently
            if no service date(s) specified or for the whole duration of the
            service dates.
        insurance: The insurer may provide both the details for the requested
            coverage as well as details for additional coverages known to the
            insurer.
        form: The form to be used for printing the content.
        error: Mutually exclusive with Services Provided (Item).
    """

    __name__ = 'EligibilityResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'EligibilityResponse'
        # type: str
        # possible values: EligibilityResponse

        self.status = None
        # type: str

        self.created = None
        # type: str

        self.requestProvider = None
        # reference to Reference: identifier

        self.requestOrganization = None
        # reference to Reference: identifier

        self.request = None
        # reference to Reference: identifier

        self.outcome = None
        # reference to CodeableConcept

        self.disposition = None
        # type: str

        self.insurer = None
        # reference to Reference: identifier

        self.inforce = None
        # type: bool

        self.insurance = None
        # type: list
        # reference to EligibilityResponse_Insurance

        self.form = None
        # reference to CodeableConcept

        self.error = None
        # type: list
        # reference to EligibilityResponse_Error

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
             'child_entity': 'EligibilityResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'EligibilityResponse_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'insurance'},

            {'parent_entity': 'EligibilityResponse_Error',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'error'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'insurer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'request'},
        ]


class EligibilityResponse_Insurance(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.

    Args:
        coverage: A suite of updated or additional Coverages from the Insurer.
        contract: The contract resource which may provide more detailed
            information.
        benefitBalance: Benefits and optionally current balances by Category.
    """

    __name__ = 'EligibilityResponse_Insurance'

    def __init__(self, dict_values=None):
        self.coverage = None
        # reference to Reference: identifier

        self.contract = None
        # reference to Reference: identifier

        self.benefitBalance = None
        # type: list
        # reference to EligibilityResponse_BenefitBalance

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse_Insurance',
             'child_variable': 'coverage'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse_Insurance',
             'child_variable': 'contract'},

            {'parent_entity': 'EligibilityResponse_BenefitBalance',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Insurance',
             'child_variable': 'benefitBalance'},
        ]


class EligibilityResponse_BenefitBalance(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.

    Args:
        category: Dental, Vision, Medical, Pharmacy, Rehab etc.
        subCategory: Dental: basic, major, ortho; Vision exam, glasses,
            contacts; etc.
        excluded: True if the indicated class of service is excluded from the
            plan, missing or False indicated the service is included in the
            coverage.
        name: A short name or tag for the benefit, for example MED01, or
            DENT2.
        description: A richer description of the benefit, for example 'DENT2
            covers 100% of basic, 50% of major but exclused Ortho, Implants and
            Costmetic services'.
        network: Network designation.
        unit: Unit designation: individual or family.
        term: The term or period of the values such as 'maximum lifetime
            benefit' or 'maximum annual vistis'.
        financial: Benefits Used to date.
    """

    __name__ = 'EligibilityResponse_BenefitBalance'

    def __init__(self, dict_values=None):
        self.category = None
        # reference to CodeableConcept

        self.subCategory = None
        # reference to CodeableConcept

        self.excluded = None
        # type: bool

        self.name = None
        # type: str

        self.description = None
        # type: str

        self.network = None
        # reference to CodeableConcept

        self.unit = None
        # reference to CodeableConcept

        self.term = None
        # reference to CodeableConcept

        self.financial = None
        # type: list
        # reference to EligibilityResponse_Financial

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'unit'},

            {'parent_entity': 'EligibilityResponse_Financial',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'financial'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'network'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'subCategory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'term'},
        ]


class EligibilityResponse_Financial(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.

    Args:
        type: Deductable, visits, benefit amount.
        allowedUnsignedInt: Benefits allowed.
        allowedString: Benefits allowed.
        allowedMoney: Benefits allowed.
        usedUnsignedInt: Benefits used.
        usedMoney: Benefits used.
    """

    __name__ = 'EligibilityResponse_Financial'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.allowedUnsignedInt = None
        # type: int

        self.allowedString = None
        # type: str

        self.allowedMoney = None
        # reference to Money

        self.usedUnsignedInt = None
        # type: int

        self.usedMoney = None
        # reference to Money

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Financial',
             'child_variable': 'usedMoney'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Financial',
             'child_variable': 'allowedMoney'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Financial',
             'child_variable': 'type'},
        ]


class EligibilityResponse_Error(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.

    Args:
        code: An error code,from a specified code system, which details why
            the eligibility check could not be performed.
    """

    __name__ = 'EligibilityResponse_Error'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Error',
             'child_variable': 'code'},
        ]
