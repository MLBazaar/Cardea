from .fhirbase import fhirbase


class SampledData(fhirbase):
    """
    A series of measurements taken by a device, with upper and lower
    limits. There may be more than one dimension in the data.

    Args:
        origin: The base quantity that a measured value of zero represents. In
            addition, this provides the units of the entire measurement series.
        period: The length of time between sampling times, measured in
            milliseconds.
        factor: A correction factor that is applied to the sampled data points
            before they are added to the origin.
        lowerLimit: The lower limit of detection of the measured points. This
            is needed if any of the data points have the value "L" (lower than
            detection limit).
        upperLimit: The upper limit of detection of the measured points. This
            is needed if any of the data points have the value "U" (higher than
            detection limit).
        dimensions: The number of sample points at each time point. If this
            value is greater than one, then the dimensions will be interlaced -
            all the sample points for a point in time will be recorded at once.
        data: A series of data points which are decimal values separated by a
            single space (character u20). The special values "E" (error), "L"
            (below detection limit) and "U" (above detection limit) can also be
            used in place of a decimal value.
    """

    __name__ = 'SampledData'

    def __init__(self, dict_values=None):
        self.origin = None
        # reference to Quantity

        self.period = None
        # type: int

        self.factor = None
        # type: int

        self.lowerLimit = None
        # type: int

        self.upperLimit = None
        # type: int

        self.dimensions = None
        # type: int

        self.data = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'SampledData',
             'child_variable': 'origin'},
        ]
