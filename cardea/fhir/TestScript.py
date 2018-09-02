from .fhirbase import fhirbase


class TestScript(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # this is a testscript resource
        self.resourceType = 'TestScript'
        # type = string
        # possible values: TestScript

        # an absolute uri that is used to identify this test script when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this test script is (or will be) published. the url should include the
        # major version of the test script. for more information see [technical
        # and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the test script
        # when it is referenced in a specification, model, design or instance.
        # this is an arbitrary value managed by the test script author and is not
        # expected to be globally unique. for example, it might be a timestamp
        # (e.g. yyyymmdd) if a managed version is not available. there is also no
        # expectation that versions can be placed in a lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the test script. this name should be
        # usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the test script.
        self.title = None
        # type = string

        # the status of this test script. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this test script is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the test script was published. the
        # date must change if and when the business version changes and it must
        # change if the status code changes. in addition, it should change when
        # the substantive content of the test script changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the test
        # script.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the test script from a
        # consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate test script instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the test script is intended to be
        # used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this test script is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the test script and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the test script.
        self.copyright = None
        # type = string

        # an abstract server used in operations within this test script in the
        # origin element.
        self.origin = None
        # type = array
        # reference to TestScript_Origin: TestScript_Origin

        # an abstract server used in operations within this test script in the
        # destination element.
        self.destination = None
        # type = array
        # reference to TestScript_Destination: TestScript_Destination

        # the required capability must exist and are assumed to function correctly
        # on the fhir server being tested.
        self.metadata = None
        # reference to TestScript_Metadata: TestScript_Metadata

        # fixture in the test script - by reference (uri). all fixtures are
        # required for the test script to execute.
        self.fixture = None
        # type = array
        # reference to TestScript_Fixture: TestScript_Fixture

        # reference to the profile to be used for validation.
        self.profile = None
        # type = array
        # reference to Reference: identifier

        # variable is set based either on element value in response body or on
        # header field value in the response headers.
        self.variable = None
        # type = array
        # reference to TestScript_Variable: TestScript_Variable

        # assert rule to be used in one or more asserts within the test script.
        self.rule = None
        # type = array
        # reference to TestScript_Rule: TestScript_Rule

        # contains one or more rules.  offers a way to group rules so assertions
        # could reference the group of rules and have them all applied.
        self.ruleset = None
        # type = array
        # reference to TestScript_Ruleset: TestScript_Ruleset

        # a series of required setup operations before tests are executed.
        self.setup = None
        # reference to TestScript_Setup: TestScript_Setup

        # a test in this script.
        self.test = None
        # type = array
        # reference to TestScript_Test: TestScript_Test

        # a series of operations required to clean up after the all the tests are
        # executed (successfully or otherwise).
        self.teardown = None
        # reference to TestScript_Teardown: TestScript_Teardown

        # a formal identifier that is used to identify this test script when it is
        # represented in other formats, or referenced in a specification, model,
        # design or an instance.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Ruleset',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'ruleset'},

            {'parent_entity': 'TestScript_Setup',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'setup'},

            {'parent_entity': 'TestScript_Destination',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'destination'},

            {'parent_entity': 'TestScript_Variable',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'variable'},

            {'parent_entity': 'TestScript_Origin',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'origin'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'TestScript_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'rule'},

            {'parent_entity': 'TestScript_Fixture',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'fixture'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'useContext'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript',
             'child_variable': 'profile'},

            {'parent_entity': 'TestScript_Test',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'test'},

            {'parent_entity': 'TestScript_Teardown',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'teardown'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'contact'},

            {'parent_entity': 'TestScript_Metadata',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'metadata'},
        ]


class TestScript_Origin(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # abstract name given to an origin server in this test script.  the name
        # is provided as a number starting at 1.
        self.index = None
        # type = int

        # the type of origin profile the test system supports.
        self.profile = None
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Origin',
             'child_variable': 'profile'},
        ]


class TestScript_Destination(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # abstract name given to a destination server in this test script.  the
        # name is provided as a number starting at 1.
        self.index = None
        # type = int

        # the type of destination profile the test system supports.
        self.profile = None
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Destination',
             'child_variable': 'profile'},
        ]


