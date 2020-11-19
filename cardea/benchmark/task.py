import json
import os
import pickle
import shutil
import logging

from collections import OrderedDict

PIPELINES = ['Logistic Regression', 'K-Nearest Neightbors', 'Random Forest',
             'Gaussian Naive Bayes', 'Multinomial Naive Bayes', 'XGB',
             'Stochastic Gradient Descent', 'Gradient Boosting']

PROBLEMS = ['LOS', 'Mortality', 'Readmission']

ROOT_DIR = os.path.abspath(os.path.join(__file__, '../../../'))
PIPELINE_DIR = os.path.join(ROOT_DIR, 'cardea', 'pipelines')
VERIFIED_DIR = os.path.join(ROOT_DIR, 'benchmark', 'verified')


class Task:
    def __init__(self, task_id=None, pipeline_name=None, path_to_pipeline=None,
                 beginning_stage=None, dataset_name=None, problem_name=None, path_to_dataset=None,
                 init_hyperparameters=None, tuned=None, run_num=None, ):
        self._task_id = task_id
        self._pipeline_name = pipeline_name
        self._beginning_stage = beginning_stage
        self._dataset_name = dataset_name
        self._problem_name = problem_name
        self._path_to_dataset = path_to_dataset
        self._path_to_pipeline = path_to_pipeline
        self._init_hyperparameters = init_hyperparameters
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

    def save_as(self, file_path, file_type='pkl'):
        if file_type == 'pkl':
            with open(file_path, 'wb') as f:
                pickle.dump(self, f)
        elif file_type == 'json':
            with open(file_path, 'w') as f:
                json.dump(self.__dict__, f)
        else:
            raise NotImplementedError

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
    def init_hyperparameters(self):
        return self._init_hyperparameters

    @init_hyperparameters.setter
    def init_hyperparameters(self, init_hyperparameters):
        self._init_hyperparameters = init_hyperparameters

    def load_hyperparameters(self, path_to_hyperparameters):
        with open(path_to_hyperparameters, 'r') as f:
            self._init_hyperparameters = json.load(f)

    @property
    def tuned(self):
        return self._tuned

    @property
    def run_num(self):
        return self._run_num


def create_tasks(pipeline_names=None, problem_names=None, dataset_name='MIMIC-III',
                 beginning_stage='data_loader', optimize=False, run_num=1, output_dir=None):
    """
    Args:
        pipeline_names: list, a list of strings that verify the pipelines for testing.
        problem_names: list, a list of strings that verify the problems to be tested on.
        dataset_name: str, name of the dataset.
        beginning_stage: enumerate, the stage in which the benchmarking are applied, should be
            either "data_loader", "problem_definition", "featurization".
        optimize: boolean, whether to optimize the hyper-parameters of the pipeline.
        run_num: int, the number of executions to each pipeline on each problem.
        output_dir: str, the path to store the task configurations.

    Returns:
        a list of Task objects that store the configurations of the tasks.
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
                                                    '.pkl'.format(task.dataset_name))
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
            os.mkdir(task_path)
            task.save_as(os.path.join(task_path, 'meta.json', 'json'))

    return tasks
