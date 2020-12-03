from .fhirbase import fhirbase


class TestReport(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.

    Args:
        resourceType: This is a TestReport resource
        identifier: Identifier for the TestScript assigned for external
            purposes outside the context of FHIR.
        name: A free text natural language name identifying the executed
            TestScript.
        status: The current state of this test report.
        testScript: Ideally this is an absolute URL that is used to identify
            the version-specific TestScript that was executed, matching the
            `TestScript.url`.
        result: The overall result from the execution of the TestScript.
        score: The final score (percentage of tests passed) resulting from the
            execution of the TestScript.
        tester: Name of the tester producing this report (Organization or
            individual).
        issued: When the TestScript was executed and this TestReport was
            generated.
        participant: A participant in the test execution, either the execution
            engine, a client, or a server.
        setup: The results of the series of required setup operations before
            the tests were executed.
        test: A test executed from the test script.
        teardown: The results of the series of operations required to clean up
            after the all the tests were executed (successfully or otherwise).
    """

    __name__ = 'TestReport'

    def __init__(self, dict_values=None):
        self.resourceType = 'TestReport'
        # type: str
        # possible values: TestReport

        self.name = None
        # type: str

        self.status = None
        # type: str
        # possible values: completed, in-progress, waiting, stopped,
        # entered-in-error

        self.testScript = None
        # reference to Reference: identifier

        self.result = None
        # type: str
        # possible values: pass, fail, pending

        self.score = None
        # type: int

        self.tester = None
        # type: str

        self.issued = None
        # type: str

        self.participant = None
        # type: list
        # reference to TestReport_Participant

        self.setup = None
        # reference to TestReport_Setup

        self.test = None
        # type: list
        # reference to TestReport_Test

        self.teardown = None
        # reference to TestReport_Teardown

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'TestReport_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'participant'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestReport',
             'child_variable': 'testScript'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'identifier'},

            {'parent_entity': 'TestReport_Teardown',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'teardown'},

            {'parent_entity': 'TestReport_Setup',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'setup'},

            {'parent_entity': 'TestReport_Test',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'test'},
        ]


class TestReport_Participant(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.

    Args:
        type: The type of participant.
        uri: The uri of the participant. An absolute URL is preferred.
        display: The display name of the participant.
    """

    __name__ = 'TestReport_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: test-engine, client, server

        self.uri = None
        # type: str

        self.display = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        action: Action would contain either an operation or an assertion.
    """

    __name__ = 'TestReport_Setup'

    def __init__(self, dict_values=None):
        self.action = None
        # type: list
        # reference to TestReport_Action

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

    Args:
        operation: The operation performed.
        assert: The results of the assertion performed on the previous
            operations.
    """

    __name__ = 'TestReport_Action'

    def __init__(self, dict_values=None):
        self.operation = None
        # reference to TestReport_Operation

        self._assert = None
        # reference to TestReport_Assert

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

    Args:
        result: The result of this operation.
        message: An explanatory message associated with the result.
        detail: A link to further details on the result.
    """

    __name__ = 'TestReport_Operation'

    def __init__(self, dict_values=None):
        self.result = None
        # type: str
        # possible values: pass, skip, fail, warning, error

        self.message = None
        # type: str

        self.detail = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        result: The result of this assertion.
        message: An explanatory message associated with the result.
        detail: A link to further details on the result.
    """

    __name__ = 'TestReport_Assert'

    def __init__(self, dict_values=None):
        self.result = None
        # type: str
        # possible values: pass, skip, fail, warning, error

        self.message = None
        # type: str

        self.detail = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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

    Args:
        name: The name of this test used for tracking/logging purposes by test
            engines.
        description: A short description of the test used by test engines for
            tracking and reporting purposes.
        action: Action would contain either an operation or an assertion.
    """

    __name__ = 'TestReport_Test'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.description = None
        # type: str

        self.action = None
        # type: list
        # reference to TestReport_Action1

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

    Args:
        operation: An operation would involve a REST request to a server.
        assert: The results of the assertion performed on the previous
            operations.
    """

    __name__ = 'TestReport_Action1'

    def __init__(self, dict_values=None):
        self.operation = None
        # reference to TestReport_Operation

        self._assert = None
        # reference to TestReport_Assert

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Assert',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action1',
             'child_variable': '_assert'},

            {'parent_entity': 'TestReport_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action1',
             'child_variable': 'operation'},
        ]


class TestReport_Teardown(fhirbase):
    """
    A summary of information based on the results of executing a
    TestScript.

    Args:
        action: The teardown action will only contain an operation.
    """

    __name__ = 'TestReport_Teardown'

    def __init__(self, dict_values=None):
        self.action = None
        # type: list
        # reference to TestReport_Action2

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

    Args:
        operation: An operation would involve a REST request to a server.
    """

    __name__ = 'TestReport_Action2'

    def __init__(self, dict_values=None):
        self.operation = None
        # reference to TestReport_Operation

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
