from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Annotation import Annotation
from .Reference import Reference
from .Period import Period

class MedicationAdministration(fhirbase):
    """Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a tablet
    or it may be a long running infusion.  Related resources tie this event
    to the authorizing prescription, and the specific encounter between
    patient and health care practitioner.
    """

    def __init__(self, dict_values=None):
        # this is a medicationadministration resource
        self.resourceType = 'MedicationAdministration'
        # type = string
        # possible values = MedicationAdministration

        # a protocol, guideline, orderset or other definition that was adhered to
        # in whole or in part by this event.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # a larger event of which this particular event is a component or step.
        self.partOf = None
        # type = array
        # reference to Reference: identifier

        # will generally be set to show that the administration has been
        # completed.  for some long running administrations such as infusions it
        # is possible for an administration to be started but not completed or it
        # may be paused while some other process is under way.
        self.status = None
        # type = string
        # possible values = in-progress, on-hold, completed, entered-in-error, stopped, unknown

        # indicates the type of medication administration and where the medication
        # is expected to be consumed or administered.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the medication that was administered. this is either a link
        # to a resource representing the details of the medication or a simple
        # attribute carrying a code that identifies the medication from a known
        # list of medications.
        self.medicationCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the medication that was administered. this is either a link
        # to a resource representing the details of the medication or a simple
        # attribute carrying a code that identifies the medication from a known
        # list of medications.
        self.medicationReference = None
        # reference to Reference: identifier

        # the person or animal or group receiving the medication.
        self.subject = None
        # reference to Reference: identifier

        # the visit, admission or other contact between patient and health care
        # provider the medication administration was performed as part of.
        self.context = None
        # reference to Reference: identifier

        # additional information (for example, patient height and weight) that
        # supports the administration of the medication.
        self.supportingInformation = None
        # type = array
        # reference to Reference: identifier

        # a specific date/time or interval of time during which the administration
        # took place (or did not take place, when the 'notgiven' attribute is
        # true). for many administrations, such as swallowing a tablet the use of
        # datetime is more appropriate.
        self.effectiveDateTime = None
        # type = string

        # a specific date/time or interval of time during which the administration
        # took place (or did not take place, when the 'notgiven' attribute is
        # true). for many administrations, such as swallowing a tablet the use of
        # datetime is more appropriate.
        self.effectivePeriod = None
        # reference to Period: Period

        # the individual who was responsible for giving the medication to the
        # patient.
        self.performer = None
        # type = array
        # reference to MedicationAdministration_Performer: MedicationAdministration_Performer

        # set this to true if the record is saying that the medication was not
        # administered.
        self.notGiven = None
        # type = boolean

        # a code indicating why the administration was not performed.
        self.reasonNotGiven = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a code indicating why the medication was given.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # condition or observation that supports why the medication was
        # administered.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # the original request, instruction or authority to perform the
        # administration.
        self.prescription = None
        # reference to Reference: identifier

        # the device used in administering the medication to the patient.  for
        # example, a particular infusion pump.
        self.device = None
        # type = array
        # reference to Reference: identifier

        # extra information about the medication administration that is not
        # conveyed by the other attributes.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # describes the medication dosage information details e.g. dose, rate,
        # site, route, etc.
        self.dosage = None
        # reference to MedicationAdministration_Dosage: MedicationAdministration_Dosage

        # a summary of the events of interest that have occurred, such as when the
        # administration was verified.
        self.eventHistory = None
        # type = array
        # reference to Reference: identifier

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
                if value != None and value.lower() not in ['in-progress', 'on-hold', 'completed', 'entered-in-error', 'stopped', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'in-progress, on-hold, completed, entered-in-error, stopped, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'prescription'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'reasonCode'},

            {'parent_entity': 'MedicationAdministration_Dosage',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'dosage'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'partOf'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'reasonNotGiven'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'context'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'category'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'definition'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'eventHistory'},

            {'parent_entity': 'MedicationAdministration_Performer',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'performer'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'device'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'medicationReference'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'supportingInformation'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration',
            'child_variable': 'subject'},
        ]

class MedicationAdministration_Performer(fhirbase):
    """Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a tablet
    or it may be a long running infusion.  Related resources tie this event
    to the authorizing prescription, and the specific encounter between
    patient and health care practitioner.
    """

    def __init__(self, dict_values=None):
        # the device, practitioner, etc. who performed the action.
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
            'child_entity': 'MedicationAdministration_Performer',
            'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationAdministration_Performer',
            'child_variable': 'actor'},
        ]

class MedicationAdministration_Dosage(fhirbase):
    """Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a tablet
    or it may be a long running infusion.  Related resources tie this event
    to the authorizing prescription, and the specific encounter between
    patient and health care practitioner.
    """

    def __init__(self, dict_values=None):
        # free text dosage can be used for cases where the dosage administered is
        # too complex to code. when coded dosage is present, the free text dosage
        # may still be present for display to humans.  the dosage instructions
        # should reflect the dosage of the medication that was administered.
        self.text = None
        # type = string

        # a coded specification of the anatomic site where the medication first
        # entered the body.  for example, "left arm".
        self.site = None
        # reference to CodeableConcept: CodeableConcept

        # a code specifying the route or physiological path of administration of a
        # therapeutic agent into or onto the patient.  for example, topical,
        # intravenous, etc.
        self.route = None
        # reference to CodeableConcept: CodeableConcept

        # a coded value indicating the method by which the medication is intended
        # to be or was introduced into or on the body.  this attribute will most
        # often not be populated.  it is most commonly used for injections.  for
        # example, slow push, deep iv.
        self.method = None
        # reference to CodeableConcept: CodeableConcept

        # the amount of the medication given at one administration event.   use
        # this value when the administration is essentially an instantaneous event
        # such as a swallowing a tablet or giving an injection.
        self.dose = None
        # reference to Quantity: Quantity

        # identifies the speed with which the medication was or will be introduced
        # into the patient.  typically the rate for an infusion e.g. 100 ml per 1
        # hour or 100 ml/hr.  may also be expressed as a rate per unit of time
        # e.g. 500 ml per 2 hours.  other examples:  200 mcg/min or 200 mcg/1
        # minute; 1 liter/8 hours.
        self.rateRatio = None
        # reference to Ratio: Ratio

        # identifies the speed with which the medication was or will be introduced
        # into the patient.  typically the rate for an infusion e.g. 100 ml per 1
        # hour or 100 ml/hr.  may also be expressed as a rate per unit of time
        # e.g. 500 ml per 2 hours.  other examples:  200 mcg/min or 200 mcg/1
        # minute; 1 liter/8 hours.
        self.rateSimpleQuantity = None
        # reference to Quantity: Quantity


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration_Dosage',
            'child_variable': 'rateSimpleQuantity'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration_Dosage',
            'child_variable': 'dose'},

            {'parent_entity': 'Ratio',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration_Dosage',
            'child_variable': 'rateRatio'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration_Dosage',
            'child_variable': 'route'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration_Dosage',
            'child_variable': 'method'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationAdministration_Dosage',
            'child_variable': 'site'},
        ]

