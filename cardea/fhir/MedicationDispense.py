from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Annotation import Annotation
from .Identifier import Identifier
from .Reference import Reference
from .Dosage import Dosage
from .Quantity import Quantity

class MedicationDispense(fhirbase):
    """Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    def __init__(self, dict_values=None):
        # this is a medicationdispense resource
        self.resourceType = 'MedicationDispense'
        # type = string
        # possible values = MedicationDispense

        # the procedure that the dispense is done because of.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # a code specifying the state of the set of dispense events.
        self.status = None
        # type = string
        # possible values = preparation, in-progress, on-hold, completed, entered-in-error, stopped

        # indicates type of medication dispense and where the medication is
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

        # a link to a resource representing the person or the group to whom the
        # medication will be given.
        self.subject = None
        # reference to Reference: identifier

        # the encounter or episode of care that establishes the context for this
        # event.
        self.context = None
        # reference to Reference: identifier

        # additional information that supports the medication being dispensed.
        self.supportingInformation = None
        # type = array
        # reference to Reference: identifier

        # indicates who or what performed the event.  it should be assumed that
        # the performer is the dispenser of the medication.
        self.performer = None
        # type = array
        # reference to MedicationDispense_Performer: MedicationDispense_Performer

        # indicates the medication order that is being dispensed against.
        self.authorizingPrescription = None
        # type = array
        # reference to Reference: identifier

        # indicates the type of dispensing event that is performed. for example,
        # trial fill, completion of trial, partial fill, emergency fill, samples,
        # etc.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the amount of medication that has been dispensed. includes unit of
        # measure.
        self.quantity = None
        # reference to Quantity: Quantity

        # the amount of medication expressed as a timing amount.
        self.daysSupply = None
        # reference to Quantity: Quantity

        # the time when the dispensed product was packaged and reviewed.
        self.whenPrepared = None
        # type = string

        # the time the dispensed product was provided to the patient or their
        # representative.
        self.whenHandedOver = None
        # type = string

        # identification of the facility/location where the medication was shipped
        # to, as part of the dispense event.
        self.destination = None
        # reference to Reference: identifier

        # identifies the person who picked up the medication.  this will usually
        # be a patient or their caregiver, but some cases exist where it can be a
        # healthcare professional.
        self.receiver = None
        # type = array
        # reference to Reference: identifier

        # extra information about the dispense that could not be conveyed in the
        # other attributes.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # indicates how the medication is to be used by the patient.
        self.dosageInstruction = None
        # type = array
        # reference to Dosage: Dosage

        # indicates whether or not substitution was made as part of the dispense.
        # in some cases substitution will be expected but does not happen, in
        # other cases substitution is not expected but does happen.  this block
        # explains what substitution did or did not happen and why.  if nothing is
        # specified, substitution was not done.
        self.substitution = None
        # reference to MedicationDispense_Substitution: MedicationDispense_Substitution

        # indicates an actual or potential clinical issue with or between one or
        # more active or proposed clinical actions for a patient; e.g. drug-drug
        # interaction, duplicate therapy, dosage alert etc.
        self.detectedIssue = None
        # type = array
        # reference to Reference: identifier

        # true if the dispense was not performed for some reason.
        self.notDone = None
        # type = boolean

        # indicates the reason why a dispense was not performed.
        self.notDoneReasonCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the reason why a dispense was not performed.
        self.notDoneReasonReference = None
        # reference to Reference: identifier

        # a summary of the events of interest that have occurred, such as when the
        # dispense was verified.
        self.eventHistory = None
        # type = array
        # reference to Reference: identifier

        # identifier assigned by the dispensing facility - this is an identifier
        # assigned outside fhir.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['preparation', 'in-progress', 'on-hold', 'completed', 'entered-in-error', 'stopped']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'preparation, in-progress, on-hold, completed, entered-in-error, stopped'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'notDoneReasonCodeableConcept'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'daysSupply'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'medicationReference'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'note'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'category'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'context'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'receiver'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'destination'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'authorizingPrescription'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'detectedIssue'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'notDoneReasonReference'},

            {'parent_entity': 'MedicationDispense_Substitution',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'substitution'},

            {'parent_entity': 'MedicationDispense_Performer',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'performer'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'supportingInformation'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'partOf'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense',
            'child_variable': 'eventHistory'},

            {'parent_entity': 'Dosage',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense',
            'child_variable': 'dosageInstruction'},
        ]

class MedicationDispense_Performer(fhirbase):
    """Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    def __init__(self, dict_values=None):
        # the device, practitioner, etc. who performed the action.  it should be
        # assumed that the actor is the dispenser of the medication.
        self.actor = None
        # reference to Reference: identifier

        # the organization the device or practitioner was acting on behalf of.
        self.onBehalfOf = None
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense_Performer',
            'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense_Performer',
            'child_variable': 'actor'},
        ]

class MedicationDispense_Substitution(fhirbase):
    """Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    def __init__(self, dict_values=None):
        # true if the dispenser dispensed a different drug or product from what
        # was prescribed.
        self.wasSubstituted = None
        # type = boolean

        # a code signifying whether a different drug was dispensed from what was
        # prescribed.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # indicates the reason for the substitution of (or lack of substitution)
        # from what was prescribed.
        self.reason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the person or organization that has primary responsibility for the
        # substitution.
        self.responsibleParty = None
        # type = array
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationDispense_Substitution',
            'child_variable': 'responsibleParty'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense_Substitution',
            'child_variable': 'reason'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationDispense_Substitution',
            'child_variable': 'type'},
        ]

