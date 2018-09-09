from .fhirbase import fhirbase


class MedicationDispense(fhirbase):
    """
    Indicates that a medication product is to be or has been dispensed for
    a named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy
    system responding to a medication order.
    """

    __name__ = 'MedicationDispense'

    def __init__(self, dict_values=None):
        self.resourceType = 'MedicationDispense'
        """
        This is a MedicationDispense resource

        type: string
        possible values: MedicationDispense
        """

        self.partOf = None
        """
        The procedure that the dispense is done because of.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        A code specifying the state of the set of dispense events.

        type: string
        possible values: preparation, in-progress, on-hold, completed,
        entered-in-error, stopped
        """

        self.category = None
        """
        Indicates type of medication dispense and where the medication is
        expected to be consumed or administered.

        reference to CodeableConcept
        """

        self.medicationCodeableConcept = None
        """
        Identifies the medication being administered. This is either a link to
        a resource representing the details of the medication or a simple
        attribute carrying a code that identifies the medication from a known
        list of medications.

        reference to CodeableConcept
        """

        self.medicationReference = None
        """
        Identifies the medication being administered. This is either a link to
        a resource representing the details of the medication or a simple
        attribute carrying a code that identifies the medication from a known
        list of medications.

        reference to Reference: identifier
        """

        self.subject = None
        """
        A link to a resource representing the person or the group to whom the
        medication will be given.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter or episode of care that establishes the context for this
        event.

        reference to Reference: identifier
        """

        self.supportingInformation = None
        """
        Additional information that supports the medication being dispensed.

        type: array
        reference to Reference: identifier
        """

        self.performer = None
        """
        Indicates who or what performed the event.  It should be assumed that
        the performer is the dispenser of the medication.

        type: array
        reference to MedicationDispense_Performer
        """

        self.authorizingPrescription = None
        """
        Indicates the medication order that is being dispensed against.

        type: array
        reference to Reference: identifier
        """

        self.type = None
        """
        Indicates the type of dispensing event that is performed. For example,
        Trial Fill, Completion of Trial, Partial Fill, Emergency Fill,
        Samples, etc.

        reference to CodeableConcept
        """

        self.quantity = None
        """
        The amount of medication that has been dispensed. Includes unit of
        measure.

        reference to Quantity
        """

        self.daysSupply = None
        """
        The amount of medication expressed as a timing amount.

        reference to Quantity
        """

        self.whenPrepared = None
        """
        The time when the dispensed product was packaged and reviewed.

        type: string
        """

        self.whenHandedOver = None
        """
        The time the dispensed product was provided to the patient or their
        representative.

        type: string
        """

        self.destination = None
        """
        Identification of the facility/location where the medication was
        shipped to, as part of the dispense event.

        reference to Reference: identifier
        """

        self.receiver = None
        """
        Identifies the person who picked up the medication.  This will usually
        be a patient or their caregiver, but some cases exist where it can be
        a healthcare professional.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Extra information about the dispense that could not be conveyed in the
        other attributes.

        type: array
        reference to Annotation
        """

        self.dosageInstruction = None
        """
        Indicates how the medication is to be used by the patient.

        type: array
        reference to Dosage
        """

        self.substitution = None
        """
        Indicates whether or not substitution was made as part of the
        dispense.  In some cases substitution will be expected but does not
        happen, in other cases substitution is not expected but does happen.
        This block explains what substitution did or did not happen and why.
        If nothing is specified, substitution was not done.

        reference to MedicationDispense_Substitution
        """

        self.detectedIssue = None
        """
        Indicates an actual or potential clinical issue with or between one or
        more active or proposed clinical actions for a patient; e.g. Drug-drug
        interaction, duplicate therapy, dosage alert etc.

        type: array
        reference to Reference: identifier
        """

        self.notDone = None
        """
        True if the dispense was not performed for some reason.

        type: boolean
        """

        self.notDoneReasonCodeableConcept = None
        """
        Indicates the reason why a dispense was not performed.

        reference to CodeableConcept
        """

        self.notDoneReasonReference = None
        """
        Indicates the reason why a dispense was not performed.

        reference to Reference: identifier
        """

        self.eventHistory = None
        """
        A summary of the events of interest that have occurred, such as when
        the dispense was verified.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifier assigned by the dispensing facility - this is an identifier
        assigned outside FHIR.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'daysSupply'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'partOf'},

            {'parent_entity': 'MedicationDispense_Substitution',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'substitution'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'notDoneReasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'authorizingPrescription'},

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
             'child_variable': 'medicationReference'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'dosageInstruction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'detectedIssue'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'receiver'},

            {'parent_entity': 'MedicationDispense_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'performer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'notDoneReasonCodeableConcept'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'destination'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationDispense',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationDispense',
             'child_variable': 'eventHistory'},
        ]


class MedicationDispense_Performer(fhirbase):
    """
    Indicates that a medication product is to be or has been dispensed for
    a named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy
    system responding to a medication order.
    """

    __name__ = 'MedicationDispense_Performer'

    def __init__(self, dict_values=None):
        self.actor = None
        """
        The device, practitioner, etc. who performed the action.  It should be
        assumed that the actor is the dispenser of the medication.

        reference to Reference: identifier
        """

        self.onBehalfOf = None
        """
        The organization the device or practitioner was acting on behalf of.

        reference to Reference: identifier
        """

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
    """

    __name__ = 'MedicationDispense_Substitution'

    def __init__(self, dict_values=None):
        self.wasSubstituted = None
        """
        True if the dispenser dispensed a different drug or product from what
        was prescribed.

        type: boolean
        """

        self.type = None
        """
        A code signifying whether a different drug was dispensed from what was
        prescribed.

        reference to CodeableConcept
        """

        self.reason = None
        """
        Indicates the reason for the substitution of (or lack of substitution)
        from what was prescribed.

        type: array
        reference to CodeableConcept
        """

        self.responsibleParty = None
        """
        The person or organization that has primary responsibility for the
        substitution.

        type: array
        reference to Reference: identifier
        """

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
