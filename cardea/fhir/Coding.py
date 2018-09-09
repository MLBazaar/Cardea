from .fhirbase import fhirbase


class Coding(fhirbase):
    """A reference to a code defined by a terminology system.
    """

    def __init__(self, dict_values=None):
        # the identification of the code system that defines the meaning of the
        # symbol in the code.
        self.system = None
        # type = string

        # the version of the code system which was used when choosing this code.
        # note that a well-maintained code system does not need the version
        # reported, because the meaning of codes is consistent across versions.
        # however this cannot consistently be assured. and when the meaning is not
        # guaranteed to be consistent, the version should be exchanged.
        self.version = None
        # type = string

        # a symbol in syntax defined by the system. the symbol may be a predefined
        # code or an expression in a syntax defined by the coding system (e.g.
        # post-coordination).
        self.code = None
        # type = string

        # a representation of the meaning of the code in the system, following the
        # rules of the system.
        self.display = None
        # type = string

        # indicates that this coding was chosen by a user directly - i.e. off a
        # pick list of available items (codes or displays).
        self.userSelected = None
        # type = boolean

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)
