from .fhirbase import * 
from .Meta import Meta

class Resource(fhirbase):
    """This is the base resource type for everything.
    """

    def __init__(self, dict_values=None):
        # the metadata about the resource. this is content that is maintained by
        # the infrastructure. changes to the content may not always be associated
        # with version changes to the resource.
        self.meta = None
        # reference to Meta: Meta

        # a reference to a set of rules that were followed when the resource was
        # constructed, and which must be understood when processing the content.
        self.implicitRules = None
        # type = string

        # the base language in which the resource is written.
        self.language = None
        # type = string

        # the logical id of the resource, as used in the url for the resource.
        # once assigned, this value never changes.
        self.id = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Meta',
            'parent_variable': 'object_id',
            'child_entity': 'Resource',
            'child_variable': 'meta'},
        ]

