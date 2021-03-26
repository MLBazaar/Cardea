from .fhirbase import fhirbase


class ImagingStudy(fhirbase):
    """
    Representation of the content produced in a DICOM imaging study. A
    study comprises a set of series, each of which includes a set of
    Service-Object Pair Instances (SOP Instances - images or other data)
    acquired or produced in a common context.  A series is of only one
    modality (e.g. X-ray, CT, MR, ultrasound), but a study may have
    multiple series of different modalities.

    Args:
        resourceType: This is a ImagingStudy resource
        uid: Formal identifier for the study.
        accession: Accession Number is an identifier related to some aspect of
            imaging workflow and data management. Usage may vary across different
            institutions.  See for instance [IHE Radiology Technical Framework
            Volume 1 Appendix
            A](http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Rev13.0_Vol1_FT_2014-07-30.pdf).
        identifier: Other identifiers for the study.
        availability: Availability of study (online, offline, or nearline).
        modalityList: A list of all the Series.ImageModality values that are
            actual acquisition modalities, i.e. those in the DICOM Context Group
            29 (value set OID 1.2.840.10008.6.1.19).
        patient: The patient imaged in the study.
        context: The encounter or episode at which the request is initiated.
        started: Date and time the study started.
        basedOn: A list of the diagnostic requests that resulted in this
            imaging study being performed.
        referrer: The requesting/referring physician.
        interpreter: Who read the study and interpreted the images or other
            content.
        endpoint: The network service providing access (e.g., query, view, or
            retrieval) for the study. See implementation notes for information
            about using DICOM endpoints. A study-level endpoint applies to each
            series in the study, unless overridden by a series-level endpoint with
            the same Endpoint.type.
        numberOfSeries: Number of Series in the Study. This value given may be
            larger than the number of series elements this Resource contains due
            to resource availability, security, or other factors. This element
            should be present if any series elements are present.
        numberOfInstances: Number of SOP Instances in Study. This value given
            may be larger than the number of instance elements this resource
            contains due to resource availability, security, or other factors.
            This element should be present if any instance elements are present.
        procedureReference: A reference to the performed Procedure.
        procedureCode: The code for the performed procedure type.
        reason: Description of clinical condition indicating why the
            ImagingStudy was requested.
        description: Institution-generated description or classification of
            the Study performed.
        series: Each study has one or more series of images or other content.
    """

    __name__ = 'ImagingStudy'

    def __init__(self, dict_values=None):
        self.resourceType = 'ImagingStudy'
        # type: str
        # possible values: ImagingStudy

        self.uid = None
        # type: str

        self.accession = None
        # reference to Identifier

        self.availability = None
        # type: str
        # possible values: ONLINE, OFFLINE, NEARLINE, UNAVAILABLE

        self.modalityList = None
        # type: list
        # reference to Coding

        self.patient = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.started = None
        # type: str

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.referrer = None
        # reference to Reference: identifier

        self.interpreter = None
        # type: list
        # reference to Reference: identifier

        self.endpoint = None
        # type: list
        # reference to Reference: identifier

        self.numberOfSeries = None
        # type: int

        self.numberOfInstances = None
        # type: int

        self.procedureReference = None
        # type: list
        # reference to Reference: identifier

        self.procedureCode = None
        # type: list
        # reference to CodeableConcept

        self.reason = None
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.series = None
        # type: list
        # reference to ImagingStudy_Series

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.availability is not None:
            for value in self.availability:
                if value is not None and value.lower() not in [
                        'online', 'offline', 'nearline', 'unavailable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'ONLINE, OFFLINE, NEARLINE, UNAVAILABLE'))

    def get_relationships(self):

        return [
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
             'child_variable': 'interpreter'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'endpoint'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'procedureCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'reason'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'procedureReference'},

            {'parent_entity': 'ImagingStudy_Series',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'series'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'modalityList'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'referrer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'context'},
        ]


class ImagingStudy_Series(fhirbase):
    """
    Representation of the content produced in a DICOM imaging study. A
    study comprises a set of series, each of which includes a set of
    Service-Object Pair Instances (SOP Instances - images or other data)
    acquired or produced in a common context.  A series is of only one
    modality (e.g. X-ray, CT, MR, ultrasound), but a study may have
    multiple series of different modalities.

    Args:
        uid: Formal identifier for this series.
        number: The numeric identifier of this series in the study.
        modality: The modality of this series sequence.
        description: A description of the series.
        numberOfInstances: Number of SOP Instances in the Study. The value
            given may be larger than the number of instance elements this resource
            contains due to resource availability, security, or other factors.
            This element should be present if any instance elements are present.
        availability: Availability of series (online, offline or nearline).
        endpoint: The network service providing access (e.g., query, view, or
            retrieval) for this series. See implementation notes for information
            about using DICOM endpoints. A series-level endpoint, if present, has
            precedence over a study-level endpoint with the same Endpoint.type.
        bodySite: The anatomic structures examined. See DICOM Part 16 Annex L
            (http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html)
            for DICOM to SNOMED-CT mappings. The bodySite may indicate the
            laterality of body part imaged; if so, it shall be consistent with any
            content of ImagingStudy.series.laterality.
        laterality: The laterality of the (possibly paired) anatomic
            structures examined. E.g., the left knee, both lungs, or unpaired
            abdomen. If present, shall be consistent with any laterality
            information indicated in ImagingStudy.series.bodySite.
        started: The date and time the series was started.
        performer: The physician or operator (often the radiology technician)
            who performed the series. The performer is recorded at the series
            level, since each series in a study may be performed by a different
            practitioner, at different times, and using different devices. A
            series may be performed by multiple practitioners.
        instance: A single SOP instance within the series, e.g. an image, or
            presentation state.
    """

    __name__ = 'ImagingStudy_Series'

    def __init__(self, dict_values=None):
        self.uid = None
        # type: str

        self.number = None
        # type: int

        self.modality = None
        # reference to Coding

        self.description = None
        # type: str

        self.numberOfInstances = None
        # type: int

        self.availability = None
        # type: str
        # possible values: ONLINE, OFFLINE, NEARLINE, UNAVAILABLE

        self.endpoint = None
        # type: list
        # reference to Reference: identifier

        self.bodySite = None
        # reference to Coding

        self.laterality = None
        # reference to Coding

        self.started = None
        # type: str

        self.performer = None
        # type: list
        # reference to Reference: identifier

        self.instance = None
        # type: list
        # reference to ImagingStudy_Instance

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.availability is not None:
            for value in self.availability:
                if value is not None and value.lower() not in [
                        'online', 'offline', 'nearline', 'unavailable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'ONLINE, OFFLINE, NEARLINE, UNAVAILABLE'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'bodySite'},

            {'parent_entity': 'ImagingStudy_Instance',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'instance'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'laterality'},

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
    """
    Representation of the content produced in a DICOM imaging study. A
    study comprises a set of series, each of which includes a set of
    Service-Object Pair Instances (SOP Instances - images or other data)
    acquired or produced in a common context.  A series is of only one
    modality (e.g. X-ray, CT, MR, ultrasound), but a study may have
    multiple series of different modalities.

    Args:
        uid: Formal identifier for this image or other content.
        number: The number of instance in the series.
        sopClass: DICOM instance  type.
        title: The description of the instance.
    """

    __name__ = 'ImagingStudy_Instance'

    def __init__(self, dict_values=None):
        self.uid = None
        # type: str

        self.number = None
        # type: int

        self.sopClass = None
        # type: str

        self.title = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
