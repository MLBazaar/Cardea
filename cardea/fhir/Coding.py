from .fhirbase import fhirbase


class Coding(fhirbase):
    """
    A reference to a code defined by a terminology system.

    Args:
        system: The identification of the code system that defines the meaning
            of the symbol in the code.
        version: The version of the code system which was used when choosing
            this code. Note that a well-maintained code system does not need the
            version reported, because the meaning of codes is consistent across
            versions. However this cannot consistently be assured. and when the
            meaning is not guaranteed to be consistent, the version SHOULD be
            exchanged.
        code: A symbol in syntax defined by the system. The symbol may be a
            predefined code or an expression in a syntax defined by the coding
            system (e.g. post-coordination).
        display: A representation of the meaning of the code in the system,
            following the rules of the system.
        userSelected: Indicates that this coding was chosen by a user directly
            - i.e. off a pick list of available items (codes or displays).
    """

    __name__ = 'Coding'

    def __init__(self, dict_values=None):
        self.system = None
        # type: str

        self.version = None
        # type: str

        self.code = None
        # type: str

        self.display = None
        # type: str

        self.userSelected = None
        # type: bool

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
