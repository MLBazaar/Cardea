from .fhirbase import fhirbase


class PaymentReconciliation(fhirbase):
    """
    This resource provides payment details and claim references supporting
    a bulk payment.

    Attributes:
        resourceType: This is a PaymentReconciliation resource
        identifier: The Response business identifier.
        status: The status of the resource instance.
        period: The period of time for which payments have been gathered into
            this bulk payment for settlement.
        created: The date when the enclosed suite of services were performed
            or completed.
        organization: The Insurer who produced this adjudicated response.
        request: Original request resource reference.
        outcome: Transaction status: error, complete.
        disposition: A description of the status of the adjudication.
        requestProvider: The practitioner who is responsible for the services
            rendered to the patient.
        requestOrganization: The organization which is responsible for the
            services rendered to the patient.
        detail: List of individual settlement amounts and the corresponding
            transaction.
        form: The form to be used for printing the content.
        total: Total payment amount.
        processNote: Suite of notes.
    """

    __name__ = 'PaymentReconciliation'

    def __init__(self, dict_values=None):
        self.resourceType = 'PaymentReconciliation'
        # type: string
        # possible values: PaymentReconciliation

        self.status = None
        # type: string

        self.period = None
        # reference to Period

        self.created = None
        # type: string

        self.organization = None
        # reference to Reference: identifier

        self.request = None
        # reference to Reference: identifier

        self.outcome = None
        # reference to CodeableConcept

        self.disposition = None
        # type: string

        self.requestProvider = None
        # reference to Reference: identifier

        self.requestOrganization = None
        # reference to Reference: identifier

        self.detail = None
        # type: array
        # reference to PaymentReconciliation_Detail

        self.form = None
        # reference to CodeableConcept

        self.total = None
        # reference to Money

        self.processNote = None
        # type: array
        # reference to PaymentReconciliation_ProcessNote

        self.identifier = None
        # type: array
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'total'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'outcome'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'request'},

            {'parent_entity': 'PaymentReconciliation_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'form'},

            {'parent_entity': 'PaymentReconciliation_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'processNote'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'requestProvider'},
        ]


class PaymentReconciliation_Detail(fhirbase):
    """
    This resource provides payment details and claim references supporting
    a bulk payment.

    Attributes:
        type: Code to indicate the nature of the payment, adjustment, funds
            advance, etc.
        request: The claim or financial resource.
        response: The claim response resource.
        submitter: The Organization which submitted the claim or financial
            transaction.
        payee: The organization which is receiving the payment.
        date: The date of the invoice or financial resource.
        amount: Amount paid for this detail.
    """

    __name__ = 'PaymentReconciliation_Detail'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.request = None
        # reference to Reference: identifier

        self.response = None
        # reference to Reference: identifier

        self.submitter = None
        # reference to Reference: identifier

        self.payee = None
        # reference to Reference: identifier

        self.date = None
        # type: string

        self.amount = None
        # reference to Money

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'payee'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'amount'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'response'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'submitter'},
        ]


class PaymentReconciliation_ProcessNote(fhirbase):
    """
    This resource provides payment details and claim references supporting
    a bulk payment.

    Attributes:
        type: The note purpose: Print/Display.
        text: The note text.
    """

    __name__ = 'PaymentReconciliation_ProcessNote'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.text = None
        # type: string

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation_ProcessNote',
             'child_variable': 'type'},
        ]
