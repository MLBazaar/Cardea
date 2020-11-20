from .fhirbase import fhirbase


class Timing(fhirbase):
    """
    Specifies an event that may occur multiple times. Timing schedules are
    used to record when things are planned, expected or requested to
    occur. The most common usage is in dosage instructions for
    medications. They are also used when planning care of various kinds,
    and may be used for reporting the schedule to which past regular
    activities were carried out.

    Args:
        event: Identifies specific times when the event occurs.
        repeat: A set of rules that describe when the event is scheduled.
        code: A code for the timing schedule. Some codes such as BID are
            ubiquitous, but many institutions define their own additional codes.
            If a code is provided, the code is understood to be a complete
            statement of whatever is specified in the structured timing data, and
            either the code or the data may be used to interpret the Timing, with
            the exception that .repeat.bounds still applies over the code (and is
            not contained in the code).
    """

    __name__ = 'Timing'

    def __init__(self, dict_values=None):
        self.event = None
        # type: list

        self.repeat = None
        # reference to Timing_Repeat

        self.code = None
        # reference to CodeableConcept

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

    Args:
        boundsDuration: Either a duration for the length of the timing
            schedule, a range of possible length, or outer bounds for start and/or
            end limits of the timing schedule.
        boundsRange: Either a duration for the length of the timing schedule,
            a range of possible length, or outer bounds for start and/or end
            limits of the timing schedule.
        boundsPeriod: Either a duration for the length of the timing schedule,
            a range of possible length, or outer bounds for start and/or end
            limits of the timing schedule.
        count: A total count of the desired number of repetitions.
        countMax: A maximum value for the count of the desired repetitions
            (e.g. do something 6-8 times).
        duration: How long this thing happens for when it happens.
        durationMax: The upper limit of how long this thing happens for when
            it happens.
        durationUnit: The units of time for the duration, in UCUM units.
        frequency: The number of times to repeat the action within the
            specified period / period range (i.e. both period and periodMax
            provided).
        frequencyMax: If present, indicates that the frequency is a range - so
            to repeat between [frequency] and [frequencyMax] times within the
            period or period range.
        period: Indicates the duration of time over which repetitions are to
            occur; e.g. to express "3 times per day", 3 would be the frequency and
            "1 day" would be the period.
        periodMax: If present, indicates that the period is a range from
            [period] to [periodMax], allowing expressing concepts such as "do this
            once every 3-5 days.
        periodUnit: The units of time for the period in UCUM units.
        dayOfWeek: If one or more days of week is provided, then the action
            happens only on the specified day(s).
        timeOfDay: Specified time of day for action to take place.
        when: Real world events that the occurrence of the event should be
            tied to.
        offset: The number of minutes from the event. If the event code does
            not indicate whether the minutes is before or after the event, then
            the offset is assumed to be after the event.
    """

    __name__ = 'Timing_Repeat'

    def __init__(self, dict_values=None):
        self.boundsDuration = None
        # reference to Duration

        self.boundsRange = None
        # reference to Range

        self.boundsPeriod = None
        # reference to Period

        self.count = None
        # type: int

        self.countMax = None
        # type: int

        self.duration = None
        # type: int

        self.durationMax = None
        # type: int

        self.durationUnit = None
        # type: str
        # possible values: s, min, h, d, wk, mo, a

        self.frequency = None
        # type: int

        self.frequencyMax = None
        # type: int

        self.period = None
        # type: int

        self.periodMax = None
        # type: int

        self.periodUnit = None
        # type: str
        # possible values: s, min, h, d, wk, mo, a

        self.dayOfWeek = None
        # type: list

        self.timeOfDay = None
        # type: list

        self.when = None
        # type: list
        # possible values: MORN, AFT, EVE, NIGHT, PHS, HS, WAKE, C,
        # CM, CD, CV, AC, ACM, ACD, ACV, PC, PCM, PCD, PCV

        self.offset = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'Timing_Repeat',
             'child_variable': 'boundsDuration'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Timing_Repeat',
             'child_variable': 'boundsPeriod'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Timing_Repeat',
             'child_variable': 'boundsRange'},
        ]
