from .fhirbase import fhirbase


class TestScript(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        resourceType: This is a TestScript resource
        url: An absolute URI that is used to identify this test script when it
            is referenced in a specification, model, design or an instance. This
            SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
            which this test script is (or will be) published. The URL SHOULD
            include the major version of the test script. For more information see
            [Technical and Business Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this test
            script when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            test script when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the test script author
            and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There
            is also no expectation that versions can be placed in a
            lexicographical sequence.
        name: A natural language name identifying the test script. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the test script.
        status: The status of this test script. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this test script is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the test script was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the test script changes.
        publisher: The name of the individual or organization that published
            the test script.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the test
            script from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate test script
            instances.
        jurisdiction: A legal or geographic region in which the test script is
            intended to be used.
        purpose: Explaination of why this test script is needed and why it has
            been designed as it has.
        copyright: A copyright statement relating to the test script and/or
            its contents. Copyright statements are generally legal restrictions on
            the use and publishing of the test script.
        origin: An abstract server used in operations within this test script
            in the origin element.
        destination: An abstract server used in operations within this test
            script in the destination element.
        metadata: The required capability must exist and are assumed to
            function correctly on the FHIR server being tested.
        fixture: Fixture in the test script - by reference (uri). All fixtures
            are required for the test script to execute.
        profile: Reference to the profile to be used for validation.
        variable: Variable is set based either on element value in response
            body or on header field value in the response headers.
        rule: Assert rule to be used in one or more asserts within the test
            script.
        ruleset: Contains one or more rules.  Offers a way to group rules so
            assertions could reference the group of rules and have them all
            applied.
        setup: A series of required setup operations before tests are
            executed.
        test: A test in this script.
        teardown: A series of operations required to clean up after the all
            the tests are executed (successfully or otherwise).
    """

    __name__ = 'TestScript'

    def __init__(self, dict_values=None):
        self.resourceType = 'TestScript'
        # type: str
        # possible values: TestScript

        self.url = None
        # type: str

        self.version = None
        # type: str

        self.name = None
        # type: str

        self.title = None
        # type: str

        self.status = None
        # type: str
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # type: bool

        self.date = None
        # type: str

        self.publisher = None
        # type: str

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.description = None
        # type: str

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.purpose = None
        # type: str

        self.copyright = None
        # type: str

        self.origin = None
        # type: list
        # reference to TestScript_Origin

        self.destination = None
        # type: list
        # reference to TestScript_Destination

        self.metadata = None
        # reference to TestScript_Metadata

        self.fixture = None
        # type: list
        # reference to TestScript_Fixture

        self.profile = None
        # type: list
        # reference to Reference: identifier

        self.variable = None
        # type: list
        # reference to TestScript_Variable

        self.rule = None
        # type: list
        # reference to TestScript_Rule

        self.ruleset = None
        # type: list
        # reference to TestScript_Ruleset

        self.setup = None
        # reference to TestScript_Setup

        self.test = None
        # type: list
        # reference to TestScript_Test

        self.teardown = None
        # reference to TestScript_Teardown

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'useContext'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript',
             'child_variable': 'profile'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'identifier'},

            {'parent_entity': 'TestScript_Fixture',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'fixture'},

            {'parent_entity': 'TestScript_Teardown',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'teardown'},

            {'parent_entity': 'TestScript_Ruleset',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'ruleset'},

            {'parent_entity': 'TestScript_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'rule'},

            {'parent_entity': 'TestScript_Variable',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'variable'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'TestScript_Metadata',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'metadata'},

            {'parent_entity': 'TestScript_Origin',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'origin'},

            {'parent_entity': 'TestScript_Destination',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'destination'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'contact'},

            {'parent_entity': 'TestScript_Test',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'test'},

            {'parent_entity': 'TestScript_Setup',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'setup'},
        ]


class TestScript_Origin(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        index: Abstract name given to an origin server in this test script.
            The name is provided as a number starting at 1.
        profile: The type of origin profile the test system supports.
    """

    __name__ = 'TestScript_Origin'

    def __init__(self, dict_values=None):
        self.index = None
        # type: int

        self.profile = None
        # reference to Coding

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        index: Abstract name given to a destination server in this test
            script.  The name is provided as a number starting at 1.
        profile: The type of destination profile the test system supports.
    """

    __name__ = 'TestScript_Destination'

    def __init__(self, dict_values=None):
        self.index = None
        # type: int

        self.profile = None
        # reference to Coding

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        link: A link to the FHIR specification that this test is covering.
        capability: Capabilities that must exist and are assumed to function
            correctly on the FHIR server being tested.
    """

    __name__ = 'TestScript_Metadata'

    def __init__(self, dict_values=None):
        self.link = None
        # type: list
        # reference to TestScript_Link

        self.capability = None
        # type: list
        # reference to TestScript_Capability

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Link',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Metadata',
             'child_variable': 'link'},

            {'parent_entity': 'TestScript_Capability',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Metadata',
             'child_variable': 'capability'},
        ]


