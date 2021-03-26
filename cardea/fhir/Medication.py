from .fhirbase import fhirbase


class Medication(fhirbase):
    """
    This resource is primarily used for the identification and definition
    of a medication. It covers the ingredients and the packaging for a
    medication.

    Args:
        resourceType: This is a Medication resource
        code: A code (or set of codes) that specify this medication, or a
            textual description if no code is available. Usage note: This could be
            a standard medication code such as a code from RxNorm, SNOMED CT, IDMP
            etc. It could also be a national or local formulary code, optionally
            with translations to other code systems.
        status: A code to indicate if the medication is in active use.
        isBrand: Set to true if the item is attributable to a specific
            manufacturer.
        isOverTheCounter: Set to true if the medication can be obtained
            without an order from a prescriber.
        manufacturer: Describes the details of the manufacturer of the
            medication product.  This is not intended to represent the distributor
            of a medication product.
        form: Describes the form of the item.  Powder; tablets; capsule.
        ingredient: Identifies a particular constituent of interest in the
            product.
        package: Information that only applies to packages (not products).
        image: Photo(s) or graphic representation(s) of the medication.
    """

    __name__ = 'Medication'

    def __init__(self, dict_values=None):
        self.resourceType = 'Medication'
        # type: str
        # possible values: Medication

        self.code = None
        # reference to CodeableConcept

        self.status = None
        # type: str
        # possible values: active, inactive, entered-in-error

        self.isBrand = None
        # type: bool

        self.isOverTheCounter = None
        # type: bool

        self.manufacturer = None
        # reference to Reference: identifier

        self.form = None
        # reference to CodeableConcept

        self.ingredient = None
        # type: list
        # reference to Medication_Ingredient

        self.package = None
        # reference to Medication_Package

        self.image = None
        # type: list
        # reference to Attachment

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Medication_Package',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'package'},

            {'parent_entity': 'Medication_Ingredient',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'ingredient'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'image'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Medication',
             'child_variable': 'manufacturer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'code'},
        ]


class Medication_Ingredient(fhirbase):
    """
    This resource is primarily used for the identification and definition
    of a medication. It covers the ingredients and the packaging for a
    medication.

    Args:
        itemCodeableConcept: The actual ingredient - either a substance
            (simple ingredient) or another medication.
        itemReference: The actual ingredient - either a substance (simple
            ingredient) or another medication.
        isActive: Indication of whether this ingredient affects the
            therapeutic action of the drug.
        amount: Specifies how many (or how much) of the items there are in
            this Medication.  For example, 250 mg per tablet.  This is expressed
            as a ratio where the numerator is 250mg and the denominator is 1
            tablet.
    """

    __name__ = 'Medication_Ingredient'

    def __init__(self, dict_values=None):
        self.itemCodeableConcept = None
        # reference to CodeableConcept

        self.itemReference = None
        # reference to Reference: identifier

        self.isActive = None
        # type: bool

        self.amount = None
        # reference to Ratio

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Medication_Ingredient',
             'child_variable': 'itemReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Ingredient',
             'child_variable': 'itemCodeableConcept'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Ingredient',
             'child_variable': 'amount'},
        ]


class Medication_Package(fhirbase):
    """
    This resource is primarily used for the identification and definition
    of a medication. It covers the ingredients and the packaging for a
    medication.

    Args:
        container: The kind of container that this package comes as.
        content: A set of components that go to make up the described item.
        batch: Information about a group of medication produced or packaged
            from one production run.
    """

    __name__ = 'Medication_Package'

    def __init__(self, dict_values=None):
        self.container = None
        # reference to CodeableConcept

        self.content = None
        # type: list
        # reference to Medication_Content

        self.batch = None
        # type: list
        # reference to Medication_Batch

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Medication_Batch',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Package',
             'child_variable': 'batch'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Package',
             'child_variable': 'container'},

            {'parent_entity': 'Medication_Content',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Package',
             'child_variable': 'content'},
        ]


class Medication_Content(fhirbase):
    """
    This resource is primarily used for the identification and definition
    of a medication. It covers the ingredients and the packaging for a
    medication.

    Args:
        itemCodeableConcept: Identifies one of the items in the package.
        itemReference: Identifies one of the items in the package.
        amount: The amount of the product that is in the package.
    """

    __name__ = 'Medication_Content'

    def __init__(self, dict_values=None):
        self.itemCodeableConcept = None
        # reference to CodeableConcept

        self.itemReference = None
        # reference to Reference: identifier

        self.amount = None
        # reference to Quantity

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Medication_Content',
             'child_variable': 'itemReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Content',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Content',
             'child_variable': 'itemCodeableConcept'},
        ]


class Medication_Batch(fhirbase):
    """
    This resource is primarily used for the identification and definition
    of a medication. It covers the ingredients and the packaging for a
    medication.

    Args:
        lotNumber: The assigned lot number of a batch of the specified
            product.
        expirationDate: When this specific batch of product will expire.
    """

    __name__ = 'Medication_Batch'

    def __init__(self, dict_values=None):
        self.lotNumber = None
        # type: str

        self.expirationDate = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
