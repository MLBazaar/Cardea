from glob import glob

import featuretools as ft
import pandas as pd

from cardea.data_loader import DataLoader, Diamond


class EntitySetLoader(DataLoader):
    """A class that loads fhir class objects to featuretools entityset."""

    __name__ = 'EntitySetLoader'

    def create_entity(self, fhir, identifiers, entity_set):
        """Creates an entity from fhir dataframes and add it to entityset.

        Args:
            fhir (dict):
                A dictionary of fhir class dataframes.
            entity_set (featuretools.EntitySet):
                The global entityset that the entity will be added to.
        """

        for object_name, df in fhir.items():

            id = identifiers[object_name]
            df = df.apply(pd.to_numeric, errors='ignore')

            if object_name == 'Period':
                entity_set.entity_from_dataframe(entity_id=str(object_name),
                                                 dataframe=df,
                                                 index=id,
                                                 time_index="start")
            else:
                entity_set.entity_from_dataframe(entity_id=str(object_name),
                                                 dataframe=df,
                                                 index=id)

    def create_relationships(self, relationships, entity_set):
        """Binds entities in the entityset.

        Args:
            relationships: A dataframe of the relationships in fhir.
            entity_set: The global entityset that the entity will be added to.
        """

        for i, relation in relationships.iterrows():
            # parent table: 0, field: 1
            # child table: 2, field: 3

            new_relationship = ft.Relationship(
                entity_set[relation['parent_entity']][relation['parent_variable']],
                entity_set[relation['child_entity']][relation['child_variable']])

            entity_set.add_relationship(new_relationship)

    def load_data_entityset(self, folder_path):
        """Returns an entityset loaded with .csv files in folder_path.

        Loads .csv files into pandas dataframes then loads them into featuretools' entityset.

        Args:
            folder_path (dict):
                A directory of all .csv files that should be loaded.

        Returns:
            featuretools.EntitySet:
                An entityset with loaded data.
        """

        fhir = self.read_csv_files(folder_path=folder_path)
        return self.load_df_entityset(fhir=fhir)

    def read_csv_files(self, folder_path):
        """Returns a dictionary with loaded .csv files in folder_path.

        Loads .csv files into pandas dataframes.

        Args:
            folder_path: A dictionary of fhir resources in pandas dataframe format.

        Returns:
            A dictionary of fhir resources in pandas dataframe format.
        """

        fhir = {}

        csv_files = glob(folder_path + "/*.csv")
        for file_path in csv_files:
            df = pd.read_csv(file_path)
            file_name = file_path.split("/")[-1].split(".")[0]

            fhir[file_name] = df

        return fhir

    def load_df_entityset(self, fhir):
        """Returns an entityset loaded with received dataframes in fhir.

        Loads the received dictionary of fhir resources into featuretools' entityset, where
        the key is the resource name and the value is a pandas dataframe.

        Args:
            fhir: A dictionary of fhir resources in pandas dataframe format.

        Returns:
            An entityset with loaded data.
        """

        all_objects = []
        entity_set = ft.EntitySet(id="fhir")

        for name, df in fhir.items():

            object = self.create_object(df, name)
            all_objects.append(object)

        diamond = Diamond(all_objects)
        diamond.resolve_diamond()
        fhir = diamond.get_fhir_dataframes()
        relationships = diamond.get_fhir_relationships()
        identifiers = diamond.get_object_ids(all_objects)

        self.create_entity(fhir, identifiers, entity_set=entity_set)
        self.create_relationships(relationships, entity_set=entity_set)

        return entity_set
