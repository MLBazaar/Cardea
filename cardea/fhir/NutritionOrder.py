from .fhirbase import fhirbase


class NutritionOrder(fhirbase):
    """
    A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder'

    def __init__(self, dict_values=None):
        self.resourceType = 'NutritionOrder'
        """
        This is a NutritionOrder resource

        type: string
        possible values: NutritionOrder
        """

        self.status = None
        """
        The workflow status of the nutrition order/request.

        type: string
        possible values: proposed, draft, planned, requested, active,
        on-hold, completed, cancelled, entered-in-error
        """

        self.patient = None
        """
        The person (patient) who needs the nutrition order for an oral diet,
        nutritional supplement and/or enteral or formula feeding.

        reference to Reference: identifier
        """

        self.encounter = None
        """
        An encounter that provides additional information about the healthcare
        context in which this request is made.

        reference to Reference: identifier
        """

        self.dateTime = None
        """
        The date and time that this nutrition order was requested.

        type: string
        """

        self.orderer = None
        """
        The practitioner that holds legal responsibility for ordering the
        diet, nutritional supplement, or formula feedings.

        reference to Reference: identifier
        """

        self.allergyIntolerance = None
        """
        A link to a record of allergies or intolerances  which should be
        included in the nutrition order.

        type: array
        reference to Reference: identifier
        """

        self.foodPreferenceModifier = None
        """
        This modifier is used to convey order-specific modifiers about the
        type of food that should be given. These can be derived from patient
        allergies, intolerances, or preferences such as Halal, Vegan or
        Kosher. This modifier applies to the entire nutrition order inclusive
        of the oral diet, nutritional supplements and enteral formula
        feedings.

        type: array
        reference to CodeableConcept
        """

        self.excludeFoodModifier = None
        """
        This modifier is used to convey order-specific modifiers about the
        type of food that should NOT be given. These can be derived from
        patient allergies, intolerances, or preferences such as No Red Meat,
        No Soy or No Wheat or  Gluten-Free.  While it should not be necessary
        to repeat allergy or intolerance information captured in the
        referenced AllergyIntolerance resource in the excludeFoodModifier,
        this element may be used to convey additional specificity related to
        foods that should be eliminated from the patient’s diet for any
        reason.  This modifier applies to the entire nutrition order inclusive
        of the oral diet, nutritional supplements and enteral formula
        feedings.

        type: array
        reference to CodeableConcept
        """

        self.oralDiet = None
        """
        Diet given orally in contrast to enteral (tube) feeding.

        reference to NutritionOrder_OralDiet
        """

        self.supplement = None
        """
        Oral nutritional products given in order to add further nutritional
        value to the patient's diet.

        type: array
        reference to NutritionOrder_Supplement
        """

        self.enteralFormula = None
        """
        Feeding provided through the gastrointestinal tract via a tube,
        catheter, or stoma that delivers nutrition distal to the oral cavity.

        reference to NutritionOrder_EnteralFormula
        """

        self.identifier = None
        """
        Identifiers assigned to this order by the order sender or by the order
        receiver.

        type: array
        reference to Identifier
        """

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
            {'parent_entity': 'NutritionOrder_Supplement',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'supplement'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'encounter'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'excludeFoodModifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'allergyIntolerance'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NutritionOrder',
             'child_variable': 'orderer'},

            {'parent_entity': 'NutritionOrder_EnteralFormula',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'enteralFormula'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'foodPreferenceModifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'identifier'},

            {'parent_entity': 'NutritionOrder_OralDiet',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder',
             'child_variable': 'oralDiet'},
        ]


class NutritionOrder_OralDiet(fhirbase):
    """
    A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_OralDiet'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The kind of diet or dietary restriction such as fiber restricted diet
        or diabetic diet.

        type: array
        reference to CodeableConcept
        """

        self.schedule = None
        """
        The time period and frequency at which the diet should be given.  The
        diet should be given for the combination of all schedules if more than
        one schedule is present.

        type: array
        reference to Timing
        """

        self.nutrient = None
        """
        Class that defines the quantity and type of nutrient modifications
        (for example carbohydrate, fiber or sodium) required for the oral
        diet.

        type: array
        reference to NutritionOrder_Nutrient
        """

        self.texture = None
        """
        Class that describes any texture modifications required for the
        patient to safely consume various types of solid foods.

        type: array
        reference to NutritionOrder_Texture
        """

        self.fluidConsistencyType = None
        """
        The required consistency (e.g. honey-thick, nectar-thick, thin,
        thickened.) of liquids or fluids served to the patient.

        type: array
        reference to CodeableConcept
        """

        self.instruction = None
        """
        Free text or additional instructions or information pertaining to the
        oral diet.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'NutritionOrder_Nutrient',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'nutrient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'type'},

            {'parent_entity': 'NutritionOrder_Texture',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'texture'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'fluidConsistencyType'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_OralDiet',
             'child_variable': 'schedule'},
        ]


