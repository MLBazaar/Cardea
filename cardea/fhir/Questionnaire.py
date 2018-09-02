from .fhirbase import fhirbase


class Questionnaire(fhirbase):
    """A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.
    """

    def __init__(self, dict_values=None):
        # this is a questionnaire resource
        self.resourceType = 'Questionnaire'
        # type = string
        # possible values: Questionnaire

        # an absolute uri that is used to identify this questionnaire when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this questionnaire is (or will be) published. the url should include the
        # major version of the questionnaire. for more information see [technical
        # and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the
        # questionnaire when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the questionnaire author
        # and is not expected to be globally unique. for example, it might be a
        # timestamp (e.g. yyyymmdd) if a managed version is not available. there
        # is also no expectation that versions can be placed in a lexicographical
        # sequence.
        self.version = None
        # type = string

        # a natural language name identifying the questionnaire. this name should
        # be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the questionnaire.
        self.title = None
        # type = string

        # the status of this questionnaire. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this questionnaire is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the questionnaire was published.
        # the date must change if and when the business version changes and it
        # must change if the status code changes. in addition, it should change
        # when the substantive content of the questionnaire changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the
        # questionnaire.
        self.publisher = None
        # type = string

        # a free text natural language description of the questionnaire from a
        # consumer's perspective.
        self.description = None
        # type = string

        # explaination of why this questionnaire is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # the date on which the resource content was approved by the publisher.
        # approval happens once when the content is officially approved for usage.
        self.approvalDate = None
        # type = string

        # the date on which the resource content was last reviewed. review happens
        # periodically after approval, but doesn't change the original approval
        # date.
        self.lastReviewDate = None
        # type = string

        # the period during which the questionnaire content was or is planned to
        # be in active use.
        self.effectivePeriod = None
        # reference to Period: Period

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate questionnaire instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the questionnaire is intended to
        # be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a copyright statement relating to the questionnaire and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the questionnaire.
        self.copyright = None
        # type = string

        # an identifier for this question or group of questions in a particular
        # terminology such as loinc.
        self.code = None
        # type = array
        # reference to Coding: Coding

        # the types of subjects that can be the subject of responses created for
        # the questionnaire.
        self.subjectType = None
        # type = array

        # a particular question, question grouping or display text that is part of
        # the questionnaire.
        self.item = None
        # type = array
        # reference to Questionnaire_Item: Questionnaire_Item

        # a formal identifier that is used to identify this questionnaire when it
        # is represented in other formats, or referenced in a specification,
        # model, design or an instance.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'code'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire',
             'child_variable': 'identifier'},
        ]


