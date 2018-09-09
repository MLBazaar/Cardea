from .fhirbase import fhirbase


class BodySite(fhirbase):
    """
    Record details about the anatomical location of a specimen or body
    part.  This resource may be used when a coded concept does not provide
    the necessary detail needed for the use case.
    """

    __name__ = 'BodySite'

    def __init__(self, dict_values=None):
        self.resourceType = 'BodySite'
        """
        This is a BodySite resource

        type: string
        possible values: BodySite
        """

        self.active = None
        """
        Whether this body site is in active use.

        type: boolean
        """

        self.code = None
        """
        Named anatomical location - ideally coded where possible.

        reference to CodeableConcept
        """

        self.qualifier = None
        """
        Qualifier to refine the anatomical location.  These include qualifiers
        for laterality, relative location, directionality, number, and plane.

        type: array
        reference to CodeableConcept
        """

        self.description = None
        """
        A summary, charactarization or explanation of the anatomic location.

        type: string
        """

        self.image = None
        """
        Image or images used to identify a location.

        type: array
        reference to Attachment
        """

        self.patient = None
        """
        The person to which the body site belongs.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifier for this instance of the anatomical location.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'code'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'image'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'BodySite',
             'child_variable': 'qualifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'BodySite',
             'child_variable': 'patient'},
        ]
