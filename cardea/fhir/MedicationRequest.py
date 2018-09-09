from .fhirbase import fhirbase


class MedicationRequest(fhirbase):
    """
    An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    __name__ = 'MedicationRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'MedicationRequest'
        """
        This is a MedicationRequest resource

        type: string
        possible values: MedicationRequest
        """

        self.definition = None
        """
        Protocol or definition followed by this request.

        type: array
        reference to Reference: identifier
        """

        self.basedOn = None
        """
        A plan or request that is fulfilled in whole or in part by this
        medication request.

        type: array
        reference to Reference: identifier
        """

        self.groupIdentifier = None
        """
        A shared identifier common to all requests that were authorized more
        or less simultaneously by a single author, representing the identifier
        of the requisition or prescription.

        reference to Identifier
        """

        self.status = None
        """
        A code specifying the current state of the order.  Generally this will
        be active or completed state.

        type: string
        possible values: active, on-hold, cancelled, completed,
        entered-in-error, stopped, draft, unknown
        """

        self.intent = None
        """
        Whether the request is a proposal, plan, or an original order.

        type: string
        possible values: proposal, plan, order, instance-order
        """

        self.category = None
        """
        Indicates the type of medication order and where the medication is
        expected to be consumed or administered.

        reference to CodeableConcept
        """

        self.priority = None
        """
        Indicates how quickly the Medication Request should be addressed with
        respect to other requests.

        type: string
        possible values: routine, urgent, stat, asap
        """

        self.medicationCodeableConcept = None
        """
        Identifies the medication being requested. This is a link to a
        resource that represents the medication which may be the details of
        the medication or simply an attribute carrying a code that identifies
        the medication from a known list of medications.

        reference to CodeableConcept
        """

        self.medicationReference = None
        """
        Identifies the medication being requested. This is a link to a
        resource that represents the medication which may be the details of
        the medication or simply an attribute carrying a code that identifies
        the medication from a known list of medications.

        reference to Reference: identifier
        """

        self.subject = None
        """
        A link to a resource representing the person or set of individuals to
        whom the medication will be given.

        reference to Reference: identifier
        """

        self.context = None
        """
        A link to an encounter, or episode of care, that identifies the
        particular occurrence or set occurrences of contact between patient
        and health care provider.

        reference to Reference: identifier
        """

        self.supportingInformation = None
        """
        Include additional information (for example, patient height and
        weight) that supports the ordering of the medication.

        type: array
        reference to Reference: identifier
        """

        self.authoredOn = None
        """
        The date (and perhaps time) when the prescription was initially
        written or authored on.

        type: string
        """

        self.requester = None
        """
        The individual, organization or device that initiated the request and
        has responsibility for its activation.

        reference to MedicationRequest_Requester
        """

        self.recorder = None
        """
        The person who entered the order on behalf of another individual for
        example in the case of a verbal or a telephone order.

        reference to Reference: identifier
        """

        self.reasonCode = None
        """
        The reason or the indication for ordering the medication.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Condition or observation that supports why the medication was ordered.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Extra information about the prescription that could not be conveyed by
        the other attributes.

        type: array
        reference to Annotation
        """

        self.dosageInstruction = None
        """
        Indicates how the medication is to be used by the patient.

        type: array
        reference to Dosage
        """

        self.dispenseRequest = None
        """
        Indicates the specific details for the dispense or medication supply
        part of a medication request (also known as a Medication Prescription
        or Medication Order).  Note that this information is not always sent
        with the order.  There may be in some settings (e.g. hospitals)
        institutional or system support for completing the dispense details in
        the pharmacy department.

        reference to MedicationRequest_DispenseRequest
        """

        self.substitution = None
        """
        Indicates whether or not substitution can or should be part of the
        dispense. In some cases substitution must happen, in other cases
        substitution must not happen. This block explains the prescriber's
        intent. If nothing is specified substitution may be done.

        reference to MedicationRequest_Substitution
        """

        self.priorPrescription = None
        """
        A link to a resource representing an earlier order related order or
        prescription.

        reference to Reference: identifier
        """

        self.detectedIssue = None
        """
        Indicates an actual or potential clinical issue with or between one or
        more active or proposed clinical actions for a patient; e.g. Drug-drug
        interaction, duplicate therapy, dosage alert etc.

        type: array
        reference to Reference: identifier
        """

        self.eventHistory = None
        """
        Links to Provenance records for past versions of this resource or
        fulfilling request or event resources that identify key state
        transitions or updates that are likely to be relevant to a user
        looking at the current version of the resource.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        This records identifiers associated with this medication request that
        are defined by business processes and/or used to refer to it when a
        direct URL reference to the resource itself is not appropriate. For
        example a re-imbursement system might issue its own id for each
        prescription that is created.  This is particularly important where
        FHIR only provides part of an entire workflow process where records
        must be tracked through an entire system.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'active', 'on-hold', 'cancelled', 'completed', 'entered-in-error',
                        'stopped', 'draft', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, on-hold, cancelled, completed, entered-in-error, stopped,'
                        'draft, unknown'))

        if self.intent is not None:
            for value in self.intent:
                if value is not None and value.lower() not in [
                        'proposal', 'plan', 'order', 'instance-order']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'proposal, plan, order, instance-order'))

        if self.priority is not None:
            for value in self.priority:
                if value is not None and value.lower() not in [
                        'routine', 'urgent', 'stat', 'asap']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'routine, urgent, stat, asap'))

    def get_relationships(self):

        return [
            {'parent_entity': 'MedicationRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'supportingInformation'},

            {'parent_entity': 'MedicationRequest_DispenseRequest',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'dispenseRequest'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'recorder'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'eventHistory'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'MedicationRequest_Substitution',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'substitution'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'medicationReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'priorPrescription'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest',
             'child_variable': 'dosageInstruction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest',
             'child_variable': 'detectedIssue'},
        ]


class MedicationRequest_Requester(fhirbase):
    """
    An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    __name__ = 'MedicationRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        """
        The healthcare professional responsible for authorizing the initial
        prescription.

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
             'child_entity': 'MedicationRequest_Requester',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'MedicationRequest_Requester',
             'child_variable': 'onBehalfOf'},
        ]


