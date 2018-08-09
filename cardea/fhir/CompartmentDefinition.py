from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .ContactDetail import ContactDetail
from .UsageContext import UsageContext

class CompartmentDefinition(fhirbase):
    """A compartment definition that defines how resources are accessed on a
    server.
    """

    def __init__(self, dict_values=None):
        # this is a compartmentdefinition resource
        self.resourceType = 'CompartmentDefinition'
        # type = string
        # possible values = CompartmentDefinition

        # an absolute uri that is used to identify this compartment definition
        # when it is referenced in a specification, model, design or an instance.
        # this shall be a url, should be globally unique, and should be an address
        # at which this compartment definition is (or will be) published. the url
        # should include the major version of the compartment definition. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # a natural language name identifying the compartment definition. this
        # name should be usable as an identifier for the module by machine
        # processing applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the compartment
        # definition.
        self.title = None
        # type = string

        # the status of this compartment definition. enables tracking the life-
        # cycle of the content.
        self.status = None
        # type = string
        # possible values = draft, active, retired, unknown

        # a boolean value to indicate that this compartment definition is authored
        # for testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the compartment definition was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the compartment definition
        # changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the
        # compartment definition.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the compartment definition
        # from a consumer's perspective.
        self.description = None
        # type = string

        # explaination of why this compartment definition is needed and why it has
        # been designed as it has.
        self.purpose = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate compartment definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the compartment definition is
        # intended to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # which compartment this definition describes.
        self.code = None
        # type = string
        # possible values = Patient, Encounter, RelatedPerson, Practitioner, Device

        # whether the search syntax is supported,.
        self.search = None
        # type = boolean

        # information about how a resource is related to the compartment.
        self.resource = None
        # type = array
        # reference to CompartmentDefinition_Resource: CompartmentDefinition_Resource


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, active, retired, unknown'))

        if self.code is not None:
            for value in self.code:
                if value != None and value.lower() not in ['patient', 'encounter', 'relatedperson', 'practitioner', 'device']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'patient, encounter, relatedperson, practitioner, device'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'CompartmentDefinition',
            'child_variable': 'jurisdiction'},

            {'parent_entity': 'CompartmentDefinition_Resource',
            'parent_variable': 'object_id',
            'child_entity': 'CompartmentDefinition',
            'child_variable': 'resource'},

            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'CompartmentDefinition',
            'child_variable': 'useContext'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'CompartmentDefinition',
            'child_variable': 'contact'},
        ]

class CompartmentDefinition_Resource(fhirbase):
    """A compartment definition that defines how resources are accessed on a
    server.
    """

    def __init__(self, dict_values=None):
        # the name of a resource supported by the server.
        self.code = None
        # type = string

        # the name of a search parameter that represents the link to the
        # compartment. more than one may be listed because a resource may be
        # linked to a compartment in more than one way,.
        self.param = None
        # type = array

        # additional documentation about the resource and compartment.
        self.documentation = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


