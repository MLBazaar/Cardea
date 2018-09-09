from .fhirbase import fhirbase


class Dosage(fhirbase):
    """
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """

    __name__ = 'Dosage'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        Indicates the order in which the dosage instructions should be applied
        or interpreted.

        type: int
        """

        self.text = None
        """
        Free text dosage instructions e.g. SIG.

        type: string
        """

        self.additionalInstruction = None
        """
        Supplemental instruction - e.g. "with meals".

        type: array
        reference to CodeableConcept
        """

        self.patientInstruction = None
        """
        Instructions in terms that are understood by the patient or consumer.

        type: string
        """

        self.timing = None
        """
        When medication should be administered.

        reference to Timing
        """

        self.asNeededBoolean = None
        """
        Indicates whether the Medication is only taken when needed within a
        specific dosing schedule (Boolean option), or it indicates the
        precondition for taking the Medication (CodeableConcept).

        type: boolean
        """

        self.asNeededCodeableConcept = None
        """
        Indicates whether the Medication is only taken when needed within a
        specific dosing schedule (Boolean option), or it indicates the
        precondition for taking the Medication (CodeableConcept).

        reference to CodeableConcept
        """

        self.site = None
        """
        Body site to administer to.

        reference to CodeableConcept
        """

        self.route = None
        """
        How drug should enter body.

        reference to CodeableConcept
        """

        self.method = None
        """
        Technique for administering medication.

        reference to CodeableConcept
        """

        self.doseRange = None
        """
        Amount of medication per dose.

        reference to Range
        """

        self.doseSimpleQuantity = None
        """
        Amount of medication per dose.

        reference to Quantity
        """

        self.maxDosePerPeriod = None
        """
        Upper limit on medication per unit of time.

        reference to Ratio
        """

        self.maxDosePerAdministration = None
        """
        Upper limit on medication per administration.

        reference to Quantity
        """

        self.maxDosePerLifetime = None
        """
        Upper limit on medication per lifetime of the patient.

        reference to Quantity
        """

        self.rateRatio = None
        """
        Amount of medication per unit of time.

        reference to Ratio
        """

        self.rateRange = None
        """
        Amount of medication per unit of time.

        reference to Range
        """

        self.rateSimpleQuantity = None
        """
        Amount of medication per unit of time.

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
             'child_entity': 'Dosage',
             'child_variable': 'rateSimpleQuantity'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'doseSimpleQuantity'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'timing'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'additionalInstruction'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateRange'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerAdministration'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerLifetime'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'maxDosePerPeriod'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'rateRatio'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'site'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'method'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'asNeededCodeableConcept'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'doseRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Dosage',
             'child_variable': 'route'},
        ]
