import featuretools as ft


class Featurization():
    """A class that generates a feature matrix from its attributes.
        """
    __name__ = 'Featurization'

    @staticmethod
    def agg_prim():
        return ["sum", "std", "max", "skew", "min", "mean", "count", "percent_true"]

    @staticmethod
    def trans_prim():
        return ["day", "month", "year", "weekday", "is_weekend"]

    @staticmethod
    def n_jobs():
        return 1

    @staticmethod
    def max_depth():
        return 2

    def generate_feature_matrix(self, es, target, cutoff, verbose=True):
        """Calculates a feature matrix and features given in Featurization object.
            Args:
            es: A featuretools entityset that holds injested data.
            target: A string of the target entity name.
            cutoff: A pandas dataframe that indicates cutoff_time for each instance.
            verbose: A boolean indicator of verbose option.
            Returns:
            A pandas dataframe of the calculated matrix.
            """

        feature_matrix, features_defs = ft.dfs(entityset=es,
                                               target_entity=target,
                                               agg_primitives=self.agg_prim(),
                                               trans_primitives=self.trans_prim(),
                                               cutoff_time=cutoff,
                                               n_jobs=self.n_jobs(),
                                               max_depth=self.max_depth(),
                                               verbose=verbose)

        # encode categorical values
        fm_encoded, features_encoded = ft.encode_features(feature_matrix,
                                                          features_defs)

        return fm_encoded, features_encoded
