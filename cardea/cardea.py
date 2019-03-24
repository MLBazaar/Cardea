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

        Attributes:
            es_loader: An entityset loader.
            featurization: A featurization class.
            modeler: A modeling class.
            problems: A list of currently available prediction problems.
            chosen_problem: The selected prediction problem or regression which is acquired from the chosen problem.
            es: The loaded entityset.
            target_entity: The target entity in which the problem defines the entity of interest for the featurization.
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

            Args:
                folder_path: A directory of all .csv files that should be loaded. If empty the method will automatically load kaggle's missed appointment dataset.

            Returns:
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
                A set of the available problems.
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

            Update the select_problem attribute and generate the cutoff times, the target entity and update the entityset.

            Args:
                selection: Name of the chosen prediction problem.
                data: Entityset representation of the data.
                parameters: A variable to change the default parameters, if any.

            Returns:
                The updated version of the entityset and cutoff time label of the prediction problem.
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
                A pandas dataframe that lists and describes each built-in primitive in Featuretools.
            """
        return ft.list_primitives()

    def generate_features(self, cutoff):
        """Returns a the calculated feature matrix.

            Args:
                es: A featuretools entityset that holds data.
                cutoff: A pandas dataframe that indicates cutoff_time for each instance.

            Returns:
                Encoded feature_matrix, encoded features.
            """

        fm_encoded, _ = self.featurization.generate_feature_matrix(
            self.es, self.target_entity, cutoff)
        fm_encoded = fm_encoded.reset_index(drop=True)
        return fm_encoded

    def execute_model(self, feature_matrix, target, primitives,
                      optimize=False, hyperparameters=None):
        """Executes and predict all the pipelines.

            Args:
                data_frame: A dataframe, which encapsulates all the records of that entity.
                primitives_list: A list of the primitives within a pipeline.
                optimize: A boolean value which indicates whether to optimize the model or not.
                hyperparameters: A dictionary of hyperparameters for each primitives.

            Returns:
                A list for all the pipelines which consists of, the fold number and the used pipeline and an array of the predicted values and an array of the actual values.
            """

        return self.modeler.execute_pipeline(
            data_frame=feature_matrix,
            target=target,
            primitives_list=primitives,
            problem_type=self.chosen_problem.prediction_type,
            optimize=False,
            hyperparameters=None
        )

    def convert_to_json(dic):
        """Converts a given dictionary to json format.

            Args:
                dict: A dictionary of values to be coverted.

            Returns:
                A string in json format.
            """
        return json.dumps(dic)

    def convert_from_json(string):
        """Converts a given json string to dictionary format.

            Args:
                json: A dictionary of values to be coverted.

            Returns:
                A parsed dictionary.
            """
        return json.loads(string)
