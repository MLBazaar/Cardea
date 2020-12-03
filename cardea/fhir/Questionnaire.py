from .fhirbase import fhirbase


class Questionnaire(fhirbase):
    """
    A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.

    Args:
        resourceType: This is a Questionnaire resource
        url: An absolute URI that is used to identify this questionnaire when
            it is referenced in a specification, model, design or an instance.
            This SHALL be a URL, SHOULD be globally unique, and SHOULD be an
            address at which this questionnaire is (or will be) published. The URL
            SHOULD include the major version of the questionnaire. For more
            information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this
            questionnaire when it is represented in other formats, or referenced
            in a specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            questionnaire when it is referenced in a specification, model, design
            or instance. This is an arbitrary value managed by the questionnaire
            author and is not expected to be globally unique. For example, it
            might be a timestamp (e.g. yyyymmdd) if a managed version is not
            available. There is also no expectation that versions can be placed in
            a lexicographical sequence.
        name: A natural language name identifying the questionnaire. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the
            questionnaire.
        status: The status of this questionnaire. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this questionnaire is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the questionnaire was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the questionnaire
            changes.
        publisher: The name of the individual or organization that published
            the questionnaire.
        description: A free text natural language description of the
            questionnaire from a consumer's perspective.
        purpose: Explaination of why this questionnaire is needed and why it
            has been designed as it has.
        approvalDate: The date on which the resource content was approved by
            the publisher. Approval happens once when the content is officially
            approved for usage.
        lastReviewDate: The date on which the resource content was last
            reviewed. Review happens periodically after approval, but doesn't
            change the original approval date.
        effectivePeriod: The period during which the questionnaire content was
            or is planned to be in active use.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate questionnaire
            instances.
        jurisdiction: A legal or geographic region in which the questionnaire
            is intended to be used.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        copyright: A copyright statement relating to the questionnaire and/or
            its contents. Copyright statements are generally legal restrictions on
            the use and publishing of the questionnaire.
        code: An identifier for this question or group of questions in a
            particular terminology such as LOINC.
        subjectType: The types of subjects that can be the subject of
            responses created for the questionnaire.
        item: A particular question, question grouping or display text that is
            part of the questionnaire.
    """

    __name__ = 'Questionnaire'

    def __init__(self, dict_values=None):
        self.resourceType = 'Questionnaire'
        # type: str
        # possible values: Questionnaire

        self.url = None
        # type: str

        self.version = None
        # type: str

        self.name = None
        # type: str

        self.title = None
        # type: str

        self.status = None
        # type: str
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # type: bool

        self.date = None
        # type: str

        self.publisher = None
        # type: str

        self.description = None
        # type: str

        self.purpose = None
        # type: str

        self.approvalDate = None
        # type: str

        self.lastReviewDate = None
        # type: str

        self.effectivePeriod = None
        # reference to Period

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.copyright = None
        # type: str

        self.code = None
        # type: list
        # reference to Coding

        self.subjectType = None
        # type: list

        self.item = None
        # type: list
        # reference to Questionnaire_Item

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'useContext'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'identifier'},

            {'parent_entity': 'Questionnaire_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'item'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'jurisdiction'},
        ]


