from .fhirbase import fhirbase


class CompartmentDefinition(fhirbase):
    """
    A compartment definition that defines how resources are accessed on a
    server.

    Args:
        resourceType: This is a CompartmentDefinition resource
        url: An absolute URI that is used to identify this compartment
            definition when it is referenced in a specification, model, design or
            an instance. This SHALL be a URL, SHOULD be globally unique, and
            SHOULD be an address at which this compartment definition is (or will
            be) published. The URL SHOULD include the major version of the
            compartment definition. For more information see [Technical and
            Business Versions](resource.html#versions).
        name: A natural language name identifying the compartment definition.
            This name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        title: A short, descriptive, user-friendly title for the compartment
            definition.
        status: The status of this compartment definition. Enables tracking
            the life-cycle of the content.
        experimental: A boolean value to indicate that this compartment
            definition is authored for testing purposes (or
            education/evaluation/marketing), and is not intended to be used for
            genuine usage.
        date: The date  (and optionally time) when the compartment definition
            was published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the compartment
            definition changes.
        publisher: The name of the individual or organization that published
            the compartment definition.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the
            compartment definition from a consumer's perspective.
        purpose: Explaination of why this compartment definition is needed and
            why it has been designed as it has.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate compartment
            definition instances.
        jurisdiction: A legal or geographic region in which the compartment
            definition is intended to be used.
        code: Which compartment this definition describes.
        search: Whether the search syntax is supported,.
        resource: Information about how a resource is related to the
            compartment.
    """

    __name__ = 'CompartmentDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'CompartmentDefinition'
        # type: str
        # possible values: CompartmentDefinition

        self.url = None
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

        self.purpose = None
        # type: str

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.code = None
        # type: str
        # possible values: Patient, Encounter, RelatedPerson,
        # Practitioner, Device

        self.search = None
        # type: bool

        self.resource = None
        # type: list
        # reference to CompartmentDefinition_Resource

        self.object_id = None
        # unique identifier for object class

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

        if self.code is not None:
            for value in self.code:
                if value is not None and value.lower() not in [
                        'patient', 'encounter', 'relatedperson', 'practitioner', 'device']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'Patient, Encounter, RelatedPerson, Practitioner, Device'))

    def get_relationships(self):

        return [
            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CompartmentDefinition_Resource',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'resource'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'contact'},
        ]


class CompartmentDefinition_Resource(fhirbase):
    """
    A compartment definition that defines how resources are accessed on a
    server.

    Args:
        code: The name of a resource supported by the server.
        param: The name of a search parameter that represents the link to the
            compartment. More than one may be listed because a resource may be
            linked to a compartment in more than one way,.
        documentation: Additional documentation about the resource and
            compartment.
    """

    __name__ = 'CompartmentDefinition_Resource'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.param = None
        # type: list

        self.documentation = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
