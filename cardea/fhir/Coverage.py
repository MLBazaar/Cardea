from .fhirbase import fhirbase


class Coverage(fhirbase):
    """
    Financial instrument which may be used to reimburse or pay for health
    care products and services.

    Args:
        resourceType: This is a Coverage resource
        identifier: The main (and possibly only) identifier for the coverage -
            often referred to as a Member Id, Certificate number, Personal Health
            Number or Case ID. May be constructed as the concatination of the
            Coverage.SubscriberID and the Coverage.dependant.
        status: The status of the resource instance.
        type: The type of coverage: social program, medical plan, accident
            coverage (workers compensation, auto), group health or payment by an
            individual or organization.
        policyHolder: The party who 'owns' the insurance policy,  may be an
            individual, corporation or the subscriber's employer.
        subscriber: The party who has signed-up for or 'owns' the contractual
            relationship to the policy or to whom the benefit of the policy for
            services rendered to them or their family is due.
        subscriberId: The insurer assigned ID for the Subscriber.
        beneficiary: The party who benefits from the insurance coverage., the
            patient when services are provided.
        relationship: The relationship of beneficiary (patient) to the
            subscriber.
        period: Time period during which the coverage is in force. A missing
            start date indicates the start date isn't known, a missing end date
            means the coverage is continuing to be in force.
        payor: The program or plan underwriter or payor including both
            insurance and non-insurance agreements, such as patient-pay
            agreements. May provide multiple identifiers such as insurance company
            identifier or business identifier (BIN number).
        grouping: A suite of underwrite specific classifiers, for example may
            be used to identify a class of coverage or employer group, Policy,
            Plan.
        dependent: A unique identifier for a dependent under the coverage.
        sequence: An optional counter for a particular instance of the
            identified coverage which increments upon each renewal.
        order: The order of applicability of this coverage relative to other
            coverages which are currently inforce. Note, there may be gaps in the
            numbering and this does not imply primary, secondard etc. as the
            specific positioning of coverages depends upon the episode of care.
        network: The insurer-specific identifier for the insurer-defined
            network of providers to which the beneficiary may seek treatment which
            will be covered at the 'in-network' rate, otherwise 'out of network'
            terms and conditions apply.
        contract: The policy(s) which constitute this insurance coverage.
    """

    __name__ = 'Coverage'

    def __init__(self, dict_values=None):
        self.resourceType = 'Coverage'
        # type: str
        # possible values: Coverage

        self.status = None
        # type: str

        self.type = None
        # reference to CodeableConcept

        self.policyHolder = None
        # reference to Reference: identifier

        self.subscriber = None
        # reference to Reference: identifier

        self.subscriberId = None
        # type: str

        self.beneficiary = None
        # reference to Reference: identifier

        self.relationship = None
        # reference to CodeableConcept

        self.period = None
        # reference to Period

        self.payor = None
        # type: list
        # reference to Reference: identifier

        self.grouping = None
        # reference to Coverage_Grouping

        self.dependent = None
        # type: str

        self.sequence = None
        # type: str

        self.order = None
        # type: int

        self.network = None
        # type: str

        self.contract = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'beneficiary'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'subscriber'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'policyHolder'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'relationship'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'contract'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'payor'},

            {'parent_entity': 'Coverage_Grouping',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'grouping'},
        ]


class Coverage_Grouping(fhirbase):
    """
    Financial instrument which may be used to reimburse or pay for health
    care products and services.

    Args:
        group: Identifies a style or collective of coverage issued by the
            underwriter, for example may be used to identify an employer group.
            May also be referred to as a Policy or Group ID.
        groupDisplay: A short description for the group.
        subGroup: Identifies a style or collective of coverage issued by the
            underwriter, for example may be used to identify a subset of an
            employer group.
        subGroupDisplay: A short description for the subgroup.
        plan: Identifies a style or collective of coverage issued by the
            underwriter, for example may be used to identify a collection of
            benefits provided to employees. May be referred to as a Section or
            Division ID.
        planDisplay: A short description for the plan.
        subPlan: Identifies a sub-style or sub-collective of coverage issued
            by the underwriter, for example may be used to identify a subset of a
            collection of benefits provided to employees.
        subPlanDisplay: A short description for the subplan.
        class: Identifies a style or collective of coverage issues by the
            underwriter, for example may be used to identify a class of coverage
            such as a level of deductables or co-payment.
        classDisplay: A short description for the class.
        subClass: Identifies a sub-style or sub-collective of coverage issues
            by the underwriter, for example may be used to identify a subclass of
            coverage such as a sub-level of deductables or co-payment.
        subClassDisplay: A short description for the subclass.
    """

    __name__ = 'Coverage_Grouping'

    def __init__(self, dict_values=None):
        self.group = None
        # type: str

        self.groupDisplay = None
        # type: str

        self.subGroup = None
        # type: str

        self.subGroupDisplay = None
        # type: str

        self.plan = None
        # type: str

        self.planDisplay = None
        # type: str

        self.subPlan = None
        # type: str

        self.subPlanDisplay = None
        # type: str

        self._class = None
        # type: str

        self.classDisplay = None
        # type: str

        self.subClass = None
        # type: str

        self.subClassDisplay = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
