from .fhirbase import fhirbase


class ClaimResponse(fhirbase):
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # this is a claimresponse resource
        self.resourceType = 'ClaimResponse'
        # type = string
        # possible values: ClaimResponse

        # the status of the resource instance.
        self.status = None
        # type = string

        # patient resource.
        self.patient = None
        # reference to Reference: identifier

        # the date when the enclosed suite of services were performed or
        # completed.
        self.created = None
        # type = string

        # the insurer who produced this adjudicated response.
        self.insurer = None
        # reference to Reference: identifier

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.requestProvider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.requestOrganization = None
        # reference to Reference: identifier

        # original request resource referrence.
        self.request = None
        # reference to Reference: identifier

        # processing outcome errror, partial or complete processing.
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # a description of the status of the adjudication.
        self.disposition = None
        # type = string

        # party to be reimbursed: subscriber, provider, other.
        self.payeeType = None
        # reference to CodeableConcept: CodeableConcept

        # the first tier service adjudications for submitted services.
        self.item = None
        # type = array
        # reference to ClaimResponse_Item: ClaimResponse_Item

        # the first tier service adjudications for payor added services.
        self.addItem = None
        # type = array
        # reference to ClaimResponse_AddItem: ClaimResponse_AddItem

        # mutually exclusive with services provided (item).
        self.error = None
        # type = array
        # reference to ClaimResponse_Error: ClaimResponse_Error

        # the total cost of the services reported.
        self.totalCost = None
        # reference to Money: Money

        # the amount of deductible applied which was not allocated to any
        # particular service line.
        self.unallocDeductable = None
        # reference to Money: Money

        # total amount of benefit payable (equal to sum of the benefit amounts
        # from all detail lines and additions less the unallocated deductible).
        self.totalBenefit = None
        # reference to Money: Money

        # payment details for the claim if the claim has been paid.
        self.payment = None
        # reference to ClaimResponse_Payment: identifier

        # status of funds reservation (for provider, for patient, none).
        self.reserved = None
        # reference to Coding: Coding

        # the form to be used for printing the content.
        self.form = None
        # reference to CodeableConcept: CodeableConcept

        # note text.
        self.processNote = None
        # type = array
        # reference to ClaimResponse_ProcessNote: ClaimResponse_ProcessNote

        # request for additional supporting or authorizing information, such as:
        # documents, images or resources.
        self.communicationRequest = None
        # type = array
        # reference to Reference: identifier

        # financial instrument by which payment information for health care.
        self.insurance = None
        # type = array
        # reference to ClaimResponse_Insurance: ClaimResponse_Insurance

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
             'child_entity': 'ClaimResponse',
             'child_variable': 'communicationRequest'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'ClaimResponse_AddItem',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'addItem'},

            {'parent_entity': 'ClaimResponse_Payment',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'payment'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'totalBenefit'},

            {'parent_entity': 'ClaimResponse_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'insurance'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'insurer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'payeeType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'ClaimResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'item'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'totalCost'},

            {'parent_entity': 'ClaimResponse_Error',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'error'},

            {'parent_entity': 'ClaimResponse_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'processNote'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'form'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'reserved'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ClaimResponse',
             'child_variable': 'patient'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'unallocDeductable'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse',
             'child_variable': 'outcome'},
        ]


class ClaimResponse_Item(fhirbase):
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequenceLinkId = None
        # type = int

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudication results.
        self.adjudication = None
        # type = array
        # reference to ClaimResponse_Adjudication: ClaimResponse_Adjudication

        # the second tier service adjudications for submitted services.
        self.detail = None
        # type = array
        # reference to ClaimResponse_Detail: ClaimResponse_Detail

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Item',
             'child_variable': 'adjudication'},

            {'parent_entity': 'ClaimResponse_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Item',
             'child_variable': 'detail'},
        ]


class ClaimResponse_Adjudication(fhirbase):
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # code indicating: co-pay, deductible, eligible, benefit, tax, etc.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # adjudication reason such as limit reached.
        self.reason = None
        # reference to CodeableConcept: CodeableConcept

        # monetary amount associated with the code.
        self.amount = None
        # reference to Money: Money

        # a non-monetary value for example a percentage. mutually exclusive to the
        # amount element above.
        self.value = None
        # type = int

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'reason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'category'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Adjudication',
             'child_variable': 'amount'},
        ]


