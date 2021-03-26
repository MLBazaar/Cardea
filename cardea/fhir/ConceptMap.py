from .fhirbase import fhirbase


class ConceptMap(fhirbase):
    """
    A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.

    Args:
        resourceType: This is a ConceptMap resource
        url: An absolute URI that is used to identify this concept map when it
            is referenced in a specification, model, design or an instance. This
            SHALL be a URL, SHOULD be globally unique, and SHOULD be an address at
            which this concept map is (or will be) published. The URL SHOULD
            include the major version of the concept map. For more information see
            [Technical and Business Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this concept
            map when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            concept map when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the concept map author
            and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There
            is also no expectation that versions can be placed in a
            lexicographical sequence.
        name: A natural language name identifying the concept map. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        title: A short, descriptive, user-friendly title for the concept map.
        status: The status of this concept map. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this concept map is
            authored for testing purposes (or education/evaluation/marketing), and
            is not intended to be used for genuine usage.
        date: The date  (and optionally time) when the concept map was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the concept map changes.
        publisher: The name of the individual or organization that published
            the concept map.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the concept
            map from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate concept map
            instances.
        jurisdiction: A legal or geographic region in which the concept map is
            intended to be used.
        purpose: Explaination of why this concept map is needed and why it has
            been designed as it has.
        copyright: A copyright statement relating to the concept map and/or
            its contents. Copyright statements are generally legal restrictions on
            the use and publishing of the concept map.
        sourceUri: The source value set that specifies the concepts that are
            being mapped.
        sourceReference: The source value set that specifies the concepts that
            are being mapped.
        targetUri: The target value set provides context to the mappings. Note
            that the mapping is made between concepts, not between value sets, but
            the value set provides important context about how the concept mapping
            choices are made.
        targetReference: The target value set provides context to the
            mappings. Note that the mapping is made between concepts, not between
            value sets, but the value set provides important context about how the
            concept mapping choices are made.
        group: A group of mappings that all have the same source and target
            system.
    """

    __name__ = 'ConceptMap'

    def __init__(self, dict_values=None):
        self.resourceType = 'ConceptMap'
        # type: str
        # possible values: ConceptMap

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

        self.sourceUri = None
        # type: str

        self.sourceReference = None
        # reference to Reference: identifier

        self.targetUri = None
        # type: str

        self.targetReference = None
        # reference to Reference: identifier

        self.group = None
        # type: list
        # reference to ConceptMap_Group

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ConceptMap',
             'child_variable': 'sourceReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ConceptMap',
             'child_variable': 'targetReference'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'contact'},

            {'parent_entity': 'ConceptMap_Group',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'group'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'identifier'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap',
             'child_variable': 'jurisdiction'},
        ]


