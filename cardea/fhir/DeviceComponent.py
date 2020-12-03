from .fhirbase import fhirbase


class DeviceComponent(fhirbase):
    """
    The characteristics, operational status and capabilities of a
    medical-related component of a medical device.

    Args:
        resourceType: This is a DeviceComponent resource
        identifier: The locally assigned unique identification by the
            software. For example: handle ID.
        type: The component type as defined in the object-oriented or metric
            nomenclature partition.
        lastSystemChange: The timestamp for the most recent system change
            which includes device configuration or setting change.
        source: The link to the source Device that contains administrative
            device information such as manufacture, serial number, etc.
        parent: The link to the parent resource. For example: Channel is
            linked to its VMD parent.
        operationalStatus: The current operational status of the device. For
            example: On, Off, Standby, etc.
        parameterGroup: The parameter group supported by the current device
            component that is based on some nomenclature, e.g. cardiovascular.
        measurementPrinciple: The physical principle of the measurement. For
            example: thermal, chemical, acoustical, etc.
        productionSpecification: The production specification such as
            component revision, serial number, etc.
        languageCode: The language code for the human-readable text string
            produced by the device. This language code will follow the IETF
            language tag. Example: en-US.
    """

    __name__ = 'DeviceComponent'

    def __init__(self, dict_values=None):
        self.resourceType = 'DeviceComponent'
        # type: str
        # possible values: DeviceComponent

        self.type = None
        # reference to CodeableConcept

        self.lastSystemChange = None
        # type: str

        self.source = None
        # reference to Reference: identifier

        self.parent = None
        # reference to Reference: identifier

        self.operationalStatus = None
        # type: list
        # reference to CodeableConcept

        self.parameterGroup = None
        # reference to CodeableConcept

        self.measurementPrinciple = None
        # type: str
        # possible values: other, chemical, electrical, impedance,
        # nuclear, optical, thermal, biological, mechanical, acoustical, manual

        self.productionSpecification = None
        # type: list
        # reference to DeviceComponent_ProductionSpecification

        self.languageCode = None
        # reference to CodeableConcept

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.measurementPrinciple is not None:
            for value in self.measurementPrinciple:
                if value is not None and value.lower() not in [
                    'other', 'chemical', 'electrical', 'impedance', 'nuclear', 'optical',
                        'thermal', 'biological', 'mechanical', 'acoustical', 'manual']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'other, chemical, electrical, impedance, nuclear, optical, thermal,'
                        'biological, mechanical, acoustical, manual'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'languageCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceComponent',
             'child_variable': 'source'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'operationalStatus'},

            {'parent_entity': 'DeviceComponent_ProductionSpecification',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'productionSpecification'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'parameterGroup'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceComponent',
             'child_variable': 'parent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'type'},
        ]


class DeviceComponent_ProductionSpecification(fhirbase):
    """
    The characteristics, operational status and capabilities of a
    medical-related component of a medical device.

    Args:
        specType: The specification type, such as, serial number, part number,
            hardware revision, software revision, etc.
        componentId: The internal component unique identification. This is a
            provision for manufacture specific standard components using a private
            OID. 11073-10101 has a partition for private OID semantic that the
            manufacturer can make use of.
        productionSpec: The printable string defining the component.
    """

    __name__ = 'DeviceComponent_ProductionSpecification'

    def __init__(self, dict_values=None):
        self.specType = None
        # reference to CodeableConcept

        self.componentId = None
        # reference to Identifier

        self.productionSpec = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent_ProductionSpecification',
             'child_variable': 'specType'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent_ProductionSpecification',
             'child_variable': 'componentId'},
        ]
