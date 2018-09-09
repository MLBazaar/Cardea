from .fhirbase import fhirbase


class MedicationStatement(fhirbase):
    """A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now, or has taken the medication in the past or will be
    taking the medication in the future.  The source of this information can
    be the patient, significant other (such as a family member or spouse),
    or a clinician.  A common scenario where this information is captured is
    during the history taking process during a patient visit or stay.   The
    medication information may come from sources such as the patient's
    memory, from a prescription bottle,  or from a list of medications the
    patient, clinician or other party maintains   The primary difference
    between a medication statement and a medication administration is that
    the medication administration has complete administration information
    and is based on actual administration information from the person who
    administered the medication.  A medication statement is often, if not
    always, less specific.  There is no required date/time when the
    medication was administered, in fact we only know that a source has
    reported the patient is taking this medication, where details such as
    time, quantity, or rate or even medication product may be incomplete or
    missing or less precise.  As stated earlier, the medication statement
    information may come from the patient's memory, from a prescription
    bottle or from a list of medications the patient, clinician or other
    party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """

    def __init__(self, dict_values=None):
        # this is a medicationstatement resource
        self.resourceType = 'MedicationStatement'
        # type = string
        # possible values: MedicationStatement

        # a plan, proposal or order that is fulfilled in whole or in part by this
        # event.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # a larger event of which this particular event is a component or step.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # the encounter or episode of care that establishes the context for this
        # medicationstatement.
        self.context = None
        # reference to Reference: identifier

        # a code representing the patient or other source's judgment about the
        # state of the medication used that this statement is about.  generally
        # this will be active or completed.
        self.status = None
        # type = string
        # possible values: active, completed, entered-in-error,
        # intended, stopped, on-hold

        # indicates where type of medication statement and where the medication is
        # expected to be consumed or administered.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the medication being administered. this is either a link to a
        # resource representing the details of the medication or a simple
        # attribute carrying a code that identifies the medication from a known
        # list of medications.
        self.medicationCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the medication being administered. this is either a link to a
        # resource representing the details of the medication or a simple
        # attribute carrying a code that identifies the medication from a known
        # list of medications.
        self.medicationReference = None
        # reference to Reference: identifier

        # the interval of time during which it is being asserted that the patient
        # was taking the medication (or was not taking, when the wasnotgiven
        # element is true).
        self.effectiveDateTime = None
        # type = string

        # the interval of time during which it is being asserted that the patient
        # was taking the medication (or was not taking, when the wasnotgiven
        # element is true).
        self.effectivePeriod = None
        # reference to Period: Period

        # the date when the medication statement was asserted by the information
        # source.
        self.dateAsserted = None
        # type = string

        # the person or organization that provided the information about the
        # taking of this medication. note: use derivedfrom when a
        # medicationstatement is derived from other resources, e.g claim or
        # medicationrequest.
        self.informationSource = None
        # reference to Reference: identifier

        # the person, animal or group who is/was taking the medication.
        self.subject = None
        # reference to Reference: identifier

        # allows linking the medicationstatement to the underlying
        # medicationrequest, or to other information that supports or is used to
        # derive the medicationstatement.
        self.derivedFrom = None
        # type = array
        # reference to Reference: identifier

        # indicator of the certainty of whether the medication was taken by the
        # patient.
        self.taken = None
        # type = string
        # possible values: y, n, unk, na

        # a code indicating why the medication was not taken.
        self.reasonNotTaken = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a reason for why the medication is being/was taken.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # condition or observation that supports why the medication is being/was
        # taken.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # provides extra information about the medication statement that is not
        # conveyed by the other attributes.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # indicates how the medication is/was or should be taken by the patient.
        self.dosage = None
        # type = array
        # reference to Dosage: Dosage

        # external identifier - fhir will generate its own internal identifiers
        # (probably urls) which do not need to be explicitly managed by the
        # resource.  the identifier here is one that would be used by another non-
        # fhir system - for example an automated medication pump would provide a
        # record each time it operated; an administration while the patient was
        # off the ward might be made with a different system and entered after the
        # event.  particularly important if these records have to be updated.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'completed', 'entered-in-error', 'intended', 'stopped',
                        'on-hold']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, completed, entered-in-error, intended, stopped, on-hold'))

        if self.taken is not None:
            for value in self.taken:
                if value is not None and value.lower() not in [
                        'y', 'n', 'unk', 'na']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'y, n, unk, na'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'context'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'dosage'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'informationSource'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'reasonNotTaken'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'medicationReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'derivedFrom'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'effectivePeriod'},
        ]
