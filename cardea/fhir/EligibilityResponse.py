from .fhirbase import fhirbase


class EligibilityResponse(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.
    """

    __name__ = 'EligibilityResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'EligibilityResponse'
        """
        This is a EligibilityResponse resource

        type: string
        possible values: EligibilityResponse
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.created = None
        """
        The date when the enclosed suite of services were performed or
        completed.

        type: string
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

        self.request = None
        """
        Original request resource reference.

        reference to Reference: identifier
        """

        self.outcome = None
        """
        Transaction status: error, complete.

        reference to CodeableConcept
        """

        self.disposition = None
        """
        A description of the status of the adjudication.

        type: string
        """

        self.insurer = None
        """
        The Insurer who produced this adjudicated response.

        reference to Reference: identifier
        """

        self.inforce = None
        """
        Flag indicating if the coverage provided is inforce currently  if no
        service date(s) specified or for the whole duration of the service
        dates.

        type: boolean
        """

        self.insurance = None
        """
        The insurer may provide both the details for the requested coverage as
        well as details for additional coverages known to the insurer.

        type: array
        reference to EligibilityResponse_Insurance
        """

        self.form = None
        """
        The form to be used for printing the content.

        reference to CodeableConcept
        """

        self.error = None
        """
        Mutually exclusive with Services Provided (Item).

        type: array
        reference to EligibilityResponse_Error
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
             'child_entity': 'EligibilityResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'insurer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse',
             'child_variable': 'identifier'},

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
             'child_variable': 'requestProvider'},
        ]


class EligibilityResponse_Insurance(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.
    """

    __name__ = 'EligibilityResponse_Insurance'

    def __init__(self, dict_values=None):
        self.coverage = None
        """
        A suite of updated or additional Coverages from the Insurer.

        reference to Reference: identifier
        """

        self.contract = None
        """
        The contract resource which may provide more detailed information.

        reference to Reference: identifier
        """

        self.benefitBalance = None
        """
        Benefits and optionally current balances by Category.

        type: array
        reference to EligibilityResponse_BenefitBalance
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse_Insurance',
             'child_variable': 'contract'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'EligibilityResponse_Insurance',
             'child_variable': 'coverage'},

            {'parent_entity': 'EligibilityResponse_BenefitBalance',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Insurance',
             'child_variable': 'benefitBalance'},
        ]


class EligibilityResponse_BenefitBalance(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.
    """

    __name__ = 'EligibilityResponse_BenefitBalance'

    def __init__(self, dict_values=None):
        self.category = None
        """
        Dental, Vision, Medical, Pharmacy, Rehab etc.

        reference to CodeableConcept
        """

        self.subCategory = None
        """
        Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.

        reference to CodeableConcept
        """

        self.excluded = None
        """
        True if the indicated class of service is excluded from the plan,
        missing or False indicated the service is included in the coverage.

        type: boolean
        """

        self.name = None
        """
        A short name or tag for the benefit, for example MED01, or DENT2.

        type: string
        """

        self.description = None
        """
        A richer description of the benefit, for example 'DENT2 covers 100% of
        basic, 50% of major but exclused Ortho, Implants and Costmetic
        services'.

        type: string
        """

        self.network = None
        """
        Network designation.

        reference to CodeableConcept
        """

        self.unit = None
        """
        Unit designation: individual or family.

        reference to CodeableConcept
        """

        self.term = None
        """
        The term or period of the values such as 'maximum lifetime benefit' or
        'maximum annual vistis'.

        reference to CodeableConcept
        """

        self.financial = None
        """
        Benefits Used to date.

        type: array
        reference to EligibilityResponse_Financial
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'term'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'unit'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'network'},

            {'parent_entity': 'EligibilityResponse_Financial',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'financial'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'subCategory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_BenefitBalance',
             'child_variable': 'category'},
        ]


class EligibilityResponse_Financial(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.
    """

    __name__ = 'EligibilityResponse_Financial'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Deductable, visits, benefit amount.

        reference to CodeableConcept
        """

        self.allowedUnsignedInt = None
        """
        Benefits allowed.

        type: int
        """

        self.allowedString = None
        """
        Benefits allowed.

        type: string
        """

        self.allowedMoney = None
        """
        Benefits allowed.

        reference to Money
        """

        self.usedUnsignedInt = None
        """
        Benefits used.

        type: int
        """

        self.usedMoney = None
        """
        Benefits used.

        reference to Money
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Financial',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Financial',
             'child_variable': 'usedMoney'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'EligibilityResponse_Financial',
             'child_variable': 'allowedMoney'},
        ]


class EligibilityResponse_Error(fhirbase):
    """
    This resource provides eligibility and plan details from the
    processing of an Eligibility resource.
    """

    __name__ = 'EligibilityResponse_Error'

    def __init__(self, dict_values=None):
        self.code = None
        """
        An error code,from a specified code system, which details why the
        eligibility check could not be performed.

        reference to CodeableConcept
        """

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
