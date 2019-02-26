import featuretools as ft


class Featurization():
    """A class that generates a feature matrix from its attributes.

    Attributes:
        es: A featuretools entityset that holds injested data.
        target: A string of the target entity name.
        cutoff: A pandas dataframe that indicates cutoff_time for each instance.
    """
    __name__ = 'Featurization'

    def __init__(self, es, target_entity, cutoff):

        self.es = es
        self.target = target_entity
        self.cutoff = cutoff

    @staticmethod
    def agg_prim():
        return ["sum", "std", "max", "skew", "min", "mean", "count", "percent_true"]

    @staticmethod
    def trans_prim():
        return ["day", "month", "year", "weekday", "is_weekend"]

    @staticmethod
    def n_jobs():
        return 1

    def generate_feature_matrix(self, verbose=True):
        """Calculates a feature matrix and features given in Featurization object.

        Args:
            verbose: A boolean indicator of verbose option.
        Returns:
            A pandas dataframe of the calculated matrix.
        """

        feature_matrix, features_defs = ft.dfs(entityset=self.es,
                                               target_entity=self.target,
                                               agg_primitives=self.agg_prim(),
                                               trans_primitives=self.trans_prim(),
                                               cutoff_time=self.cutoff,
                                               n_jobs=self.n_jobs(),
                                               verbose=verbose)

        # encode categorical values
        fm_encoded, features_encoded = ft.encode_features(feature_matrix,
                                                          features_defs)

        return fm_encoded, features_encoded
