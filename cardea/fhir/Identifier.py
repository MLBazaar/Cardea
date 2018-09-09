from .fhirbase import fhirbase


class Identifier(fhirbase):
    """
    A technical identifier - identifies some entity uniquely and
    unambiguously.
    """

    __name__ = 'Identifier'

    def __init__(self, dict_values=None):
        self.use = None
        """
        The purpose of this identifier.

        type: string
        possible values: usual, official, temp, secondary
        """

        self.type = None
        """
        A coded type for the identifier that can be used to determine which
        identifier to use for a specific purpose.

        reference to CodeableConcept
        """

        self.system = None
        """
        Establishes the namespace for the value - that is, a URL that
        describes a set values that are unique.

        type: string
        """

        self.value = None
        """
        The portion of the identifier typically relevant to the user and which
        is unique within the context of the system.

        type: string
        """

        self.period = None
        """
        Time period during which identifier is/was valid for use.

        reference to Period
        """

        self.assigner = None
        """
        Organization that issued/manages the identifier.

        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.use is not None:
            for value in self.use:
                if value is not None and value.lower() not in [
                        'usual', 'official', 'temp', 'secondary']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'usual, official, temp, secondary'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Identifier',
             'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Identifier',
             'child_variable': 'type'},
        ]
