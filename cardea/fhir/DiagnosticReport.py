from .fhirbase import fhirbase


class DiagnosticReport(fhirbase):
    """The findings and interpretation of diagnostic  tests performed on
    patients, groups of patients, devices, and locations, and/or specimens
    derived from these. The report includes clinical context such as
    requesting and provider information, and some mix of atomic results,
    images, textual and coded interpretations, and formatted representation
    of diagnostic reports.
    """

    __name__ = 'DiagnosticReport'

    def __init__(self, dict_values=None):
        # this is a diagnosticreport resource
        self.resourceType = 'DiagnosticReport'
        # type = string
        # possible values: DiagnosticReport

        # details concerning a test or procedure requested.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # the status of the diagnostic report as a whole.
        self.status = None
        # type = string
        # possible values: registered, partial, preliminary, final,
        # amended, corrected, appended, cancelled, entered-in-error, unknown

        # a code that classifies the clinical discipline, department or diagnostic
        # service that created the report (e.g. cardiology, biochemistry,
        # hematology, mri). this is used for searching, sorting and display
        # purposes.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # a code or name that describes this diagnostic report.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the subject of the report. usually, but not always, this is a patient.
        # however diagnostic services also perform analyses on specimens collected
        # from a variety of other sources.
        self.subject = None
        # reference to Reference: identifier

        # the healthcare event  (e.g. a patient and healthcare provider
        # interaction) which this diagnosticreport per is about.
        self.context = None
        # reference to Reference: identifier

        # the time or time-period the observed values are related to. when the
        # subject of the report is a patient, this is usually either the time of
        # the procedure or of specimen collection(s), but very often the source of
        # the date/time is not known, only the date/time itself.
        self.effectiveDateTime = None
        # type = string

        # the time or time-period the observed values are related to. when the
        # subject of the report is a patient, this is usually either the time of
        # the procedure or of specimen collection(s), but very often the source of
        # the date/time is not known, only the date/time itself.
        self.effectivePeriod = None
        # reference to Period: Period

        # the date and time that this version of the report was released from the
        # source diagnostic service.
        self.issued = None
        # type = string

        # indicates who or what participated in producing the report.
        self.performer = None
        # type = array
        # reference to DiagnosticReport_Performer: DiagnosticReport_Performer

        # details about the specimens on which this diagnostic report is based.
        self.specimen = None
        # type = array
        # reference to Reference: identifier

        # observations that are part of this diagnostic report. observations can
        # be simple name/value pairs (e.g. "atomic" results), or they can be
        # grouping observations that include references to other members of the
        # group (e.g. "panels").
        self.result = None
        # type = array
        # reference to Reference: identifier

        # one or more links to full details of any imaging performed during the
        # diagnostic investigation. typically, this is imaging performed by dicom
        # enabled modalities, but this is not required. a fully enabled pacs
        # viewer can use this information to provide views of the source images.
        self.imagingStudy = None
        # type = array
        # reference to Reference: identifier

        # a list of key images associated with this report. the images are
        # generally created during the diagnostic process, and may be directly of
        # the patient, or of treated specimens (i.e. slides of interest).
        self.image = None
        # type = array
        # reference to DiagnosticReport_Image: DiagnosticReport_Image

        # concise and clinically contextualized impression / summary of the
        # diagnostic report.
        self.conclusion = None
        # type = string

        # codes for the conclusion.
        self.codedDiagnosis = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # rich text representation of the entire result as issued by the
        # diagnostic service. multiple formats are allowed but they shall be
        # semantically equivalent.
        self.presentedForm = None
        # type = array
        # reference to Attachment: Attachment

        # identifiers assigned to this report by the performer or other systems.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'registered', 'partial', 'preliminary', 'final', 'amended', 'corrected',
                        'appended', 'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'registered, partial, preliminary, final, amended,'
                        'corrected, appended, cancelled, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'specimen'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'identifier'},

            {'parent_entity': 'DiagnosticReport_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'performer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'category'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'context'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'presentedForm'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'imagingStudy'},

            {'parent_entity': 'DiagnosticReport_Image',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'image'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'codedDiagnosis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'result'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'subject'},
        ]


class DiagnosticReport_Performer(fhirbase):
    """The findings and interpretation of diagnostic  tests performed on
    patients, groups of patients, devices, and locations, and/or specimens
    derived from these. The report includes clinical context such as
    requesting and provider information, and some mix of atomic results,
    images, textual and coded interpretations, and formatted representation
    of diagnostic reports.
    """

    __name__ = 'DiagnosticReport_Performer'

    def __init__(self, dict_values=None):
        # describes the type of participation (e.g.  a responsible party, author,
        # or verifier).
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the reference to the  practitioner or organization involved in producing
        # the report. for example, the diagnostic service that is responsible for
        # issuing the report.
        self.actor = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport_Performer',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport_Performer',
             'child_variable': 'role'},
        ]


class DiagnosticReport_Image(fhirbase):
    """The findings and interpretation of diagnostic  tests performed on
    patients, groups of patients, devices, and locations, and/or specimens
    derived from these. The report includes clinical context such as
    requesting and provider information, and some mix of atomic results,
    images, textual and coded interpretations, and formatted representation
    of diagnostic reports.
    """

    __name__ = 'DiagnosticReport_Image'

    def __init__(self, dict_values=None):
        # a comment about the image. typically, this is used to provide an
        # explanation for why the image is included, or to draw the viewer's
        # attention to important features.
        self.comment = None
        # type = string

        # reference to the image source.
        self.link = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport_Image',
             'child_variable': 'link'},
        ]
