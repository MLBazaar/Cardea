from .fhirbase import fhirbase


class Dosage(fhirbase):
    """Indicates how the medication is/was taken or should be taken by the
    patient.
    """

    __name__ = 'Dosage'

    def __init__(self, dict_values=None):
        # indicates the order in which the dosage instructions should be applied
        # or interpreted.
        self.sequence = None
        # type = int

        # free text dosage instructions e.g. sig.
        self.text = None
        # type = string

        # supplemental instruction - e.g. "with meals".
        self.additionalInstruction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # instructions in terms that are understood by the patient or consumer.
        self.patientInstruction = None
        # type = string

        # when medication should be administered.
        self.timing = None
        # reference to Timing: Timing

        # indicates whether the medication is only taken when needed within a
        # specific dosing schedule (boolean option), or it indicates the
        # precondition for taking the medication (codeableconcept).
        self.asNeededBoolean = None
        # type = boolean

        # indicates whether the medication is only taken when needed within a
        # specific dosing schedule (boolean option), or it indicates the
        # precondition for taking the medication (codeableconcept).
        self.asNeededCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # body site to administer to.
        self.site = None
        # reference to CodeableConcept: CodeableConcept

        # how drug should enter body.
        self.route = None
        # reference to CodeableConcept: CodeableConcept

        # technique for administering medication.
        self.method = None
        # reference to CodeableConcept: CodeableConcept

        # amount of medication per dose.
        self.doseRange = None
        # reference to Range: Range

        # amount of medication per dose.
        self.doseSimpleQuantity = None
        # reference to Quantity: Quantity

        # upper limit on medication per unit of time.
        self.maxDosePerPeriod = None
        # reference to Ratio: Ratio

        # upper limit on medication per administration.
        self.maxDosePerAdministration = None
        # reference to Quantity: Quantity

        # upper limit on medication per lifetime of the patient.
        self.maxDosePerLifetime = None
        # reference to Quantity: Quantity

        # amount of medication per unit of time.
        self.rateRatio = None
        # reference to Ratio: Ratio

        # amount of medication per unit of time.
        self.rateRange = None
        # reference to Range: Range

        # amount of medication per unit of time.
        self.rateSimpleQuantity = None
        # reference to Quantity: Quantity

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'timing'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'asNeededCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'additionalInstruction'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'doseRange'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateSimpleQuantity'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateRatio'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerLifetime'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'route'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'doseSimpleQuantity'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateRange'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'site'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'method'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerAdministration'},
        ]
