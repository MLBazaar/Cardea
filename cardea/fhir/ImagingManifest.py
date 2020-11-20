from .fhirbase import fhirbase


class ImagingManifest(fhirbase):
    """
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.

    Args:
        resourceType: This is a ImagingManifest resource
        identifier: Unique identifier of the DICOM Key Object Selection (KOS)
            that this resource represents.
        patient: A patient resource reference which is the patient subject of
            all DICOM SOP Instances in this ImagingManifest.
        authoringTime: Date and time when the selection of the referenced
            instances were made. It is (typically) different from the creation
            date of the selection resource, and from dates associated with the
            referenced instances (e.g. capture time of the referenced image).
        author: Author of ImagingManifest. It can be a human author or a
            device which made the decision of the SOP instances selected. For
            example, a radiologist selected a set of imaging SOP instances to
            attach in a diagnostic report, and a CAD application may author a
            selection to describe SOP instances it used to generate a detection
            conclusion.
        description: Free text narrative description of the ImagingManifest.
            The value may be derived from the DICOM Standard Part 16, CID-7010
            descriptions (e.g. Best in Set, Complete Study Content). Note that
            those values cover the wide range of uses of the DICOM Key Object
            Selection object, several of which are not supported by
            ImagingManifest. Specifically, there is no expected behavior
            associated with descriptions that suggest referenced images be removed
            or not used.
        study: Study identity and locating information of the DICOM SOP
            instances in the selection.
    """

    __name__ = 'ImagingManifest'

    def __init__(self, dict_values=None):
        self.resourceType = 'ImagingManifest'
        # type: str
        # possible values: ImagingManifest

        self.patient = None
        # reference to Reference: identifier

        self.authoringTime = None
        # type: str

        self.author = None
        # reference to Reference: identifier

        self.description = None
        # type: str

        self.study = None
        # type: list
        # reference to ImagingManifest_Study

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingManifest',
             'child_variable': 'author'},

            {'parent_entity': 'ImagingManifest_Study',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingManifest',
             'child_variable': 'study'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingManifest',
             'child_variable': 'patient'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingManifest',
             'child_variable': 'identifier'},
        ]


class ImagingManifest_Study(fhirbase):
    """
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.

    Args:
        uid: Study instance UID of the SOP instances in the selection.
        imagingStudy: Reference to the Imaging Study in FHIR form.
        endpoint: The network service providing access (e.g., query, view, or
            retrieval) for the study. See implementation notes for information
            about using DICOM endpoints. A study-level endpoint applies to each
            series in the study, unless overridden by a series-level endpoint with
            the same Endpoint.type.
        series: Series identity and locating information of the DICOM SOP
            instances in the selection.
    """

    __name__ = 'ImagingManifest_Study'

    def __init__(self, dict_values=None):
        self.uid = None
        # type: str

        self.imagingStudy = None
        # reference to Reference: identifier

        self.endpoint = None
        # type: list
        # reference to Reference: identifier

        self.series = None
        # type: list
        # reference to ImagingManifest_Series

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingManifest_Study',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingManifest_Study',
             'child_variable': 'imagingStudy'},

            {'parent_entity': 'ImagingManifest_Series',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingManifest_Study',
             'child_variable': 'series'},
        ]


class ImagingManifest_Series(fhirbase):
    """
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.

    Args:
        uid: Series instance UID of the SOP instances in the selection.
        endpoint: The network service providing access (e.g., query, view, or
            retrieval) for this series. See implementation notes for information
            about using DICOM endpoints. A series-level endpoint, if present, has
            precedence over a study-level endpoint with the same Endpoint.type.
        instance: Identity and locating information of the selected DICOM SOP
            instances.
    """

    __name__ = 'ImagingManifest_Series'

    def __init__(self, dict_values=None):
        self.uid = None
        # type: str

        self.endpoint = None
        # type: list
        # reference to Reference: identifier

        self.instance = None
        # type: list
        # reference to ImagingManifest_Instance

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ImagingManifest_Instance',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingManifest_Series',
             'child_variable': 'instance'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingManifest_Series',
             'child_variable': 'endpoint'},
        ]


class ImagingManifest_Instance(fhirbase):
    """
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.

    Args:
        sopClass: SOP class UID of the selected instance.
        uid: SOP Instance UID of the selected instance.
    """

    __name__ = 'ImagingManifest_Instance'

    def __init__(self, dict_values=None):
        self.sopClass = None
        # type: str

        self.uid = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
