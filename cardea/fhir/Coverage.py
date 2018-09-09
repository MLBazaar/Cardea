from .fhirbase import fhirbase


class Coverage(fhirbase):
    """
    Financial instrument which may be used to reimburse or pay for health
    care products and services.
    """

    __name__ = 'Coverage'

    def __init__(self, dict_values=None):
        self.resourceType = 'Coverage'
        """
        This is a Coverage resource

        type: string
        possible values: Coverage
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.type = None
        """
        The type of coverage: social program, medical plan, accident coverage
        (workers compensation, auto), group health or payment by an individual
        or organization.

        reference to CodeableConcept
        """

        self.policyHolder = None
        """
        The party who 'owns' the insurance policy,  may be an individual,
        corporation or the subscriber's employer.

        reference to Reference: identifier
        """

        self.subscriber = None
        """
        The party who has signed-up for or 'owns' the contractual relationship
        to the policy or to whom the benefit of the policy for services
        rendered to them or their family is due.

        reference to Reference: identifier
        """

        self.subscriberId = None
        """
        The insurer assigned ID for the Subscriber.

        type: string
        """

        self.beneficiary = None
        """
        The party who benefits from the insurance coverage., the patient when
        services are provided.

        reference to Reference: identifier
        """

        self.relationship = None
        """
        The relationship of beneficiary (patient) to the subscriber.

        reference to CodeableConcept
        """

        self.period = None
        """
        Time period during which the coverage is in force. A missing start
        date indicates the start date isn't known, a missing end date means
        the coverage is continuing to be in force.

        reference to Period
        """

        self.payor = None
        """
        The program or plan underwriter or payor including both insurance and
        non-insurance agreements, such as patient-pay agreements. May provide
        multiple identifiers such as insurance company identifier or business
        identifier (BIN number).

        type: array
        reference to Reference: identifier
        """

        self.grouping = None
        """
        A suite of underwrite specific classifiers, for example may be used to
        identify a class of coverage or employer group, Policy, Plan.

        reference to Coverage_Grouping
        """

        self.dependent = None
        """
        A unique identifier for a dependent under the coverage.

        type: string
        """

        self.sequence = None
        """
        An optional counter for a particular instance of the identified
        coverage which increments upon each renewal.

        type: string
        """

        self.order = None
        """
        The order of applicability of this coverage relative to other
        coverages which are currently inforce. Note, there may be gaps in the
        numbering and this does not imply primary, secondard etc. as the
        specific positioning of coverages depends upon the episode of care.

        type: int
        """

        self.network = None
        """
        The insurer-specific identifier for the insurer-defined network of
        providers to which the beneficiary may seek treatment which will be
        covered at the 'in-network' rate, otherwise 'out of network' terms and
        conditions apply.

        type: string
        """

        self.contract = None
        """
        The policy(s) which constitute this insurance coverage.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        The main (and possibly only) identifier for the coverage - often
        referred to as a Member Id, Certificate number, Personal Health Number
        or Case ID. May be constructed as the concatination of the
        Coverage.SubscriberID and the Coverage.dependant.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'period'},

            {'parent_entity': 'Coverage_Grouping',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'grouping'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'contract'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'subscriber'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'relationship'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'beneficiary'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'policyHolder'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Coverage',
             'child_variable': 'payor'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Coverage',
             'child_variable': 'identifier'},
        ]


class Coverage_Grouping(fhirbase):
    """
    Financial instrument which may be used to reimburse or pay for health
    care products and services.
    """

    __name__ = 'Coverage_Grouping'

    def __init__(self, dict_values=None):
        self.group = None
        """
        Identifies a style or collective of coverage issued by the
        underwriter, for example may be used to identify an employer group.
        May also be referred to as a Policy or Group ID.

        type: string
        """

        self.groupDisplay = None
        """
        A short description for the group.

        type: string
        """

        self.subGroup = None
        """
        Identifies a style or collective of coverage issued by the
        underwriter, for example may be used to identify a subset of an
        employer group.

        type: string
        """

        self.subGroupDisplay = None
        """
        A short description for the subgroup.

        type: string
        """

        self.plan = None
        """
        Identifies a style or collective of coverage issued by the
        underwriter, for example may be used to identify a collection of
        benefits provided to employees. May be referred to as a Section or
        Division ID.

        type: string
        """

        self.planDisplay = None
        """
        A short description for the plan.

        type: string
        """

        self.subPlan = None
        """
        Identifies a sub-style or sub-collective of coverage issued by the
        underwriter, for example may be used to identify a subset of a
        collection of benefits provided to employees.

        type: string
        """

        self.subPlanDisplay = None
        """
        A short description for the subplan.

        type: string
        """

        self._class = None
        """
        Identifies a style or collective of coverage issues by the
        underwriter, for example may be used to identify a class of coverage
        such as a level of deductables or co-payment.

        type: string
        """

        self.classDisplay = None
        """
        A short description for the class.

        type: string
        """

        self.subClass = None
        """
        Identifies a sub-style or sub-collective of coverage issues by the
        underwriter, for example may be used to identify a subclass of
        coverage such as a sub-level of deductables or co-payment.

        type: string
        """

        self.subClassDisplay = None
        """
        A short description for the subclass.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
