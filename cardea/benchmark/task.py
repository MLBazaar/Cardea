import json
import os
import pickle
import shutil

PIPELINES = ['Logistic Regression', 'K-Nearest Neightbors', 'Random Forest',
             'Gaussian Naive Bayes', 'Multinomial Naive Bayes', 'XGB',
             'Stochastic Gradient Descent', 'Gradient Boosting']

PROBLEMS = ['LOS', 'Mortality', 'Readmission']

# relative paths from the project root path to the target directories
PIPELINE_DIR = './cardea/pipelines'
VERIFIED_DIR = './benchmark/verified'


class Task:
    """A class that stores the configurations to a prediction task."""

    def __init__(self, task_id=None, pipeline_name=None, path_to_pipeline=None,
                 beginning_stage=None, dataset_name=None, problem_name=None, path_to_dataset=None,
                 path_to_hyperparameters=None, tuned=None, run_num=None, ):
        """Create a task configuration object from a list of settings.

        Args:
            task_id (str):
                an identifier to the task.
            pipeline_name (str):
                the name to identify the pipeline, e.g., Logistic Regression.
            path_to_pipeline (str):
                the path where the pipeline .json file is stored
            beginning_stage (str):
                the stage in which the benchmarking are applied, should be either "data_loader",
                "problem_definition", "featurization".
            dataset_name (str):
                the name to identify the dataset, e.g., mimic-iii.
            problem_name (str):
                the name to identify the problem, e.g., Readmission.
            path_to_dataset (str):
                the path where the dataset is stored.
            path_to_hyperparameters (str):
                the path where the initial hyperparameters is stored.
            tuned (boolean):
                whether the hyperparameters will be tuned
            run_num (int):
                the number of runs for each pipeline on each problem.
        """
        self._task_id = task_id
        self._pipeline_name = pipeline_name
        self._beginning_stage = beginning_stage
        self._dataset_name = dataset_name
        self._problem_name = problem_name
        self._path_to_dataset = path_to_dataset
        self._path_to_pipeline = path_to_pipeline
        self._path_to_hyperparameters = path_to_hyperparameters
        self._tuned = tuned
        self._run_num = run_num

    def __str__(self):
        description_str = ""
        ordered_items = list(sorted(self.__dict__.items(), key=lambda x: x[0]))
        for k, v in ordered_items:
            description_str += "{:<20} {}\n".format(k, v)
        return description_str

    def __repr__(self):
        description_str = ""
        ordered_items = list(sorted(self.__dict__.items(), key=lambda x: x[0]))
        for k, v in ordered_items:
            description_str += "{:<20} {}\n".format(k, v)
        return description_str

    def save_as(self, file_path):
        """Save the task configurations to the given address.

        Args:
            file_path (str):
                the path to store the configurations.
        """
        _, file_type = os.path.splitext(file_path)
        if file_type == '.pkl':
            with open(file_path, 'wb') as f:
                pickle.dump(self, f)
        elif file_type == '.json':
            with open(file_path, 'w') as f:
                json.dump(self.__dict__, f)
        else:
            raise ValueError("file_type should be either \"pkl\" or \"json\"")

    @staticmethod
    def load(file_path):
        with open(file_path, 'f') as f:
            attr_dict = json.load(f)
        return Task(**attr_dict)

    @property
    def task_id(self):
        return self._task_id

    @property
    def pipeline_name(self):
        return self._pipeline_name

    @property
    def dataset_name(self):
        return self._dataset_name

    @property
    def problem_name(self):
        return self._problem_name

    @property
    def beginning_stage(self):
        return self._beginning_stage

    @property
    def path_to_pipeline(self):
        return self._path_to_pipeline

    @path_to_pipeline.setter
    def path_to_pipeline(self, path_to_pipeline):
        self._path_to_pipeline = path_to_pipeline

    @property
    def path_to_dataset(self):
        return self._path_to_dataset

    @path_to_dataset.setter
    def path_to_dataset(self, path_to_dataset):
        self._path_to_dataset = path_to_dataset

    @property
    def path_to_hyperparameters(self):
        return self._path_to_hyperparameters

    @path_to_hyperparameters.setter
    def path_to_hyperparameters(self, path_to_hyperparameters):
        self._path_to_hyperparameters = path_to_hyperparameters

    @property
    def tuned(self):
        return self._tuned

    @property
    def run_num(self):
        return self._run_num


def create_tasks(pipeline_names=None, problem_names=None, dataset_name='mimic-iii',
                 beginning_stage='data_loader', optimize=False, run_num=1, output_dir=None):
    """Create a list of task configurations from settings.

    Args:
        pipeline_names (list):
            name of the pipelines for testing.
        problem_names (list):
            name of the problems to be tested on.
        dataset_name (str) :
            name of the dataset to be tested on.
        beginning_stage (str):
            the stage in which the benchmarking are applied, should be either "data_loader",
            "problem_definition", "featurization".
        optimize (boolean):
            whether to optimize the hyper-parameters of the pipeline.
        run_num (int):
            the number of runs for each pipeline on each problem.
        output_dir (str):
            the path to store the task configurations.

    Returns:
        list:
            a list of Task objects that store the task configurations.
    """
    if pipeline_names is None:
        pipeline_names = PIPELINES
    pipeline_names = sorted(pipeline_names)

    if problem_names is None:
        problem_names = PROBLEMS
    problem_names = sorted(problem_names)

    task_num = 0
    tasks = []
    for problem in problem_names:
        for pipeline in pipeline_names:
            task_id = "{}_{}_{}".format(task_num, problem, pipeline)
            task = Task(task_id=task_id, pipeline_name=pipeline, dataset_name=dataset_name,
                        problem_name=problem, beginning_stage=beginning_stage,
                        run_num=run_num, tuned=optimize)
            task.path_to_pipeline = os.path.join(PIPELINE_DIR,
                                                 '{}.json'.format(task.pipeline_name))
            if beginning_stage == 'data_loader':
                task.path_to_dataset = os.path.join(VERIFIED_DIR, 'Raw', task.dataset_name)
            elif beginning_stage == 'problem_definition':
                task.path_to_dataset = os.path.join(VERIFIED_DIR, 'EntitySet',
                                                    '{}.pkl'.format(task.dataset_name))
            elif beginning_stage == 'featurization':
                task.path_to_dataset = os.path.join(VERIFIED_DIR, 'Problems', task.problem_name,
                                                    'FeatureMatrix',
                                                    '{}.csv'.format(task.dataset_name))
            tasks.append(task)
            task_num += 1

    if output_dir is not None:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        for task in tasks:
            task_path = os.path.join(output_dir, task.task_id)
            if os.path.exists(task_path):
                shutil.rmtree(task_path)
            os.mkdir(task_path)
            task.save_as(os.path.join(task_path, 'meta.json', 'json'))

    return tasks
