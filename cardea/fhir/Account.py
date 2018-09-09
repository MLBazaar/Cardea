from .fhirbase import fhirbase


class Account(fhirbase):
    """
    A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.
    """

    __name__ = 'Account'

    def __init__(self, dict_values=None):
        self.resourceType = 'Account'
        """
        This is a Account resource

        type: string
        possible values: Account
        """

        self.status = None
        """
        Indicates whether the account is presently used/usable or not.

        type: string
        possible values: active, inactive, entered-in-error
        """

        self.type = None
        """
        Categorizes the account for reporting and searching purposes.

        reference to CodeableConcept
        """

        self.name = None
        """
        Name used for the account when displaying it to humans in reports,
        etc.

        type: string
        """

        self.subject = None
        """
        Identifies the patient, device, practitioner, location or other object
        the account is associated with.

        reference to Reference: identifier
        """

        self.period = None
        """
        Identifies the period of time the account applies to; e.g. accounts
        created per fiscal year, quarter, etc.

        reference to Period
        """

        self.active = None
        """
        Indicates the period of time over which the account is allowed to have
        transactions posted to it. This period may be different to the
        coveragePeriod which is the duration of time that services may occur.

        reference to Period
        """

        self.balance = None
        """
        Represents the sum of all credits less all debits associated with the
        account.  Might be positive, zero or negative.

        reference to Money
        """

        self.coverage = None
        """
        The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.

        type: array
        reference to Account_Coverage
        """

        self.owner = None
        """
        Indicates the organization, department, etc. with responsibility for
        the account.

        reference to Reference: identifier
        """

        self.description = None
        """
        Provides additional information about what the account tracks and how
        it is used.

        type: string
        """

        self.guarantor = None
        """
        Parties financially responsible for the account.

        type: array
        reference to Account_Guarantor
        """

        self.identifier = None
        """
        Unique identifier used to reference the account.  May or may not be
        intended for human use (e.g. credit card number).

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account',
             'child_variable': 'subject'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'balance'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'identifier'},

            {'parent_entity': 'Account_Guarantor',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'guarantor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account',
             'child_variable': 'owner'},

            {'parent_entity': 'Account_Coverage',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'coverage'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'type'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'active'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'period'},
        ]


class Account_Coverage(fhirbase):
    """
    A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.
    """

    __name__ = 'Account_Coverage'

    def __init__(self, dict_values=None):
        self.coverage = None
        """
        The party(s) that are responsible for payment (or part of) of charges
        applied to this account (including self-pay).  A coverage may only be
        resposible for specific types of charges, and the sequence of the
        coverages in the account could be important when processing billing.

        reference to Reference: identifier
        """

        self.priority = None
        """
        The priority of the coverage in the context of this account.

        type: int
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account_Coverage',
             'child_variable': 'coverage'},
        ]


class Account_Guarantor(fhirbase):
    """
    A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.
    """

    __name__ = 'Account_Guarantor'

    def __init__(self, dict_values=None):
        self.party = None
        """
        The entity who is responsible.

        reference to Reference: identifier
        """

        self.onHold = None
        """
        A guarantor may be placed on credit hold or otherwise have their role
        temporarily suspended.

        type: boolean
        """

        self.period = None
        """
        The timeframe during which the guarantor accepts responsibility for
        the account.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account_Guarantor',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account_Guarantor',
             'child_variable': 'party'},
        ]
