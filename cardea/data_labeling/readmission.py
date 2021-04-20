import pandas as pd

from cardea.data_labeling import utils

MIMIC_META = {
    'entity': 'admissions',
    'target_entity': 'subject_id',
    'time_index': 'dischtime'
}

FHIR_META = {
    'entity': 'encounter',
    'target_entity': 'subject',
    'time_index': 'end'
}


def readmission(es, k=30):
    """Defines the labeling task of readmission.
    Predict whether or not the patient will get readmitted
    into the hospital, you can specify the number of days
    between one visit and another using k.
    """
    def label(ds, **kwargs):
        if len(ds) < 2:
            return 0
        initial_discharge = min(ds.index)
        second_admission = sorted(ds[start])[1]
        return (second_admission - initial_discharge).days

    if es.id == 'mimic':
        meta = MIMIC_META
        entities = ['admissions']
        start = 'admittime'
        end = 'dischtime'

    else:
        meta = FHIR_META
        entities = ['encounter', 'period']
        start = 'start'
        end = 'end'

    meta['type'] = 'classification'
    meta['thresh'] = k
    meta['num_examples_per_instance'] = 2
    meta['window_size'] = 2

    df = utils.denormalize(es, entities=entities)

    # generate label
    df[end] = pd.to_datetime(df[end])
    df[start] = pd.to_datetime(df[start])

    return label, df, meta
