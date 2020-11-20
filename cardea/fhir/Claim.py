from .fhirbase import fhirbase


class Claim(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        resourceType: This is a Claim resource
        identifier: The business identifier for the instance: claim number,
            pre-determination or pre-authorization number.
        status: The status of the resource instance.
        type: The category of claim, eg, oral, pharmacy, vision, insitutional,
            professional.
        subType: A finer grained suite of claim subtype codes which may convey
            Inpatient vs Outpatient and/or a specialty service. In the US the
            BillType.
        use: Complete (Bill or Claim), Proposed (Pre-Authorization),
            Exploratory (Pre-determination).
        patient: Patient Resource.
        billablePeriod: The billable period for which charges are being
            submitted.
        created: The date when the enclosed suite of services were performed
            or completed.
        enterer: Person who created the invoice/claim/pre-determination or
            pre-authorization.
        insurer: The Insurer who is target of the request.
        provider: The provider which is responsible for the bill, claim
            pre-determination, pre-authorization.
        organization: The organization which is responsible for the bill,
            claim pre-determination, pre-authorization.
        priority: Immediate (STAT), best effort (NORMAL), deferred (DEFER).
        fundsReserve: In the case of a Pre-Determination/Pre-Authorization the
            provider may request that funds in the amount of the expected Benefit
            be reserved ('Patient' or 'Provider') to pay for the Benefits
            determined on the subsequent claim(s). 'None' explicitly indicates no
            funds reserving is requested.
        related: Other claims which are related to this claim such as prior
            claim versions or for related services.
        prescription: Prescription to support the dispensing of Pharmacy or
            Vision products.
        originalPrescription: Original prescription which has been superceded
            by this prescription to support the dispensing of pharmacy services,
            medications or products. For example, a physician may prescribe a
            medication which the pharmacy determines is contraindicated, or for
            which the patient has an intolerance, and therefor issues a new
            precription for an alternate medication which has the same theraputic
            intent. The prescription from the pharmacy becomes the 'prescription'
            and that from the physician becomes the 'original prescription'.
        payee: The party to be reimbursed for the services.
        referral: The referral resource which lists the date, practitioner,
            reason and other supporting information.
        facility: Facility where the services were provided.
        careTeam: The members of the team who provided the overall service as
            well as their role and whether responsible and qualifications.
        information: Additional information codes regarding exceptions,
            special considerations, the condition, situation, prior or concurrent
            issues. Often there are mutiple jurisdiction specific valuesets which
            are required.
        diagnosis: List of patient diagnosis for which care is sought.
        procedure: Ordered list of patient procedures performed to support the
            adjudication.
        insurance: Financial instrument by which payment information for
            health care.
        accident: An accident which resulted in the need for healthcare
            services.
        employmentImpacted: The start and optional end dates of when the
            patient was precluded from working due to the treatable condition(s).
        hospitalization: The start and optional end dates of when the patient
            was confined to a treatment center.
        item: First tier of goods and services.
        total: The total value of the claim.
    """

    __name__ = 'Claim'

    def __init__(self, dict_values=None):
        self.resourceType = 'Claim'
        # type: str
        # possible values: Claim

        self.status = None
        # type: str

        self.type = None
        # reference to CodeableConcept

        self.subType = None
        # type: list
        # reference to CodeableConcept

        self.use = None
        # type: str
        # possible values: complete, proposed, exploratory, other

        self.patient = None
        # reference to Reference: identifier

        self.billablePeriod = None
        # reference to Period

        self.created = None
        # type: str

        self.enterer = None
        # reference to Reference: identifier

        self.insurer = None
        # reference to Reference: identifier

        self.provider = None
        # reference to Reference: identifier

        self.organization = None
        # reference to Reference: identifier

        self.priority = None
        # reference to CodeableConcept

        self.fundsReserve = None
        # reference to CodeableConcept

        self.related = None
        # type: list
        # reference to Claim_Related

        self.prescription = None
        # reference to Reference: identifier

        self.originalPrescription = None
        # reference to Reference: identifier

        self.payee = None
        # reference to Claim_Payee

        self.referral = None
        # reference to Reference: identifier

        self.facility = None
        # reference to Reference: identifier

        self.careTeam = None
        # type: list
        # reference to Claim_CareTeam

        self.information = None
        # type: list
        # reference to Claim_Information

        self.diagnosis = None
        # type: list
        # reference to Claim_Diagnosis

        self.procedure = None
        # type: list
        # reference to Claim_Procedure

        self.insurance = None
        # type: list
        # reference to Claim_Insurance

        self.accident = None
        # reference to Claim_Accident

        self.employmentImpacted = None
        # reference to Period

        self.hospitalization = None
        # reference to Period

        self.item = None
        # type: list
        # reference to Claim_Item

        self.total = None
        # reference to Money

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
             'child_variable': 'type'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'billablePeriod'},

            {'parent_entity': 'Claim_Accident',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'accident'},

            {'parent_entity': 'Claim_CareTeam',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'careTeam'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'organization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'subType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'prescription'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'facility'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'originalPrescription'},

            {'parent_entity': 'Claim_Related',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'related'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'fundsReserve'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'patient'},

            {'parent_entity': 'Claim_Procedure',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'procedure'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'insurer'},

            {'parent_entity': 'Claim_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'insurance'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'Claim_Information',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'information'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'provider'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'priority'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'total'},

            {'parent_entity': 'Claim_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'item'},

            {'parent_entity': 'Claim_Payee',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'payee'},

            {'parent_entity': 'Claim_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'employmentImpacted'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'referral'},
        ]


class Claim_Related(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        claim: Other claims which are related to this claim such as prior
            claim versions or for related services.
        relationship: For example prior or umbrella.
        reference: An alternate organizational reference to the case or file
            to which this particular claim pertains - eg Property/Casualy insurer
            claim # or Workers Compensation case # .
    """

    __name__ = 'Claim_Related'

    def __init__(self, dict_values=None):
        self.claim = None
        # reference to Reference: identifier

        self.relationship = None
        # reference to CodeableConcept

        self.reference = None
        # reference to Identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Related',
             'child_variable': 'reference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Related',
             'child_variable': 'claim'},

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

    Args:
        type: Type of Party to be reimbursed: Subscriber, provider, other.
        resourceType: organization | patient | practitioner | relatedperson.
        party: Party to be reimbursed: Subscriber, provider, other.
    """

    __name__ = 'Claim_Payee'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.resourceType = None
        # reference to Coding

        self.party = None
        # reference to Reference: identifier

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

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Payee',
             'child_variable': 'resourceType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Payee',
             'child_variable': 'type'},
        ]


class Claim_CareTeam(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        sequence: Sequence of the careTeam which serves to order and provide a
            link.
        provider: Member of the team who provided the overall service.
        responsible: The party who is billing and responsible for the claimed
            good or service rendered to the patient.
        role: The lead, assisting or supervising practitioner and their
            discipline if a multidisiplinary team.
        qualification: The qualification which is applicable for this service.
    """

    __name__ = 'Claim_CareTeam'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.provider = None
        # reference to Reference: identifier

        self.responsible = None
        # type: bool

        self.role = None
        # reference to CodeableConcept

        self.qualification = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'role'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'qualification'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'provider'},
        ]


