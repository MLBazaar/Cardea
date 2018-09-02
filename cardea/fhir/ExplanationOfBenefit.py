from .fhirbase import fhirbase


class ExplanationOfBenefit(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # this is a explanationofbenefit resource
        self.resourceType = 'ExplanationOfBenefit'
        # type = string
        # possible values: ExplanationOfBenefit

        # the status of the resource instance.
        self.status = None
        # type = string
        # possible values: active, cancelled, draft, entered-in-error

        # the category of claim, eg, oral, pharmacy, vision, insitutional,
        # professional.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # a finer grained suite of claim subtype codes which may convey inpatient
        # vs outpatient and/or a specialty service. in the us the billtype.
        self.subType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # patient resource.
        self.patient = None
        # reference to Reference: identifier

        # the billable period for which charges are being submitted.
        self.billablePeriod = None
        # reference to Period: Period

        # the date when the eob was created.
        self.created = None
        # type = string

        # the person who created the explanation of benefit.
        self.enterer = None
        # reference to Reference: identifier

        # the insurer which is responsible for the explanation of benefit.
        self.insurer = None
        # reference to Reference: identifier

        # the provider which is responsible for the claim.
        self.provider = None
        # reference to Reference: identifier

        # the provider which is responsible for the claim.
        self.organization = None
        # reference to Reference: identifier

        # the referral resource which lists the date, practitioner, reason and
        # other supporting information.
        self.referral = None
        # reference to Reference: identifier

        # facility where the services were provided.
        self.facility = None
        # reference to Reference: identifier

        # the business identifier for the instance: invoice number, claim number,
        # pre-determination or pre-authorization number.
        self.claim = None
        # reference to Reference: identifier

        # the business identifier for the instance: invoice number, claim number,
        # pre-determination or pre-authorization number.
        self.claimResponse = None
        # reference to Reference: identifier

        # processing outcome errror, partial or complete processing.
        self.outcome = None
        # reference to CodeableConcept: CodeableConcept

        # a description of the status of the adjudication.
        self.disposition = None
        # type = string

        # other claims which are related to this claim such as prior claim
        # versions or for related services.
        self.related = None
        # type = array
        # reference to ExplanationOfBenefit_Related: ExplanationOfBenefit_Related

        # prescription to support the dispensing of pharmacy or vision products.
        self.prescription = None
        # reference to Reference: identifier

        # original prescription which has been superceded by this prescription to
        # support the dispensing of pharmacy services, medications or products.
        # for example, a physician may prescribe a medication which the pharmacy
        # determines is contraindicated, or for which the patient has an
        # intolerance, and therefor issues a new precription for an alternate
        # medication which has the same theraputic intent. the prescription from
        # the pharmacy becomes the 'prescription' and that from the physician
        # becomes the 'original prescription'.
        self.originalPrescription = None
        # reference to Reference: identifier

        # the party to be reimbursed for the services.
        self.payee = None
        # reference to ExplanationOfBenefit_Payee: ExplanationOfBenefit_Payee

        # additional information codes regarding exceptions, special
        # considerations, the condition, situation, prior or concurrent issues.
        # often there are mutiple jurisdiction specific valuesets which are
        # required.
        self.information = None
        # type = array
        # reference to ExplanationOfBenefit_Information: ExplanationOfBenefit_Information

        # the members of the team who provided the overall service as well as
        # their role and whether responsible and qualifications.
        self.careTeam = None
        # type = array
        # reference to ExplanationOfBenefit_CareTeam: ExplanationOfBenefit_CareTeam

        # ordered list of patient diagnosis for which care is sought.
        self.diagnosis = None
        # type = array
        # reference to ExplanationOfBenefit_Diagnosis: ExplanationOfBenefit_Diagnosis

        # ordered list of patient procedures performed to support the
        # adjudication.
        self.procedure = None
        # type = array
        # reference to ExplanationOfBenefit_Procedure: ExplanationOfBenefit_Procedure

        # precedence (primary, secondary, etc.).
        self.precedence = None
        # type = int

        # financial instrument by which payment information for health care.
        self.insurance = None
        # reference to ExplanationOfBenefit_Insurance: ExplanationOfBenefit_Insurance

        # an accident which resulted in the need for healthcare services.
        self.accident = None
        # reference to ExplanationOfBenefit_Accident: ExplanationOfBenefit_Accident

        # the start and optional end dates of when the patient was precluded from
        # working due to the treatable condition(s).
        self.employmentImpacted = None
        # reference to Period: Period

        # the start and optional end dates of when the patient was confined to a
        # treatment center.
        self.hospitalization = None
        # reference to Period: Period

        # first tier of goods and services.
        self.item = None
        # type = array
        # reference to ExplanationOfBenefit_Item: ExplanationOfBenefit_Item

        # the first tier service adjudications for payor added services.
        self.addItem = None
        # type = array
        # reference to ExplanationOfBenefit_AddItem: ExplanationOfBenefit_AddItem

        # the total cost of the services reported.
        self.totalCost = None
        # reference to Money: Money

        # the amount of deductable applied which was not allocated to any
        # particular service line.
        self.unallocDeductable = None
        # reference to Money: Money

        # total amount of benefit payable (equal to sum of the benefit amounts
        # from all detail lines and additions less the unallocated deductable).
        self.totalBenefit = None
        # reference to Money: Money

        # payment details for the claim if the claim has been paid.
        self.payment = None
        # reference to ExplanationOfBenefit_Payment: identifier

        # the form to be used for printing the content.
        self.form = None
        # reference to CodeableConcept: CodeableConcept

        # note text.
        self.processNote = None
        # type = array
        # reference to ExplanationOfBenefit_ProcessNote: ExplanationOfBenefit_ProcessNote

        # balance by benefit category.
        self.benefitBalance = None
        # type = array
        # reference to ExplanationOfBenefit_BenefitBalance: ExplanationOfBenefit_BenefitBalance

        # the eob business identifier.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'enterer'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'ExplanationOfBenefit_BenefitBalance',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'benefitBalance'},

            {'parent_entity': 'ExplanationOfBenefit_CareTeam',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'careTeam'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'facility'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'claim'},

            {'parent_entity': 'ExplanationOfBenefit_Accident',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'accident'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'organization'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'subType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'originalPrescription'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'referral'},

            {'parent_entity': 'ExplanationOfBenefit_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'insurance'},

            {'parent_entity': 'ExplanationOfBenefit_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'ExplanationOfBenefit_Payment',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'payment'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'totalCost'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'billablePeriod'},

            {'parent_entity': 'ExplanationOfBenefit_Information',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'information'},

            {'parent_entity': 'ExplanationOfBenefit_ProcessNote',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'processNote'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'employmentImpacted'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'unallocDeductable'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'insurer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'claimResponse'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'outcome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'form'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'provider'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'patient'},

            {'parent_entity': 'ExplanationOfBenefit_Procedure',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'procedure'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'prescription'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'totalBenefit'},

            {'parent_entity': 'ExplanationOfBenefit_Related',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'related'},

            {'parent_entity': 'ExplanationOfBenefit_Item',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'item'},

            {'parent_entity': 'ExplanationOfBenefit_AddItem',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'addItem'},

            {'parent_entity': 'ExplanationOfBenefit_Payee',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit',
             'child_variable': 'payee'},
        ]


class ExplanationOfBenefit_Related(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # other claims which are related to this claim such as prior claim
        # versions or for related services.
        self.claim = None
        # reference to Reference: identifier

        # for example prior or umbrella.
        self.relationship = None
        # reference to CodeableConcept: CodeableConcept

        # an alternate organizational reference to the case or file to which this
        # particular claim pertains - eg property/casualy insurer claim # or
        # workers compensation case # .
        self.reference = None
        # reference to Identifier: Identifier

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # type of party to be reimbursed: subscriber, provider, other.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # organization | patient | practitioner | relatedperson.
        self.resourceType = None
        # reference to CodeableConcept: CodeableConcept

        # party to be reimbursed: subscriber, provider, other.
        self.party = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'resourceType'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Payee',
             'child_variable': 'party'},
        ]


class ExplanationOfBenefit_Information(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # sequence of the information element which serves to provide a link.
        self.sequence = None
        # type = int

        # the general class of the information supplied: information; exception;
        # accident, employment; onset, etc.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # system and code pertaining to the specific information regarding special
        # conditions relating to the setting, treatment or patient  for which care
        # is sought which may influence the adjudication.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the date when or period to which this information refers.
        self.timingDate = None
        # type = string

        # the date when or period to which this information refers.
        self.timingPeriod = None
        # reference to Period: Period

        # additional data or information such as resources, documents, images etc.
        # including references to the data or the actual inclusion of the data.
        self.valueString = None
        # type = string

        # additional data or information such as resources, documents, images etc.
        # including references to the data or the actual inclusion of the data.
        self.valueQuantity = None
        # reference to Quantity: Quantity

        # additional data or information such as resources, documents, images etc.
        # including references to the data or the actual inclusion of the data.
        self.valueAttachment = None
        # reference to Attachment: Attachment

        # additional data or information such as resources, documents, images etc.
        # including references to the data or the actual inclusion of the data.
        self.valueReference = None
        # reference to Reference: identifier

        # for example, provides the reason for: the additional stay, or missing
        # tooth or any other situation where a reason code is required in addition
        # to the content.
        self.reason = None
        # reference to Coding: Coding

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'code'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'category'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Information',
             'child_variable': 'reason'},
        ]


class ExplanationOfBenefit_CareTeam(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # sequence of careteam which serves to order and provide a link.
        self.sequence = None
        # type = int

        # the members of the team who provided the overall service.
        self.provider = None
        # reference to Reference: identifier

        # the practitioner who is billing and responsible for the claimed services
        # rendered to the patient.
        self.responsible = None
        # type = boolean

        # the lead, assisting or supervising practitioner and their discipline if
        # a multidisiplinary team.
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the qualification which is applicable for this service.
        self.qualification = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

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
             'child_variable': 'qualification'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_CareTeam',
             'child_variable': 'role'},
        ]


