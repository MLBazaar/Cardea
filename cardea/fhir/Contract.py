from .fhirbase import fhirbase


class Contract(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        resourceType: This is a Contract resource
        identifier: Unique identifier for this Contract.
        status: The status of the resource instance.
        issued: When this  Contract was issued.
        applies: Relevant time or time-period when this Contract is
            applicable.
        subject: The target entity impacted by or of interest to parties to
            the agreement.
        topic: The matter of concern in the context of this agreement.
        authority: A formally or informally recognized grouping of people,
            principals, organizations, or jurisdictions formed for the purpose of
            achieving some form of collective action such as the promulgation,
            administration and enforcement of contracts and policies.
        domain: Recognized governance framework or system operating with a
            circumscribed scope in accordance with specified principles, policies,
            processes or procedures for managing rights, actions, or behaviors of
            parties or principals relative to resources.
        type: Type of Contract such as an insurance policy, real estate
            contract, a will, power of attorny, Privacy or Security policy , trust
            framework agreement, etc.
        subType: More specific type or specialization of an overarching or
            more general contract such as auto insurance, home owner  insurance,
            prenupial agreement, Advanced-Directive, or privacy consent.
        action: Action stipulated by this Contract.
        actionReason: Reason for action stipulated by this Contract.
        decisionType: The type of decision made by a grantor with respect to
            an offer made by a grantee.
        contentDerivative: The minimal content derived from the basal
            information source at a specific stage in its lifecycle.
        securityLabel: A set of security labels that define which resources
            are controlled by this consent. If more than one label is specified,
            all resources must have all the specified labels.
        agent: An actor taking a role in an activity for which it can be
            assigned some degree of responsibility for the activity taking place.
        signer: Parties with legal standing in the Contract, including the
            principal parties, the grantor(s) and grantee(s), which are any person
            or organization bound by the contract, and any ancillary parties,
            which facilitate the execution of the contract such as a notary or
            witness.
        valuedItem: Contract Valued Item List.
        term: One or more Contract Provisions, which may be related and
            conveyed as a group, and may contain nested groups.
        bindingAttachment: Legally binding Contract: This is the signed and
            legally recognized representation of the Contract, which is considered
            the "source of truth" and which would be the basis for legal action
            related to enforcement of this Contract.
        bindingReference: Legally binding Contract: This is the signed and
            legally recognized representation of the Contract, which is considered
            the "source of truth" and which would be the basis for legal action
            related to enforcement of this Contract.
        friendly: The "patient friendly language" versionof the Contract in
            whole or in parts. "Patient friendly language" means the
            representation of the Contract and Contract Provisions in a manner
            that is readily accessible and understandable by a layperson in
            accordance with best practices for communication styles that ensure
            that those agreeing to or signing the Contract understand the roles,
            actions, obligations, responsibilities, and implication of the
            agreement.
        legal: List of Legal expressions or representations of this Contract.
        rule: List of Computable Policy Rule Language Representations of this
            Contract.
    """

    __name__ = 'Contract'

    def __init__(self, dict_values=None):
        self.resourceType = 'Contract'
        # type: str
        # possible values: Contract

        self.status = None
        # type: str

        self.issued = None
        # type: str

        self.applies = None
        # reference to Period

        self.subject = None
        # type: list
        # reference to Reference: identifier

        self.topic = None
        # type: list
        # reference to Reference: identifier

        self.authority = None
        # type: list
        # reference to Reference: identifier

        self.domain = None
        # type: list
        # reference to Reference: identifier

        self.type = None
        # reference to CodeableConcept

        self.subType = None
        # type: list
        # reference to CodeableConcept

        self.action = None
        # type: list
        # reference to CodeableConcept

        self.actionReason = None
        # type: list
        # reference to CodeableConcept

        self.decisionType = None
        # reference to CodeableConcept

        self.contentDerivative = None
        # reference to CodeableConcept

        self.securityLabel = None
        # type: list
        # reference to Coding

        self.agent = None
        # type: list
        # reference to Contract_Agent

        self.signer = None
        # type: list
        # reference to Contract_Signer

        self.valuedItem = None
        # type: list
        # reference to Contract_ValuedItem: identifier

        self.term = None
        # type: list
        # reference to Contract_Term: identifier

        self.bindingAttachment = None
        # reference to Attachment

        self.bindingReference = None
        # reference to Reference: identifier

        self.friendly = None
        # type: list
        # reference to Contract_Friendly

        self.legal = None
        # type: list
        # reference to Contract_Legal

        self.rule = None
        # type: list
        # reference to Contract_Rule

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Contract_Term',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'term'},

            {'parent_entity': 'Contract_Friendly',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'friendly'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'actionReason'},

            {'parent_entity': 'Contract_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'rule'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'decisionType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'action'},

            {'parent_entity': 'Contract_Agent',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'authority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'topic'},

            {'parent_entity': 'Contract_ValuedItem',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'valuedItem'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'contentDerivative'},

            {'parent_entity': 'Contract_Signer',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'signer'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'subject'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'bindingReference'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'applies'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'subType'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Contract_Legal',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'legal'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'domain'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'bindingAttachment'},
        ]


class Contract_Agent(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        actor: Who or what parties are assigned roles in this Contract.
        role: Role type of agent assigned roles in this Contract.
    """

    __name__ = 'Contract_Agent'

    def __init__(self, dict_values=None):
        self.actor = None
        # reference to Reference: identifier

        self.role = None
        # type: list
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

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
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        type: Role of this Contract signer, e.g. notary, grantee.
        party: Party which is a signator to this Contract.
        signature: Legally binding Contract DSIG signature contents in Base64.
    """

    __name__ = 'Contract_Signer'

    def __init__(self, dict_values=None):
        self.type = None
        # reference to Coding

        self.party = None
        # reference to Reference: identifier

        self.signature = None
        # type: list
        # reference to Signature

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Signer',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Signer',
             'child_variable': 'party'},

            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Signer',
             'child_variable': 'signature'},
        ]


class Contract_ValuedItem(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        entityCodeableConcept: Specific type of Contract Valued Item that may
            be priced.
        entityReference: Specific type of Contract Valued Item that may be
            priced.
        identifier: Identifies a Contract Valued Item instance.
        effectiveTime: Indicates the time during which this Contract
            ValuedItem information is effective.
        quantity: Specifies the units by which the Contract Valued Item is
            measured or counted, and quantifies the countable or measurable
            Contract Valued Item instances.
        unitPrice: A Contract Valued Item unit valuation measure.
        factor: A real number that represents a multiplier used in determining
            the overall value of the Contract Valued Item delivered. The concept
            of a Factor allows for a discount or surcharge multiplier to be
            applied to a monetary amount.
        points: An amount that expresses the weighting (based on difficulty,
            cost and/or resource intensiveness) associated with the Contract
            Valued Item delivered. The concept of Points allows for assignment of
            point values for a Contract Valued Item, such that a monetary amount
            can be assigned to each point.
        net: Expresses the product of the Contract Valued Item unitQuantity
            and the unitPriceAmt. For example, the formula: unit Quantity * unit
            Price (Cost per Point) * factor Number  * points = net Amount.
            Quantity, factor and points are assumed to be 1 if not supplied.
    """

    __name__ = 'Contract_ValuedItem'

    def __init__(self, dict_values=None):
        self.entityCodeableConcept = None
        # reference to CodeableConcept

        self.entityReference = None
        # reference to Reference: identifier

        self.effectiveTime = None
        # type: str

        self.quantity = None
        # reference to Quantity

        self.unitPrice = None
        # reference to Money

        self.factor = None
        # type: int

        self.points = None
        # type: int

        self.net = None
        # reference to Money

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'identifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'net'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'entityReference'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'entityCodeableConcept'},
        ]


