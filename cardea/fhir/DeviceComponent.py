from .fhirbase import fhirbase


class DeviceComponent(fhirbase):
    """
    The characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """

    __name__ = 'DeviceComponent'

    def __init__(self, dict_values=None):
        self.resourceType = 'DeviceComponent'
        """
        This is a DeviceComponent resource

        type: string
        possible values: DeviceComponent
        """

        self.type = None
        """
        The component type as defined in the object-oriented or metric
        nomenclature partition.

        reference to CodeableConcept
        """

        self.lastSystemChange = None
        """
        The timestamp for the most recent system change which includes device
        configuration or setting change.

        type: string
        """

        self.source = None
        """
        The link to the source Device that contains administrative device
        information such as manufacture, serial number, etc.

        reference to Reference: identifier
        """

        self.parent = None
        """
        The link to the parent resource. For example: Channel is linked to its
        VMD parent.

        reference to Reference: identifier
        """

        self.operationalStatus = None
        """
        The current operational status of the device. For example: On, Off,
        Standby, etc.

        type: array
        reference to CodeableConcept
        """

        self.parameterGroup = None
        """
        The parameter group supported by the current device component that is
        based on some nomenclature, e.g. cardiovascular.

        reference to CodeableConcept
        """

        self.measurementPrinciple = None
        """
        The physical principle of the measurement. For example: thermal,
        chemical, acoustical, etc.

        type: string
        possible values: other, chemical, electrical, impedance,
        nuclear, optical, thermal, biological, mechanical, acoustical, manual
        """

        self.productionSpecification = None
        """
        The production specification such as component revision, serial
        number, etc.

        type: array
        reference to DeviceComponent_ProductionSpecification
        """

        self.languageCode = None
        """
        The language code for the human-readable text string produced by the
        device. This language code will follow the IETF language tag. Example:
        en-US.

        reference to CodeableConcept
        """

        self.identifier = None
        """
        The locally assigned unique identification by the software. For
        example: handle ID.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceComponent',
             'child_variable': 'operationalStatus'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceComponent',
             'child_variable': 'source'},

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
             'child_variable': 'languageCode'},
        ]


class DeviceComponent_ProductionSpecification(fhirbase):
    """
    The characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """

    __name__ = 'DeviceComponent_ProductionSpecification'

    def __init__(self, dict_values=None):
        self.specType = None
        """
        The specification type, such as, serial number, part number, hardware
        revision, software revision, etc.

        reference to CodeableConcept
        """

        self.componentId = None
        """
        The internal component unique identification. This is a provision for
        manufacture specific standard components using a private OID.
        11073-10101 has a partition for private OID semantic that the
        manufacturer can make use of.

        reference to Identifier
        """

        self.productionSpec = None
        """
        The printable string defining the component.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

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