class ExplanationOfBenefit_Diagnosis(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # sequence of diagnosis which serves to provide a link.
        self.sequence = None
        # type = int

        # the diagnosis.
        self.diagnosisCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the diagnosis.
        self.diagnosisReference = None
        # reference to Reference: identifier

        # the type of the diagnosis, for example: admitting, primary, secondary,
        # discharge.
        self.type = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the package billing code, for example drg, based on the assigned
        # grouping code system.
        self.packageCode = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Diagnosis',
             'child_variable': 'packageCode'},

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
             'child_variable': 'diagnosisCodeableConcept'},
        ]


class ExplanationOfBenefit_Procedure(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # sequence of procedures which serves to order and provide a link.
        self.sequence = None
        # type = int

        # date and optionally time the procedure was performed .
        self.date = None
        # type = string

        # the procedure code.
        self.procedureCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # the procedure code.
        self.procedureReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Procedure',
             'child_variable': 'procedureReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Procedure',
             'child_variable': 'procedureCodeableConcept'},
        ]


class ExplanationOfBenefit_Insurance(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # reference to the program or plan identification, underwriter or payor.
        self.coverage = None
        # reference to Reference: identifier

        # a list of references from the insurer to which these services pertain.
        self.preAuthRef = None
        # type = array

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # date of an accident which these services are addressing.
        self.date = None
        # type = string

        # type of accident: work, auto, etc.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # where the accident occurred.
        self.locationAddress = None
        # reference to Address: Address

        # where the accident occurred.
        self.locationReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Accident',
             'child_variable': 'type'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Accident',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Accident',
             'child_variable': 'locationReference'},
        ]


