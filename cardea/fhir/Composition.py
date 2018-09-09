from .fhirbase import fhirbase


class Composition(fhirbase):
    """A set of healthcare-related information that is assembled together into
    a single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation
    with regard to who is making the statement. While a Composition defines
    the structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition
    is the first resource contained.
    """

    __name__ = 'Composition'

    def __init__(self, dict_values=None):
        # this is a composition resource
        self.resourceType = 'Composition'
        # type = string
        # possible values: Composition

        # the workflow/clinical status of this composition. the status is a marker
        # for the clinical standing of the document.
        self.status = None
        # type = string
        # possible values: preliminary, final, amended, entered-in-error

        # specifies the particular kind of composition (e.g. history and physical,
        # discharge summary, progress note). this usually equates to the purpose
        # of making the composition.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # a categorization for the type of the composition - helps for indexing
        # and searching. this may be implied by or derived from the code specified
        # in the composition type.
        self._class = None
        # reference to CodeableConcept: CodeableConcept

        # who or what the composition is about. the composition can be about a
        # person, (patient or healthcare practitioner), a device (e.g. a machine)
        # or even a group of subjects (such as a document about a herd of
        # livestock, or a set of patients that share a common exposure).
        self.subject = None
        # reference to Reference: identifier

        # describes the clinical encounter or type of care this documentation is
        # associated with.
        self.encounter = None
        # reference to Reference: identifier

        # the composition editing time, when the composition was last logically
        # changed by the author.
        self.date = None
        # type = string

        # identifies who is responsible for the information in the composition,
        # not necessarily who typed it in.
        self.author = None
        # type = array
        # reference to Reference: identifier

        # official human-readable label for the composition.
        self.title = None
        # type = string

        # the code specifying the level of confidentiality of the composition.
        self.confidentiality = None
        # type = string

        # a participant who has attested to the accuracy of the
        # composition/document.
        self.attester = None
        # type = array
        # reference to Composition_Attester: Composition_Attester

        # identifies the organization or group who is responsible for ongoing
        # maintenance of and access to the composition/document information.
        self.custodian = None
        # reference to Reference: identifier

        # relationships that this composition has with other compositions or
        # documents that already exist.
        self.relatesTo = None
        # type = array
        # reference to Composition_RelatesTo: Composition_RelatesTo

        # the clinical service, such as a colonoscopy or an appendectomy, being
        # documented.
        self.event = None
        # type = array
        # reference to Composition_Event: Composition_Event

        # the root of the sections that make up the composition.
        self.section = None
        # type = array
        # reference to Composition_Section: Composition_Section

        # logical identifier for the composition, assigned when created. this
        # identifier stays constant as the composition is changed over time.
        self.identifier = None
        # reference to Identifier: Identifier

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
             'child_variable': 'custodian'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'author'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition',
             'child_variable': 'subject'},

            {'parent_entity': 'Composition_Section',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'section'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': '_class'},

            {'parent_entity': 'Composition_Attester',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'attester'},

            {'parent_entity': 'Composition_Event',
             'parent_variable': 'object_id',
             'child_entity': 'Composition',
             'child_variable': 'event'},
        ]


class Composition_Attester(fhirbase):
    """A set of healthcare-related information that is assembled together into
    a single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation
    with regard to who is making the statement. While a Composition defines
    the structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition
    is the first resource contained.
    """

    __name__ = 'Composition_Attester'

    def __init__(self, dict_values=None):
        # the type of attestation the authenticator offers.
        self.mode = None
        # type = array
        # possible values: personal, professional, legal, official

        # when the composition was attested by the party.
        self.time = None
        # type = string

        # who attested the composition in the specified way.
        self.party = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
    """A set of healthcare-related information that is assembled together into
    a single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation
    with regard to who is making the statement. While a Composition defines
    the structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition
    is the first resource contained.
    """

    __name__ = 'Composition_RelatesTo'

    def __init__(self, dict_values=None):
        # the type of relationship that this composition has with anther
        # composition or document.
        self.code = None
        # type = string

        # the target composition/document of this relationship.
        self.targetIdentifier = None
        # reference to Identifier: Identifier

        # the target composition/document of this relationship.
        self.targetReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
    """A set of healthcare-related information that is assembled together into
    a single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation
    with regard to who is making the statement. While a Composition defines
    the structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition
    is the first resource contained.
    """

    __name__ = 'Composition_Event'

    def __init__(self, dict_values=None):
        # this list of codes represents the main clinical acts, such as a
        # colonoscopy or an appendectomy, being documented. in some cases, the
        # event is inherent in the typecode, such as a "history and physical
        # report" in which the procedure being documented is necessarily a
        # "history and physical" act.
        self.code = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the period of time covered by the documentation. there is no assertion
        # that the documentation is a complete representation for this period,
        # only that it documents events during this time.
        self.period = None
        # reference to Period: Period

        # the description and/or reference of the event(s) being documented. for
        # example, this could be used to document such a colonoscopy or an
        # appendectomy.
        self.detail = None
        # type = array
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
    """A set of healthcare-related information that is assembled together into
    a single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation
    with regard to who is making the statement. While a Composition defines
    the structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition
    is the first resource contained.
    """

    __name__ = 'Composition_Section'

    def __init__(self, dict_values=None):
        # the label for this particular section.  this will be part of the
        # rendered content for the document, and is often used to build a table of
        # contents.
        self.title = None
        # type = string

        # a code identifying the kind of content contained within the section.
        # this must be consistent with the section title.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a human-readable narrative that contains the attested content of the
        # section, used to represent the content of the resource to a human. the
        # narrative need not encode all the structured data, but is required to
        # contain sufficient detail to make it "clinically safe" for a human to
        # just read the narrative.
        self.text = None
        # reference to Narrative: Narrative

        # how the entry list was prepared - whether it is a working list that is
        # suitable for being maintained on an ongoing basis, or if it represents a
        # snapshot of a list of items from another source, or whether it is a
        # prepared list where items may be marked as added, modified or deleted.
        self.mode = None
        # type = string

        # specifies the order applied to the items in the section entries.
        self.orderedBy = None
        # reference to CodeableConcept: CodeableConcept

        # a reference to the actual resource from which the narrative in the
        # section is derived.
        self.entry = None
        # type = array
        # reference to Reference: identifier

        # if the section is empty, why the list is empty. an empty section
        # typically has some text explaining the empty reason.
        self.emptyReason = None
        # reference to CodeableConcept: CodeableConcept

        # a nested sub-section within this section.
        self.section = None
        # type = array
        # reference to Composition_Section: Composition_Section

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'code'},

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
             'child_variable': 'orderedBy'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Composition_Section',
             'child_variable': 'entry'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Composition_Section',
             'child_variable': 'emptyReason'},
        ]
