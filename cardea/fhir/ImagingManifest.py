from .fhirbase import fhirbase


class ImagingManifest(fhirbase):
    """A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """

    def __init__(self, dict_values=None):
        # this is a imagingmanifest resource
        self.resourceType = 'ImagingManifest'
        # type = string
        # possible values: ImagingManifest

        # a patient resource reference which is the patient subject of all dicom
        # sop instances in this imagingmanifest.
        self.patient = None
        # reference to Reference: identifier

        # date and time when the selection of the referenced instances were made.
        # it is (typically) different from the creation date of the selection
        # resource, and from dates associated with the referenced instances (e.g.
        # capture time of the referenced image).
        self.authoringTime = None
        # type = string

        # author of imagingmanifest. it can be a human author or a device which
        # made the decision of the sop instances selected. for example, a
        # radiologist selected a set of imaging sop instances to attach in a
        # diagnostic report, and a cad application may author a selection to
        # describe sop instances it used to generate a detection conclusion.
        self.author = None
        # reference to Reference: identifier

        # free text narrative description of the imagingmanifest.   the value may
        # be derived from the dicom standard part 16, cid-7010 descriptions (e.g.
        # best in set, complete study content). note that those values cover the
        # wide range of uses of the dicom key object selection object, several of
        # which are not supported by imagingmanifest. specifically, there is no
        # expected behavior associated with descriptions that suggest referenced
        # images be removed or not used.
        self.description = None
        # type = string

        # study identity and locating information of the dicom sop instances in
        # the selection.
        self.study = None
        # type = array
        # reference to ImagingManifest_Study: ImagingManifest_Study

        # unique identifier of the dicom key object selection (kos) that this
        # resource represents.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

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
    """A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """

    def __init__(self, dict_values=None):
        # study instance uid of the sop instances in the selection.
        self.uid = None
        # type = string

        # reference to the imaging study in fhir form.
        self.imagingStudy = None
        # reference to Reference: identifier

        # the network service providing access (e.g., query, view, or retrieval)
        # for the study. see implementation notes for information about using
        # dicom endpoints. a study-level endpoint applies to each series in the
        # study, unless overridden by a series-level endpoint with the same
        # endpoint.type.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # series identity and locating information of the dicom sop instances in
        # the selection.
        self.series = None
        # type = array
        # reference to ImagingManifest_Series: ImagingManifest_Series

        # unique identifier for object class
        self.object_id = None

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
    """A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """

    def __init__(self, dict_values=None):
        # series instance uid of the sop instances in the selection.
        self.uid = None
        # type = string

        # the network service providing access (e.g., query, view, or retrieval)
        # for this series. see implementation notes for information about using
        # dicom endpoints. a series-level endpoint, if present, has precedence
        # over a study-level endpoint with the same endpoint.type.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # identity and locating information of the selected dicom sop instances.
        self.instance = None
        # type = array
        # reference to ImagingManifest_Instance: ImagingManifest_Instance

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingManifest_Series',
             'child_variable': 'endpoint'},

            {'parent_entity': 'ImagingManifest_Instance',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingManifest_Series',
             'child_variable': 'instance'},
        ]


class ImagingManifest_Instance(fhirbase):
    """A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """

    def __init__(self, dict_values=None):
        # sop class uid of the selected instance.
        self.sopClass = None
        # type = string

        # sop instance uid of the selected instance.
        self.uid = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
