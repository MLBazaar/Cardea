from .fhirbase import fhirbase


class TestScript(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript'

    def __init__(self, dict_values=None):
        self.resourceType = 'TestScript'
        """
        This is a TestScript resource

        type: string
        possible values: TestScript
        """

        self.url = None
        """
        An absolute URI that is used to identify this test script when it is
        referenced in a specification, model, design or an instance. This
        SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
        which this test script is (or will be) published. The URL SHOULD
        include the major version of the test script. For more information see
        [Technical and Business Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the test
        script when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the test script author
        and is not expected to be globally unique. For example, it might be a
        timestamp (e.g. yyyymmdd) if a managed version is not available. There
        is also no expectation that versions can be placed in a
        lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the test script. This name should
        be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the test script.

        type: string
        """

        self.status = None
        """
        The status of this test script. Enables tracking the life-cycle of the
        content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this test script is authored for
        testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the test script was published.
        The date must change if and when the business version changes and it
        must change if the status code changes. In addition, it should change
        when the substantive content of the test script changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the test
        script.

        type: string
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        publisher.

        type: array
        reference to ContactDetail
        """

        self.description = None
        """
        A free text natural language description of the test script from a
        consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate test script instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the test script is intended to
        be used.

        type: array
        reference to CodeableConcept
        """

        self.purpose = None
        """
        Explaination of why this test script is needed and why it has been
        designed as it has.

        type: string
        """

        self.copyright = None
        """
        A copyright statement relating to the test script and/or its contents.
        Copyright statements are generally legal restrictions on the use and
        publishing of the test script.

        type: string
        """

        self.origin = None
        """
        An abstract server used in operations within this test script in the
        origin element.

        type: array
        reference to TestScript_Origin
        """

        self.destination = None
        """
        An abstract server used in operations within this test script in the
        destination element.

        type: array
        reference to TestScript_Destination
        """

        self.metadata = None
        """
        The required capability must exist and are assumed to function
        correctly on the FHIR server being tested.

        reference to TestScript_Metadata
        """

        self.fixture = None
        """
        Fixture in the test script - by reference (uri). All fixtures are
        required for the test script to execute.

        type: array
        reference to TestScript_Fixture
        """

        self.profile = None
        """
        Reference to the profile to be used for validation.

        type: array
        reference to Reference: identifier
        """

        self.variable = None
        """
        Variable is set based either on element value in response body or on
        header field value in the response headers.

        type: array
        reference to TestScript_Variable
        """

        self.rule = None
        """
        Assert rule to be used in one or more asserts within the test script.

        type: array
        reference to TestScript_Rule
        """

        self.ruleset = None
        """
        Contains one or more rules.  Offers a way to group rules so assertions
        could reference the group of rules and have them all applied.

        type: array
        reference to TestScript_Ruleset
        """

        self.setup = None
        """
        A series of required setup operations before tests are executed.

        reference to TestScript_Setup
        """

        self.test = None
        """
        A test in this script.

        type: array
        reference to TestScript_Test
        """

        self.teardown = None
        """
        A series of operations required to clean up after the all the tests
        are executed (successfully or otherwise).

        reference to TestScript_Teardown
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this test script when it
        is represented in other formats, or referenced in a specification,
        model, design or an instance.

        reference to Identifier
        """

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

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'identifier'},

            {'parent_entity': 'TestScript_Fixture',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'fixture'},

            {'parent_entity': 'TestScript_Metadata',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'metadata'},

            {'parent_entity': 'TestScript_Setup',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'setup'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'TestScript_Test',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'test'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'TestScript',
             'child_variable': 'profile'},

            {'parent_entity': 'TestScript_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'rule'},

            {'parent_entity': 'TestScript_Teardown',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'teardown'},

            {'parent_entity': 'TestScript_Destination',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'destination'},

            {'parent_entity': 'TestScript_Origin',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'origin'},

            {'parent_entity': 'TestScript_Variable',
             'parent_variable': 'object_id',
             'child_entity': 'TestScript',
             'child_variable': 'variable'},
        ]


