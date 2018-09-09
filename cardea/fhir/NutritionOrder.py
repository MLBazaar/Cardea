from .fhirbase import fhirbase


class NutritionOrder(fhirbase):
    """A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder'

    def __init__(self, dict_values=None):
        # this is a nutritionorder resource
        self.resourceType = 'NutritionOrder'
        # type = string
        # possible values: NutritionOrder

        # the workflow status of the nutrition order/request.
        self.status = None
        # type = string
        # possible values: proposed, draft, planned, requested, active,
        # on-hold, completed, cancelled, entered-in-error

        # the person (patient) who needs the nutrition order for an oral diet,
        # nutritional supplement and/or enteral or formula feeding.
        self.patient = None
        # reference to Reference: identifier

        # an encounter that provides additional information about the healthcare
        # context in which this request is made.
        self.encounter = None
        # reference to Reference: identifier

        # the date and time that this nutrition order was requested.
        self.dateTime = None
        # type = string

        # the practitioner that holds legal responsibility for ordering the diet,
        # nutritional supplement, or formula feedings.
        self.orderer = None
        # reference to Reference: identifier

        # a link to a record of allergies or intolerances  which should be
        # included in the nutrition order.
        self.allergyIntolerance = None
        # type = array
        # reference to Reference: identifier

        # this modifier is used to convey order-specific modifiers about the type
        # of food that should be given. these can be derived from patient
        # allergies, intolerances, or preferences such as halal, vegan or kosher.
        # this modifier applies to the entire nutrition order inclusive of the
        # oral diet, nutritional supplements and enteral formula feedings.
        self.foodPreferenceModifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # this modifier is used to convey order-specific modifiers about the type
        # of food that should not be given. these can be derived from patient
        # allergies, intolerances, or preferences such as no red meat, no soy or
        # no wheat or  gluten-free.  while it should not be necessary to repeat
        # allergy or intolerance information captured in the referenced
        # allergyintolerance resource in the excludefoodmodifier, this element may
        # be used to convey additional specificity related to foods that should be
        # eliminated from the patient’s diet for any reason.  this modifier
        # applies to the entire nutrition order inclusive of the oral diet,
        # nutritional supplements and enteral formula feedings.
        self.excludeFoodModifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # diet given orally in contrast to enteral (tube) feeding.
        self.oralDiet = None
        # reference to NutritionOrder_OralDiet: NutritionOrder_OralDiet

        # oral nutritional products given in order to add further nutritional
        # value to the patient's diet.
        self.supplement = None
        # type = array
        # reference to NutritionOrder_Supplement: NutritionOrder_Supplement

        # feeding provided through the gastrointestinal tract via a tube,
        # catheter, or stoma that delivers nutrition distal to the oral cavity.
        self.enteralFormula = None
        # reference to NutritionOrder_EnteralFormula: NutritionOrder_EnteralFormula

        # identifiers assigned to this order by the order sender or by the order
        # receiver.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'proposed', 'draft', 'planned', 'requested', 'active', 'on-hold',
                        'completed', 'cancelled', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposed, draft, planned, requested, active, on-hold, completed,'
                        'cancelled, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'foodPreferenceModifier'},

            {'parent_entity': 'NutritionOrder_OralDiet',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'oralDiet'},

            {'parent_entity': 'NutritionOrder_EnteralFormula',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'enteralFormula'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'excludeFoodModifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'allergyIntolerance'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'orderer'},

            {'parent_entity': 'NutritionOrder_Supplement',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'supplement'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'encounter'},
        ]


class NutritionOrder_OralDiet(fhirbase):
    """A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_OralDiet'

    def __init__(self, dict_values=None):
        # the kind of diet or dietary restriction such as fiber restricted diet or
        # diabetic diet.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the time period and frequency at which the diet should be given.  the
        # diet should be given for the combination of all schedules if more than
        # one schedule is present.
        self.schedule = None
        # type = array
        # reference to Timing: Timing

        # class that defines the quantity and type of nutrient modifications (for
        # example carbohydrate, fiber or sodium) required for the oral diet.
        self.nutrient = None
        # type = array
        # reference to NutritionOrder_Nutrient: NutritionOrder_Nutrient

        # class that describes any texture modifications required for the patient
        # to safely consume various types of solid foods.
        self.texture = None
        # type = array
        # reference to NutritionOrder_Texture: NutritionOrder_Texture

        # the required consistency (e.g. honey-thick, nectar-thick, thin,
        # thickened.) of liquids or fluids served to the patient.
        self.fluidConsistencyType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # free text or additional instructions or information pertaining to the
        # oral diet.
        self.instruction = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'NutritionOrder_Texture',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'texture'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'type'},

            {'parent_entity': 'NutritionOrder_Nutrient',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'nutrient'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'schedule'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'fluidConsistencyType'},
        ]


