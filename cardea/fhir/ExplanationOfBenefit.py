from .fhirbase import fhirbase


class ExplanationOfBenefit(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit'

    def __init__(self, dict_values=None):
        self.resourceType = 'ExplanationOfBenefit'
        """
        This is a ExplanationOfBenefit resource

        type: string
        possible values: ExplanationOfBenefit
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        possible values: active, cancelled, draft, entered-in-error
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
        The date when the EOB was created.

        type: string
        """

        self.enterer = None
        """
        The person who created the explanation of benefit.

        reference to Reference: identifier
        """

        self.insurer = None
        """
        The insurer which is responsible for the explanation of benefit.

        reference to Reference: identifier
        """

        self.provider = None
        """
        The provider which is responsible for the claim.

        reference to Reference: identifier
        """

        self.organization = None
        """
        The provider which is responsible for the claim.

        reference to Reference: identifier
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

        self.claim = None
        """
        The business identifier for the instance: invoice number, claim
        number, pre-determination or pre-authorization number.

        reference to Reference: identifier
        """

        self.claimResponse = None
        """
        The business identifier for the instance: invoice number, claim
        number, pre-determination or pre-authorization number.

        reference to Reference: identifier
        """

        self.outcome = None
        """
        Processing outcome errror, partial or complete processing.

        reference to CodeableConcept
        """

        self.disposition = None
        """
        A description of the status of the adjudication.

        type: string
        """

        self.related = None
        """
        Other claims which are related to this claim such as prior claim
        versions or for related services.

        type: array
        reference to ExplanationOfBenefit_Related
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

        reference to ExplanationOfBenefit_Payee
        """

        self.information = None
        """
        Additional information codes regarding exceptions, special
        considerations, the condition, situation, prior or concurrent issues.
        Often there are mutiple jurisdiction specific valuesets which are
        required.

        type: array
        reference to ExplanationOfBenefit_Information
        """

        self.careTeam = None
        """
        The members of the team who provided the overall service as well as
        their role and whether responsible and qualifications.

        type: array
        reference to ExplanationOfBenefit_CareTeam
        """

        self.diagnosis = None
        """
        Ordered list of patient diagnosis for which care is sought.

        type: array
        reference to ExplanationOfBenefit_Diagnosis
        """

        self.procedure = None
        """
        Ordered list of patient procedures performed to support the
        adjudication.

        type: array
        reference to ExplanationOfBenefit_Procedure
        """

        self.precedence = None
        """
        Precedence (primary, secondary, etc.).

        type: int
        """

        self.insurance = None
        """
        Financial instrument by which payment information for health care.

        reference to ExplanationOfBenefit_Insurance
        """

        self.accident = None
        """
        An accident which resulted in the need for healthcare services.

        reference to ExplanationOfBenefit_Accident
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
        reference to ExplanationOfBenefit_Item
        """

        self.addItem = None
        """
        The first tier service adjudications for payor added services.

        type: array
        reference to ExplanationOfBenefit_AddItem
        """

        self.totalCost = None
        """
        The total cost of the services reported.

        reference to Money
        """

        self.unallocDeductable = None
        """
        The amount of deductable applied which was not allocated to any
        particular service line.

        reference to Money
        """

        self.totalBenefit = None
        """
        Total amount of benefit payable (Equal to sum of the Benefit amounts
        from all detail lines and additions less the Unallocated Deductable).

        reference to Money
        """

        self.payment = None
        """
        Payment details for the claim if the claim has been paid.

        reference to ExplanationOfBenefit_Payment: identifier
        """

        self.form = None
        """
        The form to be used for printing the content.

        reference to CodeableConcept
        """

        self.processNote = None
        """
        Note text.

        type: array
        reference to ExplanationOfBenefit_ProcessNote
        """

        self.benefitBalance = None
        """
        Balance by Benefit Category.

        type: array
        reference to ExplanationOfBenefit_BenefitBalance
        """

        self.identifier = None
        """
        The EOB Business Identifier.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'active', 'cancelled', 'draft', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, cancelled, draft, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'outcome'},

            {'parent_entity': 'ExplanationOfBenefit_Information',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'information'},

            {'parent_entity': 'ExplanationOfBenefit_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'processNote'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'prescription'},

            {'parent_entity': 'ExplanationOfBenefit_Payee',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'payee'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'provider'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'referral'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'claimResponse'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'form'},

            {'parent_entity': 'ExplanationOfBenefit_Procedure',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'procedure'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'billablePeriod'},

            {'parent_entity': 'ExplanationOfBenefit_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'insurance'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'organization'},

            {'parent_entity': 'ExplanationOfBenefit_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'claim'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'insurer'},

            {'parent_entity': 'ExplanationOfBenefit_AddItem',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'addItem'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'facility'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'identifier'},

            {'parent_entity': 'ExplanationOfBenefit_Payment',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'payment'},

            {'parent_entity': 'ExplanationOfBenefit_Related',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'related'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'totalCost'},

            {'parent_entity': 'ExplanationOfBenefit_Accident',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'accident'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'employmentImpacted'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'enterer'},

            {'parent_entity': 'ExplanationOfBenefit_BenefitBalance',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'benefitBalance'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'unallocDeductable'},

            {'parent_entity': 'ExplanationOfBenefit_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'item'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'originalPrescription'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'patient'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'totalBenefit'},

            {'parent_entity': 'ExplanationOfBenefit_CareTeam',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'careTeam'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'subType'},
        ]


class ExplanationOfBenefit_Related(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_Related'

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Related',
             'child_variable': 'relationship'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Related',
             'child_variable': 'claim'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Related',
             'child_variable': 'reference'},
        ]


class ExplanationOfBenefit_Payee(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_Payee'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Type of Party to be reimbursed: Subscriber, provider, other.

        reference to CodeableConcept
        """

        self.resourceType = None
        """
        organization | patient | practitioner | relatedperson.

        reference to CodeableConcept
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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'party'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'resourceType'},
        ]


class ExplanationOfBenefit_Information(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_Information'

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

        reference to Coding
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'reason'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'code'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueReference'},
        ]


class ExplanationOfBenefit_CareTeam(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_CareTeam'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        Sequence of careteam which serves to order and provide a link.

        type: int
        """

        self.provider = None
        """
        The members of the team who provided the overall service.

        reference to Reference: identifier
        """

        self.responsible = None
        """
        The practitioner who is billing and responsible for the claimed
        services rendered to the patient.

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
    """

    __name__ = 'ExplanationOfBenefit_Diagnosis'

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
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'diagnosisCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'diagnosisReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'packageCode'},
        ]


class ExplanationOfBenefit_Procedure(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_Procedure'

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
    """

    __name__ = 'ExplanationOfBenefit_Insurance'

    def __init__(self, dict_values=None):
        self.coverage = None
        """
        Reference to the program or plan identification, underwriter or payor.

        reference to Reference: identifier
        """

        self.preAuthRef = None
        """
        A list of references from the Insurer to which these services pertain.

        type: array
        """

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
    """

    __name__ = 'ExplanationOfBenefit_Accident'

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
        Where the accident occurred.

        reference to Address
        """

        self.locationReference = None
        """
        Where the accident occurred.

        reference to Reference: identifier
        """

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
    """

    __name__ = 'ExplanationOfBenefit_Item'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        A service line number.

        type: int
        """

        self.careTeamLinkId = None
        """
        Careteam applicable for this service or product line.

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

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ExplanationOfBenefit_Adjudication
        """

        self.detail = None
        """
        Second tier of goods and services.

        type: array
        reference to ExplanationOfBenefit_Detail
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'net'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'udi'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'bodySite'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'encounter'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'programCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'subSite'},

            {'parent_entity': 'ExplanationOfBenefit_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'modifier'},
        ]


class ExplanationOfBenefit_Adjudication(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_Adjudication'

    def __init__(self, dict_values=None):
        self.category = None
        """
        Code indicating: Co-Pay, deductable, elegible, benefit, tax, etc.

        reference to CodeableConcept
        """

        self.reason = None
        """
        Adjudication reason such as limit reached.

        reference to CodeableConcept
        """

        self.amount = None
        """
        Monitory amount associated with the code.

        reference to Money
        """

        self.value = None
        """
        A non-monetary value for example a percentage. Mutually exclusive to
        the amount element above.

        type: int
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Adjudication',
             'child_variable': 'category'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Adjudication',
             'child_variable': 'amount'},

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
    """

    __name__ = 'ExplanationOfBenefit_Detail'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        A service line number.

        type: int
        """

        self.type = None
        """
        The type of product or service.

        reference to CodeableConcept
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

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ExplanationOfBenefit_Adjudication
        """

        self.subDetail = None
        """
        Third tier of goods and services.

        type: array
        reference to ExplanationOfBenefit_SubDetail
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'modifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'service'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'programCode'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'ExplanationOfBenefit_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'subDetail'},
        ]


class ExplanationOfBenefit_SubDetail(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_SubDetail'

    def __init__(self, dict_values=None):
        self.sequence = None
        """
        A service line number.

        type: int
        """

        self.type = None
        """
        The type of product or service.

        reference to CodeableConcept
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

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ExplanationOfBenefit_Adjudication
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'category'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'net'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'programCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'revenue'},
        ]


