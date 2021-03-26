import pandas as pd

from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class Readmission (ProblemDefinition):
    """Defines the problem of readmission.

    Predicting whether a patient will revisit the hospital within certain period of time.

    Note:
        The patient visit is considered a readmission if he/she visits
        the hospital again within 30 days.

        The readmission diagnosis does not have to be the same as the initial visit diagnosis,
        (The patient could be diagnosed of something that is a complication
        of the initial diagnosis).

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
    __name__ = 'readmission'

    updated_es = None
    target_label_column_name = 'readmitted'
    target_entity = 'Encounter'
    cutoff_time_label = 'end'
    cutoff_entity = 'Period'
    prediction_type = 'classification'
    conn = 'period'

    def __init__(self, t=30):
        self.readmission_threshold = t

    def generate_cutoff_times(self, es):
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

        self.generate_target_label(es)

        if DataLoader().check_column_existence(
                es,
                self.cutoff_entity,
                self.cutoff_time_label):  # check the existance of the cutoff label

            generated_cts = self.unify_cutoff_time_discharge_time(
                es, self.cutoff_entity, self.cutoff_time_label)

            es = es.entity_from_dataframe(entity_id=self.cutoff_entity,
                                          dataframe=generated_cts,
                                          index='object_id')
            cutoff_times = es[self.cutoff_entity].df['ct'].to_frame()

            label = es[self.target_entity].df[self.conn].values
            instance_id = list(es[self.target_entity].df.index)
            cutoff_times = cutoff_times.reindex(index=label)

            cutoff_times = cutoff_times[cutoff_times.index.isin(label)]

            cutoff_times['instance_id'] = instance_id
            cutoff_times.columns = ['time', 'instance_id']
            cutoff_times['label'] = list(es[self.target_entity].df[self.target_label_column_name])
            return(es, self.target_entity, cutoff_times)
        else:
            raise ValueError('Cutoff time label {} in table {} does not exist'.format(
                self.cutoff_time_label, self.target_entity))

    def generate_target_label(self, es):
        """Generates target labels in the case of having missing label in the entityset.

        Args:
            es: fhir entityset.

        Returns:
            Updated entityset with the generated label.

        Raises:
            ValueError: An error occurs if the target label cannot be generated.
        """
        generate_from = 'Period'
        end = 'end'
        if (DataLoader().check_column_existence(
            es,
            generate_from,
            end)) and (DataLoader().check_column_existence(es,
                                                           self.target_entity,
                                                           'period')):

            if not DataLoader().check_for_missing_values(
                    es,
                    generate_from, end):

                entity_set_df = es[self.target_entity].df
                generated_df = es[generate_from].df
                merged_df = pd.merge(entity_set_df, generated_df, how='left',
                                     left_on='period', right_on='object_id')

                generated_target_label = []
                encounter_identifier = []

                for patient in set(merged_df['subject']):
                    patient_visits = merged_df[merged_df['subject'] == patient]
                    inital_date = patient_visits[end].iloc[0]

                    encounter_identifier.append(patient_visits['identifier'].iloc[0])
                    generated_target_label.append(False)  # first visit

                    if len(patient_visits) != 1:
                        for visit_date, encounter_id in zip(patient_visits[end][1:],
                                                            patient_visits['identifier'][1:]):

                            visit_range = visit_date - inital_date
                            inital_date = visit_date

                            if visit_range.days <= self.readmission_threshold:
                                generated_target_label.append(True)
                                encounter_identifier.append(encounter_id)

                            else:
                                generated_target_label.append(False)
                                encounter_identifier.append(encounter_id)

                generated_labels = pd.DataFrame(
                    {self.target_label_column_name: generated_target_label,
                     'identifier': encounter_identifier})
                updated_target_entity = pd.merge(entity_set_df,
                                                 generated_labels,
                                                 on='identifier')

                es = es.entity_from_dataframe(entity_id=self.target_entity,
                                              dataframe=updated_target_entity,
                                              index='identifier')

                return es

            else:
                raise ValueError(
                    'Can not generate target label {} in table {} beacuse end label in \
                     table {} contains missing value.'.format(
                        self.target_label_column_name, self. target_entity, generate_from))

        else:
            raise ValueError(
                'Can not generate target label {} in table {}.'.format(
                    self.target_label_column_name,
                    self.target_entity))
