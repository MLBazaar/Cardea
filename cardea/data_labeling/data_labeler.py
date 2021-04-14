import composeml as cp

from cardea.data_labeling.utils import _get_arguments


class DataLabeler:
    """Class that defines the prediction problem.

    This class supports the generation of `label_times` which
    is fundamental to the feature generation phase as well
    as specifying the target labels.

    Args:
        function (method):
            function that defines the labeling function, it should return a
            tuple of labeling function, the dataframe, and the name of the
            target entity.
    """

    def __init__(self, function):
        self.function = function

    def generate_label_times(self, es, subset, verbose, **kwargs):
        """Searches the data to calculate label times.

          Args:
              es (featuretools.EntitySet):
                Entityset to extract `label_times` from.

          Returns:
              composeml.LabelTimes:
                  Calculated labels with cutoff times.
        """
        labeling_function, df, meta = self.function(es)

        data = df
        if isinstance(subset, float) or isinstance(subset, int):
            data = data.sample(subset)

        if isinstance(subset, list):
            data = data[data['isinstance'].isin(subset)]

        target_entity = meta.get('target_entity')
        time_index = meta.get('time_index')
        window_size = meta.get('window_size')
        thresh = meta.get('thresh')
        pred_type = meta.get('type')
        label_maker = cp.LabelMaker(labeling_function=labeling_function,
                                    target_entity=target_entity,
                                    time_index=time_index,
                                    window_size=window_size)

        kwargs = {**meta, **kwargs}
        kwargs = _get_arguments(kwargs, label_maker.search)
        label_times = label_maker.search(data.sort_values(time_index),
                                         verbose=verbose, **kwargs)
        if thresh is not None:
            label_times = label_times.threshold(thresh)

        return label_times, pred_type, meta
