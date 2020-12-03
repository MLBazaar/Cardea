from .fhirbase import fhirbase


class Basic(fhirbase):
    """
    Basic is used for handling concepts not yet defined in FHIR,
    narrative-only resources that don't map to an existing resource, and
    custom resources not appropriate for inclusion in the FHIR
    specification.

    Args:
        resourceType: This is a Basic resource
        identifier: Identifier assigned to the resource for business purposes,
            outside the context of FHIR.
        code: Identifies the 'type' of resource - equivalent to the resource
            name for other resources.
        subject: Identifies the patient, practitioner, device or any other
            resource that is the "focus" of this resource.
        created: Identifies when the resource was first created.
        author: Indicates who was responsible for creating the resource
            instance.
    """

    __name__ = 'Basic'

    def __init__(self, dict_values=None):
        self.resourceType = 'Basic'
        # type: str
        # possible values: Basic

        self.code = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.created = None
        # type: str

        self.author = None
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Basic',
             'child_variable': 'author'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Basic',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Basic',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Basic',
             'child_variable': 'identifier'},
        ]
