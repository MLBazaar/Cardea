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
    """

    __name__ = 'ResearchSubject'

    def __init__(self, dict_values=None):
        self.resourceType = 'ResearchSubject'
        """
        This is a ResearchSubject resource

        type: string
        possible values: ResearchSubject
        """

        self.status = None
        """
        The current state of the subject.

        type: string
        possible values: candidate, enrolled, active, suspended,
        withdrawn, completed
        """

        self.period = None
        """
        The dates the subject began and ended their participation in the
        study.

        reference to Period
        """

        self.study = None
        """
        Reference to the study the subject is participating in.

        reference to Reference: identifier
        """

        self.individual = None
        """
        The record of the person or animal who is involved in the study.

        reference to Reference: identifier
        """

        self.assignedArm = None
        """
        The name of the arm in the study the subject is expected to follow as
        part of this study.

        type: string
        """

        self.actualArm = None
        """
        The name of the arm in the study the subject actually followed as part
        of this study.

        type: string
        """

        self.consent = None
        """
        A record of the patient's informed agreement to participate in the
        study.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifiers assigned to this research study by the sponsor or other
        systems.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'consent'},

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
             'child_variable': 'study'},
        ]
