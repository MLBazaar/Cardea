from .fhirbase import fhirbase


class QuestionnaireResponse(fhirbase):
    """
    A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.
    """

    __name__ = 'QuestionnaireResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'QuestionnaireResponse'
        """
        This is a QuestionnaireResponse resource

        type: string
        possible values: QuestionnaireResponse
        """

        self.basedOn = None
        """
        The order, proposal or plan that is fulfilled in whole or in part by
        this QuestionnaireResponse.  For example, a ProcedureRequest seeking
        an intake assessment or a decision support recommendation to assess
        for post-partum depression.

        type: array
        reference to Reference: identifier
        """

        self.parent = None
        """
        A procedure or observation that this questionnaire was performed as
        part of the execution of.  For example, the surgery a checklist was
        executed as part of.

        type: array
        reference to Reference: identifier
        """

        self.questionnaire = None
        """
        The Questionnaire that defines and organizes the questions for which
        answers are being provided.

        reference to Reference: identifier
        """

        self.status = None
        """
        The position of the questionnaire response within its overall
        lifecycle.

        type: string
        possible values: in-progress, completed, amended,
        entered-in-error, stopped
        """

        self.subject = None
        """
        The subject of the questionnaire response.  This could be a patient,
        organization, practitioner, device, etc.  This is who/what the answers
        apply to, but is not necessarily the source of information.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter or episode of care with primary association to the
        questionnaire response.

        reference to Reference: identifier
        """

        self.authored = None
        """
        The date and/or time that this set of answers were last changed.

        type: string
        """

        self.author = None
        """
        Person who received the answers to the questions in the
        QuestionnaireResponse and recorded them in the system.

        reference to Reference: identifier
        """

        self.source = None
        """
        The person who answered the questions about the subject.

        reference to Reference: identifier
        """

        self.item = None
        """
        A group or question item from the original questionnaire for which
        answers are provided.

        type: array
        reference to QuestionnaireResponse_Item
        """

        self.identifier = None
        """
        A business identifier assigned to a particular completed (or partially
        completed) questionnaire.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'in-progress', 'completed', 'amended', 'entered-in-error', 'stopped']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'in-progress, completed, amended, entered-in-error, stopped'))

    def get_relationships(self):

        return [
            {'parent_entity': 'QuestionnaireResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'item'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'parent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'source'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'questionnaire'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'context'},
        ]


class QuestionnaireResponse_Item(fhirbase):
    """
    A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.
    """

    __name__ = 'QuestionnaireResponse_Item'

    def __init__(self, dict_values=None):
        self.linkId = None
        """
        The item from the Questionnaire that corresponds to this item in the
        QuestionnaireResponse resource.

        type: string
        """

        self.definition = None
        """
        A reference to an [[[ElementDefinition]]] that provides the details
        for the item.

        type: string
        """

        self.text = None
        """
        Text that is displayed above the contents of the group or as the text
        of the question being answered.

        type: string
        """

        self.subject = None
        """
        More specific subject this section's answers are about, details the
        subject given in QuestionnaireResponse.

        reference to Reference: identifier
        """

        self.answer = None
        """
        The respondent's answer(s) to the question.

        type: array
        reference to QuestionnaireResponse_Answer
        """

        self.item = None
        """
        Questions or sub-groups nested beneath a question or group.

        type: array
        reference to QuestionnaireResponse_Item
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'QuestionnaireResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Item',
             'child_variable': 'item'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse_Item',
             'child_variable': 'subject'},

            {'parent_entity': 'QuestionnaireResponse_Answer',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Item',
             'child_variable': 'answer'},
        ]


class QuestionnaireResponse_Answer(fhirbase):
    """
    A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.
    """

    __name__ = 'QuestionnaireResponse_Answer'

    def __init__(self, dict_values=None):
        self.valueBoolean = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: boolean
        """

        self.valueDecimal = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: int
        """

        self.valueInteger = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: int
        """

        self.valueDate = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: string
        """

        self.valueDateTime = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: string
        """

        self.valueTime = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: string
        """

        self.valueString = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: string
        """

        self.valueUri = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        type: string
        """

        self.valueAttachment = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        reference to Attachment
        """

        self.valueCoding = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        reference to Coding
        """

        self.valueQuantity = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        reference to Quantity
        """

        self.valueReference = None
        """
        The answer (or one of the answers) provided by the respondent to the
        question.

        reference to Reference: identifier
        """

        self.item = None
        """
        Nested groups and/or questions found within this particular answer.

        type: array
        reference to QuestionnaireResponse_Item
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'QuestionnaireResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'item'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueCoding'},
        ]
