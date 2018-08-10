from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Reference import Reference
from .Period import Period

class Coverage(fhirbase):
    """Financial instrument which may be used to reimburse or pay for health
    care products and services.
    """

    def __init__(self, dict_values=None):
        # this is a coverage resource
        self.resourceType = 'Coverage'
        # type = string
        # possible values = Coverage

        # the status of the resource instance.
        self.status = None
        # type = string

        # the type of coverage: social program, medical plan, accident coverage
        # (workers compensation, auto), group health or payment by an individual
        # or organization.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the party who 'owns' the insurance policy,  may be an individual,
        # corporation or the subscriber's employer.
        self.policyHolder = None
        # reference to Reference: identifier

        # the party who has signed-up for or 'owns' the contractual relationship
        # to the policy or to whom the benefit of the policy for services rendered
        # to them or their family is due.
        self.subscriber = None
        # reference to Reference: identifier

        # the insurer assigned id for the subscriber.
        self.subscriberId = None
        # type = string

        # the party who benefits from the insurance coverage., the patient when
        # services are provided.
        self.beneficiary = None
        # reference to Reference: identifier

        # the relationship of beneficiary (patient) to the subscriber.
        self.relationship = None
        # reference to CodeableConcept: CodeableConcept

        # time period during which the coverage is in force. a missing start date
        # indicates the start date isn't known, a missing end date means the
        # coverage is continuing to be in force.
        self.period = None
        # reference to Period: Period

        # the program or plan underwriter or payor including both insurance and
        # non-insurance agreements, such as patient-pay agreements. may provide
        # multiple identifiers such as insurance company identifier or business
        # identifier (bin number).
        self.payor = None
        # type = array
        # reference to Reference: identifier

        # a suite of underwrite specific classifiers, for example may be used to
        # identify a class of coverage or employer group, policy, plan.
        self.grouping = None
        # reference to Coverage_Grouping: Coverage_Grouping

        # a unique identifier for a dependent under the coverage.
        self.dependent = None
        # type = string

        # an optional counter for a particular instance of the identified coverage
        # which increments upon each renewal.
        self.sequence = None
        # type = string

        # the order of applicability of this coverage relative to other coverages
        # which are currently inforce. note, there may be gaps in the numbering
        # and this does not imply primary, secondard etc. as the specific
        # positioning of coverages depends upon the episode of care.
        self.order = None
        # type = int

        # the insurer-specific identifier for the insurer-defined network of
        # providers to which the beneficiary may seek treatment which will be
        # covered at the 'in-network' rate, otherwise 'out of network' terms and
        # conditions apply.
        self.network = None
        # type = string

        # the policy(s) which constitute this insurance coverage.
        self.contract = None
        # type = array
        # reference to Reference: identifier

        # the main (and possibly only) identifier for the coverage - often
        # referred to as a member id, certificate number, personal health number
        # or case id. may be constructed as the concatination of the
        # coverage.subscriberid and the coverage.dependant.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Coverage',
            'child_variable': 'subscriber'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Coverage',
            'child_variable': 'beneficiary'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Coverage',
            'child_variable': 'contract'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Coverage',
            'child_variable': 'period'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Coverage',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Coverage',
            'child_variable': 'payor'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Coverage',
            'child_variable': 'relationship'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Coverage',
            'child_variable': 'type'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Coverage',
            'child_variable': 'policyHolder'},

            {'parent_entity': 'Coverage_Grouping',
            'parent_variable': 'object_id',
            'child_entity': 'Coverage',
            'child_variable': 'grouping'},
        ]

class Coverage_Grouping(fhirbase):
    """Financial instrument which may be used to reimburse or pay for health
    care products and services.
    """

    def __init__(self, dict_values=None):
        # identifies a style or collective of coverage issued by the underwriter,
        # for example may be used to identify an employer group. may also be
        # referred to as a policy or group id.
        self.group = None
        # type = string

        # a short description for the group.
        self.groupDisplay = None
        # type = string

        # identifies a style or collective of coverage issued by the underwriter,
        # for example may be used to identify a subset of an employer group.
        self.subGroup = None
        # type = string

        # a short description for the subgroup.
        self.subGroupDisplay = None
        # type = string

        # identifies a style or collective of coverage issued by the underwriter,
        # for example may be used to identify a collection of benefits provided to
        # employees. may be referred to as a section or division id.
        self.plan = None
        # type = string

        # a short description for the plan.
        self.planDisplay = None
        # type = string

        # identifies a sub-style or sub-collective of coverage issued by the
        # underwriter, for example may be used to identify a subset of a
        # collection of benefits provided to employees.
        self.subPlan = None
        # type = string

        # a short description for the subplan.
        self.subPlanDisplay = None
        # type = string

        # identifies a style or collective of coverage issues by the underwriter,
        # for example may be used to identify a class of coverage such as a level
        # of deductables or co-payment.
        self._class = None
        # type = string

        # a short description for the class.
        self.classDisplay = None
        # type = string

        # identifies a sub-style or sub-collective of coverage issues by the
        # underwriter, for example may be used to identify a subclass of coverage
        # such as a sub-level of deductables or co-payment.
        self.subClass = None
        # type = string

        # a short description for the subclass.
        self.subClassDisplay = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


