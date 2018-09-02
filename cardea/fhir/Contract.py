from .fhirbase import fhirbase


class Contract(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # this is a contract resource
        self.resourceType = 'Contract'
        # type = string
        # possible values: Contract

        # the status of the resource instance.
        self.status = None
        # type = string

        # when this  contract was issued.
        self.issued = None
        # type = string

        # relevant time or time-period when this contract is applicable.
        self.applies = None
        # reference to Period: Period

        # the target entity impacted by or of interest to parties to the
        # agreement.
        self.subject = None
        # type = array
        # reference to Reference: identifier

        # the matter of concern in the context of this agreement.
        self.topic = None
        # type = array
        # reference to Reference: identifier

        # a formally or informally recognized grouping of people, principals,
        # organizations, or jurisdictions formed for the purpose of achieving some
        # form of collective action such as the promulgation, administration and
        # enforcement of contracts and policies.
        self.authority = None
        # type = array
        # reference to Reference: identifier

        # recognized governance framework or system operating with a circumscribed
        # scope in accordance with specified principles, policies, processes or
        # procedures for managing rights, actions, or behaviors of parties or
        # principals relative to resources.
        self.domain = None
        # type = array
        # reference to Reference: identifier

        # type of contract such as an insurance policy, real estate contract, a
        # will, power of attorny, privacy or security policy , trust framework
        # agreement, etc.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # more specific type or specialization of an overarching or more general
        # contract such as auto insurance, home owner  insurance, prenupial
        # agreement, advanced-directive, or privacy consent.
        self.subType = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # action stipulated by this contract.
        self.action = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # reason for action stipulated by this contract.
        self.actionReason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the type of decision made by a grantor with respect to an offer made by
        # a grantee.
        self.decisionType = None
        # reference to CodeableConcept: CodeableConcept

        # the minimal content derived from the basal information source at a
        # specific stage in its lifecycle.
        self.contentDerivative = None
        # reference to CodeableConcept: CodeableConcept

        # a set of security labels that define which resources are controlled by
        # this consent. if more than one label is specified, all resources must
        # have all the specified labels.
        self.securityLabel = None
        # type = array
        # reference to Coding: Coding

        # an actor taking a role in an activity for which it can be assigned some
        # degree of responsibility for the activity taking place.
        self.agent = None
        # type = array
        # reference to Contract_Agent: Contract_Agent

        # parties with legal standing in the contract, including the principal
        # parties, the grantor(s) and grantee(s), which are any person or
        # organization bound by the contract, and any ancillary parties, which
        # facilitate the execution of the contract such as a notary or witness.
        self.signer = None
        # type = array
        # reference to Contract_Signer: Contract_Signer

        # contract valued item list.
        self.valuedItem = None
        # type = array
        # reference to Contract_ValuedItem: identifier

        # one or more contract provisions, which may be related and conveyed as a
        # group, and may contain nested groups.
        self.term = None
        # type = array
        # reference to Contract_Term: identifier

        # legally binding contract: this is the signed and legally recognized
        # representation of the contract, which is considered the "source of
        # truth" and which would be the basis for legal action related to
        # enforcement of this contract.
        self.bindingAttachment = None
        # reference to Attachment: Attachment

        # legally binding contract: this is the signed and legally recognized
        # representation of the contract, which is considered the "source of
        # truth" and which would be the basis for legal action related to
        # enforcement of this contract.
        self.bindingReference = None
        # reference to Reference: identifier

        # the "patient friendly language" versionof the contract in whole or in
        # parts. "patient friendly language" means the representation of the
        # contract and contract provisions in a manner that is readily accessible
        # and understandable by a layperson in accordance with best practices for
        # communication styles that ensure that those agreeing to or signing the
        # contract understand the roles, actions, obligations, responsibilities,
        # and implication of the agreement.
        self.friendly = None
        # type = array
        # reference to Contract_Friendly: Contract_Friendly

        # list of legal expressions or representations of this contract.
        self.legal = None
        # type = array
        # reference to Contract_Legal: Contract_Legal

        # list of computable policy rule language representations of this
        # contract.
        self.rule = None
        # type = array
        # reference to Contract_Rule: Contract_Rule

        # unique identifier for this contract.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'bindingReference'},

            {'parent_entity': 'Contract_Agent',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'agent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'subType'},

            {'parent_entity': 'Contract_Term',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'term'},

            {'parent_entity': 'Contract_ValuedItem',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'valuedItem'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'authority'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'decisionType'},

            {'parent_entity': 'Contract_Legal',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'legal'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'bindingAttachment'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Contract_Friendly',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'friendly'},

            {'parent_entity': 'Contract_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'rule'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'domain'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'topic'},

            {'parent_entity': 'Contract_Signer',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'signer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'contentDerivative'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'applies'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'actionReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'action'},
        ]


class Contract_Agent(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # who or what parties are assigned roles in this contract.
        self.actor = None
        # reference to Reference: identifier

        # role type of agent assigned roles in this contract.
        self.role = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Agent',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Agent',
             'child_variable': 'role'},
        ]


class Contract_Signer(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # role of this contract signer, e.g. notary, grantee.
        self.type = None
        # reference to Coding: Coding

        # party which is a signator to this contract.
        self.party = None
        # reference to Reference: identifier

        # legally binding contract dsig signature contents in base64.
        self.signature = None
        # type = array
        # reference to Signature: Signature

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Signer',
             'child_variable': 'party'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Signer',
             'child_variable': 'type'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Signer',
             'child_variable': 'signature'},
        ]


class Contract_ValuedItem(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # specific type of contract valued item that may be priced.
        self.entityCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # specific type of contract valued item that may be priced.
        self.entityReference = None
        # reference to Reference: identifier

        # indicates the time during which this contract valueditem information is
        # effective.
        self.effectiveTime = None
        # type = string

        # specifies the units by which the contract valued item is measured or
        # counted, and quantifies the countable or measurable contract valued item
        # instances.
        self.quantity = None
        # reference to Quantity: Quantity

        # a contract valued item unit valuation measure.
        self.unitPrice = None
        # reference to Money: Money

        # a real number that represents a multiplier used in determining the
        # overall value of the contract valued item delivered. the concept of a
        # factor allows for a discount or surcharge multiplier to be applied to a
        # monetary amount.
        self.factor = None
        # type = int

        # an amount that expresses the weighting (based on difficulty, cost and/or
        # resource intensiveness) associated with the contract valued item
        # delivered. the concept of points allows for assignment of point values
        # for a contract valued item, such that a monetary amount can be assigned
        # to each point.
        self.points = None
        # type = int

        # expresses the product of the contract valued item unitquantity and the
        # unitpriceamt. for example, the formula: unit quantity * unit price (cost
        # per point) * factor number  * points = net amount. quantity, factor and
        # points are assumed to be 1 if not supplied.
        self.net = None
        # reference to Money: Money

        # identifies a contract valued item instance.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'net'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'entityReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'identifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'entityCodeableConcept'},
        ]


class Contract_Term(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # when this contract provision was issued.
        self.issued = None
        # type = string

        # relevant time or time-period when this contract provision is applicable.
        self.applies = None
        # reference to Period: Period

        # type of contract provision such as specific requirements, purposes for
        # actions, obligations, prohibitions, e.g. life time maximum benefit.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # subtype of this contract provision, e.g. life time maximum payment for a
        # contract term for specific valued item, e.g. disability payment.
        self.subType = None
        # reference to CodeableConcept: CodeableConcept

        # the matter of concern in the context of this provision of the agrement.
        self.topic = None
        # type = array
        # reference to Reference: identifier

        # action stipulated by this contract provision.
        self.action = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # reason or purpose for the action stipulated by this contract provision.
        self.actionReason = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a set of security labels that define which terms are controlled by this
        # condition.
        self.securityLabel = None
        # type = array
        # reference to Coding: Coding

        # an actor taking a role in an activity for which it can be assigned some
        # degree of responsibility for the activity taking place.
        self.agent = None
        # type = array
        # reference to Contract_Agent1: Contract_Agent1

        # human readable form of this contract provision.
        self.text = None
        # type = string

        # contract provision valued item list.
        self.valuedItem = None
        # type = array
        # reference to Contract_ValuedItem1: identifier

        # nested group of contract provisions.
        self.group = None
        # type = array
        # reference to Contract_Term: identifier

        # unique identifier for this particular contract provision.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'topic'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'actionReason'},

            {'parent_entity': 'Contract_Agent1',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'agent'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'applies'},

            {'parent_entity': 'Contract_ValuedItem1',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'valuedItem'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'type'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'subType'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'action'},

            {'parent_entity': 'Contract_Term',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'group'},
        ]


class Contract_Agent1(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # the agent assigned a role in this contract provision.
        self.actor = None
        # reference to Reference: identifier

        # role played by the agent assigned this role in the execution of this
        # contract provision.
        self.role = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Agent1',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Agent1',
             'child_variable': 'role'},
        ]


