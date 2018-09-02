from .fhirbase import fhirbase


class DeviceMetric(fhirbase):
    """Describes a measurement, calculation or setting capability of a medical
    device.
    """

    def __init__(self, dict_values=None):
        # this is a devicemetric resource
        self.resourceType = 'DeviceMetric'
        # type = string
        # possible values: DeviceMetric

        # describes the type of the metric. for example: heart rate, peep setting,
        # etc.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # describes the unit that an observed value determined for this metric
        # will have. for example: percent, seconds, etc.
        self.unit = None
        # reference to CodeableConcept: CodeableConcept

        # describes the link to the  device that this devicemetric belongs to and
        # that contains administrative device information such as manufacturer,
        # serial number, etc.
        self.source = None
        # reference to Reference: identifier

        # describes the link to the  devicecomponent that this devicemetric
        # belongs to and that provide information about the location of this
        # devicemetric in the containment structure of the parent device. an
        # example would be a devicecomponent that represents a channel. this
        # reference can be used by a client application to distinguish
        # devicemetrics that have the same type, but should be interpreted based
        # on their containment location.
        self.parent = None
        # reference to Reference: identifier

        # indicates current operational state of the device. for example: on, off,
        # standby, etc.
        self.operationalStatus = None
        # type = string
        # possible values: on, off, standby, entered-in-error

        # describes the color representation for the metric. this is often used to
        # aid clinicians to track and identify parameter types by color. in
        # practice, consider a patient monitor that has ecg/hr and pleth for
        # example; the parameters are displayed in different characteristic
        # colors, such as hr-blue, bp-green, and pr and spo2- magenta.
        self.color = None
        # type = string
        # possible values: black, red, green, yellow, blue, magenta,
        # cyan, white

        # indicates the category of the observation generation process. a
        # devicemetric can be for example a setting, measurement, or calculation.
        self.category = None
        # type = string
        # possible values: measurement, setting, calculation,
        # unspecified

        # describes the measurement repetition time. this is not necessarily the
        # same as the update period. the measurement repetition time can range
        # from milliseconds up to hours. an example for a measurement repetition
        # time in the range of milliseconds is the sampling rate of an ecg. an
        # example for a measurement repetition time in the range of hours is a
        # nibp that is triggered automatically every hour. the update period may
        # be different than the measurement repetition time, if the device does
        # not update the published observed value with the same frequency as it
        # was measured.
        self.measurementPeriod = None
        # reference to Timing: Timing

        # describes the calibrations that have been performed or that are required
        # to be performed.
        self.calibration = None
        # type = array
        # reference to DeviceMetric_Calibration: DeviceMetric_Calibration

        # describes the unique identification of this metric that has been
        # assigned by the device or gateway software. for example: handle id.  it
        # should be noted that in order to make the identifier unique, the system
        # element of the identifier should be set to the unique identifier of the
        # device.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.operationalStatus is not None:
            for value in self.operationalStatus:
                if value is not None and value.lower() not in [
                        'on', 'off', 'standby', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'on, off, standby, entered-in-error'))

        if self.color is not None:
            for value in self.color:
                if value is not None and value.lower() not in [
                        'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'black, red, green, yellow, blue, magenta, cyan, white'))

        if self.category is not None:
            for value in self.category:
                if value is not None and value.lower() not in [
                        'measurement', 'setting', 'calculation', 'unspecified']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'measurement, setting, calculation, unspecified'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'identifier'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'measurementPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceMetric',
             'child_variable': 'source'},

            {'parent_entity': 'DeviceMetric_Calibration',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'calibration'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'unit'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceMetric',
             'child_variable': 'parent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'type'},
        ]


class DeviceMetric_Calibration(fhirbase):
    """Describes a measurement, calculation or setting capability of a medical
    device.
    """

    def __init__(self, dict_values=None):
        # describes the type of the calibration method.
        self.type = None
        # type = string
        # possible values: unspecified, offset, gain, two-point

        # describes the state of the calibration.
        self.state = None
        # type = string
        # possible values: not-calibrated, calibration-required,
        # calibrated, unspecified

        # describes the time last calibration has been performed.
        self.time = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'unspecified', 'offset', 'gain', 'two-point']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'unspecified, offset, gain, two-point'))

        if self.state is not None:
            for value in self.state:
                if value is not None and value.lower() not in [
                        'not-calibrated', 'calibration-required', 'calibrated', 'unspecified']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'not-calibrated, calibration-required, calibrated, unspecified'))
