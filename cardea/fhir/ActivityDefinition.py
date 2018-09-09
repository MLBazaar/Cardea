from .fhirbase import fhirbase


class ActivityDefinition(fhirbase):
    """
    This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.
    """

    __name__ = 'ActivityDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'ActivityDefinition'
        """
        This is a ActivityDefinition resource

        type: string
        possible values: ActivityDefinition
        """

        self.url = None
        """
        An absolute URI that is used to identify this activity definition when
        it is referenced in a specification, model, design or an instance.
        This SHALL be a URL, SHOULD be globally unique, and SHOULD be an
        address at which this activity definition is (or will be) published.
        The URL SHOULD include the major version of the activity definition.
        For more information see [Technical and Business
        Versions](resource.html#versions).

        type: string
        """

        self.version = None
        """
        The identifier that is used to identify this version of the activity
        definition when it is referenced in a specification, model, design or
        instance. This is an arbitrary value managed by the activity
        definition author and is not expected to be globally unique. For
        example, it might be a timestamp (e.g. yyyymmdd) if a managed version
        is not available. There is also no expectation that versions can be
        placed in a lexicographical sequence. To provide a version consistent
        with the Decision Support Service specification, use the format
        Major.Minor.Revision (e.g. 1.0.0). For more information on versioning
        knowledge assets, refer to the Decision Support Service specification.
        Note that a version is required for non-experimental active assets.

        type: string
        """

        self.name = None
        """
        A natural language name identifying the activity definition. This name
        should be usable as an identifier for the module by machine processing
        applications such as code generation.

        type: string
        """

        self.title = None
        """
        A short, descriptive, user-friendly title for the activity definition.

        type: string
        """

        self.status = None
        """
        The status of this activity definition. Enables tracking the
        life-cycle of the content.

        type: string
        possible values: draft, active, retired, unknown
        """

        self.experimental = None
        """
        A boolean value to indicate that this activity definition is authored
        for testing purposes (or education/evaluation/marketing), and is not
        intended to be used for genuine usage.

        type: boolean
        """

        self.date = None
        """
        The date  (and optionally time) when the activity definition was
        published. The date must change if and when the business version
        changes and it must change if the status code changes. In addition, it
        should change when the substantive content of the activity definition
        changes.

        type: string
        """

        self.publisher = None
        """
        The name of the individual or organization that published the activity
        definition.

        type: string
        """

        self.description = None
        """
        A free text natural language description of the activity definition
        from a consumer's perspective.

        type: string
        """

        self.purpose = None
        """
        Explaination of why this activity definition is needed and why it has
        been designed as it has.

        type: string
        """

        self.usage = None
        """
        A detailed description of how the asset is used from a clinical
        perspective.

        type: string
        """

        self.approvalDate = None
        """
        The date on which the resource content was approved by the publisher.
        Approval happens once when the content is officially approved for
        usage.

        type: string
        """

        self.lastReviewDate = None
        """
        The date on which the resource content was last reviewed. Review
        happens periodically after approval, but doesn't change the original
        approval date.

        type: string
        """

        self.effectivePeriod = None
        """
        The period during which the activity definition content was or is
        planned to be in active use.

        reference to Period
        """

        self.useContext = None
        """
        The content was developed with a focus and intent of supporting the
        contexts that are listed. These terms may be used to assist with
        indexing and searching for appropriate activity definition instances.

        type: array
        reference to UsageContext
        """

        self.jurisdiction = None
        """
        A legal or geographic region in which the activity definition is
        intended to be used.

        type: array
        reference to CodeableConcept
        """

        self.topic = None
        """
        Descriptive topics related to the content of the activity. Topics
        provide a high-level categorization of the activity that can be useful
        for filtering and searching.

        type: array
        reference to CodeableConcept
        """

        self.contributor = None
        """
        A contributor to the content of the asset, including authors, editors,
        reviewers, and endorsers.

        type: array
        reference to Contributor
        """

        self.contact = None
        """
        Contact details to assist a user in finding and communicating with the
        publisher.

        type: array
        reference to ContactDetail
        """

        self.copyright = None
        """
        A copyright statement relating to the activity definition and/or its
        contents. Copyright statements are generally legal restrictions on the
        use and publishing of the activity definition.

        type: string
        """

        self.relatedArtifact = None
        """
        Related artifacts such as additional documentation, justification, or
        bibliographic references.

        type: array
        reference to RelatedArtifact
        """

        self.library = None
        """
        A reference to a Library resource containing any formal logic used by
        the asset.

        type: array
        reference to Reference: identifier
        """

        self.kind = None
        """
        A description of the kind of resource the activity definition is
        representing. For example, a MedicationRequest, a ProcedureRequest, or
        a CommunicationRequest. Typically, but not always, this is a Request
        resource.

        type: string
        """

        self.code = None
        """
        Detailed description of the type of activity; e.g. What lab test, what
        procedure, what kind of encounter.

        reference to CodeableConcept
        """

        self.timingTiming = None
        """
        The period, timing or frequency upon which the described activity is
        to occur.

        reference to Timing
        """

        self.timingDateTime = None
        """
        The period, timing or frequency upon which the described activity is
        to occur.

        type: string
        """

        self.timingPeriod = None
        """
        The period, timing or frequency upon which the described activity is
        to occur.

        reference to Period
        """

        self.timingRange = None
        """
        The period, timing or frequency upon which the described activity is
        to occur.

        reference to Range
        """

        self.location = None
        """
        Identifies the facility where the activity will occur; e.g. home,
        hospital, specific clinic, etc.

        reference to Reference: identifier
        """

        self.participant = None
        """
        Indicates who should participate in performing the action described.

        type: array
        reference to ActivityDefinition_Participant
        """

        self.productReference = None
        """
        Identifies the food, drug or other product being consumed or supplied
        in the activity.

        reference to Reference: identifier
        """

        self.productCodeableConcept = None
        """
        Identifies the food, drug or other product being consumed or supplied
        in the activity.

        reference to CodeableConcept
        """

        self.quantity = None
        """
        Identifies the quantity expected to be consumed at once (per dose, per
        meal, etc.).

        reference to Quantity
        """

        self.dosage = None
        """
        Provides detailed dosage instructions in the same way that they are
        described for MedicationRequest resources.

        type: array
        reference to Dosage
        """

        self.bodySite = None
        """
        Indicates the sites on the subject's body where the procedure should
        be performed (I.e. the target sites).

        type: array
        reference to CodeableConcept
        """

        self.transform = None
        """
        A reference to a StructureMap resource that defines a transform that
        can be executed to produce the intent resource using the
        ActivityDefinition instance as the input.

        reference to Reference: identifier
        """

        self.dynamicValue = None
        """
        Dynamic values that will be evaluated to produce values for elements
        of the resulting resource. For example, if the dosage of a medication
        must be computed based on the patient's weight, a dynamic value would
        be used to specify an expression that calculated the weight, and the
        path on the intent resource that would contain the result.

        type: array
        reference to ActivityDefinition_DynamicValue
        """

        self.identifier = None
        """
        A formal identifier that is used to identify this activity definition
        when it is represented in other formats, or referenced in a
        specification, model, design or an instance.

        type: array
        reference to Identifier
        """

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
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'library'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingRange'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'productReference'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'transform'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'dosage'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'productCodeableConcept'},

            {'parent_entity': 'ActivityDefinition_DynamicValue',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'dynamicValue'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'code'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'location'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'ActivityDefinition_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'participant'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'topic'},
        ]


class ActivityDefinition_Participant(fhirbase):
    """
    This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.
    """

    __name__ = 'ActivityDefinition_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        """
        The type of participant in the action.

        type: string
        """

        self.role = None
        """
        The role the participant should play in performing the described
        action.

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
             'child_entity': 'ActivityDefinition_Participant',
             'child_variable': 'role'},
        ]


class ActivityDefinition_DynamicValue(fhirbase):
    """
    This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.
    """

    __name__ = 'ActivityDefinition_DynamicValue'

    def __init__(self, dict_values=None):
        self.description = None
        """
        A brief, natural language description of the intended semantics of the
        dynamic value.

        type: string
        """

        self.path = None
        """
        The path to the element to be customized. This is the path on the
        resource that will hold the result of the calculation defined by the
        expression.

        type: string
        """

        self.language = None
        """
        The media type of the language for the expression.

        type: string
        """

        self.expression = None
        """
        An expression specifying the value of the customized element.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
