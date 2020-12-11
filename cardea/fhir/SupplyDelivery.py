from .fhirbase import fhirbase


class SupplyDelivery(fhirbase):
    """
    Record of delivery of what is supplied.

    Args:
        resourceType: This is a SupplyDelivery resource
        identifier: Identifier assigned by the dispensing facility when the
            item(s) is dispensed.
        basedOn: A plan, proposal or order that is fulfilled in whole or in
            part by this event.
        partOf: A larger event of which this particular event is a component
            or step.
        status: A code specifying the state of the dispense event.
        patient: A link to a resource representing the person whom the
            delivered item is for.
        type: Indicates the type of dispensing event that is performed.
            Examples include: Trial Fill, Completion of Trial, Partial Fill,
            Emergency Fill, Samples, etc.
        suppliedItem: The item that is being delivered or has been supplied.
        occurrenceDateTime: The date or time(s) the activity occurred.
        occurrencePeriod: The date or time(s) the activity occurred.
        occurrenceTiming: The date or time(s) the activity occurred.
        supplier: The individual responsible for dispensing the medication,
            supplier or device.
        destination: Identification of the facility/location where the Supply
            was shipped to, as part of the dispense event.
        receiver: Identifies the person who picked up the Supply.
    """

    __name__ = 'SupplyDelivery'

    def __init__(self, dict_values=None):
        self.resourceType = 'SupplyDelivery'
        # type: str
        # possible values: SupplyDelivery

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: in-progress, completed, abandoned,
        # entered-in-error

        self.patient = None
        # reference to Reference: identifier

        self.type = None
        # reference to CodeableConcept

        self.suppliedItem = None
        # reference to SupplyDelivery_SuppliedItem

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.occurrenceTiming = None
        # reference to Timing

        self.supplier = None
        # reference to Reference: identifier

        self.destination = None
        # reference to Reference: identifier

        self.receiver = None
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
                        'in-progress', 'completed', 'abandoned', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'in-progress, completed, abandoned, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'patient'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'destination'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'receiver'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'type'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'supplier'},

            {'parent_entity': 'SupplyDelivery_SuppliedItem',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'suppliedItem'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'basedOn'},
        ]


class SupplyDelivery_SuppliedItem(fhirbase):
    """
    Record of delivery of what is supplied.

    Args:
        quantity: The amount of supply that has been dispensed. Includes unit
            of measure.
        itemCodeableConcept: Identifies the medication, substance or device
            being dispensed. This is either a link to a resource representing the
            details of the item or a code that identifies the item from a known
            list.
        itemReference: Identifies the medication, substance or device being
            dispensed. This is either a link to a resource representing the
            details of the item or a code that identifies the item from a known
            list.
    """

    __name__ = 'SupplyDelivery_SuppliedItem'

    def __init__(self, dict_values=None):
        self.quantity = None
        # reference to Quantity

        self.itemCodeableConcept = None
        # reference to CodeableConcept

        self.itemReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery_SuppliedItem',
             'child_variable': 'itemReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery_SuppliedItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery_SuppliedItem',
             'child_variable': 'itemCodeableConcept'},
        ]
