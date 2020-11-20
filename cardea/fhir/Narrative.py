from .fhirbase import fhirbase


class Narrative(fhirbase):
    """
    A human-readable formatted text, including images.

    Args:
        status: The status of the narrative - whether it's entirely generated
            (from just the defined data or the extensions too), or whether a human
            authored it and it may contain additional data.
        div: The actual narrative content, a stripped down version of XHTML.
    """

    __name__ = 'Narrative'

    def __init__(self, dict_values=None):
        self.status = None
        # type: str
        # possible values: generated, extensions, additional, empty

        self.div = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'generated', 'extensions', 'additional', 'empty']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'generated, extensions, additional, empty'))
