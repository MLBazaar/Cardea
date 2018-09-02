from .fhirbase import fhirbase


class DataRequirement(fhirbase):
    """Describes a required data item for evaluation in terms of the type of
    data, and optional code or date-based filters of the data.
    """

    def __init__(self, dict_values=None):
        # the type of the required data, specified as the type name of a resource.
        # for profiles, this value is set to the type of the base resource of the
        # profile.
        self.type = None
        # type = string

        # the profile of the required data, specified as the uri of the profile
        # definition.
        self.profile = None
        # type = array

        # indicates that specific elements of the type are referenced by the
        # knowledge module and must be supported by the consumer in order to
        # obtain an effective evaluation. this does not mean that a value is
        # required for this element, only that the consuming system must
        # understand the element and be able to provide values for it if they are
        # available. note that the value for this element can be a path to allow
        # references to nested elements. in that case, all the elements along the
        # path must be supported.
        self.mustSupport = None
        # type = array

        # code filters specify additional constraints on the data, specifying the
        # value set of interest for a particular element of the data.
        self.codeFilter = None
        # type = array
        # reference to DataRequirement_CodeFilter: DataRequirement_CodeFilter

        # date filters specify additional constraints on the data in terms of the
        # applicable date range for specific elements.
        self.dateFilter = None
        # type = array
        # reference to DataRequirement_DateFilter: DataRequirement_DateFilter

        # unique identifier for object class
        self.object_id = None

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
    """Describes a required data item for evaluation in terms of the type of
    data, and optional code or date-based filters of the data.
    """

    def __init__(self, dict_values=None):
        # the code-valued attribute of the filter. the specified path must be
        # resolvable from the type of the required data. the path is allowed to
        # contain qualifiers (.) to traverse sub-elements, as well as indexers
        # ([x]) to traverse multiple-cardinality sub-elements. note that the index
        # must be an integer constant. the path must resolve to an element of type
        # code, coding, or codeableconcept.
        self.path = None
        # type = string

        # the valueset for the code filter. the valueset and value elements are
        # exclusive. if valueset is specified, the filter will return only those
        # data items for which the value of the code-valued element specified in
        # the path is a member of the specified valueset.
        self.valueSetString = None
        # type = string

        # the valueset for the code filter. the valueset and value elements are
        # exclusive. if valueset is specified, the filter will return only those
        # data items for which the value of the code-valued element specified in
        # the path is a member of the specified valueset.
        self.valueSetReference = None
        # reference to Reference: identifier

        # the codes for the code filter. only one of valueset, valuecode,
        # valuecoding, or valuecodeableconcept may be specified. if values are
        # given, the filter will return only those data items for which the code-
        # valued attribute specified by the path has a value that is one of the
        # specified codes.
        self.valueCode = None
        # type = array

        # the codings for the code filter. only one of valueset, valuecode,
        # valueconding, or valuecodeableconcept may be specified. if values are
        # given, the filter will return only those data items for which the code-
        # valued attribute specified by the path has a value that is one of the
        # specified codings.
        self.valueCoding = None
        # type = array
        # reference to Coding: Coding

        # the codeableconcepts for the code filter. only one of valueset,
        # valuecode, valueconding, or valuecodeableconcept may be specified. if
        # values are given, the filter will return only those data items for which
        # the code-valued attribute specified by the path has a value that is one
        # of the specified codeableconcepts.
        self.valueCodeableConcept = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

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
    """Describes a required data item for evaluation in terms of the type of
    data, and optional code or date-based filters of the data.
    """

    def __init__(self, dict_values=None):
        # the date-valued attribute of the filter. the specified path must be
        # resolvable from the type of the required data. the path is allowed to
        # contain qualifiers (.) to traverse sub-elements, as well as indexers
        # ([x]) to traverse multiple-cardinality sub-elements. note that the index
        # must be an integer constant. the path must resolve to an element of type
        # datetime, period, schedule, or timing.
        self.path = None
        # type = string

        # the value of the filter. if period is specified, the filter will return
        # only those data items that fall within the bounds determined by the
        # period, inclusive of the period boundaries. if datetime is specified,
        # the filter will return only those data items that are equal to the
        # specified datetime. if a duration is specified, the filter will return
        # only those data items that fall within duration from now.
        self.valueDateTime = None
        # type = string

        # the value of the filter. if period is specified, the filter will return
        # only those data items that fall within the bounds determined by the
        # period, inclusive of the period boundaries. if datetime is specified,
        # the filter will return only those data items that are equal to the
        # specified datetime. if a duration is specified, the filter will return
        # only those data items that fall within duration from now.
        self.valuePeriod = None
        # reference to Period: Period

        # the value of the filter. if period is specified, the filter will return
        # only those data items that fall within the bounds determined by the
        # period, inclusive of the period boundaries. if datetime is specified,
        # the filter will return only those data items that are equal to the
        # specified datetime. if a duration is specified, the filter will return
        # only those data items that fall within duration from now.
        self.valueDuration = None
        # reference to Duration: Duration

        # unique identifier for object class
        self.object_id = None

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
