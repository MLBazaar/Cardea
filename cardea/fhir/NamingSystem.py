from .fhirbase import fhirbase


class NamingSystem(fhirbase):
    """A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    def __init__(self, dict_values=None):
        # this is a namingsystem resource
        self.resourceType = 'NamingSystem'
        # type = string
        # possible values: NamingSystem

        # a natural language name identifying the naming system. this name should
        # be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # the status of this naming system. enables tracking the life-cycle of the
        # content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # indicates the purpose for the naming system - what kinds of things does
        # it make unique?
        self.kind = None
        # type = string
        # possible values: codesystem, identifier, root

        # the date  (and optionally time) when the naming system was published.
        # the date must change if and when the business version changes and it
        # must change if the status code changes. in addition, it should change
        # when the substantive content of the naming system changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the naming
        # system.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # the name of the organization that is responsible for issuing identifiers
        # or codes for this namespace and ensuring their non-collision.
        self.responsible = None
        # type = string

        # categorizes a naming system for easier search by grouping related naming
        # systems.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # a free text natural language description of the naming system from a
        # consumer's perspective. details about what the namespace identifies
        # including scope, granularity, version labeling, etc.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate naming system instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the naming system is intended to
        # be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # provides guidance on the use of the namespace, including the handling of
        # formatting characters, use of upper vs. lower case, etc.
        self.usage = None
        # type = string

        # indicates how the system may be identified when referenced in electronic
        # exchange.
        self.uniqueId = None
        # type = array
        # reference to NamingSystem_UniqueId: NamingSystem_UniqueId

        # for naming systems that are retired, indicates the naming system that
        # should be used in their place (if any).
        self.replacedBy = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

        if self.kind is not None:
            for value in self.kind:
                if value is not None and value.lower() not in [
                        'codesystem', 'identifier', 'root']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'codesystem, identifier, root'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem',
             'child_variable': 'contact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'NamingSystem_UniqueId',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem',
             'child_variable': 'uniqueId'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NamingSystem',
             'child_variable': 'replacedBy'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem',
             'child_variable': 'type'},
        ]


class NamingSystem_UniqueId(fhirbase):
    """A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    def __init__(self, dict_values=None):
        # identifies the unique identifier scheme used for this particular
        # identifier.
        self.type = None
        # type = string
        # possible values: oid, uuid, uri, other

        # the string that should be sent over the wire to identify the code system
        # or identifier system.
        self.value = None
        # type = string

        # indicates whether this identifier is the "preferred" identifier of this
        # type.
        self.preferred = None
        # type = boolean

        # notes about the past or intended usage of this identifier.
        self.comment = None
        # type = string

        # identifies the period of time over which this identifier is considered
        # appropriate to refer to the naming system.  outside of this window, the
        # identifier might be non-deterministic.
        self.period = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'oid', 'uuid', 'uri', 'other']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'oid, uuid, uri, other'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem_UniqueId',
             'child_variable': 'period'},
        ]
