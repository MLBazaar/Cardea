from .fhirbase import fhirbase


class ParameterDefinition(fhirbase):
    """
    The parameters to the module. This collection specifies both the input
    and output parameters. Input parameters are provided by the caller as
    part of the $evaluate operation. Output parameters are included in the
    GuidanceResponse.

    Args:
        name: The name of the parameter used to allow access to the value of
            the parameter in evaluation contexts.
        use: Whether the parameter is input or output for the module.
        min: The minimum number of times this parameter SHALL appear in the
            request or response.
        max: The maximum number of times this element is permitted to appear
            in the request or response.
        documentation: A brief discussion of what the parameter is for and how
            it is used by the module.
        type: The type of the parameter.
        profile: If specified, this indicates a profile that the input data
            must conform to, or that the output data will conform to.
    """

    __name__ = 'ParameterDefinition'

    def __init__(self, dict_values=None):
        self.name = None
        # type: str

        self.use = None
        # type: str

        self.min = None
        # type: int

        self.max = None
        # type: str

        self.documentation = None
        # type: str

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
             'child_entity': 'ParameterDefinition',
             'child_variable': 'profile'},
        ]
