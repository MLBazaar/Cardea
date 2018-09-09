from .fhirbase import fhirbase


class DomainResource(fhirbase):
    """A resource that includes narrative, extensions, and contained resources.
    """

    __name__ = 'DomainResource'

    def __init__(self, dict_values=None):
        # a human-readable narrative that contains a summary of the resource, and
        # may be used to represent the content of the resource to a human. the
        # narrative need not encode all the structured data, but is required to
        # contain sufficient detail to make it "clinically safe" for a human to
        # just read the narrative. resource definitions may define what content
        # should be represented in the narrative to ensure clinical safety.
        self.text = None
        # reference to Narrative: Narrative

        # these resources do not have an independent existence apart from the
        # resource that contains them - they cannot be identified independently,
        # and nor can they have their own independent transaction scope.
        self.contained = None
        # type = array
        # reference to ResourceList: ResourceList

        # may be used to represent additional information that is not part of the
        # basic definition of the resource. in order to make the use of extensions
        # safe and manageable, there is a strict set of governance  applied to the
        # definition and use of extensions. though any implementer is allowed to
        # define an extension, there is a set of requirements that shall be met as
        # part of the definition of the extension.
        self.extension = None
        # type = array
        # reference to Extension: Extension

        # may be used to represent additional information that is not part of the
        # basic definition of the resource, and that modifies the understanding of
        # the element that contains it. usually modifier elements provide negation
        # or qualification. in order to make the use of extensions safe and
        # manageable, there is a strict set of governance applied to the
        # definition and use of extensions. though any implementer is allowed to
        # define an extension, there is a set of requirements that shall be met as
        # part of the definition of the extension. applications processing a
        # resource are required to check for modifier extensions.
        self.modifierExtension = None
        # type = array
        # reference to Extension: Extension

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'modifierExtension'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'text'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'extension'},

            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'contained'},
        ]
