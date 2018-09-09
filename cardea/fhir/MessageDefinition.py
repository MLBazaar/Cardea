from .fhirbase import fhirbase


class MessageDefinition(fhirbase):
    """
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    __name__ = 'MessageDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'MessageDefinition'
        """
        This is a MessageDefinition resource

        type: string
        possible values: MessageDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this message definition when
        it is referenced in a specification, model, design or an instance.
        This SHALL be a URL, SHOULD be globally unique, and SHOULD be an
        address at which this message definition is (or will be) published.
        The URL SHOULD include the major version of the message definition.
        For more information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the message
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the message definition
        author and is not expected to be globally unique. For example, it
        might be a timestamp (e.g. yyyymmdd) if a managed version is not
        available. There is also no expectation that versions can be placed in
        a lexicographical sequence.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the message definition. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the message definition.

        type: string
        """

        self.status = None
        """
        The status of this message definition. Enables tracking the life-cycle
        of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this message definition is authored
        for testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the message definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the message definition
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the message
        definition.

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
        A free text natural language description of the message definition
        from a consumer's perspective.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate message definition instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the message definition is
        intended to be used.

        type: array
        reference to CodeableConcept
        """

        self.purpose = None
        """
        Explaination of why this message definition is needed and why it has
        been designed as it has.

        type: string
        """

        self.copyright = None
        """
        A copyright statement relating to the message definition and/or its
        contents. Copyright statements are generally legal restrictions on the
        use and publishing of the message definition.

        type: string
        """

        self.base = None
        """
        The MessageDefinition that is the basis for the contents of this
        resource.

        reference to Reference: identifier
        """

        self.parent = None
        """
        Identifies a protocol or workflow that this MessageDefinition
        represents a step in.

        type: array
        reference to Reference: identifier
        """

        self.replaces = None
        """
        A MessageDefinition that is superseded by this definition.

        type: array
        reference to Reference: identifier
        """

        self.event = None
        """
        A coded identifier of a supported messaging event.

        reference to Coding
        """

        self.category = None
        """
        The impact of the content of the message.

        type: string
        """

        self.focus = None
        """
        Identifies the resource (or resources) that are being addressed by the
        event.  For example, the Encounter for an admit message or two Account
        records for a merge.

        type: array
        reference to MessageDefinition_Focus
        """

        self.responseRequired = None
        """
        Indicates whether a response is required for this message.

        type: boolean
        """

        self.allowedResponse = None
        """
        Indicates what types of messages may be sent as an application-level
        response to this message.

        type: array
        reference to MessageDefinition_AllowedResponse
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this message definition
        when it is represented in other formats, or referenced in a
        specification, model, design or an instance.

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
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'MessageDefinition_Focus',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'focus'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition',
             'child_variable': 'base'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'event'},

            {'parent_entity': 'MessageDefinition_AllowedResponse',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'allowedResponse'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition',
             'child_variable': 'replaces'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition',
             'child_variable': 'parent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'jurisdiction'},
        ]


class MessageDefinition_Focus(fhirbase):
    """
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    __name__ = 'MessageDefinition_Focus'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The kind of resource that must be the focus for this message.

        type: string
        """

        self.profile = None
        """
        A profile that reflects constraints for the focal resource (and
        potentially for related resources).

        reference to Reference: identifier
        """

        self.min = None
        """
        Identifies the minimum number of resources of this type that must be
        pointed to by a message in order for it to be valid against this
        MessageDefinition.

        type: int
        """

        self.max = None
        """
        Identifies the maximum number of resources of this type that must be
        pointed to by a message in order for it to be valid against this
        MessageDefinition.

        type: string
        """

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
    """

    __name__ = 'MessageDefinition_AllowedResponse'

    def __init__(self, dict_values=None):
        self.message = None
        """
        A reference to the message definition that must be adhered to by this
        supported response.

        reference to Reference: identifier
        """

        self.situation = None
        """
        Provides a description of the circumstances in which this response
        should be used (as opposed to one of the alternative responses).

        type: string
        """

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
