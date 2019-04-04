import pandas as pd

from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class Sepsis (ProblemDefinition):
    """Defines the problem of Sepsis Prediction

        Predicting whether a patient will have a sepsis or not.

        Note:
        The patient visit is considered a readmission if he/she visits
        the hospital again within 30 days.

        The readmission diagnosis does not have to be the same as the initial visit diagnosis,
        (The patient could be diagnosed of something that is a complication
        of the initial diagnosis).

        Attributes:
        target_label_column_name: The target label of the prediction problem.
        target_entity: Name of the entity containing the target label.
        cutoff_time_label: The cutoff time label of the prediction problem.
        cutoff_entity: Name of the entity containing the cutoff time label.
        prediction_type: The type of the machine learning prediction.
        """
    __name__ = 'sepsis'

    updated_es = None
    target_label_column_name = 'SepsisLabel'
    target_entity = 'Visits'
    cutoff_time_label = 'ICULOS'
    cutoff_entity = 'Visits'
    prediction_type = 'classification'

    def generate_cutoff_times(self, es):
        """Generates cutoff times for the predection problem.

            Args:
            es: fhir entityset.

            Returns:
            entity_set, target_entity, and a dataframe of cutoff_times and target_labels.

            Raises:
            ValueError: An error occurs if the cutoff variable does not exist.
            """

        if DataLoader().check_column_existence(
                es,
                self.cutoff_entity,
                self.cutoff_time_label):  # check the existance of the cutoff label

            cutoff_times = pd.DataFrame()
            cutoff_times['instance_id'] = es[self.target_entity].df['ID']
            cutoff_times['cutoff_time'] = es[self.cutoff_entity].df[self.cutoff_time_label]
            cutoff_times['label'] = es[self.target_entity].df[self.target_label_column_name]
            return(es, self.target_entity, cutoff_times)
        else:
            raise ValueError('Cutoff time label {} in table {} does not exist'
                             .format(self.cutoff_time_label, self.target_entity))
