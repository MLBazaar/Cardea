from .fhirbase import fhirbase


class Substance(fhirbase):
    """A homogeneous material with a definite composition.
    """

    def __init__(self, dict_values=None):
        # this is a substance resource
        self.resourceType = 'Substance'
        # type = string
        # possible values: Substance

        # a code to indicate if the substance is actively used.
        self.status = None
        # type = string
        # possible values: active, inactive, entered-in-error

        # a code that classifies the general type of substance.  this is used  for
        # searching, sorting and display purposes.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a code (or set of codes) that identify this substance.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a description of the substance - its appearance, handling requirements,
        # and other usage notes.
        self.description = None
        # type = string

        # substance may be used to describe a kind of substance, or a specific
        # package/container of the substance: an instance.
        self.instance = None
        # type = array
        # reference to Substance_Instance: identifier

        # a substance can be composed of other substances.
        self.ingredient = None
        # type = array
        # reference to Substance_Ingredient: Substance_Ingredient

        # unique identifier for the substance.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Substance',
             'child_variable': 'category'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Substance',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Substance',
             'child_variable': 'code'},

            {'parent_entity': 'Substance_Ingredient',
             'parent_variable': 'object_id',
             'child_entity': 'Substance',
             'child_variable': 'ingredient'},

            {'parent_entity': 'Substance_Instance',
             'parent_variable': 'identifier',
             'child_entity': 'Substance',
             'child_variable': 'instance'},
        ]


class Substance_Instance(fhirbase):
    """A homogeneous material with a definite composition.
    """

    def __init__(self, dict_values=None):
        # when the substance is no longer valid to use. for some substances, a
        # single arbitrary date is used for expiry.
        self.expiry = None
        # type = string

        # the amount of the substance.
        self.quantity = None
        # reference to Quantity: Quantity

        # identifier associated with the package/container (usually a label
        # affixed directly).
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Instance',
             'child_variable': 'quantity'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Instance',
             'child_variable': 'identifier'},
        ]


class Substance_Ingredient(fhirbase):
    """A homogeneous material with a definite composition.
    """

    def __init__(self, dict_values=None):
        # the amount of the ingredient in the substance - a concentration ratio.
        self.quantity = None
        # reference to Ratio: Ratio

        # another substance that is a component of this substance.
        self.substanceCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # another substance that is a component of this substance.
        self.substanceReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Substance_Ingredient',
             'child_variable': 'substanceReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Ingredient',
             'child_variable': 'substanceCodeableConcept'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Ingredient',
             'child_variable': 'quantity'},
        ]
