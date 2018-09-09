from .fhirbase import fhirbase


class Medication(fhirbase):
    """This resource is primarily used for the identification and definition of
    a medication. It covers the ingredients and the packaging for a
    medication.
    """

    __name__ = 'Medication'

    def __init__(self, dict_values=None):
        # this is a medication resource
        self.resourceType = 'Medication'
        # type = string
        # possible values: Medication

        # a code (or set of codes) that specify this medication, or a textual
        # description if no code is available. usage note: this could be a
        # standard medication code such as a code from rxnorm, snomed ct, idmp
        # etc. it could also be a national or local formulary code, optionally
        # with translations to other code systems.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # a code to indicate if the medication is in active use.
        self.status = None
        # type = string
        # possible values: active, inactive, entered-in-error

        # set to true if the item is attributable to a specific manufacturer.
        self.isBrand = None
        # type = boolean

        # set to true if the medication can be obtained without an order from a
        # prescriber.
        self.isOverTheCounter = None
        # type = boolean

        # describes the details of the manufacturer of the medication product.
        # this is not intended to represent the distributor of a medication
        # product.
        self.manufacturer = None
        # reference to Reference: identifier

        # describes the form of the item.  powder; tablets; capsule.
        self.form = None
        # reference to CodeableConcept: CodeableConcept

        # identifies a particular constituent of interest in the product.
        self.ingredient = None
        # type = array
        # reference to Medication_Ingredient: Medication_Ingredient

        # information that only applies to packages (not products).
        self.package = None
        # reference to Medication_Package: Medication_Package

        # photo(s) or graphic representation(s) of the medication.
        self.image = None
        # type = array
        # reference to Attachment: Attachment

        # unique identifier for object class
        self.object_id = None

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Medication',
             'child_variable': 'manufacturer'},

            {'parent_entity': 'Medication_Ingredient',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'ingredient'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'image'},

            {'parent_entity': 'Medication_Package',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'package'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication',
             'child_variable': 'form'},
        ]


class Medication_Ingredient(fhirbase):
    """This resource is primarily used for the identification and definition of
    a medication. It covers the ingredients and the packaging for a
    medication.
    """

    __name__ = 'Medication_Ingredient'

    def __init__(self, dict_values=None):
        # the actual ingredient - either a substance (simple ingredient) or
        # another medication.
        self.itemCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the actual ingredient - either a substance (simple ingredient) or
        # another medication.
        self.itemReference = None
        # reference to Reference: identifier

        # indication of whether this ingredient affects the therapeutic action of
        # the drug.
        self.isActive = None
        # type = boolean

        # specifies how many (or how much) of the items there are in this
        # medication.  for example, 250 mg per tablet.  this is expressed as a
        # ratio where the numerator is 250mg and the denominator is 1 tablet.
        self.amount = None
        # reference to Ratio: Ratio

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Ingredient',
             'child_variable': 'itemCodeableConcept'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Ingredient',
             'child_variable': 'amount'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Medication_Ingredient',
             'child_variable': 'itemReference'},
        ]


class Medication_Package(fhirbase):
    """This resource is primarily used for the identification and definition of
    a medication. It covers the ingredients and the packaging for a
    medication.
    """

    __name__ = 'Medication_Package'

    def __init__(self, dict_values=None):
        # the kind of container that this package comes as.
        self.container = None
        # reference to CodeableConcept: CodeableConcept

        # a set of components that go to make up the described item.
        self.content = None
        # type = array
        # reference to Medication_Content: Medication_Content

        # information about a group of medication produced or packaged from one
        # production run.
        self.batch = None
        # type = array
        # reference to Medication_Batch: Medication_Batch

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Package',
             'child_variable': 'container'},

            {'parent_entity': 'Medication_Batch',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Package',
             'child_variable': 'batch'},

            {'parent_entity': 'Medication_Content',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Package',
             'child_variable': 'content'},
        ]


class Medication_Content(fhirbase):
    """This resource is primarily used for the identification and definition of
    a medication. It covers the ingredients and the packaging for a
    medication.
    """

    __name__ = 'Medication_Content'

    def __init__(self, dict_values=None):
        # identifies one of the items in the package.
        self.itemCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # identifies one of the items in the package.
        self.itemReference = None
        # reference to Reference: identifier

        # the amount of the product that is in the package.
        self.amount = None
        # reference to Quantity: Quantity

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Content',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Medication_Content',
             'child_variable': 'itemCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Medication_Content',
             'child_variable': 'itemReference'},
        ]


class Medication_Batch(fhirbase):
    """This resource is primarily used for the identification and definition of
    a medication. It covers the ingredients and the packaging for a
    medication.
    """

    __name__ = 'Medication_Batch'

    def __init__(self, dict_values=None):
        # the assigned lot number of a batch of the specified product.
        self.lotNumber = None
        # type = string

        # when this specific batch of product will expire.
        self.expirationDate = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
