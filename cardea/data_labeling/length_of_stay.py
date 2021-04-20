import pandas as pd

from cardea.data_labeling import utils

MIMIC_META = {
    'entity': 'admissions',
    'target_entity': 'hadm_id',
    'time_index': 'admittime',
}

FHIR_META = {
    'entity': 'encounter',
    'target_entity': 'identifier',
    'time_index': 'start',
}


def length_of_stay(es, k=None):
    """Defines the labeling task of length of stay.

    Predict how many days the patient will be in the hospital. For
    a classification version of the problem, specify k.
    """
    def label(ds, **kwargs):
        return (ds['los'].dt.days).sum()

    if es.id == 'mimic':
        meta = MIMIC_META
        entities = ['admissions']
        start = 'admittime'
        end = 'dischtime'

    elif es.id == 'fhir':
        meta = FHIR_META
        entities = ['Encounter', 'Period']
        start = 'start'
        end = 'end'

    meta['type'] = 'regression'
    meta['num_examples_per_instance'] = 1

    if k:
        meta['type'] = 'classification'
        meta['thresh'] = k

    df = utils.denormalize(es, entities=entities)

    # generate label
    df[end] = pd.to_datetime(df[end])
    df[start] = pd.to_datetime(df[start])
    df['los'] = df[end] - df[start]

    return label, df, meta
