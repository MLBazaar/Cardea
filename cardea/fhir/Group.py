from .fhirbase import fhirbase


class Group(fhirbase):
    """Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.
    """

    __name__ = 'Group'

    def __init__(self, dict_values=None):
        # this is a group resource
        self.resourceType = 'Group'
        # type = string
        # possible values: Group

        # indicates whether the record for the group is available for use or is
        # merely being retained for historical purposes.
        self.active = None
        # type = boolean

        # identifies the broad classification of the kind of resources the group
        # includes.
        self.type = None
        # type = string
        # possible values: person, animal, practitioner, device,
        # medication, substance

        # if true, indicates that the resource refers to a specific group of real
        # individuals.  if false, the group defines a set of intended individuals.
        self.actual = None
        # type = boolean

        # provides a specific type of resource the group includes; e.g. "cow",
        # "syringe", etc.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a label assigned to the group for human identification and
        # communication.
        self.name = None
        # type = string

        # a count of the number of resource instances that are part of the group.
        self.quantity = None
        # type = int

        # identifies the traits shared by members of the group.
        self.characteristic = None
        # type = array
        # reference to Group_Characteristic: Group_Characteristic

        # identifies the resource instances that are members of the group.
        self.member = None
        # type = array
        # reference to Group_Member: Group_Member

        # a unique business identifier for this group.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'person', 'animal', 'practitioner', 'device', 'medication', 'substance']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'person, animal, practitioner, device, medication, substance'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Group',
             'child_variable': 'code'},

            {'parent_entity': 'Group_Characteristic',
             'parent_variable': 'object_id',
             'child_entity': 'Group',
             'child_variable': 'characteristic'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Group',
             'child_variable': 'identifier'},

            {'parent_entity': 'Group_Member',
             'parent_variable': 'object_id',
             'child_entity': 'Group',
             'child_variable': 'member'},
        ]


class Group_Characteristic(fhirbase):
    """Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.
    """

    __name__ = 'Group_Characteristic'

    def __init__(self, dict_values=None):
        # a code that identifies the kind of trait being asserted.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the value of the trait that holds (or does not hold - see 'exclude') for
        # members of the group.
        self.valueCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the value of the trait that holds (or does not hold - see 'exclude') for
        # members of the group.
        self.valueBoolean = None
        # type = boolean

        # the value of the trait that holds (or does not hold - see 'exclude') for
        # members of the group.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # the value of the trait that holds (or does not hold - see 'exclude') for
        # members of the group.
        self.valueRange = None
        # reference to Range: Range

        # if true, indicates the characteristic is one that is not held by members
        # of the group.
        self.exclude = None
        # type = boolean

        # the period over which the characteristic is tested; e.g. the patient had
        # an operation during the month of june.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'period'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'code'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueRange'},
        ]


class Group_Member(fhirbase):
    """Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.
    """

    __name__ = 'Group_Member'

    def __init__(self, dict_values=None):
        # a reference to the entity that is a member of the group. must be
        # consistent with group.type.
        self.entity = None
        # reference to Reference: identifier

        # the period that the member was in the group, if known.
        self.period = None
        # reference to Period: Period

        # a flag to indicate that the member is no longer in the group, but
        # previously may have been a member.
        self.inactive = None
        # type = boolean

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Member',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Group_Member',
             'child_variable': 'entity'},
        ]
