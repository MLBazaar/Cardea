# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import community as co


class CommunityBestPartition(object):

    def produce(self, X, best_partition=None, graph=None):
        best_partition = best_partition or co.best_partition(graph)
        values = [b for a, b in best_partition.items()]
        missing_community_index = np.max(values) + 10

        result = pd.Series(index=X.index)

        for i in X.index:
            node = X.loc[i][0]

            if node in best_partition:
                community = best_partition[node]

            elif str(node) in best_partition:
                community = best_partition[str(node)]

            else:
                community = missing_community_index

                # increment missing index
                missing_community_index += 1

            result.loc[i] = community

        return result.values
