from .fhirbase import fhirbase


class Linkage(fhirbase):
    """
    Identifies two or more records (resource instances) that are referring
    to the same real-world "occurrence".

    Args:
        resourceType: This is a Linkage resource
        active: Indicates whether the asserted set of linkages are considered
            to be "in effect".
        author: Identifies the user or organization responsible for asserting
            the linkages and who establishes the context for evaluating the nature
            of each linkage.
        item: Identifies one of the records that is considered to refer to the
            same real-world occurrence as well as how the items hould be evaluated
            within the collection of linked items.
    """

    __name__ = 'Linkage'

    def __init__(self, dict_values=None):
        self.resourceType = 'Linkage'
        # type: str
        # possible values: Linkage

        self.active = None
        # type: bool

        self.author = None
        # reference to Reference: identifier

        self.item = None
        # type: list
        # reference to Linkage_Item

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        type: Distinguishes which item is "source of truth" (if any) and which
            items are no longer considered to be current representations.
        resource: The resource instance being linked as part of the group.
    """

    __name__ = 'Linkage_Item'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: source, alternate, historical

        self.resource = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