class TestScript_Metadata(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # a link to the fhir specification that this test is covering.
        self.link = None
        # type = array
        # reference to TestScript_Link: TestScript_Link

        # capabilities that must exist and are assumed to function correctly on
        # the fhir server being tested.
        self.capability = None
        # type = array
        # reference to TestScript_Capability: TestScript_Capability

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Capability',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Metadata',
             'child_variable': 'capability'},

            {'parent_entity': 'TestScript_Link',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Metadata',
             'child_variable': 'link'},
        ]


class TestScript_Link(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # url to a particular requirement or feature within the fhir
        # specification.
        self.url = None
        # type = string

        # short description of the link.
        self.description = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Capability(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # whether or not the test execution will require the given capabilities of
        # the server in order for this test script to execute.
        self.required = None
        # type = boolean

        # whether or not the test execution will validate the given capabilities
        # of the server in order for this test script to execute.
        self.validated = None
        # type = boolean

        # description of the capabilities that this test script is requiring the
        # server to support.
        self.description = None
        # type = string

        # which origin server these requirements apply to.
        self.origin = None
        # type = array

        # which server these requirements apply to.
        self.destination = None
        # type = int

        # links to the fhir specification that describes this interaction and the
        # resources involved in more detail.
        self.link = None
        # type = array

        # minimum capabilities required of server for test script to execute
        # successfully.   if server does not meet at a minimum the referenced
        # capability statement, then all tests in this script are skipped.
        self.capabilities = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript_Capability',
             'child_variable': 'capabilities'},
        ]


class TestScript_Fixture(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # whether or not to implicitly create the fixture during setup. if true,
        # the fixture is automatically created on each server being tested during
        # setup, therefore no create operation is required for this fixture in the
        # testscript.setup section.
        self.autocreate = None
        # type = boolean

        # whether or not to implicitly delete the fixture during teardown. if
        # true, the fixture is automatically deleted on each server being tested
        # during teardown, therefore no delete operation is required for this
        # fixture in the testscript.teardown section.
        self.autodelete = None
        # type = boolean

        # reference to the resource (containing the contents of the resource
        # needed for operations).
        self.resource = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript_Fixture',
             'child_variable': 'resource'},
        ]


class TestScript_Variable(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # descriptive name for this variable.
        self.name = None
        # type = string

        # a default, hard-coded, or user-defined value for this variable.
        self.defaultValue = None
        # type = string

        # a free text natural language description of the variable and its
        # purpose.
        self.description = None
        # type = string

        # the fluentpath expression to evaluate against the fixture body. when
        # variables are defined, only one of either expression, headerfield or
        # path must be specified.
        self.expression = None
        # type = string

        # will be used to grab the http header field value from the headers that
        # sourceid is pointing to.
        self.headerField = None
        # type = string

        # displayable text string with hint help information to the user when
        # entering a default value.
        self.hint = None
        # type = string

        # xpath or jsonpath to evaluate against the fixture body.  when variables
        # are defined, only one of either expression, headerfield or path must be
        # specified.
        self.path = None
        # type = string

        # fixture to evaluate the xpath/jsonpath expression or the headerfield
        # against within this variable.
        self.sourceId = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Rule(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # reference to the resource (containing the contents of the rule needed
        # for assertions).
        self.resource = None
        # reference to Reference: identifier

        # each rule template can take one or more parameters for rule evaluation.
        self.param = None
        # type = array
        # reference to TestScript_Param: TestScript_Param

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Param',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Rule',
             'child_variable': 'param'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript_Rule',
             'child_variable': 'resource'},
        ]


class TestScript_Param(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # descriptive name for this parameter that matches the external assert
        # rule parameter name.
        self.name = None
        # type = string

        # the explicit or dynamic value for the parameter that will be passed on
        # to the external rule template.
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Ruleset(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # reference to the resource (containing the contents of the ruleset needed
        # for assertions).
        self.resource = None
        # reference to Reference: identifier

        # the referenced rule within the external ruleset template.
        self.rule = None
        # type = array
        # reference to TestScript_Rule1: TestScript_Rule1

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Rule1',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Ruleset',
             'child_variable': 'rule'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript_Ruleset',
             'child_variable': 'resource'},
        ]