class ExplanationOfBenefit_Item(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequence = None
        # type = int

        # careteam applicable for this service or product line.
        self.careTeamLinkId = None
        # type = array

        # diagnosis applicable for this service or product line.
        self.diagnosisLinkId = None
        # type = array

        # procedures applicable for this service or product line.
        self.procedureLinkId = None
        # type = array

        # exceptions, special conditions and supporting information pplicable for
        # this service or product line.
        self.informationLinkId = None
        # type = array

        # the type of reveneu or cost center providing the product and/or service.
        self.revenue = None
        # reference to CodeableConcept: CodeableConcept

        # health care service type codes  to identify the classification of
        # service or benefits.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # if this is an actual service or product line, ie. not a group, then use
        # code to indicate the professional service or product supplied (eg. ctp,
        # hcpcs,uscls,icd10, ncpdp,din,achi,cci). if a grouping item then use a
        # group code to indicate the type of thing being grouped eg. 'glasses' or
        # 'compound'.
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # for programs which require reson codes for the inclusion, covering, of
        # this billed item under the program or sub-program.
        self.programCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the date or dates when the enclosed suite of services were performed or
        # completed.
        self.servicedDate = None
        # type = string

        # the date or dates when the enclosed suite of services were performed or
        # completed.
        self.servicedPeriod = None
        # reference to Period: Period

        # where the service was provided.
        self.locationCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # where the service was provided.
        self.locationAddress = None
        # reference to Address: Address

        # where the service was provided.
        self.locationReference = None
        # reference to Reference: identifier

        # the number of repetitions of a service or product.
        self.quantity = None
        # reference to Quantity: Quantity

        # if the item is a node then this is the fee for the product or service,
        # otherwise this is the total of the fees for the children of the group.
        self.unitPrice = None
        # reference to Money: Money

        # a real number that represents a multiplier used in determining the
        # overall value of services delivered and/or goods received. the concept
        # of a factor allows for a discount or surcharge multiplier to be applied
        # to a monetary amount.
        self.factor = None
        # type = int

        # the quantity times the unit price for an addittional service or product
        # or charge. for example, the formula: unit quantity * unit price (cost
        # per point) * factor number  * points = net amount. quantity, factor and
        # points are assumed to be 1 if not supplied.
        self.net = None
        # reference to Money: Money

        # list of unique device identifiers associated with this line item.
        self.udi = None
        # type = array
        # reference to Reference: identifier

        # physical service site on the patient (limb, tooth, etc).
        self.bodySite = None
        # reference to CodeableConcept: CodeableConcept

        # a region or surface of the site, eg. limb region or tooth surface(s).
        self.subSite = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a billed item may include goods or services provided in multiple
        # encounters.
        self.encounter = None
        # type = array
        # reference to Reference: identifier

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ExplanationOfBenefit_Adjudication: ExplanationOfBenefit_Adjudication

        # second tier of goods and services.
        self.detail = None
        # type = array
        # reference to ExplanationOfBenefit_Detail: ExplanationOfBenefit_Detail

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'net'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationCodeableConcept'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'locationReference'},

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

            {'parent_entity': 'ExplanationOfBenefit_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'detail'},

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
             'child_variable': 'encounter'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'programCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'udi'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'revenue'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Item',
             'child_variable': 'subSite'},
        ]


