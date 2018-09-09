from .fhirbase import fhirbase


class GuidanceResponse(fhirbase):
    """A guidance response is the formal response to a guidance request,
    including any output parameters returned by the evaluation, as well as
    the description of any proposed actions to be taken.
    """

    def __init__(self, dict_values=None):
        # this is a guidanceresponse resource
        self.resourceType = 'GuidanceResponse'
        # type = string
        # possible values: GuidanceResponse

        # the id of the request associated with this response. if an id was given
        # as part of the request, it will be reproduced here to enable the
        # requester to more easily identify the response in a multi-request
        # scenario.
        self.requestId = None
        # type = string

        # a reference to the knowledge module that was invoked.
        self.module = None
        # reference to Reference: identifier

        # the status of the response. if the evaluation is completed successfully,
        # the status will indicate success. however, in order to complete the
        # evaluation, the engine may require more information. in this case, the
        # status will be data-required, and the response will contain a
        # description of the additional required information. if the evaluation
        # completed successfully, but the engine determines that a potentially
        # more accurate response could be provided if more data was available, the
        # status will be data-requested, and the response will contain a
        # description of the additional requested information.
        self.status = None
        # type = string
        # possible values: success, data-requested, data-required, in-
        # progress, failure, entered-in-error

        # the patient for which the request was processed.
        self.subject = None
        # reference to Reference: identifier

        # allows the context of the guidance response to be provided if available.
        # in a service context, this would likely be unavailable.
        self.context = None
        # reference to Reference: identifier

        # indicates when the guidance response was processed.
        self.occurrenceDateTime = None
        # type = string

        # provides a reference to the device that performed the guidance.
        self.performer = None
        # reference to Reference: identifier

        # indicates the reason the request was initiated. this is typically
        # provided as a parameter to the evaluation and echoed by the service,
        # although for some use cases, such as subscription- or event-based
        # scenarios, it may provide an indication of the cause for the response.
        self.reasonCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the reason the request was initiated. this is typically
        # provided as a parameter to the evaluation and echoed by the service,
        # although for some use cases, such as subscription- or event-based
        # scenarios, it may provide an indication of the cause for the response.
        self.reasonReference = None
        # reference to Reference: identifier

        # provides a mechanism to communicate additional information about the
        # response.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # messages resulting from the evaluation of the artifact or artifacts. as
        # part of evaluating the request, the engine may produce informational or
        # warning messages. these messages will be provided by this element.
        self.evaluationMessage = None
        # type = array
        # reference to Reference: identifier

        # the output parameters of the evaluation, if any. many modules will
        # result in the return of specific resources such as procedure or
        # communication requests that are returned as part of the operation
        # result. however, modules may define specific outputs that would be
        # returned as the result of the evaluation, and these would be returned in
        # this element.
        self.outputParameters = None
        # reference to Reference: identifier

        # the actions, if any, produced by the evaluation of the artifact.
        self.result = None
        # reference to Reference: identifier

        # if the evaluation could not be completed due to lack of information, or
        # additional information would potentially result in a more accurate
        # response, this element will a description of the data required in order
        # to proceed with the evaluation. a subsequent request to the service
        # should include this data.
        self.dataRequirement = None
        # type = array
        # reference to DataRequirement: DataRequirement

        # allows a service to provide a unique, business identifier for the
        # response.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'success', 'data-requested', 'data-required', 'in-progress', 'failure',
                        'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'success, data-requested, data-required, in-progress,'
                        'failure, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'outputParameters'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'result'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'dataRequirement'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'evaluationMessage'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'module'},
        ]
