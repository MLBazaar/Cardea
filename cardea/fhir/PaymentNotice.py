from .fhirbase import fhirbase


class PaymentNotice(fhirbase):
    """
    This resource provides the status of the payment for goods and
    services rendered, and the request and response resource references.
    """

    __name__ = 'PaymentNotice'

    def __init__(self, dict_values=None):
        self.resourceType = 'PaymentNotice'
        """
        This is a PaymentNotice resource

        type: string
        possible values: PaymentNotice
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.request = None
        """
        Reference of resource for which payment is being made.

        reference to Reference: identifier
        """

        self.response = None
        """
        Reference of response to resource for which payment is being made.

        reference to Reference: identifier
        """

        self.statusDate = None
        """
        The date when the above payment action occurrred.

        type: string
        """

        self.created = None
        """
        The date when this resource was created.

        type: string
        """

        self.target = None
        """
        The Insurer who is target  of the request.

        reference to Reference: identifier
        """

        self.provider = None
        """
        The practitioner who is responsible for the services rendered to the
        patient.

        reference to Reference: identifier
        """

        self.organization = None
        """
        The organization which is responsible for the services rendered to the
        patient.

        reference to Reference: identifier
        """

        self.paymentStatus = None
        """
        The payment status, typically paid: payment sent, cleared: payment
        received.

        reference to CodeableConcept
        """

        self.identifier = None
        """
        The notice business identifier.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'target'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'provider'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentNotice',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'organization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentNotice',
             'child_variable': 'paymentStatus'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'response'},
        ]
