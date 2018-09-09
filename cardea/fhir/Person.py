from .fhirbase import fhirbase


class Person(fhirbase):
    """
    Demographics and administrative information about a person independent
    of a specific health-related context.
    """

    __name__ = 'Person'

    def __init__(self, dict_values=None):
        self.resourceType = 'Person'
        """
        This is a Person resource

        type: string
        possible values: Person
        """

        self.name = None
        """
        A name associated with the person.

        type: array
        reference to HumanName
        """

        self.telecom = None
        """
        A contact detail for the person, e.g. a telephone number or an email
        address.

        type: array
        reference to ContactPoint
        """

        self.gender = None
        """
        Administrative Gender.

        type: string
        possible values: male, female, other, unknown
        """

        self.birthDate = None
        """
        The birth date for the person.

        type: string
        """

        self.address = None
        """
        One or more addresses for the person.

        type: array
        reference to Address
        """

        self.photo = None
        """
        An image that can be displayed as a thumbnail of the person to enhance
        the identification of the individual.

        reference to Attachment
        """

        self.managingOrganization = None
        """
        The organization that is the custodian of the person record.

        reference to Reference: identifier
        """

        self.active = None
        """
        Whether this person's record is in active use.

        type: boolean
        """

        self.link = None
        """
        Link to a resource that concerns the same actual person.

        type: array
        reference to Person_Link
        """

        self.identifier = None
        """
        Identifier for a person within a particular scope.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.gender is not None:
            for value in self.gender:
                if value is not None and value.lower() not in [
                        'male', 'female', 'other', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'male, female, other, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Person',
             'child_variable': 'managingOrganization'},

            {'parent_entity': 'ContactPoint',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'telecom'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'identifier'},

            {'parent_entity': 'Person_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'link'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'photo'},

            {'parent_entity': 'HumanName',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'name'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Person',
             'child_variable': 'address'},
        ]


class Person_Link(fhirbase):
    """
    Demographics and administrative information about a person independent
    of a specific health-related context.
    """

    __name__ = 'Person_Link'

    def __init__(self, dict_values=None):
        self.target = None
        """
        The resource to which this actual person is associated.

        reference to Reference: identifier
        """

        self.assurance = None
        """
        Level of assurance that this link is actually associated with the
        target resource.

        type: string
        possible values: level1, level2, level3, level4
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
