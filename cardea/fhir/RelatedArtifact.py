from .fhirbase import fhirbase


class RelatedArtifact(fhirbase):
    """Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """

    __name__ = 'RelatedArtifact'

    def __init__(self, dict_values=None):
        # the type of relationship to the related artifact.
        self.type = None
        # type = string
        # possible values: documentation, justification, citation,
        # predecessor, successor, derived-from, depends-on, composed-of

        # a brief description of the document or knowledge resource being
        # referenced, suitable for display to a consumer.
        self.display = None
        # type = string

        # a bibliographic citation for the related artifact. this text should be
        # formatted according to an accepted citation format.
        self.citation = None
        # type = string

        # a url for the artifact that can be followed to access the actual
        # content.
        self.url = None
        # type = string

        # the document being referenced, represented as an attachment. this is
        # exclusive with the resource element.
        self.document = None
        # reference to Attachment: Attachment

        # the related resource, such as a library, value set, profile, or other
        # knowledge resource.
        self.resource = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'documentation', 'justification', 'citation', 'predecessor',
                        'successor', 'derived-from', 'depends-on', 'composed-of']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'documentation, justification, citation, predecessor,'
                        'successor, derived-from, depends-on, composed-of'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'RelatedArtifact',
             'child_variable': 'resource'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'RelatedArtifact',
             'child_variable': 'document'},
        ]