class ExplanationOfBenefit_AddItem(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_AddItem'

    def __init__(self, dict_values=None):
        self.sequenceLinkId = None
        """
        List of input service items which this service line is intended to
        replace.

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

        self.fee = None
        """
        The fee charged for the professional service or product.

        reference to Money
        """

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ExplanationOfBenefit_Adjudication
        """

        self.detail = None
        """
        The second tier service adjudications for payor added services.

        type: array
        reference to ExplanationOfBenefit_Detail1
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'revenue'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'fee'},

            {'parent_entity': 'ExplanationOfBenefit_Detail1',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'modifier'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'service'},
        ]


class ExplanationOfBenefit_Detail1(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_Detail1'

    def __init__(self, dict_values=None):
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

        self.fee = None
        """
        The fee charged for the professional service or product.

        reference to Money
        """

        self.noteNumber = None
        """
        A list of note references to the notes provided below.

        type: array
        """

        self.adjudication = None
        """
        The adjudications results.

        type: array
        reference to ExplanationOfBenefit_Adjudication
        """

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
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'revenue'},

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
    """

    __name__ = 'ExplanationOfBenefit_Payment'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Whether this represents partial or complete payment of the claim.

        reference to CodeableConcept
        """

        self.adjustment = None
        """
        Adjustment to the payment of this transaction which is not related to
        adjudication of this transaction.

        reference to Money
        """

        self.adjustmentReason = None
        """
        Reason for the payment adjustment.

        reference to CodeableConcept
        """

        self.date = None
        """
        Estimated payment date.

        type: string
        """

        self.amount = None
        """
        Payable less any payment adjustment.

        reference to Money
        """

        self.identifier = None
        """
        Payment identifer.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'amount'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'adjustment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'adjustmentReason'},
        ]


