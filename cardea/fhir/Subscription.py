from .fhirbase import fhirbase


class Subscription(fhirbase):
    """
    The subscription resource is used to define a push based subscription
    from a server to another system. Once a subscription is registered
    with the server, the server checks every resource that is created or
    updated, and if the resource matches the given criteria, it sends a
    message on the defined "channel" so that another system is able to
    take an appropriate action.
    """

    __name__ = 'Subscription'

    def __init__(self, dict_values=None):
        self.resourceType = 'Subscription'
        """
        This is a Subscription resource

        type: string
        possible values: Subscription
        """

        self.status = None
        """
        The status of the subscription, which marks the server state for
        managing the subscription.

        type: string
        possible values: requested, active, error, off
        """

        self.contact = None
        """
        Contact details for a human to contact about the subscription. The
        primary use of this for system administrator troubleshooting.

        type: array
        reference to ContactPoint
        """

        self.end = None
        """
        The time for the server to turn the subscription off.

        type: string
        """

        self.reason = None
        """
        A description of why this subscription is defined.

        type: string
        """

        self.criteria = None
        """
        The rules that the server should use to determine when to generate
        notifications for this subscription.

        type: string
        """

        self.error = None
        """
        A record of the last error that occurred when the server processed a
        notification.

        type: string
        """

        self.channel = None
        """
        Details where to send notifications when resources are received that
        meet the criteria.

        reference to Subscription_Channel
        """

        self.tag = None
        """
        A tag to add to any resource that matches the criteria, after the
        subscription is processed.

        type: array
        reference to Coding
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'requested', 'active', 'error', 'off']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'requested, active, error, off'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Subscription',
             'child_variable': 'contact'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Subscription',
             'child_variable': 'tag'},

            {'parent_entity': 'Subscription_Channel',
             'parent_variable': 'object_id',
             'child_entity': 'Subscription',
             'child_variable': 'channel'},
        ]


class Subscription_Channel(fhirbase):
    """
    The subscription resource is used to define a push based subscription
    from a server to another system. Once a subscription is registered
    with the server, the server checks every resource that is created or
    updated, and if the resource matches the given criteria, it sends a
    message on the defined "channel" so that another system is able to
    take an appropriate action.
    """

    __name__ = 'Subscription_Channel'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The type of channel to send notifications on.

        type: string
        possible values: rest-hook, websocket, email, sms, message
        """

        self.endpoint = None
        """
        The uri that describes the actual end-point to send messages to.

        type: string
        """

        self.payload = None
        """
        The mime type to send the payload in - either application/fhir+xml, or
        application/fhir+json. If the payload is not present, then there is no
        payload in the notification, just a notification.

        type: string
        """

        self.header = None
        """
        Additional headers / information to send as part of the notification.

        type: array
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'rest-hook', 'websocket', 'email', 'sms', 'message']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'rest-hook, websocket, email, sms, message'))
