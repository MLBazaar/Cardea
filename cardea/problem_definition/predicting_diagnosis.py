import pandas as pd

from cardea.data_loader import DataLoader
from cardea.problem_definition import ProblemDefinition


class DiagnosisPrediction (ProblemDefinition):
    """Defines the problem of diagnosis Prediction, finding whether
        a patient will be diagnosed with a specifed diagnosis.

        Attributes:
        target_label_column_name: The target label of the prediction problem.
        target_entity: Name of the entity containing the target label.
        cutoff_time_label: The cutoff time label of the prediction problem.
        cutoff_entity: Name of the entity containing the cutoff time label.
        prediction_type: The type of the machine learning prediction.

        Assumptions:
        the patient visit is considered a readmission if he visits
            the hospital again within 30 days.

        the readmission diagnosis does not have to be the same as the initial visit diagnosis,
            (he could be diagnosed of something that is a complication of the initial diagnosis).

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
        df[str(self.cutoff_time_label)] = pd.to_datetime(df[self.cutoff_time_label])
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

        es = self.generate_target_label(es)

        if DataLoader().check_column_existence(
            es,
            self.cutoff_entity,
                self.cutoff_time_label):  # check the existance of the cutoff label

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
            cutoff_times['label'] = list(es[self.target_entity].df[self.target_label_column_name])
            cutoff_times['label'] = cutoff_times['label'] == self.diagnosis

            return(es, self.target_entity, cutoff_times)
        else:
            raise ValueError('Cutoff time label {} in table {} does not exist'
                             .format(self.cutoff_time_label, self.target_entity))

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
