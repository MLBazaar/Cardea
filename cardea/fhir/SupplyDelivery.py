from .fhirbase import fhirbase


class SupplyDelivery(fhirbase):
    """Record of delivery of what is supplied.
    """

    def __init__(self, dict_values=None):
        # this is a supplydelivery resource
        self.resourceType = 'SupplyDelivery'
        # type = string
        # possible values: SupplyDelivery

        # a plan, proposal or order that is fulfilled in whole or in part by this
        # event.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # a larger event of which this particular event is a component or step.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # a code specifying the state of the dispense event.
        self.status = None
        # type = string
        # possible values: in-progress, completed, abandoned, entered-
        # in-error

        # a link to a resource representing the person whom the delivered item is
        # for.
        self.patient = None
        # reference to Reference: identifier

        # indicates the type of dispensing event that is performed. examples
        # include: trial fill, completion of trial, partial fill, emergency fill,
        # samples, etc.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the item that is being delivered or has been supplied.
        self.suppliedItem = None
        # reference to SupplyDelivery_SuppliedItem: SupplyDelivery_SuppliedItem

        # the date or time(s) the activity occurred.
        self.occurrenceDateTime = None
        # type = string

        # the date or time(s) the activity occurred.
        self.occurrencePeriod = None
        # reference to Period: Period

        # the date or time(s) the activity occurred.
        self.occurrenceTiming = None
        # reference to Timing: Timing

        # the individual responsible for dispensing the medication, supplier or
        # device.
        self.supplier = None
        # reference to Reference: identifier

        # identification of the facility/location where the supply was shipped to,
        # as part of the dispense event.
        self.destination = None
        # reference to Reference: identifier

        # identifies the person who picked up the supply.
        self.receiver = None
        # type = array
        # reference to Reference: identifier

        # identifier assigned by the dispensing facility when the item(s) is
        # dispensed.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'in-progress', 'completed', 'abandoned', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'in-progress, completed, abandoned, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'destination'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'identifier'},

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
             'child_variable': 'receiver'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery',
             'child_variable': 'occurrencePeriod'},
        ]


class SupplyDelivery_SuppliedItem(fhirbase):
    """Record of delivery of what is supplied.
    """

    def __init__(self, dict_values=None):
        # the amount of supply that has been dispensed. includes unit of measure.
        self.quantity = None
        # reference to Quantity: Quantity

        # identifies the medication, substance or device being dispensed. this is
        # either a link to a resource representing the details of the item or a
        # code that identifies the item from a known list.
        self.itemCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the medication, substance or device being dispensed. this is
        # either a link to a resource representing the details of the item or a
        # code that identifies the item from a known list.
        self.itemReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyDelivery_SuppliedItem',
             'child_variable': 'itemReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery_SuppliedItem',
             'child_variable': 'itemCodeableConcept'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyDelivery_SuppliedItem',
             'child_variable': 'quantity'},
        ]
