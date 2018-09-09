from .fhirbase import fhirbase


class Media(fhirbase):
    """A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """

    __name__ = 'Media'

    def __init__(self, dict_values=None):
        # this is a media resource
        self.resourceType = 'Media'
        # type = string
        # possible values: Media

        # a procedure that is fulfilled in whole or in part by the creation of
        # this media.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # whether the media is a photo (still image), an audio recording, or a
        # video recording.
        self.type = None
        # type = string
        # possible values: photo, video, audio

        # details of the type of the media - usually, how it was acquired (what
        # type of device). if images sourced from a dicom system, are wrapped in a
        # media resource, then this is the modality.
        self.subtype = None
        # reference to CodeableConcept: CodeableConcept

        # the name of the imaging view e.g. lateral or antero-posterior (ap).
        self.view = None
        # reference to CodeableConcept: CodeableConcept

        # who/what this media is a record of.
        self.subject = None
        # reference to Reference: identifier

        # the encounter or episode of care that establishes the context for this
        # media.
        self.context = None
        # reference to Reference: identifier

        # the date and time(s) at which the media was collected.
        self.occurrenceDateTime = None
        # type = string

        # the date and time(s) at which the media was collected.
        self.occurrencePeriod = None
        # reference to Period: Period

        # the person who administered the collection of the image.
        self.operator = None
        # reference to Reference: identifier

        # describes why the event occurred in coded or textual form.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates the site on the subject's body where the media was collected
        # (i.e. the target site).
        self.bodySite = None
        # reference to CodeableConcept: CodeableConcept

        # the device used to collect the media.
        self.device = None
        # reference to Reference: identifier

        # height of the image in pixels (photo/video).
        self.height = None
        # type = int

        # width of the image in pixels (photo/video).
        self.width = None
        # type = int

        # the number of frames in a photo. this is used with a multi-page fax, or
        # an imaging acquisition context that takes multiple slices in a single
        # image, or an animated gif. if there is more than one frame, this shall
        # have a value in order to alert interface software that a multi-frame
        # capable rendering widget is required.
        self.frames = None
        # type = int

        # the duration of the recording in seconds - for audio and video.
        self.duration = None
        # type = int

        # the actual content of the media - inline or by direct reference to the
        # media source file.
        self.content = None
        # reference to Attachment: Attachment

        # comments made about the media by the performer, subject or other
        # participants.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # identifiers associated with the image - these may include identifiers
        # for the image itself, identifiers for the context of its collection
        # (e.g. series ids) and context ids such as accession numbers or other
        # workflow identifiers.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'operator'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'view'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'device'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'subtype'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'content'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Media',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Media',
             'child_variable': 'basedOn'},
        ]
