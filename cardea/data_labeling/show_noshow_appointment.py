

from cardea.data_labeling.utils import denormalize


def appointment_no_show(es):
    """Defines the labeling task of appointment no show.
    """
    def missed(ds, **kwargs):
        return True if 'noshow' in ds["status"].values else False

    if es.id == 'mimic':
        raise ValueError("Problem not supported for MIMIC data.")

    meta = {
        "entity": "Appointment",
        "target_entity": "identifier",  # automatically, should this be the index of the table?
        "time_index": "created",
        "type": "classification",
        "num_examples_per_instance": 1
    }

    df = denormalize(es, entities=['Appointment'])

    return missed, df, meta
