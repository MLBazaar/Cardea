from cardea.data_loader import DataLoader


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
        """
        return DataLoader().check_column_existence(entity_set, target_entity, target_label)

    def check_for_missing_values_in_target_label(
            self, entity_set, target_entity, target_label_column_name):
        """Checks if there is a missing value in the target label.

        Args:
            entity_set: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name which contains the target label.

        Returns:
            False is the target label does not contain a missing value.

        """
        return DataLoader().check_for_missing_values(entity_set,
                                                     target_entity,
                                                     target_label_column_name)

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
