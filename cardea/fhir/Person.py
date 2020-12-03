from .fhirbase import fhirbase


class Person(fhirbase):
    """
    Demographics and administrative information about a person independent
    of a specific health-related context.

    Args:
        resourceType: This is a Person resource
        identifier: Identifier for a person within a particular scope.
        name: A name associated with the person.
        telecom: A contact detail for the person, e.g. a telephone number or
            an email address.
        gender: Administrative Gender.
        birthDate: The birth date for the person.
        address: One or more addresses for the person.
        photo: An image that can be displayed as a thumbnail of the person to
            enhance the identification of the individual.
        managingOrganization: The organization that is the custodian of the
            person record.
        active: Whether this person's record is in active use.
        link: Link to a resource that concerns the same actual person.
    """

    __name__ = 'Person'

    def __init__(self, dict_values=None):
        self.resourceType = 'Person'
        # type: str
        # possible values: Person

        self.name = None
        # type: list
        # reference to HumanName

        self.telecom = None
        # type: list
        # reference to ContactPoint

        self.gender = None
        # type: str
        # possible values: male, female, other, unknown

        self.birthDate = None
        # type: str

        self.address = None
        # type: list
        # reference to Address

        self.photo = None
        # reference to Attachment

        self.managingOrganization = None
        # reference to Reference: identifier

        self.active = None
        # type: bool

        self.link = None
        # type: list
        # reference to Person_Link

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.gender is not None:
            for value in self.gender:
                if value is not None and value.lower() not in [
                        'male', 'female', 'other', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'male, female, other, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'name'},

            {'parent_entity': 'Person_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'link'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'telecom'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Person',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'identifier'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'address'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'photo'},
        ]


class Person_Link(fhirbase):
    """
    Demographics and administrative information about a person independent
    of a specific health-related context.

    Args:
        target: The resource to which this actual person is associated.
        assurance: Level of assurance that this link is actually associated
            with the target resource.
    """

    __name__ = 'Person_Link'

    def __init__(self, dict_values=None):
        self.target = None
        # reference to Reference: identifier

        self.assurance = None
        # type: str
        # possible values: level1, level2, level3, level4

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.assurance is not None:
            for value in self.assurance:
                if value is not None and value.lower() not in [
                        'level1', 'level2', 'level3', 'level4']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'level1, level2, level3, level4'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Person_Link',
             'child_variable': 'target'},
        ]
