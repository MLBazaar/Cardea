from .fhirbase import fhirbase


class ActivityDefinition(fhirbase):
    """
    This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.

    Attributes:
        resourceType: This is a ActivityDefinition resource
        url: An absolute URI that is used to identify this activity definition
            when it is referenced in a specification, model, design or an
            instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
            be an address at which this activity definition is (or will be)
            published. The URL SHOULD include the major version of the activity
            definition. For more information see [Technical and Business
            Versions](resource.html#versions).
        identifier: A formal identifier that is used to identify this activity
            definition when it is represented in other formats, or referenced in a
            specification, model, design or an instance.
        version: The identifier that is used to identify this version of the
            activity definition when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the activity
            definition author and is not expected to be globally unique. For
            example, it might be a timestamp (e.g. yyyymmdd) if a managed version
            is not available. There is also no expectation that versions can be
            placed in a lexicographical sequence. To provide a version consistent
            with the Decision Support Service specification, use the format
            Major.Minor.Revision (e.g. 1.0.0). For more information on versioning
            knowledge assets, refer to the Decision Support Service specification.
            Note that a version is required for non-experimental active assets.
        name: A natural language name identifying the activity definition.
            This name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        title: A short, descriptive, user-friendly title for the activity
            definition.
        status: The status of this activity definition. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this activity
            definition is authored for testing purposes (or
            education/evaluation/marketing), and is not intended to be used for
            genuine usage.
        date: The date  (and optionally time) when the activity definition was
            published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the activity definition
            changes.
        publisher: The name of the individual or organization that published
            the activity definition.
        description: A free text natural language description of the activity
            definition from a consumer's perspective.
        purpose: Explaination of why this activity definition is needed and
            why it has been designed as it has.
        usage: A detailed description of how the asset is used from a clinical
            perspective.
        approvalDate: The date on which the resource content was approved by
            the publisher. Approval happens once when the content is officially
            approved for usage.
        lastReviewDate: The date on which the resource content was last
            reviewed. Review happens periodically after approval, but doesn't
            change the original approval date.
        effectivePeriod: The period during which the activity definition
            content was or is planned to be in active use.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate activity definition
            instances.
        jurisdiction: A legal or geographic region in which the activity
            definition is intended to be used.
        topic: Descriptive topics related to the content of the activity.
            Topics provide a high-level categorization of the activity that can be
            useful for filtering and searching.
        contributor: A contributor to the content of the asset, including
            authors, editors, reviewers, and endorsers.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        copyright: A copyright statement relating to the activity definition
            and/or its contents. Copyright statements are generally legal
            restrictions on the use and publishing of the activity definition.
        relatedArtifact: Related artifacts such as additional documentation,
            justification, or bibliographic references.
        library: A reference to a Library resource containing any formal logic
            used by the asset.
        kind: A description of the kind of resource the activity definition is
            representing. For example, a MedicationRequest, a ProcedureRequest, or
            a CommunicationRequest. Typically, but not always, this is a Request
            resource.
        code: Detailed description of the type of activity; e.g. What lab
            test, what procedure, what kind of encounter.
        timingTiming: The period, timing or frequency upon which the described
            activity is to occur.
        timingDateTime: The period, timing or frequency upon which the
            described activity is to occur.
        timingPeriod: The period, timing or frequency upon which the described
            activity is to occur.
        timingRange: The period, timing or frequency upon which the described
            activity is to occur.
        location: Identifies the facility where the activity will occur; e.g.
            home, hospital, specific clinic, etc.
        participant: Indicates who should participate in performing the action
            described.
        productReference: Identifies the food, drug or other product being
            consumed or supplied in the activity.
        productCodeableConcept: Identifies the food, drug or other product
            being consumed or supplied in the activity.
        quantity: Identifies the quantity expected to be consumed at once (per
            dose, per meal, etc.).
        dosage: Provides detailed dosage instructions in the same way that
            they are described for MedicationRequest resources.
        bodySite: Indicates the sites on the subject's body where the
            procedure should be performed (I.e. the target sites).
        transform: A reference to a StructureMap resource that defines a
            transform that can be executed to produce the intent resource using
            the ActivityDefinition instance as the input.
        dynamicValue: Dynamic values that will be evaluated to produce values
            for elements of the resulting resource. For example, if the dosage of
            a medication must be computed based on the patient's weight, a dynamic
            value would be used to specify an expression that calculated the
            weight, and the path on the intent resource that would contain the
            result.
    """

    __name__ = 'ActivityDefinition'

    def __init__(self, dict_values=None):
        self.resourceType = 'ActivityDefinition'
        # type: string
        # possible values: ActivityDefinition

        self.url = None
        # type: string

        self.version = None
        # type: string

        self.name = None
        # type: string

        self.title = None
        # type: string

        self.status = None
        # type: string
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # type: boolean

        self.date = None
        # type: string

        self.publisher = None
        # type: string

        self.description = None
        # type: string

        self.purpose = None
        # type: string

        self.usage = None
        # type: string

        self.approvalDate = None
        # type: string

        self.lastReviewDate = None
        # type: string

        self.effectivePeriod = None
        # reference to Period

        self.useContext = None
        # type: array
        # reference to UsageContext

        self.jurisdiction = None
        # type: array
        # reference to CodeableConcept

        self.topic = None
        # type: array
        # reference to CodeableConcept

        self.contributor = None
        # type: array
        # reference to Contributor

        self.contact = None
        # type: array
        # reference to ContactDetail

        self.copyright = None
        # type: string

        self.relatedArtifact = None
        # type: array
        # reference to RelatedArtifact

        self.library = None
        # type: array
        # reference to Reference: identifier

        self.kind = None
        # type: string

        self.code = None
        # reference to CodeableConcept

        self.timingTiming = None
        # reference to Timing

        self.timingDateTime = None
        # type: string

        self.timingPeriod = None
        # reference to Period

        self.timingRange = None
        # reference to Range

        self.location = None
        # reference to Reference: identifier

        self.participant = None
        # type: array
        # reference to ActivityDefinition_Participant

        self.productReference = None
        # reference to Reference: identifier

        self.productCodeableConcept = None
        # reference to CodeableConcept

        self.quantity = None
        # reference to Quantity

        self.dosage = None
        # type: array
        # reference to Dosage

        self.bodySite = None
        # type: array
        # reference to CodeableConcept

        self.transform = None
        # reference to Reference: identifier

        self.dynamicValue = None
        # type: array
        # reference to ActivityDefinition_DynamicValue

        self.identifier = None
        # type: array
        # reference to Identifier

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

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'quantity'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'transform'},

            {'parent_entity': 'Dosage',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'dosage'},

            {'parent_entity': 'Contributor',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'contributor'},

            {'parent_entity': 'RelatedArtifact',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'relatedArtifact'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'contact'},

            {'parent_entity': 'ActivityDefinition_Participant',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'participant'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'productCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'topic'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'productReference'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'identifier'},

            {'parent_entity': 'ActivityDefinition_DynamicValue',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'dynamicValue'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'library'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'ActivityDefinition',
             'child_variable': 'timingPeriod'},
        ]


class ActivityDefinition_Participant(fhirbase):
    """
    This resource allows for the definition of some activity to be
    performed, independent of a particular patient, practitioner, or other
    performance context.

    Attributes:
        type: The type of participant in the action.
        role: The role the participant should play in performing the described
            action.
    """

    __name__ = 'ActivityDefinition_Participant'

    def __init__(self, dict_values=None):
        self.type = None
        # type: string

        self.role = None
        # reference to CodeableConcept

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

    Attributes:
        description: A brief, natural language description of the intended
            semantics of the dynamic value.
        path: The path to the element to be customized. This is the path on
            the resource that will hold the result of the calculation defined by
            the expression.
        language: The media type of the language for the expression.
        expression: An expression specifying the value of the customized
            element.
    """

    __name__ = 'ActivityDefinition_DynamicValue'

    def __init__(self, dict_values=None):
        self.description = None
        # type: string

        self.path = None
        # type: string

        self.language = None
        # type: string

        self.expression = None
        # type: string

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
