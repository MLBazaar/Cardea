
import pandas as pd

from cardea.data_labeling.utils import denormalize

def appointment_no_show(es):
    """Defines the labeling task of appointment no show. 
    """
    def missed(ds, **kwargs):
        return (ds["status"]).sum()

    meta = {
        "entity": "Appointment",
        "target_entity": "identifier",
        "time_index": "created",
        "type": "classification",
        "num_examples_per_instance": 1,
        "thresh": 1
    }

    df = denormalize(es, entities=['Appointment'])
    df['status'] = pd.Categorical(df['status']).codes

    return missed, df, meta
