from .fhirbase import fhirbase


class Endpoint(fhirbase):
    """
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint
    for another FHIR server. This may include any security context
    information.

    Args:
        resourceType: This is a Endpoint resource
        identifier: Identifier for the organization that is used to identify
            the endpoint across multiple disparate systems.
        status: active | suspended | error | off | test.
        connectionType: A coded value that represents the technical details of
            the usage of this endpoint, such as what WSDLs should be used in what
            way. (e.g. XDS.b/DICOM/cds-hook).
        name: A friendly name that this endpoint can be referred to with.
        managingOrganization: The organization that manages this endpoint
            (even if technically another organisation is hosting this in the
            cloud, it is the organisation associated with the data).
        contact: Contact details for a human to contact about the
            subscription. The primary use of this for system administrator
            troubleshooting.
        period: The interval during which the endpoint is expected to be
            operational.
        payloadType: The payload type describes the acceptable content that
            can be communicated on the endpoint.
        payloadMimeType: The mime type to send the payload in - e.g.
            application/fhir+xml, application/fhir+json. If the mime type is not
            specified, then the sender could send any content (including no
            content depending on the connectionType).
        address: The uri that describes the actual end-point to connect to.
        header: Additional headers / information to send as part of the
            notification.
    """

    __name__ = 'Endpoint'

    def __init__(self, dict_values=None):
        self.resourceType = 'Endpoint'
        # type: str
        # possible values: Endpoint

        self.status = None
        # type: str
        # possible values: active, suspended, error, off,
        # entered-in-error, test

        self.connectionType = None
        # reference to Coding

        self.name = None
        # type: str

        self.managingOrganization = None
        # reference to Reference: identifier

        self.contact = None
        # type: list
        # reference to ContactPoint

        self.period = None
        # reference to Period

        self.payloadType = None
        # type: list
        # reference to CodeableConcept

        self.payloadMimeType = None
        # type: list

        self.address = None
        # type: str

        self.header = None
        # type: list

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'suspended', 'error', 'off', 'entered-in-error', 'test']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, suspended, error, off, entered-in-error, test'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'period'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'identifier'},

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

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'connectionType'},
        ]
