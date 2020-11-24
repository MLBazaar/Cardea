from .fhirbase import fhirbase


class ProcedureRequest(fhirbase):
    """
    A record of a request for diagnostic investigations, treatments, or
    operations to be performed.

    Args:
        resourceType: This is a ProcedureRequest resource
        identifier: Identifiers assigned to this order instance by the orderer
            and/or the receiver and/or order fulfiller.
        definition: Protocol or definition followed by this request.
        basedOn: Plan/proposal/order fulfilled by this request.
        replaces: The request takes the place of the referenced completed or
            terminated request(s).
        requisition: A shared identifier common to all procedure or diagnostic
            requests that were authorized more or less simultaneously by a single
            author, representing the composite or group identifier.
        status: The status of the order.
        intent: Whether the request is a proposal, plan, an original order or
            a reflex order.
        priority: Indicates how quickly the ProcedureRequest should be
            addressed with respect to other requests.
        doNotPerform: Set this to true if the record is saying that the
            procedure should NOT be performed.
        category: A code that classifies the procedure for searching, sorting
            and display purposes (e.g. "Surgical Procedure").
        code: A code that identifies a particular procedure, diagnostic
            investigation, or panel of investigations, that have been requested.
        subject: On whom or what the procedure or diagnostic is to be
            performed. This is usually a human patient, but can also be requested
            on animals, groups of humans or animals, devices such as dialysis
            machines, or even locations (typically for environmental scans).
        context: An encounter or episode of care that provides additional
            information about the healthcare context in which this request is
            made.
        occurrenceDateTime: The date/time at which the diagnostic testing
            should occur.
        occurrencePeriod: The date/time at which the diagnostic testing should
            occur.
        occurrenceTiming: The date/time at which the diagnostic testing should
            occur.
        asNeededBoolean: If a CodeableConcept is present, it indicates the
            pre-condition for performing the procedure.  For example "pain", "on
            flare-up", etc.
        asNeededCodeableConcept: If a CodeableConcept is present, it indicates
            the pre-condition for performing the procedure.  For example "pain",
            "on flare-up", etc.
        authoredOn: When the request transitioned to being actionable.
        requester: The individual who initiated the request and has
            responsibility for its activation.
        performerType: Desired type of performer for doing the diagnostic
            testing.
        performer: The desired perfomer for doing the diagnostic testing.  For
            example, the surgeon, dermatopathologist, endoscopist, etc.
        reasonCode: An explanation or justification for why this diagnostic
            investigation is being requested in coded or textual form.   This is
            often for billing purposes.  May relate to the resources referred to
            in supportingInformation.
        reasonReference: Indicates another resource that provides a
            justification for why this diagnostic investigation is being
            requested.   May relate to the resources referred to in
            supportingInformation.
        supportingInfo: Additional clinical information about the patient or
            specimen that may influence the procedure or diagnostics or their
            interpretations.     This information includes diagnosis, clinical
            findings and other observations.  In laboratory ordering these are
            typically referred to as "ask at order entry questions (AOEs)".  This
            includes observations explicitly requested by the producer (filler) to
            provide context or supporting information needed to complete the
            order. For example,  reporting the amount of inspired oxygen for blood
            gas measurements.
        specimen: One or more specimens that the laboratory procedure will
            use.
        bodySite: Anatomic location where the procedure should be performed.
            This is the target site.
        note: Any other notes and comments made about the service request. For
            example, letting provider know that "patient hates needles" or other
            provider instructions.
        relevantHistory: Key events in the history of the request.
    """

    __name__ = 'ProcedureRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'ProcedureRequest'
        # type: str
        # possible values: ProcedureRequest

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.replaces = None
        # type: list
        # reference to Reference: identifier

        self.requisition = None
        # reference to Identifier

        self.status = None
        # type: str

        self.intent = None
        # type: str

        self.priority = None
        # type: str

        self.doNotPerform = None
        # type: bool

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.code = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.occurrenceTiming = None
        # reference to Timing

        self.asNeededBoolean = None
        # type: bool

        self.asNeededCodeableConcept = None
        # reference to CodeableConcept

        self.authoredOn = None
        # type: str

        self.requester = None
        # reference to ProcedureRequest_Requester

        self.performerType = None
        # reference to CodeableConcept

        self.performer = None
        # reference to Reference: identifier

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.supportingInfo = None
        # type: list
        # reference to Reference: identifier

        self.specimen = None
        # type: list
        # reference to Reference: identifier

        self.bodySite = None
        # type: list
        # reference to CodeableConcept

        self.note = None
        # type: list
        # reference to Annotation

        self.relevantHistory = None
        # type: list
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'performer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'asNeededCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'performerType'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'specimen'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'requisition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'context'},

            {'parent_entity': 'ProcedureRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'note'},
        ]


class ProcedureRequest_Requester(fhirbase):
    """
    A record of a request for diagnostic investigations, treatments, or
    operations to be performed.

    Args:
        agent: The device, practitioner or organization who initiated the
            request.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'ProcedureRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        # reference to Reference: identifier

        self.onBehalfOf = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest_Requester',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest_Requester',
             'child_variable': 'onBehalfOf'},
        ]
