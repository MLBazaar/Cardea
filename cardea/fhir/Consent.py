from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Reference import Reference
from .Period import Period
from .Attachment import Attachment
from .Coding import Coding

class Consent(fhirbase):
    """A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    def __init__(self, dict_values=None):
        # this is a consent resource
        self.resourceType = 'Consent'
        # type = string
        # possible values = Consent

        # indicates the current state of this consent.
        self.status = None
        # type = string
        # possible values = draft, proposed, active, rejected, inactive, entered-in-error

        # a classification of the type of consents found in the statement. this
        # element supports indexing and retrieval of consent statements.
        self.category = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the patient/healthcare consumer to whom this consent applies.
        self.patient = None
        # reference to Reference: identifier

        # relevant time or time-period when this consent is applicable.
        self.period = None
        # reference to Period: Period

        # when this  consent was issued / created / indexed.
        self.dateTime = None
        # type = string

        # either the grantor, which is the entity responsible for granting the
        # rights listed in a consent directive or the grantee, which is the entity
        # responsible for complying with the consent directive, including any
        # obligations or limitations on authorizations and enforcement of
        # prohibitions.
        self.consentingParty = None
        # type = array
        # reference to Reference: identifier

        # who or what is controlled by this consent. use group to identify a set
        # of actors by some property they share (e.g. 'admitting officers').
        self.actor = None
        # type = array
        # reference to Consent_Actor: Consent_Actor

        # actions controlled by this consent.
        self.action = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the organization that manages the consent, and the framework within
        # which it is executed.
        self.organization = None
        # type = array
        # reference to Reference: identifier

        # the source on which this consent statement is based. the source might be
        # a scanned original paper form, or a reference to a consent that links
        # back to such a source, a reference to a document repository (e.g. xds)
        # that stores the original consent document.
        self.sourceAttachment = None
        # reference to Attachment: Attachment

        # the source on which this consent statement is based. the source might be
        # a scanned original paper form, or a reference to a consent that links
        # back to such a source, a reference to a document repository (e.g. xds)
        # that stores the original consent document.
        self.sourceIdentifier = None
        # reference to Identifier: Identifier

        # the source on which this consent statement is based. the source might be
        # a scanned original paper form, or a reference to a consent that links
        # back to such a source, a reference to a document repository (e.g. xds)
        # that stores the original consent document.
        self.sourceReference = None
        # reference to Reference: identifier

        # the references to the policies that are included in this consent scope.
        # policies may be organizational, but are often defined jurisdictionally,
        # or in law.
        self.policy = None
        # type = array
        # reference to Consent_Policy: Consent_Policy

        # a referece to the specific computable policy.
        self.policyRule = None
        # type = string

        # a set of security labels that define which resources are controlled by
        # this consent. if more than one label is specified, all resources must
        # have all the specified labels.
        self.securityLabel = None
        # type = array
        # reference to Coding: Coding

        # the context of the activities a user is taking - why the user is
        # accessing the data - that are controlled by this consent.
        self.purpose = None
        # type = array
        # reference to Coding: Coding

        # clinical or operational relevant period of time that bounds the data
        # controlled by this consent.
        self.dataPeriod = None
        # reference to Period: Period

        # the resources controlled by this consent, if specific resources are
        # referenced.
        self.data = None
        # type = array
        # reference to Consent_Data: Consent_Data

        # an exception to the base policy of this consent. an exception can be an
        # addition or removal of access permissions.
        self._except = None
        # type = array
        # reference to Consent_Except: Consent_Except

        # unique identifier for this copy of the consent statement.
        self.identifier = None
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'proposed', 'active', 'rejected', 'inactive', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, proposed, active, rejected, inactive, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Consent',
            'child_variable': 'consentingParty'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'securityLabel'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'action'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Consent',
            'child_variable': 'organization'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Consent',
            'child_variable': 'sourceReference'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'period'},

            {'parent_entity': 'Consent_Except',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'except'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'sourceIdentifier'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'dataPeriod'},

            {'parent_entity': 'Consent_Actor',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'actor'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'category'},

            {'parent_entity': 'Consent_Data',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'data'},

            {'parent_entity': 'Consent_Policy',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'policy'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Consent',
            'child_variable': 'patient'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'purpose'},

            {'parent_entity': 'Attachment',
            'parent_variable': 'object_id',
            'child_entity': 'Consent',
            'child_variable': 'sourceAttachment'},
        ]

class Consent_Actor(fhirbase):
    """A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    def __init__(self, dict_values=None):
        # how the individual is involved in the resources content that is
        # described in the consent.
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the resource that identifies the actor. to identify a actors by type,
        # use group to identify a set of actors by some property they share (e.g.
        # 'admitting officers').
        self.reference = None
        # reference to Reference: identifier


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
    """A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    def __init__(self, dict_values=None):
        # entity or organization having regulatory jurisdiction or accountability
        # for  enforcing policies pertaining to consent directives.
        self.authority = None
        # type = string

        # the references to the policies that are included in this consent scope.
        # policies may be organizational, but are often defined jurisdictionally,
        # or in law.
        self.uri = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


class Consent_Data(fhirbase):
    """A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    def __init__(self, dict_values=None):
        # how the resource reference is interpreted when testing consent
        # restrictions.
        self.meaning = None
        # type = string
        # possible values = instance, related, dependents, authoredby

        # a reference to a specific resource that defines which resources are
        # covered by this consent.
        self.reference = None
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.meaning is not None:
            for value in self.meaning:
                if value != None and value.lower() not in ['instance', 'related', 'dependents', 'authoredby']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'instance, related, dependents, authoredby'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Consent_Data',
            'child_variable': 'reference'},
        ]

