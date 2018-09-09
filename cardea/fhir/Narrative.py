from .fhirbase import fhirbase


class Narrative(fhirbase):
    """A human-readable formatted text, including images.
    """

    def __init__(self, dict_values=None):
        # the status of the narrative - whether it's entirely generated (from just
        # the defined data or the extensions too), or whether a human authored it
        # and it may contain additional data.
        self.status = None
        # type = string
        # possible values: generated, extensions, additional, empty

        # the actual narrative content, a stripped down version of xhtml.
        self.div = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'generated', 'extensions', 'additional', 'empty']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'generated, extensions, additional, empty'))
