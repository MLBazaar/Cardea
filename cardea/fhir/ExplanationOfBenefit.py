from .fhirbase import fhirbase


class ExplanationOfBenefit(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        resourceType: This is a ExplanationOfBenefit resource
        identifier: The EOB Business Identifier.
        status: The status of the resource instance.
        type: The category of claim, eg, oral, pharmacy, vision, insitutional,
            professional.
        subType: A finer grained suite of claim subtype codes which may convey
            Inpatient vs Outpatient and/or a specialty service. In the US the
            BillType.
        patient: Patient Resource.
        billablePeriod: The billable period for which charges are being
            submitted.
        created: The date when the EOB was created.
        enterer: The person who created the explanation of benefit.
        insurer: The insurer which is responsible for the explanation of
            benefit.
        provider: The provider which is responsible for the claim.
        organization: The provider which is responsible for the claim.
        referral: The referral resource which lists the date, practitioner,
            reason and other supporting information.
        facility: Facility where the services were provided.
        claim: The business identifier for the instance: invoice number, claim
            number, pre-determination or pre-authorization number.
        claimResponse: The business identifier for the instance: invoice
            number, claim number, pre-determination or pre-authorization number.
        outcome: Processing outcome errror, partial or complete processing.
        disposition: A description of the status of the adjudication.
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
        information: Additional information codes regarding exceptions,
            special considerations, the condition, situation, prior or concurrent
            issues. Often there are mutiple jurisdiction specific valuesets which
            are required.
        careTeam: The members of the team who provided the overall service as
            well as their role and whether responsible and qualifications.
        diagnosis: Ordered list of patient diagnosis for which care is sought.
        procedure: Ordered list of patient procedures performed to support the
            adjudication.
        precedence: Precedence (primary, secondary, etc.).
        insurance: Financial instrument by which payment information for
            health care.
        accident: An accident which resulted in the need for healthcare
            services.
        employmentImpacted: The start and optional end dates of when the
            patient was precluded from working due to the treatable condition(s).
        hospitalization: The start and optional end dates of when the patient
            was confined to a treatment center.
        item: First tier of goods and services.
        addItem: The first tier service adjudications for payor added
            services.
        totalCost: The total cost of the services reported.
        unallocDeductable: The amount of deductable applied which was not
            allocated to any particular service line.
        totalBenefit: Total amount of benefit payable (Equal to sum of the
            Benefit amounts from all detail lines and additions less the
            Unallocated Deductable).
        payment: Payment details for the claim if the claim has been paid.
        form: The form to be used for printing the content.
        processNote: Note text.
        benefitBalance: Balance by Benefit Category.
    """

    __name__ = 'ExplanationOfBenefit'

    def __init__(self, dict_values=None):
        self.resourceType = 'ExplanationOfBenefit'
        # type: str
        # possible values: ExplanationOfBenefit

        self.status = None
        # type: str
        # possible values: active, cancelled, draft, entered-in-error

        self.type = None
        # reference to CodeableConcept

        self.subType = None
        # type: list
        # reference to CodeableConcept

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

        self.referral = None
        # reference to Reference: identifier

        self.facility = None
        # reference to Reference: identifier

        self.claim = None
        # reference to Reference: identifier

        self.claimResponse = None
        # reference to Reference: identifier

        self.outcome = None
        # reference to CodeableConcept

        self.disposition = None
        # type: str

        self.related = None
        # type: list
        # reference to ExplanationOfBenefit_Related

        self.prescription = None
        # reference to Reference: identifier

        self.originalPrescription = None
        # reference to Reference: identifier

        self.payee = None
        # reference to ExplanationOfBenefit_Payee

        self.information = None
        # type: list
        # reference to ExplanationOfBenefit_Information

        self.careTeam = None
        # type: list
        # reference to ExplanationOfBenefit_CareTeam

        self.diagnosis = None
        # type: list
        # reference to ExplanationOfBenefit_Diagnosis

        self.procedure = None
        # type: list
        # reference to ExplanationOfBenefit_Procedure

        self.precedence = None
        # type: int

        self.insurance = None
        # reference to ExplanationOfBenefit_Insurance

        self.accident = None
        # reference to ExplanationOfBenefit_Accident

        self.employmentImpacted = None
        # reference to Period

        self.hospitalization = None
        # reference to Period

        self.item = None
        # type: list
        # reference to ExplanationOfBenefit_Item

        self.addItem = None
        # type: list
        # reference to ExplanationOfBenefit_AddItem

        self.totalCost = None
        # reference to Money

        self.unallocDeductable = None
        # reference to Money

        self.totalBenefit = None
        # reference to Money

        self.payment = None
        # reference to ExplanationOfBenefit_Payment: identifier

        self.form = None
        # reference to CodeableConcept

        self.processNote = None
        # type: list
        # reference to ExplanationOfBenefit_ProcessNote

        self.benefitBalance = None
        # type: list
        # reference to ExplanationOfBenefit_BenefitBalance

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'cancelled', 'draft', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, cancelled, draft, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ExplanationOfBenefit_BenefitBalance',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'benefitBalance'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'prescription'},

            {'parent_entity': 'ExplanationOfBenefit_AddItem',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'addItem'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'claimResponse'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'totalCost'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'unallocDeductable'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'provider'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'originalPrescription'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'subType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'claim'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'totalBenefit'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'form'},

            {'parent_entity': 'ExplanationOfBenefit_Procedure',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'procedure'},

            {'parent_entity': 'ExplanationOfBenefit_Related',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'related'},

            {'parent_entity': 'ExplanationOfBenefit_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'insurance'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'patient'},

            {'parent_entity': 'ExplanationOfBenefit_Information',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'information'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'ExplanationOfBenefit_Accident',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'accident'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'billablePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'referral'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'organization'},

            {'parent_entity': 'ExplanationOfBenefit_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'processNote'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'outcome'},

            {'parent_entity': 'ExplanationOfBenefit_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'item'},

            {'parent_entity': 'ExplanationOfBenefit_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'identifier'},

            {'parent_entity': 'ExplanationOfBenefit_Payee',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'payee'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'insurer'},

            {'parent_entity': 'ExplanationOfBenefit_Payment',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'payment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'facility'},

            {'parent_entity': 'ExplanationOfBenefit_CareTeam',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'careTeam'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'employmentImpacted'},
        ]


class ExplanationOfBenefit_Related(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        claim: Other claims which are related to this claim such as prior
            claim versions or for related services.
        relationship: For example prior or umbrella.
        reference: An alternate organizational reference to the case or file
            to which this particular claim pertains - eg Property/Casualy insurer
            claim # or Workers Compensation case # .
    """

    __name__ = 'ExplanationOfBenefit_Related'

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
             'child_entity': 'ExplanationOfBenefit_Related',
             'child_variable': 'reference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Related',
             'child_variable': 'claim'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Related',
             'child_variable': 'relationship'},
        ]


