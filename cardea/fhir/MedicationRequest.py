from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Annotation import Annotation
from .Identifier import Identifier
from .Reference import Reference
from .Dosage import Dosage

class MedicationRequest(fhirbase):
    """An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    def __init__(self, dict_values=None):
        # this is a medicationrequest resource
        self.resourceType = 'MedicationRequest'
        # type = string
        # possible values = MedicationRequest

        # protocol or definition followed by this request.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # a plan or request that is fulfilled in whole or in part by this
        # medication request.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # a shared identifier common to all requests that were authorized more or
        # less simultaneously by a single author, representing the identifier of
        # the requisition or prescription.
        self.groupIdentifier = None
        # reference to Identifier: Identifier

        # a code specifying the current state of the order.  generally this will
        # be active or completed state.
        self.status = None
        # type = string
        # possible values = active, on-hold, cancelled, completed, entered-in-error, stopped, draft, unknown

        # whether the request is a proposal, plan, or an original order.
        self.intent = None
        # type = string
        # possible values = proposal, plan, order, instance-order

        # indicates the type of medication order and where the medication is
        # expected to be consumed or administered.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # indicates how quickly the medication request should be addressed with
        # respect to other requests.
        self.priority = None
        # type = string
        # possible values = routine, urgent, stat, asap

        # identifies the medication being requested. this is a link to a resource
        # that represents the medication which may be the details of the
        # medication or simply an attribute carrying a code that identifies the
        # medication from a known list of medications.
        self.medicationCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the medication being requested. this is a link to a resource
        # that represents the medication which may be the details of the
        # medication or simply an attribute carrying a code that identifies the
        # medication from a known list of medications.
        self.medicationReference = None
        # reference to Reference: identifier

        # a link to a resource representing the person or set of individuals to
        # whom the medication will be given.
        self.subject = None
        # reference to Reference: identifier

        # a link to an encounter, or episode of care, that identifies the
        # particular occurrence or set occurrences of contact between patient and
        # health care provider.
        self.context = None
        # reference to Reference: identifier

        # include additional information (for example, patient height and weight)
        # that supports the ordering of the medication.
        self.supportingInformation = None
        # type = array
        # reference to Reference: identifier

        # the date (and perhaps time) when the prescription was initially written
        # or authored on.
        self.authoredOn = None
        # type = string

        # the individual, organization or device that initiated the request and
        # has responsibility for its activation.
        self.requester = None
        # reference to MedicationRequest_Requester: MedicationRequest_Requester

        # the person who entered the order on behalf of another individual for
        # example in the case of a verbal or a telephone order.
        self.recorder = None
        # reference to Reference: identifier

        # the reason or the indication for ordering the medication.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # condition or observation that supports why the medication was ordered.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # extra information about the prescription that could not be conveyed by
        # the other attributes.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # indicates how the medication is to be used by the patient.
        self.dosageInstruction = None
        # type = array
        # reference to Dosage: Dosage

        # indicates the specific details for the dispense or medication supply
        # part of a medication request (also known as a medication prescription or
        # medication order).  note that this information is not always sent with
        # the order.  there may be in some settings (e.g. hospitals) institutional
        # or system support for completing the dispense details in the pharmacy
        # department.
        self.dispenseRequest = None
        # reference to MedicationRequest_DispenseRequest: MedicationRequest_DispenseRequest

        # indicates whether or not substitution can or should be part of the
        # dispense. in some cases substitution must happen, in other cases
        # substitution must not happen. this block explains the prescriber's
        # intent. if nothing is specified substitution may be done.
        self.substitution = None
        # reference to MedicationRequest_Substitution: MedicationRequest_Substitution

        # a link to a resource representing an earlier order related order or
        # prescription.
        self.priorPrescription = None
        # reference to Reference: identifier

        # indicates an actual or potential clinical issue with or between one or
        # more active or proposed clinical actions for a patient; e.g. drug-drug
        # interaction, duplicate therapy, dosage alert etc.
        self.detectedIssue = None
        # type = array
        # reference to Reference: identifier

        # links to provenance records for past versions of this resource or
        # fulfilling request or event resources that identify key state
        # transitions or updates that are likely to be relevant to a user looking
        # at the current version of the resource.
        self.eventHistory = None
        # type = array
        # reference to Reference: identifier

        # this records identifiers associated with this medication request that
        # are defined by business processes and/or used to refer to it when a
        # direct url reference to the resource itself is not appropriate. for
        # example a re-imbursement system might issue its own id for each
        # prescription that is created.  this is particularly important where fhir
        # only provides part of an entire workflow process where records must be
        # tracked through an entire system.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['active', 'on-hold', 'cancelled', 'completed', 'entered-in-error', 'stopped', 'draft', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'active, on-hold, cancelled, completed, entered-in-error, stopped, draft, unknown'))

        if self.intent is not None:
            for value in self.intent:
                if value != None and value.lower() not in ['proposal', 'plan', 'order', 'instance-order']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'proposal, plan, order, instance-order'))

        if self.priority is not None:
            for value in self.priority:
                if value != None and value.lower() not in ['routine', 'urgent', 'stat', 'asap']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'routine, urgent, stat, asap'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'note'},

            {'parent_entity': 'Dosage',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'dosageInstruction'},

            {'parent_entity': 'MedicationRequest_Requester',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'requester'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'recorder'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'definition'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'eventHistory'},

            {'parent_entity': 'MedicationRequest_Substitution',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'substitution'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'supportingInformation'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'category'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'detectedIssue'},

            {'parent_entity': 'MedicationRequest_DispenseRequest',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'dispenseRequest'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'medicationCodeableConcept'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'context'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'priorPrescription'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest',
            'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest',
            'child_variable': 'medicationReference'},
        ]

class MedicationRequest_Requester(fhirbase):
    """An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    def __init__(self, dict_values=None):
        # the healthcare professional responsible for authorizing the initial
        # prescription.
        self.agent = None
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
            'child_entity': 'MedicationRequest_Requester',
            'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest_Requester',
            'child_variable': 'agent'},
        ]

