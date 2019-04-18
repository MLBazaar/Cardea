import featuretools as ft
import pandas as pd

from cardea.data_loader import DataLoader as DL
from cardea.problem_definition import ProblemDefinition


class LengthOfStay(ProblemDefinition):
    """Defines the problem of Length of Stay.

    It predicts how many days the patient will be in the hospital.
    """

    __name__ = 'los'

    def __init__(self):
        super().__init__(
            'length',           # target_label_column_name
            'Encounter',        # target_entity
            'start',            # cutoff_time_label
            'Period',           # cutoff_entity
            'regression',       # prediction_type
            conn='period'
        )

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

        if (DL().check_column_existence(es,
                                        generate_from,
                                        start) and DL().check_column_existence(es,
                                                                               generate_from,
                                                                               end)):
            if (not DL().check_for_missing_values(es,
                                                  generate_from,
                                                  start) and not
                (DL().check_for_missing_values(es,
                                               generate_from,
                                               end))):

                es[generate_from].df[start] = pd.to_datetime(
                    es[generate_from].df[start])
                es[generate_from].df[end] = pd.to_datetime(
                    es[generate_from].df[end])
                duration = (es[generate_from].df[end] - es[generate_from].df[start]).dt.days
                duration = duration.tolist()
                es[self.target_entity].df[label_name] = duration
                updated_target_entity = es[self.target_entity].df
                duration_df = pd.DataFrame({'object_id': duration})

                es = es.entity_from_dataframe(entity_id='Duration',
                                              dataframe=duration_df,
                                              index='object_id')

                es = es.entity_from_dataframe(entity_id=self.target_entity,
                                              dataframe=updated_target_entity, index='identifier')
                new_relationship = ft.Relationship(es['Duration']['object_id'],
                                                   es[self.target_entity][label_name])
                es = es.add_relationship(new_relationship)

                return es

            else:
                raise ValueError('Can not generate target label {} in table {} \
                                beacuse start or end labels in table {} contain \
                                missing value.'.format(label_name,
                                                       self.target_entity,
                                                       generate_from))

        else:
            raise ValueError('Can not generate target label {} in \
                             table {}.'.format(label_name,
                                               self.target_entity))
