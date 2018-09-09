from .fhirbase import fhirbase


class ResearchSubject(fhirbase):
    """A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices,
    therapies and other interventional and investigative techniques.  A
    ResearchStudy involves the gathering of information about human or
    animal subjects.
    """

    def __init__(self, dict_values=None):
        # this is a researchsubject resource
        self.resourceType = 'ResearchSubject'
        # type = string
        # possible values: ResearchSubject

        # the current state of the subject.
        self.status = None
        # type = string
        # possible values: candidate, enrolled, active, suspended,
        # withdrawn, completed

        # the dates the subject began and ended their participation in the study.
        self.period = None
        # reference to Period: Period

        # reference to the study the subject is participating in.
        self.study = None
        # reference to Reference: identifier

        # the record of the person or animal who is involved in the study.
        self.individual = None
        # reference to Reference: identifier

        # the name of the arm in the study the subject is expected to follow as
        # part of this study.
        self.assignedArm = None
        # type = string

        # the name of the arm in the study the subject actually followed as part
        # of this study.
        self.actualArm = None
        # type = string

        # a record of the patient's informed agreement to participate in the
        # study.
        self.consent = None
        # reference to Reference: identifier

        # identifiers assigned to this research study by the sponsor or other
        # systems.
        self.identifier = None
        # reference to Identifier: Identifier

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
