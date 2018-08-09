from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .UsageContext import UsageContext
from .ContactDetail import ContactDetail

class ImplementationGuide(fhirbase):
    """A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into
    a logical whole and to publish a computable definition of all the parts.
    """

    def __init__(self, dict_values=None):
        # this is a implementationguide resource
        self.resourceType = 'ImplementationGuide'
        # type = string
        # possible values = ImplementationGuide

        # an absolute uri that is used to identify this implementation guide when
        # it is referenced in a specification, model, design or an instance. this
        # shall be a url, should be globally unique, and should be an address at
        # which this implementation guide is (or will be) published. the url
        # should include the major version of the implementation guide. for more
        # information see [technical and business
        # versions](resource.html#versions).
        self.url = None
        # type = string

        # the identifier that is used to identify this version of the
        # implementation guide when it is referenced in a specification, model,
        # design or instance. this is an arbitrary value managed by the
        # implementation guide author and is not expected to be globally unique.
        # for example, it might be a timestamp (e.g. yyyymmdd) if a managed
        # version is not available. there is also no expectation that versions can
        # be placed in a lexicographical sequence.
        self.version = None
        # type = string

        # a natural language name identifying the implementation guide. this name
        # should be usable as an identifier for the module by machine processing
        # applications such as code generation.
        self.name = None
        # type = string

        # the status of this implementation guide. enables tracking the life-cycle
        # of the content.
        self.status = None
        # type = string
        # possible values = draft, active, retired, unknown

        # a boolean value to indicate that this implementation guide is authored
        # for testing purposes (or education/evaluation/marketing), and is not
        # intended to be used for genuine usage.
        self.experimental = None
        # type = boolean

        # the date  (and optionally time) when the implementation guide was
        # published. the date must change if and when the business version changes
        # and it must change if the status code changes. in addition, it should
        # change when the substantive content of the implementation guide changes.
        self.date = None
        # type = string

        # the name of the individual or organization that published the
        # implementation guide.
        self.publisher = None
        # type = string

        # contact details to assist a user in finding and communicating with the
        # publisher.
        self.contact = None
        # type = array
        # reference to ContactDetail: ContactDetail

        # a free text natural language description of the implementation guide
        # from a consumer's perspective.
        self.description = None
        # type = string

        # the content was developed with a focus and intent of supporting the
        # contexts that are listed. these terms may be used to assist with
        # indexing and searching for appropriate implementation guide instances.
        self.useContext = None
        # type = array
        # reference to UsageContext: UsageContext

        # a legal or geographic region in which the implementation guide is
        # intended to be used.
        self.jurisdiction = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # a copyright statement relating to the implementation guide and/or its
        # contents. copyright statements are generally legal restrictions on the
        # use and publishing of the implementation guide.
        self.copyright = None
        # type = string

        # the version of the fhir specification on which this implementationguide
        # is based - this is the formal version of the specification, without the
        # revision number, e.g. [publication].[major].[minor], which is 3.0.1 for
        # this version.
        self.fhirVersion = None
        # type = string

        # another implementation guide that this implementation depends on.
        # typically, an implementation guide uses value sets, profiles etc.defined
        # in other implementation guides.
        self.dependency = None
        # type = array
        # reference to ImplementationGuide_Dependency: ImplementationGuide_Dependency

        # a logical group of resources. logical groups can be used when building
        # pages.
        self.package = None
        # type = array
        # reference to ImplementationGuide_Package: ImplementationGuide_Package

        # a set of profiles that all resources covered by this implementation
        # guide must conform to.
        self._global = None
        # type = array
        # reference to ImplementationGuide_Global: ImplementationGuide_Global

        # a binary file that is included in the  implementation guide when it is
        # published.
        self.binary = None
        # type = array

        # a page / section in the implementation guide. the root page is the
        # implementation guide home page.
        self.page = None
        # reference to ImplementationGuide_Page: ImplementationGuide_Page


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['draft', 'active', 'retired', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'draft, active, retired, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'UsageContext',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide',
            'child_variable': 'useContext'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide',
            'child_variable': 'jurisdiction'},

            {'parent_entity': 'ImplementationGuide_Page',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide',
            'child_variable': 'page'},

            {'parent_entity': 'ImplementationGuide_Dependency',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide',
            'child_variable': 'dependency'},

            {'parent_entity': 'ContactDetail',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide',
            'child_variable': 'contact'},

            {'parent_entity': 'ImplementationGuide_Package',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide',
            'child_variable': 'package'},

            {'parent_entity': 'ImplementationGuide_Global',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide',
            'child_variable': 'global'},
        ]

