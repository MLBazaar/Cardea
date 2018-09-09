from .fhirbase import fhirbase


class Identifier(fhirbase):
    """A technical identifier - identifies some entity uniquely and
    unambiguously.
    """

    __name__ = 'Identifier'

    def __init__(self, dict_values=None):
        # the purpose of this identifier.
        self.use = None
        # type = string
        # possible values: usual, official, temp, secondary

        # a coded type for the identifier that can be used to determine which
        # identifier to use for a specific purpose.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # establishes the namespace for the value - that is, a url that describes
        # a set values that are unique.
        self.system = None
        # type = string

        # the portion of the identifier typically relevant to the user and which
        # is unique within the context of the system.
        self.value = None
        # type = string

        # time period during which identifier is/was valid for use.
        self.period = None
        # reference to Period: Period

        # organization that issued/manages the identifier.
        self.assigner = None

        # unique identifier for object class
        self.object_id = None

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
