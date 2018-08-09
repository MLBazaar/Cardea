from .fhirbase import * 
from .Coding import Coding
from .ContactPoint import ContactPoint

class Subscription(fhirbase):
    """The subscription resource is used to define a push based subscription
    from a server to another system. Once a subscription is registered with
    the server, the server checks every resource that is created or updated,
    and if the resource matches the given criteria, it sends a message on
    the defined "channel" so that another system is able to take an
    appropriate action.
    """

    def __init__(self, dict_values=None):
        # this is a subscription resource
        self.resourceType = 'Subscription'
        # type = string
        # possible values = Subscription

        # the status of the subscription, which marks the server state for
        # managing the subscription.
        self.status = None
        # type = string
        # possible values = requested, active, error, off

        # contact details for a human to contact about the subscription. the
        # primary use of this for system administrator troubleshooting.
        self.contact = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # the time for the server to turn the subscription off.
        self.end = None
        # type = string

        # a description of why this subscription is defined.
        self.reason = None
        # type = string

        # the rules that the server should use to determine when to generate
        # notifications for this subscription.
        self.criteria = None
        # type = string

        # a record of the last error that occurred when the server processed a
        # notification.
        self.error = None
        # type = string

        # details where to send notifications when resources are received that
        # meet the criteria.
        self.channel = None
        # reference to Subscription_Channel: Subscription_Channel

        # a tag to add to any resource that matches the criteria, after the
        # subscription is processed.
        self.tag = None
        # type = array
        # reference to Coding: Coding


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['requested', 'active', 'error', 'off']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'requested, active, error, off'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Subscription_Channel',
            'parent_variable': 'object_id',
            'child_entity': 'Subscription',
            'child_variable': 'channel'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Subscription',
            'child_variable': 'tag'},

            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Subscription',
            'child_variable': 'contact'},
        ]

class Subscription_Channel(fhirbase):
    """The subscription resource is used to define a push based subscription
    from a server to another system. Once a subscription is registered with
    the server, the server checks every resource that is created or updated,
    and if the resource matches the given criteria, it sends a message on
    the defined "channel" so that another system is able to take an
    appropriate action.
    """

    def __init__(self, dict_values=None):
        # the type of channel to send notifications on.
        self.type = None
        # type = string
        # possible values = rest-hook, websocket, email, sms, message

        # the uri that describes the actual end-point to send messages to.
        self.endpoint = None
        # type = string

        # the mime type to send the payload in - either application/fhir+xml, or
        # application/fhir+json. if the payload is not present, then there is no
        # payload in the notification, just a notification.
        self.payload = None
        # type = string

        # additional headers / information to send as part of the notification.
        self.header = None
        # type = array


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value != None and value.lower() not in ['rest-hook', 'websocket', 'email', 'sms', 'message']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'rest-hook, websocket, email, sms, message'))

