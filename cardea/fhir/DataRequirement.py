from .fhirbase import fhirbase


class DataRequirement(fhirbase):
    """
    Describes a required data item for evaluation in terms of the type of
    data, and optional code or date-based filters of the data.

    Args:
        type: The type of the required data, specified as the type name of a
            resource. For profiles, this value is set to the type of the base
            resource of the profile.
        profile: The profile of the required data, specified as the uri of the
            profile definition.
        mustSupport: Indicates that specific elements of the type are
            referenced by the knowledge module and must be supported by the
            consumer in order to obtain an effective evaluation. This does not
            mean that a value is required for this element, only that the
            consuming system must understand the element and be able to provide
            values for it if they are available. Note that the value for this
            element can be a path to allow references to nested elements. In that
            case, all the elements along the path must be supported.
        codeFilter: Code filters specify additional constraints on the data,
            specifying the value set of interest for a particular element of the
            data.
        dateFilter: Date filters specify additional constraints on the data in
            terms of the applicable date range for specific elements.
    """

    __name__ = 'DataRequirement'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str

        self.profile = None
        # type: list

        self.mustSupport = None
        # type: list

        self.codeFilter = None
        # type: list
        # reference to DataRequirement_CodeFilter

        self.dateFilter = None
        # type: list
        # reference to DataRequirement_DateFilter

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'DataRequirement_DateFilter',
             'parent_variable': 'object_id',
             'child_entity': 'DataRequirement',
             'child_variable': 'dateFilter'},

            {'parent_entity': 'DataRequirement_CodeFilter',
             'parent_variable': 'object_id',
             'child_entity': 'DataRequirement',
             'child_variable': 'codeFilter'},
        ]


class DataRequirement_CodeFilter(fhirbase):
    """
    Describes a required data item for evaluation in terms of the type of
    data, and optional code or date-based filters of the data.

    Args:
        path: The code-valued attribute of the filter. The specified path must
            be resolvable from the type of the required data. The path is allowed
            to contain qualifiers (.) to traverse sub-elements, as well as
            indexers ([x]) to traverse multiple-cardinality sub-elements. Note
            that the index must be an integer constant. The path must resolve to
            an element of type code, Coding, or CodeableConcept.
        valueSetString: The valueset for the code filter. The valueSet and
            value elements are exclusive. If valueSet is specified, the filter
            will return only those data items for which the value of the
            code-valued element specified in the path is a member of the specified
            valueset.
        valueSetReference: The valueset for the code filter. The valueSet and
            value elements are exclusive. If valueSet is specified, the filter
            will return only those data items for which the value of the
            code-valued element specified in the path is a member of the specified
            valueset.
        valueCode: The codes for the code filter. Only one of valueSet,
            valueCode, valueCoding, or valueCodeableConcept may be specified. If
            values are given, the filter will return only those data items for
            which the code-valued attribute specified by the path has a value that
            is one of the specified codes.
        valueCoding: The Codings for the code filter. Only one of valueSet,
            valueCode, valueConding, or valueCodeableConcept may be specified. If
            values are given, the filter will return only those data items for
            which the code-valued attribute specified by the path has a value that
            is one of the specified Codings.
        valueCodeableConcept: The CodeableConcepts for the code filter. Only
            one of valueSet, valueCode, valueConding, or valueCodeableConcept may
            be specified. If values are given, the filter will return only those
            data items for which the code-valued attribute specified by the path
            has a value that is one of the specified CodeableConcepts.
    """

    __name__ = 'DataRequirement_CodeFilter'

    def __init__(self, dict_values=None):
        self.path = None
        # type: str

        self.valueSetString = None
        # type: str

        self.valueSetReference = None
        # reference to Reference: identifier

        self.valueCode = None
        # type: list

        self.valueCoding = None
        # type: list
        # reference to Coding

        self.valueCodeableConcept = None
        # type: list
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DataRequirement_CodeFilter',
             'child_variable': 'valueSetReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DataRequirement_CodeFilter',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'DataRequirement_CodeFilter',
             'child_variable': 'valueCoding'},
        ]


class DataRequirement_DateFilter(fhirbase):
    """
    Describes a required data item for evaluation in terms of the type of
    data, and optional code or date-based filters of the data.

    Args:
        path: The date-valued attribute of the filter. The specified path must
            be resolvable from the type of the required data. The path is allowed
            to contain qualifiers (.) to traverse sub-elements, as well as
            indexers ([x]) to traverse multiple-cardinality sub-elements. Note
            that the index must be an integer constant. The path must resolve to
            an element of type dateTime, Period, Schedule, or Timing.
        valueDateTime: The value of the filter. If period is specified, the
            filter will return only those data items that fall within the bounds
            determined by the Period, inclusive of the period boundaries. If
            dateTime is specified, the filter will return only those data items
            that are equal to the specified dateTime. If a Duration is specified,
            the filter will return only those data items that fall within Duration
            from now.
        valuePeriod: The value of the filter. If period is specified, the
            filter will return only those data items that fall within the bounds
            determined by the Period, inclusive of the period boundaries. If
            dateTime is specified, the filter will return only those data items
            that are equal to the specified dateTime. If a Duration is specified,
            the filter will return only those data items that fall within Duration
            from now.
        valueDuration: The value of the filter. If period is specified, the
            filter will return only those data items that fall within the bounds
            determined by the Period, inclusive of the period boundaries. If
            dateTime is specified, the filter will return only those data items
            that are equal to the specified dateTime. If a Duration is specified,
            the filter will return only those data items that fall within Duration
            from now.
    """

    __name__ = 'DataRequirement_DateFilter'

    def __init__(self, dict_values=None):
        self.path = None
        # type: str

        self.valueDateTime = None
        # type: str

        self.valuePeriod = None
        # reference to Period

        self.valueDuration = None
        # reference to Duration

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DataRequirement_DateFilter',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'DataRequirement_DateFilter',
             'child_variable': 'valueDuration'},
        ]
