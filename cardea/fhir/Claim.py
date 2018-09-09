from .fhirbase import fhirbase


class Claim(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    def __init__(self, dict_values=None):
        # this is a claim resource
        self.resourceType = 'Claim'
        # type = string
        # possible values: Claim

        # the status of the resource instance.
        self.status = None
        # type = string

        # the category of claim, eg, oral, pharmacy, vision, insitutional,
        # professional.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # a finer grained suite of claim subtype codes which may convey inpatient
        # vs outpatient and/or a specialty service. in the us the billtype.
        self.subType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # complete (bill or claim), proposed (pre-authorization), exploratory
        # (pre-determination).
        self.use = None
        # type = string
        # possible values: complete, proposed, exploratory, other

        # patient resource.
        self.patient = None
        # reference to Reference: identifier

        # the billable period for which charges are being submitted.
        self.billablePeriod = None
        # reference to Period: Period

        # the date when the enclosed suite of services were performed or
        # completed.
        self.created = None
        # type = string

        # person who created the invoice/claim/pre-determination or pre-
        # authorization.
        self.enterer = None
        # reference to Reference: identifier

        # the insurer who is target of the request.
        self.insurer = None
        # reference to Reference: identifier

        # the provider which is responsible for the bill, claim pre-determination,
        # pre-authorization.
        self.provider = None
        # reference to Reference: identifier

        # the organization which is responsible for the bill, claim pre-
        # determination, pre-authorization.
        self.organization = None
        # reference to Reference: identifier

        # immediate (stat), best effort (normal), deferred (defer).
        self.priority = None
        # reference to CodeableConcept: CodeableConcept

        # in the case of a pre-determination/pre-authorization the provider may
        # request that funds in the amount of the expected benefit be reserved
        # ('patient' or 'provider') to pay for the benefits determined on the
        # subsequent claim(s). 'none' explicitly indicates no funds reserving is
        # requested.
        self.fundsReserve = None
        # reference to CodeableConcept: CodeableConcept

        # other claims which are related to this claim such as prior claim
        # versions or for related services.
        self.related = None
        # type = array
        # reference to Claim_Related: Claim_Related

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
        # reference to Claim_Payee: Claim_Payee

        # the referral resource which lists the date, practitioner, reason and
        # other supporting information.
        self.referral = None
        # reference to Reference: identifier

        # facility where the services were provided.
        self.facility = None
        # reference to Reference: identifier

        # the members of the team who provided the overall service as well as
        # their role and whether responsible and qualifications.
        self.careTeam = None
        # type = array
        # reference to Claim_CareTeam: Claim_CareTeam

        # additional information codes regarding exceptions, special
        # considerations, the condition, situation, prior or concurrent issues.
        # often there are mutiple jurisdiction specific valuesets which are
        # required.
        self.information = None
        # type = array
        # reference to Claim_Information: Claim_Information

        # list of patient diagnosis for which care is sought.
        self.diagnosis = None
        # type = array
        # reference to Claim_Diagnosis: Claim_Diagnosis

        # ordered list of patient procedures performed to support the
        # adjudication.
        self.procedure = None
        # type = array
        # reference to Claim_Procedure: Claim_Procedure

        # financial instrument by which payment information for health care.
        self.insurance = None
        # type = array
        # reference to Claim_Insurance: Claim_Insurance

        # an accident which resulted in the need for healthcare services.
        self.accident = None
        # reference to Claim_Accident: Claim_Accident

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
        # reference to Claim_Item: Claim_Item

        # the total value of the claim.
        self.total = None
        # reference to Money: Money

        # the business identifier for the instance: claim number, pre-
        # determination or pre-authorization number.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'hospitalization'},

            {'parent_entity': 'Claim_Related',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'related'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'referral'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'originalPrescription'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'billablePeriod'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'prescription'},

            {'parent_entity': 'Claim_Accident',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'accident'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'total'},

            {'parent_entity': 'Claim_Insurance',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'insurance'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'priority'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'fundsReserve'},

            {'parent_entity': 'Claim_Payee',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'payee'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'employmentImpacted'},

            {'parent_entity': 'Claim_Procedure',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'procedure'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'insurer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'patient'},

            {'parent_entity': 'Claim_Information',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'information'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'provider'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'subType'},

            {'parent_entity': 'Claim_CareTeam',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'careTeam'},

            {'parent_entity': 'Claim_Item',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'item'},

            {'parent_entity': 'Claim_Diagnosis',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'diagnosis'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'enterer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim',
             'child_variable': 'facility'},
        ]


class Claim_Related(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Related',
             'child_variable': 'claim'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Related',
             'child_variable': 'relationship'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Related',
             'child_variable': 'reference'},
        ]


