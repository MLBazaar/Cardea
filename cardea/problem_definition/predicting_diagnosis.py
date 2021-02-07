import pandas as pd

from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class DiagnosisPrediction (ProblemDefinition):
    """Defines the problem of diagnosis Prediction.

    Finding whether a patient will be diagnosed with a specifed diagnosis.

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
    __name__ = 'diagnosis'

    updated_es = None
    target_label_column_name = 'diagnosis'
    target_entity = 'Encounter'
    cutoff_time_label = 'start'
    cutoff_entity = 'Period'
    prediction_type = 'classification'
    conn = 'period'

    def __init__(self, d):
        self.diagnosis = d

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

        es = self.generate_target_label(es)

        if DataLoader().check_column_existence(
            es,
            self.cutoff_entity,
                self.cutoff_time_label):  # check the existance of the cutoff label

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
            cutoff_times['label'] = list(es[self.target_entity].df[self.target_label_column_name])
            cutoff_times['label'] = cutoff_times['label'] == self.diagnosis

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
        if (self.check_target_label(
            es,
            self.target_entity,
                self.target_label_column_name)):

            if not DataLoader().check_for_missing_values(es,
                                                         self.target_entity,
                                                         self.target_label_column_name):
                entity_set_df = es[self.target_entity].df

                merging_coding = pd.merge(es['Coding'].df, es['CodeableConcept'].df,
                                          left_on='object_id', right_on='coding', how='left')
                merging_condtion = pd.merge(merging_coding, es['Condition'].df,
                                            left_on='object_id_y', right_on='code', how='left')
                merging_diagnosis = pd.merge(
                    merging_condtion,
                    es['Encounter_Diagnosis'].df,
                    left_on='identifier',
                    right_on='condition', how='left')

                merging_encouter = pd.merge(merging_diagnosis, es[self.target_entity].df,
                                            left_on='subject', right_on='identifier', how='left')
                merging_encouter['target'] = merging_encouter['code_x']

                set(es[self.target_entity].df.identifier)

                entity_set_df[self.target_label_column_name] = list(merging_encouter['target'])

                es = es.entity_from_dataframe(entity_id=self.target_entity,
                                              dataframe=entity_set_df,
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