class TestScript_Rule1(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # id of the referenced rule within the external ruleset template.
        self.ruleId = None
        # type = string

        # each rule template can take one or more parameters for rule evaluation.
        self.param = None
        # type = array
        # reference to TestScript_Param1: TestScript_Param1

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Param1',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Rule1',
             'child_variable': 'param'},
        ]


class TestScript_Param1(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # descriptive name for this parameter that matches the external assert
        # ruleset rule parameter name.
        self.name = None
        # type = string

        # the value for the parameter that will be passed on to the external
        # ruleset rule template.
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Setup(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # action would contain either an operation or an assertion.
        self.action = None
        # type = array
        # reference to TestScript_Action: TestScript_Action

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Action',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Setup',
             'child_variable': 'action'},
        ]


class TestScript_Action(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # the operation to perform.
        self.operation = None
        # reference to TestScript_Operation: TestScript_Operation

        # evaluates the results of previous operations to determine if the server
        # under test behaves appropriately.
        self._assert = None
        # reference to TestScript_Assert: TestScript_Assert

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Assert',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action',
             'child_variable': '_assert'},

            {'parent_entity': 'TestScript_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action',
             'child_variable': 'operation'},
        ]


class TestScript_Operation(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # server interaction or operation type.
        self.type = None
        # reference to Coding: Coding

        # the type of the resource.  see http://build.fhir.org/resourcelist.html.
        self.resource = None
        # type = string

        # the label would be used for tracking/logging purposes by test engines.
        self.label = None
        # type = string

        # the description would be used by test engines for tracking and reporting
        # purposes.
        self.description = None
        # type = string

        # the content-type or mime-type to use for restful operation in the
        # 'accept' header.
        self.accept = None
        # type = string
        # possible values: xml, json, ttl, none

        # the content-type or mime-type to use for restful operation in the
        # 'content-type' header.
        self.contentType = None
        # type = string
        # possible values: xml, json, ttl, none

        # the server where the request message is destined for.  must be one of
        # the server numbers listed in testscript.destination section.
        self.destination = None
        # type = int

        # whether or not to implicitly send the request url in encoded format. the
        # default is true to match the standard restful client behavior. set to
        # false when communicating with a server that does not support encoded url
        # paths.
        self.encodeRequestUrl = None
        # type = boolean

        # the server where the request message originates from.  must be one of
        # the server numbers listed in testscript.origin section.
        self.origin = None
        # type = int

        # path plus parameters after [type].  used to set parts of the request url
        # explicitly.
        self.params = None
        # type = string

        # header elements would be used to set http headers.
        self.requestHeader = None
        # type = array
        # reference to TestScript_RequestHeader: TestScript_RequestHeader

        # the fixture id (maybe new) to map to the request.
        self.requestId = None
        # type = string

        # the fixture id (maybe new) to map to the response.
        self.responseId = None
        # type = string

        # the id of the fixture used as the body of a put or post request.
        self.sourceId = None
        # type = string

        # id of fixture used for extracting the [id],  [type], and [vid] for get
        # requests.
        self.targetId = None
        # type = string

        # complete request url.
        self.url = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.accept is not None:
            for value in self.accept:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

        if self.contentType is not None:
            for value in self.contentType:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

        if self.accept is not None:
            for value in self.accept:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

        if self.contentType is not None:
            for value in self.contentType:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

        if self.accept is not None:
            for value in self.accept:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

        if self.contentType is not None:
            for value in self.contentType:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Operation',
             'child_variable': 'type'},

            {'parent_entity': 'TestScript_RequestHeader',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Operation',
             'child_variable': 'requestHeader'},
        ]