class Claim_Payee(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    def __init__(self, dict_values=None):
        # type of party to be reimbursed: subscriber, provider, other.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # organization | patient | practitioner | relatedperson.
        self.resourceType = None
        # reference to Coding: Coding

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
             'child_entity': 'Claim_Payee',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Payee',
             'child_variable': 'party'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Payee',
             'child_variable': 'resourceType'},
        ]


class Claim_CareTeam(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    def __init__(self, dict_values=None):
        # sequence of the careteam which serves to order and provide a link.
        self.sequence = None
        # type = int

        # member of the team who provided the overall service.
        self.provider = None
        # reference to Reference: identifier

        # the party who is billing and responsible for the claimed good or service
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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'provider'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_CareTeam',
             'child_variable': 'qualification'},
        ]


class Claim_Information(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
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
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

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
             'child_variable': 'code'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Information',
             'child_variable': 'valueReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Information',
             'child_variable': 'reason'},
        ]


class Claim_Diagnosis(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'diagnosisReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'diagnosisCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Diagnosis',
             'child_variable': 'packageCode'},
        ]


class Claim_Procedure(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
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
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    def __init__(self, dict_values=None):
        # sequence of coverage which serves to provide a link and convey
        # coordination of benefit order.
        self.sequence = None
        # type = int

        # a flag to indicate that this coverage is the focus for adjudication. the
        # coverage against which the claim is to be adjudicated.
        self.focal = None
        # type = boolean

        # reference to the program or plan identification, underwriter or payor.
        self.coverage = None
        # reference to Reference: identifier

        # the contract number of a business agreement which describes the terms
        # and conditions.
        self.businessArrangement = None
        # type = string

        # a list of references from the insurer to which these services pertain.
        self.preAuthRef = None
        # type = array

        # the coverages adjudication details.
        self.claimResponse = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Insurance',
             'child_variable': 'coverage'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Insurance',
             'child_variable': 'claimResponse'},
        ]


class Claim_Accident(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    def __init__(self, dict_values=None):
        # date of an accident which these services are addressing.
        self.date = None
        # type = string

        # type of accident: work, auto, etc.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # accident place.
        self.locationAddress = None
        # reference to Address: Address

        # accident place.
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
             'child_entity': 'Claim_Accident',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Accident',
             'child_variable': 'locationReference'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Accident',
             'child_variable': 'locationAddress'},
        ]


class Claim_Item(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
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
        # hcpcs,uscls,icd10, ncpdp,din,rxnorm,achi,cci). if a grouping item then
        # use a group code to indicate the type of thing being grouped eg.
        # 'glasses' or 'compound'.
        self.service = None
        # reference to CodeableConcept: CodeableConcept

        # item typification or modifiers codes, eg for oral whether the treatment
        # is cosmetic or associated with tmj, or for medical whether the treatment
        # was outside the clinic or out of office hours.
        self.modifier = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # for programs which require reason codes for the inclusion or covering of
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

        # second tier of goods and services.
        self.detail = None
        # type = array
        # reference to Claim_Detail: Claim_Detail

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'subSite'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'service'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'encounter'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'udi'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'revenue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'programCode'},

            {'parent_entity': 'Address',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationAddress'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'servicedPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Item',
             'child_variable': 'locationReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'modifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Claim_Detail',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Item',
             'child_variable': 'detail'},
        ]


class Claim_Detail(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequence = None
        # type = int

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

        # third tier of goods and services.
        self.subDetail = None
        # type = array
        # reference to Claim_SubDetail: Claim_SubDetail

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Claim_SubDetail',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'subDetail'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_Detail',
             'child_variable': 'udi'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'net'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'modifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'programCode'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_Detail',
             'child_variable': 'revenue'},
        ]


class Claim_SubDetail(fhirbase):
    """A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """

    def __init__(self, dict_values=None):
        # a service line number.
        self.sequence = None
        # type = int

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

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'category'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'revenue'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'programCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'udi'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'service'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Claim_SubDetail',
             'child_variable': 'modifier'},
        ]
