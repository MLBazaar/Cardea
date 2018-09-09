from .fhirbase import fhirbase


class Questionnaire(fhirbase):
    """
    A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.
    """

    __name__ = 'Questionnaire'

    def __init__(self, dict_values=None):
        self.resourceType = 'Questionnaire'
        """
        This is a Questionnaire resource

        type: string
        possible values: Questionnaire
        """

        self.url = None
        """
        An absolute URI that is used to identify this questionnaire when it is
        referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this questionnaire is (or will be) published. The URL SHOULD
        include the major version of the questionnaire. For more information
        see [Technical and Business Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the
        questionnaire when it is referenced in a specification, model, design
        or instance. This is an arbitrary value managed by the questionnaire
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the questionnaire. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the questionnaire.

        type: string
        """

        self.status = None
        """
        The status of this questionnaire. Enables tracking the life-cycle of
        the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this questionnaire is authored for
        testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the questionnaire was published.
        The date must change if and when the business version changes and it
        must change if the status code changes. In addition, it should change
        when the substantive content of the questionnaire changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the
        questionnaire.

        type: string
        """

        self.description = None
        """
        A free text natural language description of the questionnaire from a
        consumer's perspective.

        type: string
        """

        self.purpose = None
        """
        Explaination of why this questionnaire is needed and why it has been
        designed as it has.

        type: string
        """

        self.approvalDate = None
        """
        The date on which the resource content was approved by the publisher.
        Approval happens once when the content is officially approved for
        usage.

        type: string
        """

        self.lastReviewDate = None
        """
        The date on which the resource content was last reviewed. Review
        happens periodically after approval, but doesn't change the original
        approval date.

        type: string
        """

        self.effectivePeriod = None
        """
        The period during which the questionnaire content was or is planned to
        be in active use.

        reference to Period
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate questionnaire instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the questionnaire is intended to
        be used.

        type: array
        reference to CodeableConcept
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        publisher.

        type: array
        reference to ContactDetail
        """

        self.copyright = None
        """
        A copyright statement relating to the questionnaire and/or its
        contents. Copyright statements are generally legal restrictions on the
        use and publishing of the questionnaire.

        type: string
        """

        self.code = None
        """
        An identifier for this question or group of questions in a particular
        terminology such as LOINC.

        type: array
        reference to Coding
        """

        self.subjectType = None
        """
        The types of subjects that can be the subject of responses created for
        the questionnaire.

        type: array
        """

        self.item = None
        """
        A particular question, question grouping or display text that is part
        of the questionnaire.

        type: array
        reference to Questionnaire_Item
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this questionnaire when
        it is represented in other formats, or referenced in a specification,
        model, design or an instance.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Questionnaire_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'item'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'useContext'},

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
    """

    __name__ = 'Questionnaire_Item'

    def __init__(self, dict_values=None):
        self.linkId = None
        """
        An identifier that is unique within the Questionnaire allowing linkage
        to the equivalent item in a QuestionnaireResponse resource.

        type: string
        """

        self.definition = None
        """
        A reference to an [[[ElementDefinition]]] that provides the details
        for the item. If a definition is provided, then the following element
        values can be inferred from the definition:   * code
        (ElementDefinition.code) * type (ElementDefinition.type) * required
        (ElementDefinition.min) * repeats (ElementDefinition.max) * maxLength
        (ElementDefinition.maxLength) * options (ElementDefinition.binding)
        Any information provided in these elements on a Questionnaire Item
        overrides the information from the definition.

        type: string
        """

        self.code = None
        """
        A terminology code that corresponds to this group or question (e.g. a
        code from LOINC, which defines many questions and answers).

        type: array
        reference to Coding
        """

        self.prefix = None
        """
        A short label for a particular group, question or set of display text
        within the questionnaire used for reference by the individual
        completing the questionnaire.

        type: string
        """

        self.text = None
        """
        The name of a section, the text of a question or text content for a
        display item.

        type: string
        """

        self.type = None
        """
        The type of questionnaire item this is - whether text for display, a
        grouping of other items or a particular type of data to be captured
        (string, integer, coded choice, etc.).

        type: string
        possible values: group, display, boolean, decimal, integer,
        date, dateTime, time, string, text, url, choice, open-choice,
        attachment, reference, quantity
        """

        self.enableWhen = None
        """
        A constraint indicating that this item should only be enabled
        (displayed/allow answers to be captured) when the specified condition
        is true.

        type: array
        reference to Questionnaire_EnableWhen
        """

        self.required = None
        """
        An indication, if true, that the item must be present in a "completed"
        QuestionnaireResponse.  If false, the item may be skipped when
        answering the questionnaire.

        type: boolean
        """

        self.repeats = None
        """
        An indication, if true, that the item may occur multiple times in the
        response, collecting multiple answers answers for questions or
        multiple sets of answers for groups.

        type: boolean
        """

        self.readOnly = None
        """
        An indication, when true, that the value cannot be changed by a human
        respondent to the Questionnaire.

        type: boolean
        """

        self.maxLength = None
        """
        The maximum number of characters that are permitted in the answer to
        be considered a "valid" QuestionnaireResponse.

        type: int
        """

        self.options = None
        """
        A reference to a value set containing a list of codes representing
        permitted answers for a "choice" or "open-choice" question.

        reference to Reference: identifier
        """

        self.option = None
        """
        One of the permitted answers for a "choice" or "open-choice" question.

        type: array
        reference to Questionnaire_Option
        """

        self.initialBoolean = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: boolean
        """

        self.initialDecimal = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: int
        """

        self.initialInteger = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: int
        """

        self.initialDate = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: string
        """

        self.initialDateTime = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: string
        """

        self.initialTime = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: string
        """

        self.initialString = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: string
        """

        self.initialUri = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        type: string
        """

        self.initialAttachment = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        reference to Attachment
        """

        self.initialCoding = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        reference to Coding
        """

        self.initialQuantity = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        reference to Quantity
        """

        self.initialReference = None
        """
        The value that should be defaulted when initially rendering the
        questionnaire for user input.

        reference to Reference: identifier
        """

        self.item = None
        """
        Text, questions and other groups to be nested beneath a question or
        group.

        type: array
        reference to Questionnaire_Item
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Questionnaire_EnableWhen',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'enableWhen'},

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
             'child_variable': 'initialReference'},

            {'parent_entity': 'Questionnaire_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'item'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'code'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialQuantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'options'},

            {'parent_entity': 'Questionnaire_Option',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'option'},
        ]


