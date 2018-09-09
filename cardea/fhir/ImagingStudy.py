from .fhirbase import fhirbase


class ImagingStudy(fhirbase):
    """
    Representation of the content produced in a DICOM imaging study. A
    study comprises a set of series, each of which includes a set of
    Service-Object Pair Instances (SOP Instances - images or other data)
    acquired or produced in a common context.  A series is of only one
    modality (e.g. X-ray, CT, MR, ultrasound), but a study may have
    multiple series of different modalities.
    """

    __name__ = 'ImagingStudy'

    def __init__(self, dict_values=None):
        self.resourceType = 'ImagingStudy'
        """
        This is a ImagingStudy resource

        type: string
        possible values: ImagingStudy
        """

        self.uid = None
        """
        Formal identifier for the study.

        type: string
        """

        self.accession = None
        """
        Accession Number is an identifier related to some aspect of imaging
        workflow and data management. Usage may vary across different
        institutions.  See for instance [IHE Radiology Technical Framework
        Volume 1 Appendix
        A](http://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Rev13.0_Vol1_FT_2014-07-30.pdf).

        reference to Identifier
        """

        self.availability = None
        """
        Availability of study (online, offline, or nearline).

        type: string
        possible values: ONLINE, OFFLINE, NEARLINE, UNAVAILABLE
        """

        self.modalityList = None
        """
        A list of all the Series.ImageModality values that are actual
        acquisition modalities, i.e. those in the DICOM Context Group 29
        (value set OID 1.2.840.10008.6.1.19).

        type: array
        reference to Coding
        """

        self.patient = None
        """
        The patient imaged in the study.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter or episode at which the request is initiated.

        reference to Reference: identifier
        """

        self.started = None
        """
        Date and time the study started.

        type: string
        """

        self.basedOn = None
        """
        A list of the diagnostic requests that resulted in this imaging study
        being performed.

        type: array
        reference to Reference: identifier
        """

        self.referrer = None
        """
        The requesting/referring physician.

        reference to Reference: identifier
        """

        self.interpreter = None
        """
        Who read the study and interpreted the images or other content.

        type: array
        reference to Reference: identifier
        """

        self.endpoint = None
        """
        The network service providing access (e.g., query, view, or retrieval)
        for the study. See implementation notes for information about using
        DICOM endpoints. A study-level endpoint applies to each series in the
        study, unless overridden by a series-level endpoint with the same
        Endpoint.type.

        type: array
        reference to Reference: identifier
        """

        self.numberOfSeries = None
        """
        Number of Series in the Study. This value given may be larger than the
        number of series elements this Resource contains due to resource
        availability, security, or other factors. This element should be
        present if any series elements are present.

        type: int
        """

        self.numberOfInstances = None
        """
        Number of SOP Instances in Study. This value given may be larger than
        the number of instance elements this resource contains due to resource
        availability, security, or other factors. This element should be
        present if any instance elements are present.

        type: int
        """

        self.procedureReference = None
        """
        A reference to the performed Procedure.

        type: array
        reference to Reference: identifier
        """

        self.procedureCode = None
        """
        The code for the performed procedure type.

        type: array
        reference to CodeableConcept
        """

        self.reason = None
        """
        Description of clinical condition indicating why the ImagingStudy was
        requested.

        reference to CodeableConcept
        """

        self.description = None
        """
        Institution-generated description or classification of the Study
        performed.

        type: string
        """

        self.series = None
        """
        Each study has one or more series of images or other content.

        type: array
        reference to ImagingStudy_Series
        """

        self.identifier = None
        """
        Other identifiers for the study.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'procedureCode'},

            {'parent_entity': 'ImagingStudy_Series',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'series'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'reason'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'modalityList'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'procedureReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'interpreter'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'endpoint'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'referrer'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy',
             'child_variable': 'accession'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy',
             'child_variable': 'patient'},
        ]


class ImagingStudy_Series(fhirbase):
    """
    Representation of the content produced in a DICOM imaging study. A
    study comprises a set of series, each of which includes a set of
    Service-Object Pair Instances (SOP Instances - images or other data)
    acquired or produced in a common context.  A series is of only one
    modality (e.g. X-ray, CT, MR, ultrasound), but a study may have
    multiple series of different modalities.
    """

    __name__ = 'ImagingStudy_Series'

    def __init__(self, dict_values=None):
        self.uid = None
        """
        Formal identifier for this series.

        type: string
        """

        self.number = None
        """
        The numeric identifier of this series in the study.

        type: int
        """

        self.modality = None
        """
        The modality of this series sequence.

        reference to Coding
        """

        self.description = None
        """
        A description of the series.

        type: string
        """

        self.numberOfInstances = None
        """
        Number of SOP Instances in the Study. The value given may be larger
        than the number of instance elements this resource contains due to
        resource availability, security, or other factors. This element should
        be present if any instance elements are present.

        type: int
        """

        self.availability = None
        """
        Availability of series (online, offline or nearline).

        type: string
        possible values: ONLINE, OFFLINE, NEARLINE, UNAVAILABLE
        """

        self.endpoint = None
        """
        The network service providing access (e.g., query, view, or retrieval)
        for this series. See implementation notes for information about using
        DICOM endpoints. A series-level endpoint, if present, has precedence
        over a study-level endpoint with the same Endpoint.type.

        type: array
        reference to Reference: identifier
        """

        self.bodySite = None
        """
        The anatomic structures examined. See DICOM Part 16 Annex L
        (http://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html)
        for DICOM to SNOMED-CT mappings. The bodySite may indicate the
        laterality of body part imaged; if so, it shall be consistent with any
        content of ImagingStudy.series.laterality.

        reference to Coding
        """

        self.laterality = None
        """
        The laterality of the (possibly paired) anatomic structures examined.
        E.g., the left knee, both lungs, or unpaired abdomen. If present,
        shall be consistent with any laterality information indicated in
        ImagingStudy.series.bodySite.

        reference to Coding
        """

        self.started = None
        """
        The date and time the series was started.

        type: string
        """

        self.performer = None
        """
        The physician or operator (often the radiology technician)  who
        performed the series. The performer is recorded at the series level,
        since each series in a study may be performed by a different
        practitioner, at different times, and using different devices. A
        series may be performed by multiple practitioners.

        type: array
        reference to Reference: identifier
        """

        self.instance = None
        """
        A single SOP instance within the series, e.g. an image, or
        presentation state.

        type: array
        reference to ImagingStudy_Instance
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.availability is not None:
            for value in self.availability:
                if value is not None and value.lower() not in [
                        'online', 'offline', 'nearline', 'unavailable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'ONLINE, OFFLINE, NEARLINE, UNAVAILABLE'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'modality'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'endpoint'},

            {'parent_entity': 'ImagingStudy_Instance',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'instance'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'performer'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ImagingStudy_Series',
             'child_variable': 'laterality'},
        ]


class ImagingStudy_Instance(fhirbase):
    """
    Representation of the content produced in a DICOM imaging study. A
    study comprises a set of series, each of which includes a set of
    Service-Object Pair Instances (SOP Instances - images or other data)
    acquired or produced in a common context.  A series is of only one
    modality (e.g. X-ray, CT, MR, ultrasound), but a study may have
    multiple series of different modalities.
    """

    __name__ = 'ImagingStudy_Instance'

    def __init__(self, dict_values=None):
        self.uid = None
        """
        Formal identifier for this image or other content.

        type: string
        """

        self.number = None
        """
        The number of instance in the series.

        type: int
        """

        self.sopClass = None
        """
        DICOM instance  type.

        type: string
        """

        self.title = None
        """
        The description of the instance.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
