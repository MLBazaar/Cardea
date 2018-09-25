import numpy as np
from numpy import nan


class ProblemDefinition:
    """A class that defines the prediction problem
        by generating the target label if it does not exist and specify cutoff times."""

    def check_target_label(self, entity_set, target_entity, target_label):
        """Checks if target label exists in the entity set.

        Args:
            entity_set: FHIR entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name, in which it contains the target label.

        Returns:
            True if the target label exists, false otherwise.
        """

        columns_list = []
        does_exist = True

        for variable in (entity_set.__getitem__(target_entity).variables):
            columns_list.append(variable.name)

        does_exist = target_label in columns_list

        return does_exist

    def check_target_label_values(self, entity_set, target_entity, target_label):
        """Checks if there is a missing value in the target label.

        Args:
            entity_set: FHIR entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name in which it contains the target label.

        Returns:
            True if there is a missing value, false otherwise.
        Raises:
            ValueError: An error occurs if the target label does not exist.
        """

        if self.check_target_label(self, entity_set, target_entity, target_label):

            nat = np.datetime64('NaT')
            missings = [
                nat,
                nan,
                'null',
                'nan',
                'NAN',
                'Nan',
                'NaN',
                'undefined',
                'unknown']
            contains_nan = False

            target_label_values = entity_set.__getitem__(target_entity).df[target_label]

            for missing_value in missings:
                if missing_value in list(target_label_values):
                    contains_nan = True

            return contains_nan
        else:
            raise ValueError('Target value does not exist')

    def generate_target_label(self, entity_set, target_entity, target_label):
        """Generates target labels in the case of having missing label in the entityset.

        Args:
            entity_set: FHIR entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name in which it contains the target label.

        Returns:
            Target entity with the generated label.
        """

    def generate_cutoff_times(self, entity_set):
        """Generates cutoff times for the predection problem.

        Args:
            entity_set: FHIR entityset.

        Returns:
            DataFrame with entity id, cutoff times and target labels.

        Raises:
            ValueError: An error occurs if the target label contains a missing value.
            ValueError: An error occurs if the target label does not exist.
        """
