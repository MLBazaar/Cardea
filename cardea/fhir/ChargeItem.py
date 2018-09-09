from .fhirbase import fhirbase


class ChargeItem(fhirbase):
    """
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like
    date, time, amounts and participating organizations and persons. Main
    Usage of the ChargeItem is to enable the billing process and internal
    cost allocation.
    """

    __name__ = 'ChargeItem'

    def __init__(self, dict_values=None):
        self.resourceType = 'ChargeItem'
        """
        This is a ChargeItem resource

        type: string
        possible values: ChargeItem
        """

        self.definition = None
        """
        References the source of pricing information, rules of application for
        the code this ChargeItem uses.

        type: array
        """

        self.status = None
        """
        The current state of the ChargeItem.

        type: string
        possible values: planned, billable, not-billable, aborted,
        billed, entered-in-error, unknown
        """

        self.partOf = None
        """
        ChargeItems can be grouped to larger ChargeItems covering the whole
        set.

        type: array
        reference to Reference: identifier
        """

        self.code = None
        """
        A code that identifies the charge, like a billing code.

        reference to CodeableConcept
        """

        self.subject = None
        """
        The individual or set of individuals the action is being or was
        performed on.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter or episode of care that establishes the context for this
        event.

        reference to Reference: identifier
        """

        self.occurrenceDateTime = None
        """
        Date/time(s) or duration when the charged service was applied.

        type: string
        """

        self.occurrencePeriod = None
        """
        Date/time(s) or duration when the charged service was applied.

        reference to Period
        """

        self.occurrenceTiming = None
        """
        Date/time(s) or duration when the charged service was applied.

        reference to Timing
        """

        self.participant = None
        """
        Indicates who or what performed or participated in the charged
        service.

        type: array
        reference to ChargeItem_Participant
        """

        self.performingOrganization = None
        """
        The organization requesting the service.

        reference to Reference: identifier
        """

        self.requestingOrganization = None
        """
        The organization performing the service.

        reference to Reference: identifier
        """

        self.quantity = None
        """
        Quantity of which the charge item has been serviced.

        reference to Quantity
        """

        self.bodysite = None
        """
        The anatomical location where the related service has been applied.

        type: array
        reference to CodeableConcept
        """

        self.factorOverride = None
        """
        Factor overriding the factor determined by the rules associated with
        the code.

        type: int
        """

        self.priceOverride = None
        """
        Total price of the charge overriding the list price associated with
        the code.

        reference to Money
        """

        self.overrideReason = None
        """
        If the list price or the rule based factor associated with the code is
        overridden, this attribute can capture a text to indicate the  reason
        for this action.

        type: string
        """

        self.enterer = None
        """
        The device, practitioner, etc. who entered the charge item.

        reference to Reference: identifier
        """

        self.enteredDate = None
        """
        Date the charge item was entered.

        type: string
        """

        self.reason = None
        """
        Describes why the event occurred in coded or textual form.

        type: array
        reference to CodeableConcept
        """

        self.service = None
        """
        Indicated the rendered service that caused this charge.

        type: array
        reference to Reference: identifier
        """

        self.account = None
        """
        Account into which this ChargeItems belongs.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Comments made about the event by the performer, subject or other
        participants.

        type: array
        reference to Annotation
        """

        self.supportingInformation = None
        """
        Further information supporting the this charge.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifiers assigned to this event performer or other systems.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'requestingOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'performingOrganization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'bodysite'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'priceOverride'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'partOf'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'service'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'ChargeItem_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'account'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'reason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'code'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'note'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'occurrenceTiming'},

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
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'context'},
        ]


class ChargeItem_Participant(fhirbase):
    """
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like
    date, time, amounts and participating organizations and persons. Main
    Usage of the ChargeItem is to enable the billing process and internal
    cost allocation.
    """

    __name__ = 'ChargeItem_Participant'

    def __init__(self, dict_values=None):
        self.role = None
        """
        Describes the type of performance or participation(e.g. primary
        surgeon, anaesthesiologiest, etc.).

        reference to CodeableConcept
        """

        self.actor = None
        """
        The device, practitioner, etc. who performed or participated in the
        service.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem_Participant',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem_Participant',
             'child_variable': 'actor'},
        ]