class ExplanationOfBenefit_Payee(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        type: Type of Party to be reimbursed: Subscriber, provider, other.
        resourceType: organization | patient | practitioner | relatedperson.
        party: Party to be reimbursed: Subscriber, provider, other.
    """

    __name__ = 'ExplanationOfBenefit_Payee'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.resourceType = None
        # reference to CodeableConcept

        self.party = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'resourceType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'party'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'type'},
        ]


class ExplanationOfBenefit_Information(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

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

    __name__ = 'ExplanationOfBenefit_Information'

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
        # reference to Coding

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'code'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'reason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'category'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'timingPeriod'},
        ]


class ExplanationOfBenefit_CareTeam(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        sequence: Sequence of careteam which serves to order and provide a
            link.
        provider: The members of the team who provided the overall service.
        responsible: The practitioner who is billing and responsible for the
            claimed services rendered to the patient.
        role: The lead, assisting or supervising practitioner and their
            discipline if a multidisiplinary team.
        qualification: The qualification which is applicable for this service.
    """

    __name__ = 'ExplanationOfBenefit_CareTeam'

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_CareTeam',
             'child_variable': 'provider'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_CareTeam',
             'child_variable': 'role'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_CareTeam',
             'child_variable': 'qualification'},
        ]


class ExplanationOfBenefit_Diagnosis(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        sequence: Sequence of diagnosis which serves to provide a link.
        diagnosisCodeableConcept: The diagnosis.
        diagnosisReference: The diagnosis.
        type: The type of the Diagnosis, for example: admitting, primary,
            secondary, discharge.
        packageCode: The package billing code, for example DRG, based on the
            assigned grouping code system.
    """

    __name__ = 'ExplanationOfBenefit_Diagnosis'

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
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'diagnosisReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'packageCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'diagnosisCodeableConcept'},
        ]


class ExplanationOfBenefit_Procedure(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        sequence: Sequence of procedures which serves to order and provide a
            link.
        date: Date and optionally time the procedure was performed .
        procedureCodeableConcept: The procedure code.
        procedureReference: The procedure code.
    """

    __name__ = 'ExplanationOfBenefit_Procedure'

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Procedure',
             'child_variable': 'procedureCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Procedure',
             'child_variable': 'procedureReference'},
        ]