class ExplanationOfBenefit_Adjudication(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # code indicating: co-pay, deductable, elegible, benefit, tax, etc.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # adjudication reason such as limit reached.
        self.reason = None
        # reference to CodeableConcept: CodeableConcept

        # monitory amount associated with the code.
        self.amount = None
        # reference to Money: Money

        # a non-monetary value for example a percentage. mutually exclusive to the
        # amount element above.
        self.value = None
        # type = int

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequence = None
        # type = int

        # the type of product or service.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the type of reveneu or cost center providing the product and/or service.
        self.revenue = None
        # reference to CodeableConcept: CodeableConcept

        # health care service type codes  to identify the classification of
        # service or benefits.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # if this is an actual service or product line, ie. not a group, then use
        # code to indicate the professional service or product supplied (eg. ctp,
        # hcpcs,uscls,icd10, ncpdp,din,achi,cci). if a grouping item then use a
        # group code to indicate the type of thing being grouped eg. 'glasses' or
        # 'compound'.
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # for programs which require reson codes for the inclusion, covering, of
        # this billed item under the program or sub-program.
        self.programCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the number of repetitions of a service or product.
        self.quantity = None
        # reference to Quantity: Quantity

        # if the item is a node then this is the fee for the product or service,
        # otherwise this is the total of the fees for the children of the group.
        self.unitPrice = None
        # reference to Money: Money

        # a real number that represents a multiplier used in determining the
        # overall value of services delivered and/or goods received. the concept
        # of a factor allows for a discount or surcharge multiplier to be applied
        # to a monetary amount.
        self.factor = None
        # type = int

        # the quantity times the unit price for an addittional service or product
        # or charge. for example, the formula: unit quantity * unit price (cost
        # per point) * factor number  * points = net amount. quantity, factor and
        # points are assumed to be 1 if not supplied.
        self.net = None
        # reference to Money: Money

        # list of unique device identifiers associated with this line item.
        self.udi = None
        # type = array
        # reference to Reference: identifier

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ExplanationOfBenefit_Adjudication: ExplanationOfBenefit_Adjudication

        # third tier of goods and services.
        self.subDetail = None
        # type = array
        # reference to ExplanationOfBenefit_SubDetail: ExplanationOfBenefit_SubDetail

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'programCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'revenue'},

            {'parent_entity': 'ExplanationOfBenefit_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'subDetail'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'net'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail',
             'child_variable': 'service'},
        ]


