from .fhirbase import fhirbase


class ImplementationGuide(fhirbase):
    """
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide
    into a logical whole and to publish a computable definition of all the
    parts.

    Args:
        resourceType: This is a ImplementationGuide resource
        url: An absolute URI that is used to identify this implementation
            guide when it is referenced in a specification, model, design or an
            instance. This SHALL be a URL, SHOULD be globally unique, and SHOULD
            be an address at which this implementation guide is (or will be)
            published. The URL SHOULD include the major version of the
            implementation guide. For more information see [Technical and Business
            Versions](resource.html#versions).
        version: The identifier that is used to identify this version of the
            implementation guide when it is referenced in a specification, model,
            design or instance. This is an arbitrary value managed by the
            implementation guide author and is not expected to be globally unique.
            For example, it might be a timestamp (e.g. yyyymmdd) if a managed
            version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.
        name: A natural language name identifying the implementation guide.
            This name should be usable as an identifier for the module by machine
            processing applications such as code generation.
        status: The status of this implementation guide. Enables tracking the
            life-cycle of the content.
        experimental: A boolean value to indicate that this implementation
            guide is authored for testing purposes (or
            education/evaluation/marketing), and is not intended to be used for
            genuine usage.
        date: The date  (and optionally time) when the implementation guide
            was published. The date must change if and when the business version
            changes and it must change if the status code changes. In addition, it
            should change when the substantive content of the implementation guide
            changes.
        publisher: The name of the individual or organization that published
            the implementation guide.
        contact: Contact details to assist a user in finding and communicating
            with the publisher.
        description: A free text natural language description of the
            implementation guide from a consumer's perspective.
        useContext: The content was developed with a focus and intent of
            supporting the contexts that are listed. These terms may be used to
            assist with indexing and searching for appropriate implementation
            guide instances.
        jurisdiction: A legal or geographic region in which the implementation
            guide is intended to be used.
        copyright: A copyright statement relating to the implementation guide
            and/or its contents. Copyright statements are generally legal
            restrictions on the use and publishing of the implementation guide.
        fhirVersion: The version of the FHIR specification on which this
            ImplementationGuide is based - this is the formal version of the
            specification, without the revision number, e.g.
            [publication].[major].[minor], which is 3.0.1 for this version.
        dependency: Another implementation guide that this implementation
            depends on. Typically, an implementation guide uses value sets,
            profiles etc.defined in other implementation guides.
        package: A logical group of resources. Logical groups can be used when
            building pages.
        global: A set of profiles that all resources covered by this
            implementation guide must conform to.
        binary: A binary file that is included in the  implementation guide
            when it is published.
        page: A page / section in the implementation guide. The root page is
            the implementation guide home page.
    """

    __name__ = 'ImplementationGuide'

    def __init__(self, dict_values=None):
        self.resourceType = 'ImplementationGuide'
        # type: str
        # possible values: ImplementationGuide

        self.url = None
        # type: str

        self.version = None
        # type: str

        self.name = None
        # type: str

        self.status = None
        # type: str
        # possible values: draft, active, retired, unknown

        self.experimental = None
        # type: bool

        self.date = None
        # type: str

        self.publisher = None
        # type: str

        self.contact = None
        # type: list
        # reference to ContactDetail

        self.description = None
        # type: str

        self.useContext = None
        # type: list
        # reference to UsageContext

        self.jurisdiction = None
        # type: list
        # reference to CodeableConcept

        self.copyright = None
        # type: str

        self.fhirVersion = None
        # type: str

        self.dependency = None
        # type: list
        # reference to ImplementationGuide_Dependency

        self.package = None
        # type: list
        # reference to ImplementationGuide_Package

        self._global = None
        # type: list
        # reference to ImplementationGuide_Global

        self.binary = None
        # type: list

        self.page = None
        # reference to ImplementationGuide_Page

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

    def get_relationships(self):

        return [
            {'parent_entity': 'ImplementationGuide_Package',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide',
             'child_variable': 'package'},

            {'parent_entity': 'ContactDetail',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide',
             'child_variable': 'contact'},

            {'parent_entity': 'ImplementationGuide_Global',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide',
             'child_variable': '_global'},

            {'parent_entity': 'ImplementationGuide_Dependency',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide',
             'child_variable': 'dependency'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide',
             'child_variable': 'jurisdiction'},

            {'parent_entity': 'UsageContext',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide',
             'child_variable': 'useContext'},

            {'parent_entity': 'ImplementationGuide_Page',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide',
             'child_variable': 'page'},
        ]


