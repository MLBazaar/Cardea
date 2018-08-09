from .fhirbase import * 
from .Reference import Reference
from .Period import Period
from .Coding import Coding
from .Signature import Signature

class Provenance(fhirbase):
    """Provenance of a resource is a record that describes entities and
    processes involved in producing and delivering or otherwise influencing
    that resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement
    indicates clinical significance in terms of confidence in authenticity,
    reliability, and trustworthiness, integrity, and stage in lifecycle
    (e.g. Document Completion - has the artifact been legally
    authenticated), all of which may impact security, privacy, and trust
    policies.
    """

    def __init__(self, dict_values=None):
        # this is a provenance resource
        self.resourceType = 'Provenance'
        # type = string
        # possible values = Provenance

        # the reference(s) that were generated or updated by  the activity
        # described in this resource. a provenance can point to more than one
        # target if multiple resources were created/updated by the same activity.
        self.target = None
        # type = array
        # reference to Reference: identifier

        # the period during which the activity occurred.
        self.period = None
        # reference to Period: Period

        # the instant of time at which the activity was recorded.
        self.recorded = None
        # type = string

        # policy or plan the activity was defined by. typically, a single activity
        # may have multiple applicable policy documents, such as patient consent,
        # guarantor funding, etc.
        self.policy = None
        # type = array

        # where the activity occurred, if relevant.
        self.location = None
        # reference to Reference: identifier

        # the reason that the activity was taking place.
        self.reason = None
        # type = array
        # reference to Coding: Coding

        # an activity is something that occurs over a period of time and acts upon
        # or with entities; it may include consuming, processing, transforming,
        # modifying, relocating, using, or generating entities.
        self.activity = None
        # reference to Coding: Coding

        # an actor taking a role in an activity  for which it can be assigned some
        # degree of responsibility for the activity taking place.
        self.agent = None
        # type = array
        # reference to Provenance_Agent: Provenance_Agent

        # an entity used in this activity.
        self.entity = None
        # type = array
        # reference to Provenance_Entity: Provenance_Entity

        # a digital signature on the target reference(s). the signer should match
        # a provenance.agent. the purpose of the signature is indicated.
        self.signature = None
        # type = array
        # reference to Signature: Signature


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Provenance',
            'child_variable': 'target'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance',
            'child_variable': 'period'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Provenance',
            'child_variable': 'location'},

            {'parent_entity': 'Provenance_Agent',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance',
            'child_variable': 'agent'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance',
            'child_variable': 'activity'},

            {'parent_entity': 'Provenance_Entity',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance',
            'child_variable': 'entity'},

            {'parent_entity': 'Signature',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance',
            'child_variable': 'signature'},

            {'parent_entity': 'Coding',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance',
            'child_variable': 'reason'},
        ]

class Provenance_Agent(fhirbase):
    """Provenance of a resource is a record that describes entities and
    processes involved in producing and delivering or otherwise influencing
    that resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement
    indicates clinical significance in terms of confidence in authenticity,
    reliability, and trustworthiness, integrity, and stage in lifecycle
    (e.g. Document Completion - has the artifact been legally
    authenticated), all of which may impact security, privacy, and trust
    policies.
    """

    def __init__(self, dict_values=None):
        # the function of the agent with respect to the activity. the security
        # role enabling the agent with respect to the activity.
        # the function of the agent with respect to the activity. the security
        # role enabling the agent with respect to the activity.
        self.role = None
        # type = array
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # the individual, device or organization that participated in the event.
        # the individual, device or organization that participated in the event.
        self.whoUri = None
        # type = string
        # type = string

        # the individual, device or organization that participated in the event.
        # the individual, device or organization that participated in the event.
        self.whoReference = None
        # reference to Reference: identifier

        # the individual, device, or organization for whom the change was made.
        # the individual, device, or organization for whom the change was made.
        self.onBehalfOfUri = None
        # type = string
        # type = string

        # the individual, device, or organization for whom the change was made.
        # the individual, device, or organization for whom the change was made.
        self.onBehalfOfReference = None
        # reference to Reference: identifier

        # the type of relationship between agents.
        # the type of relationship between agents.
        self.relatedAgentType = None
        # reference to CodeableConcept: CodeableConcept


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Provenance_Agent',
            'child_variable': 'onBehalfOfReference'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance_Agent',
            'child_variable': 'relatedAgentType'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance_Agent',
            'child_variable': 'role'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Provenance_Agent',
            'child_variable': 'whoReference'},
        ]

class Provenance_Entity(fhirbase):
    """Provenance of a resource is a record that describes entities and
    processes involved in producing and delivering or otherwise influencing
    that resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement
    indicates clinical significance in terms of confidence in authenticity,
    reliability, and trustworthiness, integrity, and stage in lifecycle
    (e.g. Document Completion - has the artifact been legally
    authenticated), all of which may impact security, privacy, and trust
    policies.
    """

    def __init__(self, dict_values=None):
        # how the entity was used during the activity.
        self.role = None
        # type = string
        # possible values = derivation, revision, quotation, source, removal

        # identity of the  entity used. may be a logical or physical uri and maybe
        # absolute or relative.
        self.whatUri = None
        # type = string

        # identity of the  entity used. may be a logical or physical uri and maybe
        # absolute or relative.
        self.whatReference = None
        # reference to Reference: identifier

        # identity of the  entity used. may be a logical or physical uri and maybe
        # absolute or relative.
        self.whatIdentifier = None
        # reference to Identifier: Identifier

        # the entity is attributed to an agent to express the agent's
        # responsibility for that entity, possibly along with other agents. this
        # description can be understood as shorthand for saying that the agent was
        # responsible for the activity which generated the entity.
        self.agent = None
        # type = array
        # reference to Provenance_Agent: Provenance_Agent


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.role is not None:
            for value in self.role:
                if value != None and value.lower() not in ['derivation', 'revision', 'quotation', 'source', 'removal']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'derivation, revision, quotation, source, removal'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance_Entity',
            'child_variable': 'whatIdentifier'},

            {'parent_entity': 'Provenance_Agent',
            'parent_variable': 'object_id',
            'child_entity': 'Provenance_Entity',
            'child_variable': 'agent'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'Provenance_Entity',
            'child_variable': 'whatReference'},
        ]

