from .fhirbase import fhirbase


class MedicationDispense(fhirbase):
    """
    Indicates that a medication product is to be or has been dispensed for
    a named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy
    system responding to a medication order.

    Args:
        resourceType: This is a MedicationDispense resource
        identifier: Identifier assigned by the dispensing facility - this is
            an identifier assigned outside FHIR.
        partOf: The procedure that the dispense is done because of.
        status: A code specifying the state of the set of dispense events.
        category: Indicates type of medication dispense and where the
            medication is expected to be consumed or administered.
        medicationCodeableConcept: Identifies the medication being
            administered. This is either a link to a resource representing the
            details of the medication or a simple attribute carrying a code that
            identifies the medication from a known list of medications.
        medicationReference: Identifies the medication being administered.
            This is either a link to a resource representing the details of the
            medication or a simple attribute carrying a code that identifies the
            medication from a known list of medications.
        subject: A link to a resource representing the person or the group to
            whom the medication will be given.
        context: The encounter or episode of care that establishes the context
            for this event.
        supportingInformation: Additional information that supports the
            medication being dispensed.
        performer: Indicates who or what performed the event.  It should be
            assumed that the performer is the dispenser of the medication.
        authorizingPrescription: Indicates the medication order that is being
            dispensed against.
        type: Indicates the type of dispensing event that is performed. For
            example, Trial Fill, Completion of Trial, Partial Fill, Emergency
            Fill, Samples, etc.
        quantity: The amount of medication that has been dispensed. Includes
            unit of measure.
        daysSupply: The amount of medication expressed as a timing amount.
        whenPrepared: The time when the dispensed product was packaged and
            reviewed.
        whenHandedOver: The time the dispensed product was provided to the
            patient or their representative.
        destination: Identification of the facility/location where the
            medication was shipped to, as part of the dispense event.
        receiver: Identifies the person who picked up the medication.  This
            will usually be a patient or their caregiver, but some cases exist
            where it can be a healthcare professional.
        note: Extra information about the dispense that could not be conveyed
            in the other attributes.
        dosageInstruction: Indicates how the medication is to be used by the
            patient.
        substitution: Indicates whether or not substitution was made as part
            of the dispense.  In some cases substitution will be expected but does
            not happen, in other cases substitution is not expected but does
            happen.  This block explains what substitution did or did not happen
            and why.  If nothing is specified, substitution was not done.
        detectedIssue: Indicates an actual or potential clinical issue with or
            between one or more active or proposed clinical actions for a patient;
            e.g. Drug-drug interaction, duplicate therapy, dosage alert etc.
        notDone: True if the dispense was not performed for some reason.
        notDoneReasonCodeableConcept: Indicates the reason why a dispense was
            not performed.
        notDoneReasonReference: Indicates the reason why a dispense was not
            performed.
        eventHistory: A summary of the events of interest that have occurred,
            such as when the dispense was verified.
    """

    __name__ = 'MedicationDispense'

    def __init__(self, dict_values=None):
        self.resourceType = 'MedicationDispense'
        # type: str
        # possible values: MedicationDispense

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: preparation, in-progress, on-hold,
        # completed, entered-in-error, stopped

        self.category = None
        # reference to CodeableConcept

        self.medicationCodeableConcept = None
        # reference to CodeableConcept

        self.medicationReference = None
        # reference to Reference: identifier

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.supportingInformation = None
        # type: list
        # reference to Reference: identifier

        self.performer = None
        # type: list
        # reference to MedicationDispense_Performer

        self.authorizingPrescription = None
        # type: list
        # reference to Reference: identifier

        self.type = None
        # reference to CodeableConcept

        self.quantity = None
        # reference to Quantity

        self.daysSupply = None
        # reference to Quantity

        self.whenPrepared = None
        # type: str

        self.whenHandedOver = None
        # type: str

        self.destination = None
        # reference to Reference: identifier

        self.receiver = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.dosageInstruction = None
        # type: list
        # reference to Dosage

        self.substitution = None
        # reference to MedicationDispense_Substitution

        self.detectedIssue = None
        # type: list
        # reference to Reference: identifier

        self.notDone = None
        # type: bool

        self.notDoneReasonCodeableConcept = None
        # reference to CodeableConcept

        self.notDoneReasonReference = None
        # reference to Reference: identifier

        self.eventHistory = None
        # type: list
        # reference to Reference: identifier

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
                    'preparation', 'in-progress', 'on-hold', 'completed',
                        'entered-in-error', 'stopped']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'preparation, in-progress, on-hold, completed, entered-in-error,'
                        'stopped'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'dosageInstruction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'receiver'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'detectedIssue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'identifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'daysSupply'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'medicationReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'destination'},

            {'parent_entity': 'MedicationDispense_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'performer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'notDoneReasonCodeableConcept'},

            {'parent_entity': 'MedicationDispense_Substitution',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'substitution'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'eventHistory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'authorizingPrescription'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'notDoneReasonReference'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'category'},
        ]


class MedicationDispense_Performer(fhirbase):
    """
    Indicates that a medication product is to be or has been dispensed for
    a named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy
    system responding to a medication order.

    Args:
        actor: The device, practitioner, etc. who performed the action.  It
            should be assumed that the actor is the dispenser of the medication.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'MedicationDispense_Performer'

    def __init__(self, dict_values=None):
        self.actor = None
        # reference to Reference: identifier

        self.onBehalfOf = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense_Performer',
             'child_variable': 'actor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense_Performer',
             'child_variable': 'onBehalfOf'},
        ]


class MedicationDispense_Substitution(fhirbase):
    """
    Indicates that a medication product is to be or has been dispensed for
    a named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy
    system responding to a medication order.

    Args:
        wasSubstituted: True if the dispenser dispensed a different drug or
            product from what was prescribed.
        type: A code signifying whether a different drug was dispensed from
            what was prescribed.
        reason: Indicates the reason for the substitution of (or lack of
            substitution) from what was prescribed.
        responsibleParty: The person or organization that has primary
            responsibility for the substitution.
    """

    __name__ = 'MedicationDispense_Substitution'

    def __init__(self, dict_values=None):
        self.wasSubstituted = None
        # type: bool

        self.type = None
        # reference to CodeableConcept

        self.reason = None
        # type: list
        # reference to CodeableConcept

        self.responsibleParty = None
        # type: list
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense_Substitution',
             'child_variable': 'reason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense_Substitution',
             'child_variable': 'responsibleParty'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense_Substitution',
             'child_variable': 'type'},
        ]