class ImplementationGuide_Dependency(fhirbase):
    """
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide
    into a logical whole and to publish a computable definition of all the
    parts.

    Args:
        type: How the dependency is represented when the guide is published.
        uri: Where the dependency is located.
    """

    __name__ = 'ImplementationGuide_Dependency'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str
        # possible values: reference, inclusion

        self.uri = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                        'reference', 'inclusion']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'reference, inclusion'))


class ImplementationGuide_Package(fhirbase):
    """
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide
    into a logical whole and to publish a computable definition of all the
    parts.

    Args:
        name: The name for the group, as used in page.package.
        description: Human readable text describing the package.
        resource: A resource that is part of the implementation guide.
            Conformance resources (value set, structure definition, capability
            statements etc.) are obvious candidates for inclusion, but any kind of
            resource can be included as an example resource.
    """

    __name__ = 'ImplementationGuide_Package'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.description = None
        # type: str

        self.resource = None
        # type: list
        # reference to ImplementationGuide_Resource

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ImplementationGuide_Resource',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide_Package',
             'child_variable': 'resource'},
        ]


class ImplementationGuide_Resource(fhirbase):
    """
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide
    into a logical whole and to publish a computable definition of all the
    parts.

    Args:
        example: Whether a resource is included in the guide as part of the
            rules defined by the guide, or just as an example of a resource that
            conforms to the rules and/or help implementers understand the intent
            of the guide.
        name: A human assigned name for the resource. All resources SHOULD
            have a name, but the name may be extracted from the resource (e.g.
            ValueSet.name).
        description: A description of the reason that a resource has been
            included in the implementation guide.
        acronym: A short code that may be used to identify the resource
            throughout the implementation guide.
        sourceUri: Where this resource is found.
        sourceReference: Where this resource is found.
        exampleFor: Another resource that this resource is an example for.
            This is mostly used for resources that are included as examples of
            StructureDefinitions.
    """

    __name__ = 'ImplementationGuide_Resource'

    def __init__(self, dict_values=None):
        self.example = None
        # type: bool

        self.name = None
        # type: str

        self.description = None
        # type: str

        self.acronym = None
        # type: str

        self.sourceUri = None
        # type: str

        self.sourceReference = None
        # reference to Reference: identifier

        self.exampleFor = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImplementationGuide_Resource',
             'child_variable': 'sourceReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImplementationGuide_Resource',
             'child_variable': 'exampleFor'},
        ]


class ImplementationGuide_Global(fhirbase):
    """
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide
    into a logical whole and to publish a computable definition of all the
    parts.

    Args:
        type: The type of resource that all instances must conform to.
        profile: A reference to the profile that all instances must conform
            to.
    """

    __name__ = 'ImplementationGuide_Global'

    def __init__(self, dict_values=None):
        self.type = None
        # type: str

        self.profile = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ImplementationGuide_Global',
             'child_variable': 'profile'},
        ]


class ImplementationGuide_Page(fhirbase):
    """
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide
    into a logical whole and to publish a computable definition of all the
    parts.

    Args:
        source: The source address for the page.
        title: A short title used to represent this page in navigational
            structures such as table of contents, bread crumbs, etc.
        kind: The kind of page that this is. Some pages are autogenerated
            (list, example), and other kinds are of interest so that tools can
            navigate the user to the page of interest.
        type: For constructed pages, what kind of resources to include in the
            list.
        package: For constructed pages, a list of packages to include in the
            page (or else empty for everything).
        format: The format of the page.
        page: Nested Pages/Sections under this page.
    """

    __name__ = 'ImplementationGuide_Page'

    def __init__(self, dict_values=None):
        self.source = None
        # type: str

        self.title = None
        # type: str

        self.kind = None
        # type: str
        # possible values: page, example, list, include, directory,
        # dictionary, toc, resource

        self.type = None
        # type: list

        self.package = None
        # type: list

        self.format = None
        # type: str

        self.page = None
        # type: list
        # reference to ImplementationGuide_Page

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.kind is not None:
            for value in self.kind:
                if value is not None and value.lower() not in [
                    'page', 'example', 'list', 'include', 'directory', 'dictionary',
                        'toc', 'resource']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'page, example, list, include, directory, dictionary, toc, '
                        'resource'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ImplementationGuide_Page',
             'parent_variable': 'object_id',
             'child_entity': 'ImplementationGuide_Page',
             'child_variable': 'page'},
        ]