class ConceptMap_Group(fhirbase):
    """
    A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.

    Args:
        source: An absolute URI that identifies the Code System (if the source
            is a value set that crosses more than one code system).
        sourceVersion: The specific version of the code system, as determined
            by the code system authority.
        target: An absolute URI that identifies the code system of the target
            code (if the target is a value set that cross code systems).
        targetVersion: The specific version of the code system, as determined
            by the code system authority.
        element: Mappings for an individual concept in the source to one or
            more concepts in the target.
        unmapped: What to do when there is no match in the mappings in the
            group.
    """

    __name__ = 'ConceptMap_Group'

    def __init__(self, dict_values=None):
        self.source = None
        # type: str

        self.sourceVersion = None
        # type: str

        self.target = None
        # type: str

        self.targetVersion = None
        # type: str

        self.element = None
        # type: list
        # reference to ConceptMap_Element

        self.unmapped = None
        # reference to ConceptMap_Unmapped

        self.object_id = None
        # unique identifier for object class

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
    """
    A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.

    Args:
        code: Identity (code or path) or the element/item being mapped.
        display: The display for the code. The display is only provided to
            help editors when editing the concept map.
        target: A concept from the target value set that this concept maps to.
    """

    __name__ = 'ConceptMap_Element'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.display = None
        # type: str

        self.target = None
        # type: list
        # reference to ConceptMap_Target

        self.object_id = None
        # unique identifier for object class

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
    """
    A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.

    Args:
        code: Identity (code or path) or the element/item that the map refers
            to.
        display: The display for the code. The display is only provided to
            help editors when editing the concept map.
        equivalence: The equivalence between the source and target concepts
            (counting for the dependencies and products). The equivalence is read
            from target to source (e.g. the target is 'wider' than the source).
        comment: A description of status/issues in mapping that conveys
            additional information not represented in  the structured data.
        dependsOn: A set of additional dependencies for this mapping to hold.
            This mapping is only applicable if the specified element can be
            resolved, and it has the specified value.
        product: A set of additional outcomes from this mapping to other
            elements. To properly execute this mapping, the specified element must
            be mapped to some data element or source that is in context. The
            mapping may still be useful without a place for the additional data
            elements, but the equivalence cannot be relied on.
    """

    __name__ = 'ConceptMap_Target'

    def __init__(self, dict_values=None):
        self.code = None
        # type: str

        self.display = None
        # type: str

        self.equivalence = None
        # type: str
        # possible values: relatedto, equivalent, equal, wider,
        # subsumes, narrower, specializes, inexact, unmatched, disjoint

        self.comment = None
        # type: str

        self.dependsOn = None
        # type: list
        # reference to ConceptMap_DependsOn

        self.product = None
        # type: list
        # reference to ConceptMap_DependsOn

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.equivalence is not None:
            for value in self.equivalence:
                if value is not None and value.lower() not in [
                    'relatedto', 'equivalent', 'equal', 'wider', 'subsumes', 'narrower',
                        'specializes', 'inexact', 'unmatched', 'disjoint']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'relatedto, equivalent, equal, wider, subsumes, narrower, '
                        'specializes, inexact, unmatched, disjoint'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ConceptMap_DependsOn',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap_Target',
             'child_variable': 'product'},

            {'parent_entity': 'ConceptMap_DependsOn',
             'parent_variable': 'object_id',
             'child_entity': 'ConceptMap_Target',
             'child_variable': 'dependsOn'},
        ]


class ConceptMap_DependsOn(fhirbase):
    """
    A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.

    Args:
        property: A reference to an element that holds a coded value that
            corresponds to a code system property. The idea is that the
            information model carries an element somwhere that is labeled to
            correspond with a code system property.
        system: An absolute URI that identifies the code system of the
            dependency code (if the source/dependency is a value set that crosses
            code systems).
        code: Identity (code or path) or the element/item/ValueSet that the
            map depends on / refers to.
        display: The display for the code. The display is only provided to
            help editors when editing the concept map.
    """

    __name__ = 'ConceptMap_DependsOn'

    def __init__(self, dict_values=None):
        self.property = None
        # type: str

        self.system = None
        # type: str

        self.code = None
        # type: str

        self.display = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class ConceptMap_Unmapped(fhirbase):
    """
    A statement of relationships from one set of concepts to one or more
    other concepts - either code systems or data elements, or classes in
    class models.

    Args:
        mode: Defines which action to take if there is no match in the group.
            One of 3 actions is possible: use the unmapped code (this is useful
            when doing a mapping between versions, and only a few codes have
            changed), use a fixed code (a default code), or alternatively, a
            reference to a different concept map can be provided (by canonical
            URL).
        code: The fixed code to use when the mode = 'fixed'  - all unmapped
            codes are mapped to a single fixed code.
        display: The display for the code. The display is only provided to
            help editors when editing the concept map.
        url: The canonical URL of the map to use if this map contains no
            mapping.
    """

    __name__ = 'ConceptMap_Unmapped'

    def __init__(self, dict_values=None):
        self.mode = None
        # type: str
        # possible values: provided, fixed, other-map

        self.code = None
        # type: str

        self.display = None
        # type: str

        self.url = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'provided', 'fixed', 'other-map']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'provided, fixed, other-map'))
