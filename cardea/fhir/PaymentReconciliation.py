from .fhirbase import fhirbase


class PaymentReconciliation(fhirbase):
    """This resource provides payment details and claim references supporting a
    bulk payment.
    """

    __name__ = 'PaymentReconciliation'

    def __init__(self, dict_values=None):
        # this is a paymentreconciliation resource
        self.resourceType = 'PaymentReconciliation'
        # type = string
        # possible values: PaymentReconciliation

        # the status of the resource instance.
        self.status = None
        # type = string

        # the period of time for which payments have been gathered into this bulk
        # payment for settlement.
        self.period = None
        # reference to Period: Period

        # the date when the enclosed suite of services were performed or
        # completed.
        self.created = None
        # type = string

        # the insurer who produced this adjudicated response.
        self.organization = None
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

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.requestProvider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.requestOrganization = None
        # reference to Reference: identifier

        # list of individual settlement amounts and the corresponding transaction.
        self.detail = None
        # type = array
        # reference to PaymentReconciliation_Detail: PaymentReconciliation_Detail

        # the form to be used for printing the content.
        self.form = None
        # reference to CodeableConcept: CodeableConcept

        # total payment amount.
        self.total = None
        # reference to Money: Money

        # suite of notes.
        self.processNote = None
        # type = array
        # reference to PaymentReconciliation_ProcessNote: PaymentReconciliation_ProcessNote

        # the response business identifier.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'total'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'request'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'organization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'form'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'outcome'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'PaymentReconciliation_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'detail'},

            {'parent_entity': 'PaymentReconciliation_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'processNote'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'requestProvider'},
        ]


class PaymentReconciliation_Detail(fhirbase):
    """This resource provides payment details and claim references supporting a
    bulk payment.
    """

    __name__ = 'PaymentReconciliation_Detail'

    def __init__(self, dict_values=None):
        # code to indicate the nature of the payment, adjustment, funds advance,
        # etc.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the claim or financial resource.
        self.request = None
        # reference to Reference: identifier

        # the claim response resource.
        self.response = None
        # reference to Reference: identifier

        # the organization which submitted the claim or financial transaction.
        self.submitter = None
        # reference to Reference: identifier

        # the organization which is receiving the payment.
        self.payee = None
        # reference to Reference: identifier

        # the date of the invoice or financial resource.
        self.date = None
        # type = string

        # amount paid for this detail.
        self.amount = None
        # reference to Money: Money

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'payee'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'response'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'amount'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'submitter'},
        ]


class PaymentReconciliation_ProcessNote(fhirbase):
    """This resource provides payment details and claim references supporting a
    bulk payment.
    """

    __name__ = 'PaymentReconciliation_ProcessNote'

    def __init__(self, dict_values=None):
        # the note purpose: print/display.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the note text.
        self.text = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation_ProcessNote',
             'child_variable': 'type'},
        ]
