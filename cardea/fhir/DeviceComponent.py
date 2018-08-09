from .fhirbase import * 
from .Reference import Reference
from .Identifier import Identifier
from .CodeableConcept import CodeableConcept

class DeviceComponent(fhirbase):
    """The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    def __init__(self, dict_values=None):
        # this is a devicecomponent resource
        self.resourceType = 'DeviceComponent'
        # type = string
        # possible values = DeviceComponent

        # the component type as defined in the object-oriented or metric
        # nomenclature partition.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the timestamp for the most recent system change which includes device
        # configuration or setting change.
        self.lastSystemChange = None
        # type = string

        # the link to the source device that contains administrative device
        # information such as manufacture, serial number, etc.
        self.source = None
        # reference to Reference: identifier

        # the link to the parent resource. for example: channel is linked to its
        # vmd parent.
        self.parent = None
        # reference to Reference: identifier

        # the current operational status of the device. for example: on, off,
        # standby, etc.
        self.operationalStatus = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the parameter group supported by the current device component that is
        # based on some nomenclature, e.g. cardiovascular.
        self.parameterGroup = None
        # reference to CodeableConcept: CodeableConcept

        # the physical principle of the measurement. for example: thermal,
        # chemical, acoustical, etc.
        self.measurementPrinciple = None
        # type = string
        # possible values = other, chemical, electrical, impedance, nuclear, optical, thermal, biological, mechanical, acoustical, manual

        # the production specification such as component revision, serial number,
        # etc.
        self.productionSpecification = None
        # type = array
        # reference to DeviceComponent_ProductionSpecification: DeviceComponent_ProductionSpecification

        # the language code for the human-readable text string produced by the
        # device. this language code will follow the ietf language tag. example:
        # en-us.
        self.languageCode = None
        # reference to CodeableConcept: CodeableConcept

        # the locally assigned unique identification by the software. for example:
        # handle id.
        self.identifier = None
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.measurementPrinciple is not None:
            for value in self.measurementPrinciple:
                if value != None and value.lower() not in ['other', 'chemical', 'electrical', 'impedance', 'nuclear', 'optical', 'thermal', 'biological', 'mechanical', 'acoustical', 'manual']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'other, chemical, electrical, impedance, nuclear, optical, thermal, biological, mechanical, acoustical, manual'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceComponent',
            'child_variable': 'parent'},

            {'parent_entity': 'DeviceComponent_ProductionSpecification',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent',
            'child_variable': 'productionSpecification'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent',
            'child_variable': 'languageCode'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent',
            'child_variable': 'parameterGroup'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent',
            'child_variable': 'type'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceComponent',
            'child_variable': 'source'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent',
            'child_variable': 'operationalStatus'},
        ]

class DeviceComponent_ProductionSpecification(fhirbase):
    """The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """

    def __init__(self, dict_values=None):
        # the specification type, such as, serial number, part number, hardware
        # revision, software revision, etc.
        self.specType = None
        # reference to CodeableConcept: CodeableConcept

        # the internal component unique identification. this is a provision for
        # manufacture specific standard components using a private oid.
        # 11073-10101 has a partition for private oid semantic that the
        # manufacturer can make use of.
        self.componentId = None
        # reference to Identifier: Identifier

        # the printable string defining the component.
        self.productionSpec = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent_ProductionSpecification',
            'child_variable': 'componentId'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceComponent_ProductionSpecification',
            'child_variable': 'specType'},
        ]

