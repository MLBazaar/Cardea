from .fhirbase import fhirbase


class DataElement(fhirbase):
    """The formal description of a single piece of information that can be
    gathered and reported.
    """

    __name__ = 'DataElement'

    def __init__(self, dict_values=None):
        # this is a dataelement resource
        self.resourceType = 'DataElement'
        # type = string
        # possible values: DataElement

        # an absolute uri that is used to identify this data element when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this data element is (or will be) published. the url should include the
        # major version of the data element. for more information see [technical
        # and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the data element
        # when it is referenced in a specification, model, design or instance.
        # this is an arbitrary value managed by the data element author and is not
        # expected to be globally unique. for example, it might be a timestamp
        # (e.g. yyyymmdd) if a managed version is not available. there is also no
        # expectation that versions can be placed in a lexicographical sequence.
        self.version = None
        # type = string

        # the status of this data element. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this data element is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the data element was published. the
        # date must change if and when the business version changes and it must
        # change if the status code changes. in addition, it should change when
        # the substantive content of the data element changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the data
        # element.
        self.publisher = None
        # type = string

        # a natural language name identifying the data element. this name should
        # be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the data element.
        self.title = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate data element instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the data element is intended to be
        # used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a copyright statement relating to the data element and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the data element.
        self.copyright = None
        # type = string

        # identifies how precise the data element is in its definition.
        self.stringency = None
        # type = string
        # possible values: comparable, fully-specified, equivalent,
        # convertable, scaleable, flexible

        # identifies a specification (other than a terminology) that the elements
        # which make up the dataelement have some correspondence with.
        self.mapping = None
        # type = array
        # reference to DataElement_Mapping: DataElement_Mapping

        # defines the structure, type, allowed values and other constraining
        # characteristics of the data element.
        self.element = None
        # type = array
        # reference to ElementDefinition: ElementDefinition

        # a formal identifier that is used to identify this data element when it
        # is represented in other formats, or referenced in a specification,
        # model, design or an instance.
        self.identifier = None
        # type = array
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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'useContext'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'contact'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'identifier'},

            {'parent_entity': 'DataElement_Mapping',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'mapping'},

            {'parent_entity': 'ElementDefinition',
             'parent_variable': 'object_id',
             'child_entity': 'DataElement',
             'child_variable': 'element'},
        ]


class DataElement_Mapping(fhirbase):
    """The formal description of a single piece of information that can be
    gathered and reported.
    """

    __name__ = 'DataElement_Mapping'

    def __init__(self, dict_values=None):
        # an internal id that is used to identify this mapping set when specific
        # mappings are made on a per-element basis.
        self.identity = None
        # type = string

        # an absolute uri that identifies the specification that this mapping is
        # expressed to.
        self.uri = None
        # type = string

        # a name for the specification that is being mapped to.
        self.name = None
        # type = string

        # comments about this mapping, including version notes, issues, scope
        # limitations, and other important notes for usage.
        self.comment = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
