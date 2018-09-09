from .fhirbase import fhirbase


class SampledData(fhirbase):
    """A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    __name__ = 'SampledData'

    def __init__(self, dict_values=None):
        # the base quantity that a measured value of zero represents. in addition,
        # this provides the units of the entire measurement series.
        self.origin = None
        # reference to Quantity: Quantity

        # the length of time between sampling times, measured in milliseconds.
        self.period = None
        # type = int

        # a correction factor that is applied to the sampled data points before
        # they are added to the origin.
        self.factor = None
        # type = int

        # the lower limit of detection of the measured points. this is needed if
        # any of the data points have the value "l" (lower than detection limit).
        self.lowerLimit = None
        # type = int

        # the upper limit of detection of the measured points. this is needed if
        # any of the data points have the value "u" (higher than detection limit).
        self.upperLimit = None
        # type = int

        # the number of sample points at each time point. if this value is greater
        # than one, then the dimensions will be interlaced - all the sample points
        # for a point in time will be recorded at once.
        self.dimensions = None
        # type = int

        # a series of data points which are decimal values separated by a single
        # space (character u20). the special values "e" (error), "l" (below
        # detection limit) and "u" (above detection limit) can also be used in
        # place of a decimal value.
        self.data = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'SampledData',
             'child_variable': 'origin'},
        ]
