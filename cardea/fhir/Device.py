from .fhirbase import fhirbase


class Device(fhirbase):
    """
    This resource identifies an instance or a type of a manufactured item
    that is used in the provision of healthcare without being
    substantially changed through that activity. The device may be a
    medical or non-medical device.  Medical devices include durable
    (reusable) medical equipment, implantable devices, as well as
    disposable equipment used for diagnostic, treatment, and research for
    healthcare and public health.  Non-medical devices may include items
    such as a machine, cellphone, computer, application, etc.

    Args:
        resourceType: This is a Device resource
        identifier: Unique instance identifiers assigned to a device by
            manufacturers other organizations or owners.
        udi: [Unique device identifier (UDI)](device.html#5.11.3.2.2) assigned
            to device label or package.
        status: Status of the Device availability.
        type: Code or identifier to identify a kind of device.
        lotNumber: Lot number assigned by the manufacturer.
        manufacturer: A name of the manufacturer.
        manufactureDate: The date and time when the device was manufactured.
        expirationDate: The date and time beyond which this device is no
            longer valid or should not be used (if applicable).
        model: The "model" is an identifier assigned by the manufacturer to
            identify the product by its type. This number is shared by the all
            devices sold as the same type.
        version: The version of the device, if the device has multiple
            releases under the same model, or if the device is software or carries
            firmware.
        patient: Patient information, If the device is affixed to a person.
        owner: An organization that is responsible for the provision and
            ongoing maintenance of the device.
        contact: Contact details for an organization or a particular human
            that is responsible for the device.
        location: The place where the device can be found.
        url: A network address on which the device may be contacted directly.
        note: Descriptive information, usage information or implantation
            information that is not captured in an existing element.
        safety: Provides additional safety characteristics about a medical
            device.  For example devices containing latex.
    """

    __name__ = 'Device'

    def __init__(self, dict_values=None):
        self.resourceType = 'Device'
        # type: str
        # possible values: Device

        self.udi = None
        # reference to Device_Udi

        self.status = None
        # type: str
        # possible values: active, inactive, entered-in-error, unknown

        self.type = None
        # reference to CodeableConcept

        self.lotNumber = None
        # type: str

        self.manufacturer = None
        # type: str

        self.manufactureDate = None
        # type: str

        self.expirationDate = None
        # type: str

        self.model = None
        # type: str

        self.version = None
        # type: str

        self.patient = None
        # reference to Reference: identifier

        self.owner = None
        # reference to Reference: identifier

        self.contact = None
        # type: list
        # reference to ContactPoint

        self.location = None
        # reference to Reference: identifier

        self.url = None
        # type: str

        self.note = None
        # type: list
        # reference to Annotation

        self.safety = None
        # type: list
        # reference to CodeableConcept

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
                        'active', 'inactive', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Device_Udi',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'safety'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Device',
             'child_variable': 'owner'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Device',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Device',
             'child_variable': 'patient'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'note'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'identifier'},
        ]


class Device_Udi(fhirbase):
    """
    This resource identifies an instance or a type of a manufactured item
    that is used in the provision of healthcare without being
    substantially changed through that activity. The device may be a
    medical or non-medical device.  Medical devices include durable
    (reusable) medical equipment, implantable devices, as well as
    disposable equipment used for diagnostic, treatment, and research for
    healthcare and public health.  Non-medical devices may include items
    such as a machine, cellphone, computer, application, etc.

    Args:
        deviceIdentifier: The device identifier (DI) is a mandatory, fixed
            portion of a UDI that identifies the labeler and the specific version
            or model of a device.
        name: Name of device as used in labeling or catalog.
        jurisdiction: The identity of the authoritative source for UDI
            generation within a  jurisdiction.  All UDIs are globally unique
            within a single namespace. with the appropriate repository uri as the
            system.  For example,  UDIs of devices managed in the U.S. by the FDA,
            the value is  http://hl7.org/fhir/NamingSystem/fda-udi.
        carrierHRF: The full UDI carrier as the human readable form (HRF)
            representation of the barcode string as printed on the packaging of
            the device.
        carrierAIDC: The full UDI carrier of the Automatic Identification and
            Data Capture (AIDC) technology representation of the barcode string as
            printed on the packaging of the device - E.g a barcode or RFID.
            Because of limitations on character sets in XML and the need to
            round-trip JSON data through XML, AIDC Formats *SHALL* be base64
            encoded.
        issuer: Organization that is charged with issuing UDIs for devices.
            For example, the US FDA issuers include : 1) GS1:
            http://hl7.org/fhir/NamingSystem/gs1-di,  2) HIBCC:
            http://hl7.org/fhir/NamingSystem/hibcc-dI,  3) ICCBBA for blood
            containers: http://hl7.org/fhir/NamingSystem/iccbba-blood-di,  4)
            ICCBA for other devices:
            http://hl7.org/fhir/NamingSystem/iccbba-other-di.
        entryType: A coded entry to indicate how the data was entered.
    """

    __name__ = 'Device_Udi'

    def __init__(self, dict_values=None):
        self.deviceIdentifier = None
        # type: str

        self.name = None
        # type: str

        self.jurisdiction = None
        # type: str

        self.carrierHRF = None
        # type: str

        self.carrierAIDC = None
        # type: str

        self.issuer = None
        # type: str

        self.entryType = None
        # type: str
        # possible values: barcode, rfid, manual, card, self-reported,
        # unknown

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.entryType is not None:
            for value in self.entryType:
                if value is not None and value.lower() not in [
                        'barcode', 'rfid', 'manual', 'card', 'self-reported', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'barcode, rfid, manual, card, self-reported, unknown'))
