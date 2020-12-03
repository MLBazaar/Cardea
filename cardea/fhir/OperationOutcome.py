from .fhirbase import fhirbase


class OperationOutcome(fhirbase):
    """
    A collection of error, warning or information messages that result
    from a system action.

    Args:
        resourceType: This is a OperationOutcome resource
        issue: An error, warning or information message that results from a
            system action.
    """

    __name__ = 'OperationOutcome'

    def __init__(self, dict_values=None):
        self.resourceType = 'OperationOutcome'
        # type: str
        # possible values: OperationOutcome

        self.issue = None
        # type: list
        # reference to OperationOutcome_Issue

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'OperationOutcome_Issue',
             'parent_variable': 'object_id',
             'child_entity': 'OperationOutcome',
             'child_variable': 'issue'},
        ]


class OperationOutcome_Issue(fhirbase):
    """
    A collection of error, warning or information messages that result
    from a system action.

    Args:
        severity: Indicates whether the issue indicates a variation from
            successful processing.
        code: Describes the type of the issue. The system that creates an
            OperationOutcome SHALL choose the most applicable code from the
            IssueType value set, and may additional provide its own code for the
            error in the details element.
        details: Additional details about the error. This may be a text
            description of the error, or a system code that identifies the error.
        diagnostics: Additional diagnostic information about the issue.
            Typically, this may be a description of how a value is erroneous, or a
            stack dump to help trace the issue.
        location: For resource issues, this will be a simple XPath limited to
            element names, repetition indicators and the default child access that
            identifies one of the elements in the resource that caused this issue
            to be raised.  For HTTP errors, will be "http." + the parameter name.
        expression: A simple FHIRPath limited to element names, repetition
            indicators and the default child access that identifies one of the
            elements in the resource that caused this issue to be raised.
    """

    __name__ = 'OperationOutcome_Issue'

    def __init__(self, dict_values=None):
        self.severity = None
        # type: str
        # possible values: fatal, error, warning, information

        self.code = None
        # type: str
        # possible values: invalid, structure, required, value,
        # invariant, security, login, unknown, expired, forbidden, suppressed,
        # processing, not-supported, duplicate, not-found, too-long,
        # code-invalid, extension, too-costly, business-rule, conflict,
        # incomplete, transient, lock-error, no-store, exception, timeout,
        # throttled, informational

        self.details = None
        # reference to CodeableConcept

        self.diagnostics = None
        # type: str

        self.location = None
        # type: list

        self.expression = None
        # type: list

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
                    'login', 'unknown', 'expired', 'forbidden', 'suppressed',
                    'processing', 'not-supported', 'duplicate', 'not-found', 'too-long',
                    'code-invalid', 'extension', 'too-costly', 'business-rule',
                    'conflict', 'incomplete', 'transient', 'lock-error', 'no-store',
                        'exception', 'timeout', 'throttled', 'informational']:
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
