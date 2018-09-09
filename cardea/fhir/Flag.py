from .fhirbase import fhirbase


class Flag(fhirbase):
    """
    Prospective warnings of potential issues when providing care to the
    patient.
    """

    __name__ = 'Flag'

    def __init__(self, dict_values=None):
        self.resourceType = 'Flag'
        """
        This is a Flag resource

        type: string
        possible values: Flag
        """

        self.status = None
        """
        Supports basic workflow.

        type: string
        possible values: active, inactive, entered-in-error
        """

        self.category = None
        """
        Allows an flag to be divided into different categories like clinical,
        administrative etc. Intended to be used as a means of filtering which
        flags are displayed to particular user or in a given context.

        reference to CodeableConcept
        """

        self.code = None
        """
        The coded value or textual component of the flag to display to the
        user.

        reference to CodeableConcept
        """

        self.subject = None
        """
        The patient, location, group , organization , or practitioner, etc.
        this is about record this flag is associated with.

        reference to Reference: identifier
        """

        self.period = None
        """
        The period of time from the activation of the flag to inactivation of
        the flag. If the flag is active, the end of the period should be
        unspecified.

        reference to Period
        """

        self.encounter = None
        """
        This alert is only relevant during the encounter.

        reference to Reference: identifier
        """

        self.author = None
        """
        The person, organization or device that created the flag.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifier assigned to the flag for external use (outside the FHIR
        environment).

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'code'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'period'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'author'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'encounter'},
        ]
