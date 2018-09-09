from .fhirbase import fhirbase


class Contract(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __name__ = 'Contract'

    def __init__(self, dict_values=None):
        self.resourceType = 'Contract'
        """
        This is a Contract resource

        type: string
        possible values: Contract
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.issued = None
        """
        When this  Contract was issued.

        type: string
        """

        self.applies = None
        """
        Relevant time or time-period when this Contract is applicable.

        reference to Period
        """

        self.subject = None
        """
        The target entity impacted by or of interest to parties to the
        agreement.

        type: array
        reference to Reference: identifier
        """

        self.topic = None
        """
        The matter of concern in the context of this agreement.

        type: array
        reference to Reference: identifier
        """

        self.authority = None
        """
        A formally or informally recognized grouping of people, principals,
        organizations, or jurisdictions formed for the purpose of achieving
        some form of collective action such as the promulgation,
        administration and enforcement of contracts and policies.

        type: array
        reference to Reference: identifier
        """

        self.domain = None
        """
        Recognized governance framework or system operating with a
        circumscribed scope in accordance with specified principles, policies,
        processes or procedures for managing rights, actions, or behaviors of
        parties or principals relative to resources.

        type: array
        reference to Reference: identifier
        """

        self.type = None
        """
        Type of Contract such as an insurance policy, real estate contract, a
        will, power of attorny, Privacy or Security policy , trust framework
        agreement, etc.

        reference to CodeableConcept
        """

        self.subType = None
        """
        More specific type or specialization of an overarching or more general
        contract such as auto insurance, home owner  insurance, prenupial
        agreement, Advanced-Directive, or privacy consent.

        type: array
        reference to CodeableConcept
        """

        self.action = None
        """
        Action stipulated by this Contract.

        type: array
        reference to CodeableConcept
        """

        self.actionReason = None
        """
        Reason for action stipulated by this Contract.

        type: array
        reference to CodeableConcept
        """

        self.decisionType = None
        """
        The type of decision made by a grantor with respect to an offer made
        by a grantee.

        reference to CodeableConcept
        """

        self.contentDerivative = None
        """
        The minimal content derived from the basal information source at a
        specific stage in its lifecycle.

        reference to CodeableConcept
        """

        self.securityLabel = None
        """
        A set of security labels that define which resources are controlled by
        this consent. If more than one label is specified, all resources must
        have all the specified labels.

        type: array
        reference to Coding
        """

        self.agent = None
        """
        An actor taking a role in an activity for which it can be assigned
        some degree of responsibility for the activity taking place.

        type: array
        reference to Contract_Agent
        """

        self.signer = None
        """
        Parties with legal standing in the Contract, including the principal
        parties, the grantor(s) and grantee(s), which are any person or
        organization bound by the contract, and any ancillary parties, which
        facilitate the execution of the contract such as a notary or witness.

        type: array
        reference to Contract_Signer
        """

        self.valuedItem = None
        """
        Contract Valued Item List.

        type: array
        reference to Contract_ValuedItem: identifier
        """

        self.term = None
        """
        One or more Contract Provisions, which may be related and conveyed as
        a group, and may contain nested groups.

        type: array
        reference to Contract_Term: identifier
        """

        self.bindingAttachment = None
        """
        Legally binding Contract: This is the signed and legally recognized
        representation of the Contract, which is considered the "source of
        truth" and which would be the basis for legal action related to
        enforcement of this Contract.

        reference to Attachment
        """

        self.bindingReference = None
        """
        Legally binding Contract: This is the signed and legally recognized
        representation of the Contract, which is considered the "source of
        truth" and which would be the basis for legal action related to
        enforcement of this Contract.

        reference to Reference: identifier
        """

        self.friendly = None
        """
        The "patient friendly language" versionof the Contract in whole or in
        parts. "Patient friendly language" means the representation of the
        Contract and Contract Provisions in a manner that is readily
        accessible and understandable by a layperson in accordance with best
        practices for communication styles that ensure that those agreeing to
        or signing the Contract understand the roles, actions, obligations,
        responsibilities, and implication of the agreement.

        type: array
        reference to Contract_Friendly
        """

        self.legal = None
        """
        List of Legal expressions or representations of this Contract.

        type: array
        reference to Contract_Legal
        """

        self.rule = None
        """
        List of Computable Policy Rule Language Representations of this
        Contract.

        type: array
        reference to Contract_Rule
        """

        self.identifier = None
        """
        Unique identifier for this Contract.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'action'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'topic'},

            {'parent_entity': 'Contract_Term',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'term'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'subject'},

            {'parent_entity': 'Contract_ValuedItem',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'valuedItem'},

            {'parent_entity': 'Contract_Legal',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'legal'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'subType'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'type'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'bindingAttachment'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'bindingReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'decisionType'},

            {'parent_entity': 'Contract_Friendly',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'friendly'},

            {'parent_entity': 'Contract_Agent',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'agent'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'contentDerivative'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'actionReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'authority'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract',
             'child_variable': 'domain'},

            {'parent_entity': 'Contract_Signer',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'signer'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'applies'},

            {'parent_entity': 'Contract_Rule',
             'parent_variable': 'object_id',
             'child_entity': 'Contract',
             'child_variable': 'rule'},
        ]


