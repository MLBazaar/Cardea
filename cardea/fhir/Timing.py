from .fhirbase import fhirbase


class Timing(fhirbase):
    """
    Specifies an event that may occur multiple times. Timing schedules are
    used to record when things are planned, expected or requested to
    occur. The most common usage is in dosage instructions for
    medications. They are also used when planning care of various kinds,
    and may be used for reporting the schedule to which past regular
    activities were carried out.
    """

    __name__ = 'Timing'

    def __init__(self, dict_values=None):
        self.event = None
        """
        Identifies specific times when the event occurs.

        type: array
        """

        self.repeat = None
        """
        A set of rules that describe when the event is scheduled.

        reference to Timing_Repeat
        """

        self.code = None
        """
        A code for the timing schedule. Some codes such as BID are ubiquitous,
        but many institutions define their own additional codes. If a code is
        provided, the code is understood to be a complete statement of
        whatever is specified in the structured timing data, and either the
        code or the data may be used to interpret the Timing, with the
        exception that .repeat.bounds still applies over the code (and is not
        contained in the code).

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Timing',
             'child_variable': 'code'},

            {'parent_entity': 'Timing_Repeat',
             'parent_variable': 'object_id',
             'child_entity': 'Timing',
             'child_variable': 'repeat'},
        ]


class Timing_Repeat(fhirbase):
    """
    Specifies an event that may occur multiple times. Timing schedules are
    used to record when things are planned, expected or requested to
    occur. The most common usage is in dosage instructions for
    medications. They are also used when planning care of various kinds,
    and may be used for reporting the schedule to which past regular
    activities were carried out.
    """

    __name__ = 'Timing_Repeat'

    def __init__(self, dict_values=None):
        self.boundsDuration = None
        """
        Either a duration for the length of the timing schedule, a range of
        possible length, or outer bounds for start and/or end limits of the
        timing schedule.

        reference to Duration
        """

        self.boundsRange = None
        """
        Either a duration for the length of the timing schedule, a range of
        possible length, or outer bounds for start and/or end limits of the
        timing schedule.

        reference to Range
        """

        self.boundsPeriod = None
        """
        Either a duration for the length of the timing schedule, a range of
        possible length, or outer bounds for start and/or end limits of the
        timing schedule.

        reference to Period
        """

        self.count = None
        """
        A total count of the desired number of repetitions.

        type: int
        """

        self.countMax = None
        """
        A maximum value for the count of the desired repetitions (e.g. do
        something 6-8 times).

        type: int
        """

        self.duration = None
        """
        How long this thing happens for when it happens.

        type: int
        """

        self.durationMax = None
        """
        The upper limit of how long this thing happens for when it happens.

        type: int
        """

        self.durationUnit = None
        """
        The units of time for the duration, in UCUM units.

        type: string
        possible values: s, min, h, d, wk, mo, a
        """

        self.frequency = None
        """
        The number of times to repeat the action within the specified period /
        period range (i.e. both period and periodMax provided).

        type: int
        """

        self.frequencyMax = None
        """
        If present, indicates that the frequency is a range - so to repeat
        between [frequency] and [frequencyMax] times within the period or
        period range.

        type: int
        """

        self.period = None
        """
        Indicates the duration of time over which repetitions are to occur;
        e.g. to express "3 times per day", 3 would be the frequency and "1
        day" would be the period.

        type: int
        """

        self.periodMax = None
        """
        If present, indicates that the period is a range from [period] to
        [periodMax], allowing expressing concepts such as "do this once every
        3-5 days.

        type: int
        """

        self.periodUnit = None
        """
        The units of time for the period in UCUM units.

        type: string
        possible values: s, min, h, d, wk, mo, a
        """

        self.dayOfWeek = None
        """
        If one or more days of week is provided, then the action happens only
        on the specified day(s).

        type: array
        """

        self.timeOfDay = None
        """
        Specified time of day for action to take place.

        type: array
        """

        self.when = None
        """
        Real world events that the occurrence of the event should be tied to.

        type: array
        possible values: MORN, AFT, EVE, NIGHT, PHS, HS, WAKE, C, CM,
        CD, CV, AC, ACM, ACD, ACV, PC, PCM, PCD, PCV
        """

        self.offset = None
        """
        The number of minutes from the event. If the event code does not
        indicate whether the minutes is before or after the event, then the
        offset is assumed to be after the event.

        type: int
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.durationUnit is not None:
            for value in self.durationUnit:
                if value is not None and value.lower() not in [
                        's', 'min', 'h', 'd', 'wk', 'mo', 'a']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 's, min, h, d, wk, mo, a'))

        if self.periodUnit is not None:
            for value in self.periodUnit:
                if value is not None and value.lower() not in [
                        's', 'min', 'h', 'd', 'wk', 'mo', 'a']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 's, min, h, d, wk, mo, a'))

        if self.when is not None:
            for value in self.when:
                if value is not None and value.lower() not in [
                    'morn', 'aft', 'eve', 'night', 'phs', 'hs', 'wake', 'c', 'cm', 'cd',
                        'cv', 'ac', 'acm', 'acd', 'acv', 'pc', 'pcm', 'pcd', 'pcv']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'MORN, AFT, EVE, NIGHT, PHS, HS, WAKE, C, CM, CD, CV, AC, ACM, ACD,'
                        'ACV, PC, PCM, PCD, PCV'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Timing_Repeat',
             'child_variable': 'boundsRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Timing_Repeat',
             'child_variable': 'boundsPeriod'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Timing_Repeat',
             'child_variable': 'boundsDuration'},
        ]
