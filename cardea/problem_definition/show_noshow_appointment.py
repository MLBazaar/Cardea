
from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class MissedAppointmentProblemDefinition(ProblemDefinition):
    """Defines the problem of Missed Appointments.

    It preditcs whether the patient showed to the appointment or not.
    """
    __name__ = 'mapp'

    def __init__(self):
        super().__init__(
            'status',           # target_label_column_name
            'Appointment',      # target_entity
            'created',          # cutoff_time_label
            'Appointment',      # cutoff_entity
            'classification'    # prediction_type
        )

    def generate_cutoff_times(self, entity_set):
        """Generates cutoff times for the predection problem.

        Args:
            entity_set: fhir entityset.

        Returns:
            entity_set, target_entity and a dataframe of cutoff_times and target_labels

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
                cutoff_times.columns = ['cutoff_time', 'instance_id']
                cutoff_times['label'] = list(
                    entity_set[self.target_entity].df[self.target_label_column_name])
                entity_set[self.target_entity].delete_variable(self.target_label_column_name)
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
