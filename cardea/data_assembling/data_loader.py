import inspect
import sys

import networkx as nx
import numpy as np
import pandas as pd
from numpy import nan

from cardea import fhir as fh


class DataLoader():
    """A class that loads data into fhir class objects."""

    __name__ = 'DataLoader'

    def create_object(self, df, file_name):
        """Returns fhir representation of pandas dataframe.

        Args:
            df: A dataframe with fhir class data.
            file_name: A string that determines the resource type of fhir class.

        Returns:
            An object with the corresponding fhir class.

        Raises:
            LookupError: An error occurs if df doesn't have an id.
        """

        fhir_classes = [c[0] for c in inspect.getmembers(fh)]
        if file_name not in fhir_classes:
            raise LookupError('{} file is not part of FHIR schema'.format(file_name))

        object_values = df.to_dict('list')
        id_enum = ['identifier', 'id', 'object_id']

        id_exist = any(i in df.columns for i in id_enum)

        if not id_exist:
            raise LookupError('{} is missing an identifier column'.format(file_name))

        object = getattr(sys.modules[fh.__name__], file_name)(object_values)
        object.assert_type()
        return object

    def get_object_ids(self, objects):
        """Returns list of fhir object identifiers.

        Args:
            objects: A list of fhir class objects.

        Returns:
            A list of the corresponding identifiers.
        """

        identifiers = [(object.__class__.__name__, object.get_id()) for object in objects]
        identifiers = dict(identifiers)

        return identifiers

    def get_relationships(self, objects, names):
        """Returns relationships of fhir objects.

        Args:
            objects: A list of fhir class objects.

        Returns:
            A pandas dataframe of the corresponding relationships.
        """

        relationships = [relation for o in objects for relation in o.get_eligible_relationships()
                         if relation['parent_entity'] in names]
        relationships = pd.DataFrame(relationships)

        return relationships

    def get_dataframes(self, objects):
        """Returns pandas dataframe of fhir objects.

        Args:
            objects: A list of fhir class objects.

        Returns:
            A dictionary with the dataframes of the loaded fhir classes.
        """

        fhir = [(object.__class__.__name__, object.get_dataframe()) for object in objects]
        fhir = dict(fhir)

        return fhir

    def check_column_existence(self, entity_set, target_entity, column_name):
        """Checks if a coulmn exists in the entity set.

        Args:
            entity_set: fhir entityset.
            column_name: The column name to be checked.
            target_entity: The entity name which contains the column_name.

        Returns:
            True if the column_name exists, False otherwise.
        """
        columns_list = []
        does_exist = True

        for variable in entity_set.__getitem__(target_entity).variables:
            columns_list.append(variable.name)

        does_exist = column_name in columns_list
        if does_exist:
            return does_exist
        else:
            return False

    def check_for_missing_values(self, entity_set, target_entity, column_name):
        """Checks if there is a missing value in the given column.

        Args:
            entity_set: fhir entityset.
            column_name: The column name to be checked for missing values.
            target_entity: The entity name which contains the column_name.

        Returns:
            False is the column_name does not contain a missing value.
        """
        if self.check_column_existence(entity_set, target_entity, column_name):

            nat = np.datetime64('NaT')
            missings = [
                nat,
                nan,
                'null',
                'nan',
                'NAN',
                'Nan',
                'NaN',
                'undefined',
                None,
                'unknown']
            contains_nan = False

            target_label_values = entity_set.__getitem__(target_entity).df[column_name]

            for missing_value in missings:
                if missing_value in list(target_label_values):
                    contains_nan = True

            for missing_value in missings:
                for target_value in (target_label_values):
                    if pd.isnull(target_value):
                        contains_nan = True

            return contains_nan
        else:
            return False


