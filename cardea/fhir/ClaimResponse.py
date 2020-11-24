from .fhirbase import fhirbase


class ClaimResponse(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        resourceType: This is a ClaimResponse resource
        identifier: The Response business identifier.
        status: The status of the resource instance.
        patient: Patient Resource.
        created: The date when the enclosed suite of services were performed
            or completed.
        insurer: The Insurer who produced this adjudicated response.
        requestProvider: The practitioner who is responsible for the services
            rendered to the patient.
        requestOrganization: The organization which is responsible for the
            services rendered to the patient.
        request: Original request resource referrence.
        outcome: Processing outcome errror, partial or complete processing.
        disposition: A description of the status of the adjudication.
        payeeType: Party to be reimbursed: Subscriber, provider, other.
        item: The first tier service adjudications for submitted services.
        addItem: The first tier service adjudications for payor added
            services.
        error: Mutually exclusive with Services Provided (Item).
        totalCost: The total cost of the services reported.
        unallocDeductable: The amount of deductible applied which was not
            allocated to any particular service line.
        totalBenefit: Total amount of benefit payable (Equal to sum of the
            Benefit amounts from all detail lines and additions less the
            Unallocated Deductible).
        payment: Payment details for the claim if the claim has been paid.
        reserved: Status of funds reservation (For provider, for Patient,
            None).
        form: The form to be used for printing the content.
        processNote: Note text.
        communicationRequest: Request for additional supporting or authorizing
            information, such as: documents, images or resources.
        insurance: Financial instrument by which payment information for
            health care.
    """

    __name__ = 'ClaimResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'ClaimResponse'
        # type: str
        # possible values: ClaimResponse

        self.status = None
        # type: str

        self.patient = None
        # reference to Reference: identifier

        self.created = None
        # type: str

        self.insurer = None
        # reference to Reference: identifier

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

        self.payeeType = None
        # reference to CodeableConcept

        self.item = None
        # type: list
        # reference to ClaimResponse_Item

        self.addItem = None
        # type: list
        # reference to ClaimResponse_AddItem

        self.error = None
        # type: list
        # reference to ClaimResponse_Error

        self.totalCost = None
        # reference to Money

        self.unallocDeductable = None
        # reference to Money

        self.totalBenefit = None
        # reference to Money

        self.payment = None
        # reference to ClaimResponse_Payment: identifier

        self.reserved = None
        # reference to Coding

        self.form = None
        # reference to CodeableConcept

        self.processNote = None
        # type: list
        # reference to ClaimResponse_ProcessNote

        self.communicationRequest = None
        # type: list
        # reference to Reference: identifier

        self.insurance = None
        # type: list
        # reference to ClaimResponse_Insurance

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
             'child_entity': 'ClaimResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'ClaimResponse_AddItem',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'addItem'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'reserved'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'totalCost'},

            {'parent_entity': 'ClaimResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'item'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'unallocDeductable'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'insurer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'payeeType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'ClaimResponse_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'processNote'},

            {'parent_entity': 'ClaimResponse_Payment',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'payment'},

            {'parent_entity': 'ClaimResponse_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'insurance'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'request'},

            {'parent_entity': 'ClaimResponse_Error',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'error'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'totalBenefit'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'communicationRequest'},
        ]


class ClaimResponse_Item(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        sequenceLinkId: A service line number.
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudication results.
        detail: The second tier service adjudications for submitted services.
    """

    __name__ = 'ClaimResponse_Item'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        # type: int

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ClaimResponse_Adjudication

        self.detail = None
        # type: list
        # reference to ClaimResponse_Detail

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ClaimResponse_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Item',
             'child_variable': 'detail'},

            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Item',
             'child_variable': 'adjudication'},
        ]


class ClaimResponse_Adjudication(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        category: Code indicating: Co-Pay, deductible, eligible, benefit, tax,
            etc.
        reason: Adjudication reason such as limit reached.
        amount: Monetary amount associated with the code.
        value: A non-monetary value for example a percentage. Mutually
            exclusive to the amount element above.
    """

    __name__ = 'ClaimResponse_Adjudication'

    def __init__(self, dict_values=None):
        self.category = None
        # reference to CodeableConcept

        self.reason = None
        # reference to CodeableConcept

        self.amount = None
        # reference to Money

        self.value = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'reason'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'amount'},
        ]


class ClaimResponse_Detail(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        sequenceLinkId: A service line number.
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
        subDetail: The third tier service adjudications for submitted
            services.
    """

    __name__ = 'ClaimResponse_Detail'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        # type: int

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ClaimResponse_Adjudication

        self.subDetail = None
        # type: list
        # reference to ClaimResponse_SubDetail

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail',
             'child_variable': 'adjudication'},

            {'parent_entity': 'ClaimResponse_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail',
             'child_variable': 'subDetail'},
        ]


