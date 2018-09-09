from .fhirbase import fhirbase


class MessageDefinition(fhirbase):
    """Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    def __init__(self, dict_values=None):
        # this is a messagedefinition resource
        self.resourceType = 'MessageDefinition'
        # type = string
        # possible values: MessageDefinition

        # an absolute uri that is used to identify this message definition when it
        # is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this message definition is (or will be) published. the url should
        # include the major version of the message definition. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the message
        # definition when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the message definition
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the message definition. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the message definition.
        self.title = None
        # type = string

        # the status of this message definition. enables tracking the life-cycle
        # of the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this message definition is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the message definition was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the message definition changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the message
        # definition.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the message definition from
        # a consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate message definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the message definition is intended
        # to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this message definition is needed and why it has
        # been designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the message definition and/or its
        # contents. copyright statements are generally legal restrictions on the
        # use and publishing of the message definition.
        self.copyright = None
        # type = string

        # the messagedefinition that is the basis for the contents of this
        # resource.
        self.base = None
        # reference to Reference: identifier

        # identifies a protocol or workflow that this messagedefinition represents
        # a step in.
        self.parent = None
        # type = array
        # reference to Reference: identifier

        # a messagedefinition that is superseded by this definition.
        self.replaces = None
        # type = array
        # reference to Reference: identifier

        # a coded identifier of a supported messaging event.
        self.event = None
        # reference to Coding: Coding

        # the impact of the content of the message.
        self.category = None
        # type = string

        # identifies the resource (or resources) that are being addressed by the
        # event.  for example, the encounter for an admit message or two account
        # records for a merge.
        self.focus = None
        # type = array
        # reference to MessageDefinition_Focus: MessageDefinition_Focus

        # indicates whether a response is required for this message.
        self.responseRequired = None
        # type = boolean

        # indicates what types of messages may be sent as an application-level
        # response to this message.
        self.allowedResponse = None
        # type = array
        # reference to MessageDefinition_AllowedResponse: MessageDefinition_AllowedResponse

        # a formal identifier that is used to identify this message definition
        # when it is represented in other formats, or referenced in a
        # specification, model, design or an instance.
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
            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'MessageDefinition_AllowedResponse',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'allowedResponse'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'event'},

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

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'MessageDefinition_Focus',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'focus'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MessageDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition',
             'child_variable': 'base'},
        ]


class MessageDefinition_Focus(fhirbase):
    """Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    def __init__(self, dict_values=None):
        # the kind of resource that must be the focus for this message.
        self.code = None
        # type = string

        # a profile that reflects constraints for the focal resource (and
        # potentially for related resources).
        self.profile = None
        # reference to Reference: identifier

        # identifies the minimum number of resources of this type that must be
        # pointed to by a message in order for it to be valid against this
        # messagedefinition.
        self.min = None
        # type = int

        # identifies the maximum number of resources of this type that must be
        # pointed to by a message in order for it to be valid against this
        # messagedefinition.
        self.max = None
        # type = string

        # unique identifier for object class
        self.object_id = None

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
    """Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    def __init__(self, dict_values=None):
        # a reference to the message definition that must be adhered to by this
        # supported response.
        self.message = None
        # reference to Reference: identifier

        # provides a description of the circumstances in which this response
        # should be used (as opposed to one of the alternative responses).
        self.situation = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MessageDefinition_AllowedResponse',
             'child_variable': 'message'},
        ]
