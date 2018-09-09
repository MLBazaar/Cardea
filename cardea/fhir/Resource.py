from .fhirbase import fhirbase


class Resource(fhirbase):
    """
    This is the base resource type for everything.
    """

    __name__ = 'Resource'

    def __init__(self, dict_values=None):
        self.meta = None
        """
        The metadata about the resource. This is content that is maintained by
        the infrastructure. Changes to the content may not always be
        associated with version changes to the resource.

        reference to Meta
        """

        self.implicitRules = None
        """
        A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content.

        type: string
        """

        self.language = None
        """
        The base language in which the resource is written.

        type: string
        """

        self.id = None
        """
        The logical id of the resource, as used in the URL for the resource.
        Once assigned, this value never changes.

        type: string
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Meta',
             'parent_variable': 'object_id',
             'child_entity': 'Resource',
             'child_variable': 'meta'},
        ]