class Contract_ValuedItem1(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # specific type of contract provision valued item that may be priced.
        self.entityCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # specific type of contract provision valued item that may be priced.
        self.entityReference = None
        # reference to Reference: identifier

        # indicates the time during which this contract term valueditem
        # information is effective.
        self.effectiveTime = None
        # type = string

        # specifies the units by which the contract provision valued item is
        # measured or counted, and quantifies the countable or measurable contract
        # term valued item instances.
        self.quantity = None
        # reference to Quantity: Quantity

        # a contract provision valued item unit valuation measure.
        self.unitPrice = None
        # reference to Money: Money

        # a real number that represents a multiplier used in determining the
        # overall value of the contract provision valued item delivered. the
        # concept of a factor allows for a discount or surcharge multiplier to be
        # applied to a monetary amount.
        self.factor = None
        # type = int

        # an amount that expresses the weighting (based on difficulty, cost and/or
        # resource intensiveness) associated with the contract provision valued
        # item delivered. the concept of points allows for assignment of point
        # values for a contract provisionvalued item, such that a monetary amount
        # can be assigned to each point.
        self.points = None
        # type = int

        # expresses the product of the contract provision valued item unitquantity
        # and the unitpriceamt. for example, the formula: unit quantity * unit
        # price (cost per point) * factor number  * points = net amount. quantity,
        # factor and points are assumed to be 1 if not supplied.
        self.net = None
        # reference to Money: Money

        # identifies a contract provision valued item instance.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'entityCodeableConcept'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'net'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'identifier'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'quantity'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'entityReference'},
        ]


class Contract_Friendly(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # human readable rendering of this contract in a format and representation
        # intended to enhance comprehension and ensure understandability.
        self.contentAttachment = None
        # reference to Attachment: Attachment

        # human readable rendering of this contract in a format and representation
        # intended to enhance comprehension and ensure understandability.
        self.contentReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Friendly',
             'child_variable': 'contentAttachment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Friendly',
             'child_variable': 'contentReference'},
        ]


class Contract_Legal(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # contract legal text in human renderable form.
        self.contentAttachment = None
        # reference to Attachment: Attachment

        # contract legal text in human renderable form.
        self.contentReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Legal',
             'child_variable': 'contentAttachment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Legal',
             'child_variable': 'contentReference'},
        ]


class Contract_Rule(fhirbase):
    """A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    def __init__(self, dict_values=None):
        # computable contract conveyed using a policy rule language (e.g. xacml,
        # dkal, secpal).
        self.contentAttachment = None
        # reference to Attachment: Attachment

        # computable contract conveyed using a policy rule language (e.g. xacml,
        # dkal, secpal).
        self.contentReference = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Rule',
             'child_variable': 'contentAttachment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Rule',
             'child_variable': 'contentReference'},
        ]
