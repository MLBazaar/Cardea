from .fhirbase import fhirbase


class GuidanceResponse(fhirbase):
    """
    A guidance response is the formal response to a guidance request,
    including any output parameters returned by the evaluation, as well as
    the description of any proposed actions to be taken.
    """

    __name__ = 'GuidanceResponse'

    def __init__(self, dict_values=None):
        self.resourceType = 'GuidanceResponse'
        """
        This is a GuidanceResponse resource

        type: string
        possible values: GuidanceResponse
        """

        self.requestId = None
        """
        The id of the request associated with this response. If an id was
        given as part of the request, it will be reproduced here to enable the
        requester to more easily identify the response in a multi-request
        scenario.

        type: string
        """

        self.module = None
        """
        A reference to the knowledge module that was invoked.

        reference to Reference: identifier
        """

        self.status = None
        """
        The status of the response. If the evaluation is completed
        successfully, the status will indicate success. However, in order to
        complete the evaluation, the engine may require more information. In
        this case, the status will be data-required, and the response will
        contain a description of the additional required information. If the
        evaluation completed successfully, but the engine determines that a
        potentially more accurate response could be provided if more data was
        available, the status will be data-requested, and the response will
        contain a description of the additional requested information.

        type: string
        possible values: success, data-requested, data-required,
        in-progress, failure, entered-in-error
        """

        self.subject = None
        """
        The patient for which the request was processed.

        reference to Reference: identifier
        """

        self.context = None
        """
        Allows the context of the guidance response to be provided if
        available. In a service context, this would likely be unavailable.

        reference to Reference: identifier
        """

        self.occurrenceDateTime = None
        """
        Indicates when the guidance response was processed.

        type: string
        """

        self.performer = None
        """
        Provides a reference to the device that performed the guidance.

        reference to Reference: identifier
        """

        self.reasonCodeableConcept = None
        """
        Indicates the reason the request was initiated. This is typically
        provided as a parameter to the evaluation and echoed by the service,
        although for some use cases, such as subscription- or event-based
        scenarios, it may provide an indication of the cause for the response.

        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Indicates the reason the request was initiated. This is typically
        provided as a parameter to the evaluation and echoed by the service,
        although for some use cases, such as subscription- or event-based
        scenarios, it may provide an indication of the cause for the response.

        reference to Reference: identifier
        """

        self.note = None
        """
        Provides a mechanism to communicate additional information about the
        response.

        type: array
        reference to Annotation
        """

        self.evaluationMessage = None
        """
        Messages resulting from the evaluation of the artifact or artifacts.
        As part of evaluating the request, the engine may produce
        informational or warning messages. These messages will be provided by
        this element.

        type: array
        reference to Reference: identifier
        """

        self.outputParameters = None
        """
        The output parameters of the evaluation, if any. Many modules will
        result in the return of specific resources such as procedure or
        communication requests that are returned as part of the operation
        result. However, modules may define specific outputs that would be
        returned as the result of the evaluation, and these would be returned
        in this element.

        reference to Reference: identifier
        """

        self.result = None
        """
        The actions, if any, produced by the evaluation of the artifact.

        reference to Reference: identifier
        """

        self.dataRequirement = None
        """
        If the evaluation could not be completed due to lack of information,
        or additional information would potentially result in a more accurate
        response, this element will a description of the data required in
        order to proceed with the evaluation. A subsequent request to the
        service should include this data.

        type: array
        reference to DataRequirement
        """

        self.identifier = None
        """
        Allows a service to provide a unique, business identifier for the
        response.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'success', 'data-requested', 'data-required', 'in-progress',
                        'failure', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'success, data-requested, data-required, in-progress, failure,'
                        'entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'DataRequirement',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'dataRequirement'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'module'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'evaluationMessage'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'outputParameters'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'subject'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'GuidanceResponse',
             'child_variable': 'result'},
        ]
