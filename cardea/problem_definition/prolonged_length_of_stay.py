import featuretools as ft
import pandas as pd

from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class ProlongedLengthOfStay (ProblemDefinition):
    """Defines the problem of length of stay

    Predicting whether a patient stayed in the hospital more or less than
    a week (by default).

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
    __name__ = 'plos'

    updated_es = None
    target_label_column_name = 'length'
    target_entity = 'Encounter'
    cutoff_time_label = 'start'
    cutoff_entity = 'Period'
    conn = 'period'
    prediction_type = 'classification'

    def __init__(self, t=7):
        self.threshold = t

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

        if (self.check_target_label(es,
                                    self.target_entity,
                                    self.target_label_column_name) and not
            self.check_for_missing_values_in_target_label(es,
                                                          self.target_entity,
                                                          self.target_label_column_name)):
            if DataLoader().check_column_existence(
                    es,
                    self.cutoff_entity,
                    self.cutoff_time_label):

                generated_cts = self.unify_cutoff_time_admission_time(
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
                update_es = es[self.target_entity].df

                # threshold
                update_es['length'] = (update_es['length'] >= self.threshold)
                update_es['length'] = update_es['length'].astype(int)

                es = es.entity_from_dataframe(entity_id=self.target_entity,
                                              dataframe=update_es,
                                              index='identifier')

                cutoff_times['label'] = list(
                    es[self.target_entity].df[self.target_label_column_name])
                return(es, self.target_entity, cutoff_times)
            else:
                raise ValueError('Cutoff time label {} in table {} does not exist'.format(
                    self.cutoff_time_label, self.target_entity))

        else:
            updated_es = self.generate_target_label(es)
            return self.generate_cutoff_times(updated_es)

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
        start = self.cutoff_time_label
        end = 'end'
        label_name = self.target_label_column_name
        if (DataLoader().check_column_existence(
            es,
            generate_from,
            start) and DataLoader().check_column_existence(es,
                                                           generate_from,
                                                           end)):

            if (not DataLoader().check_for_missing_values(
                    es,
                    generate_from,
                    start) and not DataLoader().check_for_missing_values(es,
                                                                         generate_from,
                                                                         end)):

                es[generate_from].df[start] = pd.to_datetime(
                    es[generate_from]
                    .df[start])
                es[generate_from].df[end] = pd.to_datetime(
                    es[generate_from].df[end])
                duration = (es[generate_from].df[end] -
                            es[generate_from].df[start]).dt.days
                duration = duration.tolist()
                es[self.target_entity].df[label_name] = duration
                updated_target_entity = es[self.target_entity].df
                duration_df = pd.DataFrame({'object_id': duration})

                es = es.entity_from_dataframe(
                    entity_id='Duration',
                    dataframe=duration_df,
                    index='object_id')

                es = es.entity_from_dataframe(entity_id=self.target_entity,
                                              dataframe=updated_target_entity,
                                              index='identifier')
                new_relationship = ft.Relationship(es['Duration']['object_id'],
                                                   es[self.target_entity][label_name])
                es = es.add_relationship(new_relationship)

                return es

            else:
                raise ValueError(
                    'Can not generate target label {} in table {} beacuse start or end labels in \
                     table {} contain missing value.'.format(
                        label_name, self.target_entity, generate_from))

        else:
            raise ValueError(
                'Can not generate target label {} in table {}.'.format(
                    label_name,
                    self.target_entity))