class TestScript_RequestHeader(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # the http header field e.g. "accept".
        self.field = None
        # type = string

        # the value of the header e.g. "application/fhir+xml".
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Assert(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # the label would be used for tracking/logging purposes by test engines.
        self.label = None
        # type = string

        # the description would be used by test engines for tracking and reporting
        # purposes.
        self.description = None
        # type = string

        # the direction to use for the assertion.
        self.direction = None
        # type = string
        # possible values: response, request

        # id of the source fixture used as the contents to be evaluated by either
        # the "source/expression" or "sourceid/path" definition.
        self.compareToSourceId = None
        # type = string

        # the fluentpath expression to evaluate against the source fixture. when
        # comparetosourceid is defined, either comparetosourceexpression or
        # comparetosourcepath must be defined, but not both.
        self.compareToSourceExpression = None
        # type = string

        # xpath or jsonpath expression to evaluate against the source fixture.
        # when comparetosourceid is defined, either comparetosourceexpression or
        # comparetosourcepath must be defined, but not both.
        self.compareToSourcePath = None
        # type = string

        # the content-type or mime-type to use for restful operation in the
        # 'content-type' header.
        self.contentType = None
        # type = string
        # possible values: xml, json, ttl, none

        # the fluentpath expression to be evaluated against the request or
        # response message contents - http headers and payload.
        self.expression = None
        # type = string

        # the http header field name e.g. 'location'.
        self.headerField = None
        # type = string

        # the id of a fixture.  asserts that the response contains at a minimum
        # the fixture specified by minimumid.
        self.minimumId = None
        # type = string

        # whether or not the test execution performs validation on the bundle
        # navigation links.
        self.navigationLinks = None
        # type = boolean

        # the operator type defines the conditional behavior of the assert. if not
        # defined, the default is equals.
        self.operator = None
        # type = string
        # possible values: equals, notEquals, in, notIn, greaterThan,
        # lessThan, empty, notEmpty, contains, notContains, eval

        # the xpath or jsonpath expression to be evaluated against the fixture
        # representing the response received from server.
        self.path = None
        # type = string

        # the request method or http operation code to compare against that used
        # by the client system under test.
        self.requestMethod = None
        # type = string
        # possible values: delete, get, options, patch, post, put

        # the value to use in a comparison against the request url path string.
        self.requestURL = None
        # type = string

        # the type of the resource.  see http://build.fhir.org/resourcelist.html.
        self.resource = None
        # type = string

        # okay | created | nocontent | notmodified | bad | forbidden | notfound |
        # methodnotallowed | conflict | gone | preconditionfailed | unprocessable.
        self.response = None
        # type = string
        # possible values: okay, created, noContent, notModified, bad,
        # forbidden, notFound, methodNotAllowed, conflict, gone,
        # preconditionFailed, unprocessable

        # the value of the http response code to be tested.
        self.responseCode = None
        # type = string

        # the testscript.rule this assert will evaluate.
        self.rule = None
        # reference to TestScript_Rule2: TestScript_Rule2

        # the testscript.ruleset this assert will evaluate.
        self.ruleset = None
        # reference to TestScript_Ruleset1: TestScript_Ruleset1

        # fixture to evaluate the xpath/jsonpath expression or the headerfield
        # against.
        self.sourceId = None
        # type = string

        # the id of the profile to validate against.
        self.validateProfileId = None
        # type = string

        # the value to compare to.
        self.value = None
        # type = string

        # whether or not the test execution will produce a warning only on error
        # for this assert.
        self.warningOnly = None
        # type = boolean

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.direction is not None:
            for value in self.direction:
                if value is not None and value.lower() not in [
                        'response', 'request']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'response, request'))

        if self.contentType is not None:
            for value in self.contentType:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

        if self.operator is not None:
            for value in self.operator:
                if value is not None and value.lower() not in [
                    'equals', 'notequals', 'in', 'notin', 'greaterthan', 'lessthan',
                        'empty', 'notempty', 'contains', 'notcontains', 'eval']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'equals, notEquals, in, notIn, greaterThan, lessThan,'
                        'empty, notEmpty, contains, notContains, eval'))

        if self.requestMethod is not None:
            for value in self.requestMethod:
                if value is not None and value.lower() not in [
                        'delete', 'get', 'options', 'patch', 'post', 'put']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'delete, get, options, patch, post, put'))

        if self.response is not None:
            for value in self.response:
                if value is not None and value.lower() not in [
                    'okay', 'created', 'nocontent', 'notmodified', 'bad', 'forbidden',
                    'notfound', 'methodnotallowed', 'conflict', 'gone',
                        'preconditionfailed', 'unprocessable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'okay, created, noContent, notModified, bad, forbidden, notFound,'
                        'methodNotAllowed, conflict, gone, preconditionFailed, unprocessable'))

        if self.direction is not None:
            for value in self.direction:
                if value is not None and value.lower() not in [
                        'response', 'request']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'response, request'))

        if self.contentType is not None:
            for value in self.contentType:
                if value is not None and value.lower() not in [
                        'xml', 'json', 'ttl', 'none']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'xml, json, ttl, none'))

        if self.operator is not None:
            for value in self.operator:
                if value is not None and value.lower() not in [
                    'equals', 'notequals', 'in', 'notin', 'greaterthan', 'lessthan',
                        'empty', 'notempty', 'contains', 'notcontains', 'eval']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'equals, notEquals, in, notIn, greaterThan, lessThan,'
                        'empty, notEmpty, contains, notContains, eval'))

        if self.requestMethod is not None:
            for value in self.requestMethod:
                if value is not None and value.lower() not in [
                        'delete', 'get', 'options', 'patch', 'post', 'put']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'delete, get, options, patch, post, put'))

        if self.response is not None:
            for value in self.response:
                if value is not None and value.lower() not in [
                    'okay', 'created', 'nocontent', 'notmodified', 'bad', 'forbidden',
                    'notfound', 'methodnotallowed', 'conflict', 'gone',
                        'preconditionfailed', 'unprocessable']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'okay, created, noContent, notModified, bad, forbidden, notFound,'
                        'methodNotAllowed, conflict, gone, preconditionFailed, unprocessable'))

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Rule2',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Assert',
             'child_variable': 'rule'},

            {'parent_entity': 'TestScript_Ruleset1',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Assert',
             'child_variable': 'ruleset'},
        ]