class Contract_Agent(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __name__ = 'Contract_Agent'

    def __init__(self, dict_values=None):
        self.actor = None
        """
        Who or what parties are assigned roles in this Contract.

        reference to Reference: identifier
        """

        self.role = None
        """
        Role type of agent assigned roles in this Contract.

        type: array
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
    """

    __name__ = 'Contract_Signer'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Role of this Contract signer, e.g. notary, grantee.

        reference to Coding
        """

        self.party = None
        """
        Party which is a signator to this Contract.

        reference to Reference: identifier
        """

        self.signature = None
        """
        Legally binding Contract DSIG signature contents in Base64.

        type: array
        reference to Signature
        """

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
    """

    __name__ = 'Contract_ValuedItem'

    def __init__(self, dict_values=None):
        self.entityCodeableConcept = None
        """
        Specific type of Contract Valued Item that may be priced.

        reference to CodeableConcept
        """

        self.entityReference = None
        """
        Specific type of Contract Valued Item that may be priced.

        reference to Reference: identifier
        """

        self.effectiveTime = None
        """
        Indicates the time during which this Contract ValuedItem information
        is effective.

        type: string
        """

        self.quantity = None
        """
        Specifies the units by which the Contract Valued Item is measured or
        counted, and quantifies the countable or measurable Contract Valued
        Item instances.

        reference to Quantity
        """

        self.unitPrice = None
        """
        A Contract Valued Item unit valuation measure.

        reference to Money
        """

        self.factor = None
        """
        A real number that represents a multiplier used in determining the
        overall value of the Contract Valued Item delivered. The concept of a
        Factor allows for a discount or surcharge multiplier to be applied to
        a monetary amount.

        type: int
        """

        self.points = None
        """
        An amount that expresses the weighting (based on difficulty, cost
        and/or resource intensiveness) associated with the Contract Valued
        Item delivered. The concept of Points allows for assignment of point
        values for a Contract Valued Item, such that a monetary amount can be
        assigned to each point.

        type: int
        """

        self.net = None
        """
        Expresses the product of the Contract Valued Item unitQuantity and the
        unitPriceAmt. For example, the formula: unit Quantity * unit Price
        (Cost per Point) * factor Number  * points = net Amount. Quantity,
        factor and points are assumed to be 1 if not supplied.

        reference to Money
        """

        self.identifier = None
        """
        Identifies a Contract Valued Item instance.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'entityCodeableConcept'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'net'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'entityReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem',
             'child_variable': 'quantity'},
        ]


class Contract_Term(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __name__ = 'Contract_Term'

    def __init__(self, dict_values=None):
        self.issued = None
        """
        When this Contract Provision was issued.

        type: string
        """

        self.applies = None
        """
        Relevant time or time-period when this Contract Provision is
        applicable.

        reference to Period
        """

        self.type = None
        """
        Type of Contract Provision such as specific requirements, purposes for
        actions, obligations, prohibitions, e.g. life time maximum benefit.

        reference to CodeableConcept
        """

        self.subType = None
        """
        Subtype of this Contract Provision, e.g. life time maximum payment for
        a contract term for specific valued item, e.g. disability payment.

        reference to CodeableConcept
        """

        self.topic = None
        """
        The matter of concern in the context of this provision of the
        agrement.

        type: array
        reference to Reference: identifier
        """

        self.action = None
        """
        Action stipulated by this Contract Provision.

        type: array
        reference to CodeableConcept
        """

        self.actionReason = None
        """
        Reason or purpose for the action stipulated by this Contract
        Provision.

        type: array
        reference to CodeableConcept
        """

        self.securityLabel = None
        """
        A set of security labels that define which terms are controlled by
        this condition.

        type: array
        reference to Coding
        """

        self.agent = None
        """
        An actor taking a role in an activity for which it can be assigned
        some degree of responsibility for the activity taking place.

        type: array
        reference to Contract_Agent1
        """

        self.text = None
        """
        Human readable form of this Contract Provision.

        type: string
        """

        self.valuedItem = None
        """
        Contract Provision Valued Item List.

        type: array
        reference to Contract_ValuedItem1: identifier
        """

        self.group = None
        """
        Nested group of Contract Provisions.

        type: array
        reference to Contract_Term: identifier
        """

        self.identifier = None
        """
        Unique identifier for this particular Contract Provision.

        reference to Identifier
        """

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
             'child_variable': 'subType'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'applies'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'action'},

            {'parent_entity': 'Contract_Term',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'group'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'actionReason'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'type'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Contract_ValuedItem1',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Term',
             'child_variable': 'valuedItem'},

            {'parent_entity': 'Contract_Agent1',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Term',
             'child_variable': 'agent'},
        ]


class Contract_Agent1(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __name__ = 'Contract_Agent1'

    def __init__(self, dict_values=None):
        self.actor = None
        """
        The agent assigned a role in this Contract Provision.

        reference to Reference: identifier
        """

        self.role = None
        """
        Role played by the agent assigned this role in the execution of this
        Contract Provision.

        type: array
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
             'child_entity': 'Contract_Agent1',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_Agent1',
             'child_variable': 'actor'},
        ]


