from .fhirbase import * 
from .Period import Period

class HumanName(fhirbase):
    """A human's name with the ability to identify parts and usage.
    """

    def __init__(self, dict_values=None):
        # identifies the purpose for this name.
        self.use = None
        # type = string
        # possible values = usual, official, temp, nickname, anonymous, old, maiden

        # a full text representation of the name.
        self.text = None
        # type = string

        # the part of a name that links to the genealogy. in some cultures (e.g.
        # eritrea) the family name of a son is the first name of his father.
        self.family = None
        # type = string

        # given name.
        self.given = None
        # type = array

        # part of the name that is acquired as a title due to academic, legal,
        # employment or nobility status, etc. and that appears at the start of the
        # name.
        self.prefix = None
        # type = array

        # part of the name that is acquired as a title due to academic, legal,
        # employment or nobility status, etc. and that appears at the end of the
        # name.
        self.suffix = None
        # type = array

        # indicates the period of time when this name was valid for the named
        # person.
        self.period = None
        # reference to Period: Period


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.use is not None:
            for value in self.use:
                if value != None and value.lower() not in ['usual', 'official', 'temp', 'nickname', 'anonymous', 'old', 'maiden']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'usual, official, temp, nickname, anonymous, old, maiden'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'HumanName',
            'child_variable': 'period'},
        ]

