

from cardea.data_labeling import utils


def appointment_no_show(es):
    """Defines the labeling task of appointment no show.
    """
    def label(ds, **kwargs):
        return True if 'noshow' in ds["status"].values else False

    if es.id == 'mimic':
        raise ValueError("Problem not supported for MIMIC data.")

    meta = {
        "entity": "Appointment",
        "target_entity": "identifier",
        "time_index": "created",
        "type": "classification",
        "num_examples_per_instance": 1,
        "ignore_variables": {'Appointment': ['status']}
    }

    df = utils.denormalize(es, entities=['Appointment'])

    return label, df, meta
