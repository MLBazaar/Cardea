from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Reference import Reference

class Basic(fhirbase):
    """Basic is used for handling concepts not yet defined in FHIR, narrative-
    only resources that don't map to an existing resource, and custom
    resources not appropriate for inclusion in the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # this is a basic resource
        self.resourceType = 'Basic'
        # type = string
        # possible values = Basic

        # identifies the 'type' of resource - equivalent to the resource name for
        # other resources.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the patient, practitioner, device or any other resource that
        # is the "focus" of this resource.
        self.subject = None
        # reference to Reference: identifier

        # identifies when the resource was first created.
        self.created = None
        # type = string

        # indicates who was responsible for creating the resource instance.
        self.author = None
        # reference to Reference: identifier

        # identifier assigned to the resource for business purposes, outside the
        # context of fhir.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
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

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Basic',
            'child_variable': 'author'},
        ]