class ExplanationOfBenefit_Insurance(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        coverage: Reference to the program or plan identification, underwriter
            or payor.
        preAuthRef: A list of references from the Insurer to which these
            services pertain.
    """

    __name__ = 'ExplanationOfBenefit_Insurance'

    def __init__(self, dict_values=None):
        self.coverage = None
        # reference to Reference: identifier

        self.preAuthRef = None
        # type: list

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Insurance',
             'child_variable': 'coverage'},
        ]


class ExplanationOfBenefit_Accident(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        date: Date of an accident which these services are addressing.
        type: Type of accident: work, auto, etc.
        locationAddress: Where the accident occurred.
        locationReference: Where the accident occurred.
    """

    __name__ = 'ExplanationOfBenefit_Accident'

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
            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Accident',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Accident',
             'child_variable': 'locationReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Accident',
             'child_variable': 'type'},
        ]


class ExplanationOfBenefit_Item(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        sequence: A service line number.
        careTeamLinkId: Careteam applicable for this service or product line.
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
            supplied (eg. CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI). If a
            grouping item then use a group code to indicate the type of thing
            being grouped eg. 'glasses' or 'compound'.
        modifier: Item typification or modifiers codes, eg for Oral whether
            the treatment is cosmetic or associated with TMJ, or for medical
            whether the treatment was outside the clinic or out of office hours.
        programCode: For programs which require reson codes for the inclusion,
            covering, of this billed item under the program or sub-program.
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
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
        detail: Second tier of goods and services.
    """

    __name__ = 'ExplanationOfBenefit_Item'

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

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ExplanationOfBenefit_Adjudication

        self.detail = None
        # type: list
        # reference to ExplanationOfBenefit_Detail

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'subSite'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'net'},

            {'parent_entity': 'ExplanationOfBenefit_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'programCode'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'quantity'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'bodySite'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'encounter'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'revenue'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'udi'},
        ]


class ExplanationOfBenefit_Adjudication(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        category: Code indicating: Co-Pay, deductable, elegible, benefit, tax,
            etc.
        reason: Adjudication reason such as limit reached.
        amount: Monitory amount associated with the code.
        value: A non-monetary value for example a percentage. Mutually
            exclusive to the amount element above.
    """

    __name__ = 'ExplanationOfBenefit_Adjudication'

    def __init__(self, dict_values=None):
        self.category = None
        # reference to CodeableConcept

        self.reason = None
        # reference to CodeableConcept

        self.amount = None
        # reference to Money

        self.value = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Adjudication',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Adjudication',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Adjudication',
             'child_variable': 'reason'},
        ]


class ExplanationOfBenefit_Detail(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        sequence: A service line number.
        type: The type of product or service.
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
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
        subDetail: Third tier of goods and services.
    """

    __name__ = 'ExplanationOfBenefit_Detail'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.type = None
        # reference to CodeableConcept

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

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ExplanationOfBenefit_Adjudication

        self.subDetail = None
        # type: list
        # reference to ExplanationOfBenefit_SubDetail

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ExplanationOfBenefit_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'subDetail'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'service'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'programCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'revenue'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'modifier'},
        ]


class ExplanationOfBenefit_SubDetail(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        sequence: A service line number.
        type: The type of product or service.
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
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
    """

    __name__ = 'ExplanationOfBenefit_SubDetail'

    def __init__(self, dict_values=None):
        self.sequence = None
        # type: int

        self.type = None
        # reference to CodeableConcept

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

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ExplanationOfBenefit_Adjudication

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'programCode'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'modifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'service'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'revenue'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'category'},
        ]


class ExplanationOfBenefit_AddItem(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        sequenceLinkId: List of input service items which this service line is
            intended to replace.
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
        fee: The fee charged for the professional service or product.
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
        detail: The second tier service adjudications for payor added
            services.
    """

    __name__ = 'ExplanationOfBenefit_AddItem'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
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

        self.fee = None
        # reference to Money

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ExplanationOfBenefit_Adjudication

        self.detail = None
        # type: list
        # reference to ExplanationOfBenefit_Detail1

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'modifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'revenue'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'adjudication'},

            {'parent_entity': 'ExplanationOfBenefit_Detail1',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'detail'},
        ]


class ExplanationOfBenefit_Detail1(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        revenue: The type of reveneu or cost center providing the product
            and/or service.
        category: Health Care Service Type Codes  to identify the
            classification of service or benefits.
        service: A code to indicate the Professional Service or Product
            supplied (eg. CTP, HCPCS,USCLS,ICD10, NCPDP,DIN,ACHI,CCI).
        modifier: Item typification or modifiers codes, eg for Oral whether
            the treatment is cosmetic or associated with TMJ, or for medical
            whether the treatment was outside the clinic or out of office hours.
        fee: The fee charged for the professional service or product.
        noteNumber: A list of note references to the notes provided below.
        adjudication: The adjudications results.
    """

    __name__ = 'ExplanationOfBenefit_Detail1'

    def __init__(self, dict_values=None):
        self.revenue = None
        # reference to CodeableConcept

        self.category = None
        # reference to CodeableConcept

        self.service = None
        # reference to CodeableConcept

        self.modifier = None
        # type: list
        # reference to CodeableConcept

        self.fee = None
        # reference to Money

        self.noteNumber = None
        # type: list

        self.adjudication = None
        # type: list
        # reference to ExplanationOfBenefit_Adjudication

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'category'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'modifier'},
        ]


