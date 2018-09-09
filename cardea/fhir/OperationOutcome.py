from .fhirbase import fhirbase


class OperationOutcome(fhirbase):
    """A collection of error, warning or information messages that result from
    a system action.
    """

    __name__ = 'OperationOutcome'

    def __init__(self, dict_values=None):
        # this is a operationoutcome resource
        self.resourceType = 'OperationOutcome'
        # type = string
        # possible values: OperationOutcome

        # an error, warning or information message that results from a system
        # action.
        self.issue = None
        # type = array
        # reference to OperationOutcome_Issue: OperationOutcome_Issue

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'OperationOutcome_Issue',
             'parent_variable': 'object_id',
             'child_entity': 'OperationOutcome',
             'child_variable': 'issue'},
        ]


class OperationOutcome_Issue(fhirbase):
    """A collection of error, warning or information messages that result from
    a system action.
    """

    __name__ = 'OperationOutcome_Issue'

    def __init__(self, dict_values=None):
        # indicates whether the issue indicates a variation from successful
        # processing.
        self.severity = None
        # type = string
        # possible values: fatal, error, warning, information

        # describes the type of the issue. the system that creates an
        # operationoutcome shall choose the most applicable code from the
        # issuetype value set, and may additional provide its own code for the
        # error in the details element.
        self.code = None
        # type = string
        # possible values: invalid, structure, required, value,
        # invariant, security, login, unknown, expired, forbidden, suppressed,
        # processing, not-supported, duplicate, not-found, too-long, code-invalid,
        # extension, too-costly, business-rule, conflict, incomplete, transient,
        # lock-error, no-store, exception, timeout, throttled, informational

        # additional details about the error. this may be a text description of
        # the error, or a system code that identifies the error.
        self.details = None
        # reference to CodeableConcept: CodeableConcept

        # additional diagnostic information about the issue.  typically, this may
        # be a description of how a value is erroneous, or a stack dump to help
        # trace the issue.
        self.diagnostics = None
        # type = string

        # for resource issues, this will be a simple xpath limited to element
        # names, repetition indicators and the default child access that
        # identifies one of the elements in the resource that caused this issue to
        # be raised.  for http errors, will be "http." + the parameter name.
        self.location = None
        # type = array

        # a simple fhirpath limited to element names, repetition indicators and
        # the default child access that identifies one of the elements in the
        # resource that caused this issue to be raised.
        self.expression = None
        # type = array

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.severity is not None:
            for value in self.severity:
                if value is not None and value.lower() not in [
                        'fatal', 'error', 'warning', 'information']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'fatal, error, warning, information'))

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                    'invalid', 'structure', 'required', 'value', 'invariant', 'security',
                    'login', 'unknown', 'expired', 'forbidden', 'suppressed', 'processing',
                    'not-supported', 'duplicate', 'not-found', 'too-long', 'code-invalid',
                    'extension', 'too-costly', 'business-rule', 'conflict', 'incomplete',
                    'transient', 'lock-error', 'no-store', 'exception', 'timeout',
                        'throttled', 'informational']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'invalid, structure, required, value, invariant, security, login,'
                        'unknown, expired, forbidden, suppressed, processing, not-supported,'
                        'duplicate, not-found, too-long, code-invalid, extension, too-costly,'
                        'business-rule, conflict, incomplete, transient, lock-error, no-store,'
                        'exception, timeout, throttled, informational'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'OperationOutcome_Issue',
             'child_variable': 'details'},
        ]
