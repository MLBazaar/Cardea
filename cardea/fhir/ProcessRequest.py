from .fhirbase import fhirbase


class ProcessRequest(fhirbase):
    """
    This resource provides the target, request and response, and action
    details for an action to be performed by the target on or about
    existing resources.

    Args:
        resourceType: This is a ProcessRequest resource
        identifier: The ProcessRequest business identifier.
        status: The status of the resource instance.
        action: The type of processing action being requested, for example
            Reversal, Readjudication, StatusRequest,PendedRequest.
        target: The organization which is the target of the request.
        created: The date when this resource was created.
        provider: The practitioner who is responsible for the action specified
            in this request.
        organization: The organization which is responsible for the action
            speccified in this request.
        request: Reference of resource which is the target or subject of this
            action.
        response: Reference of a prior response to resource which is the
            target or subject of this action.
        nullify: If true remove all history excluding audit.
        reference: A reference to supply which authenticates the process.
        item: List of top level items to be re-adjudicated, if none specified
            then the entire submission is re-adjudicated.
        include: Names of resource types to include.
        exclude: Names of resource types to exclude.
        period: A period of time during which the fulfilling resources would
            have been created.
    """

    __name__ = 'ProcessRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'ProcessRequest'
        # type: str
        # possible values: ProcessRequest

        self.status = None
        # type: str

        self.action = None
        # type: str
        # possible values: cancel, poll, reprocess, status

        self.target = None
        # reference to Reference: identifier

        self.created = None
        # type: str

        self.provider = None
        # reference to Reference: identifier

        self.organization = None
        # reference to Reference: identifier

        self.request = None
        # reference to Reference: identifier

        self.response = None
        # reference to Reference: identifier

        self.nullify = None
        # type: bool

        self.reference = None
        # type: str

        self.item = None
        # type: list
        # reference to ProcessRequest_Item

        self.include = None
        # type: list

        self.exclude = None
        # type: list

        self.period = None
        # reference to Period

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.action is not None:
            for value in self.action:
                if value is not None and value.lower() not in [
                        'cancel', 'poll', 'reprocess', 'status']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'cancel, poll, reprocess, status'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessRequest',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessRequest',
             'child_variable': 'provider'},

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
             'child_variable': 'target'},

            {'parent_entity': 'ProcessRequest_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessRequest',
             'child_variable': 'item'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessRequest',
             'child_variable': 'response'},
        ]


class ProcessRequest_Item(fhirbase):
    """
    This resource provides the target, request and response, and action
    details for an action to be performed by the target on or about
    existing resources.

    Args:
        sequenceLinkId: A service line number.
    """

    __name__ = 'ProcessRequest_Item'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
