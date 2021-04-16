
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


def diagnosis_prediction(es, diag):
    """Defines the labeling task of length of stay.

    Predict how many days the patient will be in the hospital. For
    a classification version of the problem, specify k.
    """
    def label(ds, **kwargs):
        return True if diag in ds[column].values else False

    if es.id == 'mimic':
        meta = MIMIC_META
        entities = ['admissions']
        column = 'diagnosis'

    elif es.id == 'fhir':
        meta = FHIR_META
        entities = ['encounter', 'encounter_diagnosis', 'condition',
                    'codeableconcept', 'coding', 'period']
        column = 'code'

    meta['type'] = 'classification'
    meta['num_examples_per_instance'] = 1

    df = denormalize(es, entities=entities)

    return label, df, meta
