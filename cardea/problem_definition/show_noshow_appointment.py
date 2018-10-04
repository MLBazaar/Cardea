
from cardea.problem_definition import ProblemDefinition


class MissedAppointmentProblemDefinition (ProblemDefinition):
    """Defines the problem of missed appointments,
        whether the patient showed to the appointment or not.

    Attributes:
        target_label: The target label of the prediction problem.
        target_entity: The entity name which contains the target label.
        prediction_type: The type of the machine learning prediction.
    """

    global target_label
    global target_entity

    target_label = 'status'
    target_entity = 'Appointment'
    prediction_type = 'classification'

    def generate_cutoff_times(self, entity_set):
        """Generates cutoff times for the predection problem.

        Args:
            entity_set: FHIR entityset.

        Returns:
            entity_set, target_entity, target_label and a dataframe of cutoff_times

        Raises:
            ValueError: An error occurs if the cutoff variable does not exist.
        """

        if (self.check_target_label(
                ProblemDefinition,
                entity_set,
                target_entity,
                target_label)) and not (self.check_target_label_values(
                    ProblemDefinition,
                    entity_set,
                    target_entity,
                    target_label)):

            if self.check_target_label(
                    ProblemDefinition,
                    entity_set,
                    target_entity,
                    'created'):  # check the existance of the cutoff time in the entity.

                cutoff_times = entity_set[target_entity].df['created']
                cutoff_times = cutoff_times.to_frame()
                cutoff_times.index = entity_set[target_entity].df.index
                cutoff_times = cutoff_times.rename(columns={'created': 'cutoff_time'})
                return entity_set, target_entity, target_label, cutoff_times
            else:
                raise ValueError(
                    'Cutoff time {} in {} does not exist'.format(
                        'created', target_entity))
