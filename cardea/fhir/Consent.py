from .fhirbase import fhirbase


class Consent(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.

    Args:
        resourceType: This is a Consent resource
        identifier: Unique identifier for this copy of the Consent Statement.
        status: Indicates the current state of this consent.
        category: A classification of the type of consents found in the
            statement. This element supports indexing and retrieval of consent
            statements.
        patient: The patient/healthcare consumer to whom this consent applies.
        period: Relevant time or time-period when this Consent is applicable.
        dateTime: When this  Consent was issued / created / indexed.
        consentingParty: Either the Grantor, which is the entity responsible
            for granting the rights listed in a Consent Directive or the Grantee,
            which is the entity responsible for complying with the Consent
            Directive, including any obligations or limitations on authorizations
            and enforcement of prohibitions.
        actor: Who or what is controlled by this consent. Use group to
            identify a set of actors by some property they share (e.g. 'admitting
            officers').
        action: Actions controlled by this consent.
        organization: The organization that manages the consent, and the
            framework within which it is executed.
        sourceAttachment: The source on which this consent statement is based.
            The source might be a scanned original paper form, or a reference to a
            consent that links back to such a source, a reference to a document
            repository (e.g. XDS) that stores the original consent document.
        sourceIdentifier: The source on which this consent statement is based.
            The source might be a scanned original paper form, or a reference to a
            consent that links back to such a source, a reference to a document
            repository (e.g. XDS) that stores the original consent document.
        sourceReference: The source on which this consent statement is based.
            The source might be a scanned original paper form, or a reference to a
            consent that links back to such a source, a reference to a document
            repository (e.g. XDS) that stores the original consent document.
        policy: The references to the policies that are included in this
            consent scope. Policies may be organizational, but are often defined
            jurisdictionally, or in law.
        policyRule: A referece to the specific computable policy.
        securityLabel: A set of security labels that define which resources
            are controlled by this consent. If more than one label is specified,
            all resources must have all the specified labels.
        purpose: The context of the activities a user is taking - why the user
            is accessing the data - that are controlled by this consent.
        dataPeriod: Clinical or Operational Relevant period of time that
            bounds the data controlled by this consent.
        data: The resources controlled by this consent, if specific resources
            are referenced.
        except: An exception to the base policy of this consent. An exception
            can be an addition or removal of access permissions.
    """

    __name__ = 'Consent'

    def __init__(self, dict_values=None):
        self.resourceType = 'Consent'
        # type: str
        # possible values: Consent

        self.status = None
        # type: str
        # possible values: draft, proposed, active, rejected,
        # inactive, entered-in-error

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.patient = None
        # reference to Reference: identifier

        self.period = None
        # reference to Period

        self.dateTime = None
        # type: str

        self.consentingParty = None
        # type: list
        # reference to Reference: identifier

        self.actor = None
        # type: list
        # reference to Consent_Actor

        self.action = None
        # type: list
        # reference to CodeableConcept

        self.organization = None
        # type: list
        # reference to Reference: identifier

        self.sourceAttachment = None
        # reference to Attachment

        self.sourceIdentifier = None
        # reference to Identifier

        self.sourceReference = None
        # reference to Reference: identifier

        self.policy = None
        # type: list
        # reference to Consent_Policy

        self.policyRule = None
        # type: str

        self.securityLabel = None
        # type: list
        # reference to Coding

        self.purpose = None
        # type: list
        # reference to Coding

        self.dataPeriod = None
        # reference to Period

        self.data = None
        # type: list
        # reference to Consent_Data

        self._except = None
        # type: list
        # reference to Consent_Except

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'draft', 'proposed', 'active', 'rejected', 'inactive',
                        'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, proposed, active, rejected, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'category'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'sourceAttachment'},

            {'parent_entity': 'Consent_Policy',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'policy'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'sourceReference'},

            {'parent_entity': 'Consent_Data',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'data'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'period'},

            {'parent_entity': 'Consent_Actor',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'actor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'organization'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'consentingParty'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'dataPeriod'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'sourceIdentifier'},

            {'parent_entity': 'Consent_Except',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': '_except'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'action'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'purpose'},
        ]


class Consent_Actor(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.

    Args:
        role: How the individual is involved in the resources content that is
            described in the consent.
        reference: The resource that identifies the actor. To identify a
            actors by type, use group to identify a set of actors by some property
            they share (e.g. 'admitting officers').
    """

    __name__ = 'Consent_Actor'

    def __init__(self, dict_values=None):
        self.role = None
        # reference to CodeableConcept

        self.reference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Actor',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent_Actor',
             'child_variable': 'reference'},
        ]


