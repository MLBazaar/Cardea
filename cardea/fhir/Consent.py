from .fhirbase import fhirbase


class Consent(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    __name__ = 'Consent'

    def __init__(self, dict_values=None):
        self.resourceType = 'Consent'
        """
        This is a Consent resource

        type: string
        possible values: Consent
        """

        self.status = None
        """
        Indicates the current state of this consent.

        type: string
        possible values: draft, proposed, active, rejected, inactive,
        entered-in-error
        """

        self.category = None
        """
        A classification of the type of consents found in the statement. This
        element supports indexing and retrieval of consent statements.

        type: array
        reference to CodeableConcept
        """

        self.patient = None
        """
        The patient/healthcare consumer to whom this consent applies.

        reference to Reference: identifier
        """

        self.period = None
        """
        Relevant time or time-period when this Consent is applicable.

        reference to Period
        """

        self.dateTime = None
        """
        When this  Consent was issued / created / indexed.

        type: string
        """

        self.consentingParty = None
        """
        Either the Grantor, which is the entity responsible for granting the
        rights listed in a Consent Directive or the Grantee, which is the
        entity responsible for complying with the Consent Directive, including
        any obligations or limitations on authorizations and enforcement of
        prohibitions.

        type: array
        reference to Reference: identifier
        """

        self.actor = None
        """
        Who or what is controlled by this consent. Use group to identify a set
        of actors by some property they share (e.g. 'admitting officers').

        type: array
        reference to Consent_Actor
        """

        self.action = None
        """
        Actions controlled by this consent.

        type: array
        reference to CodeableConcept
        """

        self.organization = None
        """
        The organization that manages the consent, and the framework within
        which it is executed.

        type: array
        reference to Reference: identifier
        """

        self.sourceAttachment = None
        """
        The source on which this consent statement is based. The source might
        be a scanned original paper form, or a reference to a consent that
        links back to such a source, a reference to a document repository
        (e.g. XDS) that stores the original consent document.

        reference to Attachment
        """

        self.sourceIdentifier = None
        """
        The source on which this consent statement is based. The source might
        be a scanned original paper form, or a reference to a consent that
        links back to such a source, a reference to a document repository
        (e.g. XDS) that stores the original consent document.

        reference to Identifier
        """

        self.sourceReference = None
        """
        The source on which this consent statement is based. The source might
        be a scanned original paper form, or a reference to a consent that
        links back to such a source, a reference to a document repository
        (e.g. XDS) that stores the original consent document.

        reference to Reference: identifier
        """

        self.policy = None
        """
        The references to the policies that are included in this consent
        scope. Policies may be organizational, but are often defined
        jurisdictionally, or in law.

        type: array
        reference to Consent_Policy
        """

        self.policyRule = None
        """
        A referece to the specific computable policy.

        type: string
        """

        self.securityLabel = None
        """
        A set of security labels that define which resources are controlled by
        this consent. If more than one label is specified, all resources must
        have all the specified labels.

        type: array
        reference to Coding
        """

        self.purpose = None
        """
        The context of the activities a user is taking - why the user is
        accessing the data - that are controlled by this consent.

        type: array
        reference to Coding
        """

        self.dataPeriod = None
        """
        Clinical or Operational Relevant period of time that bounds the data
        controlled by this consent.

        reference to Period
        """

        self.data = None
        """
        The resources controlled by this consent, if specific resources are
        referenced.

        type: array
        reference to Consent_Data
        """

        self._except = None
        """
        An exception to the base policy of this consent. An exception can be
        an addition or removal of access permissions.

        type: array
        reference to Consent_Except
        """

        self.identifier = None
        """
        Unique identifier for this copy of the Consent Statement.

        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'dataPeriod'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'sourceIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'consentingParty'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'sourceReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'action'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'patient'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'sourceAttachment'},

            {'parent_entity': 'Consent_Policy',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'policy'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Consent',
             'child_variable': 'organization'},

            {'parent_entity': 'Consent_Except',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': '_except'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'purpose'},

            {'parent_entity': 'Consent_Data',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'data'},

            {'parent_entity': 'Consent_Actor',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'actor'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent',
             'child_variable': 'period'},
        ]


class Consent_Actor(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    __name__ = 'Consent_Actor'

    def __init__(self, dict_values=None):
        self.role = None
        """
        How the individual is involved in the resources content that is
        described in the consent.

        reference to CodeableConcept
        """

        self.reference = None
        """
        The resource that identifies the actor. To identify a actors by type,
        use group to identify a set of actors by some property they share
        (e.g. 'admitting officers').

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
             'child_entity': 'Consent_Actor',
             'child_variable': 'reference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Actor',
             'child_variable': 'role'},
        ]


