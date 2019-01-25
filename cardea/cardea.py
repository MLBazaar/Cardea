from cardea.data_loader import EntitySetLoader
from cardea.problem_definition import (LengthOfStay, MortalityPrediction, Readmission,
DiagnosisPrediction, MissedAppointmentProblemDefinition, ProlongedLengthOfStay)
from cardea.featurization import Featurization
from cardea.modeling import Modeler

class Cardea():
    """"An interface class that ties the end-to-end system together.
    
    Attributes:
        es_loader: An entityset loader.
        featurization: A featurization class.
        modeler: A modeling class.
        problems: A list of currently available prediction problems.
        chosen_problem: The selected prediction problem.
        or regression which is acquired from the chosen problem.
        target_entity: The target entity in which the problem defines the 
        entity of interest for the featurization.

    """

    def __init__(self):
        
        self.es_loader = EntitySetLoader()
        self.featurization = Featurization()
        self.modeler = Modeler()

        self.problems = ['los', 
                         'plos', 
                         'mortality', 
                         'readmission', 
                         'diagnosis', 
                         'mapp']

        self.chosen_problem = None
        self.target_entity = None

    def load_data_entityset(self, folder_path=None):
        """Returns an entityset loaded with .csv files in folder_path.

        Args:
            folder_path: A directory of all .csv files that should be loaded. If empty
            the method will automatically load kaggle's missed appointment dataset.

        Returns:
            An entityset with loaded data.
        """

        if folder_path:
            return self.es_loader.load_data_entityset(folder_path)
        
        csv_s3 = "https://s3.amazonaws.com/dai-cardea/"
        kaggle = ['Address',
                  'Appointment_Participant'
                  'Appointment',
                  'CodeableConcept',
                  'Coding',
                  'Identifier',
                  'Observation',
                  'Patient',
                  'Reference']

        fhir = {resource: pd.read_csv(csv_s3 + resource + ".zip", compression='zip') for resource in kaggle}
        return self.es_loader.load_df_entityset(fhir)

        

    def list_problems(self):
        """Returns a list of the currently available problems.

        los: Length of stay prediction problem, predicting how many days
        a patient will be in the hospital.
        plos: Prolonged length of stay prediction problem, predicting whether
        a patient stayed in the hospital more or less than a week.
        mortality: Mortality prediction problem, finding whether
        a patient will suffer from mortality.
        readmission: Readmission prediction problem, predicting whether
        a patient will revisit the hospital within certain period of time.
        diagnosis: Diagnosis prediction problem, finding whether
        a patient will be diagnosed with a specifed diagnosis.
        mapp: Missed appointment prediction problem, predicting 
        whether the patient showed to the appointment or not.
        
        Returns:
            A list of the available problems.
        """
        return self.problems
    
    def select_problem(self, data, selection, parameter=None):
        """Select a prediction problem and extract information.

        Update the select_problem attribute and generate the cutoff times,
        the target entity and update the entityset.
        
        Args:
            selection: Name of the chosen prediction problem.
            data: Entityset representation of the data.
            parameters: A variable to change the default parameters, if any.
        
        Returns:
            The updated version of the entityset and cutoff time label 
            of the prediction problem.
        """
        
        # problem selection
        if selection == 'los':
            self.chosen_problem = LengthOfStay()
            
        elif selection == 'mortality':
            self.chosen_problem = MortalityPrediction()
    
        elif selection == 'mapp':
            self.chosen_problem = MissedAppointmentProblemDefinition()
            
        elif selection == 'plos' and parameter:
            self.chosen_problem = ProlongedLengthOfStay(parameter)
            
        elif selection == 'plos':
            self.chosen_problem = ProlongedLengthOfStay()
            
        elif selection == 'readmission' and parameter:
            self.chosen_problem = Readmission(parameter)
            
        elif selection == 'readmission':
            self.chosen_problem = Readmission()
            
        elif selection == 'diagnosis' and parameter:
            self.chosen_problem = DiagnosisPrediction(parameter)
        
        elif selection == 'diagnosis':
            raise ValueError('unspecified diagnosis code')
        
        else:
            raise ValueError('{} is not a defined problem'.format(selection))
            
        # target label calculation
        es, self.target_entity, cutoff = self.select_problem.generate_cutoff_times(data)
        return es, cutoff
    
    def generate_features(self, es, cutoff):
        """Returns a the calculated feature matrix.
        
        Args:
            es: A featuretools entityset that holds data.
            cutoff: A pandas dataframe that indicates cutoff_time for each instance.
        
        Returns:
            Encoded feature_matrix, encoded features.
        """
        
        fm_encoded,_ = self.featurization.generate_feature_matrix(es, self.target_entity, cutoff)
        fm_encoded = fm_encoded.reset_index(drop=True)
        y = list(fm_encoded.pop('label'))
        return fm_encoded.values, y
    
    def execute_model(self, X, y, primitives, optimize=False, hyperparameters=None):
        '''Executes and predict all the pipelines.

        Args:
            data_frame: A dataframe, which encapsulates all the records of that entity.
            target: An array of labels for the target variable.
            primitives_list: A list of the primitives within a pipeline.
            optimize: A boolean value which indicates whether to optimize the model or not.
            hyperparameters: A dictionary of hyperparameters for each primitives.

        Returns:
            A list for all the pipelines which consists of, the fold number and the used pipeline
            and an array of the predicted values and an array of the actual values.
        '''
        return self.modeler.execute_pipeline(
            data_frame=X,
            target=y,
            primitives_list=primitives,
            problem_type=self.chosen_problem.prediction_type, 
            optimize=False, 
            hyperparameters=None
        )
        
            