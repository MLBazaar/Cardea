import pandas as pd

from cardea.problem_definition import ProblemDefinition


class LengthOfStay(ProblemDefinition):
    """Defines the problem of length of stay.

    Predict how many days the patient will be in the hospital. For
    a classification version of the problem, refer to ProlongedLengthOfStay.
    """

    def __init__(self, es):
        target_entity = "hadm_id"
        time_index = "admittime"
        prediction_type = "regression"
        ProblemDefinition.__init__(self, target_entity, time_index, prediction_type, es)

        self.label = "los"

    def los(self, ds):
        return (ds[self.label].dt.days).sum()

    def _generate_label(self, df):
        start = 'admittime'
        end = 'dischtime'
        df[end] = pd.to_datetime(df[end])
        df[start] = pd.to_datetime(df[start])

        df[self.label] = df[end] - df[start]

    def generate_label_times(self, *args, **kwargs):
        df = self.denormalize(entities=['admissions'])
        self._generate_label(df)
        label_times = super().generate_label_times(df,
                                                   target_entity=self.target_entity,
                                                   time_index=self.time_index,
                                                   labeling_function=self.los,
                                                   *args, **kwargs)
        return label_times


class ProlongedLengthOfStay(LengthOfStay):
    """Defines the problem of length of stay in a classification context.

    Predict whether the patient will stay more than a number of days in the
    hospital. For a regression version of the problem, refer to LengthOfStay.
    """

    def __init__(self, es, thresh=7):
        LengthOfStay.__init__(self, es)
        self.prediction_type = "classification"
        self.thresh = thresh

    def generate_label_times(self, *args, **kwargs):
        label_times = super().generate_label_times(*args, **kwargs)
        label_times = label_times.threshold(self.thresh)
        return label_times
