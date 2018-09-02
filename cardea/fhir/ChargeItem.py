from .fhirbase import fhirbase


class ChargeItem(fhirbase):
    """The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """

    def __init__(self, dict_values=None):
        # this is a chargeitem resource
        self.resourceType = 'ChargeItem'
        # type = string
        # possible values: ChargeItem

        # references the source of pricing information, rules of application for
        # the code this chargeitem uses.
        self.definition = None
        # type = array

        # the current state of the chargeitem.
        self.status = None
        # type = string
        # possible values: planned, billable, not-billable, aborted,
        # billed, entered-in-error, unknown

        # chargeitems can be grouped to larger chargeitems covering the whole set.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # a code that identifies the charge, like a billing code.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the individual or set of individuals the action is being or was
        # performed on.
        self.subject = None
        # reference to Reference: identifier

        # the encounter or episode of care that establishes the context for this
        # event.
        self.context = None
        # reference to Reference: identifier

        # date/time(s) or duration when the charged service was applied.
        self.occurrenceDateTime = None
        # type = string

        # date/time(s) or duration when the charged service was applied.
        self.occurrencePeriod = None
        # reference to Period: Period

        # date/time(s) or duration when the charged service was applied.
        self.occurrenceTiming = None
        # reference to Timing: Timing

        # indicates who or what performed or participated in the charged service.
        self.participant = None
        # type = array
        # reference to ChargeItem_Participant: ChargeItem_Participant

        # the organization requesting the service.
        self.performingOrganization = None
        # reference to Reference: identifier

        # the organization performing the service.
        self.requestingOrganization = None
        # reference to Reference: identifier

        # quantity of which the charge item has been serviced.
        self.quantity = None
        # reference to Quantity: Quantity

        # the anatomical location where the related service has been applied.
        self.bodysite = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # factor overriding the factor determined by the rules associated with the
        # code.
        self.factorOverride = None
        # type = int

        # total price of the charge overriding the list price associated with the
        # code.
        self.priceOverride = None
        # reference to Money: Money

        # if the list price or the rule based factor associated with the code is
        # overridden, this attribute can capture a text to indicate the  reason
        # for this action.
        self.overrideReason = None
        # type = string

        # the device, practitioner, etc. who entered the charge item.
        self.enterer = None
        # reference to Reference: identifier

        # date the charge item was entered.
        self.enteredDate = None
        # type = string

        # describes why the event occurred in coded or textual form.
        self.reason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicated the rendered service that caused this charge.
        self.service = None
        # type = array
        # reference to Reference: identifier

        # account into which this chargeitems belongs.
        self.account = None
        # type = array
        # reference to Reference: identifier

        # comments made about the event by the performer, subject or other
        # participants.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # further information supporting the this charge.
        self.supportingInformation = None
        # type = array
        # reference to Reference: identifier

        # identifiers assigned to this event performer or other systems.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'planned', 'billable', 'not-billable', 'aborted', 'billed',
                        'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'planned, billable, not-billable, aborted, billed,'
                        'entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'performingOrganization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'enterer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'reason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'account'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'service'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'priceOverride'},

            {'parent_entity': 'ChargeItem_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'participant'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'requestingOrganization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'bodysite'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ChargeItem',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ChargeItem',
             'child_variable': 'partOf'},
        ]


class ChargeItem_Participant(fhirbase):
    """The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """

    def __init__(self, dict_values=None):
        # describes the type of performance or participation(e.g. primary surgeon,
        # anaesthesiologiest, etc.).
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the device, practitioner, etc. who performed or participated in the
        # service.
        self.actor = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
