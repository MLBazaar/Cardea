from glob import glob

import pandas as pd

import featuretools as ft
from cardea.data_loader import DataLoader


class EntitySetLoader(DataLoader):

    def create_entity(self, object, entity_set):
        """Create an entity from FHIR object and add it to entityset."""

        df = object.get_dataframe()
        object_name = object.__class__.__name__

        # get ID if exists
        if 'identifier' in df.columns:
            id = 'identifier'
        elif 'id' in df.columns:
            id = 'id'
        elif 'object_id' in df.columns:
            id = 'object_id'
        else:
            raise LookupError('{} is missing an identifier column', object_name)

        if object_name == 'Period':
            entity_set.entity_from_dataframe(entity_id=str(object_name),
                                             dataframe=df,
                                             index=id,
                                             time_index="start")
        else:
            entity_set.entity_from_dataframe(entity_id=str(object_name),
                                             dataframe=df,
                                             index=id)

    def create_relationships(self, object, entity_set):
        """Bind entities in the entityset."""

        for relation in object.get_relationships():
            # parent table: 0, field: 1
            # child table: 2, field: 3

            if relation['parent_entity'] in entity_set.entity_names and getattr(
                    object, relation['child_variable']) is not None:
                new_relationship = ft.Relationship(
                    entity_set[relation['parent_entity']][relation['parent_variable']],
                    entity_set[relation['child_entity']][relation['child_variable']])

                entity_set.add_relationship(new_relationship)

    def load_data_entityset(self, folder_path):
        """Return entityset loaded with .csv files in folder_path."""

        all_objects = []
        csv_files = glob(folder_path + "/*.csv")
        entity_set = ft.EntitySet(id="fhir")

        for file_path in csv_files:
            df = pd.read_csv(file_path)
            file_name = file_path.split("/")[-1].split(".")[0]

            object = self.create_object(df, file_name)
            all_objects.append(object)
            self.create_entity(object, entity_set=entity_set)

        for object in all_objects:
            self.create_relationships(object, entity_set=entity_set)

        return entity_set