class Questionnaire_EnableWhen(fhirbase):
    """
    A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.
    """

    __name__ = 'Questionnaire_EnableWhen'

    def __init__(self, dict_values=None):
        self.question = None
        """
        The linkId for the question whose answer (or lack of answer) governs
        whether this item is enabled.

        type: string
        """

        self.hasAnswer = None
        """
        An indication that this item should be enabled only if the specified
        question is answered (hasAnswer=true) or not answered
        (hasAnswer=false).

        type: boolean
        """

        self.answerBoolean = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: boolean
        """

        self.answerDecimal = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: int
        """

        self.answerInteger = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: int
        """

        self.answerDate = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: string
        """

        self.answerDateTime = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: string
        """

        self.answerTime = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: string
        """

        self.answerString = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: string
        """

        self.answerUri = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        type: string
        """

        self.answerAttachment = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        reference to Attachment
        """

        self.answerCoding = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        reference to Coding
        """

        self.answerQuantity = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        reference to Quantity
        """

        self.answerReference = None
        """
        An answer that the referenced question must match in order for the
        item to be enabled.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerCoding'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerAttachment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerQuantity'},
        ]


class Questionnaire_Option(fhirbase):
    """
    A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.
    """

    __name__ = 'Questionnaire_Option'

    def __init__(self, dict_values=None):
        self.valueInteger = None
        """
        A potential answer that's allowed as the answer to this question.

        type: int
        """

        self.valueDate = None
        """
        A potential answer that's allowed as the answer to this question.

        type: string
        """

        self.valueTime = None
        """
        A potential answer that's allowed as the answer to this question.

        type: string
        """

        self.valueString = None
        """
        A potential answer that's allowed as the answer to this question.

        type: string
        """

        self.valueCoding = None
        """
        A potential answer that's allowed as the answer to this question.

        reference to Coding
        """

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
