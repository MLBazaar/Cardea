import numpy as np
import pandas as pd
from numpy import nan


class ProblemDefinition:
    """A class that defines the prediction problem
        by specifying cutoff times and generating the target label if it does not exist"""

    def check_target_label(self, entity_set, target_entity, target_label):
        """Checks if target label exists in the entity set.

        Args:
            entity_set: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name which contains the target label.

        Returns:
            True if the target label exists.
        Raises:
            ValueError: An error occurs if the target label does not exist.

        """
        columns_list = []
        does_exist = True

        for variable in entity_set.__getitem__(target_entity).variables:
            columns_list.append(variable.name)

        does_exist = target_label in columns_list
        if does_exist:
            return does_exist
        else:
            return False

    def check_target_label_values(self, entity_set, target_entity, target_label):
        """Checks if there is a missing value in the target label.

        Args:
            entity_set: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name which contains the target label.

        Returns:
            False is the target label does not contain a missing value.
        Raises:
            ValueError: An error occurs if the target label contains a missing value.
        """

        if self.check_target_label(entity_set, target_entity, target_label):

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
                None,
                'unknown']
            contains_nan = False

            target_label_values = entity_set.__getitem__(target_entity).df[target_label]

            for missing_value in missings:
                if missing_value in list(target_label_values):
                    contains_nan = True

            for missing_value in missings:
                for target_value in (target_label_values):
                    if pd.isnull(target_value):
                        contains_nan = True

            return contains_nan
        else:
            return False

    def generate_target_label(self, entity_set, target_entity, target_label):
        """Generates target labels if the entityset is missing labels.

        Args:
            entity_set: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name which contains the target label.

        Returns:
            Target entity with the generated label.
        """

    def generate_cutoff_times(self, entity_set):
        """Generates cutoff times for the predection problem.

        Args:
            entity_set: fhir entityset.

        Returns:
            entity_set, target_entity, series of target_labels and a dataframe of cutoff_times.

        Raises:
            ValueError: An error occurs if the cutoff variable does not exist.
            """
