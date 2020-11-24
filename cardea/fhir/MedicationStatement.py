from .fhirbase import fhirbase


class MedicationStatement(fhirbase):
    """
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now, or has taken the medication in the past or will be
    taking the medication in the future.  The source of this information
    can be the patient, significant other (such as a family member or
    spouse), or a clinician.  A common scenario where this information is
    captured is during the history taking process during a patient visit
    or stay.   The medication information may come from sources such as
    the patient's memory, from a prescription bottle,  or from a list of
    medications the patient, clinician or other party maintains   The
    primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A
    medication statement is often, if not always, less specific.  There is
    no required date/time when the medication was administered, in fact we
    only know that a source has reported the patient is taking this
    medication, where details such as time, quantity, or rate or even
    medication product may be incomplete or missing or less precise.  As
    stated earlier, the medication statement information may come from the
    patient's memory, from a prescription bottle or from a list of
    medications the patient, clinician or other party maintains.
    Medication administration is more formal and is not missing detailed
    information.

    Args:
        resourceType: This is a MedicationStatement resource
        identifier: External identifier - FHIR will generate its own internal
            identifiers (probably URLs) which do not need to be explicitly managed
            by the resource.  The identifier here is one that would be used by
            another non-FHIR system - for example an automated medication pump
            would provide a record each time it operated; an administration while
            the patient was off the ward might be made with a different system and
            entered after the event.  Particularly important if these records have
            to be updated.
        basedOn: A plan, proposal or order that is fulfilled in whole or in
            part by this event.
        partOf: A larger event of which this particular event is a component
            or step.
        context: The encounter or episode of care that establishes the context
            for this MedicationStatement.
        status: A code representing the patient or other source's judgment
            about the state of the medication used that this statement is about.
            Generally this will be active or completed.
        category: Indicates where type of medication statement and where the
            medication is expected to be consumed or administered.
        medicationCodeableConcept: Identifies the medication being
            administered. This is either a link to a resource representing the
            details of the medication or a simple attribute carrying a code that
            identifies the medication from a known list of medications.
        medicationReference: Identifies the medication being administered.
            This is either a link to a resource representing the details of the
            medication or a simple attribute carrying a code that identifies the
            medication from a known list of medications.
        effectiveDateTime: The interval of time during which it is being
            asserted that the patient was taking the medication (or was not
            taking, when the wasNotGiven element is true).
        effectivePeriod: The interval of time during which it is being
            asserted that the patient was taking the medication (or was not
            taking, when the wasNotGiven element is true).
        dateAsserted: The date when the medication statement was asserted by
            the information source.
        informationSource: The person or organization that provided the
            information about the taking of this medication. Note: Use derivedFrom
            when a MedicationStatement is derived from other resources, e.g Claim
            or MedicationRequest.
        subject: The person, animal or group who is/was taking the medication.
        derivedFrom: Allows linking the MedicationStatement to the underlying
            MedicationRequest, or to other information that supports or is used to
            derive the MedicationStatement.
        taken: Indicator of the certainty of whether the medication was taken
            by the patient.
        reasonNotTaken: A code indicating why the medication was not taken.
        reasonCode: A reason for why the medication is being/was taken.
        reasonReference: Condition or observation that supports why the
            medication is being/was taken.
        note: Provides extra information about the medication statement that
            is not conveyed by the other attributes.
        dosage: Indicates how the medication is/was or should be taken by the
            patient.
    """

    __name__ = 'MedicationStatement'

    def __init__(self, dict_values=None):
        self.resourceType = 'MedicationStatement'
        # type: str
        # possible values: MedicationStatement

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: active, completed, entered-in-error,
        # intended, stopped, on-hold

        self.category = None
        # reference to CodeableConcept

        self.medicationCodeableConcept = None
        # reference to CodeableConcept

        self.medicationReference = None
        # reference to Reference: identifier

        self.effectiveDateTime = None
        # type: str

        self.effectivePeriod = None
        # reference to Period

        self.dateAsserted = None
        # type: str

        self.informationSource = None
        # reference to Reference: identifier

        self.subject = None
        # reference to Reference: identifier

        self.derivedFrom = None
        # type: list
        # reference to Reference: identifier

        self.taken = None
        # type: str
        # possible values: y, n, unk, na

        self.reasonNotTaken = None
        # type: list
        # reference to CodeableConcept

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.dosage = None
        # type: list
        # reference to Dosage

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'derivedFrom'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'medicationReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'context'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'dosage'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'reasonNotTaken'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'informationSource'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'subject'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationStatement',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationStatement',
             'child_variable': 'partOf'},
        ]
