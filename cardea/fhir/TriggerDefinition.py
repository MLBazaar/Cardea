from .fhirbase import fhirbase


class TriggerDefinition(fhirbase):
    """
    A description of a triggering event.
    """

    __name__ = 'TriggerDefinition'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The type of triggering event.

        type: string
        possible values: named-event, periodic, data-added,
        data-modified, data-removed, data-accessed, data-access-ended
        """

        self.eventName = None
        """
        The name of the event (if this is a named-event trigger).

        type: string
        """

        self.eventTimingTiming = None
        """
        The timing of the event (if this is a period trigger).

        reference to Timing
        """

        self.eventTimingReference = None
        """
        The timing of the event (if this is a period trigger).

        reference to Reference: identifier
        """

        self.eventTimingDate = None
        """
        The timing of the event (if this is a period trigger).

        type: string
        """

        self.eventTimingDateTime = None
        """
        The timing of the event (if this is a period trigger).

        type: string
        """

        self.eventData = None
        """
        The triggering data of the event (if this is a data trigger).

        reference to DataRequirement
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TriggerDefinition',
             'child_variable': 'eventTimingReference'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'TriggerDefinition',
             'child_variable': 'eventTimingTiming'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'TriggerDefinition',
             'child_variable': 'eventData'},
        ]
