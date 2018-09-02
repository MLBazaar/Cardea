from .fhirbase import fhirbase


class ActivityDefinition(fhirbase):
    """This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.
    """

    def __init__(self, dict_values=None):
        # this is a activitydefinition resource
        self.resourceType = 'ActivityDefinition'
        # type = string
        # possible values: ActivityDefinition

        # an absolute uri that is used to identify this activity definition when
        # it is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this activity definition is (or will be) published. the url should
        # include the major version of the activity definition. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the activity
        # definition when it is referenced in a specification, model, design or
        # instance. this is an arbitrary value managed by the activity definition
        # author and is not expected to be globally unique. for example, it might
        # be a timestamp (e.g. yyyymmdd) if a managed version is not available.
        # there is also no expectation that versions can be placed in a
        # lexicographical sequence. to provide a version consistent with the
        # decision support service specification, use the format
        # major.minor.revision (e.g. 1.0.0). for more information on versioning
        # knowledge assets, refer to the decision support service specification.
        # note that a version is required for non-experimental active assets.
        self.version = None
        # type = string

        # a natural language name identifying the activity definition. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # a short, descriptive, user-friendly title for the activity definition.
        self.title = None
        # type = string

        # the status of this activity definition. enables tracking the life-cycle
        # of the content.
        self.status = None
        # type = string
        # possible values: draft, active, retired, unknown

        # a boolean value to indicate that this activity definition is authored
        # for testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the activity definition was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the activity definition changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the activity
        # definition.
        self.publisher = None
        # type = string

        # a free text natural language description of the activity definition from
        # a consumer's perspective.
        self.description = None
        # type = string

        # explaination of why this activity definition is needed and why it has
        # been designed as it has.
        self.purpose = None
        # type = string

        # a detailed description of how the asset is used from a clinical
        # perspective.
        self.usage = None
        # type = string

        # the date on which the resource content was approved by the publisher.
        # approval happens once when the content is officially approved for usage.
        self.approvalDate = None
        # type = string

        # the date on which the resource content was last reviewed. review happens
        # periodically after approval, but doesn't change the original approval
        # date.
        self.lastReviewDate = None
        # type = string

        # the period during which the activity definition content was or is
        # planned to be in active use.
        self.effectivePeriod = None
        # reference to Period: Period

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate activity definition instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the activity definition is
        # intended to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # descriptive topics related to the content of the activity. topics
        # provide a high-level categorization of the activity that can be useful
        # for filtering and searching.
        self.topic = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a contributor to the content of the asset, including authors, editors,
        # reviewers, and endorsers.
        self.contributor = None
        # type = array
        # reference to Contributor: Contributor

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a copyright statement relating to the activity definition and/or its
        # contents. copyright statements are generally legal restrictions on the
        # use and publishing of the activity definition.
        self.copyright = None
        # type = string

        # related artifacts such as additional documentation, justification, or
        # bibliographic references.
        self.relatedArtifact = None
        # type = array
        # reference to RelatedArtifact: RelatedArtifact

        # a reference to a library resource containing any formal logic used by
        # the asset.
        self.library = None
        # type = array
        # reference to Reference: identifier

        # a description of the kind of resource the activity definition is
        # representing. for example, a medicationrequest, a procedurerequest, or a
        # communicationrequest. typically, but not always, this is a request
        # resource.
        self.kind = None
        # type = string

        # detailed description of the type of activity; e.g. what lab test, what
        # procedure, what kind of encounter.
        self.code = None
        # reference to CodeableConcept: CodeableConcept

        # the period, timing or frequency upon which the described activity is to
        # occur.
        self.timingTiming = None
        # reference to Timing: Timing

        # the period, timing or frequency upon which the described activity is to
        # occur.
        self.timingDateTime = None
        # type = string

        # the period, timing or frequency upon which the described activity is to
        # occur.
        self.timingPeriod = None
        # reference to Period: Period

        # the period, timing or frequency upon which the described activity is to
        # occur.
        self.timingRange = None
        # reference to Range: Range

        # identifies the facility where the activity will occur; e.g. home,
        # hospital, specific clinic, etc.
        self.location = None
        # reference to Reference: identifier

        # indicates who should participate in performing the action described.
        self.participant = None
        # type = array
        # reference to ActivityDefinition_Participant: ActivityDefinition_Participant

        # identifies the food, drug or other product being consumed or supplied in
        # the activity.
        self.productReference = None
        # reference to Reference: identifier

        # identifies the food, drug or other product being consumed or supplied in
        # the activity.
        self.productCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # identifies the quantity expected to be consumed at once (per dose, per
        # meal, etc.).
        self.quantity = None
        # reference to Quantity: Quantity

        # provides detailed dosage instructions in the same way that they are
        # described for medicationrequest resources.
        self.dosage = None
        # type = array
        # reference to Dosage: Dosage

        # indicates the sites on the subject's body where the procedure should be
        # performed (i.e. the target sites).
        self.bodySite = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a reference to a structuremap resource that defines a transform that can
        # be executed to produce the intent resource using the activitydefinition
        # instance as the input.
        self.transform = None
        # reference to Reference: identifier

        # dynamic values that will be evaluated to produce values for elements of
        # the resulting resource. for example, if the dosage of a medication must
        # be computed based on the patient's weight, a dynamic value would be used
        # to specify an expression that calculated the weight, and the path on the
        # intent resource that would contain the result.
        self.dynamicValue = None
        # type = array
        # reference to ActivityDefinition_DynamicValue: ActivityDefinition_DynamicValue

        # a formal identifier that is used to identify this activity definition
        # when it is represented in other formats, or referenced in a
        # specification, model, design or an instance.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'location'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'bodySite'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'topic'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'ActivityDefinition_DynamicValue',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'dynamicValue'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'dosage'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'transform'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'ActivityDefinition_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'participant'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'code'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'quantity'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingRange'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'productReference'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'productCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'library'},
        ]


class ActivityDefinition_Participant(fhirbase):
    """This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.
    """

    def __init__(self, dict_values=None):
        # the type of participant in the action.
        self.type = None
        # type = string

        # the role the participant should play in performing the described action.
        self.role = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition_Participant',
             'child_variable': 'role'},
        ]


class ActivityDefinition_DynamicValue(fhirbase):
    """This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.
    """

    def __init__(self, dict_values=None):
        # a brief, natural language description of the intended semantics of the
        # dynamic value.
        self.description = None
        # type = string

        # the path to the element to be customized. this is the path on the
        # resource that will hold the result of the calculation defined by the
        # expression.
        self.path = None
        # type = string

        # the media type of the language for the expression.
        self.language = None
        # type = string

        # an expression specifying the value of the customized element.
        self.expression = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