class TestScript_Origin(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Origin'

    def __init__(self, dict_values=None):
        self.index = None
        """
        Abstract name given to an origin server in this test script.  The name
        is provided as a number starting at 1.

        type: int
        """

        self.profile = None
        """
        The type of origin profile the test system supports.

        reference to Coding
        """

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
    """

    __name__ = 'TestScript_Destination'

    def __init__(self, dict_values=None):
        self.index = None
        """
        Abstract name given to a destination server in this test script.  The
        name is provided as a number starting at 1.

        type: int
        """

        self.profile = None
        """
        The type of destination profile the test system supports.

        reference to Coding
        """

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
    """

    __name__ = 'TestScript_Metadata'

    def __init__(self, dict_values=None):
        self.link = None
        """
        A link to the FHIR specification that this test is covering.

        type: array
        reference to TestScript_Link
        """

        self.capability = None
        """
        Capabilities that must exist and are assumed to function correctly on
        the FHIR server being tested.

        type: array
        reference to TestScript_Capability
        """

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
    """

    __name__ = 'TestScript_Link'

    def __init__(self, dict_values=None):
        self.url = None
        """
        URL to a particular requirement or feature within the FHIR
        specification.

        type: string
        """

        self.description = None
        """
        Short description of the link.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Capability(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Capability'

    def __init__(self, dict_values=None):
        self.required = None
        """
        Whether or not the test execution will require the given capabilities
        of the server in order for this test script to execute.

        type: boolean
        """

        self.validated = None
        """
        Whether or not the test execution will validate the given capabilities
        of the server in order for this test script to execute.

        type: boolean
        """

        self.description = None
        """
        Description of the capabilities that this test script is requiring the
        server to support.

        type: string
        """

        self.origin = None
        """
        Which origin server these requirements apply to.

        type: array
        """

        self.destination = None
        """
        Which server these requirements apply to.

        type: int
        """

        self.link = None
        """
        Links to the FHIR specification that describes this interaction and
        the resources involved in more detail.

        type: array
        """

        self.capabilities = None
        """
        Minimum capabilities required of server for test script to execute
        successfully.   If server does not meet at a minimum the referenced
        capability statement, then all tests in this script are skipped.

        reference to Reference: identifier
        """

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
    """

    __name__ = 'TestScript_Fixture'

    def __init__(self, dict_values=None):
        self.autocreate = None
        """
        Whether or not to implicitly create the fixture during setup. If true,
        the fixture is automatically created on each server being tested
        during setup, therefore no create operation is required for this
        fixture in the TestScript.setup section.

        type: boolean
        """

        self.autodelete = None
        """
        Whether or not to implicitly delete the fixture during teardown. If
        true, the fixture is automatically deleted on each server being tested
        during teardown, therefore no delete operation is required for this
        fixture in the TestScript.teardown section.

        type: boolean
        """

        self.resource = None
        """
        Reference to the resource (containing the contents of the resource
        needed for operations).

        reference to Reference: identifier
        """

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
    """

    __name__ = 'TestScript_Variable'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Descriptive name for this variable.

        type: string
        """

        self.defaultValue = None
        """
        A default, hard-coded, or user-defined value for this variable.

        type: string
        """

        self.description = None
        """
        A free text natural language description of the variable and its
        purpose.

        type: string
        """

        self.expression = None
        """
        The fluentpath expression to evaluate against the fixture body. When
        variables are defined, only one of either expression, headerField or
        path must be specified.

        type: string
        """

        self.headerField = None
        """
        Will be used to grab the HTTP header field value from the headers that
        sourceId is pointing to.

        type: string
        """

        self.hint = None
        """
        Displayable text string with hint help information to the user when
        entering a default value.

        type: string
        """

        self.path = None
        """
        XPath or JSONPath to evaluate against the fixture body.  When
        variables are defined, only one of either expression, headerField or
        path must be specified.

        type: string
        """

        self.sourceId = None
        """
        Fixture to evaluate the XPath/JSONPath expression or the headerField
        against within this variable.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Rule(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Rule'

    def __init__(self, dict_values=None):
        self.resource = None
        """
        Reference to the resource (containing the contents of the rule needed
        for assertions).

        reference to Reference: identifier
        """

        self.param = None
        """
        Each rule template can take one or more parameters for rule
        evaluation.

        type: array
        reference to TestScript_Param
        """

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
    """

    __name__ = 'TestScript_Param'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Descriptive name for this parameter that matches the external assert
        rule parameter name.

        type: string
        """

        self.value = None
        """
        The explicit or dynamic value for the parameter that will be passed on
        to the external rule template.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Ruleset(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Ruleset'

    def __init__(self, dict_values=None):
        self.resource = None
        """
        Reference to the resource (containing the contents of the ruleset
        needed for assertions).

        reference to Reference: identifier
        """

        self.rule = None
        """
        The referenced rule within the external ruleset template.

        type: array
        reference to TestScript_Rule1
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Rule1'

    def __init__(self, dict_values=None):
        self.ruleId = None
        """
        Id of the referenced rule within the external ruleset template.

        type: string
        """

        self.param = None
        """
        Each rule template can take one or more parameters for rule
        evaluation.

        type: array
        reference to TestScript_Param1
        """

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
    """

    __name__ = 'TestScript_Param1'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Descriptive name for this parameter that matches the external assert
        ruleset rule parameter name.

        type: string
        """

        self.value = None
        """
        The value for the parameter that will be passed on to the external
        ruleset rule template.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Setup(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Setup'

    def __init__(self, dict_values=None):
        self.action = None
        """
        Action would contain either an operation or an assertion.

        type: array
        reference to TestScript_Action
        """

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
    """

    __name__ = 'TestScript_Action'

    def __init__(self, dict_values=None):
        self.operation = None
        """
        The operation to perform.

        reference to TestScript_Operation
        """

        self._assert = None
        """
        Evaluates the results of previous operations to determine if the
        server under test behaves appropriately.

        reference to TestScript_Assert
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Operation'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Server interaction or operation type.

        reference to Coding
        """

        self.resource = None
        """
        The type of the resource.  See
        http://build.fhir.org/resourcelist.html.

        type: string
        """

        self.label = None
        """
        The label would be used for tracking/logging purposes by test engines.

        type: string
        """

        self.description = None
        """
        The description would be used by test engines for tracking and
        reporting purposes.

        type: string
        """

        self.accept = None
        """
        The content-type or mime-type to use for RESTful operation in the
        'Accept' header.

        type: string
        possible values: xml, json, ttl, none
        """

        self.contentType = None
        """
        The content-type or mime-type to use for RESTful operation in the
        'Content-Type' header.

        type: string
        possible values: xml, json, ttl, none
        """

        self.destination = None
        """
        The server where the request message is destined for.  Must be one of
        the server numbers listed in TestScript.destination section.

        type: int
        """

        self.encodeRequestUrl = None
        """
        Whether or not to implicitly send the request url in encoded format.
        The default is true to match the standard RESTful client behavior. Set
        to false when communicating with a server that does not support
        encoded url paths.

        type: boolean
        """

        self.origin = None
        """
        The server where the request message originates from.  Must be one of
        the server numbers listed in TestScript.origin section.

        type: int
        """

        self.params = None
        """
        Path plus parameters after [type].  Used to set parts of the request
        URL explicitly.

        type: string
        """

        self.requestHeader = None
        """
        Header elements would be used to set HTTP headers.

        type: array
        reference to TestScript_RequestHeader
        """

        self.requestId = None
        """
        The fixture id (maybe new) to map to the request.

        type: string
        """

        self.responseId = None
        """
        The fixture id (maybe new) to map to the response.

        type: string
        """

        self.sourceId = None
        """
        The id of the fixture used as the body of a PUT or POST request.

        type: string
        """

        self.targetId = None
        """
        Id of fixture used for extracting the [id],  [type], and [vid] for GET
        requests.

        type: string
        """

        self.url = None
        """
        Complete request URL.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_RequestHeader'

    def __init__(self, dict_values=None):
        self.field = None
        """
        The HTTP header field e.g. "Accept".

        type: string
        """

        self.value = None
        """
        The value of the header e.g. "application/fhir+xml".

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Assert(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Assert'

    def __init__(self, dict_values=None):
        self.label = None
        """
        The label would be used for tracking/logging purposes by test engines.

        type: string
        """

        self.description = None
        """
        The description would be used by test engines for tracking and
        reporting purposes.

        type: string
        """

        self.direction = None
        """
        The direction to use for the assertion.

        type: string
        possible values: response, request
        """

        self.compareToSourceId = None
        """
        Id of the source fixture used as the contents to be evaluated by
        either the "source/expression" or "sourceId/path" definition.

        type: string
        """

        self.compareToSourceExpression = None
        """
        The fluentpath expression to evaluate against the source fixture. When
        compareToSourceId is defined, either compareToSourceExpression or
        compareToSourcePath must be defined, but not both.

        type: string
        """

        self.compareToSourcePath = None
        """
        XPath or JSONPath expression to evaluate against the source fixture.
        When compareToSourceId is defined, either compareToSourceExpression or
        compareToSourcePath must be defined, but not both.

        type: string
        """

        self.contentType = None
        """
        The content-type or mime-type to use for RESTful operation in the
        'Content-Type' header.

        type: string
        possible values: xml, json, ttl, none
        """

        self.expression = None
        """
        The fluentpath expression to be evaluated against the request or
        response message contents - HTTP headers and payload.

        type: string
        """

        self.headerField = None
        """
        The HTTP header field name e.g. 'Location'.

        type: string
        """

        self.minimumId = None
        """
        The ID of a fixture.  Asserts that the response contains at a minimum
        the fixture specified by minimumId.

        type: string
        """

        self.navigationLinks = None
        """
        Whether or not the test execution performs validation on the bundle
        navigation links.

        type: boolean
        """

        self.operator = None
        """
        The operator type defines the conditional behavior of the assert. If
        not defined, the default is equals.

        type: string
        possible values: equals, notEquals, in, notIn, greaterThan,
        lessThan, empty, notEmpty, contains, notContains, eval
        """

        self.path = None
        """
        The XPath or JSONPath expression to be evaluated against the fixture
        representing the response received from server.

        type: string
        """

        self.requestMethod = None
        """
        The request method or HTTP operation code to compare against that used
        by the client system under test.

        type: string
        possible values: delete, get, options, patch, post, put
        """

        self.requestURL = None
        """
        The value to use in a comparison against the request URL path string.

        type: string
        """

        self.resource = None
        """
        The type of the resource.  See
        http://build.fhir.org/resourcelist.html.

        type: string
        """

        self.response = None
        """
        okay | created | noContent | notModified | bad | forbidden | notFound
        | methodNotAllowed | conflict | gone | preconditionFailed |
        unprocessable.

        type: string
        possible values: okay, created, noContent, notModified, bad,
        forbidden, notFound, methodNotAllowed, conflict, gone,
        preconditionFailed, unprocessable
        """

        self.responseCode = None
        """
        The value of the HTTP response code to be tested.

        type: string
        """

        self.rule = None
        """
        The TestScript.rule this assert will evaluate.

        reference to TestScript_Rule2
        """

        self.ruleset = None
        """
        The TestScript.ruleset this assert will evaluate.

        reference to TestScript_Ruleset1
        """

        self.sourceId = None
        """
        Fixture to evaluate the XPath/JSONPath expression or the headerField
        against.

        type: string
        """

        self.validateProfileId = None
        """
        The ID of the Profile to validate against.

        type: string
        """

        self.value = None
        """
        The value to compare to.

        type: string
        """

        self.warningOnly = None
        """
        Whether or not the test execution will produce a warning only on error
        for this assert.

        type: boolean
        """

        self.object_id = None
        # unique identifier for object class

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
                        value, 'equals, notEquals, in, notIn, greaterThan, lessThan, empty, '
                        'notEmpty, contains, notContains, eval'))

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
                        value, 'equals, notEquals, in, notIn, greaterThan, lessThan, empty, '
                        'notEmpty, contains, notContains, eval'))

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
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Rule2'

    def __init__(self, dict_values=None):
        self.ruleId = None
        """
        The TestScript.rule id value this assert will evaluate.

        type: string
        """

        self.param = None
        """
        Each rule template can take one or more parameters for rule
        evaluation.

        type: array
        reference to TestScript_Param2
        """

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
    """

    __name__ = 'TestScript_Param2'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Descriptive name for this parameter that matches the external assert
        rule parameter name.

        type: string
        """

        self.value = None
        """
        The value for the parameter that will be passed on to the external
        rule template.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Ruleset1(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Ruleset1'

    def __init__(self, dict_values=None):
        self.rulesetId = None
        """
        The TestScript.ruleset id value this assert will evaluate.

        type: string
        """

        self.rule = None
        """
        The referenced rule within the external ruleset template.

        type: array
        reference to TestScript_Rule3
        """

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
    """

    __name__ = 'TestScript_Rule3'

    def __init__(self, dict_values=None):
        self.ruleId = None
        """
        Id of the referenced rule within the external ruleset template.

        type: string
        """

        self.param = None
        """
        Each rule template can take one or more parameters for rule
        evaluation.

        type: array
        reference to TestScript_Param3
        """

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
    """

    __name__ = 'TestScript_Param3'

    def __init__(self, dict_values=None):
        self.name = None
        """
        Descriptive name for this parameter that matches the external assert
        ruleset rule parameter name.

        type: string
        """

        self.value = None
        """
        The value for the parameter that will be passed on to the external
        ruleset rule template.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class TestScript_Test(fhirbase):
    """
    A structured set of tests against a FHIR server implementation to
    determine compliance against the FHIR specification.
    """

    __name__ = 'TestScript_Test'

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
        reference to TestScript_Action1
        """

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
    """

    __name__ = 'TestScript_Action1'

    def __init__(self, dict_values=None):
        self.operation = None
        """
        An operation would involve a REST request to a server.

        reference to TestScript_Operation
        """

        self._assert = None
        """
        Evaluates the results of previous operations to determine if the
        server under test behaves appropriately.

        reference to TestScript_Assert
        """

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
    """

    __name__ = 'TestScript_Teardown'

    def __init__(self, dict_values=None):
        self.action = None
        """
        The teardown action will only contain an operation.

        type: array
        reference to TestScript_Action2
        """

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
    """

    __name__ = 'TestScript_Action2'

    def __init__(self, dict_values=None):
        self.operation = None
        """
        An operation would involve a REST request to a server.

        reference to TestScript_Operation
        """

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
