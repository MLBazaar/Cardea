from .fhirbase import fhirbase


class Claim(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim'

    def __init__(self, dict_values=None):
        self.resourceType = 'Claim'
        """
        This is a Claim resource

        type: string
        possible values: Claim
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.type = None
        """
        The category of claim, eg, oral, pharmacy, vision, insitutional,
        professional.

        reference to CodeableConcept
        """

        self.subType = None
        """
        A finer grained suite of claim subtype codes which may convey
        Inpatient vs Outpatient and/or a specialty service. In the US the
        BillType.

        type: array
        reference to CodeableConcept
        """

        self.use = None
        """
        Complete (Bill or Claim), Proposed (Pre-Authorization), Exploratory
        (Pre-determination).

        type: string
        possible values: complete, proposed, exploratory, other
        """

        self.patient = None
        """
        Patient Resource.

        reference to Reference: identifier
        """

        self.billablePeriod = None
        """
        The billable period for which charges are being submitted.

        reference to Period
        """

        self.created = None
        """
        The date when the enclosed suite of services were performed or
        completed.

        type: string
        """

        self.enterer = None
        """
        Person who created the invoice/claim/pre-determination or
        pre-authorization.

        reference to Reference: identifier
        """

        self.insurer = None
        """
        The Insurer who is target of the request.

        reference to Reference: identifier
        """

        self.provider = None
        """
        The provider which is responsible for the bill, claim
        pre-determination, pre-authorization.

        reference to Reference: identifier
        """

        self.organization = None
        """
        The organization which is responsible for the bill, claim
        pre-determination, pre-authorization.

        reference to Reference: identifier
        """

        self.priority = None
        """
        Immediate (STAT), best effort (NORMAL), deferred (DEFER).

        reference to CodeableConcept
        """

        self.fundsReserve = None
        """
        In the case of a Pre-Determination/Pre-Authorization the provider may
        request that funds in the amount of the expected Benefit be reserved
        ('Patient' or 'Provider') to pay for the Benefits determined on the
        subsequent claim(s). 'None' explicitly indicates no funds reserving is
        requested.

        reference to CodeableConcept
        """

        self.related = None
        """
        Other claims which are related to this claim such as prior claim
        versions or for related services.

        type: array
        reference to Claim_Related
        """

        self.prescription = None
        """
        Prescription to support the dispensing of Pharmacy or Vision products.

        reference to Reference: identifier
        """

        self.originalPrescription = None
        """
        Original prescription which has been superceded by this prescription
        to support the dispensing of pharmacy services, medications or
        products. For example, a physician may prescribe a medication which
        the pharmacy determines is contraindicated, or for which the patient
        has an intolerance, and therefor issues a new precription for an
        alternate medication which has the same theraputic intent. The
        prescription from the pharmacy becomes the 'prescription' and that
        from the physician becomes the 'original prescription'.

        reference to Reference: identifier
        """

        self.payee = None
        """
        The party to be reimbursed for the services.

        reference to Claim_Payee
        """

        self.referral = None
        """
        The referral resource which lists the date, practitioner, reason and
        other supporting information.

        reference to Reference: identifier
        """

        self.facility = None
        """
        Facility where the services were provided.

        reference to Reference: identifier
        """

        self.careTeam = None
        """
        The members of the team who provided the overall service as well as
        their role and whether responsible and qualifications.

        type: array
        reference to Claim_CareTeam
        """

        self.information = None
        """
        Additional information codes regarding exceptions, special
        considerations, the condition, situation, prior or concurrent issues.
        Often there are mutiple jurisdiction specific valuesets which are
        required.

        type: array
        reference to Claim_Information
        """

        self.diagnosis = None
        """
        List of patient diagnosis for which care is sought.

        type: array
        reference to Claim_Diagnosis
        """

        self.procedure = None
        """
        Ordered list of patient procedures performed to support the
        adjudication.

        type: array
        reference to Claim_Procedure
        """

        self.insurance = None
        """
        Financial instrument by which payment information for health care.

        type: array
        reference to Claim_Insurance
        """

        self.accident = None
        """
        An accident which resulted in the need for healthcare services.

        reference to Claim_Accident
        """

        self.employmentImpacted = None
        """
        The start and optional end dates of when the patient was precluded
        from working due to the treatable condition(s).

        reference to Period
        """

        self.hospitalization = None
        """
        The start and optional end dates of when the patient was confined to a
        treatment center.

        reference to Period
        """

        self.item = None
        """
        First tier of goods and services.

        type: array
        reference to Claim_Item
        """

        self.total = None
        """
        The total value of the claim.

        reference to Money
        """

        self.identifier = None
        """
        The business identifier for the instance: claim number,
        pre-determination or pre-authorization number.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.use is not None:
            for value in self.use:
                if value is not None and value.lower() not in [
                        'complete', 'proposed', 'exploratory', 'other']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'complete, proposed, exploratory, other'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'fundsReserve'},

            {'parent_entity': 'Claim_Payee',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'payee'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'insurer'},

            {'parent_entity': 'Claim_CareTeam',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'careTeam'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'facility'},

            {'parent_entity': 'Claim_Procedure',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'procedure'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'employmentImpacted'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'prescription'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'total'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'Claim_Information',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'information'},

            {'parent_entity': 'Claim_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'insurance'},

            {'parent_entity': 'Claim_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'item'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'subType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'referral'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'organization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'priority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'provider'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'billablePeriod'},

            {'parent_entity': 'Claim_Related',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'related'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'enterer'},

            {'parent_entity': 'Claim_Accident',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'accident'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'originalPrescription'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'identifier'},

            {'parent_entity': 'Claim_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'patient'},
        ]


class Claim_Related(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Related'

    def __init__(self, dict_values=None):
        self.claim = None
        """
        Other claims which are related to this claim such as prior claim
        versions or for related services.

        reference to Reference: identifier
        """

        self.relationship = None
        """
        For example prior or umbrella.

        reference to CodeableConcept
        """

        self.reference = None
        """
        An alternate organizational reference to the case or file to which
        this particular claim pertains - eg Property/Casualy insurer claim #
        or Workers Compensation case # .

        reference to Identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Related',
             'child_variable': 'claim'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Related',
             'child_variable': 'reference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Related',
             'child_variable': 'relationship'},
        ]


class Claim_Payee(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Payee'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Type of Party to be reimbursed: Subscriber, provider, other.

        reference to CodeableConcept
        """

        self.resourceType = None
        """
        organization | patient | practitioner | relatedperson.

        reference to Coding
        """

        self.party = None
        """
        Party to be reimbursed: Subscriber, provider, other.

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
             'child_entity': 'Claim_Payee',
             'child_variable': 'party'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Payee',
             'child_variable': 'type'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Payee',
             'child_variable': 'resourceType'},
        ]


class Claim_CareTeam(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_CareTeam'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        Sequence of the careTeam which serves to order and provide a link.

        type: int
        """

        self.provider = None
        """
        Member of the team who provided the overall service.

        reference to Reference: identifier
        """

        self.responsible = None
        """
        The party who is billing and responsible for the claimed good or
        service rendered to the patient.

        type: boolean
        """

        self.role = None
        """
        The lead, assisting or supervising practitioner and their discipline
        if a multidisiplinary team.

        reference to CodeableConcept
        """

        self.qualification = None
        """
        The qualification which is applicable for this service.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'qualification'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'provider'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'role'},
        ]


class Claim_Information(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Information'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        Sequence of the information element which serves to provide a link.

        type: int
        """

        self.category = None
        """
        The general class of the information supplied: information; exception;
        accident, employment; onset, etc.

        reference to CodeableConcept
        """

        self.code = None
        """
        System and code pertaining to the specific information regarding
        special conditions relating to the setting, treatment or patient  for
        which care is sought which may influence the adjudication.

        reference to CodeableConcept
        """

        self.timingDate = None
        """
        The date when or period to which this information refers.

        type: string
        """

        self.timingPeriod = None
        """
        The date when or period to which this information refers.

        reference to Period
        """

        self.valueString = None
        """
        Additional data or information such as resources, documents, images
        etc. including references to the data or the actual inclusion of the
        data.

        type: string
        """

        self.valueQuantity = None
        """
        Additional data or information such as resources, documents, images
        etc. including references to the data or the actual inclusion of the
        data.

        reference to Quantity
        """

        self.valueAttachment = None
        """
        Additional data or information such as resources, documents, images
        etc. including references to the data or the actual inclusion of the
        data.

        reference to Attachment
        """

        self.valueReference = None
        """
        Additional data or information such as resources, documents, images
        etc. including references to the data or the actual inclusion of the
        data.

        reference to Reference: identifier
        """

        self.reason = None
        """
        For example, provides the reason for: the additional stay, or missing
        tooth or any other situation where a reason code is required in
        addition to the content.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'category'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Information',
             'child_variable': 'valueReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'reason'},
        ]


class Claim_Diagnosis(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Diagnosis'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        Sequence of diagnosis which serves to provide a link.

        type: int
        """

        self.diagnosisCodeableConcept = None
        """
        The diagnosis.

        reference to CodeableConcept
        """

        self.diagnosisReference = None
        """
        The diagnosis.

        reference to Reference: identifier
        """

        self.type = None
        """
        The type of the Diagnosis, for example: admitting, primary, secondary,
        discharge.

        type: array
        reference to CodeableConcept
        """

        self.packageCode = None
        """
        The package billing code, for example DRG, based on the assigned
        grouping code system.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'diagnosisCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'diagnosisReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'packageCode'},
        ]


class Claim_Procedure(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Procedure'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        Sequence of procedures which serves to order and provide a link.

        type: int
        """

        self.date = None
        """
        Date and optionally time the procedure was performed .

        type: string
        """

        self.procedureCodeableConcept = None
        """
        The procedure code.

        reference to CodeableConcept
        """

        self.procedureReference = None
        """
        The procedure code.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Procedure',
             'child_variable': 'procedureCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Procedure',
             'child_variable': 'procedureReference'},
        ]


class Claim_Insurance(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Insurance'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        Sequence of coverage which serves to provide a link and convey
        coordination of benefit order.

        type: int
        """

        self.focal = None
        """
        A flag to indicate that this Coverage is the focus for adjudication.
        The Coverage against which the claim is to be adjudicated.

        type: boolean
        """

        self.coverage = None
        """
        Reference to the program or plan identification, underwriter or payor.

        reference to Reference: identifier
        """

        self.businessArrangement = None
        """
        The contract number of a business agreement which describes the terms
        and conditions.

        type: string
        """

        self.preAuthRef = None
        """
        A list of references from the Insurer to which these services pertain.

        type: array
        """

        self.claimResponse = None
        """
        The Coverages adjudication details.

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
             'child_entity': 'Claim_Insurance',
             'child_variable': 'claimResponse'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Insurance',
             'child_variable': 'coverage'},
        ]


class Claim_Accident(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Accident'

    def __init__(self, dict_values=None):
        self.date = None
        """
        Date of an accident which these services are addressing.

        type: string
        """

        self.type = None
        """
        Type of accident: work, auto, etc.

        reference to CodeableConcept
        """

        self.locationAddress = None
        """
        Accident Place.

        reference to Address
        """

        self.locationReference = None
        """
        Accident Place.

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
             'child_entity': 'Claim_Accident',
             'child_variable': 'locationReference'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Accident',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Accident',
             'child_variable': 'type'},
        ]