class TestScript_Link(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        url: URL to a particular requirement or feature within the FHIR
            specification.
        description: Short description of the link.
    """

    __name__ = 'TestScript_Link'

    def __init__(self, dict_values=None):
        self.url = None
        # type: str

        self.description = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Capability(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        required: Whether or not the test execution will require the given
            capabilities of the server in order for this test script to execute.
        validated: Whether or not the test execution will validate the given
            capabilities of the server in order for this test script to execute.
        description: Description of the capabilities that this test script is
            requiring the server to support.
        origin: Which origin server these requirements apply to.
        destination: Which server these requirements apply to.
        link: Links to the FHIR specification that describes this interaction
            and the resources involved in more detail.
        capabilities: Minimum capabilities required of server for test script
            to execute successfully.   If server does not meet at a minimum the
            referenced capability statement, then all tests in this script are
            skipped.
    """

    __name__ = 'TestScript_Capability'

    def __init__(self, dict_values=None):
        self.required = None
        # type: bool

        self.validated = None
        # type: bool

        self.description = None
        # type: str

        self.origin = None
        # type: list

        self.destination = None
        # type: int

        self.link = None
        # type: list

        self.capabilities = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        autocreate: Whether or not to implicitly create the fixture during
            setup. If true, the fixture is automatically created on each server
            being tested during setup, therefore no create operation is required
            for this fixture in the TestScript.setup section.
        autodelete: Whether or not to implicitly delete the fixture during
            teardown. If true, the fixture is automatically deleted on each server
            being tested during teardown, therefore no delete operation is
            required for this fixture in the TestScript.teardown section.
        resource: Reference to the resource (containing the contents of the
            resource needed for operations).
    """

    __name__ = 'TestScript_Fixture'

    def __init__(self, dict_values=None):
        self.autocreate = None
        # type: bool

        self.autodelete = None
        # type: bool

        self.resource = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        name: Descriptive name for this variable.
        defaultValue: A default, hard-coded, or user-defined value for this
            variable.
        description: A free text natural language description of the variable
            and its purpose.
        expression: The fluentpath expression to evaluate against the fixture
            body. When variables are defined, only one of either expression,
            headerField or path must be specified.
        headerField: Will be used to grab the HTTP header field value from the
            headers that sourceId is pointing to.
        hint: Displayable text string with hint help information to the user
            when entering a default value.
        path: XPath or JSONPath to evaluate against the fixture body.  When
            variables are defined, only one of either expression, headerField or
            path must be specified.
        sourceId: Fixture to evaluate the XPath/JSONPath expression or the
            headerField  against within this variable.
    """

    __name__ = 'TestScript_Variable'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.defaultValue = None
        # type: str

        self.description = None
        # type: str

        self.expression = None
        # type: str

        self.headerField = None
        # type: str

        self.hint = None
        # type: str

        self.path = None
        # type: str

        self.sourceId = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Rule(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        resource: Reference to the resource (containing the contents of the
            rule needed for assertions).
        param: Each rule template can take one or more parameters for rule
            evaluation.
    """

    __name__ = 'TestScript_Rule'

    def __init__(self, dict_values=None):
        self.resource = None
        # reference to Reference: identifier

        self.param = None
        # type: list
        # reference to TestScript_Param

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        name: Descriptive name for this parameter that matches the external
            assert rule parameter name.
        value: The explicit or dynamic value for the parameter that will be
            passed on to the external rule template.
    """

    __name__ = 'TestScript_Param'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Ruleset(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        resource: Reference to the resource (containing the contents of the
            ruleset needed for assertions).
        rule: The referenced rule within the external ruleset template.
    """

    __name__ = 'TestScript_Ruleset'

    def __init__(self, dict_values=None):
        self.resource = None
        # reference to Reference: identifier

        self.rule = None
        # type: list
        # reference to TestScript_Rule1

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript_Ruleset',
             'child_variable': 'resource'},

            {'parent_entity': 'TestScript_Rule1',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Ruleset',
             'child_variable': 'rule'},
        ]


class TestScript_Rule1(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        ruleId: Id of the referenced rule within the external ruleset
            template.
        param: Each rule template can take one or more parameters for rule
            evaluation.
    """

    __name__ = 'TestScript_Rule1'

    def __init__(self, dict_values=None):
        self.ruleId = None
        # type: str

        self.param = None
        # type: list
        # reference to TestScript_Param1

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        name: Descriptive name for this parameter that matches the external
            assert ruleset rule parameter name.
        value: The value for the parameter that will be passed on to the
            external ruleset rule template.
    """

    __name__ = 'TestScript_Param1'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Setup(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        action: Action would contain either an operation or an assertion.
    """

    __name__ = 'TestScript_Setup'

    def __init__(self, dict_values=None):
        self.action = None
        # type: list
        # reference to TestScript_Action

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        operation: The operation to perform.
        assert: Evaluates the results of previous operations to determine if
            the server under test behaves appropriately.
    """

    __name__ = 'TestScript_Action'

    def __init__(self, dict_values=None):
        self.operation = None
        # reference to TestScript_Operation

        self._assert = None
        # reference to TestScript_Assert

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action',
             'child_variable': 'operation'},

            {'parent_entity': 'TestScript_Assert',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action',
             'child_variable': '_assert'},
        ]


class TestScript_Operation(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        type: Server interaction or operation type.
        resource: The type of the resource.  See
            http://build.fhir.org/resourcelist.html.
        label: The label would be used for tracking/logging purposes by test
            engines.
        description: The description would be used by test engines for
            tracking and reporting purposes.
        accept: The content-type or mime-type to use for RESTful operation in
            the 'Accept' header.
        contentType: The content-type or mime-type to use for RESTful
            operation in the 'Content-Type' header.
        destination: The server where the request message is destined for.
            Must be one of the server numbers listed in TestScript.destination
            section.
        encodeRequestUrl: Whether or not to implicitly send the request url in
            encoded format. The default is true to match the standard RESTful
            client behavior. Set to false when communicating with a server that
            does not support encoded url paths.
        origin: The server where the request message originates from.  Must be
            one of the server numbers listed in TestScript.origin section.
        params: Path plus parameters after [type].  Used to set parts of the
            request URL explicitly.
        requestHeader: Header elements would be used to set HTTP headers.
        requestId: The fixture id (maybe new) to map to the request.
        responseId: The fixture id (maybe new) to map to the response.
        sourceId: The id of the fixture used as the body of a PUT or POST
            request.
        targetId: Id of fixture used for extracting the [id],  [type], and
            [vid] for GET requests.
        url: Complete request URL.
    """

    __name__ = 'TestScript_Operation'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to Coding

        self.resource = None
        # type: str

        self.label = None
        # type: str

        self.description = None
        # type: str

        self.accept = None
        # type: str
        # possible values: xml, json, ttl, none

        self.contentType = None
        # type: str
        # possible values: xml, json, ttl, none

        self.destination = None
        # type: int

        self.encodeRequestUrl = None
        # type: bool

        self.origin = None
        # type: int

        self.params = None
        # type: str

        self.requestHeader = None
        # type: list
        # reference to TestScript_RequestHeader

        self.requestId = None
        # type: str

        self.responseId = None
        # type: str

        self.sourceId = None
        # type: str

        self.targetId = None
        # type: str

        self.url = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        field: The HTTP header field e.g. "Accept".
        value: The value of the header e.g. "application/fhir+xml".
    """

    __name__ = 'TestScript_RequestHeader'

    def __init__(self, dict_values=None):
        self.field = None
        # type: str

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Assert(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        label: The label would be used for tracking/logging purposes by test
            engines.
        description: The description would be used by test engines for
            tracking and reporting purposes.
        direction: The direction to use for the assertion.
        compareToSourceId: Id of the source fixture used as the contents to be
            evaluated by either the "source/expression" or "sourceId/path"
            definition.
        compareToSourceExpression: The fluentpath expression to evaluate
            against the source fixture. When compareToSourceId is defined, either
            compareToSourceExpression or compareToSourcePath must be defined, but
            not both.
        compareToSourcePath: XPath or JSONPath expression to evaluate against
            the source fixture. When compareToSourceId is defined, either
            compareToSourceExpression or compareToSourcePath must be defined, but
            not both.
        contentType: The content-type or mime-type to use for RESTful
            operation in the 'Content-Type' header.
        expression: The fluentpath expression to be evaluated against the
            request or response message contents - HTTP headers and payload.
        headerField: The HTTP header field name e.g. 'Location'.
        minimumId: The ID of a fixture.  Asserts that the response contains at
            a minimum the fixture specified by minimumId.
        navigationLinks: Whether or not the test execution performs validation
            on the bundle navigation links.
        operator: The operator type defines the conditional behavior of the
            assert. If not defined, the default is equals.
        path: The XPath or JSONPath expression to be evaluated against the
            fixture representing the response received from server.
        requestMethod: The request method or HTTP operation code to compare
            against that used by the client system under test.
        requestURL: The value to use in a comparison against the request URL
            path string.
        resource: The type of the resource.  See
            http://build.fhir.org/resourcelist.html.
        response: okay | created | noContent | notModified | bad | forbidden |
            notFound | methodNotAllowed | conflict | gone | preconditionFailed |
            unprocessable.
        responseCode: The value of the HTTP response code to be tested.
        rule: The TestScript.rule this assert will evaluate.
        ruleset: The TestScript.ruleset this assert will evaluate.
        sourceId: Fixture to evaluate the XPath/JSONPath expression or the
            headerField  against.
        validateProfileId: The ID of the Profile to validate against.
        value: The value to compare to.
        warningOnly: Whether or not the test execution will produce a warning
            only on error for this assert.
    """

    __name__ = 'TestScript_Assert'

    def __init__(self, dict_values=None):
        self.label = None
        # type: str

        self.description = None
        # type: str

        self.direction = None
        # type: str
        # possible values: response, request

        self.compareToSourceId = None
        # type: str

        self.compareToSourceExpression = None
        # type: str

        self.compareToSourcePath = None
        # type: str

        self.contentType = None
        # type: str
        # possible values: xml, json, ttl, none

        self.expression = None
        # type: str

        self.headerField = None
        # type: str

        self.minimumId = None
        # type: str

        self.navigationLinks = None
        # type: bool

        self.operator = None
        # type: str
        # possible values: equals, notEquals, in, notIn, greaterThan,
        # lessThan, empty, notEmpty, contains, notContains, eval

        self.path = None
        # type: str

        self.requestMethod = None
        # type: str
        # possible values: delete, get, options, patch, post, put

        self.requestURL = None
        # type: str

        self.resource = None
        # type: str

        self.response = None
        # type: str
        # possible values: okay, created, noContent, notModified, bad,
        # forbidden, notFound, methodNotAllowed, conflict, gone,
        # preconditionFailed, unprocessable

        self.responseCode = None
        # type: str

        self.rule = None
        # reference to TestScript_Rule2

        self.ruleset = None
        # reference to TestScript_Ruleset1

        self.sourceId = None
        # type: str

        self.validateProfileId = None
        # type: str

        self.value = None
        # type: str

        self.warningOnly = None
        # type: bool

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
                        value, 'equals, notEquals, in, notIn, greaterThan, lessThan, empty,'
                        ' notEmpty, contains, notContains, eval'))

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
                        value, 'equals, notEquals, in, notIn, greaterThan, lessThan, empty,'
                        ' notEmpty, contains, notContains, eval'))

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
            {'parent_entity': 'TestScript_Ruleset1',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Assert',
             'child_variable': 'ruleset'},

            {'parent_entity': 'TestScript_Rule2',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Assert',
             'child_variable': 'rule'},
        ]


