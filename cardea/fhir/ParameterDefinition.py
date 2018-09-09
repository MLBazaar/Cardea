from .fhirbase import fhirbase


class ParameterDefinition(fhirbase):
    """The parameters to the module. This collection specifies both the input
    and output parameters. Input parameters are provided by the caller as
    part of the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """

    __name__ = 'ParameterDefinition'

    def __init__(self, dict_values=None):
        # the name of the parameter used to allow access to the value of the
        # parameter in evaluation contexts.
        self.name = None
        # type = string

        # whether the parameter is input or output for the module.
        self.use = None
        # type = string

        # the minimum number of times this parameter shall appear in the request
        # or response.
        self.min = None
        # type = int

        # the maximum number of times this element is permitted to appear in the
        # request or response.
        self.max = None
        # type = string

        # a brief discussion of what the parameter is for and how it is used by
        # the module.
        self.documentation = None
        # type = string

        # the type of the parameter.
        self.type = None
        # type = string

        # if specified, this indicates a profile that the input data must conform
        # to, or that the output data will conform to.
        self.profile = None
        # reference to Reference: identifier

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'ParameterDefinition',
             'child_variable': 'profile'},
        ]