class ExplanationOfBenefit_Payment(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        type: Whether this represents partial or complete payment of the
            claim.
        adjustment: Adjustment to the payment of this transaction which is not
            related to adjudication of this transaction.
        adjustmentReason: Reason for the payment adjustment.
        date: Estimated payment date.
        amount: Payable less any payment adjustment.
        identifier: Payment identifer.
    """

    __name__ = 'ExplanationOfBenefit_Payment'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.adjustment = None
        # reference to Money

        self.adjustmentReason = None
        # reference to CodeableConcept

        self.date = None
        # type: str

        self.amount = None
        # reference to Money

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'adjustmentReason'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'identifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'adjustment'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'amount'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'type'},
        ]


class ExplanationOfBenefit_ProcessNote(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        number: An integer associated with each note which may be referred to
            from each service line item.
        type: The note purpose: Print/Display.
        text: The note text.
        language: The ISO-639-1 alpha 2 code in lower case for the language,
            optionally followed by a hyphen and the ISO-3166-1 alpha 2 code for
            the region in upper case; e.g. "en" for English, or "en-US" for
            American English versus "en-EN" for England English.
    """

    __name__ = 'ExplanationOfBenefit_ProcessNote'

    def __init__(self, dict_values=None):
        self.number = None
        # type: int

        self.type = None
        # reference to CodeableConcept

        self.text = None
        # type: str

        self.language = None
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_ProcessNote',
             'child_variable': 'language'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_ProcessNote',
             'child_variable': 'type'},
        ]


class ExplanationOfBenefit_BenefitBalance(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        category: Dental, Vision, Medical, Pharmacy, Rehab etc.
        subCategory: Dental: basic, major, ortho; Vision exam, glasses,
            contacts; etc.
        excluded: True if the indicated class of service is excluded from the
            plan, missing or False indicated the service is included in the
            coverage.
        name: A short name or tag for the benefit, for example MED01, or
            DENT2.
        description: A richer description of the benefit, for example 'DENT2
            covers 100% of basic, 50% of major but exclused Ortho, Implants and
            Costmetic services'.
        network: Network designation.
        unit: Unit designation: individual or family.
        term: The term or period of the values such as 'maximum lifetime
            benefit' or 'maximum annual vistis'.
        financial: Benefits Used to date.
    """

    __name__ = 'ExplanationOfBenefit_BenefitBalance'

    def __init__(self, dict_values=None):
        self.category = None
        # reference to CodeableConcept

        self.subCategory = None
        # reference to CodeableConcept

        self.excluded = None
        # type: bool

        self.name = None
        # type: str

        self.description = None
        # type: str

        self.network = None
        # reference to CodeableConcept

        self.unit = None
        # reference to CodeableConcept

        self.term = None
        # reference to CodeableConcept

        self.financial = None
        # type: list
        # reference to ExplanationOfBenefit_Financial

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'subCategory'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'term'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'unit'},

            {'parent_entity': 'ExplanationOfBenefit_Financial',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'financial'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'network'},
        ]


class ExplanationOfBenefit_Financial(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.

    Args:
        type: Deductable, visits, benefit amount.
        allowedUnsignedInt: Benefits allowed.
        allowedString: Benefits allowed.
        allowedMoney: Benefits allowed.
        usedUnsignedInt: Benefits used.
        usedMoney: Benefits used.
    """

    __name__ = 'ExplanationOfBenefit_Financial'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to CodeableConcept

        self.allowedUnsignedInt = None
        # type: int

        self.allowedString = None
        # type: str

        self.allowedMoney = None
        # reference to Money

        self.usedUnsignedInt = None
        # type: int

        self.usedMoney = None
        # reference to Money

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'allowedMoney'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'usedMoney'},
        ]
