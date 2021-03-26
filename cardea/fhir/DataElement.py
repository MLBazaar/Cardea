from .fhirbase import fhirbase


class DataElement(fhirbase):
    """
    The formal description of a single piece of information that can be
    gathered and reported.

    Args:
        resourceType: This is a DataElement resource
        url: An absolute URI that is used to identify this data element when
            it is referenced in a specification, model, design or an instance.
            This SHALL be a URL, SHOULD be globally unique, and SHOULD be an
            address at which this data element is (or will be) published. The URL
            SHOULD include the major version of the data element. For more
            information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this data
            element when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            data element when it is referenced in a specification, model, design
            or instance. This is an arbitrary value managed by the data element
            author and is not expected to be globally unique. For example, it
            might be a timestamp (e.g. yyyymmdd) if a managed version is not
            available. There is also no expectation that versions can be placed in
            a lexicographical sequence.
        status: The status of this data element. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this data element is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the data element was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the data element
            changes.
        publisher: The name of the individual or organization that published
            the data element.
        name: A natural language name identifying the data element. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the data element.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate data element
            instances.
        jurisdiction: A legal or geographic region in which the data element
            is intended to be used.
        copyright: A copyright statement relating to the data element and/or
            its contents. Copyright statements are generally legal restrictions on
            the use and publishing of the data element.
        stringency: Identifies how precise the data element is in its
            definition.
        mapping: Identifies a specification (other than a terminology) that
            the elements which make up the DataElement have some correspondence
            with.
        element: Defines the structure, type, allowed values and other
            constraining characteristics of the data element.
    """

    __name__ = 'DataElement'

    def __init__(self, dict_values=None):
        self.resourceType = 'DataElement'
        # type: str
        # possible values: DataElement

        self.url = None
        # type: str

        self.version = None
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

        self.name = None
        # type: str

        self.title = None
        # type: str

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.copyright = None
        # type: str

        self.stringency = None
        # type: str
        # possible values: comparable, fully-specified, equivalent,
        # convertable, scaleable, flexible

        self.mapping = None
        # type: list
        # reference to DataElement_Mapping

        self.element = None
        # type: list
        # reference to ElementDefinition

        self.identifier = None
        # type: list
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

        if self.stringency is not None:
            for value in self.stringency:
                if value is not None and value.lower() not in [
                    'comparable', 'fully-specified', 'equivalent', 'convertable',
                        'scaleable', 'flexible']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'comparable, fully-specified, equivalent, convertable, scaleable,'
                        'flexible'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'identifier'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'element'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'useContext'},

            {'parent_entity': 'DataElement_Mapping',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'mapping'},
        ]


class DataElement_Mapping(fhirbase):
    """
    The formal description of a single piece of information that can be
    gathered and reported.

    Args:
        identity: An internal id that is used to identify this mapping set
            when specific mappings are made on a per-element basis.
        uri: An absolute URI that identifies the specification that this
            mapping is expressed to.
        name: A name for the specification that is being mapped to.
        comment: Comments about this mapping, including version notes, issues,
            scope limitations, and other important notes for usage.
    """

    __name__ = 'DataElement_Mapping'

    def __init__(self, dict_values=None):
        self.identity = None
        # type: str

        self.uri = None
        # type: str

        self.name = None
        # type: str

        self.comment = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
