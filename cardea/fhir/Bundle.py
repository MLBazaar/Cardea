from .fhirbase import fhirbase


class Bundle(fhirbase):
    """A container for a collection of resources.
    """

    __name__ = 'Bundle'

    def __init__(self, dict_values=None):
        # this is a bundle resource
        self.resourceType = 'Bundle'
        # type = string
        # possible values: Bundle

        # indicates the purpose of this bundle - how it was intended to be used.
        self.type = None
        # type = string
        # possible values: document, message, transaction, transaction-
        # response, batch, batch-response, history, searchset, collection

        # if a set of search matches, this is the total number of matches for the
        # search (as opposed to the number of results in this bundle).
        self.total = None
        # type = int

        # a series of links that provide context to this bundle.
        self.link = None
        # type = array
        # reference to Bundle_Link: Bundle_Link

        # an entry in a bundle resource - will either contain a resource, or
        # information about a resource (transactions and history only).
        self.entry = None
        # type = array
        # reference to Bundle_Entry: Bundle_Entry

        # digital signature - base64 encoded. xml-dsig or a jwt.
        self.signature = None
        # reference to Signature: Signature

        # a persistent identifier for the batch that won't change as a batch is
        # copied from server to server.
        self.identifier = None
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'document', 'message', 'transaction', 'transaction-response', 'batch',
                        'batch-response', 'history', 'searchset', 'collection']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'document, message, transaction, transaction-response,'
                        'batch, batch-response, history, searchset, collection'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'signature'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'identifier'},

            {'parent_entity': 'Bundle_Entry',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'entry'},

            {'parent_entity': 'Bundle_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'link'},
        ]


class Bundle_Link(fhirbase):
    """A container for a collection of resources.
    """

    __name__ = 'Bundle_Link'

    def __init__(self, dict_values=None):
        # a name which details the functional use for this link - see
        # [http://www.iana.org/assignments/link-relations/link-
        # relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-
        # relations/link-relations.xhtml#link-relations-1).
        self.relation = None
        # type = string

        # the reference details for the link.
        self.url = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)


class Bundle_Entry(fhirbase):
    """A container for a collection of resources.
    """

    __name__ = 'Bundle_Entry'

    def __init__(self, dict_values=None):
        # a series of links that provide context to this entry.
        self.link = None
        # type = array
        # reference to Bundle_Link: Bundle_Link

        # the absolute url for the resource.  the fullurl shall not disagree with
        # the id in the resource. the fullurl is a version independent reference
        # to the resource. the fullurl element shall have a value except that:  *
        # fullurl can be empty on a post (although it does not need to when
        # specifying a temporary id for reference in the bundle) * results from
        # operations might involve resources that are not identified.
        self.fullUrl = None
        # type = string

        # the resources for the entry.
        self.resource = None
        # reference to ResourceList: ResourceList

        # information about the search process that lead to the creation of this
        # entry.
        self.search = None
        # reference to Bundle_Search: Bundle_Search

        # additional information about how this entry should be processed as part
        # of a transaction.
        self.request = None
        # reference to Bundle_Request: Bundle_Request

        # additional information about how this entry should be processed as part
        # of a transaction.
        self.response = None
        # reference to Bundle_Response: Bundle_Response

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Bundle_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'link'},

            {'parent_entity': 'Bundle_Search',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'search'},

            {'parent_entity': 'Bundle_Response',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'response'},

            {'parent_entity': 'Bundle_Request',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'request'},

            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'resource'},
        ]


class Bundle_Search(fhirbase):
    """A container for a collection of resources.
    """

    __name__ = 'Bundle_Search'

    def __init__(self, dict_values=None):
        # why this entry is in the result set - whether it's included as a match
        # or because of an _include requirement.
        self.mode = None
        # type = string
        # possible values: match, include, outcome

        # when searching, the server's search ranking score for the entry.
        self.score = None
        # type = int

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'match', 'include', 'outcome']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'match, include, outcome'))


class Bundle_Request(fhirbase):
    """A container for a collection of resources.
    """

    __name__ = 'Bundle_Request'

    def __init__(self, dict_values=None):
        # the http verb for this entry in either a change history, or a
        # transaction/ transaction response.
        self.method = None
        # type = string
        # possible values: GET, POST, PUT, DELETE

        # the url for this entry, relative to the root (the address to which the
        # request is posted).
        self.url = None
        # type = string

        # if the etag values match, return a 304 not modified status. see the api
        # documentation for ["conditional read"](http.html#cread).
        self.ifNoneMatch = None
        # type = string

        # only perform the operation if the last updated date matches. see the api
        # documentation for ["conditional read"](http.html#cread).
        self.ifModifiedSince = None
        # type = string

        # only perform the operation if the etag value matches. for more
        # information, see the api section ["managing resource
        # contention"](http.html#concurrency).
        self.ifMatch = None
        # type = string

        # instruct the server not to perform the create if a specified resource
        # already exists. for further information, see the api documentation for
        # ["conditional create"](http.html#ccreate). this is just the query
        # portion of the url - what follows the "?" (not including the "?").
        self.ifNoneExist = None
        # type = string

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.method is not None:
            for value in self.method:
                if value is not None and value.lower() not in [
                        'get', 'post', 'put', 'delete']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'GET, POST, PUT, DELETE'))


class Bundle_Response(fhirbase):
    """A container for a collection of resources.
    """

    __name__ = 'Bundle_Response'

    def __init__(self, dict_values=None):
        # the status code returned by processing this entry. the status shall
        # start with a 3 digit http code (e.g. 404) and may contain the standard
        # http description associated with the status code.
        self.status = None
        # type = string

        # the location header created by processing this operation.
        self.location = None
        # type = string

        # the etag for the resource, it the operation for the entry produced a
        # versioned resource (see [resource metadata and
        # versioning](http.html#versioning) and [managing resource
        # contention](http.html#concurrency)).
        self.etag = None
        # type = string

        # the date/time that the resource was modified on the server.
        self.lastModified = None
        # type = string

        # an operationoutcome containing hints and warnings produced as part of
        # processing this entry in a batch or transaction.
        self.outcome = None
        # reference to ResourceList: ResourceList

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Response',
             'child_variable': 'outcome'},
        ]
