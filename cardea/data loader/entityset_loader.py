from glob import glob

import featuretools as ft

import object_loader

def create_entity(object, entity_set):
    """ this method receives FHIR objects and creates featuretools entities and adds them to the
    entityset
    """

    df = object.get_dataframe()

    # get ID if exists
    if 'identifier' in df.columns:
        id = 'identifier'
    elif 'id' in df.columns:
        id = 'id'
    else:
        id = 'object_id'

    if object.__class__.__name__ == 'Period':
        entity_set.entity_from_dataframe(entity_id=str(object.__class__.__name__),
                                 dataframe=df,
                                 index=id,
                                 time_index="start")
    else:
        entity_set.entity_from_dataframe(entity_id=str(object.__class__.__name__),
                                 dataframe=df,
                                 index=id)


def create_relationships(object, entity_set):
    """ this method binds the different entities in the entityset
    """

    for relation in object.get_relationships():
        # parent table: 0, field: 1
        # child table: 2, field: 3

        if relation['parent_entity'] in entity_set.entity_names and getattr(object, relation['child_variable']) is not None:
            new_relationship = ft.Relationship(entity_set[relation['parent_entity']][relation['parent_variable']],
                                               entity_set[relation['child_entity']][relation['child_variable']])

            entity_set.add_relationship(new_relationship)


def load_data_entityset(folder_path):
    """ this method takes the path of .csv files and loads them to FHIR schema entityset
    """

    all_objects = []
    csv_files = glob(folder_path + "/*.csv")
    entity_set = ft.EntitySet(id="fhir")

    for file_path in csv_files:
        object = object_loader.create_object(file_path)
        all_objects.append(object)
        create_entity(object, entity_set=entity_set)

    for object in all_objects:
        create_relationships(object, entity_set=entity_set)

    return entity_set

load_data_entityset("data/KFMC_Segmentd")