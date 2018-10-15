import featuretools as ft
import pandas as pd

from cardea.problem_definition import ProblemDefinition


class LengthOfStay (ProblemDefinition):
    """Defines the problem of length of stay, finding how many days
        the patient will be in the hospital.

        Attributes:
        target_label: The target label of the prediction problem.
        target_entity: The entity name in which it contains the target label.
        cutoff_time_label: The cutoff time label of the prediction problem
        cutoff_entity: The entity name in which it contains the cutoff time label.
        prediction_type: The type of the machine learning prediction.
        """

    global target_label
    global target_entity
    global prediction_type
    global cutoff_time_label
    global cutoff_entity

    updated_es = None
    target_label = 'length'
    target_entity = 'Encounter'
    cutoff_time_label = 'start'
    cutoff_entity = 'Period'
    prediction_type = 'classification'

    def __init__(self, t=7):
        self.threshold = t

    def generate_cutoff_times(self, es):
        """Generates cutoff times for the predection problem.

            Args:
            es: fhir entityset.

            Returns:
            es, target_entity, target_label and a dataframe of cutoff_times

            Raises:
            ValueError: An error occurs if the cutoff variable does not exist.
            """
        try:
            if (self.check_target_label(es, target_entity, target_label)):
                if not (self.check_target_label_values(es, target_entity, target_label)):
                    try:
                        self.check_target_label(
                            es,
                            cutoff_entity,
                            cutoff_time_label)

                        cutoff_times = es[cutoff_entity].df[cutoff_time_label]
                        cutoff_times = cutoff_times.to_frame()
                        cutoff_times.index = es[cutoff_entity].df.index
                        cutoff_times = cutoff_times.rename(columns={cutoff_time_label:
                                                                    'cutoff_time'})
                        update_es = es[target_entity].df

                        # threshold
                        update_es['length'] = (update_es['length'] >= self.threshold)
                        update_es['length'] = update_es['length'].astype(int)

                        es = es.entity_from_dataframe(entity_id=target_entity,
                                                      dataframe=update_es,
                                                      index='identifier')

                        return es, target_entity, target_label, cutoff_times
                    except ValueError:
                        raise ValueError('Cutoff time label {} in table {} does not exist'
                                         .format(cutoff_time_label, target_entity))

        except ValueError:
            updated_es = self.generate_target_label(es)
            return self.generate_cutoff_times(updated_es)

    def generate_target_label(self, es):
        """Generates target labels in the case of having missing label in the entityset.

            Args:
            es: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name in which it contains the target label.

            Returns:
            Updated entityset with the generated label.

            Raises:
            ValueError: An error occurs if the target label cannot be generated.
            """
        generate_from = 'Period'
        start = 'start'
        end = 'end'

        try:
            if(self.check_target_label(
                es,
                generate_from,
                start) and
               self.check_target_label(
                    es,
                    generate_from,
                    end)):
                try:
                    self.check_target_label_values(
                        es,
                        generate_from,
                        start)
                    self.check_target_label_values(
                        es,
                        generate_from,
                        end)
                    es[generate_from].df[start] = pd.to_datetime(
                        es[generate_from]
                        .df[start])
                    es[generate_from].df[end] = pd.to_datetime(
                        es[generate_from].df[end])
                    duration = (es[generate_from].df[end] -
                                es[generate_from].df[start]).dt.days
                    duration = duration.tolist()
                    es['Encounter'].df['length'] = duration
                    updated_target_entity = es['Encounter'].df
                    duration_df = pd.DataFrame({'object_id': duration})

                    es = es.entity_from_dataframe(
                        entity_id='Duration',
                        dataframe=duration_df,
                        index='object_id')

                    es = es.entity_from_dataframe(entity_id='Encounter',
                                                  dataframe=updated_target_entity,
                                                  index='identifier')
                    new_relationship = ft.Relationship(es['Duration']['object_id'],
                                                       es[target_entity][target_label])
                    es = es.add_relationship(new_relationship)

                    return es

                except ValueError:
                    raise ValueError(
                        'Can not generate target label {} in table {}' +
                        'beacuse start or end labels in table {} contain missing value.'
                        .format(target_label,
                                target_entity,
                                generate_from))

        except ValueError:
            raise ValueError(
                'Can not generate target label {} in table {}.'.format(
                    target_label,
                    target_entity))