class Contract_ValuedItem1(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __name__ = 'Contract_ValuedItem1'

    def __init__(self, dict_values=None):
        self.entityCodeableConcept = None
        """
        Specific type of Contract Provision Valued Item that may be priced.

        reference to CodeableConcept
        """

        self.entityReference = None
        """
        Specific type of Contract Provision Valued Item that may be priced.

        reference to Reference: identifier
        """

        self.effectiveTime = None
        """
        Indicates the time during which this Contract Term ValuedItem
        information is effective.

        type: string
        """

        self.quantity = None
        """
        Specifies the units by which the Contract Provision Valued Item is
        measured or counted, and quantifies the countable or measurable
        Contract Term Valued Item instances.

        reference to Quantity
        """

        self.unitPrice = None
        """
        A Contract Provision Valued Item unit valuation measure.

        reference to Money
        """

        self.factor = None
        """
        A real number that represents a multiplier used in determining the
        overall value of the Contract Provision Valued Item delivered. The
        concept of a Factor allows for a discount or surcharge multiplier to
        be applied to a monetary amount.

        type: int
        """

        self.points = None
        """
        An amount that expresses the weighting (based on difficulty, cost
        and/or resource intensiveness) associated with the Contract Provision
        Valued Item delivered. The concept of Points allows for assignment of
        point values for a Contract ProvisionValued Item, such that a monetary
        amount can be assigned to each point.

        type: int
        """

        self.net = None
        """
        Expresses the product of the Contract Provision Valued Item
        unitQuantity and the unitPriceAmt. For example, the formula: unit
        Quantity * unit Price (Cost per Point) * factor Number  * points = net
        Amount. Quantity, factor and points are assumed to be 1 if not
        supplied.

        reference to Money
        """

        self.identifier = None
        """
        Identifies a Contract Provision Valued Item instance.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'entityReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'quantity'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'identifier'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'unitPrice'},

            {'parent_entity': 'Money',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'net'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_ValuedItem1',
             'child_variable': 'entityCodeableConcept'},
        ]


class Contract_Friendly(fhirbase):
    """
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """

    __name__ = 'Contract_Friendly'

    def __init__(self, dict_values=None):
        self.contentAttachment = None
        """
        Human readable rendering of this Contract in a format and
        representation intended to enhance comprehension and ensure
        understandability.

        reference to Attachment
        """

        self.contentReference = None
        """
        Human readable rendering of this Contract in a format and
        representation intended to enhance comprehension and ensure
        understandability.

        reference to Reference: identifier
        """

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
    """

    __name__ = 'Contract_Legal'

    def __init__(self, dict_values=None):
        self.contentAttachment = None
        """
        Contract legal text in human renderable form.

        reference to Attachment
        """

        self.contentReference = None
        """
        Contract legal text in human renderable form.

        reference to Reference: identifier
        """

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
    """

    __name__ = 'Contract_Rule'

    def __init__(self, dict_values=None):
        self.contentAttachment = None
        """
        Computable Contract conveyed using a policy rule language (e.g. XACML,
        DKAL, SecPal).

        reference to Attachment
        """

        self.contentReference = None
        """
        Computable Contract conveyed using a policy rule language (e.g. XACML,
        DKAL, SecPal).

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
             'child_entity': 'Contract_Rule',
             'child_variable': 'contentReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Contract_Rule',
             'child_variable': 'contentAttachment'},
        ]
