import featuretools as ft
import pandas as pd

from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class ProlongedLengthOfStay (ProblemDefinition):
    """Defines the problem of length of stay, predicting whether
        a patient stayed in the hospital more or less than a week (Default).

        Attributes:
        target_label_column_name: The target label of the prediction problem.
        target_entity: Name of the entity containing the target label.
        cutoff_time_label: The cutoff time label of the prediction problem.
        cutoff_entity: Name of the entity containing the cutoff time label.
        prediction_type: The type of the machine learning prediction.
        """

    updated_es = None
    target_label_column_name = 'length'
    target_entity = 'Encounter'
    cutoff_time_label = 'start'
    cutoff_entity = 'Period'
    conn = 'period'
    prediction_type = 'classification'

    def __init__(self, t=7):
        self.threshold = t

    def unify_cutoff_times_hours(self, df):
        """ Unify records cutoff times based on shared time.

            Attributes:
            df: cutoff_entity dataframe.
            """

        df = df.sort_values(by=[self.cutoff_time_label])
        df = df.reset_index()

        for i in df.index:

            if i == 0:
                if df.get_value(i, 'checked') is not True:
                    df.set_value(i, 'ct', df.get_value(i, self.cutoff_time_label))
                    df.set_value(i, 'checked', True)

            elif df.get_value(i, 'checked') is not True:

                ct_val1 = df.get_value(i - 1, 'ct')
                end_val1 = df.get_value(i - 1, 'end')
                start_val2 = df.get_value(i, self.cutoff_time_label)
                df.get_value(i, 'end')

                if ct_val1 < start_val2 < end_val1:
                    df.set_value(i - 1, 'ct', start_val2)
                    df.set_value(i, 'ct', start_val2)
                    df.set_value(i, 'checked', True)

                else:
                    df.set_value(i, 'ct', df.get_value(i, self.cutoff_time_label))
                    df.set_value(i, 'checked', True)

                if i + 1 == len(df):
                    break
        return df

    def unify_cutoff_times_days(self, df):
        """ Unify records cutoff times based on shared days.

            Attributes:
            df: cutoff_entity dataframe.
            """
        frames = []
        for d in set(df['date']):
            sub_day = df[df['date'] == d]

            sub_duration_greater = sub_day[sub_day['duration'] > 0]
            sub_duration_less = sub_day[sub_day['duration'] <= 0]
            frames.append(sub_duration_less)
            sub_duration_greater = sub_duration_greater.sort_values(by=[self.cutoff_time_label])

            if len(sub_duration_greater) != 0:
                final_date = sub_duration_greater.iloc[-1][self.cutoff_time_label]

                for i in sub_duration_greater.index:
                    sub_duration_greater.set_value(i, 'ct', final_date)
                    sub_duration_greater.set_value(i, 'checked', True)

                frames.append(sub_duration_greater)

                for i in sub_duration_less.index:
                    sub_duration_less.set_value(i, 'ct', pd.NaT)
                    sub_duration_less.set_value(i, 'checked', False)

                frames.append(sub_duration_less)

            result = pd.concat(frames)
            result = result.drop_duplicates()
            result[self.cutoff_time_label] = pd.to_datetime(result.start)
            result = result.sort_values(by=[self.cutoff_time_label])
            result = result.reset_index()
        return result

    def unify_cutoff_time(self, es):
        """ Process records in the entity that contains cutoff times
            based on shared days and time.

            Attributes:
            es: fhir entityset.

            Returns:
            processed entity
            """

        df = es[self.cutoff_entity].df
        df['start'] = pd.to_datetime(df['start'])
        df['end'] = pd.to_datetime(df['end'])
        duration = (df['end'] - df[self.cutoff_time_label]).dt.days
        duration = duration.tolist()
        df['duration'] = duration
        df['date'] = df[self.cutoff_time_label].dt.date
        df['ct'] = ''
        df['checked'] = False
        result1 = self.unify_cutoff_times_days(df)

        result = self.unify_cutoff_times_hours(result1)
        if 'level_0' in result.columns:
            result = result.drop(columns=['level_0'])
        return result

    def generate_cutoff_times(self, es):
        """Generates cutoff times for the predection problem.

            Args:
            es: fhir entityset.

            Returns:
            entity_set, target_entity, and a dataframe of cutoff_times and target_labels.

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

                generated_cts = self.unify_cutoff_time(es)

                es = es.entity_from_dataframe(entity_id=self.cutoff_entity,
                                              dataframe=generated_cts,
                                              index='object_id')

                cutoff_times = es[self.cutoff_entity].df['ct'].to_frame()

                label = es[self.target_entity].df[self.conn].values
                instance_id = list(es[self.target_entity].df.index)
                cutoff_times = cutoff_times.reindex(index=label)
                cutoff_times = cutoff_times[cutoff_times.index.isin(label)]
                cutoff_times['instance_id'] = instance_id
                cutoff_times.columns = ['cutoff_time', 'instance_id']
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
                raise ValueError('Cutoff time label {} in table {} does not exist'
                                 .format(self.cutoff_time_label, self.target_entity))

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
                    'Can not generate target label {} in table {}' +
                    'beacuse start or end labels in table {} contain missing value.'
                    .format(label_name,
                            self.target_entity,
                            generate_from))

        else:
            raise ValueError(
                'Can not generate target label {} in table {}.'.format(
                    label_name,
                    self.target_entity))
