import json
import logging
import os
import pickle
import shutil
from datetime import datetime
from os.path import dirname

import numpy as np
import pandas as pd
from mlblocks import MLPipeline

from cardea.modeling.modeler import Modeler

LOGGER = logging.getLogger(__name__)

ROOT_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))

PROBLEM_TYPE = {
    'LOS': 'classification',
    'Mortality': 'classification',
    'Readmission': 'classification',
}

TARGET_NAME = {
    'LOS': 'label',
    'Mortality': 'label',
    'Readmission': 'label',
}


def _split_features_target(feature_matrix, problem_name):
    """Split the features and labels.

    Args:
        feature_matrix (pd.DataFrame):
            a dataframe consists of both feature values and target values.
        problem_name (str):
            the name of the problem.

    Returns:
        tuple:
            features (pd.DataFrame) and target (pd.Series).
    """
    features = feature_matrix.copy().reset_index(drop=True)

    if problem_name.lower() in features.columns:
        features.pop(problem_name.lower())

    target = features.pop(TARGET_NAME[problem_name])
    features = features
    return features, target


def aggregate_results_by_pipeline(performance, metric, record_time=True, output_path=None):
    """Aggregate the results of each pipeline.

    Args:
        performance (pd.DataFrame):
            the performance of each pipeline execution.
        metric (str):
            the name of the target metric for summary.
        record_time (boolean):
            whether to the record the elapsed time in the summary.
        output_path (str):
            the path to store the results.

    Returns:
        pd.DataFrame:
            aggregated performance of each pipeline on each problem.
    """
    if 'Status' in performance.columns:
        performance = performance[performance['Status'] == 'OK']

    problems = performance['Problem Name'].unique()
    pipelines = performance['Pipeline Name'].unique()

    aggr_results = []
    for problem in problems:
        problem_dict = {}
        for pipeline in pipelines:
            runs = _select_runs(performance, problem, pipeline)
            problem_dict["{}_Average {}".format(pipeline, metric)] = runs[metric].mean()
            problem_dict["{}_Best {}".format(pipeline, metric)] = runs[metric].max()
            if record_time:
                problem_dict["{}_Average Elapsed Time(s)".format(pipeline)] = \
                    runs["Elapsed Time(s)"].mean()
        aggr_results.append(problem_dict)
    aggr_df = pd.DataFrame(aggr_results, index=problems)
    aggr_df.columns = aggr_df.columns.str.split('_', expand=True)

    if output_path:
        aggr_df.to_csv(output_path)

    return aggr_df


def aggregate_results_by_problem(performance, metric, record_time=True, output_path=None):
    """Aggregate the results on each problem.

    Args:
        performance (pd.DataFrame):
            the performance of each pipeline execution.
        metric (str):
            the name of the target metric for summary.
        record_time (boolean):
            whether to the record the elapsed time in the summary.
        output_path (str):
            the path to store the results.

    Returns:
        pd.DataFrame:
            aggregated performance on each problem.
    """
    if 'Status' in performance.columns:
        performance = performance[performance['Status'] == 'OK']

    problems = performance['Problem Name'].unique()
    aggr_results = []
    for problem in problems:
        runs = _select_runs(performance, problem)
        problem_dict = {
            "Average {}".format(metric): runs[metric].mean(),
            "Best {}".format(metric): runs[metric].max(),
            "Best Pipeline": runs.loc[runs[metric].idxmax(), 'Pipeline Name']
        }
        if record_time:
            problem_dict["Average Elapsed Time(s)"] = runs["Elapsed Time(s)"].mean()
        aggr_results.append(problem_dict)
    aggr_df = pd.DataFrame(aggr_results, index=problems)

    if output_path:
        aggr_df.to_csv(output_path)

    return aggr_df


def _select_runs(df, problem=None, pipeline=None):
    if isinstance(problem, str):
        df = df[df['Problem Name'] == problem]
    if isinstance(pipeline, str):
        df = df[df['Pipeline Name'] == pipeline]
    return df


def benchmark(tasks, metrics=None, output_path=None, save_results=True,
              save_model=True, save_intermedia_data=True, save_hyperparameters=True):
    """Run benchmark testing on a set of tasks. Return detailed results of each run stored in a
    DataFrame object.

    Args:
        tasks (list):
            a list of task instances storing meta information of each task.
        metrics (list)
            a list of strings to identify the metric functions.
        output_path (str):
            the dir path to store benchmark results and records of each task.
        save_results (boolean):
            whether to store the benchmark results.
        save_intermedia_data (boolean):
            whether to store the intermedia data including an entity set and a feature matrix if
            the beginning stage is "data_loader" or "problem_definition".
        save_model (boolean):
            whether to store the trained model.
        save_hyperparameters (boolean):
            whether to store the hyperparameters if task.tuned is true.

    Returns:
        pd.DataFrame:
            benchmarking results in detail.
    """
    if output_path is not None:
        if not os.path.exists(output_path):
            os.mkdir(output_path)

    performance = []
    for task in tasks:
        if output_path is not None:
            task_output_path = os.path.join(output_path, task.task_id)
        else:
            task_output_path = None
        performance.extend(evaluate_task(task=task, metrics=metrics, output_path=task_output_path,
                                         save_model=save_model,
                                         save_intermedia_data=save_intermedia_data,
                                         save_hyperparameters=save_hyperparameters))
    result_df = pd.DataFrame.from_records(performance)

    if output_path is not None and save_results:
        result_df.to_csv(os.path.join(output_path, 'details.csv'))

    return result_df