class ClaimResponse_Detail(fhirbase):
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequenceLinkId = None
        # type = int

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ClaimResponse_Adjudication: ClaimResponse_Adjudication

        # the third tier service adjudications for submitted services.
        self.subDetail = None
        # type = array
        # reference to ClaimResponse_SubDetail: ClaimResponse_SubDetail

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequenceLinkId = None
        # type = int

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ClaimResponse_Adjudication: ClaimResponse_Adjudication

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # list of input service items which this service line is intended to
        # replace.
        self.sequenceLinkId = None
        # type = array

        # the type of reveneu or cost center providing the product and/or service.
        self.revenue = None
        # reference to CodeableConcept: CodeableConcept

        # health care service type codes  to identify the classification of
        # service or benefits.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # a code to indicate the professional service or product supplied.
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the fee charged for the professional service or product..
        self.fee = None
        # reference to Money: Money

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ClaimResponse_Adjudication: ClaimResponse_Adjudication

        # the second tier service adjudications for payor added services.
        self.detail = None
        # type = array
        # reference to ClaimResponse_Detail1: ClaimResponse_Detail1

        # unique identifier for object class
        self.object_id = None

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

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'revenue'},

            {'parent_entity': 'ClaimResponse_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_AddItem',
             'child_variable': 'fee'},
        ]


class ClaimResponse_Detail1(fhirbase):
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # the type of reveneu or cost center providing the product and/or service.
        self.revenue = None
        # reference to CodeableConcept: CodeableConcept

        # health care service type codes  to identify the classification of
        # service or benefits.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # a code to indicate the professional service or product supplied.
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the fee charged for the professional service or product..
        self.fee = None
        # reference to Money: Money

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ClaimResponse_Adjudication: ClaimResponse_Adjudication

        # unique identifier for object class
        self.object_id = None

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
             'child_variable': 'category'},

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
             'child_variable': 'modifier'},
        ]


class ClaimResponse_Error(fhirbase):
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # the sequence number of the line item submitted which contains the error.
        # this value is omitted when the error is elsewhere.
        self.sequenceLinkId = None
        # type = int

        # the sequence number of the addition within the line item submitted which
        # contains the error. this value is omitted when the error is not related
        # to an addition.
        self.detailSequenceLinkId = None
        # type = int

        # the sequence number of the addition within the line item submitted which
        # contains the error. this value is omitted when the error is not related
        # to an addition.
        self.subdetailSequenceLinkId = None
        # type = int

        # an error code,from a specified code system, which details why the claim
        # could not be adjudicated.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # whether this represents partial or complete payment of the claim.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # adjustment to the payment of this transaction which is not related to
        # adjudication of this transaction.
        self.adjustment = None
        # reference to Money: Money

        # reason for the payment adjustment.
        self.adjustmentReason = None
        # reference to CodeableConcept: CodeableConcept

        # estimated payment data.
        self.date = None
        # type = string

        # payable less any payment adjustment.
        self.amount = None
        # reference to Money: Money

        # payment identifier.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'amount'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'identifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'adjustment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ClaimResponse_Payment',
             'child_variable': 'adjustmentReason'},
        ]


class ClaimResponse_ProcessNote(fhirbase):
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # an integer associated with each note which may be referred to from each
        # service line item.
        self.number = None
        # type = int

        # the note purpose: print/display.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the note text.
        self.text = None
        # type = string

        # the iso-639-1 alpha 2 code in lower case for the language, optionally
        # followed by a hyphen and the iso-3166-1 alpha 2 code for the region in
        # upper case; e.g. "en" for english, or "en-us" for american english
        # versus "en-en" for england english.
        self.language = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    def __init__(self, dict_values=None):
        # a service line item.
        self.sequence = None
        # type = int

        # the instance number of the coverage which is the focus for adjudication.
        # the coverage against which the claim is to be adjudicated.
        self.focal = None
        # type = boolean

        # reference to the program or plan identification, underwriter or payor.
        self.coverage = None
        # reference to Reference: identifier

        # the contract number of a business agreement which describes the terms
        # and conditions.
        self.businessArrangement = None
        # type = string

        # a list of references from the insurer to which these services pertain.
        self.preAuthRef = None
        # type = array

        # the coverages adjudication details.
        self.claimResponse = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
