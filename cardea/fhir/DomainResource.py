from .fhirbase import fhirbase


class DomainResource(fhirbase):
    """
    A resource that includes narrative, extensions, and contained
    resources.

    Args:
        text: A human-readable narrative that contains a summary of the
            resource, and may be used to represent the content of the resource to
            a human. The narrative need not encode all the structured data, but is
            required to contain sufficient detail to make it "clinically safe" for
            a human to just read the narrative. Resource definitions may define
            what content should be represented in the narrative to ensure clinical
            safety.
        contained: These resources do not have an independent existence apart
            from the resource that contains them - they cannot be identified
            independently, and nor can they have their own independent transaction
            scope.
        extension: May be used to represent additional information that is not
            part of the basic definition of the resource. In order to make the use
            of extensions safe and manageable, there is a strict set of governance
            applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the
            extension.
        modifierExtension: May be used to represent additional information
            that is not part of the basic definition of the resource, and that
            modifies the understanding of the element that contains it. Usually
            modifier elements provide negation or qualification. In order to make
            the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the
            extension. Applications processing a resource are required to check
            for modifier extensions.
    """

    __name__ = 'DomainResource'

    def __init__(self, dict_values=None):
        self.text = None
        # reference to Narrative

        self.contained = None
        # type: list
        # reference to ResourceList

        self.extension = None
        # type: list
        # reference to Extension

        self.modifierExtension = None
        # type: list
        # reference to Extension

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'extension'},

            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'contained'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'text'},

            {'parent_entity': 'Extension',
             'parent_variable': 'object_id',
             'child_entity': 'DomainResource',
             'child_variable': 'modifierExtension'},
        ]
