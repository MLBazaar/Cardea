from .fhirbase import * 
from .Reference import Reference
from .Period import Period
from .Identifier import Identifier

class ProcessRequest(fhirbase):
    """This resource provides the target, request and response, and action
    details for an action to be performed by the target on or about existing
    resources.
    """

    def __init__(self, dict_values=None):
        # this is a processrequest resource
        self.resourceType = 'ProcessRequest'
        # type = string
        # possible values = ProcessRequest

        # the status of the resource instance.
        self.status = None
        # type = string

        # the type of processing action being requested, for example reversal,
        # readjudication, statusrequest,pendedrequest.
        self.action = None
        # type = string
        # possible values = cancel, poll, reprocess, status

        # the organization which is the target of the request.
        self.target = None
        # reference to Reference: identifier

        # the date when this resource was created.
        self.created = None
        # type = string

        # the practitioner who is responsible for the action specified in this
        # request.
        self.provider = None
        # reference to Reference: identifier

        # the organization which is responsible for the action speccified in this
        # request.
        self.organization = None
        # reference to Reference: identifier

        # reference of resource which is the target or subject of this action.
        self.request = None
        # reference to Reference: identifier

        # reference of a prior response to resource which is the target or subject
        # of this action.
        self.response = None
        # reference to Reference: identifier

        # if true remove all history excluding audit.
        self.nullify = None
        # type = boolean

        # a reference to supply which authenticates the process.
        self.reference = None
        # type = string

        # list of top level items to be re-adjudicated, if none specified then the
        # entire submission is re-adjudicated.
        self.item = None
        # type = array
        # reference to ProcessRequest_Item: ProcessRequest_Item

        # names of resource types to include.
        self.include = None
        # type = array

        # names of resource types to exclude.
        self.exclude = None
        # type = array

        # a period of time during which the fulfilling resources would have been
        # created.
        self.period = None
        # reference to Period: Period

        # the processrequest business identifier.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.action is not None:
            for value in self.action:
                if value != None and value.lower() not in ['cancel', 'poll', 'reprocess', 'status']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'cancel, poll, reprocess, status'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcessRequest',
            'child_variable': 'provider'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcessRequest',
            'child_variable': 'target'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcessRequest',
            'child_variable': 'request'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcessRequest',
            'child_variable': 'organization'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'ProcessRequest',
            'child_variable': 'period'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ProcessRequest',
            'child_variable': 'response'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ProcessRequest',
            'child_variable': 'identifier'},

            {'parent_entity': 'ProcessRequest_Item',
            'parent_variable': 'object_id',
            'child_entity': 'ProcessRequest',
            'child_variable': 'item'},
        ]

class ProcessRequest_Item(fhirbase):
    """This resource provides the target, request and response, and action
    details for an action to be performed by the target on or about existing
    resources.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequenceLinkId = None
        # type = int


        if dict_values:
              self.set_attributes(dict_values)