class ExplanationOfBenefit_ProcessNote(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_ProcessNote'

    def __init__(self, dict_values=None):
        self.number = None
        """
        An integer associated with each note which may be referred to from
        each service line item.

        type: int
        """

        self.type = None
        """
        The note purpose: Print/Display.

        reference to CodeableConcept
        """

        self.text = None
        """
        The note text.

        type: string
        """

        self.language = None
        """
        The ISO-639-1 alpha 2 code in lower case for the language, optionally
        followed by a hyphen and the ISO-3166-1 alpha 2 code for the region in
        upper case; e.g. "en" for English, or "en-US" for American English
        versus "en-EN" for England English.

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
             'child_entity': 'ExplanationOfBenefit_ProcessNote',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_ProcessNote',
             'child_variable': 'language'},
        ]


class ExplanationOfBenefit_BenefitBalance(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_BenefitBalance'

    def __init__(self, dict_values=None):
        self.category = None
        """
        Dental, Vision, Medical, Pharmacy, Rehab etc.

        reference to CodeableConcept
        """

        self.subCategory = None
        """
        Dental: basic, major, ortho; Vision exam, glasses, contacts; etc.

        reference to CodeableConcept
        """

        self.excluded = None
        """
        True if the indicated class of service is excluded from the plan,
        missing or False indicated the service is included in the coverage.

        type: boolean
        """

        self.name = None
        """
        A short name or tag for the benefit, for example MED01, or DENT2.

        type: string
        """

        self.description = None
        """
        A richer description of the benefit, for example 'DENT2 covers 100% of
        basic, 50% of major but exclused Ortho, Implants and Costmetic
        services'.

        type: string
        """

        self.network = None
        """
        Network designation.

        reference to CodeableConcept
        """

        self.unit = None
        """
        Unit designation: individual or family.

        reference to CodeableConcept
        """

        self.term = None
        """
        The term or period of the values such as 'maximum lifetime benefit' or
        'maximum annual vistis'.

        reference to CodeableConcept
        """

        self.financial = None
        """
        Benefits Used to date.

        type: array
        reference to ExplanationOfBenefit_Financial
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ExplanationOfBenefit_Financial',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'financial'},

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
             'child_variable': 'network'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'unit'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'subCategory'},
        ]


class ExplanationOfBenefit_Financial(fhirbase):
    """
    This resource provides: the claim details; adjudication details from
    the processing of a Claim; and optionally account balance information,
    for informing the subscriber of the benefits provided.
    """

    __name__ = 'ExplanationOfBenefit_Financial'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Deductable, visits, benefit amount.

        reference to CodeableConcept
        """

        self.allowedUnsignedInt = None
        """
        Benefits allowed.

        type: int
        """

        self.allowedString = None
        """
        Benefits allowed.

        type: string
        """

        self.allowedMoney = None
        """
        Benefits allowed.

        reference to Money
        """

        self.usedUnsignedInt = None
        """
        Benefits used.

        type: int
        """

        self.usedMoney = None
        """
        Benefits used.

        reference to Money
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'usedMoney'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'allowedMoney'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'type'},
        ]
