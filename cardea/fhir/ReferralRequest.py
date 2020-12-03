from .fhirbase import fhirbase


class ReferralRequest(fhirbase):
    """
    Used to record and send details about a request for referral service
    or transfer of a patient to the care of another provider or provider
    organization.

    Args:
        resourceType: This is a ReferralRequest resource
        identifier: Business identifier that uniquely identifies the
            referral/care transfer request instance.
        definition: A protocol, guideline, orderset or other definition that
            is adhered to in whole or in part by this request.
        basedOn: Indicates any plans, proposals or orders that this request is
            intended to satisfy - in whole or in part.
        replaces: Completed or terminated request(s) whose function is taken
            by this new request.
        groupIdentifier: The business identifier of the logical "grouping"
            request/order that this referral is a part of.
        status: The status of the authorization/intention reflected by the
            referral request record.
        intent: Distinguishes the "level" of authorization/demand implicit in
            this request.
        type: An indication of the type of referral (or where applicable the
            type of transfer of care) request.
        priority: An indication of the urgency of referral (or where
            applicable the type of transfer of care) request.
        serviceRequested: The service(s) that is/are requested to be provided
            to the patient.  For example: cardiac pacemaker insertion.
        subject: The patient who is the subject of a referral or transfer of
            care request.
        context: The encounter at which the request for referral or transfer
            of care is initiated.
        occurrenceDateTime: The period of time within which the services
            identified in the referral/transfer of care is specified or required
            to occur.
        occurrencePeriod: The period of time within which the services
            identified in the referral/transfer of care is specified or required
            to occur.
        authoredOn: Date/DateTime of creation for draft requests and date of
            activation for active requests.
        requester: The individual who initiated the request and has
            responsibility for its activation.
        specialty: Indication of the clinical domain or discipline to which
            the referral or transfer of care request is sent.  For example:
            Cardiology Gastroenterology Diabetology.
        recipient: The healthcare provider(s) or provider organization(s)
            who/which is to receive the referral/transfer of care request.
        reasonCode: Description of clinical condition indicating why
            referral/transfer of care is requested.  For example:  Pathological
            Anomalies, Disabled (physical or mental),  Behavioral Management.
        reasonReference: Indicates another resource whose existence justifies
            this request.
        description: The reason element gives a short description of why the
            referral is being made, the description expands on this to support a
            more complete clinical summary.
        supportingInfo: Any additional (administrative, financial or clinical)
            information required to support request for referral or transfer of
            care.  For example: Presenting problems/chief complaints Medical
            History Family History Alerts Allergy/Intolerance and Adverse
            Reactions Medications Observations/Assessments (may include cognitive
            and fundtional assessments) Diagnostic Reports Care Plan.
        note: Comments made about the referral request by any of the
            participants.
        relevantHistory: Links to Provenance records for past versions of this
            resource or fulfilling request or event resources that identify key
            state transitions or updates that are likely to be relevant to a user
            looking at the current version of the resource.
    """

    __name__ = 'ReferralRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'ReferralRequest'
        # type: str
        # possible values: ReferralRequest

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.replaces = None
        # type: list
        # reference to Reference: identifier

        self.groupIdentifier = None
        # reference to Identifier

        self.status = None
        # type: str

        self.intent = None
        # type: str

        self.type = None
        # reference to CodeableConcept

        self.priority = None
        # type: str

        self.serviceRequested = None
        # type: list
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.authoredOn = None
        # type: str

        self.requester = None
        # reference to ReferralRequest_Requester

        self.specialty = None
        # reference to CodeableConcept

        self.recipient = None
        # type: list
        # reference to Reference: identifier

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.description = None
        # type: str

        self.supportingInfo = None
        # type: list
        # reference to Reference: identifier

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
            {'parent_entity': 'ReferralRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'recipient'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'serviceRequested'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'specialty'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'replaces'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'definition'},
        ]


class ReferralRequest_Requester(fhirbase):
    """
    Used to record and send details about a request for referral service
    or transfer of a patient to the care of another provider or provider
    organization.

    Args:
        agent: The device, practitioner, etc. who initiated the request.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'ReferralRequest_Requester'

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
             'child_entity': 'ReferralRequest_Requester',
             'child_variable': 'onBehalfOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest_Requester',
             'child_variable': 'agent'},
        ]
