from .fhirbase import fhirbase


class Flag(fhirbase):
    """
    Prospective warnings of potential issues when providing care to the
    patient.

    Args:
        resourceType: This is a Flag resource
        identifier: Identifier assigned to the flag for external use (outside
            the FHIR environment).
        status: Supports basic workflow.
        category: Allows an flag to be divided into different categories like
            clinical, administrative etc. Intended to be used as a means of
            filtering which flags are displayed to particular user or in a given
            context.
        code: The coded value or textual component of the flag to display to
            the user.
        subject: The patient, location, group , organization , or
            practitioner, etc. this is about record this flag is associated with.
        period: The period of time from the activation of the flag to
            inactivation of the flag. If the flag is active, the end of the period
            should be unspecified.
        encounter: This alert is only relevant during the encounter.
        author: The person, organization or device that created the flag.
    """

    __name__ = 'Flag'

    def __init__(self, dict_values=None):
        self.resourceType = 'Flag'
        # type: str
        # possible values: Flag

        self.status = None
        # type: str
        # possible values: active, inactive, entered-in-error

        self.category = None
        # reference to CodeableConcept

        self.code = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.encounter = None
        # reference to Reference: identifier

        self.author = None
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
                        'active', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'encounter'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'period'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'category'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'subject'},
        ]
