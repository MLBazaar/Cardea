from .fhirbase import fhirbase


class PaymentReconciliation(fhirbase):
    """
    This resource provides payment details and claim references supporting
    a bulk payment.
    """

    __name__ = 'PaymentReconciliation'

    def __init__(self, dict_values=None):
        self.resourceType = 'PaymentReconciliation'
        """
        This is a PaymentReconciliation resource

        type: string
        possible values: PaymentReconciliation
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.period = None
        """
        The period of time for which payments have been gathered into this
        bulk payment for settlement.

        reference to Period
        """

        self.created = None
        """
        The date when the enclosed suite of services were performed or
        completed.

        type: string
        """

        self.organization = None
        """
        The Insurer who produced this adjudicated response.

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

        self.detail = None
        """
        List of individual settlement amounts and the corresponding
        transaction.

        type: array
        reference to PaymentReconciliation_Detail
        """

        self.form = None
        """
        The form to be used for printing the content.

        reference to CodeableConcept
        """

        self.total = None
        """
        Total payment amount.

        reference to Money
        """

        self.processNote = None
        """
        Suite of notes.

        type: array
        reference to PaymentReconciliation_ProcessNote
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
            {'parent_entity': 'PaymentReconciliation_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'detail'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'requestProvider'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'organization'},

            {'parent_entity': 'PaymentReconciliation_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'processNote'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'request'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'outcome'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'total'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'requestOrganization'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation',
             'child_variable': 'period'},
        ]


class PaymentReconciliation_Detail(fhirbase):
    """
    This resource provides payment details and claim references supporting
    a bulk payment.
    """

    __name__ = 'PaymentReconciliation_Detail'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Code to indicate the nature of the payment, adjustment, funds advance,
        etc.

        reference to CodeableConcept
        """

        self.request = None
        """
        The claim or financial resource.

        reference to Reference: identifier
        """

        self.response = None
        """
        The claim response resource.

        reference to Reference: identifier
        """

        self.submitter = None
        """
        The Organization which submitted the claim or financial transaction.

        reference to Reference: identifier
        """

        self.payee = None
        """
        The organization which is receiving the payment.

        reference to Reference: identifier
        """

        self.date = None
        """
        The date of the invoice or financial resource.

        type: string
        """

        self.amount = None
        """
        Amount paid for this detail.

        reference to Money
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'payee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'type'},

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
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentReconciliation_Detail',
             'child_variable': 'submitter'},
        ]


class PaymentReconciliation_ProcessNote(fhirbase):
    """
    This resource provides payment details and claim references supporting
    a bulk payment.
    """

    __name__ = 'PaymentReconciliation_ProcessNote'

    def __init__(self, dict_values=None):
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
