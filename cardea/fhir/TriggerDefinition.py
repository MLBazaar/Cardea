from .fhirbase import fhirbase


class TriggerDefinition(fhirbase):
    """A description of a triggering event.
    """

    __name__ = 'TriggerDefinition'

    def __init__(self, dict_values=None):
        # the type of triggering event.
        self.type = None
        # type = string
        # possible values: named-event, periodic, data-added, data-
        # modified, data-removed, data-accessed, data-access-ended

        # the name of the event (if this is a named-event trigger).
        self.eventName = None
        # type = string

        # the timing of the event (if this is a period trigger).
        self.eventTimingTiming = None
        # reference to Timing: Timing

        # the timing of the event (if this is a period trigger).
        self.eventTimingReference = None
        # reference to Reference: identifier

        # the timing of the event (if this is a period trigger).
        self.eventTimingDate = None
        # type = string

        # the timing of the event (if this is a period trigger).
        self.eventTimingDateTime = None
        # type = string

        # the triggering data of the event (if this is a data trigger).
        self.eventData = None
        # reference to DataRequirement: DataRequirement

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'named-event', 'periodic', 'data-added', 'data-modified',
                        'data-removed', 'data - accessed', 'data - access - ended']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'named-event, periodic, data-added, data-modified,'
                        'data-removed, data-accessed, data-access-ended'))

    def get_relationships(self):

        return [
            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'TriggerDefinition',
             'child_variable': 'eventData'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'TriggerDefinition',
             'child_variable': 'eventTimingTiming'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TriggerDefinition',
             'child_variable': 'eventTimingReference'},
        ]
