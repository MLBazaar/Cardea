import pandas as pd

from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition

DEFAULT_CAUSES = ['X60', 'X84', 'Y87.0', 'X85', 'Y09', 'Y87.1',
                  'V02', 'V04', 'V09.0', 'V09.2', 'V12', 'V14']


class MortalityPrediction(ProblemDefinition):
    """Defines the problem of Diagnosis Prediction.

    It finds whether a patient will be diagnosed with a specifed diagnosis.

    Note:
        The patient visit is considered a readmission if he visits
        the hospital again within 30 days.

        The readmission diagnosis does not have to be the same as the initial visit diagnosis,
        (he could be diagnosed of something that is a complication of the initial diagnosis).
    """
    __name__ = 'mortality'

    def __init__(self, causes_of_death=DEFAULT_CAUSES):
        self.causes_of_death = causes_of_death

        super().__init__(
            'diagnosis',        # target_label_column_name
            'Encounter',        # target_entity
            'start',            # cutoff_time_label
            'Period',           # cutoff_entity
            'classification',   # prediction_type
            conn='period'
        )

    def generate_cutoff_times(self, es):
        es = self.generate_target_label(es)

        entity_set, target_entity, cutoff_times = super().generate_cutoff_times(es)

        # post-processing step
        for (idx, row) in cutoff_times.iterrows():
            new_val = row.loc['label'] in self.causes_of_death
            cutoff_times.at[idx, 'label'] = new_val

        return (entity_set, target_entity, cutoff_times)

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
                    'Can not generate target label {} in table {}' +
                    ' beacuse end label in table {} contains missing value.'
                    .format(self.target_label_column_name,
                            self. target_entity,
                            generate_from))

        else:
            raise ValueError(
                'Can not generate target label {} in table {}.'.format(
                    self.target_label_column_name,
                    self.target_entity))
