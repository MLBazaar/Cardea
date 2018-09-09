from .fhirbase import fhirbase


class ClaimResponse(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'ClaimResponse'
        """
        This is a ClaimResponse resource

        type: string
        possible values: ClaimResponse
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.patient = None
        """
        Patient Resource.

        reference to Reference: identifier
        """

        self.created = None
        """
        The date when the enclosed suite of services were performed or
        completed.

        type: string
        """

        self.insurer = None
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

        self.request = None
        """
        Original request resource referrence.

        reference to Reference: identifier
        """

        self.outcome = None
        """
        Processing outcome errror, partial or complete processing.

        reference to CodeableConcept
        """

        self.disposition = None
        """
        A description of the status of the adjudication.

        type: string
        """

        self.payeeType = None
        """
        Party to be reimbursed: Subscriber, provider, other.

        reference to CodeableConcept
        """

        self.item = None
        """
        The first tier service adjudications for submitted services.

        type: array
        reference to ClaimResponse_Item
        """

        self.addItem = None
        """
        The first tier service adjudications for payor added services.

        type: array
        reference to ClaimResponse_AddItem
        """

        self.error = None
        """
        Mutually exclusive with Services Provided (Item).

        type: array
        reference to ClaimResponse_Error
        """

        self.totalCost = None
        """
        The total cost of the services reported.

        reference to Money
        """

        self.unallocDeductable = None
        """
        The amount of deductible applied which was not allocated to any
        particular service line.

        reference to Money
        """

        self.totalBenefit = None
        """
        Total amount of benefit payable (Equal to sum of the Benefit amounts
        from all detail lines and additions less the Unallocated Deductible).

        reference to Money
        """

        self.payment = None
        """
        Payment details for the claim if the claim has been paid.

        reference to ClaimResponse_Payment: identifier
        """

        self.reserved = None
        """
        Status of funds reservation (For provider, for Patient, None).

        reference to Coding
        """

        self.form = None
        """
        The form to be used for printing the content.

        reference to CodeableConcept
        """

        self.processNote = None
        """
        Note text.

        type: array
        reference to ClaimResponse_ProcessNote
        """

        self.communicationRequest = None
        """
        Request for additional supporting or authorizing information, such as:
        documents, images or resources.

        type: array
        reference to Reference: identifier
        """

        self.insurance = None
        """
        Financial instrument by which payment information for health care.

        type: array
        reference to ClaimResponse_Insurance
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
             'child_entity': 'ClaimResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'ClaimResponse_AddItem',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'addItem'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'totalBenefit'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'outcome'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'unallocDeductable'},

            {'parent_entity': 'ClaimResponse_Error',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'error'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'patient'},

            {'parent_entity': 'ClaimResponse_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'processNote'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'insurer'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'totalCost'},

            {'parent_entity': 'ClaimResponse_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'insurance'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'communicationRequest'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'reserved'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'request'},

            {'parent_entity': 'ClaimResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'item'},

            {'parent_entity': 'ClaimResponse_Payment',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'payment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'payeeType'},
        ]


class ClaimResponse_Item(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse_Item'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        """
        A service line number.

        type: int
        """

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudication results.

        type: array
        reference to ClaimResponse_Adjudication
        """

        self.detail = None
        """
        The second tier service adjudications for submitted services.

        type: array
        reference to ClaimResponse_Detail
        """

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
    """

    __name__ = 'ClaimResponse_Adjudication'

    def __init__(self, dict_values=None):
        self.category = None
        """
        Code indicating: Co-Pay, deductible, eligible, benefit, tax, etc.

        reference to CodeableConcept
        """

        self.reason = None
        """
        Adjudication reason such as limit reached.

        reference to CodeableConcept
        """

        self.amount = None
        """
        Monetary amount associated with the code.

        reference to Money
        """

        self.value = None
        """
        A non-monetary value for example a percentage. Mutually exclusive to
        the amount element above.

        type: int
        """

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

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'reason'},
        ]


class ClaimResponse_Detail(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse_Detail'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        """
        A service line number.

        type: int
        """

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ClaimResponse_Adjudication
        """

        self.subDetail = None
        """
        The third tier service adjudications for submitted services.

        type: array
        reference to ClaimResponse_SubDetail
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ClaimResponse_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail',
             'child_variable': 'subDetail'},

            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail',
             'child_variable': 'adjudication'},
        ]


class ClaimResponse_SubDetail(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse_SubDetail'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        """
        A service line number.

        type: int
        """

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ClaimResponse_Adjudication
        """

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
    """

    __name__ = 'ClaimResponse_AddItem'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        """
        List of input service items which this service line is intended to
        replace.

        type: array
        """

        self.revenue = None
        """
        The type of reveneu or cost center providing the product and/or
        service.

        reference to CodeableConcept
        """

        self.category = None
        """
        Health Care Service Type Codes  to identify the classification of
        service or benefits.

        reference to CodeableConcept
        """

        self.service = None
        """
        A code to indicate the Professional Service or Product supplied.

        reference to CodeableConcept
        """

        self.modifier = None
        """
        Item typification or modifiers codes, eg for Oral whether the
        treatment is cosmetic or associated with TMJ, or for medical whether
        the treatment was outside the clinic or out of office hours.

        type: array
        reference to CodeableConcept
        """

        self.fee = None
        """
        The fee charged for the professional service or product..

        reference to Money
        """

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ClaimResponse_Adjudication
        """

        self.detail = None
        """
        The second tier service adjudications for payor added services.

        type: array
        reference to ClaimResponse_Detail1
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'revenue'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'service'},

            {'parent_entity': 'ClaimResponse_Detail1',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'detail'},
        ]


class ClaimResponse_Detail1(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse_Detail1'

    def __init__(self, dict_values=None):
        self.revenue = None
        """
        The type of reveneu or cost center providing the product and/or
        service.

        reference to CodeableConcept
        """

        self.category = None
        """
        Health Care Service Type Codes  to identify the classification of
        service or benefits.

        reference to CodeableConcept
        """

        self.service = None
        """
        A code to indicate the Professional Service or Product supplied.

        reference to CodeableConcept
        """

        self.modifier = None
        """
        Item typification or modifiers codes, eg for Oral whether the
        treatment is cosmetic or associated with TMJ, or for medical whether
        the treatment was outside the clinic or out of office hours.

        type: array
        reference to CodeableConcept
        """

        self.fee = None
        """
        The fee charged for the professional service or product..

        reference to Money
        """

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ClaimResponse_Adjudication
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'revenue'},

            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'modifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Detail1',
             'child_variable': 'service'},
        ]


class ClaimResponse_Error(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse_Error'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        """
        The sequence number of the line item submitted which contains the
        error. This value is omitted when the error is elsewhere.

        type: int
        """

        self.detailSequenceLinkId = None
        """
        The sequence number of the addition within the line item submitted
        which contains the error. This value is omitted when the error is not
        related to an Addition.

        type: int
        """

        self.subdetailSequenceLinkId = None
        """
        The sequence number of the addition within the line item submitted
        which contains the error. This value is omitted when the error is not
        related to an Addition.

        type: int
        """

        self.code = None
        """
        An error code,from a specified code system, which details why the
        claim could not be adjudicated.

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
             'child_entity': 'ClaimResponse_Error',
             'child_variable': 'code'},
        ]


class ClaimResponse_Payment(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse_Payment'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Whether this represents partial or complete payment of the claim.

        reference to CodeableConcept
        """

        self.adjustment = None
        """
        Adjustment to the payment of this transaction which is not related to
        adjudication of this transaction.

        reference to Money
        """

        self.adjustmentReason = None
        """
        Reason for the payment adjustment.

        reference to CodeableConcept
        """

        self.date = None
        """
        Estimated payment data.

        type: string
        """

        self.amount = None
        """
        Payable less any payment adjustment.

        reference to Money
        """

        self.identifier = None
        """
        Payment identifier.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'adjustmentReason'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'adjustment'},
        ]


class ClaimResponse_ProcessNote(fhirbase):
    """
    This resource provides the adjudication details from the processing of
    a Claim resource.
    """

    __name__ = 'ClaimResponse_ProcessNote'

    def __init__(self, dict_values=None):
        self.number = None
        """
        An integer associated with each note which may be referred to from
        each service line item.

        type: int
        """

        self.type = None
        """
        The note purpose: Print/Display.

        reference to CodeableConcept
        """

        self.text = None
        """
        The note text.

        type: string
        """

        self.language = None
        """
        The ISO-639-1 alpha 2 code in lower case for the language, optionally
        followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in
        upper case; e.g. "en" for English, or "en-US" for American English
        versus "en-EN" for England English.

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
    """

    __name__ = 'ClaimResponse_Insurance'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        A service line item.

        type: int
        """

        self.focal = None
        """
        The instance number of the Coverage which is the focus for
        adjudication. The Coverage against which the claim is to be
        adjudicated.

        type: boolean
        """

        self.coverage = None
        """
        Reference to the program or plan identification, underwriter or payor.

        reference to Reference: identifier
        """

        self.businessArrangement = None
        """
        The contract number of a business agreement which describes the terms
        and conditions.

        type: string
        """

        self.preAuthRef = None
        """
        A list of references from the Insurer to which these services pertain.

        type: array
        """

        self.claimResponse = None
        """
        The Coverages adjudication details.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse_Insurance',
             'child_variable': 'claimResponse'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse_Insurance',
             'child_variable': 'coverage'},
        ]