class Contract_Term(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        identifier: Unique identifier for this particular Contract Provision.
        issued: When this Contract Provision was issued.
        applies: Relevant time or time-period when this Contract Provision is
            applicable.
        type: Type of Contract Provision such as specific requirements,
            purposes for actions, obligations, prohibitions, e.g. life time
            maximum benefit.
        subType: Subtype of this Contract Provision, e.g. life time maximum
            payment for a contract term for specific valued item, e.g. disability
            payment.
        topic: The matter of concern in the context of this provision of the
            agrement.
        action: Action stipulated by this Contract Provision.
        actionReason: Reason or purpose for the action stipulated by this
            Contract Provision.
        securityLabel: A set of security labels that define which terms are
            controlled by this condition.
        agent: An actor taking a role in an activity for which it can be
            assigned some degree of responsibility for the activity taking place.
        text: Human readable form of this Contract Provision.
        valuedItem: Contract Provision Valued Item List.
        group: Nested group of Contract Provisions.
    """

    __name__ = 'Contract_Term'

    def __init__(self, dict_values=None):
        self.issued = None
        # type: str

        self.applies = None
        # reference to Period

        self.type = None
        # reference to CodeableConcept

        self.subType = None
        # reference to CodeableConcept

        self.topic = None
        # type: list
        # reference to Reference: identifier

        self.action = None
        # type: list
        # reference to CodeableConcept

        self.actionReason = None
        # type: list
        # reference to CodeableConcept

        self.securityLabel = None
        # type: list
        # reference to Coding

        self.agent = None
        # type: list
        # reference to Contract_Agent1

        self.text = None
        # type: str

        self.valuedItem = None
        # type: list
        # reference to Contract_ValuedItem1: identifier

        self.group = None
        # type: list
        # reference to Contract_Term: identifier

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Contract_Agent1',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'agent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'actionReason'},

            {'parent_entity': 'Contract_Term',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'group'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'type'},

            {'parent_entity': 'Contract_ValuedItem1',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'valuedItem'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'applies'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'subType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'action'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'topic'},
        ]


class Contract_Agent1(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        actor: The agent assigned a role in this Contract Provision.
        role: Role played by the agent assigned this role in the execution of
            this Contract Provision.
    """

    __name__ = 'Contract_Agent1'

    def __init__(self, dict_values=None):
        self.actor = None
        # reference to Reference: identifier

        self.role = None
        # type: list
        # reference to CodeableConcept

        self.object_id = None
        # unique identifier for object class

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
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        entityCodeableConcept: Specific type of Contract Provision Valued Item
            that may be priced.
        entityReference: Specific type of Contract Provision Valued Item that
            may be priced.
        identifier: Identifies a Contract Provision Valued Item instance.
        effectiveTime: Indicates the time during which this Contract Term
            ValuedItem information is effective.
        quantity: Specifies the units by which the Contract Provision Valued
            Item is measured or counted, and quantifies the countable or
            measurable Contract Term Valued Item instances.
        unitPrice: A Contract Provision Valued Item unit valuation measure.
        factor: A real number that represents a multiplier used in determining
            the overall value of the Contract Provision Valued Item delivered. The
            concept of a Factor allows for a discount or surcharge multiplier to
            be applied to a monetary amount.
        points: An amount that expresses the weighting (based on difficulty,
            cost and/or resource intensiveness) associated with the Contract
            Provision Valued Item delivered. The concept of Points allows for
            assignment of point values for a Contract ProvisionValued Item, such
            that a monetary amount can be assigned to each point.
        net: Expresses the product of the Contract Provision Valued Item
            unitQuantity and the unitPriceAmt. For example, the formula: unit
            Quantity * unit Price (Cost per Point) * factor Number  * points = net
            Amount. Quantity, factor and points are assumed to be 1 if not
            supplied.
    """

    __name__ = 'Contract_ValuedItem1'

    def __init__(self, dict_values=None):
        self.entityCodeableConcept = None
        # reference to CodeableConcept

        self.entityReference = None
        # reference to Reference: identifier

        self.effectiveTime = None
        # type: str

        self.quantity = None
        # reference to Quantity

        self.unitPrice = None
        # reference to Money

        self.factor = None
        # type: int

        self.points = None
        # type: int

        self.net = None
        # reference to Money

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'quantity'},

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

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'entityReference'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'unitPrice'},
        ]


class Contract_Friendly(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        contentAttachment: Human readable rendering of this Contract in a
            format and representation intended to enhance comprehension and ensure
            understandability.
        contentReference: Human readable rendering of this Contract in a
            format and representation intended to enhance comprehension and ensure
            understandability.
    """

    __name__ = 'Contract_Friendly'

    def __init__(self, dict_values=None):
        self.contentAttachment = None
        # reference to Attachment

        self.contentReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        contentAttachment: Contract legal text in human renderable form.
        contentReference: Contract legal text in human renderable form.
    """

    __name__ = 'Contract_Legal'

    def __init__(self, dict_values=None):
        self.contentAttachment = None
        # reference to Attachment

        self.contentReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.

    Args:
        contentAttachment: Computable Contract conveyed using a policy rule
            language (e.g. XACML, DKAL, SecPal).
        contentReference: Computable Contract conveyed using a policy rule
            language (e.g. XACML, DKAL, SecPal).
    """

    __name__ = 'Contract_Rule'

    def __init__(self, dict_values=None):
        self.contentAttachment = None
        # reference to Attachment

        self.contentReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

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
