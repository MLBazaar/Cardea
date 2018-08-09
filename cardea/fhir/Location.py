from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Address import Address
from .Reference import Reference
from .ContactPoint import ContactPoint
from .Coding import Coding

class Location(fhirbase):
    """Details and position information for a physical place where services are
    provided  and resources and participants may be stored, found, contained
    or accommodated.
    """

    def __init__(self, dict_values=None):
        # this is a location resource
        self.resourceType = 'Location'
        # type = string
        # possible values = Location

        # the status property covers the general availability of the resource, not
        # the current value which may be covered by the operationstatus, or by a
        # schedule/slots if they are configured for the location.
        self.status = None
        # type = string
        # possible values = active, suspended, inactive

        # the operational status covers operation values most relevant to beds
        # (but can also apply to rooms/units/chair/etc such as an isolation
        # unit/dialisys chair). this typically covers concepts such as
        # contamination, housekeeping and other activities like maintenance.
        self.operationalStatus = None
        # reference to Coding: Coding

        # name of the location as used by humans. does not need to be unique.
        self.name = None
        # type = string

        # a list of alternate names that the location is known as, or was known as
        # in the past.
        self.alias = None
        # type = array

        # description of the location, which helps in finding or referencing the
        # place.
        self.description = None
        # type = string

        # indicates whether a resource instance represents a specific location or
        # a class of locations.
        self.mode = None
        # type = string
        # possible values = instance, kind

        # indicates the type of function performed at the location.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the contact details of communication devices available at the location.
        # this can include phone numbers, fax numbers, mobile numbers, email
        # addresses and web sites.
        self.telecom = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # physical location.
        self.address = None
        # reference to Address: Address

        # physical form of the location, e.g. building, room, vehicle, road.
        self.physicalType = None
        # reference to CodeableConcept: CodeableConcept

        # the absolute geographic location of the location, expressed using the
        # wgs84 datum (this is the same co-ordinate system used in kml).
        self.position = None
        # reference to Location_Position: Location_Position

        # the organization responsible for the provisioning and upkeep of the
        # location.
        self.managingOrganization = None
        # reference to Reference: identifier

        # another location which this location is physically part of.
        self.partOf = None
        # reference to Reference: identifier

        # technical endpoints providing access to services operated for the
        # location.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # unique code or number identifying the location to its users.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['active', 'suspended', 'inactive']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'active, suspended, inactive'))

        if self.mode is not None:
            for value in self.mode:
                if value != None and value.lower() not in ['instance', 'kind']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'instance, kind'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactPoint',
            'parent_variable': 'object_id',
            'child_entity': 'Location',
            'child_variable': 'telecom'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Location',
            'child_variable': 'physicalType'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Location',
            'child_variable': 'partOf'},

            {'parent_entity': 'Address',
            'parent_variable': 'object_id',
            'child_entity': 'Location',
            'child_variable': 'address'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Location',
            'child_variable': 'operationalStatus'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Location',
            'child_variable': 'type'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Location',
            'child_variable': 'managingOrganization'},

            {'parent_entity': 'Location_Position',
            'parent_variable': 'object_id',
            'child_entity': 'Location',
            'child_variable': 'position'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Location',
            'child_variable': 'endpoint'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Location',
            'child_variable': 'identifier'},
        ]

class Location_Position(fhirbase):
    """Details and position information for a physical place where services are
    provided  and resources and participants may be stored, found, contained
    or accommodated.
    """

    def __init__(self, dict_values=None):
        # longitude. the value domain and the interpretation are the same as for
        # the text of the longitude element in kml (see notes below).
        self.longitude = None
        # type = int

        # latitude. the value domain and the interpretation are the same as for
        # the text of the latitude element in kml (see notes below).
        self.latitude = None
        # type = int

        # altitude. the value domain and the interpretation are the same as for
        # the text of the altitude element in kml (see notes below).
        self.altitude = None
        # type = int


        if dict_values:
              self.set_attributes(dict_values)