def evaluate_task(task, metrics=None, feature_matrix=None, output_path=None,
                  save_intermedia_data=True, save_model=True, save_hyperparameters=True):
    """Run benchmark testing on a task. Save intermedia data, trained models, and optimized
    hyperparameters. Return testing results.

    Args:
        task (Task):
            a task instance storing meta information of the task.
        metrics (list)
            a list of strings to identify the metric functions.
        feature_matrix (pd.DataFrame):
            a dataframe consists of both feature values and target values.
        output_path (str):
            a directory path to store the intermedia data, model and hyperparametes.
        save_intermedia_data (boolean):
            whether to store the intermedia data including an entity set and a feature matrix if
            the beginning stage is "data_loader" or "problem_definition".
        save_model (boolean):
            whether to store the trained model.
        save_hyperparameters (boolean):
            whether to store the hyperparameters if task.tuned is true.

    Returns:
        list:
            benchmarking results of each run.
    """
    # Load pipeline.
    pipeline = MLPipeline.load(os.path.join(ROOT_DIR, task.path_to_pipeline))

    # Set hyperparameters.
    if task.path_to_hyperparameters is not None:
        _, extension = os.path.splitext(task.path_to_hyperparameters)
        with open(os.path.join(ROOT_DIR, task.path_to_hyperparameters)) as f:
            if extension == '.json':
                init_hyperparameters = json.load(f)
            elif extension == '.pkl':
                init_hyperparameters = pickle.load(f)
            else:
                raise TypeError("Unsupported file type {}.".format(extension))
        pipeline.set_hyperparameters(init_hyperparameters)

    # Load Dataset.
    if feature_matrix is None:
        if task.beginning_stage == "data_loader":
            raise NotImplementedError

        elif task.beginning_stage == "problem_definition":
            raise NotImplementedError

        elif task.beginning_stage == "featurization":
            feature_matrix = pd.read_csv(os.path.join(ROOT_DIR, task.path_to_dataset), index_col=0)

    else:
        raise ValueError("Beginning stage should be either \"data_loader\", "
                         "\"problem_definition\" or \"featurization\".")

    # Run the pipeline for #task.run_num times and record each run.
    results = []
    records = []
    for i in range(task.run_num):
        scores, model, hyperparameters = _evaluate_pipeline(i, pipeline, feature_matrix,
                                                            task.pipeline_name,
                                                            task.problem_name,
                                                            task.dataset_name,
                                                            task.beginning_stage,
                                                            task.tuned, metrics)
        results.append(scores)
        records.append((model, hyperparameters))

    # Store the output results.
    if output_path is not None:
        # Initialize the output directory.
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.mkdir(output_path)

        # Save task meta information
        task.save_as(os.path.join(output_path, "meta.json"))
        matrix = 'F1 Macro'
        best_index = np.argmax([scores[matrix] for scores in results])
        models, hyperparameters = records[best_index]

        # Save pipeline models if required
        if save_model:
            with open(os.path.join(output_path, "model.pkl"), 'wb') as f:
                pickle.dump(models, f)

        # Save pipeline hyperparameters if required
        if save_hyperparameters and hyperparameters is not None:
            with open(os.path.join(output_path, "hyperparameters.pkl"), 'wb') as f:
                pickle.dump(hyperparameters, f)

    return results


def _evaluate_pipeline(run_id, pipeline, feature_matrix, pipeline_name=None, problem_name=None,
                       dataset_name=None, beginning_stage=None, optimize=False, metrics=None):
    """Evaluate a pipeline's performance on a target dataset according to the given metrics.

    Args:
        run_id (int):
            the index to specify the execution to the pipeline.
        pipeline (MLPipeline):
            a pipeline instance.
        feature_matrix (pd.DataFrame):
            a dataframe consists of both feature values and target values.
        pipeline_name (str):
            the name of the pipeline.
        problem_name (str):
            the name of the problem.
        dataset_name (str):
            the name of the dataset.
        beginning_stage (str):
            the stage in which the benchmarking are applied, should be either "data_loader",
            "problem_definition", "featurization".
        optimize (boolean):
            whether to optimize the hyper-parameters of the pipeline.
        metrics (list)
            a list of strings to identify the metric functions.

    Returns:
        tuple:
            pipeline evaluation results including (performance, models, hyperparameters).
    """
    modeler = Modeler(pipeline, PROBLEM_TYPE[problem_name])

    features, target = _split_features_target(feature_matrix, problem_name)
    # TODO: digitize the labels in the featurization (problem definition) stage.
    if problem_name == 'LOS' and dataset_name == 'mimic-iii':
        target = np.digitize(target, [0, 7])

    LOGGER.info("Starting pipeline {} for {} problem..".format(pipeline_name, problem_name))

    start = datetime.utcnow()
    try:
        scores = modeler.evaluate(features, target,
                                  tune=optimize, scoring='F1 Macro', metrics=metrics, max_evals=10)
        elapsed = datetime.utcnow() - start
        model = modeler.pipeline
        hyperparameters = modeler.pipeline.get_hyperparameters() if optimize else None
        scores['Elapsed Time(s)'] = elapsed.total_seconds()
        scores['Status'] = 'OK'

    except Exception as ex:
        LOGGER.exception(
            "Exception scoring pipeline {} in problem {}, exception {}".format(pipeline_name,
                                                                               problem_name, ex))
        elapsed = datetime.utcnow() - start
        model = None
        hyperparameters = None
        scores = {'Elapsed Time(s)': elapsed.total_seconds(), 'Status': 'Fail'}

    scores['Pipeline Name'] = pipeline_name
    scores['Run #'] = run_id
    scores['Problem Name'] = problem_name
    scores['Dataset Name'] = dataset_name
    scores['Beginning Stage'] = beginning_stage
    scores['Tuned'] = optimize

    return scores, model, hyperparameters
