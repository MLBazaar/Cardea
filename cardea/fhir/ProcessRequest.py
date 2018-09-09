from .fhirbase import fhirbase


class ProcessRequest(fhirbase):
    """
    This resource provides the target, request and response, and action
    details for an action to be performed by the target on or about
    existing resources.
    """

    __name__ = 'ProcessRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'ProcessRequest'
        """
        This is a ProcessRequest resource

        type: string
        possible values: ProcessRequest
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.action = None
        """
        The type of processing action being requested, for example Reversal,
        Readjudication, StatusRequest,PendedRequest.

        type: string
        possible values: cancel, poll, reprocess, status
        """

        self.target = None
        """
        The organization which is the target of the request.

        reference to Reference: identifier
        """

        self.created = None
        """
        The date when this resource was created.

        type: string
        """

        self.provider = None
        """
        The practitioner who is responsible for the action specified in this
        request.

        reference to Reference: identifier
        """

        self.organization = None
        """
        The organization which is responsible for the action speccified in
        this request.

        reference to Reference: identifier
        """

        self.request = None
        """
        Reference of resource which is the target or subject of this action.

        reference to Reference: identifier
        """

        self.response = None
        """
        Reference of a prior response to resource which is the target or
        subject of this action.

        reference to Reference: identifier
        """

        self.nullify = None
        """
        If true remove all history excluding audit.

        type: boolean
        """

        self.reference = None
        """
        A reference to supply which authenticates the process.

        type: string
        """

        self.item = None
        """
        List of top level items to be re-adjudicated, if none specified then
        the entire submission is re-adjudicated.

        type: array
        reference to ProcessRequest_Item
        """

        self.include = None
        """
        Names of resource types to include.

        type: array
        """

        self.exclude = None
        """
        Names of resource types to exclude.

        type: array
        """

        self.period = None
        """
        A period of time during which the fulfilling resources would have been
        created.

        reference to Period
        """

        self.identifier = None
        """
        The ProcessRequest business identifier.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.action is not None:
            for value in self.action:
                if value is not None and value.lower() not in [
                        'cancel', 'poll', 'reprocess', 'status']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'cancel, poll, reprocess, status'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ProcessRequest_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessRequest',
             'child_variable': 'item'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessRequest',
             'child_variable': 'target'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessRequest',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcessRequest',
             'child_variable': 'response'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ProcessRequest',
             'child_variable': 'period'},

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
        ]


class ProcessRequest_Item(fhirbase):
    """
    This resource provides the target, request and response, and action
    details for an action to be performed by the target on or about
    existing resources.
    """

    __name__ = 'ProcessRequest_Item'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        """
        A service line number.

        type: int
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
