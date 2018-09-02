from .fhirbase import fhirbase


class Flag(fhirbase):
    """Prospective warnings of potential issues when providing care to the
    patient.
    """

    def __init__(self, dict_values=None):
        # this is a flag resource
        self.resourceType = 'Flag'
        # type = string
        # possible values: Flag

        # supports basic workflow.
        self.status = None
        # type = string
        # possible values: active, inactive, entered-in-error

        # allows an flag to be divided into different categories like clinical,
        # administrative etc. intended to be used as a means of filtering which
        # flags are displayed to particular user or in a given context.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # the coded value or textual component of the flag to display to the user.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the patient, location, group , organization , or practitioner, etc. this
        # is about record this flag is associated with.
        self.subject = None
        # reference to Reference: identifier

        # the period of time from the activation of the flag to inactivation of
        # the flag. if the flag is active, the end of the period should be
        # unspecified.
        self.period = None
        # reference to Period: Period

        # this alert is only relevant during the encounter.
        self.encounter = None
        # reference to Reference: identifier

        # the person, organization or device that created the flag.
        self.author = None
        # reference to Reference: identifier

        # identifier assigned to the flag for external use (outside the fhir
        # environment).
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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'encounter'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'author'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Flag',
             'child_variable': 'subject'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Flag',
             'child_variable': 'period'},
        ]
