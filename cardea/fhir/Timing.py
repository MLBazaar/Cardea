from .fhirbase import * 
from .CodeableConcept import CodeableConcept

class Timing(fhirbase):
    """Specifies an event that may occur multiple times. Timing schedules are
    used to record when things are planned, expected or requested to occur.
    The most common usage is in dosage instructions for medications. They
    are also used when planning care of various kinds, and may be used for
    reporting the schedule to which past regular activities were carried
    out.
    """

    def __init__(self, dict_values=None):
        # identifies specific times when the event occurs.
        self.event = None
        # type = array

        # a set of rules that describe when the event is scheduled.
        self.repeat = None
        # reference to Timing_Repeat: Timing_Repeat

        # a code for the timing schedule. some codes such as bid are ubiquitous,
        # but many institutions define their own additional codes. if a code is
        # provided, the code is understood to be a complete statement of whatever
        # is specified in the structured timing data, and either the code or the
        # data may be used to interpret the timing, with the exception that
        # .repeat.bounds still applies over the code (and is not contained in the
        # code).
        self.code = None
        # reference to CodeableConcept: CodeableConcept


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
    """Specifies an event that may occur multiple times. Timing schedules are
    used to record when things are planned, expected or requested to occur.
    The most common usage is in dosage instructions for medications. They
    are also used when planning care of various kinds, and may be used for
    reporting the schedule to which past regular activities were carried
    out.
    """

    def __init__(self, dict_values=None):
        # either a duration for the length of the timing schedule, a range of
        # possible length, or outer bounds for start and/or end limits of the
        # timing schedule.
        self.boundsDuration = None
        # reference to Duration: Duration

        # either a duration for the length of the timing schedule, a range of
        # possible length, or outer bounds for start and/or end limits of the
        # timing schedule.
        self.boundsRange = None
        # reference to Range: Range

        # either a duration for the length of the timing schedule, a range of
        # possible length, or outer bounds for start and/or end limits of the
        # timing schedule.
        self.boundsPeriod = None
        # reference to Period: Period

        # a total count of the desired number of repetitions.
        self.count = None
        # type = int

        # a maximum value for the count of the desired repetitions (e.g. do
        # something 6-8 times).
        self.countMax = None
        # type = int

        # how long this thing happens for when it happens.
        self.duration = None
        # type = int

        # the upper limit of how long this thing happens for when it happens.
        self.durationMax = None
        # type = int

        # the units of time for the duration, in ucum units.
        self.durationUnit = None
        # type = string
        # possible values = s, min, h, d, wk, mo, a

        # the number of times to repeat the action within the specified period /
        # period range (i.e. both period and periodmax provided).
        self.frequency = None
        # type = int

        # if present, indicates that the frequency is a range - so to repeat
        # between [frequency] and [frequencymax] times within the period or period
        # range.
        self.frequencyMax = None
        # type = int

        # indicates the duration of time over which repetitions are to occur; e.g.
        # to express "3 times per day", 3 would be the frequency and "1 day" would
        # be the period.
        self.period = None
        # type = int

        # if present, indicates that the period is a range from [period] to
        # [periodmax], allowing expressing concepts such as "do this once every
        # 3-5 days.
        self.periodMax = None
        # type = int

        # the units of time for the period in ucum units.
        self.periodUnit = None
        # type = string
        # possible values = s, min, h, d, wk, mo, a

        # if one or more days of week is provided, then the action happens only on
        # the specified day(s).
        self.dayOfWeek = None
        # type = array

        # specified time of day for action to take place.
        self.timeOfDay = None
        # type = array

        # real world events that the occurrence of the event should be tied to.
        self.when = None
        # type = array
        # possible values = MORN, AFT, EVE, NIGHT, PHS, HS, WAKE, C, CM, CD, CV, AC, ACM, ACD, ACV, PC, PCM, PCD, PCV

        # the number of minutes from the event. if the event code does not
        # indicate whether the minutes is before or after the event, then the
        # offset is assumed to be after the event.
        self.offset = None
        # type = int


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.durationUnit is not None:
            for value in self.durationUnit:
                if value != None and value.lower() not in ['s', 'min', 'h', 'd', 'wk', 'mo', 'a']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 's, min, h, d, wk, mo, a'))

        if self.periodUnit is not None:
            for value in self.periodUnit:
                if value != None and value.lower() not in ['s', 'min', 'h', 'd', 'wk', 'mo', 'a']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 's, min, h, d, wk, mo, a'))

        if self.when is not None:
            for value in self.when:
                if value != None and value.lower() not in ['morn', 'aft', 'eve', 'night', 'phs', 'hs', 'wake', 'c', 'cm', 'cd', 'cv', 'ac', 'acm', 'acd', 'acv', 'pc', 'pcm', 'pcd', 'pcv']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'morn, aft, eve, night, phs, hs, wake, c, cm, cd, cv, ac, acm, acd, acv, pc, pcm, pcd, pcv'))

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

