from .fhirbase import fhirbase


class Substance(fhirbase):
    """
    A homogeneous material with a definite composition.
    """

    __name__ = 'Substance'

    def __init__(self, dict_values=None):
        self.resourceType = 'Substance'
        """
        This is a Substance resource

        type: string
        possible values: Substance
        """

        self.status = None
        """
        A code to indicate if the substance is actively used.

        type: string
        possible values: active, inactive, entered-in-error
        """

        self.category = None
        """
        A code that classifies the general type of substance.  This is used
        for searching, sorting and display purposes.

        type: array
        reference to CodeableConcept
        """

        self.code = None
        """
        A code (or set of codes) that identify this substance.

        reference to CodeableConcept
        """

        self.description = None
        """
        A description of the substance - its appearance, handling
        requirements, and other usage notes.

        type: string
        """

        self.instance = None
        """
        Substance may be used to describe a kind of substance, or a specific
        package/container of the substance: an instance.

        type: array
        reference to Substance_Instance: identifier
        """

        self.ingredient = None
        """
        A substance can be composed of other substances.

        type: array
        reference to Substance_Ingredient
        """

        self.identifier = None
        """
        Unique identifier for the substance.

        type: array
        reference to Identifier
        """

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
             'child_variable': 'code'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Substance',
             'child_variable': 'identifier'},

            {'parent_entity': 'Substance_Ingredient',
             'parent_variable': 'object_id',
             'child_entity': 'Substance',
             'child_variable': 'ingredient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Substance',
             'child_variable': 'category'},

            {'parent_entity': 'Substance_Instance',
             'parent_variable': 'identifier',
             'child_entity': 'Substance',
             'child_variable': 'instance'},
        ]


class Substance_Instance(fhirbase):
    """
    A homogeneous material with a definite composition.
    """

    __name__ = 'Substance_Instance'

    def __init__(self, dict_values=None):
        self.expiry = None
        """
        When the substance is no longer valid to use. For some substances, a
        single arbitrary date is used for expiry.

        type: string
        """

        self.quantity = None
        """
        The amount of the substance.

        reference to Quantity
        """

        self.identifier = None
        """
        Identifier associated with the package/container (usually a label
        affixed directly).

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Instance',
             'child_variable': 'identifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Instance',
             'child_variable': 'quantity'},
        ]


class Substance_Ingredient(fhirbase):
    """
    A homogeneous material with a definite composition.
    """

    __name__ = 'Substance_Ingredient'

    def __init__(self, dict_values=None):
        self.quantity = None
        """
        The amount of the ingredient in the substance - a concentration ratio.

        reference to Ratio
        """

        self.substanceCodeableConcept = None
        """
        Another substance that is a component of this substance.

        reference to CodeableConcept
        """

        self.substanceReference = None
        """
        Another substance that is a component of this substance.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Ingredient',
             'child_variable': 'substanceCodeableConcept'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Substance_Ingredient',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Substance_Ingredient',
             'child_variable': 'substanceReference'},
        ]
