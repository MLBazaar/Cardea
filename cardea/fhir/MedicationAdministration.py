from .fhirbase import fhirbase


class MedicationAdministration(fhirbase):
    """
    Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a
    tablet or it may be a long running infusion.  Related resources tie
    this event to the authorizing prescription, and the specific encounter
    between patient and health care practitioner.

    Args:
        resourceType: This is a MedicationAdministration resource
        identifier: External identifier - FHIR will generate its own internal
            identifiers (probably URLs) which do not need to be explicitly managed
            by the resource.  The identifier here is one that would be used by
            another non-FHIR system - for example an automated medication pump
            would provide a record each time it operated; an administration while
            the patient was off the ward might be made with a different system and
            entered after the event.  Particularly important if these records have
            to be updated.
        definition: A protocol, guideline, orderset or other definition that
            was adhered to in whole or in part by this event.
        partOf: A larger event of which this particular event is a component
            or step.
        status: Will generally be set to show that the administration has been
            completed.  For some long running administrations such as infusions it
            is possible for an administration to be started but not completed or
            it may be paused while some other process is under way.
        category: Indicates the type of medication administration and where
            the medication is expected to be consumed or administered.
        medicationCodeableConcept: Identifies the medication that was
            administered. This is either a link to a resource representing the
            details of the medication or a simple attribute carrying a code that
            identifies the medication from a known list of medications.
        medicationReference: Identifies the medication that was administered.
            This is either a link to a resource representing the details of the
            medication or a simple attribute carrying a code that identifies the
            medication from a known list of medications.
        subject: The person or animal or group receiving the medication.
        context: The visit, admission or other contact between patient and
            health care provider the medication administration was performed as
            part of.
        supportingInformation: Additional information (for example, patient
            height and weight) that supports the administration of the medication.
        effectiveDateTime: A specific date/time or interval of time during
            which the administration took place (or did not take place, when the
            'notGiven' attribute is true). For many administrations, such as
            swallowing a tablet the use of dateTime is more appropriate.
        effectivePeriod: A specific date/time or interval of time during which
            the administration took place (or did not take place, when the
            'notGiven' attribute is true). For many administrations, such as
            swallowing a tablet the use of dateTime is more appropriate.
        performer: The individual who was responsible for giving the
            medication to the patient.
        notGiven: Set this to true if the record is saying that the medication
            was NOT administered.
        reasonNotGiven: A code indicating why the administration was not
            performed.
        reasonCode: A code indicating why the medication was given.
        reasonReference: Condition or observation that supports why the
            medication was administered.
        prescription: The original request, instruction or authority to
            perform the administration.
        device: The device used in administering the medication to the
            patient.  For example, a particular infusion pump.
        note: Extra information about the medication administration that is
            not conveyed by the other attributes.
        dosage: Describes the medication dosage information details e.g. dose,
            rate, site, route, etc.
        eventHistory: A summary of the events of interest that have occurred,
            such as when the administration was verified.
    """

    __name__ = 'MedicationAdministration'

    def __init__(self, dict_values=None):
        self.resourceType = 'MedicationAdministration'
        # type: str
        # possible values: MedicationAdministration

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str
        # possible values: in-progress, on-hold, completed,
        # entered-in-error, stopped, unknown

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

        self.effectiveDateTime = None
        # type: str

        self.effectivePeriod = None
        # reference to Period

        self.performer = None
        # type: list
        # reference to MedicationAdministration_Performer

        self.notGiven = None
        # type: bool

        self.reasonNotGiven = None
        # type: list
        # reference to CodeableConcept

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.prescription = None
        # reference to Reference: identifier

        self.device = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.dosage = None
        # reference to MedicationAdministration_Dosage

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
                    'in-progress', 'on-hold', 'completed', 'entered-in-error', 'stopped',
                        'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'in-progress, on-hold, completed, entered-in-error, stopped, '
                        'unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'device'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'medicationReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'prescription'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'note'},

            {'parent_entity': 'MedicationAdministration_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'eventHistory'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'identifier'},

            {'parent_entity': 'MedicationAdministration_Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'dosage'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'reasonNotGiven'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'subject'},
        ]


class MedicationAdministration_Performer(fhirbase):
    """
    Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a
    tablet or it may be a long running infusion.  Related resources tie
    this event to the authorizing prescription, and the specific encounter
    between patient and health care practitioner.

    Args:
        actor: The device, practitioner, etc. who performed the action.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'MedicationAdministration_Performer'

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
             'child_entity': 'MedicationAdministration_Performer',
             'child_variable': 'actor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration_Performer',
             'child_variable': 'onBehalfOf'},
        ]


class MedicationAdministration_Dosage(fhirbase):
    """
    Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a
    tablet or it may be a long running infusion.  Related resources tie
    this event to the authorizing prescription, and the specific encounter
    between patient and health care practitioner.

    Args:
        text: Free text dosage can be used for cases where the dosage
            administered is too complex to code. When coded dosage is present, the
            free text dosage may still be present for display to humans.  The
            dosage instructions should reflect the dosage of the medication that
            was administered.
        site: A coded specification of the anatomic site where the medication
            first entered the body.  For example, "left arm".
        route: A code specifying the route or physiological path of
            administration of a therapeutic agent into or onto the patient.  For
            example, topical, intravenous, etc.
        method: A coded value indicating the method by which the medication is
            intended to be or was introduced into or on the body.  This attribute
            will most often NOT be populated.  It is most commonly used for
            injections.  For example, Slow Push, Deep IV.
        dose: The amount of the medication given at one administration event.
            Use this value when the administration is essentially an instantaneous
            event such as a swallowing a tablet or giving an injection.
        rateRatio: Identifies the speed with which the medication was or will
            be introduced into the patient.  Typically the rate for an infusion
            e.g. 100 ml per 1 hour or 100 ml/hr.  May also be expressed as a rate
            per unit of time e.g. 500 ml per 2 hours.  Other examples:  200
            mcg/min or 200 mcg/1 minute; 1 liter/8 hours.
        rateSimpleQuantity: Identifies the speed with which the medication was
            or will be introduced into the patient.  Typically the rate for an
            infusion e.g. 100 ml per 1 hour or 100 ml/hr.  May also be expressed
            as a rate per unit of time e.g. 500 ml per 2 hours.  Other examples:
            200 mcg/min or 200 mcg/1 minute; 1 liter/8 hours.
    """

    __name__ = 'MedicationAdministration_Dosage'

    def __init__(self, dict_values=None):
        self.text = None
        # type: str

        self.site = None
        # reference to CodeableConcept

        self.route = None
        # reference to CodeableConcept

        self.method = None
        # reference to CodeableConcept

        self.dose = None
        # reference to Quantity

        self.rateRatio = None
        # reference to Ratio

        self.rateSimpleQuantity = None
        # reference to Quantity

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'site'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'dose'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'method'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'route'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'rateSimpleQuantity'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'rateRatio'},
        ]
