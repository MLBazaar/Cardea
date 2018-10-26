
from cardea.problem_definition import ProblemDefinition


class MissedAppointmentProblemDefinition (ProblemDefinition):
    """Defines the problem of missed appointments,
        whether the patient showed to the appointment or not.

    Attributes:
        target_label: The target label of the prediction problem.
        target_entity: The entity name which contains the target label.
        cutoff_time_label: The cutoff time label of the prediction problem
        cutoff_entity: The entity name in which it contains the cutoff time label.
        prediction_type: The type of the machine learning prediction.
    """

    target_label = 'status'
    target_entity = 'Appointment'
    prediction_type = 'classification'
    cutoff_time_label = 'created'
    cutoff_entity = target_entity

    def generate_cutoff_times(self, entity_set):
        """Generates cutoff times for the predection problem.

        Args:
            entity_set: fhir entityset.

        Returns:
            entity_set, target_entity, series of target_labels and a dataframe of cutoff_times

        Raises:
            ValueError: An error occurs if the cutoff variable does not exist.
        """

        if (self.check_target_label(
            entity_set,
            self.target_entity,
            self.target_label)) and not (self.check_target_label_values(entity_set,
                                                                        self.target_entity,
                                                                        self.target_label)):

            if self.check_target_label(entity_set,
                                       self.target_entity,
                                       self.cutoff_time_label):

                instance_id = list(entity_set[self.target_entity].df.index)
                cutoff_times = entity_set[self.cutoff_entity].df[self.cutoff_time_label].to_frame()
                cutoff_times['instance_id'] = instance_id
                cutoff_times.columns = ['cutoff_time', 'instance_id']
                cutoff_times['label'] = list(entity_set[self.target_entity].df[self.target_label])
                return (entity_set, self.target_entity, cutoff_times)
            else:
                raise ValueError(
                    'Cutoff time label {} in table {} does not exist'.format(
                        'created', self.target_entity))
        else:
            raise ValueError(
                'Can not generate target label {} in table {}.'.format(
                    self.target_label,
                    self.target_entity))
