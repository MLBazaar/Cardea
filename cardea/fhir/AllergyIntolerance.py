from .fhirbase import fhirbase


class AllergyIntolerance(fhirbase):
    """
    Risk of harmful or undesirable, physiological response which is unique
    to an individual and associated with exposure to a substance.

    Args:
        resourceType: This is a AllergyIntolerance resource
        identifier: This records identifiers associated with this
            allergy/intolerance concern that are defined by business processes
            and/or used to refer to it when a direct URL reference to the resource
            itself is not appropriate (e.g. in CDA documents, or in written /
            printed documentation).
        clinicalStatus: The clinical status of the allergy or intolerance.
        verificationStatus: Assertion about certainty associated with the
            propensity, or potential risk, of a reaction to the identified
            substance (including pharmaceutical product).
        type: Identification of the underlying physiological mechanism for the
            reaction risk.
        category: Category of the identified substance.
        criticality: Estimate of the potential clinical harm, or seriousness,
            of the reaction to the identified substance.
        code: Code for an allergy or intolerance statement (either a positive
            or a negated/excluded statement).  This may be a code for a substance
            or pharmaceutical product that is considered to be responsible for the
            adverse reaction risk (e.g., "Latex"), an allergy or intolerance
            condition (e.g., "Latex allergy"), or a negated/excluded code for a
            specific substance or class (e.g., "No latex allergy") or a general or
            categorical negated statement (e.g.,  "No known allergy", "No known
            drug allergies").
        patient: The patient who has the allergy or intolerance.
        onsetDateTime: Estimated or actual date,  date-time, or age when
            allergy or intolerance was identified.
        onsetAge: Estimated or actual date,  date-time, or age when allergy or
            intolerance was identified.
        onsetPeriod: Estimated or actual date,  date-time, or age when allergy
            or intolerance was identified.
        onsetRange: Estimated or actual date,  date-time, or age when allergy
            or intolerance was identified.
        onsetString: Estimated or actual date,  date-time, or age when allergy
            or intolerance was identified.
        assertedDate: The date on which the existance of the
            AllergyIntolerance was first asserted or acknowledged.
        recorder: Individual who recorded the record and takes responsibility
            for its content.
        asserter: The source of the information about the allergy that is
            recorded.
        lastOccurrence: Represents the date and/or time of the last known
            occurrence of a reaction event.
        note: Additional narrative about the propensity for the Adverse
            Reaction, not captured in other fields.
        reaction: Details about each adverse reaction event linked to exposure
            to the identified substance.
    """

    __name__ = 'AllergyIntolerance'

    def __init__(self, dict_values=None):
        self.resourceType = 'AllergyIntolerance'
        # type: str
        # possible values: AllergyIntolerance

        self.clinicalStatus = None
        # type: str
        # possible values: active, inactive, resolved

        self.verificationStatus = None
        # type: str
        # possible values: unconfirmed, confirmed, refuted,
        # entered-in-error

        self.type = None
        # type: str
        # possible values: allergy, intolerance

        self.category = None
        # type: list
        # possible values: food, medication, environment, biologic

        self.criticality = None
        # type: str
        # possible values: low, high, unable-to-assess

        self.code = None
        # reference to CodeableConcept

        self.patient = None
        # reference to Reference: identifier

        self.onsetDateTime = None
        # type: str

        self.onsetAge = None
        # reference to Age

        self.onsetPeriod = None
        # reference to Period

        self.onsetRange = None
        # reference to Range

        self.onsetString = None
        # type: str

        self.assertedDate = None
        # type: str

        self.recorder = None
        # reference to Reference: identifier

        self.asserter = None
        # reference to Reference: identifier

        self.lastOccurrence = None
        # type: str

        self.note = None
        # type: list
        # reference to Annotation

        self.reaction = None
        # type: list
        # reference to AllergyIntolerance_Reaction

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.clinicalStatus is not None:
            for value in self.clinicalStatus:
                if value is not None and value.lower() not in [
                        'active', 'inactive', 'resolved']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, resolved'))

        if self.verificationStatus is not None:
            for value in self.verificationStatus:
                if value is not None and value.lower() not in [
                        'unconfirmed', 'confirmed', 'refuted', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'unconfirmed, confirmed, refuted, entered-in-error'))

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'allergy', 'intolerance']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'allergy, intolerance'))

        if self.category is not None:
            for value in self.category:
                if value is not None and value.lower() not in [
                        'food', 'medication', 'environment', 'biologic']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'food, medication, environment, biologic'))

        if self.criticality is not None:
            for value in self.criticality:
                if value is not None and value.lower() not in [
                        'low', 'high', 'unable-to-assess']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'low, high, unable-to-assess'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'onsetAge'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'recorder'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'patient'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'onsetRange'},

            {'parent_entity': 'AllergyIntolerance_Reaction',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'reaction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'asserter'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'code'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'onsetPeriod'},
        ]


class AllergyIntolerance_Reaction(fhirbase):
    """
    Risk of harmful or undesirable, physiological response which is unique
    to an individual and associated with exposure to a substance.

    Args:
        substance: Identification of the specific substance (or pharmaceutical
            product) considered to be responsible for the Adverse Reaction event.
            Note: the substance for a specific reaction may be different from the
            substance identified as the cause of the risk, but it must be
            consistent with it. For instance, it may be a more specific substance
            (e.g. a brand medication) or a composite product that includes the
            identified substance. It must be clinically safe to only process the
            'code' and ignore the 'reaction.substance'.
        manifestation: Clinical symptoms and/or signs that are observed or
            associated with the adverse reaction event.
        description: Text description about the reaction as a whole, including
            details of the manifestation if required.
        onset: Record of the date and/or time of the onset of the Reaction.
        severity: Clinical assessment of the severity of the reaction event as
            a whole, potentially considering multiple different manifestations.
        exposureRoute: Identification of the route by which the subject was
            exposed to the substance.
        note: Additional text about the adverse reaction event not captured in
            other fields.
    """

    __name__ = 'AllergyIntolerance_Reaction'

    def __init__(self, dict_values=None):
        self.substance = None
        # reference to CodeableConcept

        self.manifestation = None
        # type: list
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.onset = None
        # type: str

        self.severity = None
        # type: str
        # possible values: mild, moderate, severe

        self.exposureRoute = None
        # reference to CodeableConcept

        self.note = None
        # type: list
        # reference to Annotation

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.severity is not None:
            for value in self.severity:
                if value is not None and value.lower() not in [
                        'mild', 'moderate', 'severe']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'mild, moderate, severe'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance_Reaction',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance_Reaction',
             'child_variable': 'substance'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance_Reaction',
             'child_variable': 'exposureRoute'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance_Reaction',
             'child_variable': 'manifestation'},
        ]
