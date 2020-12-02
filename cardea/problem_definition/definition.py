import composeml as cp
import pandas as pd


class ProblemDefinition:
    """Class that defines the prediction problem.

    This class supports the generation of `label_times` which
    is fundamental to the feature generation phase as well
    as specifying the target labels.

    Args:
        target_entity (str):
            The instance id of the target entity.
        time_index (str):
            The time index specifying at what point to start the prediction.
        prediction_type (str):
            The type of the machine learning prediction; classification or
            regression.
        es (featuretools.EntitySet):
            An entityset representation of the data.
    """

    def __init__(self, target_entity, time_index, prediction_type, es):
        self.target_entity = target_entity
        self.time_index = time_index
        self.prediction_type = prediction_type
        self.es = es

    def _search_relationship(self, left, right):
        for r in self.es.relationships:
            if r.parent_entity.id in left:
                if right == r.child_entity.id:
                    left_on = r.parent_variable.id
                    right_on = r.child_variable.id

            elif r.child_entity.id in left:
                if right == r.parent_entity.id:
                    left_on = r.child_variable.id
                    right_on = r.parent_variable.id

        return left_on, right_on

    def denormalize(self, entities):
        """Merge a set of entities into a single dataframe.

        Convert a set of entities from the entityset into a single
        dataframe by repetitively merging the selected entities. The
        merge process is applied sequentially.

        Args:
            entities (list):
                list of strings denoting which entities to merge.

        Returns:
            pandas.DataFrame:
                A single dataframe containing all the information from the
                selected entities.
        """
        k = len(entities)
        assert k > 0

        # initial entity to start from (should be the target entity)
        first = entities[0]
        previous = [first]
        df = self.es[first].df

        # merge the dataframes to create a single input
        for i in range(1, k):
            right = entities[i]

            left_on, right_on = self._search_relationship(previous, right)
            df = pd.merge(df, es[right].df,
                          left_on=left_on, right_on=right_on,
                          how='left', suffixes=('', '_y')).filter(regex='^(?!.*_y)')

            previous.append(right)

        return df

    def generate_label_times(self, df, *args, **kwargs):
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
        label_maker = cp.LabelMaker(*args, **kwargs)
        label_times = label_maker.search(df.sort_values(self.time_index),
                                         num_examples_per_instance=1)

        return label_times
