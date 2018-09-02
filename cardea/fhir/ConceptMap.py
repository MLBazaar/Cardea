from .fhirbase import fhirbase


class ConceptMap(fhirbase):
    """A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.
    """

    def __init__(self, dict_values=None):
        # this is a conceptmap resource
        self.resourceType = 'ConceptMap'
        # type = string
        # possible values: ConceptMap

        # an absolute uri that is used to identify this concept map when it is
        # referenced in a specification, model, design or an instance. this shall
        # be a url, should be globally unique, and should be an address at which
        # this concept map is (or will be) published. the url should include the
        # major version of the concept map. for more information see [technical
        # and business versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the concept map
        # when it is referenced in a specification, model, design or instance.
        # this is an arbitrary value managed by the concept map author and is not
        # expected to be globally unique. for example, it might be a timestamp
        # (e.g. yyyymmdd) if a managed version is not available. there is also no
        # expectation that versions can be placed in a lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the concept map. this name should be
        # usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the concept map.
        self.title = None
        # type = string

        # the status of this concept map. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this concept map is authored for
        # testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the concept map was published. the
        # date must change if and when the business version changes and it must
        # change if the status code changes. in addition, it should change when
        # the substantive content of the concept map changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the concept
        # map.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the concept map from a
        # consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate concept map instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the concept map is intended to be
        # used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # explaination of why this concept map is needed and why it has been
        # designed as it has.
        self.purpose = None
        # type = string

        # a copyright statement relating to the concept map and/or its contents.
        # copyright statements are generally legal restrictions on the use and
        # publishing of the concept map.
        self.copyright = None
        # type = string

        # the source value set that specifies the concepts that are being mapped.
        self.sourceUri = None
        # type = string

        # the source value set that specifies the concepts that are being mapped.
        self.sourceReference = None
        # reference to Reference: identifier

        # the target value set provides context to the mappings. note that the
        # mapping is made between concepts, not between value sets, but the value
        # set provides important context about how the concept mapping choices are
        # made.
        self.targetUri = None
        # type = string

        # the target value set provides context to the mappings. note that the
        # mapping is made between concepts, not between value sets, but the value
        # set provides important context about how the concept mapping choices are
        # made.
        self.targetReference = None
        # reference to Reference: identifier

        # a group of mappings that all have the same source and target system.
        self.group = None
        # type = array
        # reference to ConceptMap_Group: ConceptMap_Group

        # a formal identifier that is used to identify this concept map when it is
        # represented in other formats, or referenced in a specification, model,
        # design or an instance.
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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ConceptMap',
             'child_variable': 'targetReference'},

            {'parent_entity': 'ConceptMap_Group',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'group'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ConceptMap',
             'child_variable': 'sourceReference'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'useContext'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'identifier'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'jurisdiction'},
        ]


class ConceptMap_Group(fhirbase):
    """A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.
    """

    def __init__(self, dict_values=None):
        # an absolute uri that identifies the code system (if the source is a
        # value set that crosses more than one code system).
        self.source = None
        # type = string

        # the specific version of the code system, as determined by the code
        # system authority.
        self.sourceVersion = None
        # type = string

        # an absolute uri that identifies the code system of the target code (if
        # the target is a value set that cross code systems).
        self.target = None
        # type = string

        # the specific version of the code system, as determined by the code
        # system authority.
        self.targetVersion = None
        # type = string

        # mappings for an individual concept in the source to one or more concepts
        # in the target.
        self.element = None
        # type = array
        # reference to ConceptMap_Element: ConceptMap_Element

        # what to do when there is no match in the mappings in the group.
        self.unmapped = None
        # reference to ConceptMap_Unmapped: ConceptMap_Unmapped

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ConceptMap_Unmapped',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap_Group',
             'child_variable': 'unmapped'},

            {'parent_entity': 'ConceptMap_Element',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap_Group',
             'child_variable': 'element'},
        ]