class MedicationRequest_DispenseRequest(fhirbase):
    """An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    def __init__(self, dict_values=None):
        # this indicates the validity period of a prescription (stale dating the
        # prescription).
        self.validityPeriod = None
        # reference to Period: Period

        # an integer indicating the number of times, in addition to the original
        # dispense, (aka refills or repeats) that the patient can receive the
        # prescribed medication. usage notes: this integer does not include the
        # original order dispense. this means that if an order indicates dispense
        # 30 tablets plus "3 repeats", then the order can be dispensed a total of
        # 4 times and the patient can receive a total of 120 tablets.
        self.numberOfRepeatsAllowed = None
        # type = int

        # the amount that is to be dispensed for one fill.
        self.quantity = None
        # reference to Quantity: Quantity

        # identifies the period time over which the supplied product is expected
        # to be used, or the length of time the dispense is expected to last.
        self.expectedSupplyDuration = None
        # reference to Duration: Duration

        # indicates the intended dispensing organization specified by the
        # prescriber.
        self.performer = None
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Duration',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest_DispenseRequest',
            'child_variable': 'expectedSupplyDuration'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest_DispenseRequest',
            'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'MedicationRequest_DispenseRequest',
            'child_variable': 'performer'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest_DispenseRequest',
            'child_variable': 'validityPeriod'},
        ]

class MedicationRequest_Substitution(fhirbase):
    """An order or request for both supply of the medication and the
    instructions for administration of the medication to a patient. The
    resource is called "MedicationRequest" rather than
    "MedicationPrescription" or "MedicationOrder" to generalize the use
    across inpatient and outpatient settings, including care plans, etc.,
    and to harmonize with workflow patterns.
    """

    def __init__(self, dict_values=None):
        # true if the prescriber allows a different drug to be dispensed from what
        # was prescribed.
        self.allowed = None
        # type = boolean

        # indicates the reason for the substitution, or why substitution must or
        # must not be performed.
        self.reason = None
        # reference to CodeableConcept: CodeableConcept


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'MedicationRequest_Substitution',
            'child_variable': 'reason'},
        ]

