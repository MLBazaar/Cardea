from .fhirbase import fhirbase


class Linkage(fhirbase):
    """
    Identifies two or more records (resource instances) that are referring
    to the same real-world "occurrence".
    """

    __name__ = 'Linkage'

    def __init__(self, dict_values=None):
        self.resourceType = 'Linkage'
        """
        This is a Linkage resource

        type: string
        possible values: Linkage
        """

        self.active = None
        """
        Indicates whether the asserted set of linkages are considered to be
        "in effect".

        type: boolean
        """

        self.author = None
        """
        Identifies the user or organization responsible for asserting the
        linkages and who establishes the context for evaluating the nature of
        each linkage.

        reference to Reference: identifier
        """

        self.item = None
        """
        Identifies one of the records that is considered to refer to the same
        real-world occurrence as well as how the items hould be evaluated
        within the collection of linked items.

        type: array
        reference to Linkage_Item
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Linkage_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Linkage',
             'child_variable': 'item'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Linkage',
             'child_variable': 'author'},
        ]


class Linkage_Item(fhirbase):
    """
    Identifies two or more records (resource instances) that are referring
    to the same real-world "occurrence".
    """

    __name__ = 'Linkage_Item'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Distinguishes which item is "source of truth" (if any) and which items
        are no longer considered to be current representations.

        type: string
        possible values: source, alternate, historical
        """

        self.resource = None
        """
        The resource instance being linked as part of the group.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'source', 'alternate', 'historical']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'source, alternate, historical'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Linkage_Item',
             'child_variable': 'resource'},
        ]