class Claim_Information(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        sequence: Sequence of the information element which serves to provide
            a link.
        category: The general class of the information supplied: information;
            exception; accident, employment; onset, etc.
        code: System and code pertaining to the specific information regarding
            special conditions relating to the setting, treatment or patient  for
            which care is sought which may influence the adjudication.
        timingDate: The date when or period to which this information refers.
        timingPeriod: The date when or period to which this information
            refers.
        valueString: Additional data or information such as resources,
            documents, images etc. including references to the data or the actual
            inclusion of the data.
        valueQuantity: Additional data or information such as resources,
            documents, images etc. including references to the data or the actual
            inclusion of the data.
        valueAttachment: Additional data or information such as resources,
            documents, images etc. including references to the data or the actual
            inclusion of the data.
        valueReference: Additional data or information such as resources,
            documents, images etc. including references to the data or the actual
            inclusion of the data.
        reason: For example, provides the reason for: the additional stay, or
            missing tooth or any other situation where a reason code is required
            in addition to the content.
    """

    __name__ = 'Claim_Information'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.category = None
        # reference to CodeableConcept

        self.code = None
        # reference to CodeableConcept

        self.timingDate = None
        # type: str

        self.timingPeriod = None
        # reference to Period

        self.valueString = None
        # type: str

        self.valueQuantity = None
        # reference to Quantity

        self.valueAttachment = None
        # reference to Attachment

        self.valueReference = None
        # reference to Reference: identifier

        self.reason = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'code'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'category'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'timingPeriod'},

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

    Args:
        sequence: Sequence of diagnosis which serves to provide a link.
        diagnosisCodeableConcept: The diagnosis.
        diagnosisReference: The diagnosis.
        type: The type of the Diagnosis, for example: admitting, primary,
            secondary, discharge.
        packageCode: The package billing code, for example DRG, based on the
            assigned grouping code system.
    """

    __name__ = 'Claim_Diagnosis'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.diagnosisCodeableConcept = None
        # reference to CodeableConcept

        self.diagnosisReference = None
        # reference to Reference: identifier

        self.type = None
        # type: list
        # reference to CodeableConcept

        self.packageCode = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'packageCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'diagnosisReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'diagnosisCodeableConcept'},
        ]