class Questionnaire_Item(fhirbase):
    """A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.
    """

    def __init__(self, dict_values=None):
        # an identifier that is unique within the questionnaire allowing linkage
        # to the equivalent item in a questionnaireresponse resource.
        self.linkId = None
        # type = string

        # a reference to an [[[elementdefinition]]] that provides the details for
        # the item. if a definition is provided, then the following element values
        # can be inferred from the definition:   * code (elementdefinition.code) *
        # type (elementdefinition.type) * required (elementdefinition.min) *
        # repeats (elementdefinition.max) * maxlength
        # (elementdefinition.maxlength) * options (elementdefinition.binding)  any
        # information provided in these elements on a questionnaire item overrides
        # the information from the definition.
        self.definition = None
        # type = string

        # a terminology code that corresponds to this group or question (e.g. a
        # code from loinc, which defines many questions and answers).
        self.code = None
        # type = array
        # reference to Coding: Coding

        # a short label for a particular group, question or set of display text
        # within the questionnaire used for reference by the individual completing
        # the questionnaire.
        self.prefix = None
        # type = string

        # the name of a section, the text of a question or text content for a
        # display item.
        self.text = None
        # type = string

        # the type of questionnaire item this is - whether text for display, a
        # grouping of other items or a particular type of data to be captured
        # (string, integer, coded choice, etc.).
        self.type = None
        # type = string
        # possible values: group, display, boolean, decimal, integer,
        # date, dateTime, time, string, text, url, choice, open-choice,
        # attachment, reference, quantity

        # a constraint indicating that this item should only be enabled
        # (displayed/allow answers to be captured) when the specified condition is
        # true.
        self.enableWhen = None
        # type = array
        # reference to Questionnaire_EnableWhen: Questionnaire_EnableWhen

        # an indication, if true, that the item must be present in a "completed"
        # questionnaireresponse.  if false, the item may be skipped when answering
        # the questionnaire.
        self.required = None
        # type = boolean

        # an indication, if true, that the item may occur multiple times in the
        # response, collecting multiple answers answers for questions or multiple
        # sets of answers for groups.
        self.repeats = None
        # type = boolean

        # an indication, when true, that the value cannot be changed by a human
        # respondent to the questionnaire.
        self.readOnly = None
        # type = boolean

        # the maximum number of characters that are permitted in the answer to be
        # considered a "valid" questionnaireresponse.
        self.maxLength = None
        # type = int

        # a reference to a value set containing a list of codes representing
        # permitted answers for a "choice" or "open-choice" question.
        self.options = None
        # reference to Reference: identifier

        # one of the permitted answers for a "choice" or "open-choice" question.
        self.option = None
        # type = array
        # reference to Questionnaire_Option: Questionnaire_Option

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialBoolean = None
        # type = boolean

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialDecimal = None
        # type = int

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialInteger = None
        # type = int

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialDate = None
        # type = string

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialDateTime = None
        # type = string

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialTime = None
        # type = string

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialString = None
        # type = string

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialUri = None
        # type = string

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialAttachment = None
        # reference to Attachment: Attachment

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialCoding = None
        # reference to Coding: Coding

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialQuantity = None
        # reference to Quantity: Quantity

        # the value that should be defaulted when initially rendering the
        # questionnaire for user input.
        self.initialReference = None
        # reference to Reference: identifier

        # text, questions and other groups to be nested beneath a question or
        # group.
        self.item = None
        # type = array
        # reference to Questionnaire_Item: Questionnaire_Item

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'group', 'display', 'boolean', 'decimal', 'integer', 'date', 'datetime',
                    'time', 'string', 'text', 'url', 'choice', 'open-choice', 'attachment',
                        'reference', 'quantity']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'group, display, boolean, decimal, integer, date,'
                        'dateTime, time, string, text, url, choice, open-choice,'
                        'attachment, reference, quantity'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'code'},

            {'parent_entity': 'Questionnaire_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'item'},

            {'parent_entity': 'Questionnaire_EnableWhen',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'enableWhen'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialReference'},

            {'parent_entity': 'Questionnaire_Option',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'option'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'options'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialCoding'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialAttachment'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Item',
             'child_variable': 'initialQuantity'},
        ]


class Questionnaire_EnableWhen(fhirbase):
    """A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.
    """

    def __init__(self, dict_values=None):
        # the linkid for the question whose answer (or lack of answer) governs
        # whether this item is enabled.
        self.question = None
        # type = string

        # an indication that this item should be enabled only if the specified
        # question is answered (hasanswer=true) or not answered (hasanswer=false).
        self.hasAnswer = None
        # type = boolean

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerBoolean = None
        # type = boolean

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerDecimal = None
        # type = int

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerInteger = None
        # type = int

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerDate = None
        # type = string

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerDateTime = None
        # type = string

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerTime = None
        # type = string

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerString = None
        # type = string

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerUri = None
        # type = string

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerAttachment = None
        # reference to Attachment: Attachment

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerCoding = None
        # reference to Coding: Coding

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerQuantity = None
        # reference to Quantity: Quantity

        # an answer that the referenced question must match in order for the item
        # to be enabled.
        self.answerReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerQuantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Questionnaire_EnableWhen',
             'child_variable': 'answerReference'},
        ]


class Questionnaire_Option(fhirbase):
    """A structured set of questions intended to guide the collection of
    answers from end-users. Questionnaires provide detailed control over
    order, presentation, phraseology and grouping to allow coherent,
    consistent data collection.
    """

    def __init__(self, dict_values=None):
        # a potential answer that's allowed as the answer to this question.
        self.valueInteger = None
        # type = int

        # a potential answer that's allowed as the answer to this question.
        self.valueDate = None
        # type = string

        # a potential answer that's allowed as the answer to this question.
        self.valueTime = None
        # type = string

        # a potential answer that's allowed as the answer to this question.
        self.valueString = None
        # type = string

        # a potential answer that's allowed as the answer to this question.
        self.valueCoding = None
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Questionnaire_Option',
             'child_variable': 'valueCoding'},
        ]