class ClaimResponse_SubDetail(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        sequenceLinkId: A service line number.
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
    """

    __name__ = 'ClaimResponse_SubDetail'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        # type: int

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ClaimResponse_Adjudication

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_SubDetail',
             'child_variable': 'adjudication'},
        ]


class ClaimResponse_AddItem(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        sequenceLinkId: List of input service items which this service line is
            intended to replace.
        revenue: The type of reveneu or cost center providing the product
            and/or service.
        category: Health Care Service Type Codes  to identify the
            classification of service or benefits.
        service: A code to indicate the Professional Service or Product
            supplied.
        modifier: Item typification or modifiers codes, eg for Oral whether
            the treatment is cosmetic or associated with TMJ, or for medical
            whether the treatment was outside the clinic or out of office hours.
        fee: The fee charged for the professional service or product..
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
        detail: The second tier service adjudications for payor added
            services.
    """

    __name__ = 'ClaimResponse_AddItem'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        # type: list

        self.revenue = None
        # reference to CodeableConcept

        self.category = None
        # reference to CodeableConcept

        self.service = None
        # reference to CodeableConcept

        self.modifier = None
        # type: list
        # reference to CodeableConcept

        self.fee = None
        # reference to Money

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ClaimResponse_Adjudication

        self.detail = None
        # type: list
        # reference to ClaimResponse_Detail1

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ClaimResponse_Detail1',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'service'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'revenue'},

            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'category'},
        ]


class ClaimResponse_Detail1(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        revenue: The type of reveneu or cost center providing the product
            and/or service.
        category: Health Care Service Type Codes  to identify the
            classification of service or benefits.
        service: A code to indicate the Professional Service or Product
            supplied.
        modifier: Item typification or modifiers codes, eg for Oral whether
            the treatment is cosmetic or associated with TMJ, or for medical
            whether the treatment was outside the clinic or out of office hours.
        fee: The fee charged for the professional service or product..
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
    """

    __name__ = 'ClaimResponse_Detail1'

    def __init__(self, dict_values=None):
        self.revenue = None
        # reference to CodeableConcept

        self.category = None
        # reference to CodeableConcept

        self.service = None
        # reference to CodeableConcept

        self.modifier = None
        # type: list
        # reference to CodeableConcept

        self.fee = None
        # reference to Money

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ClaimResponse_Adjudication

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'category'},

            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'modifier'},
        ]


class ClaimResponse_Error(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        sequenceLinkId: The sequence number of the line item submitted which
            contains the error. This value is omitted when the error is elsewhere.
        detailSequenceLinkId: The sequence number of the addition within the
            line item submitted which contains the error. This value is omitted
            when the error is not related to an Addition.
        subdetailSequenceLinkId: The sequence number of the addition within
            the line item submitted which contains the error. This value is
            omitted when the error is not related to an Addition.
        code: An error code,from a specified code system, which details why
            the claim could not be adjudicated.
    """

    __name__ = 'ClaimResponse_Error'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        # type: int

        self.detailSequenceLinkId = None
        # type: int

        self.subdetailSequenceLinkId = None
        # type: int

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
             'child_entity': 'ClaimResponse_Error',
             'child_variable': 'code'},
        ]


class ClaimResponse_Payment(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        type: Whether this represents partial or complete payment of the
            claim.
        adjustment: Adjustment to the payment of this transaction which is not
            related to adjudication of this transaction.
        adjustmentReason: Reason for the payment adjustment.
        date: Estimated payment data.
        amount: Payable less any payment adjustment.
        identifier: Payment identifier.
    """

    __name__ = 'ClaimResponse_Payment'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.adjustment = None
        # reference to Money

        self.adjustmentReason = None
        # reference to CodeableConcept

        self.date = None
        # type: str

        self.amount = None
        # reference to Money

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'adjustmentReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'adjustment'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'identifier'},
        ]


class ClaimResponse_ProcessNote(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        number: An integer associated with each note which may be referred to
            from each service line item.
        type: The note purpose: Print/Display.
        text: The note text.
        language: The ISO-639-1 alpha 2 code in lower case for the language,
            optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for
            the region in upper case; e.g. "en" for English, or "en-US" for
            American English versus "en-EN" for England English.
    """

    __name__ = 'ClaimResponse_ProcessNote'

    def __init__(self, dict_values=None):
        self.number = None
        # type: int

        self.type = None
        # reference to CodeableConcept

        self.text = None
        # type: str

        self.language = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_ProcessNote',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_ProcessNote',
             'child_variable': 'language'},
        ]


class ClaimResponse_Insurance(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.

    Args:
        sequence: A service line item.
        focal: The instance number of the Coverage which is the focus for
            adjudication. The Coverage against which the claim is to be
            adjudicated.
        coverage: Reference to the program or plan identification, underwriter
            or payor.
        businessArrangement: The contract number of a business agreement which
            describes the terms and conditions.
        preAuthRef: A list of references from the Insurer to which these
            services pertain.
        claimResponse: The Coverages adjudication details.
    """

    __name__ = 'ClaimResponse_Insurance'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.focal = None
        # type: bool

        self.coverage = None
        # reference to Reference: identifier

        self.businessArrangement = None
        # type: str

        self.preAuthRef = None
        # type: list

        self.claimResponse = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse_Insurance',
             'child_variable': 'coverage'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse_Insurance',
             'child_variable': 'claimResponse'},
        ]
