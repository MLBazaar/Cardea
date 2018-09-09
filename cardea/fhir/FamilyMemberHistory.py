from .fhirbase import fhirbase


class FamilyMemberHistory(fhirbase):
    """Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """

    def __init__(self, dict_values=None):
        # this is a familymemberhistory resource
        self.resourceType = 'FamilyMemberHistory'
        # type = string
        # possible values: FamilyMemberHistory

        # a protocol or questionnaire that was adhered to in whole or in part by
        # this event.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # a code specifying the status of the record of the family history of a
        # specific family member.
        self.status = None
        # type = string
        # possible values: partial, completed, entered-in-error, health-
        # unknown

        # if true, indicates the taking of an individual family member's history
        # did not occur. the notdone element should not be used to document
        # negated conditions, such as a family member that did not have a
        # condition.
        self.notDone = None
        # type = boolean

        # describes why the family member's history is absent.
        self.notDoneReason = None
        # reference to CodeableConcept: CodeableConcept

        # the person who this history concerns.
        self.patient = None
        # reference to Reference: identifier

        # the date (and possibly time) when the family member history was taken.
        self.date = None
        # type = string

        # this will either be a name or a description; e.g. "aunt susan", "my
        # cousin with the red hair".
        self.name = None
        # type = string

        # the type of relationship this person has to the patient (father, mother,
        # brother etc.).
        self.relationship = None
        # reference to CodeableConcept: CodeableConcept

        # administrative gender - the gender that the relative is considered to
        # have for administration and record keeping purposes.
        self.gender = None
        # type = string
        # possible values: male, female, other, unknown

        # the actual or approximate date of birth of the relative.
        self.bornPeriod = None
        # reference to Period: Period

        # the actual or approximate date of birth of the relative.
        self.bornDate = None
        # type = string

        # the actual or approximate date of birth of the relative.
        self.bornString = None
        # type = string

        # the age of the relative at the time the family member history is
        # recorded.
        self.ageAge = None
        # reference to Age: Age

        # the age of the relative at the time the family member history is
        # recorded.
        self.ageRange = None
        # reference to Range: Range

        # the age of the relative at the time the family member history is
        # recorded.
        self.ageString = None
        # type = string

        # if true, indicates that the age value specified is an estimated value.
        self.estimatedAge = None
        # type = boolean

        # deceased flag or the actual or approximate age of the relative at the
        # time of death for the family member history record.
        self.deceasedBoolean = None
        # type = boolean

        # deceased flag or the actual or approximate age of the relative at the
        # time of death for the family member history record.
        self.deceasedAge = None
        # reference to Age: Age

        # deceased flag or the actual or approximate age of the relative at the
        # time of death for the family member history record.
        self.deceasedRange = None
        # reference to Range: Range

        # deceased flag or the actual or approximate age of the relative at the
        # time of death for the family member history record.
        self.deceasedDate = None
        # type = string

        # deceased flag or the actual or approximate age of the relative at the
        # time of death for the family member history record.
        self.deceasedString = None
        # type = string

        # describes why the family member history occurred in coded or textual
        # form.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates a condition, observation, allergyintolerance, or
        # questionnaireresponse that justifies this family member history event.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # this property allows a non condition-specific note to the made about the
        # related person. ideally, the note would be in the condition property,
        # but this is not always possible.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # the significant conditions (or condition) that the family member had.
        # this is a repeating section to allow a system to represent more than one
        # condition per resource, though there is nothing stopping multiple
        # resources - one per condition.
        self.condition = None
        # type = array
        # reference to FamilyMemberHistory_Condition: FamilyMemberHistory_Condition

        # this records identifiers associated with this family member history
        # record that are defined by business processes and/ or used to refer to
        # it when a direct url reference to the resource itself is not appropriate
        # (e.g. in cda documents, or in written / printed documentation).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'ageRange'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'bornPeriod'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'note'},

            {'parent_entity': 'FamilyMemberHistory_Condition',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'condition'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'identifier'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'deceasedAge'},

            {'parent_entity': 'Age',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'ageAge'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'notDoneReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'definition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'relationship'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory',
             'child_variable': 'deceasedRange'},
        ]


class FamilyMemberHistory_Condition(fhirbase):
    """Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """

    def __init__(self, dict_values=None):
        # the actual condition specified. could be a coded condition (like mi or
        # diabetes) or a less specific string like 'cancer' depending on how much
        # is known about the condition and the capabilities of the creating
        # system.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # indicates what happened as a result of this condition.  if the condition
        # resulted in death, deceased date is captured on the relation.
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # either the age of onset, range of approximate age or descriptive string
        # can be recorded.  for conditions with multiple occurrences, this
        # describes the first known occurrence.
        self.onsetAge = None
        # reference to Age: Age

        # either the age of onset, range of approximate age or descriptive string
        # can be recorded.  for conditions with multiple occurrences, this
        # describes the first known occurrence.
        self.onsetRange = None
        # reference to Range: Range

        # either the age of onset, range of approximate age or descriptive string
        # can be recorded.  for conditions with multiple occurrences, this
        # describes the first known occurrence.
        self.onsetPeriod = None
        # reference to Period: Period

        # either the age of onset, range of approximate age or descriptive string
        # can be recorded.  for conditions with multiple occurrences, this
        # describes the first known occurrence.
        self.onsetString = None
        # type = string

        # an area where general notes can be placed about this specific condition.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'note'},

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

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'code'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'FamilyMemberHistory_Condition',
             'child_variable': 'onsetRange'},
        ]
