from .fhirbase import fhirbase


class Reference(fhirbase):
    """
    A reference from one resource to another.

    Args:
        reference: A reference to a location at which the other resource is
            found. The reference may be a relative reference, in which case it is
            relative to the service base URL, or an absolute URL that resolves to
            the location where the resource is found. The reference may be version
            specific or not. If the reference is not to a FHIR RESTful server,
            then it should be assumed to be version specific. Internal fragment
            references (start with '#') refer to contained resources.
        identifier: An identifier for the other resource. This is used when
            there is no way to reference the other resource directly, either
            because the entity is not available through a FHIR server, or because
            there is no way for the author of the resource to convert a known
            identifier to an actual location. There is no requirement that a
            Reference.identifier point to something that is actually exposed as a
            FHIR instance, but it SHALL point to a business concept that would be
            expected to be exposed as a FHIR instance, and that instance would
            need to be of a FHIR resource type allowed by the reference.
        display: Plain text narrative that identifies the resource in addition
            to the resource reference.
    """

    __name__ = 'Reference'

    def __init__(self, dict_values=None):
        self.reference = None
        # type: str

        self.display = None
        # type: str

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Reference',
             'child_variable': 'identifier'},
        ]