class TestScript_Rule2(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        ruleId: The TestScript.rule id value this assert will evaluate.
        param: Each rule template can take one or more parameters for rule
            evaluation.
    """

    __name__ = 'TestScript_Rule2'

    def __init__(self, dict_values=None):
        self.ruleId = None
        # type: str

        self.param = None
        # type: list
        # reference to TestScript_Param2

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        name: Descriptive name for this parameter that matches the external
            assert rule parameter name.
        value: The value for the parameter that will be passed on to the
            external rule template.
    """

    __name__ = 'TestScript_Param2'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Ruleset1(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        rulesetId: The TestScript.ruleset id value this assert will evaluate.
        rule: The referenced rule within the external ruleset template.
    """

    __name__ = 'TestScript_Ruleset1'

    def __init__(self, dict_values=None):
        self.rulesetId = None
        # type: str

        self.rule = None
        # type: list
        # reference to TestScript_Rule3

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        ruleId: Id of the referenced rule within the external ruleset
            template.
        param: Each rule template can take one or more parameters for rule
            evaluation.
    """

    __name__ = 'TestScript_Rule3'

    def __init__(self, dict_values=None):
        self.ruleId = None
        # type: str

        self.param = None
        # type: list
        # reference to TestScript_Param3

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        name: Descriptive name for this parameter that matches the external
            assert ruleset rule parameter name.
        value: The value for the parameter that will be passed on to the
            external ruleset rule template.
    """

    __name__ = 'TestScript_Param3'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.value = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Test(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        name: The name of this test used for tracking/logging purposes by test
            engines.
        description: A short description of the test used by test engines for
            tracking and reporting purposes.
        action: Action would contain either an operation or an assertion.
    """

    __name__ = 'TestScript_Test'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.description = None
        # type: str

        self.action = None
        # type: list
        # reference to TestScript_Action1

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        operation: An operation would involve a REST request to a server.
        assert: Evaluates the results of previous operations to determine if
            the server under test behaves appropriately.
    """

    __name__ = 'TestScript_Action1'

    def __init__(self, dict_values=None):
        self.operation = None
        # reference to TestScript_Operation

        self._assert = None
        # reference to TestScript_Assert

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        action: The teardown action will only contain an operation.
    """

    __name__ = 'TestScript_Teardown'

    def __init__(self, dict_values=None):
        self.action = None
        # type: list
        # reference to TestScript_Action2

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.

    Args:
        operation: An operation would involve a REST request to a server.
    """

    __name__ = 'TestScript_Action2'

    def __init__(self, dict_values=None):
        self.operation = None
        # reference to TestScript_Operation

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'TestScript_Operation',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript_Action2',
             'child_variable': 'operation'},
        ]
