
from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class MissedAppointment(ProblemDefinition):
    """Defines the problem of missed appointment

    Predict whether the patient will show to the appointment or not.

    Args:
        target_label_column_name (str):
            The target label of the prediction problem.
        target_entity (str):
            Name of the entity containing the target label.
        cutoff_time_label (str):
            The cutoff time label of the prediction problem.
        cutoff_entity (str):
            Name of the entity containing the cutoff time label.
        prediction_type (str):
            The type of the machine learning prediction.
    """
    __name__ = 'mapp'

    target_label_column_name = 'status'
    target_entity = 'Appointment'
    prediction_type = 'classification'
    cutoff_time_label = 'created'
    cutoff_entity = target_entity

    def generate_cutoff_times(self, entity_set):
        """Generates cutoff times for the prediction problem.

        Args:
            es (featuretools.EntitySet):
                An EntitySet with the loaded data.

        Returns:
            featuretools.EntitySet, str, pandas.DataFrame:
                * An updated EntitySet if a new column is generated.
                * A string indicating the selected target entity.
                * A dataframe of cutoff times and their target labels.

        Raises:
            ValueError: An error occurs if the cutoff variable does not exist.
        """

        if (self.check_target_label(
            entity_set,
            self.target_entity,
            self.target_label_column_name)) and\
            not (self.check_for_missing_values_in_target_label(entity_set,
                                                               self.target_entity,
                                                               self.target_label_column_name)):

            if DataLoader().check_column_existence(entity_set,
                                                   self.target_entity,
                                                   self.cutoff_time_label):

                instance_id = list(entity_set[self.target_entity].df.index)
                cutoff_times = entity_set[self.cutoff_entity].df[self.cutoff_time_label].to_frame()
                cutoff_times['instance_id'] = instance_id
                cutoff_times.columns = ['time', 'instance_id']
                cutoff_times['label'] = list(
                    entity_set[self.target_entity].df[self.target_label_column_name])
                entity_set[self.target_entity].delete_variables([self.target_label_column_name])
                return (entity_set, self.target_entity, cutoff_times)
            else:
                raise ValueError(
                    'Cutoff time label {} in table {} does not exist'.format(
                        'created', self.target_entity))
        else:
            raise ValueError(
                'Can not generate target label {} in table {}.'.format(
                    self.target_label_column_name,
                    self.target_entity))
