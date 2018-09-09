from .fhirbase import fhirbase


class Composition(fhirbase):
    """
    A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement. While
    a Composition defines the structure, it does not actually contain the
    content: rather the full content of a document is contained in a
    Bundle, of which the Composition is the first resource contained.
    """

    __name__ = 'Composition'

    def __init__(self, dict_values=None):
        self.resourceType = 'Composition'
        """
        This is a Composition resource

        type: string
        possible values: Composition
        """

        self.status = None
        """
        The workflow/clinical status of this composition. The status is a
        marker for the clinical standing of the document.

        type: string
        possible values: preliminary, final, amended, entered-in-error
        """

        self.type = None
        """
        Specifies the particular kind of composition (e.g. History and
        Physical, Discharge Summary, Progress Note). This usually equates to
        the purpose of making the composition.

        reference to CodeableConcept
        """

        self._class = None
        """
        A categorization for the type of the composition - helps for indexing
        and searching. This may be implied by or derived from the code
        specified in the Composition Type.

        reference to CodeableConcept
        """

        self.subject = None
        """
        Who or what the composition is about. The composition can be about a
        person, (patient or healthcare practitioner), a device (e.g. a
        machine) or even a group of subjects (such as a document about a herd
        of livestock, or a set of patients that share a common exposure).

        reference to Reference: identifier
        """

        self.encounter = None
        """
        Describes the clinical encounter or type of care this documentation is
        associated with.

        reference to Reference: identifier
        """

        self.date = None
        """
        The composition editing time, when the composition was last logically
        changed by the author.

        type: string
        """

        self.author = None
        """
        Identifies who is responsible for the information in the composition,
        not necessarily who typed it in.

        type: array
        reference to Reference: identifier
        """

        self.title = None
        """
        Official human-readable label for the composition.

        type: string
        """

        self.confidentiality = None
        """
        The code specifying the level of confidentiality of the Composition.

        type: string
        """

        self.attester = None
        """
        A participant who has attested to the accuracy of the
        composition/document.

        type: array
        reference to Composition_Attester
        """

        self.custodian = None
        """
        Identifies the organization or group who is responsible for ongoing
        maintenance of and access to the composition/document information.

        reference to Reference: identifier
        """

        self.relatesTo = None
        """
        Relationships that this composition has with other compositions or
        documents that already exist.

        type: array
        reference to Composition_RelatesTo
        """

        self.event = None
        """
        The clinical service, such as a colonoscopy or an appendectomy, being
        documented.

        type: array
        reference to Composition_Event
        """

        self.section = None
        """
        The root of the sections that make up the composition.

        type: array
        reference to Composition_Section
        """

        self.identifier = None
        """
        Logical identifier for the composition, assigned when created. This
        identifier stays constant as the composition is changed over time.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'preliminary', 'final', 'amended', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'preliminary, final, amended, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Composition_RelatesTo',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'relatesTo'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'encounter'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'type'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'custodian'},

            {'parent_entity': 'Composition_Section',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'section'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': '_class'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'author'},

            {'parent_entity': 'Composition_Event',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'event'},

            {'parent_entity': 'Composition_Attester',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'attester'},
        ]


class Composition_Attester(fhirbase):
    """
    A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement. While
    a Composition defines the structure, it does not actually contain the
    content: rather the full content of a document is contained in a
    Bundle, of which the Composition is the first resource contained.
    """

    __name__ = 'Composition_Attester'

    def __init__(self, dict_values=None):
        self.mode = None
        """
        The type of attestation the authenticator offers.

        type: array
        possible values: personal, professional, legal, official
        """

        self.time = None
        """
        When the composition was attested by the party.

        type: string
        """

        self.party = None
        """
        Who attested the composition in the specified way.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'personal', 'professional', 'legal', 'official']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'personal, professional, legal, official'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition_Attester',
             'child_variable': 'party'},
        ]


class Composition_RelatesTo(fhirbase):
    """
    A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement. While
    a Composition defines the structure, it does not actually contain the
    content: rather the full content of a document is contained in a
    Bundle, of which the Composition is the first resource contained.
    """

    __name__ = 'Composition_RelatesTo'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The type of relationship that this composition has with anther
        composition or document.

        type: string
        """

        self.targetIdentifier = None
        """
        The target composition/document of this relationship.

        reference to Identifier
        """

        self.targetReference = None
        """
        The target composition/document of this relationship.

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
             'child_entity': 'Composition_RelatesTo',
             'child_variable': 'targetReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_RelatesTo',
             'child_variable': 'targetIdentifier'},
        ]


class Composition_Event(fhirbase):
    """
    A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement. While
    a Composition defines the structure, it does not actually contain the
    content: rather the full content of a document is contained in a
    Bundle, of which the Composition is the first resource contained.
    """

    __name__ = 'Composition_Event'

    def __init__(self, dict_values=None):
        self.code = None
        """
        This list of codes represents the main clinical acts, such as a
        colonoscopy or an appendectomy, being documented. In some cases, the
        event is inherent in the typeCode, such as a "History and Physical
        Report" in which the procedure being documented is necessarily a
        "History and Physical" act.

        type: array
        reference to CodeableConcept
        """

        self.period = None
        """
        The period of time covered by the documentation. There is no assertion
        that the documentation is a complete representation for this period,
        only that it documents events during this time.

        reference to Period
        """

        self.detail = None
        """
        The description and/or reference of the event(s) being documented. For
        example, this could be used to document such a colonoscopy or an
        appendectomy.

        type: array
        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Event',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition_Event',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Event',
             'child_variable': 'code'},
        ]


class Composition_Section(fhirbase):
    """
    A set of healthcare-related information that is assembled together
    into a single logical document that provides a single coherent
    statement of meaning, establishes its own context and that has
    clinical attestation with regard to who is making the statement. While
    a Composition defines the structure, it does not actually contain the
    content: rather the full content of a document is contained in a
    Bundle, of which the Composition is the first resource contained.
    """

    __name__ = 'Composition_Section'

    def __init__(self, dict_values=None):
        self.title = None
        """
        The label for this particular section.  This will be part of the
        rendered content for the document, and is often used to build a table
        of contents.

        type: string
        """

        self.code = None
        """
        A code identifying the kind of content contained within the section.
        This must be consistent with the section title.

        reference to CodeableConcept
        """

        self.text = None
        """
        A human-readable narrative that contains the attested content of the
        section, used to represent the content of the resource to a human. The
        narrative need not encode all the structured data, but is required to
        contain sufficient detail to make it "clinically safe" for a human to
        just read the narrative.

        reference to Narrative
        """

        self.mode = None
        """
        How the entry list was prepared - whether it is a working list that is
        suitable for being maintained on an ongoing basis, or if it represents
        a snapshot of a list of items from another source, or whether it is a
        prepared list where items may be marked as added, modified or deleted.

        type: string
        """

        self.orderedBy = None
        """
        Specifies the order applied to the items in the section entries.

        reference to CodeableConcept
        """

        self.entry = None
        """
        A reference to the actual resource from which the narrative in the
        section is derived.

        type: array
        reference to Reference: identifier
        """

        self.emptyReason = None
        """
        If the section is empty, why the list is empty. An empty section
        typically has some text explaining the empty reason.

        reference to CodeableConcept
        """

        self.section = None
        """
        A nested sub-section within this section.

        type: array
        reference to Composition_Section
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'text'},

            {'parent_entity': 'Composition_Section',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'section'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'emptyReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition_Section',
             'child_variable': 'entry'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'orderedBy'},
        ]
