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

    Args:
        resourceType: This is a Composition resource
        identifier: Logical identifier for the composition, assigned when
            created. This identifier stays constant as the composition is changed
            over time.
        status: The workflow/clinical status of this composition. The status
            is a marker for the clinical standing of the document.
        type: Specifies the particular kind of composition (e.g. History and
            Physical, Discharge Summary, Progress Note). This usually equates to
            the purpose of making the composition.
        class: A categorization for the type of the composition - helps for
            indexing and searching. This may be implied by or derived from the
            code specified in the Composition Type.
        subject: Who or what the composition is about. The composition can be
            about a person, (patient or healthcare practitioner), a device (e.g. a
            machine) or even a group of subjects (such as a document about a herd
            of livestock, or a set of patients that share a common exposure).
        encounter: Describes the clinical encounter or type of care this
            documentation is associated with.
        date: The composition editing time, when the composition was last
            logically changed by the author.
        author: Identifies who is responsible for the information in the
            composition, not necessarily who typed it in.
        title: Official human-readable label for the composition.
        confidentiality: The code specifying the level of confidentiality of
            the Composition.
        attester: A participant who has attested to the accuracy of the
            composition/document.
        custodian: Identifies the organization or group who is responsible for
            ongoing maintenance of and access to the composition/document
            information.
        relatesTo: Relationships that this composition has with other
            compositions or documents that already exist.
        event: The clinical service, such as a colonoscopy or an appendectomy,
            being documented.
        section: The root of the sections that make up the composition.
    """

    __name__ = 'Composition'

    def __init__(self, dict_values=None):
        self.resourceType = 'Composition'
        # type: str
        # possible values: Composition

        self.status = None
        # type: str
        # possible values: preliminary, final, amended,
        # entered-in-error

        self.type = None
        # reference to CodeableConcept

        self._class = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.encounter = None
        # reference to Reference: identifier

        self.date = None
        # type: str

        self.author = None
        # type: list
        # reference to Reference: identifier

        self.title = None
        # type: str

        self.confidentiality = None
        # type: str

        self.attester = None
        # type: list
        # reference to Composition_Attester

        self.custodian = None
        # reference to Reference: identifier

        self.relatesTo = None
        # type: list
        # reference to Composition_RelatesTo

        self.event = None
        # type: list
        # reference to Composition_Event

        self.section = None
        # type: list
        # reference to Composition_Section

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'preliminary', 'final', 'amended', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'preliminary, final, amended, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'author'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': '_class'},

            {'parent_entity': 'Composition_Event',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'event'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'custodian'},

            {'parent_entity': 'Composition_RelatesTo',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'relatesTo'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Composition_Section',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'section'},

            {'parent_entity': 'Composition_Attester',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'attester'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'encounter'},
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

    Args:
        mode: The type of attestation the authenticator offers.
        time: When the composition was attested by the party.
        party: Who attested the composition in the specified way.
    """

    __name__ = 'Composition_Attester'

    def __init__(self, dict_values=None):
        self.mode = None
        # type: list
        # possible values: personal, professional, legal, official

        self.time = None
        # type: str

        self.party = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        code: The type of relationship that this composition has with anther
            composition or document.
        targetIdentifier: The target composition/document of this
            relationship.
        targetReference: The target composition/document of this relationship.
    """

    __name__ = 'Composition_RelatesTo'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.targetIdentifier = None
        # reference to Identifier

        self.targetReference = None
        # reference to Reference: identifier

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

    Args:
        code: This list of codes represents the main clinical acts, such as a
            colonoscopy or an appendectomy, being documented. In some cases, the
            event is inherent in the typeCode, such as a "History and Physical
            Report" in which the procedure being documented is necessarily a
            "History and Physical" act.
        period: The period of time covered by the documentation. There is no
            assertion that the documentation is a complete representation for this
            period, only that it documents events during this time.
        detail: The description and/or reference of the event(s) being
            documented. For example, this could be used to document such a
            colonoscopy or an appendectomy.
    """

    __name__ = 'Composition_Event'

    def __init__(self, dict_values=None):
        self.code = None
        # type: list
        # reference to CodeableConcept

        self.period = None
        # reference to Period

        self.detail = None
        # type: list
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Event',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition_Event',
             'child_variable': 'detail'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Event',
             'child_variable': 'period'},
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

    Args:
        title: The label for this particular section.  This will be part of
            the rendered content for the document, and is often used to build a
            table of contents.
        code: A code identifying the kind of content contained within the
            section. This must be consistent with the section title.
        text: A human-readable narrative that contains the attested content of
            the section, used to represent the content of the resource to a human.
            The narrative need not encode all the structured data, but is required
            to contain sufficient detail to make it "clinically safe" for a human
            to just read the narrative.
        mode: How the entry list was prepared - whether it is a working list
            that is suitable for being maintained on an ongoing basis, or if it
            represents a snapshot of a list of items from another source, or
            whether it is a prepared list where items may be marked as added,
            modified or deleted.
        orderedBy: Specifies the order applied to the items in the section
            entries.
        entry: A reference to the actual resource from which the narrative in
            the section is derived.
        emptyReason: If the section is empty, why the list is empty. An empty
            section typically has some text explaining the empty reason.
        section: A nested sub-section within this section.
    """

    __name__ = 'Composition_Section'

    def __init__(self, dict_values=None):
        self.title = None
        # type: str

        self.code = None
        # reference to CodeableConcept

        self.text = None
        # reference to Narrative

        self.mode = None
        # type: str

        self.orderedBy = None
        # reference to CodeableConcept

        self.entry = None
        # type: list
        # reference to Reference: identifier

        self.emptyReason = None
        # reference to CodeableConcept

        self.section = None
        # type: list
        # reference to Composition_Section

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition_Section',
             'child_variable': 'entry'},

            {'parent_entity': 'Narrative',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'text'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'orderedBy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'emptyReason'},

            {'parent_entity': 'Composition_Section',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'section'},
        ]
