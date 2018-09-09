from .fhirbase import fhirbase


class CompartmentDefinition(fhirbase):
    """
    A compartment definition that defines how resources are accessed on a
    server.
    """

    __name__ = 'CompartmentDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'CompartmentDefinition'
        """
        This is a CompartmentDefinition resource

        type: string
        possible values: CompartmentDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this compartment definition
        when it is referenced in a specification, model, design or an
        instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
        be an address at which this compartment definition is (or will be)
        published. The URL SHOULD include the major version of the compartment
        definition. For more information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.name = None
        """
        A natural language name identifying the compartment definition. This
        name should be usable as an identifier for the module by machine
        processing applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the compartment
        definition.

        type: string
        """

        self.status = None
        """
        The status of this compartment definition. Enables tracking the
        life-cycle of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this compartment definition is
        authored for testing purposes (or education/evaluation/marketing), and
        is not intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the compartment definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the compartment
        definition changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the
        compartment definition.

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
        A free text natural language description of the compartment definition
        from a consumer's perspective.

        type: string
        """

        self.purpose = None
        """
        Explaination of why this compartment definition is needed and why it
        has been designed as it has.

        type: string
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate compartment definition
        instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the compartment definition is
        intended to be used.

        type: array
        reference to CodeableConcept
        """

        self.code = None
        """
        Which compartment this definition describes.

        type: string
        possible values: Patient, Encounter, RelatedPerson,
        Practitioner, Device
        """

        self.search = None
        """
        Whether the search syntax is supported,.

        type: boolean
        """

        self.resource = None
        """
        Information about how a resource is related to the compartment.

        type: array
        reference to CompartmentDefinition_Resource
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'CompartmentDefinition_Resource',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'resource'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CompartmentDefinition',
             'child_variable': 'jurisdiction'},
        ]


class CompartmentDefinition_Resource(fhirbase):
    """
    A compartment definition that defines how resources are accessed on a
    server.
    """

    __name__ = 'CompartmentDefinition_Resource'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The name of a resource supported by the server.

        type: string
        """

        self.param = None
        """
        The name of a search parameter that represents the link to the
        compartment. More than one may be listed because a resource may be
        linked to a compartment in more than one way,.

        type: array
        """

        self.documentation = None
        """
        Additional documentation about the resource and compartment.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
