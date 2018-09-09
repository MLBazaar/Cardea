from .fhirbase import fhirbase


class AllergyIntolerance(fhirbase):
    """Risk of harmful or undesirable, physiological response which is unique
    to an individual and associated with exposure to a substance.
    """

    def __init__(self, dict_values=None):
        # this is a allergyintolerance resource
        self.resourceType = 'AllergyIntolerance'
        # type = string
        # possible values: AllergyIntolerance

        # the clinical status of the allergy or intolerance.
        self.clinicalStatus = None
        # type = string
        # possible values: active, inactive, resolved

        # assertion about certainty associated with the propensity, or potential
        # risk, of a reaction to the identified substance (including
        # pharmaceutical product).
        self.verificationStatus = None
        # type = string
        # possible values: unconfirmed, confirmed, refuted, entered-in-
        # error

        # identification of the underlying physiological mechanism for the
        # reaction risk.
        self.type = None
        # type = string
        # possible values: allergy, intolerance

        # category of the identified substance.
        self.category = None
        # type = array
        # possible values: food, medication, environment, biologic

        # estimate of the potential clinical harm, or seriousness, of the reaction
        # to the identified substance.
        self.criticality = None
        # type = string
        # possible values: low, high, unable-to-assess

        # code for an allergy or intolerance statement (either a positive or a
        # negated/excluded statement).  this may be a code for a substance or
        # pharmaceutical product that is considered to be responsible for the
        # adverse reaction risk (e.g., "latex"), an allergy or intolerance
        # condition (e.g., "latex allergy"), or a negated/excluded code for a
        # specific substance or class (e.g., "no latex allergy") or a general or
        # categorical negated statement (e.g.,  "no known allergy", "no known drug
        # allergies").
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the patient who has the allergy or intolerance.
        self.patient = None
        # reference to Reference: identifier

        # estimated or actual date,  date-time, or age when allergy or intolerance
        # was identified.
        self.onsetDateTime = None
        # type = string

        # estimated or actual date,  date-time, or age when allergy or intolerance
        # was identified.
        self.onsetAge = None
        # reference to Age: Age

        # estimated or actual date,  date-time, or age when allergy or intolerance
        # was identified.
        self.onsetPeriod = None
        # reference to Period: Period

        # estimated or actual date,  date-time, or age when allergy or intolerance
        # was identified.
        self.onsetRange = None
        # reference to Range: Range

        # estimated or actual date,  date-time, or age when allergy or intolerance
        # was identified.
        self.onsetString = None
        # type = string

        # the date on which the existance of the allergyintolerance was first
        # asserted or acknowledged.
        self.assertedDate = None
        # type = string

        # individual who recorded the record and takes responsibility for its
        # content.
        self.recorder = None
        # reference to Reference: identifier

        # the source of the information about the allergy that is recorded.
        self.asserter = None
        # reference to Reference: identifier

        # represents the date and/or time of the last known occurrence of a
        # reaction event.
        self.lastOccurrence = None
        # type = string

        # additional narrative about the propensity for the adverse reaction, not
        # captured in other fields.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # details about each adverse reaction event linked to exposure to the
        # identified substance.
        self.reaction = None
        # type = array
        # reference to AllergyIntolerance_Reaction: AllergyIntolerance_Reaction

        # this records identifiers associated with this allergy/intolerance
        # concern that are defined by business processes and/or used to refer to
        # it when a direct url reference to the resource itself is not appropriate
        # (e.g. in cda documents, or in written / printed documentation).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'onsetRange'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'patient'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'asserter'},

            {'parent_entity': 'AllergyIntolerance_Reaction',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'reaction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'recorder'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'onsetPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'code'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'note'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance',
             'child_variable': 'onsetAge'},
        ]


class AllergyIntolerance_Reaction(fhirbase):
    """Risk of harmful or undesirable, physiological response which is unique
    to an individual and associated with exposure to a substance.
    """

    def __init__(self, dict_values=None):
        # identification of the specific substance (or pharmaceutical product)
        # considered to be responsible for the adverse reaction event. note: the
        # substance for a specific reaction may be different from the substance
        # identified as the cause of the risk, but it must be consistent with it.
        # for instance, it may be a more specific substance (e.g. a brand
        # medication) or a composite product that includes the identified
        # substance. it must be clinically safe to only process the 'code' and
        # ignore the 'reaction.substance'.
        self.substance = None
        # reference to CodeableConcept: CodeableConcept

        # clinical symptoms and/or signs that are observed or associated with the
        # adverse reaction event.
        self.manifestation = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # text description about the reaction as a whole, including details of the
        # manifestation if required.
        self.description = None
        # type = string

        # record of the date and/or time of the onset of the reaction.
        self.onset = None
        # type = string

        # clinical assessment of the severity of the reaction event as a whole,
        # potentially considering multiple different manifestations.
        self.severity = None
        # type = string
        # possible values: mild, moderate, severe

        # identification of the route by which the subject was exposed to the
        # substance.
        self.exposureRoute = None
        # reference to CodeableConcept: CodeableConcept

        # additional text about the adverse reaction event not captured in other
        # fields.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'manifestation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance_Reaction',
             'child_variable': 'exposureRoute'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AllergyIntolerance_Reaction',
             'child_variable': 'substance'},
        ]