class Consent_Policy(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.

    Args:
        authority: Entity or Organization having regulatory jurisdiction or
            accountability for  enforcing policies pertaining to Consent
            Directives.
        uri: The references to the policies that are included in this consent
            scope. Policies may be organizational, but are often defined
            jurisdictionally, or in law.
    """

    __name__ = 'Consent_Policy'

    def __init__(self, dict_values=None):
        self.authority = None
        # type: str

        self.uri = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class Consent_Data(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.

    Args:
        meaning: How the resource reference is interpreted when testing
            consent restrictions.
        reference: A reference to a specific resource that defines which
            resources are covered by this consent.
    """

    __name__ = 'Consent_Data'

    def __init__(self, dict_values=None):
        self.meaning = None
        # type: str
        # possible values: instance, related, dependents, authoredby

        self.reference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.meaning is not None:
            for value in self.meaning:
                if value is not None and value.lower() not in [
                        'instance', 'related', 'dependents', 'authoredby']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'instance, related, dependents, authoredby'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent_Data',
             'child_variable': 'reference'},
        ]


class Consent_Except(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.

    Args:
        type: Action  to take - permit or deny - when the exception conditions
            are met.
        period: The timeframe in this exception is valid.
        actor: Who or what is controlled by this Exception. Use group to
            identify a set of actors by some property they share (e.g. 'admitting
            officers').
        action: Actions controlled by this Exception.
        securityLabel: A set of security labels that define which resources
            are controlled by this exception. If more than one label is specified,
            all resources must have all the specified labels.
        purpose: The context of the activities a user is taking - why the user
            is accessing the data - that are controlled by this exception.
        class: The class of information covered by this exception. The type
            can be a FHIR resource type, a profile on a type, or a CDA document,
            or some other type that indicates what sort of information the consent
            relates to.
        code: If this code is found in an instance, then the exception
            applies.
        dataPeriod: Clinical or Operational Relevant period of time that
            bounds the data controlled by this exception.
        data: The resources controlled by this exception, if specific
            resources are referenced.
    """

    __name__ = 'Consent_Except'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: deny, permit

        self.period = None
        # reference to Period

        self.actor = None
        # type: list
        # reference to Consent_Actor1

        self.action = None
        # type: list
        # reference to CodeableConcept

        self.securityLabel = None
        # type: list
        # reference to Coding

        self.purpose = None
        # type: list
        # reference to Coding

        self._class = None
        # type: list
        # reference to Coding

        self.code = None
        # type: list
        # reference to Coding

        self.dataPeriod = None
        # reference to Period

        self.data = None
        # type: list
        # reference to Consent_Data1

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'deny', 'permit']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'deny, permit'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'purpose'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'dataPeriod'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'period'},

            {'parent_entity': 'Consent_Data1',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'data'},

            {'parent_entity': 'Consent_Actor1',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'action'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'code'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': '_class'},
        ]


class Consent_Actor1(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.

    Args:
        role: How the individual is involved in the resources content that is
            described in the exception.
        reference: The resource that identifies the actor. To identify a
            actors by type, use group to identify a set of actors by some property
            they share (e.g. 'admitting officers').
    """

    __name__ = 'Consent_Actor1'

    def __init__(self, dict_values=None):
        self.role = None
        # reference to CodeableConcept

        self.reference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent_Actor1',
             'child_variable': 'reference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Actor1',
             'child_variable': 'role'},
        ]


class Consent_Data1(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.

    Args:
        meaning: How the resource reference is interpreted when testing
            consent restrictions.
        reference: A reference to a specific resource that defines which
            resources are covered by this consent.
    """

    __name__ = 'Consent_Data1'

    def __init__(self, dict_values=None):
        self.meaning = None
        # type: str
        # possible values: instance, related, dependents, authoredby

        self.reference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.meaning is not None:
            for value in self.meaning:
                if value is not None and value.lower() not in [
                        'instance', 'related', 'dependents', 'authoredby']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'instance, related, dependents, authoredby'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent_Data1',
             'child_variable': 'reference'},
        ]
