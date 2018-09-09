from .fhirbase import fhirbase


class Media(fhirbase):
    """
    A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    __name__ = 'Media'

    def __init__(self, dict_values=None):
        self.resourceType = 'Media'
        """
        This is a Media resource

        type: string
        possible values: Media
        """

        self.basedOn = None
        """
        A procedure that is fulfilled in whole or in part by the creation of
        this media.

        type: array
        reference to Reference: identifier
        """

        self.type = None
        """
        Whether the media is a photo (still image), an audio recording, or a
        video recording.

        type: string
        possible values: photo, video, audio
        """

        self.subtype = None
        """
        Details of the type of the media - usually, how it was acquired (what
        type of device). If images sourced from a DICOM system, are wrapped in
        a Media resource, then this is the modality.

        reference to CodeableConcept
        """

        self.view = None
        """
        The name of the imaging view e.g. Lateral or Antero-posterior (AP).

        reference to CodeableConcept
        """

        self.subject = None
        """
        Who/What this Media is a record of.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter or episode of care that establishes the context for this
        media.

        reference to Reference: identifier
        """

        self.occurrenceDateTime = None
        """
        The date and time(s) at which the media was collected.

        type: string
        """

        self.occurrencePeriod = None
        """
        The date and time(s) at which the media was collected.

        reference to Period
        """

        self.operator = None
        """
        The person who administered the collection of the image.

        reference to Reference: identifier
        """

        self.reasonCode = None
        """
        Describes why the event occurred in coded or textual form.

        type: array
        reference to CodeableConcept
        """

        self.bodySite = None
        """
        Indicates the site on the subject's body where the media was collected
        (i.e. the target site).

        reference to CodeableConcept
        """

        self.device = None
        """
        The device used to collect the media.

        reference to Reference: identifier
        """

        self.height = None
        """
        Height of the image in pixels (photo/video).

        type: int
        """

        self.width = None
        """
        Width of the image in pixels (photo/video).

        type: int
        """

        self.frames = None
        """
        The number of frames in a photo. This is used with a multi-page fax,
        or an imaging acquisition context that takes multiple slices in a
        single image, or an animated gif. If there is more than one frame,
        this SHALL have a value in order to alert interface software that a
        multi-frame capable rendering widget is required.

        type: int
        """

        self.duration = None
        """
        The duration of the recording in seconds - for audio and video.

        type: int
        """

        self.content = None
        """
        The actual content of the media - inline or by direct reference to the
        media source file.

        reference to Attachment
        """

        self.note = None
        """
        Comments made about the media by the performer, subject or other
        participants.

        type: array
        reference to Annotation
        """

        self.identifier = None
        """
        Identifiers associated with the image - these may include identifiers
        for the image itself, identifiers for the context of its collection
        (e.g. series ids) and context ids such as accession numbers or other
        workflow identifiers.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'photo', 'video', 'audio']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'photo, video, audio'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'device'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'view'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'subtype'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'operator'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'content'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'reasonCode'},
        ]
