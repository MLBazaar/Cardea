import json
from inspect import isclass

import featuretools as ft
import pandas as pd

import cardea
from cardea.data_loader import EntitySetLoader
from cardea.featurization import Featurization
from cardea.modeling import Modeler
from cardea.problem_definition import (
    DiagnosisPrediction, LengthOfStay, MissedAppointmentProblemDefinition, MortalityPrediction,
    ProlongedLengthOfStay, Readmission)


class Cardea():
    """An interface class that ties the end-to-end system together.

    Args:
        es_loader (EntitySetLoader):
            An entityset loader.
        featurization (Featurization):
            A featurization class.
        modeler (Modeler):
            A modeling class.
        problems (list):
            A list of currently available prediction problems.
        chosen_problem (str):
            The selected prediction problem or regression.
        es (featuretools.EntitySet):
            The loaded entityset.
        target_entity (str):
            The target entity for featurization.
    """

    def __init__(self):

        self.es_loader = EntitySetLoader()
        self.featurization = Featurization()
        self.modeler = Modeler()

        self.es = None
        self.chosen_problem = None
        self.target_entity = None

    def load_data_entityset(self, folder_path=None):
        """Returns an entityset loaded with .csv files in folder_path.

        Load the given dataset within the folder path into an entityset. The dataset
        must be in a FHIR structure format. If no folder_path is not passed, the
        function will automatically load kaggle's missed appointment dataset.

        Args:
            folder_path (str):
                A directory of all .csv files that should be loaded.

        Returns:
            featuretools.EntitySet:
                An entityset with loaded data.
        """

        if folder_path:
            self.es = self.es_loader.load_data_entityset(folder_path)

        else:
            csv_s3 = "https://s3.amazonaws.com/dai-cardea/"
            kaggle = ['Address',
                      'Appointment_Participant',
                      'Appointment',
                      'CodeableConcept',
                      'Coding',
                      'Identifier',
                      'Observation',
                      'Patient',
                      'Reference']

            fhir = {
                resource: pd.read_csv(
                    csv_s3 + resource + ".csv") for resource in kaggle}
            self.es = self.es_loader.load_df_entityset(fhir)

    def list_problems(self):
        """Returns a list of the currently available problems.

        Returns:
            list:
                A list of the available problems.
        """

        problems = set([])
        for attribute_string in dir(cardea.problem_definition):
            attribute = getattr(cardea.problem_definition, attribute_string)
            if isclass(attribute):
                if attribute.__name__ and attribute.__name__ != 'ProblemDefinition':
                    problems.add(attribute.__name__)

        return problems

    def select_problem(self, selection, parameter=None):
        """Select a prediction problem and extract information.

        Update the select_problem attribute and generate the cutoff times,
        the target entity and update the entityset.

        Args:
            selection (str):
                Name of the chosen prediction problem.
            parameters (dict):
                Variables to change the default parameters, if any.

        Returns:
            featuretools.EntitySet, str, pandas.DataFrame:
                * An updated EntitySet if a new column is generated.
                * A string indicating the selected target entity.
                * A dataframe of cutoff times and their target labels.
        """

        # problem selection
        if selection == 'LengthOfStay':
            self.chosen_problem = LengthOfStay()

        elif selection == 'MortalityPrediction':
            self.chosen_problem = MortalityPrediction()

        elif selection == 'MissedAppointmentProblemDefinition':
            self.chosen_problem = MissedAppointmentProblemDefinition()

        elif selection == 'ProlongedLengthOfStay' and parameter:
            self.chosen_problem = ProlongedLengthOfStay(parameter)

        elif selection == 'ProlongedLengthOfStay':
            self.chosen_problem = ProlongedLengthOfStay()

        elif selection == 'Readmission' and parameter:
            self.chosen_problem = Readmission(parameter)

        elif selection == 'Readmission':
            self.chosen_problem = Readmission()

        elif selection == 'DiagnosisPrediction' and parameter:
            self.chosen_problem = DiagnosisPrediction(parameter)

        elif selection == 'DiagnosisPrediction':
            raise ValueError('unspecified diagnosis code')

        else:
            raise ValueError('{} is not a defined problem'.format(selection))

        # target label calculation
        self.es, self.target_entity, cutoff = self.chosen_problem.generate_cutoff_times(self.es)
        return cutoff

    def list_feature_primitives(self):
        """Returns built-in primitive in Featuretools.

        Returns:
            pandas.DataFrame:
                A dataframe that lists and describes each built-in primitives.
        """
        return ft.list_primitives()

    def generate_features(self, cutoff):
        """Returns a the calculated feature matrix.

        Args:
            es (featuretools.EntitySet):
                An entityset that holds data.
            cutoff (pandas.DataFrame):
                A dataframe that indicates cutoff time for each instance.

        Returns:
            pandas.DataFrame, list:
              * The generated feature matrix.
              * List of feature definitions in the feature matrix.
        """

        fm_encoded, _ = self.featurization.generate_feature_matrix(
            self.es, self.target_entity, cutoff)
        fm_encoded = fm_encoded.reset_index(drop=True)
        return fm_encoded

    def execute_model(self, feature_matrix, target, primitives,
                      optimize=False, hyperparameters=None):
        """Executes and predicts all of the pipelines.

        This method executes the given pipeline and returns a list for all the pipelines
        with the result of each fold with its associated predicted values and actual values.

        Args:
            data_frame (pandas.DataFrame or ndarray):
                A dataframe which encapsulates all the feature matrix.
            target (ndarray):
                An array of labels for the target variable.
            primitives_list (list):
                A list of the primitives within a pipeline.
            optimize (bool):
                A boolean value which indicates whether to optimize the model or not.
            hyperparameters (dict):
                A dictionary of hyperparameters for each primitive.

        Returns:
            dict:
                A dictionary for all the executed pipelines and its result.
        """

        return self.modeler.execute_pipeline(
            data_frame=feature_matrix,
            target=target,
            primitives_list=primitives,
            problem_type=self.chosen_problem.prediction_type,
            optimize=optimize,
            hyperparameters=hyperparameters
        )

    def convert_to_json(X):
        """Converts a given dictionary to json format.

        Args:
            X (dict):
                A dictionary of values to be coverted.

        Returns:
            str:
                A string in json format.
        """
        return json.dumps(X)

    def convert_from_json(X):
        """Converts a given json string to dictionary format.

        Args:
            X (str):
                A string of values to be coverted to json.

        Returns:
            dict:
                A parsed dictionary.
        """
        return json.loads(X)
