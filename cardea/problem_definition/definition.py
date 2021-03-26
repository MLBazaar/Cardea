import pandas as pd

from cardea.data_loader import DataLoader


class ProblemDefinition:
    """A class that defines the prediction problem
    by specifying cutoff times and generating the target label if it does not exist.
    """

    def check_target_label(self, entity_set, target_entity, target_label):
        """Checks if target label exists in the entity set.

        Args:
            entity_set: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name which contains the target label.

        Returns:
            True if the target label exists.
        """
        return DataLoader().check_column_existence(entity_set, target_entity, target_label)

    def check_for_missing_values_in_target_label(
            self, entity_set, target_entity, target_label_column_name):
        """Checks if there is a missing value in the target label.

        Args:
            entity_set: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name which contains the target label.

        Returns:
            False is the target label does not contain a missing value.
        """
        return DataLoader().check_for_missing_values(entity_set,
                                                     target_entity,
                                                     target_label_column_name)

    def generate_target_label(self, entity_set, target_entity, target_label):
        """Generates target labels if the entityset is missing labels.

        Args:
            entity_set: fhir entityset.
            target_label: The target label of the prediction problem.
            target_entity: The entity name which contains the target label.

        Returns:
            Target entity with the generated label.
        """

    def generate_cutoff_times(self, entity_set):
        """Generates cutoff times for the predection problem.

        Args:
            entity_set: fhir entityset.

        Returns:
            entity_set, target_entity, series of target_labels and a dataframe of cutoff_times.

        Raises:
            ValueError: An error occurs if the cutoff variable does not exist.
        """

    def unify_cutoff_times_hours_admission_time(self, df, cutoff_time_label):
        """Unify records cutoff times based on shared time.

        Args:
            df: cutoff_entity dataframe.
        """
        df = df.sort_values(by=[cutoff_time_label])
        df = df.reset_index()

        for i in df.index:

            if i == 0:

                if df.at[i, 'checked'] is not True:
                    df.at[i, 'ct'] = df.at[i, cutoff_time_label]
                    df.at[i, 'checked'] = True

            elif df.at[i, 'checked'] is not True:

                ct_val1 = df.at[i - 1, 'ct']
                end_val1 = df.at[i - 1, 'end']
                start_val2 = df.at[i, cutoff_time_label]
                df.at[i, 'end']

                if ct_val1 < start_val2 < end_val1:
                    df.at[i - 1, 'ct'] = start_val2
                    df.at[i, 'ct'] = start_val2
                    df.at[i, 'checked'] = True

                else:
                    df.at[i, 'ct'] = df.at[i, cutoff_time_label]
                    df.at[i, 'checked'] = True

                if i + 1 == len(df):
                    break
        return df

    def unify_cutoff_times_days_admission_time(self, df, cutoff_time_label):
        """Unify records cutoff times based on shared days.

        Args:
            df: cutoff_entity dataframe.
        """

        frames = []
        for d in set(df['date']):
            sub_day = df[df['date'] == d]

            sub_duration_greater = sub_day[sub_day['duration'] > 0]
            sub_duration_less = sub_day[sub_day['duration'] <= 0]
            frames.append(sub_duration_less)
            sub_duration_greater = sub_duration_greater.sort_values(by=[cutoff_time_label])
            if len(sub_duration_greater) != 0:
                final_date = sub_duration_greater.iloc[-1][cutoff_time_label]

                for i in sub_duration_greater.index:
                    sub_duration_greater.at[i, 'ct'] = final_date
                    sub_duration_greater.at[i, 'checked'] = True

                frames.append(sub_duration_greater)

                for i in sub_duration_less.index:
                    sub_duration_less.at[i, 'ct'] = pd.NaT
                    sub_duration_less.at[i, 'checked'] = False

                    frames.append(sub_duration_less)

        result = pd.concat(frames)
        result = result.drop_duplicates()
        result[cutoff_time_label] = pd.to_datetime(result.start)
        result = result.sort_values(by=[cutoff_time_label])
        result = result.reset_index()
        return result

    def unify_cutoff_time_admission_time(self, es, cutoff_entity, cutoff_time_label):
        """Process records in the entity that contains cutoff times
        based on shared days and time.

        Args:
            es: fhir entityset.

        Returns:
            processed entity
        """

        df = es[cutoff_entity].df
        df[cutoff_time_label] = pd.to_datetime(df[cutoff_time_label])
        df['end'] = pd.to_datetime(df['end'])
        duration = (df['end'] - df[cutoff_time_label]).dt.days
        duration = duration.tolist()
        df['duration'] = duration
        df['date'] = df[cutoff_time_label].dt.date
        df['ct'] = ''
        df['checked'] = False
        result1 = self.unify_cutoff_times_days_admission_time(df, cutoff_time_label)
        result = self.unify_cutoff_times_hours_admission_time(result1, cutoff_time_label)
        if 'level_0' in result.columns:
            result = result.drop(columns=['level_0'])
        return result

    def unify_cutoff_times_days_discharge_time(self, df, cutoff_time_label):
        """Unify records cutoff times based on shared days.

        Args:
            df: cutoff_entity dataframe.
        """

        frames = []
        for d in set(df['end_date']):
            sub_day = df[df['end_date'] == d]

            sub_duration_greater = sub_day[sub_day['duration'] > 0]
            sub_duration_less = sub_day[sub_day['duration'] <= 0]
            frames.append(sub_duration_less)
            sub_duration_greater = sub_duration_greater.sort_values(by=[cutoff_time_label])
            if len(sub_duration_greater) != 0:
                first_date = sub_duration_greater.iloc[0][cutoff_time_label]

                for i in sub_duration_greater.index:
                    sub_duration_greater.at[i, 'ct'] = first_date
                    sub_duration_greater.at[i, 'checked'] = True
                frames.append(sub_duration_greater)

                for i in sub_duration_less.index:
                    sub_duration_less.at[i, 'ct'] = pd.NaT
                    sub_duration_less.at[i, 'checked'] = False
                frames.append(sub_duration_less)

        result = pd.concat(frames)
        result = result.drop_duplicates()
        result[cutoff_time_label] = pd.to_datetime(result.end)
        result = result.reset_index()
        return result

    def unify_cutoff_times_hours_discharge_time(self, df, cutoff_time_label):
        """Unify records cutoff times based on shared time.

        Args:
            df: cutoff_entity dataframe.
        """

        frames = []
        for d in set(df['end_date']):
            sub_day = df[df['end_date'] == d]
            for h in set(sub_day['hour']):
                sub_hour = sub_day[sub_day['hour'] == h]
                sub_hour = sub_hour.sort_values(by=[cutoff_time_label])
                if len(sub_hour) != 0:
                    first_date = sub_hour.iloc[0][cutoff_time_label]
                    for i in sub_hour.index:
                        sub_hour.at[i, 'ct'] = first_date
                        sub_hour.at[i, 'checked'] = True

                    frames.append(sub_hour)

        result = pd.concat(frames)
        result = result.drop_duplicates()
        return result

    def unify_cutoff_time_discharge_time(self, es, cutoff_entity, cutoff_time_label):
        """Process records in the entity that contains cutoff times
        based on shared days and time.

        Args:
            es: fhir entityset.

        Returns:
            processed entity
        """

        df = es[cutoff_entity].df
        df['end_date'] = df[cutoff_time_label].dt.date
        df['hour'] = df.end.apply(lambda x: x.hour)
        duration = (df[cutoff_time_label] - df['start']).dt.days
        duration = duration.tolist()
        df['duration'] = duration
        df['ct'] = ''
        df['checked'] = False
        result1 = self.unify_cutoff_times_days_discharge_time(df, cutoff_time_label)
        result = self.unify_cutoff_times_hours_discharge_time(result1, cutoff_time_label)
        if 'level_0' in result.columns:
            result = result.drop(columns=['level_0'])
        return result
