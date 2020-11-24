from .fhirbase import fhirbase


class Meta(fhirbase):
    """
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not
    always be associated with version changes to the resource.

    Args:
        versionId: The version specific identifier, as it appears in the
            version portion of the URL. This values changes when the resource is
            created, updated, or deleted.
        lastUpdated: When the resource last changed - e.g. when the version
            changed.
        profile: A list of profiles (references to [[[StructureDefinition]]]
            resources) that this resource claims to conform to. The URL is a
            reference to [[[StructureDefinition.url]]].
        security: Security labels applied to this resource. These tags connect
            specific resources to the overall security policy and infrastructure.
        tag: Tags applied to this resource. Tags are intended to be used to
            identify and relate resources to process and workflow, and
            applications are not required to consider the tags when interpreting
            the meaning of a resource.
    """

    __name__ = 'Meta'

    def __init__(self, dict_values=None):
        self.versionId = None
        # type: str

        self.lastUpdated = None
        # type: str

        self.profile = None
        # type: list

        self.security = None
        # type: list
        # reference to Coding

        self.tag = None
        # type: list
        # reference to Coding

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Meta',
             'child_variable': 'tag'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Meta',
             'child_variable': 'security'},
        ]