class Diamond(DataLoader):
    """This class serves as a post processing step to reading the data.

    Attributes:
        fhir: A dictionary with the correspondig fhir dataframes.
        relationships: A dataframe of present fhir Relationships.
    """

    __name__ = 'Diamond'

    def __init__(self, objects):

        self.fhir = self.get_dataframes(objects)
        self.relationships = self.get_relationships(objects, list(self.fhir.keys()))

    def get_fhir_dataframes(self):
        """Returns fhir dataframes with their associated names.

        Returns:
            A dictionary with the correspondig fhir dataframes.
        """

        return self.fhir

    def get_fhir_relationships(self):
        """Returns fhir relationships.

        Returns:
            A dataframe of present fhir Relationships.
        """

        return self.relationships

    def resolve_diamond(self):
        """Resolve relationships that have a diamond graphs.

        This method is a pipline to solve diamond graphs by depending on MST to
        resolve the present cycles and maintains information by copying data from
        the cut ties.
        """

        self.relationships['weight'] = self.merge_cost()

        G = nx.from_pandas_edgelist(
            self.relationships,
            source='parent_entity',
            target='child_entity',
            edge_attr=['weight'])

        if len(list(nx.cycle_basis(G))) > 0:

            self.resolve_reference()
            G = nx.from_pandas_edgelist(
                self.relationships,
                source='parent_entity',
                target='child_entity',
                edge_attr=['weight'])

            X = nx.maximum_spanning_tree(G)
            edges = [x for x in G.edges() if x not in X.edges()]

            for edge in edges:
                if edge[0] != edge[1]:
                    self.merge(edge, remove=True)

    def get_relation(self, source, target):
        """Obtains the record for the edge to break from relationships.

        Args:
            source: The resource from which an edge leaves.
            target: The resource from which an edge enters.

        Returns:
            An index of the record of the edge in relationships.
        """

        source_df = self.relationships[self.relationships['parent_entity'] == source]
        target_df = self.relationships[self.relationships['child_entity'] == target]
        intersection = source_df[source_df.index.isin(target_df.index)]

        if len(intersection) == 0:
            source_df = self.relationships[self.relationships['child_entity'] == source]
            target_df = self.relationships[self.relationships['parent_entity'] == target]
            intersection = source_df[source_df.index.isin(target_df.index)]

        return intersection

    def merge(self, edge, remove=False):
        """Merges dataframes that are in edge then removes it from relationships and updates the fhir.

        Args:
            edge: A tuple that has the relationship to be broken.
            remove: A boolean to determine whether the edge should be removed from relationships.
        """

        relation = self.get_relation(edge[0], edge[1])

        source_entity = relation.iloc[0]['parent_entity']
        source_column = relation.iloc[0]['parent_variable']
        target_entity = relation.iloc[0]['child_entity']
        target_column = relation.iloc[0]['child_variable']

        source_df = self.fhir[source_entity].copy()
        target_df = self.fhir[target_entity].copy()

        source_df[source_column] = source_df[source_column].astype('str')
        target_df[target_column] = target_df[target_column].astype('str')

        source_df.columns = [source_entity + "." + str(col) for col in source_df.columns]
        target_df.columns = [target_entity + "." + str(col) for col in target_df.columns]

        source_merge_col = source_entity + "." + source_column
        target_merge_col = target_entity + "." + target_column

        target_df = pd.merge(source_df, target_df, how='right', left_on=[source_merge_col],
                             right_on=[target_merge_col])

        target_df = target_df.drop([source_entity + "." + source_column], axis=1)

        target_df.columns = [str(col).split('.')[-1] for col in target_df.columns]
        self.fhir[target_entity] = target_df

        if remove:
            self.relationships.drop(relation.index, inplace=True)

    def merge_cost(self):
        """ Calculates the merge cost of two dataframes.

        The equation is defined as the sum of the dataframe sizes.

        Returns:
            A list of the cost of merging for each relationship
        """

        cost = [self.fhir[row['parent_entity']].size + self.fhir[row['child_entity']].size
                for _, row in self.relationships.iterrows()]

        return cost

    def resolve_reference(self):
        """ Consolidates relationships that have a connection to References.
        """

        if 'Identifier' not in list(self.fhir.keys()):
            raise LookupError('\'Identifier\' file is not loaded.')

        identifier_df = self.fhir['Identifier']  # always subset from id
        identifier_df['object_id'] = identifier_df['object_id'].astype('str')

        for i, relation in self.relationships.iterrows():

            if relation['parent_entity'] == 'Reference':

                df = self.fhir[relation['child_entity']]
                subset_values = [str(x) for x in df[relation['child_variable']].values]
                sub_df = identifier_df.loc[identifier_df['object_id'].isin(subset_values)]

                for second_name, second_df in self.fhir.items():
                    if 'identifier' not in second_df.columns or second_name == 'Reference':
                        continue

                    second_df['identifier'] = second_df['identifier'].astype('str')
                    if len(set(second_df['identifier']).intersection(sub_df['object_id'])) > 0:
                        self.relationships.at[i, 'parent_entity'] = second_name
                        break

            if relation['parent_entity'] == 'Identifier':
                self.relationships.drop(i, inplace=True)
