from .fhirbase import fhirbase


class Device(fhirbase):
    """This resource identifies an instance or a type of a manufactured item
    that is used in the provision of healthcare without being substantially
    changed through that activity. The device may be a medical or non-
    medical device.  Medical devices include durable (reusable) medical
    equipment, implantable devices, as well as disposable equipment used for
    diagnostic, treatment, and research for healthcare and public health.
    Non-medical devices may include items such as a machine, cellphone,
    computer, application, etc.
    """

    __name__ = 'Device'

    def __init__(self, dict_values=None):
        # this is a device resource
        self.resourceType = 'Device'
        # type = string
        # possible values: Device

        # [unique device identifier (udi)](device.html#5.11.3.2.2) assigned to
        # device label or package.
        self.udi = None
        # reference to Device_Udi: Device_Udi

        # status of the device availability.
        self.status = None
        # type = string
        # possible values: active, inactive, entered-in-error, unknown

        # code or identifier to identify a kind of device.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # lot number assigned by the manufacturer.
        self.lotNumber = None
        # type = string

        # a name of the manufacturer.
        self.manufacturer = None
        # type = string

        # the date and time when the device was manufactured.
        self.manufactureDate = None
        # type = string

        # the date and time beyond which this device is no longer valid or should
        # not be used (if applicable).
        self.expirationDate = None
        # type = string

        # the "model" is an identifier assigned by the manufacturer to identify
        # the product by its type. this number is shared by the all devices sold
        # as the same type.
        self.model = None
        # type = string

        # the version of the device, if the device has multiple releases under the
        # same model, or if the device is software or carries firmware.
        self.version = None
        # type = string

        # patient information, if the device is affixed to a person.
        self.patient = None
        # reference to Reference: identifier

        # an organization that is responsible for the provision and ongoing
        # maintenance of the device.
        self.owner = None
        # reference to Reference: identifier

        # contact details for an organization or a particular human that is
        # responsible for the device.
        self.contact = None
        # type = array
        # reference to ContactPoint: ContactPoint

        # the place where the device can be found.
        self.location = None
        # reference to Reference: identifier

        # a network address on which the device may be contacted directly.
        self.url = None
        # type = string

        # descriptive information, usage information or implantation information
        # that is not captured in an existing element.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # provides additional safety characteristics about a medical device.  for
        # example devices containing latex.
        self.safety = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # unique instance identifiers assigned to a device by manufacturers other
        # organizations or owners.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'inactive', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Device',
             'child_variable': 'patient'},

            {'parent_entity': 'Device_Udi',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'udi'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'safety'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Device',
             'child_variable': 'owner'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Device',
             'child_variable': 'location'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Device',
             'child_variable': 'identifier'},
        ]


class Device_Udi(fhirbase):
    """This resource identifies an instance or a type of a manufactured item
    that is used in the provision of healthcare without being substantially
    changed through that activity. The device may be a medical or non-
    medical device.  Medical devices include durable (reusable) medical
    equipment, implantable devices, as well as disposable equipment used for
    diagnostic, treatment, and research for healthcare and public health.
    Non-medical devices may include items such as a machine, cellphone,
    computer, application, etc.
    """

    __name__ = 'Device_Udi'

    def __init__(self, dict_values=None):
        # the device identifier (di) is a mandatory, fixed portion of a udi that
        # identifies the labeler and the specific version or model of a device.
        self.deviceIdentifier = None
        # type = string

        # name of device as used in labeling or catalog.
        self.name = None
        # type = string

        # the identity of the authoritative source for udi generation within a
        # jurisdiction.  all udis are globally unique within a single namespace.
        # with the appropriate repository uri as the system.  for example,  udis
        # of devices managed in the u.s. by the fda, the value is
        # http://hl7.org/fhir/namingsystem/fda-udi.
        self.jurisdiction = None
        # type = string

        # the full udi carrier as the human readable form (hrf) representation of
        # the barcode string as printed on the packaging of the device.
        self.carrierHRF = None
        # type = string

        # the full udi carrier of the automatic identification and data capture
        # (aidc) technology representation of the barcode string as printed on the
        # packaging of the device - e.g a barcode or rfid.   because of
        # limitations on character sets in xml and the need to round-trip json
        # data through xml, aidc formats *shall* be base64 encoded.
        self.carrierAIDC = None
        # type = string

        # organization that is charged with issuing udis for devices.  for
        # example, the us fda issuers include : 1) gs1:
        # http://hl7.org/fhir/namingsystem/gs1-di,  2) hibcc:
        # http://hl7.org/fhir/namingsystem/hibcc-di,  3) iccbba for blood
        # containers: http://hl7.org/fhir/namingsystem/iccbba-blood-di,  4) iccba
        # for other devices: http://hl7.org/fhir/namingsystem/iccbba-other-di.
        self.issuer = None
        # type = string

        # a coded entry to indicate how the data was entered.
        self.entryType = None
        # type = string
        # possible values: barcode, rfid, manual, card, self-reported,
        # unknown

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.entryType is not None:
            for value in self.entryType:
                if value is not None and value.lower() not in [
                        'barcode', 'rfid', 'manual', 'card', 'self-reported', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'barcode, rfid, manual, card, self-reported, unknown'))
