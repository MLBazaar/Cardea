from .fhirbase import fhirbase


class FamilyMemberHistory(fhirbase):
    """
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """

    __name__ = 'FamilyMemberHistory'

    def __init__(self, dict_values=None):
        self.resourceType = 'FamilyMemberHistory'
        """
        This is a FamilyMemberHistory resource

        type: string
        possible values: FamilyMemberHistory
        """

        self.definition = None
        """
        A protocol or questionnaire that was adhered to in whole or in part by
        this event.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        A code specifying the status of the record of the family history of a
        specific family member.

        type: string
        possible values: partial, completed, entered-in-error,
        health-unknown
        """

        self.notDone = None
        """
        If true, indicates the taking of an individual family member's history
        did not occur. The notDone element should not be used to document
        negated conditions, such as a family member that did not have a
        condition.

        type: boolean
        """

        self.notDoneReason = None
        """
        Describes why the family member's history is absent.

        reference to CodeableConcept
        """

        self.patient = None
        """
        The person who this history concerns.

        reference to Reference: identifier
        """

        self.date = None
        """
        The date (and possibly time) when the family member history was taken.

        type: string
        """

        self.name = None
        """
        This will either be a name or a description; e.g. "Aunt Susan", "my
        cousin with the red hair".

        type: string
        """

        self.relationship = None
        """
        The type of relationship this person has to the patient (father,
        mother, brother etc.).

        reference to CodeableConcept
        """

        self.gender = None
        """
        Administrative Gender - the gender that the relative is considered to
        have for administration and record keeping purposes.

        type: string
        possible values: male, female, other, unknown
        """

        self.bornPeriod = None
        """
        The actual or approximate date of birth of the relative.

        reference to Period
        """

        self.bornDate = None
        """
        The actual or approximate date of birth of the relative.

        type: string
        """

        self.bornString = None
        """
        The actual or approximate date of birth of the relative.

        type: string
        """

        self.ageAge = None
        """
        The age of the relative at the time the family member history is
        recorded.

        reference to Age
        """

        self.ageRange = None
        """
        The age of the relative at the time the family member history is
        recorded.

        reference to Range
        """

        self.ageString = None
        """
        The age of the relative at the time the family member history is
        recorded.

        type: string
        """

        self.estimatedAge = None
        """
        If true, indicates that the age value specified is an estimated value.

        type: boolean
        """

        self.deceasedBoolean = None
        """
        Deceased flag or the actual or approximate age of the relative at the
        time of death for the family member history record.

        type: boolean
        """

        self.deceasedAge = None
        """
        Deceased flag or the actual or approximate age of the relative at the
        time of death for the family member history record.

        reference to Age
        """

        self.deceasedRange = None
        """
        Deceased flag or the actual or approximate age of the relative at the
        time of death for the family member history record.

        reference to Range
        """

        self.deceasedDate = None
        """
        Deceased flag or the actual or approximate age of the relative at the
        time of death for the family member history record.

        type: string
        """

        self.deceasedString = None
        """
        Deceased flag or the actual or approximate age of the relative at the
        time of death for the family member history record.

        type: string
        """

        self.reasonCode = None
        """
        Describes why the family member history occurred in coded or textual
        form.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Indicates a Condition, Observation, AllergyIntolerance, or
        QuestionnaireResponse that justifies this family member history event.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        This property allows a non condition-specific note to the made about
        the related person. Ideally, the note would be in the condition
        property, but this is not always possible.

        type: array
        reference to Annotation
        """

        self.condition = None
        """
        The significant Conditions (or condition) that the family member had.
        This is a repeating section to allow a system to represent more than
        one condition per resource, though there is nothing stopping multiple
        resources - one per condition.

        type: array
        reference to FamilyMemberHistory_Condition
        """

        self.identifier = None
        """
        This records identifiers associated with this family member history
        record that are defined by business processes and/ or used to refer to
        it when a direct URL reference to the resource itself is not
        appropriate (e.g. in CDA documents, or in written / printed
        documentation).

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'bornPeriod'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'note'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'ageAge'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'deceasedRange'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'patient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'relationship'},

            {'parent_entity': 'FamilyMemberHistory_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'condition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'definition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'notDoneReason'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'ageRange'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'deceasedAge'},
        ]


class FamilyMemberHistory_Condition(fhirbase):
    """
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """

    __name__ = 'FamilyMemberHistory_Condition'

    def __init__(self, dict_values=None):
        self.code = None
        """
        The actual condition specified. Could be a coded condition (like MI or
        Diabetes) or a less specific string like 'cancer' depending on how
        much is known about the condition and the capabilities of the creating
        system.

        reference to CodeableConcept
        """

        self.outcome = None
        """
        Indicates what happened as a result of this condition.  If the
        condition resulted in death, deceased date is captured on the
        relation.

        reference to CodeableConcept
        """

        self.onsetAge = None
        """
        Either the age of onset, range of approximate age or descriptive
        string can be recorded.  For conditions with multiple occurrences,
        this describes the first known occurrence.

        reference to Age
        """

        self.onsetRange = None
        """
        Either the age of onset, range of approximate age or descriptive
        string can be recorded.  For conditions with multiple occurrences,
        this describes the first known occurrence.

        reference to Range
        """

        self.onsetPeriod = None
        """
        Either the age of onset, range of approximate age or descriptive
        string can be recorded.  For conditions with multiple occurrences,
        this describes the first known occurrence.

        reference to Period
        """

        self.onsetString = None
        """
        Either the age of onset, range of approximate age or descriptive
        string can be recorded.  For conditions with multiple occurrences,
        this describes the first known occurrence.

        type: string
        """

        self.note = None
        """
        An area where general notes can be placed about this specific
        condition.

        type: array
        reference to Annotation
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'note'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'onsetRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'onsetPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'code'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'onsetAge'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'outcome'},
        ]
