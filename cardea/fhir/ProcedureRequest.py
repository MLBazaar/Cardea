from .fhirbase import fhirbase


class ProcedureRequest(fhirbase):
    """
    A record of a request for diagnostic investigations, treatments, or
    operations to be performed.
    """

    __name__ = 'ProcedureRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'ProcedureRequest'
        """
        This is a ProcedureRequest resource

        type: string
        possible values: ProcedureRequest
        """

        self.definition = None
        """
        Protocol or definition followed by this request.

        type: array
        reference to Reference: identifier
        """

        self.basedOn = None
        """
        Plan/proposal/order fulfilled by this request.

        type: array
        reference to Reference: identifier
        """

        self.replaces = None
        """
        The request takes the place of the referenced completed or terminated
        request(s).

        type: array
        reference to Reference: identifier
        """

        self.requisition = None
        """
        A shared identifier common to all procedure or diagnostic requests
        that were authorized more or less simultaneously by a single author,
        representing the composite or group identifier.

        reference to Identifier
        """

        self.status = None
        """
        The status of the order.

        type: string
        """

        self.intent = None
        """
        Whether the request is a proposal, plan, an original order or a reflex
        order.

        type: string
        """

        self.priority = None
        """
        Indicates how quickly the ProcedureRequest should be addressed with
        respect to other requests.

        type: string
        """

        self.doNotPerform = None
        """
        Set this to true if the record is saying that the procedure should NOT
        be performed.

        type: boolean
        """

        self.category = None
        """
        A code that classifies the procedure for searching, sorting and
        display purposes (e.g. "Surgical Procedure").

        type: array
        reference to CodeableConcept
        """

        self.code = None
        """
        A code that identifies a particular procedure, diagnostic
        investigation, or panel of investigations, that have been requested.

        reference to CodeableConcept
        """

        self.subject = None
        """
        On whom or what the procedure or diagnostic is to be performed. This
        is usually a human patient, but can also be requested on animals,
        groups of humans or animals, devices such as dialysis machines, or
        even locations (typically for environmental scans).

        reference to Reference: identifier
        """

        self.context = None
        """
        An encounter or episode of care that provides additional information
        about the healthcare context in which this request is made.

        reference to Reference: identifier
        """

        self.occurrenceDateTime = None
        """
        The date/time at which the diagnostic testing should occur.

        type: string
        """

        self.occurrencePeriod = None
        """
        The date/time at which the diagnostic testing should occur.

        reference to Period
        """

        self.occurrenceTiming = None
        """
        The date/time at which the diagnostic testing should occur.

        reference to Timing
        """

        self.asNeededBoolean = None
        """
        If a CodeableConcept is present, it indicates the pre-condition for
        performing the procedure.  For example "pain", "on flare-up", etc.

        type: boolean
        """

        self.asNeededCodeableConcept = None
        """
        If a CodeableConcept is present, it indicates the pre-condition for
        performing the procedure.  For example "pain", "on flare-up", etc.

        reference to CodeableConcept
        """

        self.authoredOn = None
        """
        When the request transitioned to being actionable.

        type: string
        """

        self.requester = None
        """
        The individual who initiated the request and has responsibility for
        its activation.

        reference to ProcedureRequest_Requester
        """

        self.performerType = None
        """
        Desired type of performer for doing the diagnostic testing.

        reference to CodeableConcept
        """

        self.performer = None
        """
        The desired perfomer for doing the diagnostic testing.  For example,
        the surgeon, dermatopathologist, endoscopist, etc.

        reference to Reference: identifier
        """

        self.reasonCode = None
        """
        An explanation or justification for why this diagnostic investigation
        is being requested in coded or textual form.   This is often for
        billing purposes.  May relate to the resources referred to in
        supportingInformation.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Indicates another resource that provides a justification for why this
        diagnostic investigation is being requested.   May relate to the
        resources referred to in supportingInformation.

        type: array
        reference to Reference: identifier
        """

        self.supportingInfo = None
        """
        Additional clinical information about the patient or specimen that may
        influence the procedure or diagnostics or their interpretations.
        This information includes diagnosis, clinical findings and other
        observations.  In laboratory ordering these are typically referred to
        as "ask at order entry questions (AOEs)".  This includes observations
        explicitly requested by the producer (filler) to provide context or
        supporting information needed to complete the order. For example,
        reporting the amount of inspired oxygen for blood gas measurements.

        type: array
        reference to Reference: identifier
        """

        self.specimen = None
        """
        One or more specimens that the laboratory procedure will use.

        type: array
        reference to Reference: identifier
        """

        self.bodySite = None
        """
        Anatomic location where the procedure should be performed. This is the
        target site.

        type: array
        reference to CodeableConcept
        """

        self.note = None
        """
        Any other notes and comments made about the service request. For
        example, letting provider know that "patient hates needles" or other
        provider instructions.

        type: array
        reference to Annotation
        """

        self.relevantHistory = None
        """
        Key events in the history of the request.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Identifiers assigned to this order instance by the orderer and/or the
        receiver and/or order fulfiller.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'requisition'},

            {'parent_entity': 'ProcedureRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'definition'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'performerType'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'asNeededCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'specimen'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'replaces'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'occurrenceTiming'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'performer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ProcedureRequest',
             'child_variable': 'bodySite'},
        ]


class ProcedureRequest_Requester(fhirbase):
    """
    A record of a request for diagnostic investigations, treatments, or
    operations to be performed.
    """

    __name__ = 'ProcedureRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        """
        The device, practitioner or organization who initiated the request.

        reference to Reference: identifier
        """

        self.onBehalfOf = None
        """
        The organization the device or practitioner was acting on behalf of.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest_Requester',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ProcedureRequest_Requester',
             'child_variable': 'agent'},
        ]
