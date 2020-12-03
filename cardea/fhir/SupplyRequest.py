from .fhirbase import fhirbase


class SupplyRequest(fhirbase):
    """
    A record of a request for a medication, substance or device used in
    the healthcare setting.

    Args:
        resourceType: This is a SupplyRequest resource
        identifier: Unique identifier for this supply request.
        status: Status of the supply request.
        category: Category of supply, e.g.  central, non-stock, etc. This is
            used to support work flows associated with the supply process.
        priority: Indicates how quickly this SupplyRequest should be addressed
            with respect to other requests.
        orderedItem: The item being requested.
        occurrenceDateTime: When the request should be fulfilled.
        occurrencePeriod: When the request should be fulfilled.
        occurrenceTiming: When the request should be fulfilled.
        authoredOn: When the request was made.
        requester: The individual who initiated the request and has
            responsibility for its activation.
        supplier: Who is intended to fulfill the request.
        reasonCodeableConcept: Why the supply item was requested.
        reasonReference: Why the supply item was requested.
        deliverFrom: Where the supply is expected to come from.
        deliverTo: Where the supply is destined to go.
    """

    __name__ = 'SupplyRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'SupplyRequest'
        # type: str
        # possible values: SupplyRequest

        self.status = None
        # type: str
        # possible values: draft, active, suspended, cancelled,
        # completed, entered-in-error, unknown

        self.category = None
        # reference to CodeableConcept

        self.priority = None
        # type: str

        self.orderedItem = None
        # reference to SupplyRequest_OrderedItem

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.occurrenceTiming = None
        # reference to Timing

        self.authoredOn = None
        # type: str

        self.requester = None
        # reference to SupplyRequest_Requester

        self.supplier = None
        # type: list
        # reference to Reference: identifier

        self.reasonCodeableConcept = None
        # reference to CodeableConcept

        self.reasonReference = None
        # reference to Reference: identifier

        self.deliverFrom = None
        # reference to Reference: identifier

        self.deliverTo = None
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
                    'draft', 'active', 'suspended', 'cancelled', 'completed',
                        'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, suspended, cancelled, completed, entered-in-error,'
                        'unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'deliverFrom'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'deliverTo'},

            {'parent_entity': 'SupplyRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'SupplyRequest_OrderedItem',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'orderedItem'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'supplier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest',
             'child_variable': 'reasonReference'},
        ]


class SupplyRequest_OrderedItem(fhirbase):
    """
    A record of a request for a medication, substance or device used in
    the healthcare setting.

    Args:
        quantity: The amount that is being ordered of the indicated item.
        itemCodeableConcept: The item that is requested to be supplied. This
            is either a link to a resource representing the details of the item or
            a code that identifies the item from a known list.
        itemReference: The item that is requested to be supplied. This is
            either a link to a resource representing the details of the item or a
            code that identifies the item from a known list.
    """

    __name__ = 'SupplyRequest_OrderedItem'

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
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest_OrderedItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'SupplyRequest_OrderedItem',
             'child_variable': 'itemCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest_OrderedItem',
             'child_variable': 'itemReference'},
        ]


class SupplyRequest_Requester(fhirbase):
    """
    A record of a request for a medication, substance or device used in
    the healthcare setting.

    Args:
        agent: The device, practitioner, etc. who initiated the request.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'SupplyRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        # reference to Reference: identifier

        self.onBehalfOf = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest_Requester',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'SupplyRequest_Requester',
             'child_variable': 'onBehalfOf'},
        ]
