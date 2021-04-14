import pandas as pd

from inspect import getfullargspec

def _get_arguments(arguments, function):
    function_arguments = set(getfullargspec(function)[0])
    return {k: arguments.get(k) for k in function_arguments if arguments.get(k) is not None}

def _search_relationship(es, left, right):
    for r in es.relationships:
        if r.parent_entity.id in left:
            if right == r.child_entity.id:
                left_on = r.parent_variable.id
                right_on = r.child_variable.id

        elif r.child_entity.id in left:
            if right == r.parent_entity.id:
                left_on = r.child_variable.id
                right_on = r.parent_variable.id

    return left_on, right_on


def denormalize(es, entities):
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

    # initial entity to start from (should be the target entity)
    first = entities[0]
    previous = [first]
    df = es[first].df

    # merge the dataframes to create a single input
    for i in range(1, k):
        right = entities[i]

        left_on, right_on = _search_relationship(es, previous, right)
        df = pd.merge(df, es[right].df,
                      left_on=left_on, right_on=right_on,
                      how='left', suffixes=('', '_y')).filter(regex='^(?!.*_y)')

        previous.append(right)

    return df