class Claim_Item(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Item'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        A service line number.

        type: int
        """

        self.careTeamLinkId = None
        """
        CareTeam applicable for this service or product line.

        type: array
        """

        self.diagnosisLinkId = None
        """
        Diagnosis applicable for this service or product line.

        type: array
        """

        self.procedureLinkId = None
        """
        Procedures applicable for this service or product line.

        type: array
        """

        self.informationLinkId = None
        """
        Exceptions, special conditions and supporting information pplicable
        for this service or product line.

        type: array
        """

        self.revenue = None
        """
        The type of reveneu or cost center providing the product and/or
        service.

        reference to CodeableConcept
        """

        self.category = None
        """
        Health Care Service Type Codes  to identify the classification of
        service or benefits.

        reference to CodeableConcept
        """

        self.service = None
        """
        If this is an actual service or product line, ie. not a Group, then
        use code to indicate the Professional Service or Product supplied (eg.
        CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,RXNorm,ACHI,CCI). If a grouping item
        then use a group code to indicate the type of thing being grouped eg.
        'glasses' or 'compound'.

        reference to CodeableConcept
        """

        self.modifier = None
        """
        Item typification or modifiers codes, eg for Oral whether the
        treatment is cosmetic or associated with TMJ, or for medical whether
        the treatment was outside the clinic or out of office hours.

        type: array
        reference to CodeableConcept
        """

        self.programCode = None
        """
        For programs which require reason codes for the inclusion or covering
        of this billed item under the program or sub-program.

        type: array
        reference to CodeableConcept
        """

        self.servicedDate = None
        """
        The date or dates when the enclosed suite of services were performed
        or completed.

        type: string
        """

        self.servicedPeriod = None
        """
        The date or dates when the enclosed suite of services were performed
        or completed.

        reference to Period
        """

        self.locationCodeableConcept = None
        """
        Where the service was provided.

        reference to CodeableConcept
        """

        self.locationAddress = None
        """
        Where the service was provided.

        reference to Address
        """

        self.locationReference = None
        """
        Where the service was provided.

        reference to Reference: identifier
        """

        self.quantity = None
        """
        The number of repetitions of a service or product.

        reference to Quantity
        """

        self.unitPrice = None
        """
        If the item is a node then this is the fee for the product or service,
        otherwise this is the total of the fees for the children of the group.

        reference to Money
        """

        self.factor = None
        """
        A real number that represents a multiplier used in determining the
        overall value of services delivered and/or goods received. The concept
        of a Factor allows for a discount or surcharge multiplier to be
        applied to a monetary amount.

        type: int
        """

        self.net = None
        """
        The quantity times the unit price for an addittional service or
        product or charge. For example, the formula: unit Quantity * unit
        Price (Cost per Point) * factor Number  * points = net Amount.
        Quantity, factor and points are assumed to be 1 if not supplied.

        reference to Money
        """

        self.udi = None
        """
        List of Unique Device Identifiers associated with this line item.

        type: array
        reference to Reference: identifier
        """

        self.bodySite = None
        """
        Physical service site on the patient (limb, tooth, etc).

        reference to CodeableConcept
        """

        self.subSite = None
        """
        A region or surface of the site, eg. limb region or tooth surface(s).

        type: array
        reference to CodeableConcept
        """

        self.encounter = None
        """
        A billed item may include goods or services provided in multiple
        encounters.

        type: array
        reference to Reference: identifier
        """

        self.detail = None
        """
        Second tier of goods and services.

        type: array
        reference to Claim_Detail
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'programCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'encounter'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'modifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'quantity'},

            {'parent_entity': 'Claim_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'detail'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'subSite'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'bodySite'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'service'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationCodeableConcept'},
        ]


