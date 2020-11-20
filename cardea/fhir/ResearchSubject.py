from .fhirbase import fhirbase


class ResearchSubject(fhirbase):
    """
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices,
    therapies and other interventional and investigative techniques.  A
    ResearchStudy involves the gathering of information about human or
    animal subjects.

    Args:
        resourceType: This is a ResearchSubject resource
        identifier: Identifiers assigned to this research study by the sponsor
            or other systems.
        status: The current state of the subject.
        period: The dates the subject began and ended their participation in
            the study.
        study: Reference to the study the subject is participating in.
        individual: The record of the person or animal who is involved in the
            study.
        assignedArm: The name of the arm in the study the subject is expected
            to follow as part of this study.
        actualArm: The name of the arm in the study the subject actually
            followed as part of this study.
        consent: A record of the patient's informed agreement to participate
            in the study.
    """

    __name__ = 'ResearchSubject'

    def __init__(self, dict_values=None):
        self.resourceType = 'ResearchSubject'
        # type: str
        # possible values: ResearchSubject

        self.status = None
        # type: str
        # possible values: candidate, enrolled, active, suspended,
        # withdrawn, completed

        self.period = None
        # reference to Period

        self.study = None
        # reference to Reference: identifier

        self.individual = None
        # reference to Reference: identifier

        self.assignedArm = None
        # type: str

        self.actualArm = None
        # type: str

        self.consent = None
        # reference to Reference: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'candidate', 'enrolled', 'active', 'suspended', 'withdrawn',
                        'completed']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'candidate, enrolled, active, suspended, withdrawn, completed'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchSubject',
             'child_variable': 'individual'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchSubject',
             'child_variable': 'study'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchSubject',
             'child_variable': 'period'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ResearchSubject',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ResearchSubject',
             'child_variable': 'consent'},
        ]
