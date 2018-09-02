from .fhirbase import fhirbase


class Contributor(fhirbase):
    """A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """

    def __init__(self, dict_values=None):
        # the type of contributor.
        self.type = None
        # type = string
        # possible values: author, editor, reviewer, endorser

        # the name of the individual or organization responsible for the
        # contribution.
        self.name = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # contributor.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'author', 'editor', 'reviewer', 'endorser']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'author, editor, reviewer, endorser'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Contributor',
             'child_variable': 'contact'},
        ]
