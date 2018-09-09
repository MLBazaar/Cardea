from .fhirbase import fhirbase


class ParameterDefinition(fhirbase):
    """
    The parameters to the module. This collection specifies both the input
    and output parameters. Input parameters are provided by the caller as
    part of the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """

    __name__ = 'ParameterDefinition'

    def __init__(self, dict_values=None):
        self.name = None
        """
        The name of the parameter used to allow access to the value of the
        parameter in evaluation contexts.

        type: string
        """

        self.use = None
        """
        Whether the parameter is input or output for the module.

        type: string
        """

        self.min = None
        """
        The minimum number of times this parameter SHALL appear in the request
        or response.

        type: int
        """

        self.max = None
        """
        The maximum number of times this element is permitted to appear in the
        request or response.

        type: string
        """

        self.documentation = None
        """
        A brief discussion of what the parameter is for and how it is used by
        the module.

        type: string
        """

        self.type = None
        """
        The type of the parameter.

        type: string
        """

        self.profile = None
        """
        If specified, this indicates a profile that the input data must
        conform to, or that the output data will conform to.

        reference to Reference: identifier
        """

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
