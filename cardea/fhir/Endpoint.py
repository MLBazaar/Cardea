from .fhirbase import fhirbase


class Endpoint(fhirbase):
    """The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint
    for another FHIR server. This may include any security context
    information.
    """

    def __init__(self, dict_values=None):
        # this is a endpoint resource
        self.resourceType = 'Endpoint'
        # type = string
        # possible values: Endpoint

        # active | suspended | error | off | test.
        self.status = None
        # type = string
        # possible values: active, suspended, error, off, entered-in-
        # error, test

        # a coded value that represents the technical details of the usage of this
        # endpoint, such as what wsdls should be used in what way. (e.g.
        # xds.b/dicom/cds-hook).
        self.connectionType = None
        # reference to Coding: Coding

        # a friendly name that this endpoint can be referred to with.
        self.name = None
        # type = string

        # the organization that manages this endpoint (even if technically another
        # organisation is hosting this in the cloud, it is the organisation
        # associated with the data).
        self.managingOrganization = None
        # reference to Reference: identifier

        # contact details for a human to contact about the subscription. the
        # primary use of this for system administrator troubleshooting.
        self.contact = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # the interval during which the endpoint is expected to be operational.
        self.period = None
        # reference to Period: Period

        # the payload type describes the acceptable content that can be
        # communicated on the endpoint.
        self.payloadType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the mime type to send the payload in - e.g. application/fhir+xml,
        # application/fhir+json. if the mime type is not specified, then the
        # sender could send any content (including no content depending on the
        # connectiontype).
        self.payloadMimeType = None
        # type = array

        # the uri that describes the actual end-point to connect to.
        self.address = None
        # type = string

        # additional headers / information to send as part of the notification.
        self.header = None
        # type = array

        # identifier for the organization that is used to identify the endpoint
        # across multiple disparate systems.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Endpoint',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'identifier'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'contact'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'period'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'connectionType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Endpoint',
             'child_variable': 'payloadType'},
        ]
