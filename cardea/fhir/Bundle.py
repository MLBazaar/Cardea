from .fhirbase import fhirbase


class Bundle(fhirbase):
    """
    A container for a collection of resources.

    Args:
        resourceType: This is a Bundle resource
        identifier: A persistent identifier for the batch that won't change as
            a batch is copied from server to server.
        type: Indicates the purpose of this bundle - how it was intended to be
            used.
        total: If a set of search matches, this is the total number of matches
            for the search (as opposed to the number of results in this bundle).
        link: A series of links that provide context to this bundle.
        entry: An entry in a bundle resource - will either contain a resource,
            or information about a resource (transactions and history only).
        signature: Digital Signature - base64 encoded. XML-DSIg or a JWT.
    """

    __name__ = 'Bundle'

    def __init__(self, dict_values=None):
        self.resourceType = 'Bundle'
        # type: str
        # possible values: Bundle

        self.type = None
        # type: str
        # possible values: document, message, transaction,
        # transaction-response, batch, batch-response, history, searchset,
        # collection

        self.total = None
        # type: int

        self.link = None
        # type: list
        # reference to Bundle_Link

        self.entry = None
        # type: list
        # reference to Bundle_Entry

        self.signature = None
        # reference to Signature

        self.identifier = None
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'document', 'message', 'transaction', 'transaction-response', 'batch',
                        'batch-response', 'history', 'searchset', 'collection']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'document, message, transaction, transaction-response, batch,'
                        'batch-response, history, searchset, collection'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Signature',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'signature'},

            {'parent_entity': 'Bundle_Entry',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'entry'},

            {'parent_entity': 'Bundle_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'link'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle',
             'child_variable': 'identifier'},
        ]


class Bundle_Link(fhirbase):
    """
    A container for a collection of resources.

    Args:
        relation: A name which details the functional use for this link - see
            [http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1).
        url: The reference details for the link.
    """

    __name__ = 'Bundle_Link'

    def __init__(self, dict_values=None):
        self.relation = None
        # type: str

        self.url = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)


class Bundle_Entry(fhirbase):
    """
    A container for a collection of resources.

    Args:
        link: A series of links that provide context to this entry.
        fullUrl: The Absolute URL for the resource.  The fullUrl SHALL not
            disagree with the id in the resource. The fullUrl is a version
            independent reference to the resource. The fullUrl element SHALL have
            a value except that:  * fullUrl can be empty on a POST (although it
            does not need to when specifying a temporary id for reference in the
            bundle) * Results from operations might involve resources that are not
            identified.
        resource: The Resources for the entry.
        search: Information about the search process that lead to the creation
            of this entry.
        request: Additional information about how this entry should be
            processed as part of a transaction.
        response: Additional information about how this entry should be
            processed as part of a transaction.
    """

    __name__ = 'Bundle_Entry'

    def __init__(self, dict_values=None):
        self.link = None
        # type: list
        # reference to Bundle_Link

        self.fullUrl = None
        # type: str

        self.resource = None
        # reference to ResourceList

        self.search = None
        # reference to Bundle_Search

        self.request = None
        # reference to Bundle_Request

        self.response = None
        # reference to Bundle_Response

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Bundle_Search',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'search'},

            {'parent_entity': 'Bundle_Response',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'response'},

            {'parent_entity': 'Bundle_Link',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'link'},

            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'resource'},

            {'parent_entity': 'Bundle_Request',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Entry',
             'child_variable': 'request'},
        ]


class Bundle_Search(fhirbase):
    """
    A container for a collection of resources.

    Args:
        mode: Why this entry is in the result set - whether it's included as a
            match or because of an _include requirement.
        score: When searching, the server's search ranking score for the
            entry.
    """

    __name__ = 'Bundle_Search'

    def __init__(self, dict_values=None):
        self.mode = None
        # type: str
        # possible values: match, include, outcome

        self.score = None
        # type: int

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.mode is not None:
            for value in self.mode:
                if value is not None and value.lower() not in [
                        'match', 'include', 'outcome']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'match, include, outcome'))


class Bundle_Request(fhirbase):
    """
    A container for a collection of resources.

    Args:
        method: The HTTP verb for this entry in either a change history, or a
            transaction/ transaction response.
        url: The URL for this entry, relative to the root (the address to
            which the request is posted).
        ifNoneMatch: If the ETag values match, return a 304 Not Modified
            status. See the API documentation for ["Conditional
            Read"](http.html#cread).
        ifModifiedSince: Only perform the operation if the last updated date
            matches. See the API documentation for ["Conditional
            Read"](http.html#cread).
        ifMatch: Only perform the operation if the Etag value matches. For
            more information, see the API section ["Managing Resource
            Contention"](http.html#concurrency).
        ifNoneExist: Instruct the server not to perform the create if a
            specified resource already exists. For further information, see the
            API documentation for ["Conditional Create"](http.html#ccreate). This
            is just the query portion of the URL - what follows the "?" (not
            including the "?").
    """

    __name__ = 'Bundle_Request'

    def __init__(self, dict_values=None):
        self.method = None
        # type: str
        # possible values: GET, POST, PUT, DELETE

        self.url = None
        # type: str

        self.ifNoneMatch = None
        # type: str

        self.ifModifiedSince = None
        # type: str

        self.ifMatch = None
        # type: str

        self.ifNoneExist = None
        # type: str

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.method is not None:
            for value in self.method:
                if value is not None and value.lower() not in [
                        'get', 'post', 'put', 'delete']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'GET, POST, PUT, DELETE'))


class Bundle_Response(fhirbase):
    """
    A container for a collection of resources.

    Args:
        status: The status code returned by processing this entry. The status
            SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the
            standard HTTP description associated with the status code.
        location: The location header created by processing this operation.
        etag: The etag for the resource, it the operation for the entry
            produced a versioned resource (see [Resource Metadata and
            Versioning](http.html#versioning) and [Managing Resource
            Contention](http.html#concurrency)).
        lastModified: The date/time that the resource was modified on the
            server.
        outcome: An OperationOutcome containing hints and warnings produced as
            part of processing this entry in a batch or transaction.
    """

    __name__ = 'Bundle_Response'

    def __init__(self, dict_values=None):
        self.status = None
        # type: str

        self.location = None
        # type: str

        self.etag = None
        # type: str

        self.lastModified = None
        # type: str

        self.outcome = None
        # reference to ResourceList

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'ResourceList',
             'parent_variable': 'object_id',
             'child_entity': 'Bundle_Response',
             'child_variable': 'outcome'},
        ]
