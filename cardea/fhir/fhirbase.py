import logging

import pandas as pd

logger = logging.getLogger('cardea.fhir')


class fhirbase(object):

    def set_attributes(self, dict_values):
        """Sets values to class attributes.

        Args:
            dict_values: A dictionary representation of inserted data.

        Returns:
            An object of the associate fhir class filled with data.
        """

        for key in dict_values.keys():
            if key not in self.__dict__.keys():
                logger.warning(
                    "Attribute {} in {} could not be loaded.".format(key, self.__name__))
            else:
                self.__dict__[key] = dict_values[key]

    def get_dataframe(self):
        """Returns dataframe from class attribute values.

        Returns:
            A dataframe representation of the class.
        """

        dataframe = {}
        for attr, value in self.__dict__.items():
            if value is not None and attr != 'resourceType':
                dataframe[attr] = value

        return pd.DataFrame(dataframe)

    def get_id(self):
        """Returns fhir class identifier.

        Returns:
            The name of identifier of the fhir class.

        Raises:
            LookupError: An error occurs if fhir class doesn't have an id.
        """

        if hasattr(self, 'identifier') and getattr(self, 'identifier') is not None:
            return 'identifier'
        elif hasattr(self, 'id') and getattr(self, 'id') is not None:
            return 'id'
        elif hasattr(self, 'object_id') and getattr(self, 'object_id') is not None:
            return 'object_id'
        else:
            raise LookupError('{} is missing an identifier'.format(self.__name__))

    def assert_type(self):
        """Checks class values follow set possible enumerations.

        Raises:
            ValueError: An error occurs if an attribute of the fhir class
                does not match its possible enumerations.
        """

    def get_relationships(self):
        """Returns class relationships.

        Returns:
            A list of the class's associated relationships.
        """
        return []

    def get_eligible_relationships(self):
        """Returns class relationships for attributes that are used.

        Returns:
            A list of the class's associated relationships after filtering out
            attributes that are not used.
        """

        all_relationships = self.get_relationships()
        eligible = [
            relation for relation in all_relationships if getattr(
                self, relation['child_variable']) is not None]
        return eligible