class Questionnaire_Item(fhirbase):
    """
    A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.

    Args:
        linkId: An identifier that is unique within the Questionnaire allowing
            linkage to the equivalent item in a QuestionnaireResponse resource.
        definition: A reference to an [[[ElementDefinition]]] that provides
            the details for the item. If a definition is provided, then the
            following element values can be inferred from the definition:   * code
            (ElementDefinition.code) * type (ElementDefinition.type) * required
            (ElementDefinition.min) * repeats (ElementDefinition.max) * maxLength
            (ElementDefinition.maxLength) * options (ElementDefinition.binding)
            Any information provided in these elements on a Questionnaire Item
            overrides the information from the definition.
        code: A terminology code that corresponds to this group or question
            (e.g. a code from LOINC, which defines many questions and answers).
        prefix: A short label for a particular group, question or set of
            display text within the questionnaire used for reference by the
            individual completing the questionnaire.
        text: The name of a section, the text of a question or text content
            for a display item.
        type: The type of questionnaire item this is - whether text for
            display, a grouping of other items or a particular type of data to be
            captured (string, integer, coded choice, etc.).
        enableWhen: A constraint indicating that this item should only be
            enabled (displayed/allow answers to be captured) when the specified
            condition is true.
        required: An indication, if true, that the item must be present in a
            "completed" QuestionnaireResponse.  If false, the item may be skipped
            when answering the questionnaire.
        repeats: An indication, if true, that the item may occur multiple
            times in the response, collecting multiple answers answers for
            questions or multiple sets of answers for groups.
        readOnly: An indication, when true, that the value cannot be changed
            by a human respondent to the Questionnaire.
        maxLength: The maximum number of characters that are permitted in the
            answer to be considered a "valid" QuestionnaireResponse.
        options: A reference to a value set containing a list of codes
            representing permitted answers for a "choice" or "open-choice"
            question.
        option: One of the permitted answers for a "choice" or "open-choice"
            question.
        initialBoolean: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialDecimal: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialInteger: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialDate: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialDateTime: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialTime: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialString: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialUri: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialAttachment: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialCoding: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialQuantity: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        initialReference: The value that should be defaulted when initially
            rendering the questionnaire for user input.
        item: Text, questions and other groups to be nested beneath a question
            or group.
    """

    __name__ = 'Questionnaire_Item'

    def __init__(self, dict_values=None):
        self.linkId = None
        # type: str

        self.definition = None
        # type: str

        self.code = None
        # type: list
        # reference to Coding

        self.prefix = None
        # type: str

        self.text = None
        # type: str

        self.type = None
        # type: str
        # possible values: group, display, boolean, decimal, integer,
        # date, dateTime, time, string, text, url, choice, open-choice,
        # attachment, reference, quantity

        self.enableWhen = None
        # type: list
        # reference to Questionnaire_EnableWhen

        self.required = None
        # type: bool

        self.repeats = None
        # type: bool

        self.readOnly = None
        # type: bool

        self.maxLength = None
        # type: int

        self.options = None
        # reference to Reference: identifier

        self.option = None
        # type: list
        # reference to Questionnaire_Option

        self.initialBoolean = None
        # type: bool

        self.initialDecimal = None
        # type: int

        self.initialInteger = None
        # type: int

        self.initialDate = None
        # type: str

        self.initialDateTime = None
        # type: str

        self.initialTime = None
        # type: str

        self.initialString = None
        # type: str

        self.initialUri = None
        # type: str

        self.initialAttachment = None
        # reference to Attachment

        self.initialCoding = None
        # reference to Coding

        self.initialQuantity = None
        # reference to Quantity

        self.initialReference = None
        # reference to Reference: identifier

        self.item = None
        # type: list
        # reference to Questionnaire_Item

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'group', 'display', 'boolean', 'decimal', 'integer', 'date',
                    'datetime', 'time', 'string', 'text', 'url', 'choice', 'open-choice',
                        'attachment', 'reference', 'quantity']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'group, display, boolean, decimal, integer, date, dateTime, time,'
                        'string, text, url, choice, open-choice, attachment, reference,'
                        'quantity'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialQuantity'},

            {'parent_entity': 'Questionnaire_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'item'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialAttachment'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialCoding'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'options'},

            {'parent_entity': 'Questionnaire_Option',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'option'},

            {'parent_entity': 'Questionnaire_EnableWhen',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'enableWhen'},
        ]


class Questionnaire_EnableWhen(fhirbase):
    """
    A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.

    Args:
        question: The linkId for the question whose answer (or lack of answer)
            governs whether this item is enabled.
        hasAnswer: An indication that this item should be enabled only if the
            specified question is answered (hasAnswer=true) or not answered
            (hasAnswer=false).
        answerBoolean: An answer that the referenced question must match in
            order for the item to be enabled.
        answerDecimal: An answer that the referenced question must match in
            order for the item to be enabled.
        answerInteger: An answer that the referenced question must match in
            order for the item to be enabled.
        answerDate: An answer that the referenced question must match in order
            for the item to be enabled.
        answerDateTime: An answer that the referenced question must match in
            order for the item to be enabled.
        answerTime: An answer that the referenced question must match in order
            for the item to be enabled.
        answerString: An answer that the referenced question must match in
            order for the item to be enabled.
        answerUri: An answer that the referenced question must match in order
            for the item to be enabled.
        answerAttachment: An answer that the referenced question must match in
            order for the item to be enabled.
        answerCoding: An answer that the referenced question must match in
            order for the item to be enabled.
        answerQuantity: An answer that the referenced question must match in
            order for the item to be enabled.
        answerReference: An answer that the referenced question must match in
            order for the item to be enabled.
    """

    __name__ = 'Questionnaire_EnableWhen'

    def __init__(self, dict_values=None):
        self.question = None
        # type: str

        self.hasAnswer = None
        # type: bool

        self.answerBoolean = None
        # type: bool

        self.answerDecimal = None
        # type: int

        self.answerInteger = None
        # type: int

        self.answerDate = None
        # type: str

        self.answerDateTime = None
        # type: str

        self.answerTime = None
        # type: str

        self.answerString = None
        # type: str

        self.answerUri = None
        # type: str

        self.answerAttachment = None
        # reference to Attachment

        self.answerCoding = None
        # reference to Coding

        self.answerQuantity = None
        # reference to Quantity

        self.answerReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerQuantity'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerCoding'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerAttachment'},
        ]


class Questionnaire_Option(fhirbase):
    """
    A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.

    Args:
        valueInteger: A potential answer that's allowed as the answer to this
            question.
        valueDate: A potential answer that's allowed as the answer to this
            question.
        valueTime: A potential answer that's allowed as the answer to this
            question.
        valueString: A potential answer that's allowed as the answer to this
            question.
        valueCoding: A potential answer that's allowed as the answer to this
            question.
    """

    __name__ = 'Questionnaire_Option'

    def __init__(self, dict_values=None):
        self.valueInteger = None
        # type: int

        self.valueDate = None
        # type: str

        self.valueTime = None
        # type: str

        self.valueString = None
        # type: str

        self.valueCoding = None
        # reference to Coding

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Option',
             'child_variable': 'valueCoding'},
        ]