class NutritionOrder_Nutrient(fhirbase):
    """
    A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Nutrient'

    def __init__(self, dict_values=None):
        self.modifier = None
        """
        The nutrient that is being modified such as carbohydrate or sodium.

        reference to CodeableConcept
        """

        self.amount = None
        """
        The quantity of the specified nutrient to include in diet.

        reference to Quantity
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Nutrient',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Nutrient',
             'child_variable': 'modifier'},
        ]


class NutritionOrder_Texture(fhirbase):
    """
    A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Texture'

    def __init__(self, dict_values=None):
        self.modifier = None
        """
        Any texture modifications (for solid foods) that should be made, e.g.
        easy to chew, chopped, ground, and pureed.

        reference to CodeableConcept
        """

        self.foodType = None
        """
        The food type(s) (e.g. meats, all foods)  that the texture
        modification applies to.  This could be all foods types.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Texture',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Texture',
             'child_variable': 'foodType'},
        ]


class NutritionOrder_Supplement(fhirbase):
    """
    A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Supplement'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The kind of nutritional supplement product required such as a high
        protein or pediatric clear liquid supplement.

        reference to CodeableConcept
        """

        self.productName = None
        """
        The product or brand name of the nutritional supplement such as "Acme
        Protein Shake".

        type: string
        """

        self.schedule = None
        """
        The time period and frequency at which the supplement(s) should be
        given.  The supplement should be given for the combination of all
        schedules if more than one schedule is present.

        type: array
        reference to Timing
        """

        self.quantity = None
        """
        The amount of the nutritional supplement to be given.

        reference to Quantity
        """

        self.instruction = None
        """
        Free text or additional instructions or information pertaining to the
        oral supplement.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Supplement',
             'child_variable': 'type'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Supplement',
             'child_variable': 'schedule'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Supplement',
             'child_variable': 'quantity'},
        ]


class NutritionOrder_EnteralFormula(fhirbase):
    """
    A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_EnteralFormula'

    def __init__(self, dict_values=None):
        self.baseFormulaType = None
        """
        The type of enteral or infant formula such as an adult standard
        formula with fiber or a soy-based infant formula.

        reference to CodeableConcept
        """

        self.baseFormulaProductName = None
        """
        The product or brand name of the enteral or infant formula product
        such as "ACME Adult Standard Formula".

        type: string
        """

        self.additiveType = None
        """
        Indicates the type of modular component such as protein, carbohydrate,
        fat or fiber to be provided in addition to or mixed with the base
        formula.

        reference to CodeableConcept
        """

        self.additiveProductName = None
        """
        The product or brand name of the type of modular component to be added
        to the formula.

        type: string
        """

        self.caloricDensity = None
        """
        The amount of energy (calories) that the formula should provide per
        specified volume, typically per mL or fluid oz.  For example, an
        infant may require a formula that provides 24 calories per fluid ounce
        or an adult may require an enteral formula that provides 1.5
        calorie/mL.

        reference to Quantity
        """

        self.routeofAdministration = None
        """
        The route or physiological path of administration into the patient's
        gastrointestinal  tract for purposes of providing the formula feeding,
        e.g. nasogastric tube.

        reference to CodeableConcept
        """

        self.administration = None
        """
        Formula administration instructions as structured data.  This
        repeating structure allows for changing the administration rate or
        volume over time for both bolus and continuous feeding.  An example of
        this would be an instruction to increase the rate of continuous
        feeding every 2 hours.

        type: array
        reference to NutritionOrder_Administration
        """

        self.maxVolumeToDeliver = None
        """
        The maximum total quantity of formula that may be administered to a
        subject over the period of time, e.g. 1440 mL over 24 hours.

        reference to Quantity
        """

        self.administrationInstruction = None
        """
        Free text formula administration, feeding instructions or additional
        instructions or information.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'caloricDensity'},

            {'parent_entity': 'NutritionOrder_Administration',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'administration'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'maxVolumeToDeliver'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'baseFormulaType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'additiveType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_EnteralFormula',
             'child_variable': 'routeofAdministration'},
        ]


class NutritionOrder_Administration(fhirbase):
    """
    A request to supply a diet, formula feeding (enteral) or oral
    nutritional supplement to a patient/resident.
    """

    __name__ = 'NutritionOrder_Administration'

    def __init__(self, dict_values=None):
        self.schedule = None
        """
        The time period and frequency at which the enteral formula should be
        delivered to the patient.

        reference to Timing
        """

        self.quantity = None
        """
        The volume of formula to provide to the patient per the specified
        administration schedule.

        reference to Quantity
        """

        self.rateSimpleQuantity = None
        """
        The rate of administration of formula via a feeding pump, e.g. 60 mL
        per hour, according to the specified schedule.

        reference to Quantity
        """

        self.rateRatio = None
        """
        The rate of administration of formula via a feeding pump, e.g. 60 mL
        per hour, according to the specified schedule.

        reference to Ratio
        """

        self.object_id = None
        # unique identifier for object class

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
             'child_variable': 'rateSimpleQuantity'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Administration',
             'child_variable': 'schedule'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'NutritionOrder_Administration',
             'child_variable': 'quantity'},
        ]
