from .fhirbase import fhirbase


class BodySite(fhirbase):
    """
    Record details about the anatomical location of a specimen or body
    part.  This resource may be used when a coded concept does not provide
    the necessary detail needed for the use case.

    Args:
        resourceType: This is a BodySite resource
        identifier: Identifier for this instance of the anatomical location.
        active: Whether this body site is in active use.
        code: Named anatomical location - ideally coded where possible.
        qualifier: Qualifier to refine the anatomical location.  These include
            qualifiers for laterality, relative location, directionality, number,
            and plane.
        description: A summary, charactarization or explanation of the
            anatomic location.
        image: Image or images used to identify a location.
        patient: The person to which the body site belongs.
    """

    __name__ = 'BodySite'

    def __init__(self, dict_values=None):
        self.resourceType = 'BodySite'
        # type: str
        # possible values: BodySite

        self.active = None
        # type: bool

        self.code = None
        # reference to CodeableConcept

        self.qualifier = None
        # type: list
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.image = None
        # type: list
        # reference to Attachment

        self.patient = None
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
             'child_entity': 'BodySite',
             'child_variable': 'patient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'qualifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'identifier'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'image'},
        ]