class TestScript_Rule2(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # the testscript.rule id value this assert will evaluate.
        self.ruleId = None
        # type = string

        # each rule template can take one or more parameters for rule evaluation.
        self.param = None
        # type = array
        # reference to TestScript_Param2: TestScript_Param2

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Param2',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Rule2',
             'child_variable': 'param'},
        ]


class TestScript_Param2(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # descriptive name for this parameter that matches the external assert
        # rule parameter name.
        self.name = None
        # type = string

        # the value for the parameter that will be passed on to the external rule
        # template.
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Ruleset1(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # the testscript.ruleset id value this assert will evaluate.
        self.rulesetId = None
        # type = string

        # the referenced rule within the external ruleset template.
        self.rule = None
        # type = array
        # reference to TestScript_Rule3: TestScript_Rule3

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Rule3',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Ruleset1',
             'child_variable': 'rule'},
        ]


class TestScript_Rule3(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # id of the referenced rule within the external ruleset template.
        self.ruleId = None
        # type = string

        # each rule template can take one or more parameters for rule evaluation.
        self.param = None
        # type = array
        # reference to TestScript_Param3: TestScript_Param3

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Param3',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Rule3',
             'child_variable': 'param'},
        ]


class TestScript_Param3(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # descriptive name for this parameter that matches the external assert
        # ruleset rule parameter name.
        self.name = None
        # type = string

        # the value for the parameter that will be passed on to the external
        # ruleset rule template.
        self.value = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Test(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

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
        # reference to TestScript_Action1: TestScript_Action1

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Action1',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Test',
             'child_variable': 'action'},
        ]


class TestScript_Action1(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # an operation would involve a rest request to a server.
        self.operation = None
        # reference to TestScript_Operation: TestScript_Operation

        # evaluates the results of previous operations to determine if the server
        # under test behaves appropriately.
        self._assert = None
        # reference to TestScript_Assert: TestScript_Assert

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Assert',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action1',
             'child_variable': '_assert'},

            {'parent_entity': 'TestScript_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action1',
             'child_variable': 'operation'},
        ]


class TestScript_Teardown(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # the teardown action will only contain an operation.
        self.action = None
        # type = array
        # reference to TestScript_Action2: TestScript_Action2

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Action2',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Teardown',
             'child_variable': 'action'},
        ]


class TestScript_Action2(fhirbase):
    """A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    def __init__(self, dict_values=None):
        # an operation would involve a rest request to a server.
        self.operation = None
        # reference to TestScript_Operation: TestScript_Operation

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action2',
             'child_variable': 'operation'},
        ]
