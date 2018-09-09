from .fhirbase import fhirbase


class Reference(fhirbase):
    """A reference from one resource to another.
    """

    __name__ = 'Reference'

    def __init__(self, dict_values=None):
        # a reference to a location at which the other resource is found. the
        # reference may be a relative reference, in which case it is relative to
        # the service base url, or an absolute url that resolves to the location
        # where the resource is found. the reference may be version specific or
        # not. if the reference is not to a fhir restful server, then it should be
        # assumed to be version specific. internal fragment references (start with
        # '#') refer to contained resources.
        self.reference = None
        # type = string

        # plain text narrative that identifies the resource in addition to the
        # resource reference.
        self.display = None
        # type = string

        # an identifier for the other resource. this is used when there is no way
        # to reference the other resource directly, either because the entity is
        # not available through a fhir server, or because there is no way for the
        # author of the resource to convert a known identifier to an actual
        # location. there is no requirement that a reference.identifier point to
        # something that is actually exposed as a fhir instance, but it shall
        # point to a business concept that would be expected to be exposed as a
        # fhir instance, and that instance would need to be of a fhir resource
        # type allowed by the reference.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Reference',
             'child_variable': 'identifier'},
        ]
