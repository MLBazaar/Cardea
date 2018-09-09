from .fhirbase import fhirbase


class TestReport(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport'

    def __init__(self, dict_values=None):
        self.resourceType = 'TestReport'
        """
        This is a TestReport resource

        type: string
        possible values: TestReport
        """

        self.name = None
        """
        A free text natural language name identifying the executed TestScript.

        type: string
        """

        self.status = None
        """
        The current state of this test report.

        type: string
        possible values: completed, in-progress, waiting, stopped,
        entered-in-error
        """

        self.testScript = None
        """
        Ideally this is an absolute URL that is used to identify the
        version-specific TestScript that was executed, matching the
        `TestScript.url`.

        reference to Reference: identifier
        """

        self.result = None
        """
        The overall result from the execution of the TestScript.

        type: string
        possible values: pass, fail, pending
        """

        self.score = None
        """
        The final score (percentage of tests passed) resulting from the
        execution of the TestScript.

        type: int
        """

        self.tester = None
        """
        Name of the tester producing this report (Organization or individual).

        type: string
        """

        self.issued = None
        """
        When the TestScript was executed and this TestReport was generated.

        type: string
        """

        self.participant = None
        """
        A participant in the test execution, either the execution engine, a
        client, or a server.

        type: array
        reference to TestReport_Participant
        """

        self.setup = None
        """
        The results of the series of required setup operations before the
        tests were executed.

        reference to TestReport_Setup
        """

        self.test = None
        """
        A test executed from the test script.

        type: array
        reference to TestReport_Test
        """

        self.teardown = None
        """
        The results of the series of operations required to clean up after the
        all the tests were executed (successfully or otherwise).

        reference to TestReport_Teardown
        """

        self.identifier = None
        """
        Identifier for the TestScript assigned for external purposes outside
        the context of FHIR.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'completed', 'in-progress', 'waiting', 'stopped', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'completed, in-progress, waiting, stopped, entered-in-error'))

        if self.result is not None:
            for value in self.result:
                if value is not None and value.lower() not in [
                        'pass', 'fail', 'pending']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'pass, fail, pending'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestReport',
             'child_variable': 'testScript'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'identifier'},

            {'parent_entity': 'TestReport_Test',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'test'},

            {'parent_entity': 'TestReport_Setup',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'setup'},

            {'parent_entity': 'TestReport_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'participant'},

            {'parent_entity': 'TestReport_Teardown',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'teardown'},
        ]


class TestReport_Participant(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The type of participant.

        type: string
        possible values: test-engine, client, server
        """

        self.uri = None
        """
        The uri of the participant. An absolute URL is preferred.

        type: string
        """

        self.display = None
        """
        The display name of the participant.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'test-engine', 'client', 'server']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'test-engine, client, server'))


class TestReport_Setup(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Setup'

    def __init__(self, dict_values=None):
        self.action = None
        """
        Action would contain either an operation or an assertion.

        type: array
        reference to TestReport_Action
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Action',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Setup',
             'child_variable': 'action'},
        ]


class TestReport_Action(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Action'

    def __init__(self, dict_values=None):
        self.operation = None
        """
        The operation performed.

        reference to TestReport_Operation
        """

        self._assert = None
        """
        The results of the assertion performed on the previous operations.

        reference to TestReport_Assert
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action',
             'child_variable': 'operation'},

            {'parent_entity': 'TestReport_Assert',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action',
             'child_variable': '_assert'},
        ]


class TestReport_Operation(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Operation'

    def __init__(self, dict_values=None):
        self.result = None
        """
        The result of this operation.

        type: string
        possible values: pass, skip, fail, warning, error
        """

        self.message = None
        """
        An explanatory message associated with the result.

        type: string
        """

        self.detail = None
        """
        A link to further details on the result.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.result is not None:
            for value in self.result:
                if value is not None and value.lower() not in [
                        'pass', 'skip', 'fail', 'warning', 'error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'pass, skip, fail, warning, error'))


class TestReport_Assert(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Assert'

    def __init__(self, dict_values=None):
        self.result = None
        """
        The result of this assertion.

        type: string
        possible values: pass, skip, fail, warning, error
        """

        self.message = None
        """
        An explanatory message associated with the result.

        type: string
        """

        self.detail = None
        """
        A link to further details on the result.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.result is not None:
            for value in self.result:
                if value is not None and value.lower() not in [
                        'pass', 'skip', 'fail', 'warning', 'error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'pass, skip, fail, warning, error'))


class TestReport_Test(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Test'

    def __init__(self, dict_values=None):
        self.name = None
        """
        The name of this test used for tracking/logging purposes by test
        engines.

        type: string
        """

        self.description = None
        """
        A short description of the test used by test engines for tracking and
        reporting purposes.

        type: string
        """

        self.action = None
        """
        Action would contain either an operation or an assertion.

        type: array
        reference to TestReport_Action1
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Action1',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Test',
             'child_variable': 'action'},
        ]


class TestReport_Action1(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Action1'

    def __init__(self, dict_values=None):
        self.operation = None
        """
        An operation would involve a REST request to a server.

        reference to TestReport_Operation
        """

        self._assert = None
        """
        The results of the assertion performed on the previous operations.

        reference to TestReport_Assert
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action1',
             'child_variable': 'operation'},

            {'parent_entity': 'TestReport_Assert',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action1',
             'child_variable': '_assert'},
        ]


class TestReport_Teardown(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Teardown'

    def __init__(self, dict_values=None):
        self.action = None
        """
        The teardown action will only contain an operation.

        type: array
        reference to TestReport_Action2
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Action2',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Teardown',
             'child_variable': 'action'},
        ]


class TestReport_Action2(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.
    """

    __name__ = 'TestReport_Action2'

    def __init__(self, dict_values=None):
        self.operation = None
        """
        An operation would involve a REST request to a server.

        reference to TestReport_Operation
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action2',
             'child_variable': 'operation'},
        ]