class NutritionOrder_Nutrient(fhirbase):
    """A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Nutrient'

    def __init__(self, dict_values=None):
        # the nutrient that is being modified such as carbohydrate or sodium.
        self.modifier = None
        # reference to CodeableConcept: CodeableConcept

        # the quantity of the specified nutrient to include in diet.
        self.amount = None
        # reference to Quantity: Quantity

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Nutrient',
             'child_variable': 'modifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Nutrient',
             'child_variable': 'amount'},
        ]


class NutritionOrder_Texture(fhirbase):
    """A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Texture'

    def __init__(self, dict_values=None):
        # any texture modifications (for solid foods) that should be made, e.g.
        # easy to chew, chopped, ground, and pureed.
        self.modifier = None
        # reference to CodeableConcept: CodeableConcept

        # the food type(s) (e.g. meats, all foods)  that the texture modification
        # applies to.  this could be all foods types.
        self.foodType = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Texture',
             'child_variable': 'foodType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Texture',
             'child_variable': 'modifier'},
        ]


class NutritionOrder_Supplement(fhirbase):
    """A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Supplement'

    def __init__(self, dict_values=None):
        # the kind of nutritional supplement product required such as a high
        # protein or pediatric clear liquid supplement.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the product or brand name of the nutritional supplement such as "acme
        # protein shake".
        self.productName = None
        # type = string

        # the time period and frequency at which the supplement(s) should be
        # given.  the supplement should be given for the combination of all
        # schedules if more than one schedule is present.
        self.schedule = None
        # type = array
        # reference to Timing: Timing

        # the amount of the nutritional supplement to be given.
        self.quantity = None
        # reference to Quantity: Quantity

        # free text or additional instructions or information pertaining to the
        # oral supplement.
        self.instruction = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Supplement',
             'child_variable': 'quantity'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Supplement',
             'child_variable': 'schedule'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Supplement',
             'child_variable': 'type'},
        ]


class NutritionOrder_EnteralFormula(fhirbase):
    """A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_EnteralFormula'

    def __init__(self, dict_values=None):
        # the type of enteral or infant formula such as an adult standard formula
        # with fiber or a soy-based infant formula.
        self.baseFormulaType = None
        # reference to CodeableConcept: CodeableConcept

        # the product or brand name of the enteral or infant formula product such
        # as "acme adult standard formula".
        self.baseFormulaProductName = None
        # type = string

        # indicates the type of modular component such as protein, carbohydrate,
        # fat or fiber to be provided in addition to or mixed with the base
        # formula.
        self.additiveType = None
        # reference to CodeableConcept: CodeableConcept

        # the product or brand name of the type of modular component to be added
        # to the formula.
        self.additiveProductName = None
        # type = string

        # the amount of energy (calories) that the formula should provide per
        # specified volume, typically per ml or fluid oz.  for example, an infant
        # may require a formula that provides 24 calories per fluid ounce or an
        # adult may require an enteral formula that provides 1.5 calorie/ml.
        self.caloricDensity = None
        # reference to Quantity: Quantity

        # the route or physiological path of administration into the patient's
        # gastrointestinal  tract for purposes of providing the formula feeding,
        # e.g. nasogastric tube.
        self.routeofAdministration = None
        # reference to CodeableConcept: CodeableConcept

        # formula administration instructions as structured data.  this repeating
        # structure allows for changing the administration rate or volume over
        # time for both bolus and continuous feeding.  an example of this would be
        # an instruction to increase the rate of continuous feeding every 2 hours.
        self.administration = None
        # type = array
        # reference to NutritionOrder_Administration: NutritionOrder_Administration

        # the maximum total quantity of formula that may be administered to a
        # subject over the period of time, e.g. 1440 ml over 24 hours.
        self.maxVolumeToDeliver = None
        # reference to Quantity: Quantity

        # free text formula administration, feeding instructions or additional
        # instructions or information.
        self.administrationInstruction = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'caloricDensity'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'maxVolumeToDeliver'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'routeofAdministration'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'additiveType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'baseFormulaType'},

            {'parent_entity': 'NutritionOrder_Administration',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'administration'},
        ]


class NutritionOrder_Administration(fhirbase):
    """A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Administration'

    def __init__(self, dict_values=None):
        # the time period and frequency at which the enteral formula should be
        # delivered to the patient.
        self.schedule = None
        # reference to Timing: Timing

        # the volume of formula to provide to the patient per the specified
        # administration schedule.
        self.quantity = None
        # reference to Quantity: Quantity

        # the rate of administration of formula via a feeding pump, e.g. 60 ml per
        # hour, according to the specified schedule.
        self.rateSimpleQuantity = None
        # reference to Quantity: Quantity

        # the rate of administration of formula via a feeding pump, e.g. 60 ml per
        # hour, according to the specified schedule.
        self.rateRatio = None
        # reference to Ratio: Ratio

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Administration',
             'child_variable': 'rateRatio'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Administration',
             'child_variable': 'quantity'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Administration',
             'child_variable': 'schedule'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Administration',
             'child_variable': 'rateSimpleQuantity'},
        ]
