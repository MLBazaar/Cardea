from .fhirbase import fhirbase


class Linkage(fhirbase):
    """Identifies two or more records (resource instances) that are referring
    to the same real-world "occurrence".
    """

    def __init__(self, dict_values=None):
        # this is a linkage resource
        self.resourceType = 'Linkage'
        # type = string
        # possible values: Linkage

        # indicates whether the asserted set of linkages are considered to be "in
        # effect".
        self.active = None
        # type = boolean

        # identifies the user or organization responsible for asserting the
        # linkages and who establishes the context for evaluating the nature of
        # each linkage.
        self.author = None
        # reference to Reference: identifier

        # identifies one of the records that is considered to refer to the same
        # real-world occurrence as well as how the items hould be evaluated within
        # the collection of linked items.
        self.item = None
        # type = array
        # reference to Linkage_Item: Linkage_Item

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Linkage',
             'child_variable': 'author'},

            {'parent_entity': 'Linkage_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Linkage',
             'child_variable': 'item'},
        ]


class Linkage_Item(fhirbase):
    """Identifies two or more records (resource instances) that are referring
    to the same real-world "occurrence".
    """

    def __init__(self, dict_values=None):
        # distinguishes which item is "source of truth" (if any) and which items
        # are no longer considered to be current representations.
        self.type = None
        # type = string
        # possible values: source, alternate, historical

        # the resource instance being linked as part of the group.
        self.resource = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
