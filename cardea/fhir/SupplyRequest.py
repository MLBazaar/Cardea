from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Timing import Timing
from .Reference import Reference
from .Period import Period

class SupplyRequest(fhirbase):
    """A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    def __init__(self, dict_values=None):
        # this is a supplyrequest resource
        self.resourceType = 'SupplyRequest'
        # type = string
        # possible values = SupplyRequest

        # status of the supply request.
        self.status = None
        # type = string
        # possible values = draft, active, suspended, cancelled, completed, entered-in-error, unknown

        # category of supply, e.g.  central, non-stock, etc. this is used to
        # support work flows associated with the supply process.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # indicates how quickly this supplyrequest should be addressed with
        # respect to other requests.
        self.priority = None
        # type = string

        # the item being requested.
        self.orderedItem = None
        # reference to SupplyRequest_OrderedItem: SupplyRequest_OrderedItem

        # when the request should be fulfilled.
        self.occurrenceDateTime = None
        # type = string

        # when the request should be fulfilled.
        self.occurrencePeriod = None
        # reference to Period: Period

        # when the request should be fulfilled.
        self.occurrenceTiming = None
        # reference to Timing: Timing

        # when the request was made.
        self.authoredOn = None
        # type = string

        # the individual who initiated the request and has responsibility for its
        # activation.
        self.requester = None
        # reference to SupplyRequest_Requester: SupplyRequest_Requester

        # who is intended to fulfill the request.
        self.supplier = None
        # type = array
        # reference to Reference: identifier

        # why the supply item was requested.
        self.reasonCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # why the supply item was requested.
        self.reasonReference = None
        # reference to Reference: identifier

        # where the supply is expected to come from.
        self.deliverFrom = None
        # reference to Reference: identifier

        # where the supply is destined to go.
        self.deliverTo = None
        # reference to Reference: identifier

        # unique identifier for this supply request.
        self.identifier = None
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'active', 'suspended', 'cancelled', 'completed', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, active, suspended, cancelled, completed, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'SupplyRequest',
            'child_variable': 'category'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'SupplyRequest',
            'child_variable': 'reasonReference'},

            {'parent_entity': 'SupplyRequest_OrderedItem',
            'parent_variable': 'object_id',
            'child_entity': 'SupplyRequest',
            'child_variable': 'orderedItem'},

            {'parent_entity': 'SupplyRequest_Requester',
            'parent_variable': 'object_id',
            'child_entity': 'SupplyRequest',
            'child_variable': 'requester'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'SupplyRequest',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'SupplyRequest',
            'child_variable': 'deliverTo'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'SupplyRequest',
            'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'SupplyRequest',
            'child_variable': 'deliverFrom'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'SupplyRequest',
            'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'SupplyRequest',
            'child_variable': 'supplier'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'SupplyRequest',
            'child_variable': 'occurrencePeriod'},
        ]

class SupplyRequest_OrderedItem(fhirbase):
    """A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    def __init__(self, dict_values=None):
        # the amount that is being ordered of the indicated item.
        self.quantity = None
        # reference to Quantity: Quantity

        # the item that is requested to be supplied. this is either a link to a
        # resource representing the details of the item or a code that identifies
        # the item from a known list.
        self.itemCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the item that is requested to be supplied. this is either a link to a
        # resource representing the details of the item or a code that identifies
        # the item from a known list.
        self.itemReference = None
        # reference to Reference: identifier


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
    """A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    def __init__(self, dict_values=None):
        # the device, practitioner, etc. who initiated the request.
        self.agent = None
        # reference to Reference: identifier

        # the organization the device or practitioner was acting on behalf of.
        self.onBehalfOf = None
        # reference to Reference: identifier


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

