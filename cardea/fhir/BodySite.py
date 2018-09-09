from .fhirbase import fhirbase


class BodySite(fhirbase):
    """Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """

    __name__ = 'BodySite'

    def __init__(self, dict_values=None):
        # this is a bodysite resource
        self.resourceType = 'BodySite'
        # type = string
        # possible values: BodySite

        # whether this body site is in active use.
        self.active = None
        # type = boolean

        # named anatomical location - ideally coded where possible.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # qualifier to refine the anatomical location.  these include qualifiers
        # for laterality, relative location, directionality, number, and plane.
        self.qualifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a summary, charactarization or explanation of the anatomic location.
        self.description = None
        # type = string

        # image or images used to identify a location.
        self.image = None
        # type = array
        # reference to Attachment: Attachment

        # the person to which the body site belongs.
        self.patient = None
        # reference to Reference: identifier

        # identifier for this instance of the anatomical location.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'BodySite',
             'child_variable': 'patient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'qualifier'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'image'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'code'},
        ]
