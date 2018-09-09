from .fhirbase import fhirbase


class Location(fhirbase):
    """
    Details and position information for a physical place where services
    are provided  and resources and participants may be stored, found,
    contained or accommodated.
    """

    __name__ = 'Location'

    def __init__(self, dict_values=None):
        self.resourceType = 'Location'
        """
        This is a Location resource

        type: string
        possible values: Location
        """

        self.status = None
        """
        The status property covers the general availability of the resource,
        not the current value which may be covered by the operationStatus, or
        by a schedule/slots if they are configured for the location.

        type: string
        possible values: active, suspended, inactive
        """

        self.operationalStatus = None
        """
        The Operational status covers operation values most relevant to beds
        (but can also apply to rooms/units/chair/etc such as an isolation
        unit/dialisys chair). This typically covers concepts such as
        contamination, housekeeping and other activities like maintenance.

        reference to Coding
        """

        self.name = None
        """
        Name of the location as used by humans. Does not need to be unique.

        type: string
        """

        self.alias = None
        """
        A list of alternate names that the location is known as, or was known
        as in the past.

        type: array
        """

        self.description = None
        """
        Description of the Location, which helps in finding or referencing the
        place.

        type: string
        """

        self.mode = None
        """
        Indicates whether a resource instance represents a specific location
        or a class of locations.

        type: string
        possible values: instance, kind
        """

        self.type = None
        """
        Indicates the type of function performed at the location.

        reference to CodeableConcept
        """

        self.telecom = None
        """
        The contact details of communication devices available at the
        location. This can include phone numbers, fax numbers, mobile numbers,
        email addresses and web sites.

        type: array
        reference to ContactPoint
        """

        self.address = None
        """
        Physical location.

        reference to Address
        """

        self.physicalType = None
        """
        Physical form of the location, e.g. building, room, vehicle, road.

        reference to CodeableConcept
        """

        self.position = None
        """
        The absolute geographic location of the Location, expressed using the
        WGS84 datum (This is the same co-ordinate system used in KML).

        reference to Location_Position
        """

        self.managingOrganization = None
        """
        The organization responsible for the provisioning and upkeep of the
        location.

        reference to Reference: identifier
        """

        self.partOf = None
        """
        Another Location which this Location is physically part of.

        reference to Reference: identifier
        """

        self.endpoint = None
        """
        Technical endpoints providing access to services operated for the
        location.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Unique code or number identifying the location to its users.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Location',
             'child_variable': 'partOf'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'identifier'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'address'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Location',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'telecom'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Location',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'operationalStatus'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'physicalType'},

            {'parent_entity': 'Location_Position',
             'parent_variable': 'object_id',
             'child_entity': 'Location',
             'child_variable': 'position'},
        ]


class Location_Position(fhirbase):
    """
    Details and position information for a physical place where services
    are provided  and resources and participants may be stored, found,
    contained or accommodated.
    """

    __name__ = 'Location_Position'

    def __init__(self, dict_values=None):
        self.longitude = None
        """
        Longitude. The value domain and the interpretation are the same as for
        the text of the longitude element in KML (see notes below).

        type: int
        """

        self.latitude = None
        """
        Latitude. The value domain and the interpretation are the same as for
        the text of the latitude element in KML (see notes below).

        type: int
        """

        self.altitude = None
        """
        Altitude. The value domain and the interpretation are the same as for
        the text of the altitude element in KML (see notes below).

        type: int
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
