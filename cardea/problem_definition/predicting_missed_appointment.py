
from cardea.problem_definition import ProblemDefinition


class PredictingMissedAppointmet (ProblemDefinition):
    """Defines the problem of missed appointments,
        whether the patient showed to the appointment or not.

    Attributes:
        target_label: The target label of the prediction problem.
        target_entity: The entity name in which it contains the target label.
    """

    global target_label
    global target_entity

    target_label = 'status'
    target_entity = 'Appointment'

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

        if super(PredictingMissedAppointmet, self).check_target_label(
                ProblemDefinition,
                entity_set,
                target_entity,
                target_label):
            if super(PredictingMissedAppointmet, self).check_target_label_values(
                    ProblemDefinition, entity_set, target_entity, target_label):
                raise ValueError('Please remove missing values in the target label')

            else:
                cutoff_times = entity_set[target_entity].df[[
                    'identifier', 'created', target_label]].sort_values(by='created')
                cutoff_times = cutoff_times.rename(
                    columns={'created': 'cutoff_time', target_label: 'label'})
                return cutoff_times

        else:
            raise ValueError('Target label does not exist')
