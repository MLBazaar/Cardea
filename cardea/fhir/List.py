from .fhirbase import fhirbase


class List(fhirbase):
    """A set of information summarized from a list of other resources.
    """

    def __init__(self, dict_values=None):
        # this is a list resource
        self.resourceType = 'List'
        # type = string
        # possible values: List

        # indicates the current state of this list.
        self.status = None
        # type = string
        # possible values: current, retired, entered-in-error

        # how this list was prepared - whether it is a working list that is
        # suitable for being maintained on an ongoing basis, or if it represents a
        # snapshot of a list of items from another source, or whether it is a
        # prepared list where items may be marked as added, modified or deleted.
        self.mode = None
        # type = string
        # possible values: working, snapshot, changes

        # a label for the list assigned by the author.
        self.title = None
        # type = string

        # this code defines the purpose of the list - why it was created.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the common subject (or patient) of the resources that are in the list,
        # if there is one.
        self.subject = None
        # reference to Reference: identifier

        # the encounter that is the context in which this list was created.
        self.encounter = None
        # reference to Reference: identifier

        # the date that the list was prepared.
        self.date = None
        # type = string

        # the entity responsible for deciding what the contents of the list were.
        # where the list was created by a human, this is the same as the author of
        # the list.
        self.source = None
        # reference to Reference: identifier

        # what order applies to the items in the list.
        self.orderedBy = None
        # reference to CodeableConcept: CodeableConcept

        # comments that apply to the overall list.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # entries in this list.
        self.entry = None
        # type = array
        # reference to List_Entry: List_Entry

        # if the list is empty, why the list is empty.
        self.emptyReason = None
        # reference to CodeableConcept: CodeableConcept

        # identifier for the list assigned for business purposes outside the
        # context of fhir.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'identifier'},

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
             'child_variable': 'emptyReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'List',
             'child_variable': 'source'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'orderedBy'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'List',
             'child_variable': 'subject'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'List',
             'child_variable': 'note'},
        ]


class List_Entry(fhirbase):
    """A set of information summarized from a list of other resources.
    """

    def __init__(self, dict_values=None):
        # the flag allows the system constructing the list to indicate the role
        # and significance of the item in the list.
        self.flag = None
        # reference to CodeableConcept: CodeableConcept

        # true if this item is marked as deleted in the list.
        self.deleted = None
        # type = boolean

        # when this item was added to the list.
        self.date = None
        # type = string

        # a reference to the actual resource from which data was derived.
        self.item = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'List_Entry',
             'child_variable': 'item'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'List_Entry',
             'child_variable': 'flag'},
        ]
