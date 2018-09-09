from .fhirbase import fhirbase


class AdverseEvent(fhirbase):
    """
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or
    other healthcare setting factors that requires additional monitoring,
    treatment, or hospitalization, or that results in death.
    """

    __name__ = 'AdverseEvent'

    def __init__(self, dict_values=None):
        self.resourceType = 'AdverseEvent'
        """
        This is a AdverseEvent resource

        type: string
        possible values: AdverseEvent
        """

        self.category = None
        """
        The type of event which is important to characterize what occurred and
        caused harm to the subject, or had the potential to cause harm to the
        subject.

        type: string
        possible values: AE, PAE
        """

        self.type = None
        """
        This element defines the specific type of event that occurred or that
        was prevented from occurring.

        reference to CodeableConcept
        """

        self.subject = None
        """
        This subject or group impacted by the event.  With a prospective
        adverse event, there will be no subject as the adverse event was
        prevented.

        reference to Reference: identifier
        """

        self.date = None
        """
        The date (and perhaps time) when the adverse event occurred.

        type: string
        """

        self.reaction = None
        """
        Includes information about the reaction that occurred as a result of
        exposure to a substance (for example, a drug or a chemical).

        type: array
        reference to Reference: identifier
        """

        self.location = None
        """
        The information about where the adverse event occurred.

        reference to Reference: identifier
        """

        self.seriousness = None
        """
        Describes the seriousness or severity of the adverse event.

        reference to CodeableConcept
        """

        self.outcome = None
        """
        Describes the type of outcome from the adverse event.

        reference to CodeableConcept
        """

        self.recorder = None
        """
        Information on who recorded the adverse event.  May be the patient or
        a practitioner.

        reference to Reference: identifier
        """

        self.eventParticipant = None
        """
        Parties that may or should contribute or have contributed information
        to the Act. Such information includes information leading to the
        decision to perform the Act and how to perform the Act (e.g.
        consultant), information that the Act itself seeks to reveal (e.g.
        informant of clinical history), or information about what Act was
        performed (e.g. informant witness).

        reference to Reference: identifier
        """

        self.description = None
        """
        Describes the adverse event in text.

        type: string
        """

        self.suspectEntity = None
        """
        Describes the entity that is suspected to have caused the adverse
        event.

        type: array
        reference to AdverseEvent_SuspectEntity
        """

        self.subjectMedicalHistory = None
        """
        AdverseEvent.subjectMedicalHistory.

        type: array
        reference to Reference: identifier
        """

        self.referenceDocument = None
        """
        AdverseEvent.referenceDocument.

        type: array
        reference to Reference: identifier
        """

        self.study = None
        """
        AdverseEvent.study.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        The identifier(s) of this adverse event that are assigned by business
        processes and/or used to refer to it when a direct URL reference to
        the resource itsefl is not appropriate.

        reference to Identifier
        """

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
            {'parent_entity': 'AdverseEvent_SuspectEntity',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'suspectEntity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'referenceDocument'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'recorder'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'subjectMedicalHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'reaction'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'study'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'location'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'seriousness'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'outcome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'type'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent',
             'child_variable': 'eventParticipant'},
        ]


class AdverseEvent_SuspectEntity(fhirbase):
    """
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or
    other healthcare setting factors that requires additional monitoring,
    treatment, or hospitalization, or that results in death.
    """

    __name__ = 'AdverseEvent_SuspectEntity'

    def __init__(self, dict_values=None):
        self.instance = None
        """
        Identifies the actual instance of what caused the adverse event.  May
        be a substance, medication, medication administration, medication
        statement or a device.

        reference to Reference: identifier
        """

        self.causality = None
        """
        causality1 | causality2.

        type: string
        possible values: causality1, causality2
        """

        self.causalityAssessment = None
        """
        assess1 | assess2.

        reference to CodeableConcept
        """

        self.causalityProductRelatedness = None
        """
        AdverseEvent.suspectEntity.causalityProductRelatedness.

        type: string
        """

        self.causalityMethod = None
        """
        method1 | method2.

        reference to CodeableConcept
        """

        self.causalityAuthor = None
        """
        AdverseEvent.suspectEntity.causalityAuthor.

        reference to Reference: identifier
        """

        self.causalityResult = None
        """
        result1 | result2.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityAuthor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityResult'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityMethod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'causalityAssessment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'AdverseEvent_SuspectEntity',
             'child_variable': 'instance'},
        ]
