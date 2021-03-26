from .fhirbase import fhirbase


class ChargeItem(fhirbase):
    """
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like
    date, time, amounts and participating organizations and persons. Main
    Usage of the ChargeItem is to enable the billing process and internal
    cost allocation.

    Args:
        resourceType: This is a ChargeItem resource
        identifier: Identifiers assigned to this event performer or other
            systems.
        definition: References the source of pricing information, rules of
            application for the code this ChargeItem uses.
        status: The current state of the ChargeItem.
        partOf: ChargeItems can be grouped to larger ChargeItems covering the
            whole set.
        code: A code that identifies the charge, like a billing code.
        subject: The individual or set of individuals the action is being or
            was performed on.
        context: The encounter or episode of care that establishes the context
            for this event.
        occurrenceDateTime: Date/time(s) or duration when the charged service
            was applied.
        occurrencePeriod: Date/time(s) or duration when the charged service
            was applied.
        occurrenceTiming: Date/time(s) or duration when the charged service
            was applied.
        participant: Indicates who or what performed or participated in the
            charged service.
        performingOrganization: The organization requesting the service.
        requestingOrganization: The organization performing the service.
        quantity: Quantity of which the charge item has been serviced.
        bodysite: The anatomical location where the related service has been
            applied.
        factorOverride: Factor overriding the factor determined by the rules
            associated with the code.
        priceOverride: Total price of the charge overriding the list price
            associated with the code.
        overrideReason: If the list price or the rule based factor associated
            with the code is overridden, this attribute can capture a text to
            indicate the  reason for this action.
        enterer: The device, practitioner, etc. who entered the charge item.
        enteredDate: Date the charge item was entered.
        reason: Describes why the event occurred in coded or textual form.
        service: Indicated the rendered service that caused this charge.
        account: Account into which this ChargeItems belongs.
        note: Comments made about the event by the performer, subject or other
            participants.
        supportingInformation: Further information supporting the this charge.
    """

    __name__ = 'ChargeItem'

    def __init__(self, dict_values=None):
        self.resourceType = 'ChargeItem'
        # type: str
        # possible values: ChargeItem

        self.definition = None
        # type: list

        self.status = None
        # type: str
        # possible values: planned, billable, not-billable, aborted,
        # billed, entered-in-error, unknown

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.code = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.occurrenceTiming = None
        # reference to Timing

        self.participant = None
        # type: list
        # reference to ChargeItem_Participant

        self.performingOrganization = None
        # reference to Reference: identifier

        self.requestingOrganization = None
        # reference to Reference: identifier

        self.quantity = None
        # reference to Quantity

        self.bodysite = None
        # type: list
        # reference to CodeableConcept

        self.factorOverride = None
        # type: int

        self.priceOverride = None
        # reference to Money

        self.overrideReason = None
        # type: str

        self.enterer = None
        # reference to Reference: identifier

        self.enteredDate = None
        # type: str

        self.reason = None
        # type: list
        # reference to CodeableConcept

        self.service = None
        # type: list
        # reference to Reference: identifier

        self.account = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.supportingInformation = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'planned', 'billable', 'not-billable', 'aborted', 'billed',
                        'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, billable, not-billable, aborted, billed, '
                        'entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'bodysite'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'account'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'service'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'note'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'priceOverride'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'requestingOrganization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'reason'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'ChargeItem_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'performingOrganization'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'occurrenceTiming'},
        ]


class ChargeItem_Participant(fhirbase):
    """
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like
    date, time, amounts and participating organizations and persons. Main
    Usage of the ChargeItem is to enable the billing process and internal
    cost allocation.

    Args:
        role: Describes the type of performance or participation(e.g. primary
            surgeon, anaesthesiologiest, etc.).
        actor: The device, practitioner, etc. who performed or participated in
            the service.
    """

    __name__ = 'ChargeItem_Participant'

    def __init__(self, dict_values=None):
        self.role = None
        # reference to CodeableConcept

        self.actor = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem_Participant',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem_Participant',
             'child_variable': 'role'},
        ]