class ImplementationGuide_Dependency(fhirbase):
    """A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into
    a logical whole and to publish a computable definition of all the parts.
    """

    def __init__(self, dict_values=None):
        # how the dependency is represented when the guide is published.
        self.type = None
        # type = string
        # possible values = reference, inclusion

        # where the dependency is located.
        self.uri = None
        # type = string


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value != None and value.lower() not in ['reference', 'inclusion']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'reference, inclusion'))

class ImplementationGuide_Package(fhirbase):
    """A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into
    a logical whole and to publish a computable definition of all the parts.
    """

    def __init__(self, dict_values=None):
        # the name for the group, as used in page.package.
        self.name = None
        # type = string

        # human readable text describing the package.
        self.description = None
        # type = string

        # a resource that is part of the implementation guide. conformance
        # resources (value set, structure definition, capability statements etc.)
        # are obvious candidates for inclusion, but any kind of resource can be
        # included as an example resource.
        self.resource = None
        # type = array
        # reference to ImplementationGuide_Resource: ImplementationGuide_Resource


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
    """A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into
    a logical whole and to publish a computable definition of all the parts.
    """

    def __init__(self, dict_values=None):
        # whether a resource is included in the guide as part of the rules defined
        # by the guide, or just as an example of a resource that conforms to the
        # rules and/or help implementers understand the intent of the guide.
        self.example = None
        # type = boolean

        # a human assigned name for the resource. all resources should have a
        # name, but the name may be extracted from the resource (e.g.
        # valueset.name).
        self.name = None
        # type = string

        # a description of the reason that a resource has been included in the
        # implementation guide.
        self.description = None
        # type = string

        # a short code that may be used to identify the resource throughout the
        # implementation guide.
        self.acronym = None
        # type = string

        # where this resource is found.
        self.sourceUri = None
        # type = string

        # where this resource is found.
        self.sourceReference = None
        # reference to Reference: identifier

        # another resource that this resource is an example for. this is mostly
        # used for resources that are included as examples of
        # structuredefinitions.
        self.exampleFor = None
        # reference to Reference: identifier


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
    """A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into
    a logical whole and to publish a computable definition of all the parts.
    """

    def __init__(self, dict_values=None):
        # the type of resource that all instances must conform to.
        self.type = None
        # type = string

        # a reference to the profile that all instances must conform to.
        self.profile = None
        # reference to Reference: identifier


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
    """A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into
    a logical whole and to publish a computable definition of all the parts.
    """

    def __init__(self, dict_values=None):
        # the source address for the page.
        # the source address for the page.
        self.source = None
        # type = string
        # type = string

        # a short title used to represent this page in navigational structures
        # such as table of contents, bread crumbs, etc.
        # a short title used to represent this page in navigational structures
        # such as table of contents, bread crumbs, etc.
        self.title = None
        # type = string
        # type = string

        # the kind of page that this is. some pages are autogenerated (list,
        # example), and other kinds are of interest so that tools can navigate the
        # user to the page of interest.
        # the kind of page that this is. some pages are autogenerated (list,
        # example), and other kinds are of interest so that tools can navigate the
        # user to the page of interest.
        self.kind = None
        # type = string
        # type = string
        # possible values = page, example, list, include, directory, dictionary, toc, resource
        # possible values = page, example, list, include, directory, dictionary, toc, resource

        # for constructed pages, what kind of resources to include in the list.
        # for constructed pages, what kind of resources to include in the list.
        self.type = None
        # type = array
        # type = array

        # for constructed pages, a list of packages to include in the page (or
        # else empty for everything).
        # for constructed pages, a list of packages to include in the page (or
        # else empty for everything).
        self.package = None
        # type = array
        # type = array

        # the format of the page.
        # the format of the page.
        self.format = None
        # type = string
        # type = string

        # nested pages/sections under this page.
        # nested pages/sections under this page.
        self.page = None
        # type = array
        # type = array
        # reference to ImplementationGuide_Page: ImplementationGuide_Page


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.kind is not None:
            for value in self.kind:
                if value != None and value.lower() not in ['page', 'example', 'list', 'include', 'directory', 'dictionary', 'toc', 'resource']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'page, example, list, include, directory, dictionary, toc, resource'))

        if self.kind is not None:
            for value in self.kind:
                if value != None and value.lower() not in ['page', 'example', 'list', 'include', 'directory', 'dictionary', 'toc', 'resource']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'page, example, list, include, directory, dictionary, toc, resource'))

    def get_relationships(self):

        return [
            {'parent_entity': 'ImplementationGuide_Page',
            'parent_variable': 'object_id',
            'child_entity': 'ImplementationGuide_Page',
            'child_variable': 'page'},
        ]