class MedicationRequest_DispenseRequest(fhirbase):
    """
    An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    __name__ = 'MedicationRequest_DispenseRequest'

    def __init__(self, dict_values=None):
        self.validityPeriod = None
        """
        This indicates the validity period of a prescription (stale dating the
        Prescription).

        reference to Period
        """

        self.numberOfRepeatsAllowed = None
        """
        An integer indicating the number of times, in addition to the original
        dispense, (aka refills or repeats) that the patient can receive the
        prescribed medication. Usage Notes: This integer does not include the
        original order dispense. This means that if an order indicates
        dispense 30 tablets plus "3 repeats", then the order can be dispensed
        a total of 4 times and the patient can receive a total of 120 tablets.

        type: int
        """

        self.quantity = None
        """
        The amount that is to be dispensed for one fill.

        reference to Quantity
        """

        self.expectedSupplyDuration = None
        """
        Identifies the period time over which the supplied product is expected
        to be used, or the length of time the dispense is expected to last.

        reference to Duration
        """

        self.performer = None
        """
        Indicates the intended dispensing Organization specified by the
        prescriber.

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
             'child_entity': 'MedicationRequest_DispenseRequest',
             'child_variable': 'performer'},

            {'parent_entity': 'Duration',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest_DispenseRequest',
             'child_variable': 'expectedSupplyDuration'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest_DispenseRequest',
             'child_variable': 'quantity'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest_DispenseRequest',
             'child_variable': 'validityPeriod'},
        ]


class MedicationRequest_Substitution(fhirbase):
    """
    An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    __name__ = 'MedicationRequest_Substitution'

    def __init__(self, dict_values=None):
        self.allowed = None
        """
        True if the prescriber allows a different drug to be dispensed from
        what was prescribed.

        type: boolean
        """

        self.reason = None
        """
        Indicates the reason for the substitution, or why substitution must or
        must not be performed.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'MedicationRequest_Substitution',
             'child_variable': 'reason'},
        ]
