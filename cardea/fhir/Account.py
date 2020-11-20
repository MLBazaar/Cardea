from .fhirbase import fhirbase


class Account(fhirbase):
    """
    A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.

    Args:
        resourceType: This is a Account resource
        identifier: Unique identifier used to reference the account.  May or
            may not be intended for human use (e.g. credit card number).
        status: Indicates whether the account is presently used/usable or not.
        type: Categorizes the account for reporting and searching purposes.
        name: Name used for the account when displaying it to humans in
            reports, etc.
        subject: Identifies the patient, device, practitioner, location or
            other object the account is associated with.
        period: Identifies the period of time the account applies to; e.g.
            accounts created per fiscal year, quarter, etc.
        active: Indicates the period of time over which the account is allowed
            to have transactions posted to it. This period may be different to the
            coveragePeriod which is the duration of time that services may occur.
        balance: Represents the sum of all credits less all debits associated
            with the account.  Might be positive, zero or negative.
        coverage: The party(s) that are responsible for covering the payment
            of this account, and what order should they be applied to the account.
        owner: Indicates the organization, department, etc. with
            responsibility for the account.
        description: Provides additional information about what the account
            tracks and how it is used.
        guarantor: Parties financially responsible for the account.
    """

    __name__ = 'Account'

    def __init__(self, dict_values=None):
        self.resourceType = 'Account'
        # type: str
        # possible values: Account

        self.status = None
        # type: str
        # possible values: active, inactive, entered-in-error

        self.type = None
        # reference to CodeableConcept

        self.name = None
        # type: str

        self.subject = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.active = None
        # reference to Period

        self.balance = None
        # reference to Money

        self.coverage = None
        # type: list
        # reference to Account_Coverage

        self.owner = None
        # reference to Reference: identifier

        self.description = None
        # type: str

        self.guarantor = None
        # type: list
        # reference to Account_Guarantor

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
                        'active', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account',
             'child_variable': 'subject'},

            {'parent_entity': 'Account_Coverage',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'coverage'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account',
             'child_variable': 'owner'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'active'},

            {'parent_entity': 'Account_Guarantor',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'guarantor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'balance'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'identifier'},
        ]


class Account_Coverage(fhirbase):
    """
    A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.

    Args:
        coverage: The party(s) that are responsible for payment (or part of)
            of charges applied to this account (including self-pay).  A coverage
            may only be resposible for specific types of charges, and the sequence
            of the coverages in the account could be important when processing
            billing.
        priority: The priority of the coverage in the context of this account.
    """

    __name__ = 'Account_Coverage'

    def __init__(self, dict_values=None):
        self.coverage = None
        # reference to Reference: identifier

        self.priority = None
        # type: int

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

    Args:
        party: The entity who is responsible.
        onHold: A guarantor may be placed on credit hold or otherwise have
            their role temporarily suspended.
        period: The timeframe during which the guarantor accepts
            responsibility for the account.
    """

    __name__ = 'Account_Guarantor'

    def __init__(self, dict_values=None):
        self.party = None
        # reference to Reference: identifier

        self.onHold = None
        # type: bool

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account_Guarantor',
             'child_variable': 'party'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account_Guarantor',
             'child_variable': 'period'},
        ]
