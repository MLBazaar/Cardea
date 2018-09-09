from .fhirbase import fhirbase


class List(fhirbase):
    """
    A set of information summarized from a list of other resources.
    """

    __name__ = 'List'

    def __init__(self, dict_values=None):
        self.resourceType = 'List'
        """
        This is a List resource

        type: string
        possible values: List
        """

        self.status = None
        """
        Indicates the current state of this list.

        type: string
        possible values: current, retired, entered-in-error
        """

        self.mode = None
        """
        How this list was prepared - whether it is a working list that is
        suitable for being maintained on an ongoing basis, or if it represents
        a snapshot of a list of items from another source, or whether it is a
        prepared list where items may be marked as added, modified or deleted.

        type: string
        possible values: working, snapshot, changes
        """

        self.title = None
        """
        A label for the list assigned by the author.

        type: string
        """

        self.code = None
        """
        This code defines the purpose of the list - why it was created.

        reference to CodeableConcept
        """

        self.subject = None
        """
        The common subject (or patient) of the resources that are in the list,
        if there is one.

        reference to Reference: identifier
        """

        self.encounter = None
        """
        The encounter that is the context in which this list was created.

        reference to Reference: identifier
        """

        self.date = None
        """
        The date that the list was prepared.

        type: string
        """

        self.source = None
        """
        The entity responsible for deciding what the contents of the list
        were. Where the list was created by a human, this is the same as the
        author of the list.

        reference to Reference: identifier
        """

        self.orderedBy = None
        """
        What order applies to the items in the list.

        reference to CodeableConcept
        """

        self.note = None
        """
        Comments that apply to the overall list.

        type: array
        reference to Annotation
        """

        self.entry = None
        """
        Entries in this list.

        type: array
        reference to List_Entry
        """

        self.emptyReason = None
        """
        If the list is empty, why the list is empty.

        reference to CodeableConcept
        """

        self.identifier = None
        """
        Identifier for the List assigned for business purposes outside the
        context of FHIR.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'current', 'retired', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'current, retired, entered-in-error'))

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'working', 'snapshot', 'changes']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'working, snapshot, changes'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'List',
             'child_variable': 'source'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'emptyReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'orderedBy'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'List',
             'child_variable': 'subject'},

            {'parent_entity': 'List_Entry',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'entry'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'List',
             'child_variable': 'encounter'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'code'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'identifier'},
        ]


class List_Entry(fhirbase):
    """
    A set of information summarized from a list of other resources.
    """

    __name__ = 'List_Entry'

    def __init__(self, dict_values=None):
        self.flag = None
        """
        The flag allows the system constructing the list to indicate the role
        and significance of the item in the list.

        reference to CodeableConcept
        """

        self.deleted = None
        """
        True if this item is marked as deleted in the list.

        type: boolean
        """

        self.date = None
        """
        When this item was added to the list.

        type: string
        """

        self.item = None
        """
        A reference to the actual resource from which data was derived.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'List_Entry',
             'child_variable': 'flag'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'List_Entry',
             'child_variable': 'item'},
        ]
