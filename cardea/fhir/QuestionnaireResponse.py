from .fhirbase import fhirbase


class QuestionnaireResponse(fhirbase):
    """
    A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.

    Args:
        resourceType: This is a QuestionnaireResponse resource
        identifier: A business identifier assigned to a particular completed
            (or partially completed) questionnaire.
        basedOn: The order, proposal or plan that is fulfilled in whole or in
            part by this QuestionnaireResponse.  For example, a ProcedureRequest
            seeking an intake assessment or a decision support recommendation to
            assess for post-partum depression.
        parent: A procedure or observation that this questionnaire was
            performed as part of the execution of.  For example, the surgery a
            checklist was executed as part of.
        questionnaire: The Questionnaire that defines and organizes the
            questions for which answers are being provided.
        status: The position of the questionnaire response within its overall
            lifecycle.
        subject: The subject of the questionnaire response.  This could be a
            patient, organization, practitioner, device, etc.  This is who/what
            the answers apply to, but is not necessarily the source of
            information.
        context: The encounter or episode of care with primary association to
            the questionnaire response.
        authored: The date and/or time that this set of answers were last
            changed.
        author: Person who received the answers to the questions in the
            QuestionnaireResponse and recorded them in the system.
        source: The person who answered the questions about the subject.
        item: A group or question item from the original questionnaire for
            which answers are provided.
    """

    __name__ = 'QuestionnaireResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'QuestionnaireResponse'
        # type: str
        # possible values: QuestionnaireResponse

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.parent = None
        # type: list
        # reference to Reference: identifier

        self.questionnaire = None
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: in-progress, completed, amended,
        # entered-in-error, stopped

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.authored = None
        # type: str

        self.author = None
        # reference to Reference: identifier

        self.source = None
        # reference to Reference: identifier

        self.item = None
        # type: list
        # reference to QuestionnaireResponse_Item

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'in-progress', 'completed', 'amended', 'entered-in-error', 'stopped']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'in-progress, completed, amended, entered-in-error, stopped'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'questionnaire'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'parent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'source'},

            {'parent_entity': 'QuestionnaireResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'item'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse',
             'child_variable': 'subject'},
        ]


class QuestionnaireResponse_Item(fhirbase):
    """
    A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.

    Args:
        linkId: The item from the Questionnaire that corresponds to this item
            in the QuestionnaireResponse resource.
        definition: A reference to an [[[ElementDefinition]]] that provides
            the details for the item.
        text: Text that is displayed above the contents of the group or as the
            text of the question being answered.
        subject: More specific subject this section's answers are about,
            details the subject given in QuestionnaireResponse.
        answer: The respondent's answer(s) to the question.
        item: Questions or sub-groups nested beneath a question or group.
    """

    __name__ = 'QuestionnaireResponse_Item'

    def __init__(self, dict_values=None):
        self.linkId = None
        # type: str

        self.definition = None
        # type: str

        self.text = None
        # type: str

        self.subject = None
        # reference to Reference: identifier

        self.answer = None
        # type: list
        # reference to QuestionnaireResponse_Answer

        self.item = None
        # type: list
        # reference to QuestionnaireResponse_Item

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

    Args:
        valueBoolean: The answer (or one of the answers) provided by the
            respondent to the question.
        valueDecimal: The answer (or one of the answers) provided by the
            respondent to the question.
        valueInteger: The answer (or one of the answers) provided by the
            respondent to the question.
        valueDate: The answer (or one of the answers) provided by the
            respondent to the question.
        valueDateTime: The answer (or one of the answers) provided by the
            respondent to the question.
        valueTime: The answer (or one of the answers) provided by the
            respondent to the question.
        valueString: The answer (or one of the answers) provided by the
            respondent to the question.
        valueUri: The answer (or one of the answers) provided by the
            respondent to the question.
        valueAttachment: The answer (or one of the answers) provided by the
            respondent to the question.
        valueCoding: The answer (or one of the answers) provided by the
            respondent to the question.
        valueQuantity: The answer (or one of the answers) provided by the
            respondent to the question.
        valueReference: The answer (or one of the answers) provided by the
            respondent to the question.
        item: Nested groups and/or questions found within this particular
            answer.
    """

    __name__ = 'QuestionnaireResponse_Answer'

    def __init__(self, dict_values=None):
        self.valueBoolean = None
        # type: bool

        self.valueDecimal = None
        # type: int

        self.valueInteger = None
        # type: int

        self.valueDate = None
        # type: str

        self.valueDateTime = None
        # type: str

        self.valueTime = None
        # type: str

        self.valueString = None
        # type: str

        self.valueUri = None
        # type: str

        self.valueAttachment = None
        # reference to Attachment

        self.valueCoding = None
        # reference to Coding

        self.valueQuantity = None
        # reference to Quantity

        self.valueReference = None
        # reference to Reference: identifier

        self.item = None
        # type: list
        # reference to QuestionnaireResponse_Item

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'QuestionnaireResponse_Item',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'item'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueCoding'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'QuestionnaireResponse_Answer',
             'child_variable': 'valueReference'},
        ]
