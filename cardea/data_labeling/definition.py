import composeml as cp
import pandas as pd


class DataLabeler:
    """Class that defines the prediction problem.

    This class supports the generation of `label_times` which 
    is fundamental to the feature generation phase as well 
    as specifying the target labels.

    Args:
        clf (function):
            function that defines the labeling function, it should return a
            tuple of labeling function, the dataframe, and the name of the
            target entity.
    """
    def __init__(self, clf):
        self.clf = clf

    def generate_label_times(self, es, *args, **kwargs):
      """Searches the data to calculate label times.

        Args:
            df (pandas.DataFrame): 
                Data frame to search and extract labels.
            *args: 
                Positional arguments for label maker.
            **kwargs: 
                Keyword arguments for label maker.
        Returns:
            composeml.LabelTimes: 
                Calculated labels with cutoff times.
      """
      labeling_function, df, meta = self.clf(es)
      kwargs = {**meta, **kwargs}
      target_entity = kwargs.get('target_entity')
      time_index = kwargs.get('time_index')
      window_size = kwargs.get('window_size')
      thresh = kwargs.get('thresh')
      label_maker = cp.LabelMaker(labeling_function=labeling_function,
                                  target_entity=kwargs.get('target_entity'),
                                  time_index=kwargs.get('time_index'),
                                  window_size=kwargs.get('window_size'))
      
      label_times = label_maker.search(df.sort_values(time_index),
                                       *args,
                                       **kwargs)
      if thresh is not None:
          label_times.threshold(thresh)

      return label_times, kwargs.get('entity')