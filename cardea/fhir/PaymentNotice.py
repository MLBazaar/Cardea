from .fhirbase import fhirbase


class PaymentNotice(fhirbase):
    """
    This resource provides the status of the payment for goods and
    services rendered, and the request and response resource references.

    Args:
        resourceType: This is a PaymentNotice resource
        identifier: The notice business identifier.
        status: The status of the resource instance.
        request: Reference of resource for which payment is being made.
        response: Reference of response to resource for which payment is being
            made.
        statusDate: The date when the above payment action occurrred.
        created: The date when this resource was created.
        target: The Insurer who is target  of the request.
        provider: The practitioner who is responsible for the services
            rendered to the patient.
        organization: The organization which is responsible for the services
            rendered to the patient.
        paymentStatus: The payment status, typically paid: payment sent,
            cleared: payment received.
    """

    __name__ = 'PaymentNotice'

    def __init__(self, dict_values=None):
        self.resourceType = 'PaymentNotice'
        # type: str
        # possible values: PaymentNotice

        self.status = None
        # type: str

        self.request = None
        # reference to Reference: identifier

        self.response = None
        # reference to Reference: identifier

        self.statusDate = None
        # type: str

        self.created = None
        # type: str

        self.target = None
        # reference to Reference: identifier

        self.provider = None
        # reference to Reference: identifier

        self.organization = None
        # reference to Reference: identifier

        self.paymentStatus = None
        # reference to CodeableConcept

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentNotice',
             'child_variable': 'paymentStatus'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'target'},

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
             'child_variable': 'response'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'organization'},
        ]
