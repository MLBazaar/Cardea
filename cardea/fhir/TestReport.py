from .fhirbase import fhirbase


class TestReport(fhirbase):
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport'

    def __init__(self, dict_values=None):
        # this is a testreport resource
        self.resourceType = 'TestReport'
        # type = string
        # possible values: TestReport

        # a free text natural language name identifying the executed testscript.
        self.name = None
        # type = string

        # the current state of this test report.
        self.status = None
        # type = string
        # possible values: completed, in-progress, waiting, stopped,
        # entered-in-error

        # ideally this is an absolute url that is used to identify the version-
        # specific testscript that was executed, matching the `testscript.url`.
        self.testScript = None
        # reference to Reference: identifier

        # the overall result from the execution of the testscript.
        self.result = None
        # type = string
        # possible values: pass, fail, pending

        # the final score (percentage of tests passed) resulting from the
        # execution of the testscript.
        self.score = None
        # type = int

        # name of the tester producing this report (organization or individual).
        self.tester = None
        # type = string

        # when the testscript was executed and this testreport was generated.
        self.issued = None
        # type = string

        # a participant in the test execution, either the execution engine, a
        # client, or a server.
        self.participant = None
        # type = array
        # reference to TestReport_Participant: TestReport_Participant

        # the results of the series of required setup operations before the tests
        # were executed.
        self.setup = None
        # reference to TestReport_Setup: TestReport_Setup

        # a test executed from the test script.
        self.test = None
        # type = array
        # reference to TestReport_Test: TestReport_Test

        # the results of the series of operations required to clean up after the
        # all the tests were executed (successfully or otherwise).
        self.teardown = None
        # reference to TestReport_Teardown: TestReport_Teardown

        # identifier for the testscript assigned for external purposes outside the
        # context of fhir.
        self.identifier = None
        # reference to Identifier: Identifier

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

            {'parent_entity': 'TestReport_Setup',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'setup'},

            {'parent_entity': 'TestReport_Test',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'test'},

            {'parent_entity': 'TestReport_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'participant'},

            {'parent_entity': 'TestReport_Teardown',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'teardown'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport',
             'child_variable': 'identifier'},
        ]


class TestReport_Participant(fhirbase):
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Participant'

    def __init__(self, dict_values=None):
        # the type of participant.
        self.type = None
        # type = string
        # possible values: test-engine, client, server

        # the uri of the participant. an absolute url is preferred.
        self.uri = None
        # type = string

        # the display name of the participant.
        self.display = None
        # type = string

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Setup'

    def __init__(self, dict_values=None):
        # action would contain either an operation or an assertion.
        self.action = None
        # type = array
        # reference to TestReport_Action: TestReport_Action

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Action'

    def __init__(self, dict_values=None):
        # the operation performed.
        self.operation = None
        # reference to TestReport_Operation: TestReport_Operation

        # the results of the assertion performed on the previous operations.
        self._assert = None
        # reference to TestReport_Assert: TestReport_Assert

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Operation'

    def __init__(self, dict_values=None):
        # the result of this operation.
        self.result = None
        # type = string
        # possible values: pass, skip, fail, warning, error

        # an explanatory message associated with the result.
        self.message = None
        # type = string

        # a link to further details on the result.
        self.detail = None
        # type = string

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Assert'

    def __init__(self, dict_values=None):
        # the result of this assertion.
        self.result = None
        # type = string
        # possible values: pass, skip, fail, warning, error

        # an explanatory message associated with the result.
        self.message = None
        # type = string

        # a link to further details on the result.
        self.detail = None
        # type = string

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Test'

    def __init__(self, dict_values=None):
        # the name of this test used for tracking/logging purposes by test
        # engines.
        self.name = None
        # type = string

        # a short description of the test used by test engines for tracking and
        # reporting purposes.
        self.description = None
        # type = string

        # action would contain either an operation or an assertion.
        self.action = None
        # type = array
        # reference to TestReport_Action1: TestReport_Action1

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Action1'

    def __init__(self, dict_values=None):
        # an operation would involve a rest request to a server.
        self.operation = None
        # reference to TestReport_Operation: TestReport_Operation

        # the results of the assertion performed on the previous operations.
        self._assert = None
        # reference to TestReport_Assert: TestReport_Assert

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Teardown'

    def __init__(self, dict_values=None):
        # the teardown action will only contain an operation.
        self.action = None
        # type = array
        # reference to TestReport_Action2: TestReport_Action2

        # unique identifier for object class
        self.object_id = None

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
    """A summary of information based on the results of executing a TestScript.
    """

    __name__ = 'TestReport_Action2'

    def __init__(self, dict_values=None):
        # an operation would involve a rest request to a server.
        self.operation = None
        # reference to TestReport_Operation: TestReport_Operation

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestReport_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestReport_Action2',
             'child_variable': 'operation'},
        ]
