from .fhirbase import fhirbase


class Meta(fhirbase):
    """The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always
    be associated with version changes to the resource.
    """

    __name__ = 'Meta'

    def __init__(self, dict_values=None):
        # the version specific identifier, as it appears in the version portion of
        # the url. this values changes when the resource is created, updated, or
        # deleted.
        self.versionId = None
        # type = string

        # when the resource last changed - e.g. when the version changed.
        self.lastUpdated = None
        # type = string

        # a list of profiles (references to [[[structuredefinition]]] resources)
        # that this resource claims to conform to. the url is a reference to
        # [[[structuredefinition.url]]].
        self.profile = None
        # type = array

        # security labels applied to this resource. these tags connect specific
        # resources to the overall security policy and infrastructure.
        self.security = None
        # type = array
        # reference to Coding: Coding

        # tags applied to this resource. tags are intended to be used to identify
        # and relate resources to process and workflow, and applications are not
        # required to consider the tags when interpreting the meaning of a
        # resource.
        self.tag = None
        # type = array
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Meta',
             'child_variable': 'security'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Meta',
             'child_variable': 'tag'},
        ]
