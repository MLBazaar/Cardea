from .fhirbase import fhirbase


class Location(fhirbase):
    """
    Details and position information for a physical place where services
    are provided  and resources and participants may be stored, found,
    contained or accommodated.

    Args:
        resourceType: This is a Location resource
        identifier: Unique code or number identifying the location to its
            users.
        status: The status property covers the general availability of the
            resource, not the current value which may be covered by the
            operationStatus, or by a schedule/slots if they are configured for the
            location.
        operationalStatus: The Operational status covers operation values most
            relevant to beds (but can also apply to rooms/units/chair/etc such as
            an isolation unit/dialisys chair). This typically covers concepts such
            as contamination, housekeeping and other activities like maintenance.
        name: Name of the location as used by humans. Does not need to be
            unique.
        alias: A list of alternate names that the location is known as, or was
            known as in the past.
        description: Description of the Location, which helps in finding or
            referencing the place.
        mode: Indicates whether a resource instance represents a specific
            location or a class of locations.
        type: Indicates the type of function performed at the location.
        telecom: The contact details of communication devices available at the
            location. This can include phone numbers, fax numbers, mobile numbers,
            email addresses and web sites.
        address: Physical location.
        physicalType: Physical form of the location, e.g. building, room,
            vehicle, road.
        position: The absolute geographic location of the Location, expressed
            using the WGS84 datum (This is the same co-ordinate system used in
            KML).
        managingOrganization: The organization responsible for the
            provisioning and upkeep of the location.
        partOf: Another Location which this Location is physically part of.
        endpoint: Technical endpoints providing access to services operated
            for the location.
    """

    __name__ = 'Location'

    def __init__(self, dict_values=None):
        self.resourceType = 'Location'
        # type: str
        # possible values: Location

        self.status = None
        # type: str
        # possible values: active, suspended, inactive

        self.operationalStatus = None
        # reference to Coding

        self.name = None
        # type: str

        self.alias = None
        # type: list

        self.description = None
        # type: str

        self.mode = None
        # type: str
        # possible values: instance, kind

        self.type = None
        # reference to CodeableConcept

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.address = None
        # reference to Address

        self.physicalType = None
        # reference to CodeableConcept

        self.position = None
        # reference to Location_Position

        self.managingOrganization = None
        # reference to Reference: identifier

        self.partOf = None
        # reference to Reference: identifier

        self.endpoint = None
        # type: list
        # reference to Reference: identifier

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
                        'active', 'suspended', 'inactive']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, suspended, inactive'))

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'instance', 'kind']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'instance, kind'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Location_Position',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'position'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Location',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Location',
             'child_variable': 'partOf'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'identifier'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'operationalStatus'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'physicalType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Location',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'address'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'telecom'},
        ]


class Location_Position(fhirbase):
    """
    Details and position information for a physical place where services
    are provided  and resources and participants may be stored, found,
    contained or accommodated.

    Args:
        longitude: Longitude. The value domain and the interpretation are the
            same as for the text of the longitude element in KML (see notes
            below).
        latitude: Latitude. The value domain and the interpretation are the
            same as for the text of the latitude element in KML (see notes below).
        altitude: Altitude. The value domain and the interpretation are the
            same as for the text of the altitude element in KML (see notes below).
    """

    __name__ = 'Location_Position'

    def __init__(self, dict_values=None):
        self.longitude = None
        # type: int

        self.latitude = None
        # type: int

        self.altitude = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