class ExplanationOfBenefit_SubDetail(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequence = None
        # type = int

        # the type of product or service.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the type of reveneu or cost center providing the product and/or service.
        self.revenue = None
        # reference to CodeableConcept: CodeableConcept

        # health care service type codes  to identify the classification of
        # service or benefits.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # a code to indicate the professional service or product supplied (eg.
        # ctp, hcpcs,uscls,icd10, ncpdp,din,achi,cci).
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # for programs which require reson codes for the inclusion, covering, of
        # this billed item under the program or sub-program.
        self.programCode = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the number of repetitions of a service or product.
        self.quantity = None
        # reference to Quantity: Quantity

        # the fee for an addittional service or product or charge.
        self.unitPrice = None
        # reference to Money: Money

        # a real number that represents a multiplier used in determining the
        # overall value of services delivered and/or goods received. the concept
        # of a factor allows for a discount or surcharge multiplier to be applied
        # to a monetary amount.
        self.factor = None
        # type = int

        # the quantity times the unit price for an addittional service or product
        # or charge. for example, the formula: unit quantity * unit price (cost
        # per point) * factor number  * points = net amount. quantity, factor and
        # points are assumed to be 1 if not supplied.
        self.net = None
        # reference to Money: Money

        # list of unique device identifiers associated with this line item.
        self.udi = None
        # type = array
        # reference to Reference: identifier

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ExplanationOfBenefit_Adjudication: ExplanationOfBenefit_Adjudication

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'programCode'},

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
             'child_variable': 'category'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'type'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'adjudication'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'udi'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_SubDetail',
             'child_variable': 'service'},
        ]


class ExplanationOfBenefit_AddItem(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # list of input service items which this service line is intended to
        # replace.
        self.sequenceLinkId = None
        # type = array

        # the type of reveneu or cost center providing the product and/or service.
        self.revenue = None
        # reference to CodeableConcept: CodeableConcept

        # health care service type codes  to identify the classification of
        # service or benefits.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # if this is an actual service or product line, ie. not a group, then use
        # code to indicate the professional service or product supplied (eg. ctp,
        # hcpcs,uscls,icd10, ncpdp,din,achi,cci). if a grouping item then use a
        # group code to indicate the type of thing being grouped eg. 'glasses' or
        # 'compound'.
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the fee charged for the professional service or product.
        self.fee = None
        # reference to Money: Money

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ExplanationOfBenefit_Adjudication: ExplanationOfBenefit_Adjudication

        # the second tier service adjudications for payor added services.
        self.detail = None
        # type = array
        # reference to ExplanationOfBenefit_Detail1: ExplanationOfBenefit_Detail1

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'service'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'modifier'},

            {'parent_entity': 'ExplanationOfBenefit_Detail1',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'detail'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'category'},

            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_AddItem',
             'child_variable': 'adjudication'},
        ]


