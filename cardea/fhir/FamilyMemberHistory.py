from .fhirbase import fhirbase


class FamilyMemberHistory(fhirbase):
    """
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.

    Args:
        resourceType: This is a FamilyMemberHistory resource
        identifier: This records identifiers associated with this family
            member history record that are defined by business processes and/ or
            used to refer to it when a direct URL reference to the resource itself
            is not appropriate (e.g. in CDA documents, or in written / printed
            documentation).
        definition: A protocol or questionnaire that was adhered to in whole
            or in part by this event.
        status: A code specifying the status of the record of the family
            history of a specific family member.
        notDone: If true, indicates the taking of an individual family
            member's history did not occur. The notDone element should not be used
            to document negated conditions, such as a family member that did not
            have a condition.
        notDoneReason: Describes why the family member's history is absent.
        patient: The person who this history concerns.
        date: The date (and possibly time) when the family member history was
            taken.
        name: This will either be a name or a description; e.g. "Aunt Susan",
            "my cousin with the red hair".
        relationship: The type of relationship this person has to the patient
            (father, mother, brother etc.).
        gender: Administrative Gender - the gender that the relative is
            considered to have for administration and record keeping purposes.
        bornPeriod: The actual or approximate date of birth of the relative.
        bornDate: The actual or approximate date of birth of the relative.
        bornString: The actual or approximate date of birth of the relative.
        ageAge: The age of the relative at the time the family member history
            is recorded.
        ageRange: The age of the relative at the time the family member
            history is recorded.
        ageString: The age of the relative at the time the family member
            history is recorded.
        estimatedAge: If true, indicates that the age value specified is an
            estimated value.
        deceasedBoolean: Deceased flag or the actual or approximate age of the
            relative at the time of death for the family member history record.
        deceasedAge: Deceased flag or the actual or approximate age of the
            relative at the time of death for the family member history record.
        deceasedRange: Deceased flag or the actual or approximate age of the
            relative at the time of death for the family member history record.
        deceasedDate: Deceased flag or the actual or approximate age of the
            relative at the time of death for the family member history record.
        deceasedString: Deceased flag or the actual or approximate age of the
            relative at the time of death for the family member history record.
        reasonCode: Describes why the family member history occurred in coded
            or textual form.
        reasonReference: Indicates a Condition, Observation,
            AllergyIntolerance, or QuestionnaireResponse that justifies this
            family member history event.
        note: This property allows a non condition-specific note to the made
            about the related person. Ideally, the note would be in the condition
            property, but this is not always possible.
        condition: The significant Conditions (or condition) that the family
            member had. This is a repeating section to allow a system to represent
            more than one condition per resource, though there is nothing stopping
            multiple resources - one per condition.
    """

    __name__ = 'FamilyMemberHistory'

    def __init__(self, dict_values=None):
        self.resourceType = 'FamilyMemberHistory'
        # type: str
        # possible values: FamilyMemberHistory

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: partial, completed, entered-in-error,
        # health-unknown

        self.notDone = None
        # type: bool

        self.notDoneReason = None
        # reference to CodeableConcept

        self.patient = None
        # reference to Reference: identifier

        self.date = None
        # type: str

        self.name = None
        # type: str

        self.relationship = None
        # reference to CodeableConcept

        self.gender = None
        # type: str
        # possible values: male, female, other, unknown

        self.bornPeriod = None
        # reference to Period

        self.bornDate = None
        # type: str

        self.bornString = None
        # type: str

        self.ageAge = None
        # reference to Age

        self.ageRange = None
        # reference to Range

        self.ageString = None
        # type: str

        self.estimatedAge = None
        # type: bool

        self.deceasedBoolean = None
        # type: bool

        self.deceasedAge = None
        # reference to Age

        self.deceasedRange = None
        # reference to Range

        self.deceasedDate = None
        # type: str

        self.deceasedString = None
        # type: str

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.condition = None
        # type: list
        # reference to FamilyMemberHistory_Condition

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'partial', 'completed', 'entered-in-error', 'health-unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'partial, completed, entered-in-error, health-unknown'))

        if self.gender is not None:
            for value in self.gender:
                if value is not None and value.lower() not in [
                        'male', 'female', 'other', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'male, female, other, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'note'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'deceasedAge'},

            {'parent_entity': 'FamilyMemberHistory_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'condition'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'deceasedRange'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'definition'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'ageAge'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'relationship'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'patient'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'ageRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'bornPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'notDoneReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'reasonCode'},
        ]


class FamilyMemberHistory_Condition(fhirbase):
    """
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.

    Args:
        code: The actual condition specified. Could be a coded condition (like
            MI or Diabetes) or a less specific string like 'cancer' depending on
            how much is known about the condition and the capabilities of the
            creating system.
        outcome: Indicates what happened as a result of this condition.  If
            the condition resulted in death, deceased date is captured on the
            relation.
        onsetAge: Either the age of onset, range of approximate age or
            descriptive string can be recorded.  For conditions with multiple
            occurrences, this describes the first known occurrence.
        onsetRange: Either the age of onset, range of approximate age or
            descriptive string can be recorded.  For conditions with multiple
            occurrences, this describes the first known occurrence.
        onsetPeriod: Either the age of onset, range of approximate age or
            descriptive string can be recorded.  For conditions with multiple
            occurrences, this describes the first known occurrence.
        onsetString: Either the age of onset, range of approximate age or
            descriptive string can be recorded.  For conditions with multiple
            occurrences, this describes the first known occurrence.
        note: An area where general notes can be placed about this specific
            condition.
    """

    __name__ = 'FamilyMemberHistory_Condition'

    def __init__(self, dict_values=None):
        self.code = None
        # reference to CodeableConcept

        self.outcome = None
        # reference to CodeableConcept

        self.onsetAge = None
        # reference to Age

        self.onsetRange = None
        # reference to Range

        self.onsetPeriod = None
        # reference to Period

        self.onsetString = None
        # type: str

        self.note = None
        # type: list
        # reference to Annotation

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'onsetAge'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'outcome'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'onsetPeriod'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'code'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'onsetRange'},
        ]
