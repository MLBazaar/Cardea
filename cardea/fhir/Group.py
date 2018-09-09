from .fhirbase import fhirbase


class Group(fhirbase):
    """
    Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.
    """

    __name__ = 'Group'

    def __init__(self, dict_values=None):
        self.resourceType = 'Group'
        """
        This is a Group resource

        type: string
        possible values: Group
        """

        self.active = None
        """
        Indicates whether the record for the group is available for use or is
        merely being retained for historical purposes.

        type: boolean
        """

        self.type = None
        """
        Identifies the broad classification of the kind of resources the group
        includes.

        type: string
        possible values: person, animal, practitioner, device,
        medication, substance
        """

        self.actual = None
        """
        If true, indicates that the resource refers to a specific group of
        real individuals.  If false, the group defines a set of intended
        individuals.

        type: boolean
        """

        self.code = None
        """
        Provides a specific type of resource the group includes; e.g. "cow",
        "syringe", etc.

        reference to CodeableConcept
        """

        self.name = None
        """
        A label assigned to the group for human identification and
        communication.

        type: string
        """

        self.quantity = None
        """
        A count of the number of resource instances that are part of the
        group.

        type: int
        """

        self.characteristic = None
        """
        Identifies the traits shared by members of the group.

        type: array
        reference to Group_Characteristic
        """

        self.member = None
        """
        Identifies the resource instances that are members of the group.

        type: array
        reference to Group_Member
        """

        self.identifier = None
        """
        A unique business identifier for this group.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Group',
             'child_variable': 'identifier'},

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
        ]


class Group_Characteristic(fhirbase):
    """
    Represents a defined collection of entities that may be discussed or
    acted upon collectively but which are not expected to act collectively
    and are not formally or legally recognized; i.e. a collection of
    entities that isn't an Organization.
    """

    __name__ = 'Group_Characteristic'

    def __init__(self, dict_values=None):
        self.code = None
        """
        A code that identifies the kind of trait being asserted.

        reference to CodeableConcept
        """

        self.valueCodeableConcept = None
        """
        The value of the trait that holds (or does not hold - see 'exclude')
        for members of the group.

        reference to CodeableConcept
        """

        self.valueBoolean = None
        """
        The value of the trait that holds (or does not hold - see 'exclude')
        for members of the group.

        type: boolean
        """

        self.valueQuantity = None
        """
        The value of the trait that holds (or does not hold - see 'exclude')
        for members of the group.

        reference to Quantity
        """

        self.valueRange = None
        """
        The value of the trait that holds (or does not hold - see 'exclude')
        for members of the group.

        reference to Range
        """

        self.exclude = None
        """
        If true, indicates the characteristic is one that is NOT held by
        members of the group.

        type: boolean
        """

        self.period = None
        """
        The period over which the characteristic is tested; e.g. the patient
        had an operation during the month of June.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Group_Characteristic',
             'child_variable': 'period'},

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
    """

    __name__ = 'Group_Member'

    def __init__(self, dict_values=None):
        self.entity = None
        """
        A reference to the entity that is a member of the group. Must be
        consistent with Group.type.

        reference to Reference: identifier
        """

        self.period = None
        """
        The period that the member was in the group, if known.

        reference to Period
        """

        self.inactive = None
        """
        A flag to indicate that the member is no longer in the group, but
        previously may have been a member.

        type: boolean
        """

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
