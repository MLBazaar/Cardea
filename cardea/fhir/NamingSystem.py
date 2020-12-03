from .fhirbase import fhirbase


class NamingSystem(fhirbase):
    """
    A curated namespace that issues unique symbols within that namespace
    for the identification of concepts, people, devices, etc.  Represents
    a "System" used within the Identifier and Coding data types.

    Args:
        resourceType: This is a NamingSystem resource
        name: A natural language name identifying the naming system. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.
        status: The status of this naming system. Enables tracking the
            life-cycle of the content.
        kind: Indicates the purpose for the naming system - what kinds of
            things does it make unique?
        date: The date  (and optionally time) when the naming system was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the naming system
            changes.
        publisher: The name of the individual or organization that published
            the naming system.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        responsible: The name of the organization that is responsible for
            issuing identifiers or codes for this namespace and ensuring their
            non-collision.
        type: Categorizes a naming system for easier search by grouping
            related naming systems.
        description: A free text natural language description of the naming
            system from a consumer's perspective. Details about what the namespace
            identifies including scope, granularity, version labeling, etc.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate naming system
            instances.
        jurisdiction: A legal or geographic region in which the naming system
            is intended to be used.
        usage: Provides guidance on the use of the namespace, including the
            handling of formatting characters, use of upper vs. lower case, etc.
        uniqueId: Indicates how the system may be identified when referenced
            in electronic exchange.
        replacedBy: For naming systems that are retired, indicates the naming
            system that should be used in their place (if any).
    """

    __name__ = 'NamingSystem'

    def __init__(self, dict_values=None):
        self.resourceType = 'NamingSystem'
        # type: str
        # possible values: NamingSystem

        self.name = None
        # type: str

        self.status = None
        # type: str
        # possible values: draft, active, retired, unknown

        self.kind = None
        # type: str
        # possible values: codesystem, identifier, root

        self.date = None
        # type: str

        self.publisher = None
        # type: str

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.responsible = None
        # type: str

        self.type = None
        # reference to CodeableConcept

        self.description = None
        # type: str

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.usage = None
        # type: str

        self.uniqueId = None
        # type: list
        # reference to NamingSystem_UniqueId

        self.replacedBy = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'NamingSystem',
             'child_variable': 'replacedBy'},

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

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem',
             'child_variable': 'type'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'NamingSystem',
             'child_variable': 'useContext'},
        ]


class NamingSystem_UniqueId(fhirbase):
    """
    A curated namespace that issues unique symbols within that namespace
    for the identification of concepts, people, devices, etc.  Represents
    a "System" used within the Identifier and Coding data types.

    Args:
        type: Identifies the unique identifier scheme used for this particular
            identifier.
        value: The string that should be sent over the wire to identify the
            code system or identifier system.
        preferred: Indicates whether this identifier is the "preferred"
            identifier of this type.
        comment: Notes about the past or intended usage of this identifier.
        period: Identifies the period of time over which this identifier is
            considered appropriate to refer to the naming system.  Outside of this
            window, the identifier might be non-deterministic.
    """

    __name__ = 'NamingSystem_UniqueId'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: oid, uuid, uri, other

        self.value = None
        # type: str

        self.preferred = None
        # type: bool

        self.comment = None
        # type: str

        self.period = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

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
