import pandas as pd

from cardea.data_labeling.utils import denormalize

MIMIC_META = {
    'entity': 'admissions',
    'target_entity': 'patient_id',
    'time_index': 'dischtime'
}

FHIR_META = {
    'entity': 'encounter',
    'target_entity': 'subject',
    'time_index': 'end'
}


def readmission(es, k=30):
    """Defines the labeling task of length of stay.

    Predict how many days the patient will be in the hospital. For
    a classification version of the problem, specify k.
    """
    def label(ds, **kwargs):
        initial_discharge = min(ds[end].values)
        second_admission = sorted(ds[start].values)[1]
        return (second_admission - initial_discharge).dt.days

    if es.id == 'mimic':
        meta = MIMIC_META
        entities = ['admissions']
        start = 'admittime'
        end = 'dischtime'

    elif es.id == 'fhir':
        meta = FHIR_META
        entities = ['encounter', 'period']
        start = 'start'
        end = 'end'

    meta['type'] = 'classification'
    meta['thresh'] = k
    meta['num_examples_per_instance'] = 2

    df = denormalize(es, entities=entities)

    # generate label
    df[end] = pd.to_datetime(df[end])
    df[start] = pd.to_datetime(df[start])

    return label, df, meta
