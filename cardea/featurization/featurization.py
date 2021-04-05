import featuretools as ft


class Featurization():
    """A class that generates a feature matrix from its attributes."""

    __name__ = 'Featurization'

    AGG_PRIMITIVES = ["sum", "std", "max", "skew", "min", "mean", "count", "percent_true",
                      "num_unique", "mode"]

    TRANS_PRIMITIVES = ["day", "month", "year", "weekday", "is_weekend"]

    def generate_feature_matrix(self, es, target, label_times,
                                instance_ids=None, agg_primitives=AGG_PRIMITIVES,
                                trans_primitives=TRANS_PRIMITIVES, max_depth=2,
                                ignore_entities=None, ignore_variables=None, seed_features=None,
                                drop_contains=None, drop_exact=None, max_features=-1,
                                training_window=None, n_jobs=1, verbose=False,
                                include_cutoff_time=True, encode=False):
        """Calculates a feature matrix and features given in Featurization object.

        Args:
            es (featuretools.EntitySet):
                An already initialized entityset.
            target (str):
                Name of the entity (entity id) on which to make predictions.
            label_times (pandas.DataFrame):
                A data frame that specifies the times at which to calculate the features 
                for each instance. This data frame contains three columns ``instance_id``, 
                ``time``, ``label``. The ``instance_id`` specifies the instances for 
                which to calculate features over. The ``time`` column specifies the cutoff
                time for each instance. Data before the cutoff time will be used for
                calculating the feature matrix. The ``label`` column specifies the ground 
                truth label (value we want to predict) for each instance.
            instance_ids (list):
                List of instances on which to calculate features.
            agg_primitives (list):
                List of Aggregation Feature types to apply.
            trans_primitives (list):
                List of Transform Feature functions to apply.
            max_depth (int):
                Maximum allowed depth of features.
            ignore_entities (list):
                List of entities to blacklist when creating features.
            ignore_variables (dict):
                List of specific variables within each entity to blacklist when creating features.
            seed_features (list):
                List of manually defined features to use.
            drop_contains (list):
                Drop features that contains these strings in name.
            drop_exact (list):
                Drop features that exactly match these strings in name.
            max_features (int):
                Cap the number of generated features to this number. If -1, no limit.
            training_window (ft.Timedelta or str):
                Window defining how much time before the cutoff time data can be used when c
                alculating features. If ``None``, all data before cutoff time is used.
                Defaults to ``None``. Month and year units are not relative when Pandas
                Timedeltas are used. Relative units should be passed as a Featuretools
                Timedelta or a string.
            n_jobs (int):
                Number of parallel processes to use when calculating feature matrix.
            verbose (bool):
                An indicator of verbose option.
            include_cutoff_time (bool):
                Include data at cutoff times in feature calculations. Defaults to ``True``.
            encode (bool):
                Whether or not to encode categorical into one-hot features.

        Returns:
            pandas.DataFrame, list:
                * The generated feature matrix.
                * List of feature definitions in the feature matrix.
        """

        feature_matrix, features_defs = ft.dfs(entityset=es,
                                               target_entity=target,
                                               cutoff_time=label_times,
                                               instance_ids=instance_ids,
                                               agg_primitives=agg_primitives,
                                               trans_primitives=trans_primitives,
                                               max_depth=max_depth,
                                               ignore_entities=ignore_entities,
                                               ignore_variables=ignore_variables,
                                               seed_features=seed_features,
                                               drop_contains=drop_contains,
                                               drop_exact=drop_exact,
                                               max_features=max_features,
                                               training_window=training_window,
                                               n_jobs=n_jobs,
                                               verbose=verbose,
                                               include_cutoff_time=include_cutoff_time)

        if encode:
            # encode categorical values
            return ft.encode_features(feature_matrix, features_defs)

        return feature_matrix, features_defs