class Claim_Detail(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_Detail'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        A service line number.

        type: int
        """

        self.revenue = None
        """
        The type of reveneu or cost center providing the product and/or
        service.

        reference to CodeableConcept
        """

        self.category = None
        """
        Health Care Service Type Codes  to identify the classification of
        service or benefits.

        reference to CodeableConcept
        """

        self.service = None
        """
        If this is an actual service or product line, ie. not a Group, then
        use code to indicate the Professional Service or Product supplied (eg.
        CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a grouping item then
        use a group code to indicate the type of thing being grouped eg.
        'glasses' or 'compound'.

        reference to CodeableConcept
        """

        self.modifier = None
        """
        Item typification or modifiers codes, eg for Oral whether the
        treatment is cosmetic or associated with TMJ, or for medical whether
        the treatment was outside the clinic or out of office hours.

        type: array
        reference to CodeableConcept
        """

        self.programCode = None
        """
        For programs which require reson codes for the inclusion, covering, of
        this billed item under the program or sub-program.

        type: array
        reference to CodeableConcept
        """

        self.quantity = None
        """
        The number of repetitions of a service or product.

        reference to Quantity
        """

        self.unitPrice = None
        """
        If the item is a node then this is the fee for the product or service,
        otherwise this is the total of the fees for the children of the group.

        reference to Money
        """

        self.factor = None
        """
        A real number that represents a multiplier used in determining the
        overall value of services delivered and/or goods received. The concept
        of a Factor allows for a discount or surcharge multiplier to be
        applied to a monetary amount.

        type: int
        """

        self.net = None
        """
        The quantity times the unit price for an addittional service or
        product or charge. For example, the formula: unit Quantity * unit
        Price (Cost per Point) * factor Number  * points = net Amount.
        Quantity, factor and points are assumed to be 1 if not supplied.

        reference to Money
        """

        self.udi = None
        """
        List of Unique Device Identifiers associated with this line item.

        type: array
        reference to Reference: identifier
        """

        self.subDetail = None
        """
        Third tier of goods and services.

        type: array
        reference to Claim_SubDetail
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'programCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'service'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Detail',
             'child_variable': 'udi'},

            {'parent_entity': 'Claim_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'subDetail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'revenue'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'net'},
        ]


