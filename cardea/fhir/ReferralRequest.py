from .fhirbase import fhirbase


class ReferralRequest(fhirbase):
    """
    Used to record and send details about a request for referral service
    or transfer of a patient to the care of another provider or provider
    organization.
    """

    __name__ = 'ReferralRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'ReferralRequest'
        """
        This is a ReferralRequest resource

        type: string
        possible values: ReferralRequest
        """

        self.definition = None
        """
        A protocol, guideline, orderset or other definition that is adhered to
        in whole or in part by this request.

        type: array
        reference to Reference: identifier
        """

        self.basedOn = None
        """
        Indicates any plans, proposals or orders that this request is intended
        to satisfy - in whole or in part.

        type: array
        reference to Reference: identifier
        """

        self.replaces = None
        """
        Completed or terminated request(s) whose function is taken by this new
        request.

        type: array
        reference to Reference: identifier
        """

        self.groupIdentifier = None
        """
        The business identifier of the logical "grouping" request/order that
        this referral is a part of.

        reference to Identifier
        """

        self.status = None
        """
        The status of the authorization/intention reflected by the referral
        request record.

        type: string
        """

        self.intent = None
        """
        Distinguishes the "level" of authorization/demand implicit in this
        request.

        type: string
        """

        self.type = None
        """
        An indication of the type of referral (or where applicable the type of
        transfer of care) request.

        reference to CodeableConcept
        """

        self.priority = None
        """
        An indication of the urgency of referral (or where applicable the type
        of transfer of care) request.

        type: string
        """

        self.serviceRequested = None
        """
        The service(s) that is/are requested to be provided to the patient.
        For example: cardiac pacemaker insertion.

        type: array
        reference to CodeableConcept
        """

        self.subject = None
        """
        The patient who is the subject of a referral or transfer of care
        request.

        reference to Reference: identifier
        """

        self.context = None
        """
        The encounter at which the request for referral or transfer of care is
        initiated.

        reference to Reference: identifier
        """

        self.occurrenceDateTime = None
        """
        The period of time within which the services identified in the
        referral/transfer of care is specified or required to occur.

        type: string
        """

        self.occurrencePeriod = None
        """
        The period of time within which the services identified in the
        referral/transfer of care is specified or required to occur.

        reference to Period
        """

        self.authoredOn = None
        """
        Date/DateTime of creation for draft requests and date of activation
        for active requests.

        type: string
        """

        self.requester = None
        """
        The individual who initiated the request and has responsibility for
        its activation.

        reference to ReferralRequest_Requester
        """

        self.specialty = None
        """
        Indication of the clinical domain or discipline to which the referral
        or transfer of care request is sent.  For example: Cardiology
        Gastroenterology Diabetology.

        reference to CodeableConcept
        """

        self.recipient = None
        """
        The healthcare provider(s) or provider organization(s) who/which is to
        receive the referral/transfer of care request.

        type: array
        reference to Reference: identifier
        """

        self.reasonCode = None
        """
        Description of clinical condition indicating why referral/transfer of
        care is requested.  For example:  Pathological Anomalies, Disabled
        (physical or mental),  Behavioral Management.

        type: array
        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Indicates another resource whose existence justifies this request.

        type: array
        reference to Reference: identifier
        """

        self.description = None
        """
        The reason element gives a short description of why the referral is
        being made, the description expands on this to support a more complete
        clinical summary.

        type: string
        """

        self.supportingInfo = None
        """
        Any additional (administrative, financial or clinical) information
        required to support request for referral or transfer of care.  For
        example: Presenting problems/chief complaints Medical History Family
        History Alerts Allergy/Intolerance and Adverse Reactions Medications
        Observations/Assessments (may include cognitive and fundtional
        assessments) Diagnostic Reports Care Plan.

        type: array
        reference to Reference: identifier
        """

        self.note = None
        """
        Comments made about the referral request by any of the participants.

        type: array
        reference to Annotation
        """

        self.relevantHistory = None
        """
        Links to Provenance records for past versions of this resource or
        fulfilling request or event resources that identify key state
        transitions or updates that are likely to be relevant to a user
        looking at the current version of the resource.

        type: array
        reference to Reference: identifier
        """

        self.identifier = None
        """
        Business identifier that uniquely identifies the referral/care
        transfer request instance.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'recipient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'definition'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'replaces'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'specialty'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'ReferralRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'serviceRequested'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'reasonCode'},
        ]


class ReferralRequest_Requester(fhirbase):
    """
    Used to record and send details about a request for referral service
    or transfer of a patient to the care of another provider or provider
    organization.
    """

    __name__ = 'ReferralRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        """
        The device, practitioner, etc. who initiated the request.

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
             'child_entity': 'ReferralRequest_Requester',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest_Requester',
             'child_variable': 'onBehalfOf'},
        ]