class Claim_Procedure(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        sequence: Sequence of procedures which serves to order and provide a
            link.
        date: Date and optionally time the procedure was performed .
        procedureCodeableConcept: The procedure code.
        procedureReference: The procedure code.
    """

    __name__ = 'Claim_Procedure'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.date = None
        # type: str

        self.procedureCodeableConcept = None
        # reference to CodeableConcept

        self.procedureReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Procedure',
             'child_variable': 'procedureReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Procedure',
             'child_variable': 'procedureCodeableConcept'},
        ]


class Claim_Insurance(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        sequence: Sequence of coverage which serves to provide a link and
            convey coordination of benefit order.
        focal: A flag to indicate that this Coverage is the focus for
            adjudication. The Coverage against which the claim is to be
            adjudicated.
        coverage: Reference to the program or plan identification, underwriter
            or payor.
        businessArrangement: The contract number of a business agreement which
            describes the terms and conditions.
        preAuthRef: A list of references from the Insurer to which these
            services pertain.
        claimResponse: The Coverages adjudication details.
    """

    __name__ = 'Claim_Insurance'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.focal = None
        # type: bool

        self.coverage = None
        # reference to Reference: identifier

        self.businessArrangement = None
        # type: str

        self.preAuthRef = None
        # type: list

        self.claimResponse = None
        # reference to Reference: identifier

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

    Args:
        date: Date of an accident which these services are addressing.
        type: Type of accident: work, auto, etc.
        locationAddress: Accident Place.
        locationReference: Accident Place.
    """

    __name__ = 'Claim_Accident'

    def __init__(self, dict_values=None):
        self.date = None
        # type: str

        self.type = None
        # reference to CodeableConcept

        self.locationAddress = None
        # reference to Address

        self.locationReference = None
        # reference to Reference: identifier

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

    Args:
        sequence: A service line number.
        careTeamLinkId: CareTeam applicable for this service or product line.
        diagnosisLinkId: Diagnosis applicable for this service or product
            line.
        procedureLinkId: Procedures applicable for this service or product
            line.
        informationLinkId: Exceptions, special conditions and supporting
            information pplicable for this service or product line.
        revenue: The type of reveneu or cost center providing the product
            and/or service.
        category: Health Care Service Type Codes  to identify the
            classification of service or benefits.
        service: If this is an actual service or product line, ie. not a
            Group, then use code to indicate the Professional Service or Product
            supplied (eg. CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,RXNorm,ACHI,CCI). If a
            grouping item then use a group code to indicate the type of thing
            being grouped eg. 'glasses' or 'compound'.
        modifier: Item typification or modifiers codes, eg for Oral whether
            the treatment is cosmetic or associated with TMJ, or for medical
            whether the treatment was outside the clinic or out of office hours.
        programCode: For programs which require reason codes for the inclusion
            or covering of this billed item under the program or sub-program.
        servicedDate: The date or dates when the enclosed suite of services
            were performed or completed.
        servicedPeriod: The date or dates when the enclosed suite of services
            were performed or completed.
        locationCodeableConcept: Where the service was provided.
        locationAddress: Where the service was provided.
        locationReference: Where the service was provided.
        quantity: The number of repetitions of a service or product.
        unitPrice: If the item is a node then this is the fee for the product
            or service, otherwise this is the total of the fees for the children
            of the group.
        factor: A real number that represents a multiplier used in determining
            the overall value of services delivered and/or goods received. The
            concept of a Factor allows for a discount or surcharge multiplier to
            be applied to a monetary amount.
        net: The quantity times the unit price for an addittional service or
            product or charge. For example, the formula: unit Quantity * unit
            Price (Cost per Point) * factor Number  * points = net Amount.
            Quantity, factor and points are assumed to be 1 if not supplied.
        udi: List of Unique Device Identifiers associated with this line item.
        bodySite: Physical service site on the patient (limb, tooth, etc).
        subSite: A region or surface of the site, eg. limb region or tooth
            surface(s).
        encounter: A billed item may include goods or services provided in
            multiple encounters.
        detail: Second tier of goods and services.
    """

    __name__ = 'Claim_Item'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.careTeamLinkId = None
        # type: list

        self.diagnosisLinkId = None
        # type: list

        self.procedureLinkId = None
        # type: list

        self.informationLinkId = None
        # type: list

        self.revenue = None
        # reference to CodeableConcept

        self.category = None
        # reference to CodeableConcept

        self.service = None
        # reference to CodeableConcept

        self.modifier = None
        # type: list
        # reference to CodeableConcept

        self.programCode = None
        # type: list
        # reference to CodeableConcept

        self.servicedDate = None
        # type: str

        self.servicedPeriod = None
        # reference to Period

        self.locationCodeableConcept = None
        # reference to CodeableConcept

        self.locationAddress = None
        # reference to Address

        self.locationReference = None
        # reference to Reference: identifier

        self.quantity = None
        # reference to Quantity

        self.unitPrice = None
        # reference to Money

        self.factor = None
        # type: int

        self.net = None
        # reference to Money

        self.udi = None
        # type: list
        # reference to Reference: identifier

        self.bodySite = None
        # reference to CodeableConcept

        self.subSite = None
        # type: list
        # reference to CodeableConcept

        self.encounter = None
        # type: list
        # reference to Reference: identifier

        self.detail = None
        # type: list
        # reference to Claim_Detail

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

            {'parent_entity': 'Claim_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'detail'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'unitPrice'},

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
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'service'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'revenue'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'quantity'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationReference'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'subSite'},
        ]


class Claim_Detail(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        sequence: A service line number.
        revenue: The type of reveneu or cost center providing the product
            and/or service.
        category: Health Care Service Type Codes  to identify the
            classification of service or benefits.
        service: If this is an actual service or product line, ie. not a
            Group, then use code to indicate the Professional Service or Product
            supplied (eg. CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a
            grouping item then use a group code to indicate the type of thing
            being grouped eg. 'glasses' or 'compound'.
        modifier: Item typification or modifiers codes, eg for Oral whether
            the treatment is cosmetic or associated with TMJ, or for medical
            whether the treatment was outside the clinic or out of office hours.
        programCode: For programs which require reson codes for the inclusion,
            covering, of this billed item under the program or sub-program.
        quantity: The number of repetitions of a service or product.
        unitPrice: If the item is a node then this is the fee for the product
            or service, otherwise this is the total of the fees for the children
            of the group.
        factor: A real number that represents a multiplier used in determining
            the overall value of services delivered and/or goods received. The
            concept of a Factor allows for a discount or surcharge multiplier to
            be applied to a monetary amount.
        net: The quantity times the unit price for an addittional service or
            product or charge. For example, the formula: unit Quantity * unit
            Price (Cost per Point) * factor Number  * points = net Amount.
            Quantity, factor and points are assumed to be 1 if not supplied.
        udi: List of Unique Device Identifiers associated with this line item.
        subDetail: Third tier of goods and services.
    """

    __name__ = 'Claim_Detail'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.revenue = None
        # reference to CodeableConcept

        self.category = None
        # reference to CodeableConcept

        self.service = None
        # reference to CodeableConcept

        self.modifier = None
        # type: list
        # reference to CodeableConcept

        self.programCode = None
        # type: list
        # reference to CodeableConcept

        self.quantity = None
        # reference to Quantity

        self.unitPrice = None
        # reference to Money

        self.factor = None
        # type: int

        self.net = None
        # reference to Money

        self.udi = None
        # type: list
        # reference to Reference: identifier

        self.subDetail = None
        # type: list
        # reference to Claim_SubDetail

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'net'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Detail',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'revenue'},

            {'parent_entity': 'Claim_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'subDetail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'programCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'service'},
        ]


class Claim_SubDetail(fhirbase):
    """
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.

    Args:
        sequence: A service line number.
        revenue: The type of reveneu or cost center providing the product
            and/or service.
        category: Health Care Service Type Codes  to identify the
            classification of service or benefits.
        service: A code to indicate the Professional Service or Product
            supplied (eg. CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI).
        modifier: Item typification or modifiers codes, eg for Oral whether
            the treatment is cosmetic or associated with TMJ, or for medical
            whether the treatment was outside the clinic or out of office hours.
        programCode: For programs which require reson codes for the inclusion,
            covering, of this billed item under the program or sub-program.
        quantity: The number of repetitions of a service or product.
        unitPrice: The fee for an addittional service or product or charge.
        factor: A real number that represents a multiplier used in determining
            the overall value of services delivered and/or goods received. The
            concept of a Factor allows for a discount or surcharge multiplier to
            be applied to a monetary amount.
        net: The quantity times the unit price for an addittional service or
            product or charge. For example, the formula: unit Quantity * unit
            Price (Cost per Point) * factor Number  * points = net Amount.
            Quantity, factor and points are assumed to be 1 if not supplied.
        udi: List of Unique Device Identifiers associated with this line item.
    """

    __name__ = 'Claim_SubDetail'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.revenue = None
        # reference to CodeableConcept

        self.category = None
        # reference to CodeableConcept

        self.service = None
        # reference to CodeableConcept

        self.modifier = None
        # type: list
        # reference to CodeableConcept

        self.programCode = None
        # type: list
        # reference to CodeableConcept

        self.quantity = None
        # reference to Quantity

        self.unitPrice = None
        # reference to Money

        self.factor = None
        # type: int

        self.net = None
        # reference to Money

        self.udi = None
        # type: list
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'programCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'modifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'category'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'net'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'udi'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'unitPrice'},
        ]
