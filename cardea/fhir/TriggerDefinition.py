from .fhirbase import fhirbase


class TriggerDefinition(fhirbase):
    """
    A description of a triggering event.

    Args:
        type: The type of triggering event.
        eventName: The name of the event (if this is a named-event trigger).
        eventTimingTiming: The timing of the event (if this is a period
            trigger).
        eventTimingReference: The timing of the event (if this is a period
            trigger).
        eventTimingDate: The timing of the event (if this is a period
            trigger).
        eventTimingDateTime: The timing of the event (if this is a period
            trigger).
        eventData: The triggering data of the event (if this is a data
            trigger).
    """

    __name__ = 'TriggerDefinition'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: named-event, periodic, data-added,
        # data-modified, data-removed, data-accessed, data-access-ended

        self.eventName = None
        # type: str

        self.eventTimingTiming = None
        # reference to Timing

        self.eventTimingReference = None
        # reference to Reference: identifier

        self.eventTimingDate = None
        # type: str

        self.eventTimingDateTime = None
        # type: str

        self.eventData = None
        # reference to DataRequirement

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'named-event', 'periodic', 'data-added', 'data-modified',
                        'data-removed', 'data-accessed', 'data-access-ended']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'named-event, periodic, data-added, data-modified, data-removed,'
                        'data-accessed, data-access-ended'))

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
