from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Reference import Reference
from .Coding import Coding

class ImagingStudy(fhirbase):
    """Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-
    Object Pair Instances (SOP Instances - images or other data) acquired or
    produced in a common context.  A series is of only one modality (e.g.
    X-ray, CT, MR, ultrasound), but a study may have multiple series of
    different modalities.
    """

    def __init__(self, dict_values=None):
        # this is a imagingstudy resource
        self.resourceType = 'ImagingStudy'
        # type = string
        # possible values = ImagingStudy

        # formal identifier for the study.
        self.uid = None
        # type = string

        # accession number is an identifier related to some aspect of imaging
        # workflow and data management. usage may vary across different
        # institutions.  see for instance [ihe radiology technical framework
        # volume 1 appendix
        # a](http://www.ihe.net/uploadedfiles/documents/radiology/ihe_rad_tf_rev13.0_vol1_ft_2014-07-30.pdf).
        self.accession = None
        # reference to Identifier: Identifier

        # availability of study (online, offline, or nearline).
        self.availability = None
        # type = string
        # possible values = ONLINE, OFFLINE, NEARLINE, UNAVAILABLE

        # a list of all the series.imagemodality values that are actual
        # acquisition modalities, i.e. those in the dicom context group 29 (value
        # set oid 1.2.840.10008.6.1.19).
        self.modalityList = None
        # type = array
        # reference to Coding: Coding

        # the patient imaged in the study.
        self.patient = None
        # reference to Reference: identifier

        # the encounter or episode at which the request is initiated.
        self.context = None
        # reference to Reference: identifier

        # date and time the study started.
        self.started = None
        # type = string

        # a list of the diagnostic requests that resulted in this imaging study
        # being performed.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # the requesting/referring physician.
        self.referrer = None
        # reference to Reference: identifier

        # who read the study and interpreted the images or other content.
        self.interpreter = None
        # type = array
        # reference to Reference: identifier

        # the network service providing access (e.g., query, view, or retrieval)
        # for the study. see implementation notes for information about using
        # dicom endpoints. a study-level endpoint applies to each series in the
        # study, unless overridden by a series-level endpoint with the same
        # endpoint.type.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # number of series in the study. this value given may be larger than the
        # number of series elements this resource contains due to resource
        # availability, security, or other factors. this element should be present
        # if any series elements are present.
        self.numberOfSeries = None
        # type = int

        # number of sop instances in study. this value given may be larger than
        # the number of instance elements this resource contains due to resource
        # availability, security, or other factors. this element should be present
        # if any instance elements are present.
        self.numberOfInstances = None
        # type = int

        # a reference to the performed procedure.
        self.procedureReference = None
        # type = array
        # reference to Reference: identifier

        # the code for the performed procedure type.
        self.procedureCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # description of clinical condition indicating why the imagingstudy was
        # requested.
        self.reason = None
        # reference to CodeableConcept: CodeableConcept

        # institution-generated description or classification of the study
        # performed.
        self.description = None
        # type = string

        # each study has one or more series of images or other content.
        self.series = None
        # type = array
        # reference to ImagingStudy_Series: ImagingStudy_Series

        # other identifiers for the study.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.availability is not None:
            for value in self.availability:
                if value != None and value.lower() not in ['online', 'offline', 'nearline', 'unavailable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'online, offline, nearline, unavailable'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy',
            'child_variable': 'identifier'},

            {'parent_entity': 'ImagingStudy_Series',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy',
            'child_variable': 'series'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy',
            'child_variable': 'basedOn'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy',
            'child_variable': 'accession'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy',
            'child_variable': 'procedureReference'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy',
            'child_variable': 'endpoint'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy',
            'child_variable': 'procedureCode'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy',
            'child_variable': 'referrer'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy',
            'child_variable': 'interpreter'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy',
            'child_variable': 'reason'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy',
            'child_variable': 'context'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy',
            'child_variable': 'patient'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy',
            'child_variable': 'modalityList'},
        ]

class ImagingStudy_Series(fhirbase):
    """Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-
    Object Pair Instances (SOP Instances - images or other data) acquired or
    produced in a common context.  A series is of only one modality (e.g.
    X-ray, CT, MR, ultrasound), but a study may have multiple series of
    different modalities.
    """

    def __init__(self, dict_values=None):
        # formal identifier for this series.
        self.uid = None
        # type = string

        # the numeric identifier of this series in the study.
        self.number = None
        # type = int

        # the modality of this series sequence.
        self.modality = None
        # reference to Coding: Coding

        # a description of the series.
        self.description = None
        # type = string

        # number of sop instances in the study. the value given may be larger than
        # the number of instance elements this resource contains due to resource
        # availability, security, or other factors. this element should be present
        # if any instance elements are present.
        self.numberOfInstances = None
        # type = int

        # availability of series (online, offline or nearline).
        self.availability = None
        # type = string
        # possible values = ONLINE, OFFLINE, NEARLINE, UNAVAILABLE

        # the network service providing access (e.g., query, view, or retrieval)
        # for this series. see implementation notes for information about using
        # dicom endpoints. a series-level endpoint, if present, has precedence
        # over a study-level endpoint with the same endpoint.type.
        self.endpoint = None
        # type = array
        # reference to Reference: identifier

        # the anatomic structures examined. see dicom part 16 annex l
        # (http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_l.html)
        # for dicom to snomed-ct mappings. the bodysite may indicate the
        # laterality of body part imaged; if so, it shall be consistent with any
        # content of imagingstudy.series.laterality.
        self.bodySite = None
        # reference to Coding: Coding

        # the laterality of the (possibly paired) anatomic structures examined.
        # e.g., the left knee, both lungs, or unpaired abdomen. if present, shall
        # be consistent with any laterality information indicated in
        # imagingstudy.series.bodysite.
        self.laterality = None
        # reference to Coding: Coding

        # the date and time the series was started.
        self.started = None
        # type = string

        # the physician or operator (often the radiology technician)  who
        # performed the series. the performer is recorded at the series level,
        # since each series in a study may be performed by a different
        # practitioner, at different times, and using different devices. a series
        # may be performed by multiple practitioners.
        self.performer = None
        # type = array
        # reference to Reference: identifier

        # a single sop instance within the series, e.g. an image, or presentation
        # state.
        self.instance = None
        # type = array
        # reference to ImagingStudy_Instance: ImagingStudy_Instance


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.availability is not None:
            for value in self.availability:
                if value != None and value.lower() not in ['online', 'offline', 'nearline', 'unavailable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'online, offline, nearline, unavailable'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ImagingStudy_Instance',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy_Series',
            'child_variable': 'instance'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy_Series',
            'child_variable': 'bodySite'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy_Series',
            'child_variable': 'laterality'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy_Series',
            'child_variable': 'endpoint'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'ImagingStudy_Series',
            'child_variable': 'modality'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'ImagingStudy_Series',
            'child_variable': 'performer'},
        ]

class ImagingStudy_Instance(fhirbase):
    """Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-
    Object Pair Instances (SOP Instances - images or other data) acquired or
    produced in a common context.  A series is of only one modality (e.g.
    X-ray, CT, MR, ultrasound), but a study may have multiple series of
    different modalities.
    """

    def __init__(self, dict_values=None):
        # formal identifier for this image or other content.
        self.uid = None
        # type = string

        # the number of instance in the series.
        self.number = None
        # type = int

        # dicom instance  type.
        self.sopClass = None
        # type = string

        # the description of the instance.
        self.title = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


