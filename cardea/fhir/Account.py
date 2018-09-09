from .fhirbase import fhirbase


class Account(fhirbase):
    """A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.
    """

    __name__ = 'Account'

    def __init__(self, dict_values=None):
        # this is a account resource
        self.resourceType = 'Account'
        # type = string
        # possible values: Account

        # indicates whether the account is presently used/usable or not.
        self.status = None
        # type = string
        # possible values: active, inactive, entered-in-error

        # categorizes the account for reporting and searching purposes.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # name used for the account when displaying it to humans in reports, etc.
        self.name = None
        # type = string

        # identifies the patient, device, practitioner, location or other object
        # the account is associated with.
        self.subject = None
        # reference to Reference: identifier

        # identifies the period of time the account applies to; e.g. accounts
        # created per fiscal year, quarter, etc.
        self.period = None
        # reference to Period: Period

        # indicates the period of time over which the account is allowed to have
        # transactions posted to it. this period may be different to the
        # coverageperiod which is the duration of time that services may occur.
        self.active = None
        # reference to Period: Period

        # represents the sum of all credits less all debits associated with the
        # account.  might be positive, zero or negative.
        self.balance = None
        # reference to Money: Money

        # the party(s) that are responsible for covering the payment of this
        # account, and what order should they be applied to the account.
        self.coverage = None
        # type = array
        # reference to Account_Coverage: Account_Coverage

        # indicates the organization, department, etc. with responsibility for the
        # account.
        self.owner = None
        # reference to Reference: identifier

        # provides additional information about what the account tracks and how it
        # is used.
        self.description = None
        # type = string

        # parties financially responsible for the account.
        self.guarantor = None
        # type = array
        # reference to Account_Guarantor: Account_Guarantor

        # unique identifier used to reference the account.  may or may not be
        # intended for human use (e.g. credit card number).
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'active'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account',
             'child_variable': 'subject'},

            {'parent_entity': 'Account_Coverage',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'coverage'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'identifier'},

            {'parent_entity': 'Account_Guarantor',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'guarantor'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'period'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Account',
             'child_variable': 'owner'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Account',
             'child_variable': 'balance'},
        ]


class Account_Coverage(fhirbase):
    """A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.
    """

    __name__ = 'Account_Coverage'

    def __init__(self, dict_values=None):
        # the party(s) that are responsible for payment (or part of) of charges
        # applied to this account (including self-pay).  a coverage may only be
        # resposible for specific types of charges, and the sequence of the
        # coverages in the account could be important when processing billing.
        self.coverage = None
        # reference to Reference: identifier

        # the priority of the coverage in the context of this account.
        self.priority = None
        # type = int

        # unique identifier for object class
        self.object_id = None

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
    """A financial tool for tracking value accrued for a particular purpose.
    In the healthcare field, used to track charges for a patient, cost
    centers, etc.
    """

    __name__ = 'Account_Guarantor'

    def __init__(self, dict_values=None):
        # the entity who is responsible.
        self.party = None
        # reference to Reference: identifier

        # a guarantor may be placed on credit hold or otherwise have their role
        # temporarily suspended.
        self.onHold = None
        # type = boolean

        # the timeframe during which the guarantor accepts responsibility for the
        # account.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

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