class Consent_Except(fhirbase):
    """A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    def __init__(self, dict_values=None):
        # action  to take - permit or deny - when the exception conditions are
        # met.
        self.type = None
        # type = string
        # possible values = deny, permit

        # the timeframe in this exception is valid.
        self.period = None
        # reference to Period: Period

        # who or what is controlled by this exception. use group to identify a set
        # of actors by some property they share (e.g. 'admitting officers').
        self.actor = None
        # type = array
        # reference to Consent_Actor1: Consent_Actor1

        # actions controlled by this exception.
        self.action = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a set of security labels that define which resources are controlled by
        # this exception. if more than one label is specified, all resources must
        # have all the specified labels.
        self.securityLabel = None
        # type = array
        # reference to Coding: Coding

        # the context of the activities a user is taking - why the user is
        # accessing the data - that are controlled by this exception.
        self.purpose = None
        # type = array
        # reference to Coding: Coding

        # the class of information covered by this exception. the type can be a
        # fhir resource type, a profile on a type, or a cda document, or some
        # other type that indicates what sort of information the consent relates
        # to.
        self._class = None
        # type = array
        # reference to Coding: Coding

        # if this code is found in an instance, then the exception applies.
        self.code = None
        # type = array
        # reference to Coding: Coding

        # clinical or operational relevant period of time that bounds the data
        # controlled by this exception.
        self.dataPeriod = None
        # reference to Period: Period

        # the resources controlled by this exception, if specific resources are
        # referenced.
        self.data = None
        # type = array
        # reference to Consent_Data1: Consent_Data1


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value != None and value.lower() not in ['deny', 'permit']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'deny, permit'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'class'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'securityLabel'},

            {'parent_entity': 'Consent_Data1',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'data'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'action'},

            {'parent_entity': 'Consent_Actor1',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'actor'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'purpose'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'dataPeriod'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Consent_Except',
            'child_variable': 'period'},
        ]

class Consent_Actor1(fhirbase):
    """A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    def __init__(self, dict_values=None):
        # how the individual is involved in the resources content that is
        # described in the exception.
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # the resource that identifies the actor. to identify a actors by type,
        # use group to identify a set of actors by some property they share (e.g.
        # 'admitting officers').
        self.reference = None
        # reference to Reference: identifier


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
    """A record of a healthcare consumer’s policy choices, which permits or
    denies identified recipient(s) or recipient role(s) to perform one or
    more actions within a given policy context, for specific purposes and
    periods of time.
    """

    def __init__(self, dict_values=None):
        # how the resource reference is interpreted when testing consent
        # restrictions.
        self.meaning = None
        # type = string
        # possible values = instance, related, dependents, authoredby

        # a reference to a specific resource that defines which resources are
        # covered by this consent.
        self.reference = None
        # reference to Reference: identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.meaning is not None:
            for value in self.meaning:
                if value != None and value.lower() not in ['instance', 'related', 'dependents', 'authoredby']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'instance, related, dependents, authoredby'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Consent_Data1',
            'child_variable': 'reference'},
        ]

