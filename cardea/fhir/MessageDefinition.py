from .fhirbase import fhirbase


class MessageDefinition(fhirbase):
    """
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.

    Args:
        resourceType: This is a MessageDefinition resource
        url: An absolute URI that is used to identify this message definition
            when it is referenced in a specification, model, design or an
            instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
            be an address at which this message definition is (or will be)
            published. The URL SHOULD include the major version of the message
            definition. For more information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this message
            definition when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            message definition when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the message
            definition author and is not expected to be globally unique. For
            example, it might be a timestamp (e.g. yyyymmdd) if a managed version
            is not available. There is also no expectation that versions can be
            placed in a lexicographical sequence.
        name: A natural language name identifying the message definition. This
            name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        title: A short, descriptive, user-friendly title for the message
            definition.
        status: The status of this message definition. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this message definition
            is authored for testing purposes (or education/evaluation/marketing),
            and is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the message definition was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the message definition
            changes.
        publisher: The name of the individual or organization that published
            the message definition.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the message
            definition from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate message definition
            instances.
        jurisdiction: A legal or geographic region in which the message
            definition is intended to be used.
        purpose: Explaination of why this message definition is needed and why
            it has been designed as it has.
        copyright: A copyright statement relating to the message definition
            and/or its contents. Copyright statements are generally legal
            restrictions on the use and publishing of the message definition.
        base: The MessageDefinition that is the basis for the contents of this
            resource.
        parent: Identifies a protocol or workflow that this MessageDefinition
            represents a step in.
        replaces: A MessageDefinition that is superseded by this definition.
        event: A coded identifier of a supported messaging event.
        category: The impact of the content of the message.
        focus: Identifies the resource (or resources) that are being addressed
            by the event.  For example, the Encounter for an admit message or two
            Account records for a merge.
        responseRequired: Indicates whether a response is required for this
            message.
        allowedResponse: Indicates what types of messages may be sent as an
            application-level response to this message.
    """

    __name__ = 'MessageDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'MessageDefinition'
        # type: str
        # possible values: MessageDefinition

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

        self.base = None
        # reference to Reference: identifier

        self.parent = None
        # type: list
        # reference to Reference: identifier

        self.replaces = None
        # type: list
        # reference to Reference: identifier

        self.event = None
        # reference to Coding

        self.category = None
        # type: str

        self.focus = None
        # type: list
        # reference to MessageDefinition_Focus

        self.responseRequired = None
        # type: bool

        self.allowedResponse = None
        # type: list
        # reference to MessageDefinition_AllowedResponse

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
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'event'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition',
             'child_variable': 'base'},

            {'parent_entity': 'MessageDefinition_AllowedResponse',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'allowedResponse'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition',
             'child_variable': 'replaces'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition',
             'child_variable': 'parent'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'MessageDefinition_Focus',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'focus'},
        ]


class MessageDefinition_Focus(fhirbase):
    """
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.

    Args:
        code: The kind of resource that must be the focus for this message.
        profile: A profile that reflects constraints for the focal resource
            (and potentially for related resources).
        min: Identifies the minimum number of resources of this type that must
            be pointed to by a message in order for it to be valid against this
            MessageDefinition.
        max: Identifies the maximum number of resources of this type that must
            be pointed to by a message in order for it to be valid against this
            MessageDefinition.
    """

    __name__ = 'MessageDefinition_Focus'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.profile = None
        # reference to Reference: identifier

        self.min = None
        # type: int

        self.max = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition_Focus',
             'child_variable': 'profile'},
        ]


class MessageDefinition_AllowedResponse(fhirbase):
    """
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.

    Args:
        message: A reference to the message definition that must be adhered to
            by this supported response.
        situation: Provides a description of the circumstances in which this
            response should be used (as opposed to one of the alternative
            responses).
    """

    __name__ = 'MessageDefinition_AllowedResponse'

    def __init__(self, dict_values=None):
        self.message = None
        # reference to Reference: identifier

        self.situation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition_AllowedResponse',
             'child_variable': 'message'},
        ]
