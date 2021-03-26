from .fhirbase import fhirbase


class DeviceMetric(fhirbase):
    """
    Describes a measurement, calculation or setting capability of a
    medical device.

    Args:
        resourceType: This is a DeviceMetric resource
        identifier: Describes the unique identification of this metric that
            has been assigned by the device or gateway software. For example:
            handle ID.  It should be noted that in order to make the identifier
            unique, the system element of the identifier should be set to the
            unique identifier of the device.
        type: Describes the type of the metric. For example: Heart Rate, PEEP
            Setting, etc.
        unit: Describes the unit that an observed value determined for this
            metric will have. For example: Percent, Seconds, etc.
        source: Describes the link to the  Device that this DeviceMetric
            belongs to and that contains administrative device information such as
            manufacturer, serial number, etc.
        parent: Describes the link to the  DeviceComponent that this
            DeviceMetric belongs to and that provide information about the
            location of this DeviceMetric in the containment structure of the
            parent Device. An example would be a DeviceComponent that represents a
            Channel. This reference can be used by a client application to
            distinguish DeviceMetrics that have the same type, but should be
            interpreted based on their containment location.
        operationalStatus: Indicates current operational state of the device.
            For example: On, Off, Standby, etc.
        color: Describes the color representation for the metric. This is
            often used to aid clinicians to track and identify parameter types by
            color. In practice, consider a Patient Monitor that has ECG/HR and
            Pleth for example; the parameters are displayed in different
            characteristic colors, such as HR-blue, BP-green, and PR and SpO2-
            magenta.
        category: Indicates the category of the observation generation
            process. A DeviceMetric can be for example a setting, measurement, or
            calculation.
        measurementPeriod: Describes the measurement repetition time. This is
            not necessarily the same as the update period. The measurement
            repetition time can range from milliseconds up to hours. An example
            for a measurement repetition time in the range of milliseconds is the
            sampling rate of an ECG. An example for a measurement repetition time
            in the range of hours is a NIBP that is triggered automatically every
            hour. The update period may be different than the measurement
            repetition time, if the device does not update the published observed
            value with the same frequency as it was measured.
        calibration: Describes the calibrations that have been performed or
            that are required to be performed.
    """

    __name__ = 'DeviceMetric'

    def __init__(self, dict_values=None):
        self.resourceType = 'DeviceMetric'
        # type: str
        # possible values: DeviceMetric

        self.type = None
        # reference to CodeableConcept

        self.unit = None
        # reference to CodeableConcept

        self.source = None
        # reference to Reference: identifier

        self.parent = None
        # reference to Reference: identifier

        self.operationalStatus = None
        # type: str
        # possible values: on, off, standby, entered-in-error

        self.color = None
        # type: str
        # possible values: black, red, green, yellow, blue, magenta,
        # cyan, white

        self.category = None
        # type: str
        # possible values: measurement, setting, calculation,
        # unspecified

        self.measurementPeriod = None
        # reference to Timing

        self.calibration = None
        # type: list
        # reference to DeviceMetric_Calibration

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'DeviceMetric_Calibration',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'calibration'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'unit'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceMetric',
             'child_variable': 'parent'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'measurementPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceMetric',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceMetric',
             'child_variable': 'source'},
        ]


class DeviceMetric_Calibration(fhirbase):
    """
    Describes a measurement, calculation or setting capability of a
    medical device.

    Args:
        type: Describes the type of the calibration method.
        state: Describes the state of the calibration.
        time: Describes the time last calibration has been performed.
    """

    __name__ = 'DeviceMetric_Calibration'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: unspecified, offset, gain, two-point

        self.state = None
        # type: str
        # possible values: not-calibrated, calibration-required,
        # calibrated, unspecified

        self.time = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
