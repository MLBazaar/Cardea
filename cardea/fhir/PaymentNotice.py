from .fhirbase import fhirbase


class PaymentNotice(fhirbase):
    """This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    def __init__(self, dict_values=None):
        # this is a paymentnotice resource
        self.resourceType = 'PaymentNotice'
        # type = string
        # possible values: PaymentNotice

        # the status of the resource instance.
        self.status = None
        # type = string

        # reference of resource for which payment is being made.
        self.request = None
        # reference to Reference: identifier

        # reference of response to resource for which payment is being made.
        self.response = None
        # reference to Reference: identifier

        # the date when the above payment action occurrred.
        self.statusDate = None
        # type = string

        # the date when this resource was created.
        self.created = None
        # type = string

        # the insurer who is target  of the request.
        self.target = None
        # reference to Reference: identifier

        # the practitioner who is responsible for the services rendered to the
        # patient.
        self.provider = None
        # reference to Reference: identifier

        # the organization which is responsible for the services rendered to the
        # patient.
        self.organization = None
        # reference to Reference: identifier

        # the payment status, typically paid: payment sent, cleared: payment
        # received.
        self.paymentStatus = None
        # reference to CodeableConcept: CodeableConcept

        # the notice business identifier.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'response'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'target'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentNotice',
             'child_variable': 'paymentStatus'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'PaymentNotice',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'PaymentNotice',
             'child_variable': 'provider'},
        ]
