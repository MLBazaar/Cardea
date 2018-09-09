from .fhirbase import fhirbase


class Endpoint(fhirbase):
    """
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint
    for another FHIR server. This may include any security context
    information.
    """

    __name__ = 'Endpoint'

    def __init__(self, dict_values=None):
        self.resourceType = 'Endpoint'
        """
        This is a Endpoint resource

        type: string
        possible values: Endpoint
        """

        self.status = None
        """
        active | suspended | error | off | test.

        type: string
        possible values: active, suspended, error, off,
        entered-in-error, test
        """

        self.connectionType = None
        """
        A coded value that represents the technical details of the usage of
        this endpoint, such as what WSDLs should be used in what way. (e.g.
        XDS.b/DICOM/cds-hook).

        reference to Coding
        """

        self.name = None
        """
        A friendly name that this endpoint can be referred to with.

        type: string
        """

        self.managingOrganization = None
        """
        The organization that manages this endpoint (even if technically
        another organisation is hosting this in the cloud, it is the
        organisation associated with the data).

        reference to Reference: identifier
        """

        self.contact = None
        """
        Contact details for a human to contact about the subscription. The
        primary use of this for system administrator troubleshooting.

        type: array
        reference to ContactPoint
        """

        self.period = None
        """
        The interval during which the endpoint is expected to be operational.

        reference to Period
        """

        self.payloadType = None
        """
        The payload type describes the acceptable content that can be
        communicated on the endpoint.

        type: array
        reference to CodeableConcept
        """

        self.payloadMimeType = None
        """
        The mime type to send the payload in - e.g. application/fhir+xml,
        application/fhir+json. If the mime type is not specified, then the
        sender could send any content (including no content depending on the
        connectionType).

        type: array
        """

        self.address = None
        """
        The uri that describes the actual end-point to connect to.

        type: string
        """

        self.header = None
        """
        Additional headers / information to send as part of the notification.

        type: array
        """

        self.identifier = None
        """
        Identifier for the organization that is used to identify the endpoint
        across multiple disparate systems.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'suspended', 'error', 'off', 'entered-in-error', 'test']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, suspended, error, off, entered-in-error, test'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'payloadType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Endpoint',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'identifier'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'connectionType'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'period'},
        ]
