from .fhirbase import fhirbase


class Group(fhirbase):
    """
    Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.

    Args:
        resourceType: This is a Group resource
        identifier: A unique business identifier for this group.
        active: Indicates whether the record for the group is available for
            use or is merely being retained for historical purposes.
        type: Identifies the broad classification of the kind of resources the
            group includes.
        actual: If true, indicates that the resource refers to a specific
            group of real individuals.  If false, the group defines a set of
            intended individuals.
        code: Provides a specific type of resource the group includes; e.g.
            "cow", "syringe", etc.
        name: A label assigned to the group for human identification and
            communication.
        quantity: A count of the number of resource instances that are part of
            the group.
        characteristic: Identifies the traits shared by members of the group.
        member: Identifies the resource instances that are members of the
            group.
    """

    __name__ = 'Group'

    def __init__(self, dict_values=None):
        self.resourceType = 'Group'
        # type: str
        # possible values: Group

        self.active = None
        # type: bool

        self.type = None
        # type: str
        # possible values: person, animal, practitioner, device,
        # medication, substance

        self.actual = None
        # type: bool

        self.code = None
        # reference to CodeableConcept

        self.name = None
        # type: str

        self.quantity = None
        # type: int

        self.characteristic = None
        # type: list
        # reference to Group_Characteristic

        self.member = None
        # type: list
        # reference to Group_Member

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'person', 'animal', 'practitioner', 'device', 'medication',
                        'substance']:
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

            {'parent_entity': 'Group_Member',
             'parent_variable': 'object_id',
             'child_entity': 'Group',
             'child_variable': 'member'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Group',
             'child_variable': 'identifier'},
        ]


class Group_Characteristic(fhirbase):
    """
    Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.

    Args:
        code: A code that identifies the kind of trait being asserted.
        valueCodeableConcept: The value of the trait that holds (or does not
            hold - see 'exclude') for members of the group.
        valueBoolean: The value of the trait that holds (or does not hold -
            see 'exclude') for members of the group.
        valueQuantity: The value of the trait that holds (or does not hold -
            see 'exclude') for members of the group.
        valueRange: The value of the trait that holds (or does not hold - see
            'exclude') for members of the group.
        exclude: If true, indicates the characteristic is one that is NOT held
            by members of the group.
        period: The period over which the characteristic is tested; e.g. the
            patient had an operation during the month of June.
    """

    __name__ = 'Group_Characteristic'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.valueCodeableConcept = None
        # reference to CodeableConcept

        self.valueBoolean = None
        # type: bool

        self.valueQuantity = None
        # reference to Quantity

        self.valueRange = None
        # reference to Range

        self.exclude = None
        # type: bool

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'code'},
        ]


class Group_Member(fhirbase):
    """
    Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.

    Args:
        entity: A reference to the entity that is a member of the group. Must
            be consistent with Group.type.
        period: The period that the member was in the group, if known.
        inactive: A flag to indicate that the member is no longer in the
            group, but previously may have been a member.
    """

    __name__ = 'Group_Member'

    def __init__(self, dict_values=None):
        self.entity = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.inactive = None
        # type: bool

        self.object_id = None
        # unique identifier for object class

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
