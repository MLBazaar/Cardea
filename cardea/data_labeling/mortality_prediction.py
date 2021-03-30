import pandas as pd

from cardea.data_labeling.utils import denormalize

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

def mortality(es):
    """Defines the labeling task of length of stay. 
    
    Predict how many days the patient will be in the hospital. For 
    a classification version of the problem, specify k.
    """
    def mortal(ds, **kwargs):
        return ds['hospital_expire_flag'].sum() > 0

    if es.id == 'mimic':
        meta = MIMIC_META
        entities = ['admissions']

    elif es.id == 'fhir':
        meta = FHIR_META
        entities = ['encounter', 'encounter_diagnosis', 'condition', 
                    'codeableconcept', 'coding', 'period']

    meta['type'] = 'classification'
    meta['num_examples_per_instance'] = 1

    df = denormalize(es, entities=entities)
    
    # generate label
    if es.id == 'fhir':
        causes_of_death = ['X60', 'X84', 'Y87.0', 'X85', 'Y09', 'Y87.1', 
                           'V02', 'V04', 'V09.0', 'V09.2', 'V12', 'V14']

        df['hospital_expire_flag'] = int(df['code'].isin(causes_of_death))

    return mortal, df, meta
