from .fhirbase import fhirbase


class DiagnosticReport(fhirbase):
    """
    The findings and interpretation of diagnostic  tests performed on
    patients, groups of patients, devices, and locations, and/or specimens
    derived from these. The report includes clinical context such as
    requesting and provider information, and some mix of atomic results,
    images, textual and coded interpretations, and formatted
    representation of diagnostic reports.
    """

    __name__ = 'DiagnosticReport'

    def __init__(self, dict_values=None):
        self.resourceType = 'DiagnosticReport'
        """
        This is a DiagnosticReport resource

        type: string
        possible values: DiagnosticReport
        """

        self.basedOn = None
        """
        Details concerning a test or procedure requested.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        The status of the diagnostic report as a whole.

        type: string
        possible values: registered, partial, preliminary, final,
        amended, corrected, appended, cancelled, entered-in-error, unknown
        """

        self.category = None
        """
        A code that classifies the clinical discipline, department or
        diagnostic service that created the report (e.g. cardiology,
        biochemistry, hematology, MRI). This is used for searching, sorting
        and display purposes.

        reference to CodeableConcept
        """

        self.code = None
        """
        A code or name that describes this diagnostic report.

        reference to CodeableConcept
        """

        self.subject = None
        """
        The subject of the report. Usually, but not always, this is a patient.
        However diagnostic services also perform analyses on specimens
        collected from a variety of other sources.

        reference to Reference: identifier
        """

        self.context = None
        """
        The healthcare event  (e.g. a patient and healthcare provider
        interaction) which this DiagnosticReport per is about.

        reference to Reference: identifier
        """

        self.effectiveDateTime = None
        """
        The time or time-period the observed values are related to. When the
        subject of the report is a patient, this is usually either the time of
        the procedure or of specimen collection(s), but very often the source
        of the date/time is not known, only the date/time itself.

        type: string
        """

        self.effectivePeriod = None
        """
        The time or time-period the observed values are related to. When the
        subject of the report is a patient, this is usually either the time of
        the procedure or of specimen collection(s), but very often the source
        of the date/time is not known, only the date/time itself.

        reference to Period
        """

        self.issued = None
        """
        The date and time that this version of the report was released from
        the source diagnostic service.

        type: string
        """

        self.performer = None
        """
        Indicates who or what participated in producing the report.

        type: array
        reference to DiagnosticReport_Performer
        """

        self.specimen = None
        """
        Details about the specimens on which this diagnostic report is based.

        type: array
        reference to Reference: identifier
        """

        self.result = None
        """
        Observations that are part of this diagnostic report. Observations can
        be simple name/value pairs (e.g. "atomic" results), or they can be
        grouping observations that include references to other members of the
        group (e.g. "panels").

        type: array
        reference to Reference: identifier
        """

        self.imagingStudy = None
        """
        One or more links to full details of any imaging performed during the
        diagnostic investigation. Typically, this is imaging performed by
        DICOM enabled modalities, but this is not required. A fully enabled
        PACS viewer can use this information to provide views of the source
        images.

        type: array
        reference to Reference: identifier
        """

        self.image = None
        """
        A list of key images associated with this report. The images are
        generally created during the diagnostic process, and may be directly
        of the patient, or of treated specimens (i.e. slides of interest).

        type: array
        reference to DiagnosticReport_Image
        """

        self.conclusion = None
        """
        Concise and clinically contextualized impression / summary of the
        diagnostic report.

        type: string
        """

        self.codedDiagnosis = None
        """
        Codes for the conclusion.

        type: array
        reference to CodeableConcept
        """

        self.presentedForm = None
        """
        Rich text representation of the entire result as issued by the
        diagnostic service. Multiple formats are allowed but they SHALL be
        semantically equivalent.

        type: array
        reference to Attachment
        """

        self.identifier = None
        """
        Identifiers assigned to this report by the performer or other systems.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'registered', 'partial', 'preliminary', 'final', 'amended',
                        'corrected', 'appended', 'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'registered, partial, preliminary, final, amended, corrected, '
                        'appended, cancelled, entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'presentedForm'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'codedDiagnosis'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'result'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'DiagnosticReport_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'imagingStudy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'subject'},

            {'parent_entity': 'DiagnosticReport_Image',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'image'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport',
             'child_variable': 'specimen'},
        ]


class DiagnosticReport_Performer(fhirbase):
    """
    The findings and interpretation of diagnostic  tests performed on
    patients, groups of patients, devices, and locations, and/or specimens
    derived from these. The report includes clinical context such as
    requesting and provider information, and some mix of atomic results,
    images, textual and coded interpretations, and formatted
    representation of diagnostic reports.
    """

    __name__ = 'DiagnosticReport_Performer'

    def __init__(self, dict_values=None):
        self.role = None
        """
        Describes the type of participation (e.g.  a responsible party,
        author, or verifier).

        reference to CodeableConcept
        """

        self.actor = None
        """
        The reference to the  practitioner or organization involved in
        producing the report. For example, the diagnostic service that is
        responsible for issuing the report.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    The findings and interpretation of diagnostic  tests performed on
    patients, groups of patients, devices, and locations, and/or specimens
    derived from these. The report includes clinical context such as
    requesting and provider information, and some mix of atomic results,
    images, textual and coded interpretations, and formatted
    representation of diagnostic reports.
    """

    __name__ = 'DiagnosticReport_Image'

    def __init__(self, dict_values=None):
        self.comment = None
        """
        A comment about the image. Typically, this is used to provide an
        explanation for why the image is included, or to draw the viewer's
        attention to important features.

        type: string
        """

        self.link = None
        """
        Reference to the image source.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DiagnosticReport_Image',
             'child_variable': 'link'},
        ]
