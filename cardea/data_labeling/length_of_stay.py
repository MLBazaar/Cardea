import pandas as pd

from cardea.data_labeling.utils import denormalize


def length_of_stay(es):
    """Defines the labeling task of length of stay. 
    
    Predict how many days the patient will be in the hospital. For 
    a classification version of the problem, refer to ProlongedLengthOfStay.
    """
    def los(ds, **kwargs):
        return (ds["los"].dt.days).sum()

    label = "los"

    meta = {
        "entity": "admissions",
        "target_entity": "hadm_id",
        "time_index": "admittime",
        "type": "regression",
        "num_examples_per_instance": 1,
        "thresh": 7
    }

    df = denormalize(es, entities=['admissions', ])
    
    # generate label
    start = 'admittime'
    end = 'dischtime'
    df[end] = pd.to_datetime(df[end])
    df[start] = pd.to_datetime(df[start])
    df[label] = df[end] - df[start]

    return los, df, meta