class ExplanationOfBenefit_Detail1(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # the type of reveneu or cost center providing the product and/or service.
        self.revenue = None
        # reference to CodeableConcept: CodeableConcept

        # health care service type codes  to identify the classification of
        # service or benefits.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # a code to indicate the professional service or product supplied (eg.
        # ctp, hcpcs,uscls,icd10, ncpdp,din,achi,cci).
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the fee charged for the professional service or product.
        self.fee = None
        # reference to Money: Money

        # a list of note references to the notes provided below.
        self.noteNumber = None
        # type = array

        # the adjudications results.
        self.adjudication = None
        # type = array
        # reference to ExplanationOfBenefit_Adjudication: ExplanationOfBenefit_Adjudication

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ExplanationOfBenefit_Adjudication',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'adjudication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'service'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'fee'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Detail1',
             'child_variable': 'modifier'},
        ]


class ExplanationOfBenefit_Payment(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # whether this represents partial or complete payment of the claim.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # adjustment to the payment of this transaction which is not related to
        # adjudication of this transaction.
        self.adjustment = None
        # reference to Money: Money

        # reason for the payment adjustment.
        self.adjustmentReason = None
        # reference to CodeableConcept: CodeableConcept

        # estimated payment date.
        self.date = None
        # type = string

        # payable less any payment adjustment.
        self.amount = None
        # reference to Money: Money

        # payment identifer.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'adjustmentReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'adjustment'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'amount'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Payment',
             'child_variable': 'identifier'},
        ]


class ExplanationOfBenefit_ProcessNote(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # an integer associated with each note which may be referred to from each
        # service line item.
        self.number = None
        # type = int

        # the note purpose: print/display.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the note text.
        self.text = None
        # type = string

        # the iso-639-1 alpha 2 code in lower case for the language, optionally
        # followed by a hyphen and the iso-3166-1 alpha 2 code for the region in
        # upper case; e.g. "en" for english, or "en-us" for american english
        # versus "en-en" for england english.
        self.language = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

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
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # dental, vision, medical, pharmacy, rehab etc.
        self.category = None
        # reference to CodeableConcept: CodeableConcept

        # dental: basic, major, ortho; vision exam, glasses, contacts; etc.
        self.subCategory = None
        # reference to CodeableConcept: CodeableConcept

        # true if the indicated class of service is excluded from the plan,
        # missing or false indicated the service is included in the coverage.
        self.excluded = None
        # type = boolean

        # a short name or tag for the benefit, for example med01, or dent2.
        self.name = None
        # type = string

        # a richer description of the benefit, for example 'dent2 covers 100% of
        # basic, 50% of major but exclused ortho, implants and costmetic
        # services'.
        self.description = None
        # type = string

        # network designation.
        self.network = None
        # reference to CodeableConcept: CodeableConcept

        # unit designation: individual or family.
        self.unit = None
        # reference to CodeableConcept: CodeableConcept

        # the term or period of the values such as 'maximum lifetime benefit' or
        # 'maximum annual vistis'.
        self.term = None
        # reference to CodeableConcept: CodeableConcept

        # benefits used to date.
        self.financial = None
        # type = array
        # reference to ExplanationOfBenefit_Financial: ExplanationOfBenefit_Financial

        # unique identifier for object class
        self.object_id = None

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
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'unit'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'network'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'term'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_BenefitBalance',
             'child_variable': 'subCategory'},
        ]


class ExplanationOfBenefit_Financial(fhirbase):
    """This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    def __init__(self, dict_values=None):
        # deductable, visits, benefit amount.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # benefits allowed.
        self.allowedUnsignedInt = None
        # type = int

        # benefits allowed.
        self.allowedString = None
        # type = string

        # benefits allowed.
        self.allowedMoney = None
        # reference to Money: Money

        # benefits used.
        self.usedUnsignedInt = None
        # type = int

        # benefits used.
        self.usedMoney = None
        # reference to Money: Money

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'allowedMoney'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'type'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'ExplanationOfBenefit_Financial',
             'child_variable': 'usedMoney'},
        ]
