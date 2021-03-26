from .fhirbase import fhirbase


class Dosage(fhirbase):
    """
    Indicates how the medication is/was taken or should be taken by the
    patient.

    Args:
        sequence: Indicates the order in which the dosage instructions should
            be applied or interpreted.
        text: Free text dosage instructions e.g. SIG.
        additionalInstruction: Supplemental instruction - e.g. "with meals".
        patientInstruction: Instructions in terms that are understood by the
            patient or consumer.
        timing: When medication should be administered.
        asNeededBoolean: Indicates whether the Medication is only taken when
            needed within a specific dosing schedule (Boolean option), or it
            indicates the precondition for taking the Medication
            (CodeableConcept).
        asNeededCodeableConcept: Indicates whether the Medication is only
            taken when needed within a specific dosing schedule (Boolean option),
            or it indicates the precondition for taking the Medication
            (CodeableConcept).
        site: Body site to administer to.
        route: How drug should enter body.
        method: Technique for administering medication.
        doseRange: Amount of medication per dose.
        doseSimpleQuantity: Amount of medication per dose.
        maxDosePerPeriod: Upper limit on medication per unit of time.
        maxDosePerAdministration: Upper limit on medication per
            administration.
        maxDosePerLifetime: Upper limit on medication per lifetime of the
            patient.
        rateRatio: Amount of medication per unit of time.
        rateRange: Amount of medication per unit of time.
        rateSimpleQuantity: Amount of medication per unit of time.
    """

    __name__ = 'Dosage'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.text = None
        # type: str

        self.additionalInstruction = None
        # type: list
        # reference to CodeableConcept

        self.patientInstruction = None
        # type: str

        self.timing = None
        # reference to Timing

        self.asNeededBoolean = None
        # type: bool

        self.asNeededCodeableConcept = None
        # reference to CodeableConcept

        self.site = None
        # reference to CodeableConcept

        self.route = None
        # reference to CodeableConcept

        self.method = None
        # reference to CodeableConcept

        self.doseRange = None
        # reference to Range

        self.doseSimpleQuantity = None
        # reference to Quantity

        self.maxDosePerPeriod = None
        # reference to Ratio

        self.maxDosePerAdministration = None
        # reference to Quantity

        self.maxDosePerLifetime = None
        # reference to Quantity

        self.rateRatio = None
        # reference to Ratio

        self.rateRange = None
        # reference to Range

        self.rateSimpleQuantity = None
        # reference to Quantity

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'doseRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'asNeededCodeableConcept'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'site'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateSimpleQuantity'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateRatio'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'timing'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateRange'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'doseSimpleQuantity'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerLifetime'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'method'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerAdministration'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'route'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'additionalInstruction'},
        ]
