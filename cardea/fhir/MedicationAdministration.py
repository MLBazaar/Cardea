from .fhirbase import fhirbase


class MedicationAdministration(fhirbase):
    """
    Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a
    tablet or it may be a long running infusion.  Related resources tie
    this event to the authorizing prescription, and the specific encounter
    between patient and health care practitioner.
    """

    __name__ = 'MedicationAdministration'

    def __init__(self, dict_values=None):
        self.resourceType = 'MedicationAdministration'
        """
        This is a MedicationAdministration resource

        type: string
        possible values: MedicationAdministration
        """

        self.definition = None
        """
        A protocol, guideline, orderset or other definition that was adhered
        to in whole or in part by this event.

        type: array
        reference to Reference: identifier
        """

        self.partOf = None
        """
        A larger event of which this particular event is a component or step.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        Will generally be set to show that the administration has been
        completed.  For some long running administrations such as infusions it
        is possible for an administration to be started but not completed or
        it may be paused while some other process is under way.

        type: string
        possible values: in-progress, on-hold, completed,
        entered-in-error, stopped, unknown
        """

        self.category = None
        """
        Indicates the type of medication administration and where the
        medication is expected to be consumed or administered.

        reference to CodeableConcept
        """

        self.medicationCodeableConcept = None
        """
        Identifies the medication that was administered. This is either a link
        to a resource representing the details of the medication or a simple
        attribute carrying a code that identifies the medication from a known
        list of medications.

        reference to CodeableConcept
        """

        self.medicationReference = None
        """
        Identifies the medication that was administered. This is either a link
        to a resource representing the details of the medication or a simple
        attribute carrying a code that identifies the medication from a known
        list of medications.

        reference to Reference: identifier
        """

        self.subject = None
        """
        The person or animal or group receiving the medication.

        reference to Reference: identifier
        """

        self.context = None
        """
        The visit, admission or other contact between patient and health care
        provider the medication administration was performed as part of.

        reference to Reference: identifier
        """

        self.supportingInformation = None
        """
        Additional information (for example, patient height and weight) that
        supports the administration of the medication.

        type: array
        reference to Reference: identifier
        """

        self.effectiveDateTime = None
        """
        A specific date/time or interval of time during which the
        administration took place (or did not take place, when the 'notGiven'
        attribute is true). For many administrations, such as swallowing a
        tablet the use of dateTime is more appropriate.

        type: string
        """

        self.effectivePeriod = None
        """
        A specific date/time or interval of time during which the
        administration took place (or did not take place, when the 'notGiven'
        attribute is true). For many administrations, such as swallowing a
        tablet the use of dateTime is more appropriate.

        reference to Period
        """

        self.performer = None
        """
        The individual who was responsible for giving the medication to the
        patient.

        type: array
        reference to MedicationAdministration_Performer
        """

        self.notGiven = None
        """
        Set this to true if the record is saying that the medication was NOT
        administered.

        type: boolean
        """

        self.reasonNotGiven = None
        """
        A code indicating why the administration was not performed.

        type: array
        reference to CodeableConcept
        """

        self.reasonCode = None
        """
        A code indicating why the medication was given.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Condition or observation that supports why the medication was
        administered.

        type: array
        reference to Reference: identifier
        """

        self.prescription = None
        """
        The original request, instruction or authority to perform the
        administration.

        reference to Reference: identifier
        """

        self.device = None
        """
        The device used in administering the medication to the patient.  For
        example, a particular infusion pump.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Extra information about the medication administration that is not
        conveyed by the other attributes.

        type: array
        reference to Annotation
        """

        self.dosage = None
        """
        Describes the medication dosage information details e.g. dose, rate,
        site, route, etc.

        reference to MedicationAdministration_Dosage
        """

        self.eventHistory = None
        """
        A summary of the events of interest that have occurred, such as when
        the administration was verified.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        External identifier - FHIR will generate its own internal identifiers
        (probably URLs) which do not need to be explicitly managed by the
        resource.  The identifier here is one that would be used by another
        non-FHIR system - for example an automated medication pump would
        provide a record each time it operated; an administration while the
        patient was off the ward might be made with a different system and
        entered after the event.  Particularly important if these records have
        to be updated.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'eventHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'prescription'},

            {'parent_entity': 'MedicationAdministration_Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'dosage'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'note'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'MedicationAdministration_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'device'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'reasonCode'},

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
             'child_variable': 'partOf'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'reasonNotGiven'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration',
             'child_variable': 'medicationReference'},
        ]


class MedicationAdministration_Performer(fhirbase):
    """
    Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a
    tablet or it may be a long running infusion.  Related resources tie
    this event to the authorizing prescription, and the specific encounter
    between patient and health care practitioner.
    """

    __name__ = 'MedicationAdministration_Performer'

    def __init__(self, dict_values=None):
        self.actor = None
        """
        The device, practitioner, etc. who performed the action.

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
             'child_entity': 'MedicationAdministration_Performer',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationAdministration_Performer',
             'child_variable': 'actor'},
        ]


class MedicationAdministration_Dosage(fhirbase):
    """
    Describes the event of a patient consuming or otherwise being
    administered a medication.  This may be as simple as swallowing a
    tablet or it may be a long running infusion.  Related resources tie
    this event to the authorizing prescription, and the specific encounter
    between patient and health care practitioner.
    """

    __name__ = 'MedicationAdministration_Dosage'

    def __init__(self, dict_values=None):
        self.text = None
        """
        Free text dosage can be used for cases where the dosage administered
        is too complex to code. When coded dosage is present, the free text
        dosage may still be present for display to humans.  The dosage
        instructions should reflect the dosage of the medication that was
        administered.

        type: string
        """

        self.site = None
        """
        A coded specification of the anatomic site where the medication first
        entered the body.  For example, "left arm".

        reference to CodeableConcept
        """

        self.route = None
        """
        A code specifying the route or physiological path of administration of
        a therapeutic agent into or onto the patient.  For example, topical,
        intravenous, etc.

        reference to CodeableConcept
        """

        self.method = None
        """
        A coded value indicating the method by which the medication is
        intended to be or was introduced into or on the body.  This attribute
        will most often NOT be populated.  It is most commonly used for
        injections.  For example, Slow Push, Deep IV.

        reference to CodeableConcept
        """

        self.dose = None
        """
        The amount of the medication given at one administration event.   Use
        this value when the administration is essentially an instantaneous
        event such as a swallowing a tablet or giving an injection.

        reference to Quantity
        """

        self.rateRatio = None
        """
        Identifies the speed with which the medication was or will be
        introduced into the patient.  Typically the rate for an infusion e.g.
        100 ml per 1 hour or 100 ml/hr.  May also be expressed as a rate per
        unit of time e.g. 500 ml per 2 hours.  Other examples:  200 mcg/min or
        200 mcg/1 minute; 1 liter/8 hours.

        reference to Ratio
        """

        self.rateSimpleQuantity = None
        """
        Identifies the speed with which the medication was or will be
        introduced into the patient.  Typically the rate for an infusion e.g.
        100 ml per 1 hour or 100 ml/hr.  May also be expressed as a rate per
        unit of time e.g. 500 ml per 2 hours.  Other examples:  200 mcg/min or
        200 mcg/1 minute; 1 liter/8 hours.

        reference to Quantity
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'dose'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'method'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'rateRatio'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'rateSimpleQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'route'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationAdministration_Dosage',
             'child_variable': 'site'},
        ]
