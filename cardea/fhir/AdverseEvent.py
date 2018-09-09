from .fhirbase import fhirbase


class AdverseEvent(fhirbase):
    """Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or
    other healthcare setting factors that requires additional monitoring,
    treatment, or hospitalization, or that results in death.
    """

    __name__ = 'AdverseEvent'

    def __init__(self, dict_values=None):
        # this is a adverseevent resource
        self.resourceType = 'AdverseEvent'
        # type = string
        # possible values: AdverseEvent

        # the type of event which is important to characterize what occurred and
        # caused harm to the subject, or had the potential to cause harm to the
        # subject.
        self.category = None
        # type = string
        # possible values: AE, PAE

        # this element defines the specific type of event that occurred or that
        # was prevented from occurring.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # this subject or group impacted by the event.  with a prospective adverse
        # event, there will be no subject as the adverse event was prevented.
        self.subject = None
        # reference to Reference: identifier

        # the date (and perhaps time) when the adverse event occurred.
        self.date = None
        # type = string

        # includes information about the reaction that occurred as a result of
        # exposure to a substance (for example, a drug or a chemical).
        self.reaction = None
        # type = array
        # reference to Reference: identifier

        # the information about where the adverse event occurred.
        self.location = None
        # reference to Reference: identifier

        # describes the seriousness or severity of the adverse event.
        self.seriousness = None
        # reference to CodeableConcept: CodeableConcept

        # describes the type of outcome from the adverse event.
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # information on who recorded the adverse event.  may be the patient or a
        # practitioner.
        self.recorder = None
        # reference to Reference: identifier

        # parties that may or should contribute or have contributed information to
        # the act. such information includes information leading to the decision
        # to perform the act and how to perform the act (e.g. consultant),
        # information that the act itself seeks to reveal (e.g. informant of
        # clinical history), or information about what act was performed (e.g.
        # informant witness).
        self.eventParticipant = None
        # reference to Reference: identifier

        # describes the adverse event in text.
        self.description = None
        # type = string

        # describes the entity that is suspected to have caused the adverse event.
        self.suspectEntity = None
        # type = array
        # reference to AdverseEvent_SuspectEntity: AdverseEvent_SuspectEntity

        # adverseevent.subjectmedicalhistory.
        self.subjectMedicalHistory = None
        # type = array
        # reference to Reference: identifier

        # adverseevent.referencedocument.
        self.referenceDocument = None
        # type = array
        # reference to Reference: identifier

        # adverseevent.study.
        self.study = None
        # type = array
        # reference to Reference: identifier

        # the identifier(s) of this adverse event that are assigned by business
        # processes and/or used to refer to it when a direct url reference to the
        # resource itsefl is not appropriate.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.category is not None:
            for value in self.category:
                if value is not None and value.lower() not in [
                        'ae', 'pae']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'AE, PAE'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'recorder'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'type'},

            {'parent_entity': 'AdverseEvent_SuspectEntity',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'suspectEntity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'outcome'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'reaction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'eventParticipant'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'seriousness'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'subjectMedicalHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'referenceDocument'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'study'},
        ]


class AdverseEvent_SuspectEntity(fhirbase):
    """Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or
    other healthcare setting factors that requires additional monitoring,
    treatment, or hospitalization, or that results in death.
    """

    __name__ = 'AdverseEvent_SuspectEntity'

    def __init__(self, dict_values=None):
        # identifies the actual instance of what caused the adverse event.  may be
        # a substance, medication, medication administration, medication statement
        # or a device.
        self.instance = None
        # reference to Reference: identifier

        # causality1 | causality2.
        self.causality = None
        # type = string
        # possible values: causality1, causality2

        # assess1 | assess2.
        self.causalityAssessment = None
        # reference to CodeableConcept: CodeableConcept

        # adverseevent.suspectentity.causalityproductrelatedness.
        self.causalityProductRelatedness = None
        # type = string

        # method1 | method2.
        self.causalityMethod = None
        # reference to CodeableConcept: CodeableConcept

        # adverseevent.suspectentity.causalityauthor.
        self.causalityAuthor = None
        # reference to Reference: identifier

        # result1 | result2.
        self.causalityResult = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.causality is not None:
            for value in self.causality:
                if value is not None and value.lower() not in [
                        'causality1', 'causality2']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'causality1, causality2'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityResult'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'instance'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityAssessment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityAuthor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityMethod'},
        ]