class Consent_Policy(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    __name__ = 'Consent_Policy'

    def __init__(self, dict_values=None):
        self.authority = None
        """
        Entity or Organization having regulatory jurisdiction or
        accountability for  enforcing policies pertaining to Consent
        Directives.

        type: string
        """

        self.uri = None
        """
        The references to the policies that are included in this consent
        scope. Policies may be organizational, but are often defined
        jurisdictionally, or in law.

        type: string
        """

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
    """

    __name__ = 'Consent_Data'

    def __init__(self, dict_values=None):
        self.meaning = None
        """
        How the resource reference is interpreted when testing consent
        restrictions.

        type: string
        possible values: instance, related, dependents, authoredby
        """

        self.reference = None
        """
        A reference to a specific resource that defines which resources are
        covered by this consent.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
    """

    __name__ = 'Consent_Except'

    def __init__(self, dict_values=None):
        self.type = None
        """
        Action  to take - permit or deny - when the exception conditions are
        met.

        type: string
        possible values: deny, permit
        """

        self.period = None
        """
        The timeframe in this exception is valid.

        reference to Period
        """

        self.actor = None
        """
        Who or what is controlled by this Exception. Use group to identify a
        set of actors by some property they share (e.g. 'admitting officers').

        type: array
        reference to Consent_Actor1
        """

        self.action = None
        """
        Actions controlled by this Exception.

        type: array
        reference to CodeableConcept
        """

        self.securityLabel = None
        """
        A set of security labels that define which resources are controlled by
        this exception. If more than one label is specified, all resources
        must have all the specified labels.

        type: array
        reference to Coding
        """

        self.purpose = None
        """
        The context of the activities a user is taking - why the user is
        accessing the data - that are controlled by this exception.

        type: array
        reference to Coding
        """

        self._class = None
        """
        The class of information covered by this exception. The type can be a
        FHIR resource type, a profile on a type, or a CDA document, or some
        other type that indicates what sort of information the consent relates
        to.

        type: array
        reference to Coding
        """

        self.code = None
        """
        If this code is found in an instance, then the exception applies.

        type: array
        reference to Coding
        """

        self.dataPeriod = None
        """
        Clinical or Operational Relevant period of time that bounds the data
        controlled by this exception.

        reference to Period
        """

        self.data = None
        """
        The resources controlled by this exception, if specific resources are
        referenced.

        type: array
        reference to Consent_Data1
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'deny', 'permit']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'deny, permit'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Consent_Actor1',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'actor'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'code'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'period'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': '_class'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'securityLabel'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'dataPeriod'},

            {'parent_entity': 'Coding',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'purpose'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'action'},

            {'parent_entity': 'Consent_Data1',
             'parent_variable': 'object_id',
             'child_entity': 'Consent_Except',
             'child_variable': 'data'},
        ]


class Consent_Actor1(fhirbase):
    """
    A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    __name__ = 'Consent_Actor1'

    def __init__(self, dict_values=None):
        self.role = None
        """
        How the individual is involved in the resources content that is
        described in the exception.

        reference to CodeableConcept
        """

        self.reference = None
        """
        The resource that identifies the actor. To identify a actors by type,
        use group to identify a set of actors by some property they share
        (e.g. 'admitting officers').

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
    """

    __name__ = 'Consent_Data1'

    def __init__(self, dict_values=None):
        self.meaning = None
        """
        How the resource reference is interpreted when testing consent
        restrictions.

        type: string
        possible values: instance, related, dependents, authoredby
        """

        self.reference = None
        """
        A reference to a specific resource that defines which resources are
        covered by this consent.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
