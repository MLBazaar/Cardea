from .fhirbase import fhirbase


class AdverseEvent(fhirbase):
    """
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or
    other healthcare setting factors that requires additional monitoring,
    treatment, or hospitalization, or that results in death.

    Args:
        resourceType: This is a AdverseEvent resource
        identifier: The identifier(s) of this adverse event that are assigned
            by business processes and/or used to refer to it when a direct URL
            reference to the resource itsefl is not appropriate.
        category: The type of event which is important to characterize what
            occurred and caused harm to the subject, or had the potential to cause
            harm to the subject.
        type: This element defines the specific type of event that occurred or
            that was prevented from occurring.
        subject: This subject or group impacted by the event.  With a
            prospective adverse event, there will be no subject as the adverse
            event was prevented.
        date: The date (and perhaps time) when the adverse event occurred.
        reaction: Includes information about the reaction that occurred as a
            result of exposure to a substance (for example, a drug or a chemical).
        location: The information about where the adverse event occurred.
        seriousness: Describes the seriousness or severity of the adverse
            event.
        outcome: Describes the type of outcome from the adverse event.
        recorder: Information on who recorded the adverse event.  May be the
            patient or a practitioner.
        eventParticipant: Parties that may or should contribute or have
            contributed information to the Act. Such information includes
            information leading to the decision to perform the Act and how to
            perform the Act (e.g. consultant), information that the Act itself
            seeks to reveal (e.g. informant of clinical history), or information
            about what Act was performed (e.g. informant witness).
        description: Describes the adverse event in text.
        suspectEntity: Describes the entity that is suspected to have caused
            the adverse event.
        subjectMedicalHistory: AdverseEvent.subjectMedicalHistory.
        referenceDocument: AdverseEvent.referenceDocument.
        study: AdverseEvent.study.
    """

    __name__ = 'AdverseEvent'

    def __init__(self, dict_values=None):
        self.resourceType = 'AdverseEvent'
        # type: str
        # possible values: AdverseEvent

        self.category = None
        # type: str
        # possible values: AE, PAE

        self.type = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.date = None
        # type: str

        self.reaction = None
        # type: list
        # reference to Reference: identifier

        self.location = None
        # reference to Reference: identifier

        self.seriousness = None
        # reference to CodeableConcept

        self.outcome = None
        # reference to CodeableConcept

        self.recorder = None
        # reference to Reference: identifier

        self.eventParticipant = None
        # reference to Reference: identifier

        self.description = None
        # type: str

        self.suspectEntity = None
        # type: list
        # reference to AdverseEvent_SuspectEntity

        self.subjectMedicalHistory = None
        # type: list
        # reference to Reference: identifier

        self.referenceDocument = None
        # type: list
        # reference to Reference: identifier

        self.study = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.category is not None:
            for value in self.category:
                if value is not None and value.lower() not in [
                        'ae', 'pae']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'AE, PAE'))

    def get_relationships(self):

        return [
            {'parent_entity': 'AdverseEvent_SuspectEntity',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'suspectEntity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'subjectMedicalHistory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'outcome'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'reaction'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'recorder'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'study'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'referenceDocument'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'eventParticipant'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'seriousness'},
        ]


class AdverseEvent_SuspectEntity(fhirbase):
    """
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or
    other healthcare setting factors that requires additional monitoring,
    treatment, or hospitalization, or that results in death.

    Args:
        instance: Identifies the actual instance of what caused the adverse
            event.  May be a substance, medication, medication administration,
            medication statement or a device.
        causality: causality1 | causality2.
        causalityAssessment: assess1 | assess2.
        causalityProductRelatedness:
            AdverseEvent.suspectEntity.causalityProductRelatedness.
        causalityMethod: method1 | method2.
        causalityAuthor: AdverseEvent.suspectEntity.causalityAuthor.
        causalityResult: result1 | result2.
    """

    __name__ = 'AdverseEvent_SuspectEntity'

    def __init__(self, dict_values=None):
        self.instance = None
        # reference to Reference: identifier

        self.causality = None
        # type: str
        # possible values: causality1, causality2

        self.causalityAssessment = None
        # reference to CodeableConcept

        self.causalityProductRelatedness = None
        # type: str

        self.causalityMethod = None
        # reference to CodeableConcept

        self.causalityAuthor = None
        # reference to Reference: identifier

        self.causalityResult = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.causality is not None:
            for value in self.causality:
                if value is not None and value.lower() not in [
                        'causality1', 'causality2']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'causality1, causality2'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityAuthor'},

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

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityMethod'},
        ]