class ConceptMap_Element(fhirbase):
    """A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.
    """

    def __init__(self, dict_values=None):
        # identity (code or path) or the element/item being mapped.
        self.code = None
        # type = string

        # the display for the code. the display is only provided to help editors
        # when editing the concept map.
        self.display = None
        # type = string

        # a concept from the target value set that this concept maps to.
        self.target = None
        # type = array
        # reference to ConceptMap_Target: ConceptMap_Target

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ConceptMap_Target',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap_Element',
             'child_variable': 'target'},
        ]


class ConceptMap_Target(fhirbase):
    """A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.
    """

    def __init__(self, dict_values=None):
        # identity (code or path) or the element/item that the map refers to.
        self.code = None
        # type = string

        # the display for the code. the display is only provided to help editors
        # when editing the concept map.
        self.display = None
        # type = string

        # the equivalence between the source and target concepts (counting for the
        # dependencies and products). the equivalence is read from target to
        # source (e.g. the target is 'wider' than the source).
        self.equivalence = None
        # type = string
        # possible values: relatedto, equivalent, equal, wider,
        # subsumes, narrower, specializes, inexact, unmatched, disjoint

        # a description of status/issues in mapping that conveys additional
        # information not represented in  the structured data.
        self.comment = None
        # type = string

        # a set of additional dependencies for this mapping to hold. this mapping
        # is only applicable if the specified element can be resolved, and it has
        # the specified value.
        self.dependsOn = None
        # type = array
        # reference to ConceptMap_DependsOn: ConceptMap_DependsOn

        # a set of additional outcomes from this mapping to other elements. to
        # properly execute this mapping, the specified element must be mapped to
        # some data element or source that is in context. the mapping may still be
        # useful without a place for the additional data elements, but the
        # equivalence cannot be relied on.
        self.product = None
        # type = array
        # reference to ConceptMap_DependsOn: ConceptMap_DependsOn

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.equivalence is not None:
            for value in self.equivalence:
                if value is not None and value.lower() not in [
                    'relatedto', 'equivalent', 'equal', 'wider', 'subsumes', 'narrower',
                        'specializes', 'inexact', 'unmatched', 'disjoint']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'relatedto, equivalent, equal, wider, subsumes, narrower,'
                        'specializes, inexact, unmatched, disjoint'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ConceptMap_DependsOn',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap_Target',
             'child_variable': 'dependsOn'},

            {'parent_entity': 'ConceptMap_DependsOn',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap_Target',
             'child_variable': 'product'},
        ]


class ConceptMap_DependsOn(fhirbase):
    """A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.
    """

    def __init__(self, dict_values=None):
        # a reference to an element that holds a coded value that corresponds to a
        # code system property. the idea is that the information model carries an
        # element somwhere that is labeled to correspond with a code system
        # property.
        self.property = None
        # type = string

        # an absolute uri that identifies the code system of the dependency code
        # (if the source/dependency is a value set that crosses code systems).
        self.system = None
        # type = string

        # identity (code or path) or the element/item/valueset that the map
        # depends on / refers to.
        self.code = None
        # type = string

        # the display for the code. the display is only provided to help editors
        # when editing the concept map.
        self.display = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class ConceptMap_Unmapped(fhirbase):
    """A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.
    """

    def __init__(self, dict_values=None):
        # defines which action to take if there is no match in the group. one of 3
        # actions is possible: use the unmapped code (this is useful when doing a
        # mapping between versions, and only a few codes have changed), use a
        # fixed code (a default code), or alternatively, a reference to a
        # different concept map can be provided (by canonical url).
        self.mode = None
        # type = string
        # possible values: provided, fixed, other-map

        # the fixed code to use when the mode = 'fixed'  - all unmapped codes are
        # mapped to a single fixed code.
        self.code = None
        # type = string

        # the display for the code. the display is only provided to help editors
        # when editing the concept map.
        self.display = None
        # type = string

        # the canonical url of the map to use if this map contains no mapping.
        self.url = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'provided', 'fixed', 'other-map']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'provided, fixed, other-map'))
