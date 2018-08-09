from .fhirbase import * 
from .Reference import Reference
from .Identifier import Identifier

class QuestionnaireResponse(fhirbase):
    """A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.
    """

    def __init__(self, dict_values=None):
        # this is a questionnaireresponse resource
        self.resourceType = 'QuestionnaireResponse'
        # type = string
        # possible values = QuestionnaireResponse

        # the order, proposal or plan that is fulfilled in whole or in part by
        # this questionnaireresponse.  for example, a procedurerequest seeking an
        # intake assessment or a decision support recommendation to assess for
        # post-partum depression.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # a procedure or observation that this questionnaire was performed as part
        # of the execution of.  for example, the surgery a checklist was executed
        # as part of.
        self.parent = None
        # type = array
        # reference to Reference: identifier

        # the questionnaire that defines and organizes the questions for which
        # answers are being provided.
        self.questionnaire = None
        # reference to Reference: identifier

        # the position of the questionnaire response within its overall lifecycle.
        self.status = None
        # type = string
        # possible values = in-progress, completed, amended, entered-in-error, stopped

        # the subject of the questionnaire response.  this could be a patient,
        # organization, practitioner, device, etc.  this is who/what the answers
        # apply to, but is not necessarily the source of information.
        self.subject = None
        # reference to Reference: identifier

        # the encounter or episode of care with primary association to the
        # questionnaire response.
        self.context = None
        # reference to Reference: identifier

        # the date and/or time that this set of answers were last changed.
        self.authored = None
        # type = string

        # person who received the answers to the questions in the
        # questionnaireresponse and recorded them in the system.
        self.author = None
        # reference to Reference: identifier

        # the person who answered the questions about the subject.
        self.source = None
        # reference to Reference: identifier

        # a group or question item from the original questionnaire for which
        # answers are provided.
        self.item = None
        # type = array
        # reference to QuestionnaireResponse_Item: QuestionnaireResponse_Item

        # a business identifier assigned to a particular completed (or partially
        # completed) questionnaire.
        self.identifier = None
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['in-progress', 'completed', 'amended', 'entered-in-error', 'stopped']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'in-progress, completed, amended, entered-in-error, stopped'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'questionnaire'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'subject'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'source'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'context'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'author'},

            {'parent_entity': 'QuestionnaireResponse_Item',
            'parent_variable': 'object_id',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'item'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'parent'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'QuestionnaireResponse',
            'child_variable': 'identifier'},
        ]

class QuestionnaireResponse_Item(fhirbase):
    """A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.
    """

    def __init__(self, dict_values=None):
        # the item from the questionnaire that corresponds to this item in the
        # questionnaireresponse resource.
        # the item from the questionnaire that corresponds to this item in the
        # questionnaireresponse resource.
        self.linkId = None
        # type = string
        # type = string

        # a reference to an [[[elementdefinition]]] that provides the details for
        # the item.
        # a reference to an [[[elementdefinition]]] that provides the details for
        # the item.
        self.definition = None
        # type = string
        # type = string

        # text that is displayed above the contents of the group or as the text of
        # the question being answered.
        # text that is displayed above the contents of the group or as the text of
        # the question being answered.
        self.text = None
        # type = string
        # type = string

        # more specific subject this section's answers are about, details the
        # subject given in questionnaireresponse.
        # more specific subject this section's answers are about, details the
        # subject given in questionnaireresponse.
        self.subject = None
        # reference to Reference: identifier

        # the respondent's answer(s) to the question.
        # the respondent's answer(s) to the question.
        self.answer = None
        # type = array
        # type = array
        # reference to QuestionnaireResponse_Answer: QuestionnaireResponse_Answer

        # questions or sub-groups nested beneath a question or group.
        # questions or sub-groups nested beneath a question or group.
        self.item = None
        # type = array
        # type = array
        # reference to QuestionnaireResponse_Item: QuestionnaireResponse_Item


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
    """A structured set of questions and their answers. The questions are
    ordered and grouped into coherent subsets, corresponding to the
    structure of the grouping of the questionnaire being responded to.
    """

    def __init__(self, dict_values=None):
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueBoolean = None
        # type = boolean
        # type = boolean

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueDecimal = None
        # type = int
        # type = int

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueInteger = None
        # type = int
        # type = int

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueDate = None
        # type = string
        # type = string

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueDateTime = None
        # type = string
        # type = string

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueTime = None
        # type = string
        # type = string

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueString = None
        # type = string
        # type = string

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueUri = None
        # type = string
        # type = string

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueCoding = None
        # reference to Coding: Coding

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # the answer (or one of the answers) provided by the respondent to the
        # question.
        # the answer (or one of the answers) provided by the respondent to the
        # question.
        self.valueReference = None
        # reference to Reference: identifier

        # nested groups and/or questions found within this particular answer.
        # nested groups and/or questions found within this particular answer.
        self.item = None
        # type = array
        # type = array
        # reference to QuestionnaireResponse_Item: QuestionnaireResponse_Item


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'QuestionnaireResponse_Answer',
            'child_variable': 'valueQuantity'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'QuestionnaireResponse_Answer',
            'child_variable': 'valueCoding'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'QuestionnaireResponse_Answer',
            'child_variable': 'valueReference'},

            {'parent_entity': 'QuestionnaireResponse_Item',
            'parent_variable': 'object_id',
            'child_entity': 'QuestionnaireResponse_Answer',
            'child_variable': 'item'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'QuestionnaireResponse_Answer',
            'child_variable': 'valueAttachment'},
        ]

