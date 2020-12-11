from .fhirbase import fhirbase


class Subscription(fhirbase):
    """
    The subscription resource is used to define a push based subscription
    from a server to another system. Once a subscription is registered
    with the server, the server checks every resource that is created or
    updated, and if the resource matches the given criteria, it sends a
    message on the defined "channel" so that another system is able to
    take an appropriate action.

    Args:
        resourceType: This is a Subscription resource
        status: The status of the subscription, which marks the server state
            for managing the subscription.
        contact: Contact details for a human to contact about the
            subscription. The primary use of this for system administrator
            troubleshooting.
        end: The time for the server to turn the subscription off.
        reason: A description of why this subscription is defined.
        criteria: The rules that the server should use to determine when to
            generate notifications for this subscription.
        error: A record of the last error that occurred when the server
            processed a notification.
        channel: Details where to send notifications when resources are
            received that meet the criteria.
        tag: A tag to add to any resource that matches the criteria, after the
            subscription is processed.
    """

    __name__ = 'Subscription'

    def __init__(self, dict_values=None):
        self.resourceType = 'Subscription'
        # type: str
        # possible values: Subscription

        self.status = None
        # type: str
        # possible values: requested, active, error, off

        self.contact = None
        # type: list
        # reference to ContactPoint

        self.end = None
        # type: str

        self.reason = None
        # type: str

        self.criteria = None
        # type: str

        self.error = None
        # type: str

        self.channel = None
        # reference to Subscription_Channel

        self.tag = None
        # type: list
        # reference to Coding

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        type: The type of channel to send notifications on.
        endpoint: The uri that describes the actual end-point to send messages
            to.
        payload: The mime type to send the payload in - either
            application/fhir+xml, or application/fhir+json. If the payload is not
            present, then there is no payload in the notification, just a
            notification.
        header: Additional headers / information to send as part of the
            notification.
    """

    __name__ = 'Subscription_Channel'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: rest-hook, websocket, email, sms, message

        self.endpoint = None
        # type: str

        self.payload = None
        # type: str

        self.header = None
        # type: list

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'rest-hook', 'websocket', 'email', 'sms', 'message']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'rest-hook, websocket, email, sms, message'))
