from .fhirbase import fhirbase


class ReferralRequest(fhirbase):
    """Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organization.
    """

    def __init__(self, dict_values=None):
        # this is a referralrequest resource
        self.resourceType = 'ReferralRequest'
        # type = string
        # possible values: ReferralRequest

        # a protocol, guideline, orderset or other definition that is adhered to
        # in whole or in part by this request.
        self.definition = None
        # type = array
        # reference to Reference: identifier

        # indicates any plans, proposals or orders that this request is intended
        # to satisfy - in whole or in part.
        self.basedOn = None
        # type = array
        # reference to Reference: identifier

        # completed or terminated request(s) whose function is taken by this new
        # request.
        self.replaces = None
        # type = array
        # reference to Reference: identifier

        # the business identifier of the logical "grouping" request/order that
        # this referral is a part of.
        self.groupIdentifier = None
        # reference to Identifier: Identifier

        # the status of the authorization/intention reflected by the referral
        # request record.
        self.status = None
        # type = string

        # distinguishes the "level" of authorization/demand implicit in this
        # request.
        self.intent = None
        # type = string

        # an indication of the type of referral (or where applicable the type of
        # transfer of care) request.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # an indication of the urgency of referral (or where applicable the type
        # of transfer of care) request.
        self.priority = None
        # type = string

        # the service(s) that is/are requested to be provided to the patient.  for
        # example: cardiac pacemaker insertion.
        self.serviceRequested = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the patient who is the subject of a referral or transfer of care
        # request.
        self.subject = None
        # reference to Reference: identifier

        # the encounter at which the request for referral or transfer of care is
        # initiated.
        self.context = None
        # reference to Reference: identifier

        # the period of time within which the services identified in the
        # referral/transfer of care is specified or required to occur.
        self.occurrenceDateTime = None
        # type = string

        # the period of time within which the services identified in the
        # referral/transfer of care is specified or required to occur.
        self.occurrencePeriod = None
        # reference to Period: Period

        # date/datetime of creation for draft requests and date of activation for
        # active requests.
        self.authoredOn = None
        # type = string

        # the individual who initiated the request and has responsibility for its
        # activation.
        self.requester = None
        # reference to ReferralRequest_Requester: ReferralRequest_Requester

        # indication of the clinical domain or discipline to which the referral or
        # transfer of care request is sent.  for example: cardiology
        # gastroenterology diabetology.
        self.specialty = None
        # reference to CodeableConcept: CodeableConcept

        # the healthcare provider(s) or provider organization(s) who/which is to
        # receive the referral/transfer of care request.
        self.recipient = None
        # type = array
        # reference to Reference: identifier

        # description of clinical condition indicating why referral/transfer of
        # care is requested.  for example:  pathological anomalies, disabled
        # (physical or mental),  behavioral management.
        self.reasonCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates another resource whose existence justifies this request.
        self.reasonReference = None
        # type = array
        # reference to Reference: identifier

        # the reason element gives a short description of why the referral is
        # being made, the description expands on this to support a more complete
        # clinical summary.
        self.description = None
        # type = string

        # any additional (administrative, financial or clinical) information
        # required to support request for referral or transfer of care.  for
        # example: presenting problems/chief complaints medical history family
        # history alerts allergy/intolerance and adverse reactions medications
        # observations/assessments (may include cognitive and fundtional
        # assessments) diagnostic reports care plan.
        self.supportingInfo = None
        # type = array
        # reference to Reference: identifier

        # comments made about the referral request by any of the participants.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # links to provenance records for past versions of this resource or
        # fulfilling request or event resources that identify key state
        # transitions or updates that are likely to be relevant to a user looking
        # at the current version of the resource.
        self.relevantHistory = None
        # type = array
        # reference to Reference: identifier

        # business identifier that uniquely identifies the referral/care transfer
        # request instance.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'replaces'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'serviceRequested'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'definition'},

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
             'child_variable': 'recipient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'relevantHistory'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'context'},

            {'parent_entity': 'ReferralRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'ReferralRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'supportingInfo'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ReferralRequest',
             'child_variable': 'reasonReference'},
        ]


class ReferralRequest_Requester(fhirbase):
    """Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organization.
    """

    def __init__(self, dict_values=None):
        # the device, practitioner, etc. who initiated the request.
        self.agent = None
        # reference to Reference: identifier

        # the organization the device or practitioner was acting on behalf of.
        self.onBehalfOf = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

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