class Claim_SubDetail(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    __name__ = 'Claim_SubDetail'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        A service line number.

        type: int
        """

        self.revenue = None
        """
        The type of reveneu or cost center providing the product and/or
        service.

        reference to CodeableConcept
        """

        self.category = None
        """
        Health Care Service Type Codes  to identify the classification of
        service or benefits.

        reference to CodeableConcept
        """

        self.service = None
        """
        A code to indicate the Professional Service or Product supplied (eg.
        CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI).

        reference to CodeableConcept
        """

        self.modifier = None
        """
        Item typification or modifiers codes, eg for Oral whether the
        treatment is cosmetic or associated with TMJ, or for medical whether
        the treatment was outside the clinic or out of office hours.

        type: array
        reference to CodeableConcept
        """

        self.programCode = None
        """
        For programs which require reson codes for the inclusion, covering, of
        this billed item under the program or sub-program.

        type: array
        reference to CodeableConcept
        """

        self.quantity = None
        """
        The number of repetitions of a service or product.

        reference to Quantity
        """

        self.unitPrice = None
        """
        The fee for an addittional service or product or charge.

        reference to Money
        """

        self.factor = None
        """
        A real number that represents a multiplier used in determining the
        overall value of services delivered and/or goods received. The concept
        of a Factor allows for a discount or surcharge multiplier to be
        applied to a monetary amount.

        type: int
        """

        self.net = None
        """
        The quantity times the unit price for an addittional service or
        product or charge. For example, the formula: unit Quantity * unit
        Price (Cost per Point) * factor Number  * points = net Amount.
        Quantity, factor and points are assumed to be 1 if not supplied.

        reference to Money
        """

        self.udi = None
        """
        List of Unique Device Identifiers associated with this line item.

        type: array
        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'net'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'revenue'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'udi'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'programCode'},
        ]
