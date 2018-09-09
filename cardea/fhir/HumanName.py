from .fhirbase import fhirbase


class HumanName(fhirbase):
    """
    A human's name with the ability to identify parts and usage.
    """

    __name__ = 'HumanName'

    def __init__(self, dict_values=None):
        self.use = None
        """
        Identifies the purpose for this name.

        type: string
        possible values: usual, official, temp, nickname, anonymous,
        old, maiden
        """

        self.text = None
        """
        A full text representation of the name.

        type: string
        """

        self.family = None
        """
        The part of a name that links to the genealogy. In some cultures (e.g.
        Eritrea) the family name of a son is the first name of his father.

        type: string
        """

        self.given = None
        """
        Given name.

        type: array
        """

        self.prefix = None
        """
        Part of the name that is acquired as a title due to academic, legal,
        employment or nobility status, etc. and that appears at the start of
        the name.

        type: array
        """

        self.suffix = None
        """
        Part of the name that is acquired as a title due to academic, legal,
        employment or nobility status, etc. and that appears at the end of the
        name.

        type: array
        """

        self.period = None
        """
        Indicates the period of time when this name was valid for the named
        person.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.use is not None:
            for value in self.use:
                if value is not None and value.lower() not in [
                        'usual', 'official', 'temp', 'nickname', 'anonymous', 'old', 'maiden']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'usual, official, temp, nickname, anonymous, old, maiden'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'HumanName',
             'child_variable': 'period'},
        ]
