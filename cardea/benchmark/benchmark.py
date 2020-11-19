import json
import os
import logging
import pickle
import shutil
from datetime import datetime

import numpy as np
import pandas as pd
import sklearn

from mlblocks import MLPipeline
from cardea.modeling.modeler import Modeler

LOGGER = logging.getLogger(__name__)

ROOT_DIR = os.path.abspath(os.path.join(__file__, '../../../'))
PIPELINE_DIR = os.path.join(ROOT_DIR, 'cardea', 'pipelines')
VERIFIED_DIR = os.path.join(ROOT_DIR, 'benchmark', 'verified')

CLASSIFICATION_METRICS = {
    'F1 Macro': lambda *args, **kwargs: sklearn.metrics.f1_score(*args, **kwargs, average="macro"),
    'Recall': lambda *args, **kwargs: sklearn.metrics.recall_score(*args, **kwargs,
                                                                   average="macro"),
    'Precision': lambda *args, **kwargs: sklearn.metrics.precision_score(*args, **kwargs,
                                                                         average="macro"),
    'Accuracy': sklearn.metrics.accuracy_score,
    'Confusion Matrix': sklearn.metrics.confusion_matrix
}

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


def _scoring_folds(folds, metrics):
    """Score each fold from the pipeline results.
    Args:
        folds: list or dict, a list or a dictionary of pipeline results in each fold, the results
        consists of a list of prediction values and a list of label values.
        metrics: dict, a dictionary of metric functions indexed by metric names.

    Returns:
        A dictionary of aggregated scores calculated from the fold results.
    """
    if isinstance(folds, dict):
        folds = [v for k, v in folds.items()]

    performance = pd.DataFrame([{item: func(f['Actual'], f['predicted'])
                                 for item, func in metrics.items()} for f in folds])
    scores = performance.mean().to_dict()

    return scores


def aggregate_results_by_pipeline(performance, metric, record_time=True, output_path=None):
    """Aggregate the results of each pipeline.

    Args:
        performance: pd.DataFrame, the performance of each pipeline execution.
        metric: str, the name of the target metric for summary.
        record_time: boolean, whether to the record the elapsed time in the summary.
        output_path: str, the path to store the results.

    Returns:
        A pd.DataFrame object that stores the aggregated performance of each pipeline on
        each problem.
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
    """Aggregate the results on each problem (dataset).

    Args:
        performance: pd.DataFrame, the performance of each pipeline execution.
        metric: str, the name of the target metric for summary.
        record_time: boolean, whether to the record the elapsed time in the summary.
        output_path: str, the path to store the results.

    Returns:
        A pd.DataFrame object that stores the aggregated performance on each problem.
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


def benchmark(tasks, metrics=None, results_output_path=None, tasks_output_dir=None,
              save_model=True, save_intermedia_data=True, save_hyperparameters=True):
    """
    Args:
        tasks: list, a list of task instances storing meta information of each task.
        metrics: dict, a dictionary of metric functions indexed by metric names.
        results_output_path: str, the csv file path to store the benchmarking results.
        tasks_output_dir: dirt, the dir path to store the intermedia data, model and
            hyperparametes of each task.
        save_intermedia_data: boolean, whether to store the intermedia data including an entity set
            and a feature matrix if the beginning stage is "data_loader" or "problem_definition".
        save_model: boolean, whether to store the trained model.
        save_hyperparameters: boolean, whether to store the hyperparameters if task.tuned is true.

    Returns:
        A pd.DataFrame object that stores the benchmarking results in detail.
    """
    if tasks_output_dir is not None:
        if os.path.exists(tasks_output_dir):
            shutil.rmtree(tasks_output_dir)
        os.mkdir(tasks_output_dir)

    performance = []
    for task in tasks:
        if tasks_output_dir is not None:
            if not os.path.exists(tasks_output_dir):
                os.mkdir(tasks_output_dir)
            output_path = os.path.join(tasks_output_dir, task.task_id)
        else:
            output_path = None
        performance.extend(evaluate_task(task=task, metrics=metrics, output_path=output_path,
                                         save_model=save_model,
                                         save_intermedia_data=save_intermedia_data,
                                         save_hyperparameters=save_hyperparameters))
    result_df = pd.DataFrame.from_records(performance)

    if results_output_path is not None:
        result_df.to_csv(results_output_path)

    return result_df


def evaluate_task(task, metrics=None, output_path=None, save_intermedia_data=True,
                  save_model=True, save_hyperparameters=True):
    """
    Args:
        task: Task, a task instance storing meta information of the task.
        metrics: dict, a dictionary of metric functions indexed by metric names.
        output_path: str, a dir path to store the intermedia data, model and hyperparametes.
        save_intermedia_data: boolean, whether to store the intermedia data including an entity set
            and a feature matrix if the beginning stage is "data_loader" or "problem_definition".
        save_model: boolean, whether to store the trained model.
        save_hyperparameters: boolean, whether to store the hyperparameters if task.tuned is true.

    Returns:
        A list of benchmarking results of each run.
    """
    if metrics is None:
        metrics = CLASSIFICATION_METRICS

    # Load pipeline.
    with open(task.path_to_pipeline) as f:
        pipeline = MLPipeline.from_dict(json.load(f))

    # Set hyperparameters.
    if task.init_hyperparameters is not None:
        pipeline.set_hyperparameters(task.init_hyperparameters)

    # Load Dataset.
    if task.beginning_stage == "data_loader":
        raise NotImplementedError

    elif task.beginning_stage == "problem_definition":
        raise NotImplementedError

    elif task.beginning_stage == "featurization":
        feature_matrix = pd.read_csv(task.path_to_dataset, index_col=0)

    else:
        raise ValueError("Beginning stage should be either \"data_loader\", "
                         "\"problem_definition\" or \"featurization\".")

    # Run the pipeline for #task.run_num times and record each run.
    results = []
    records = []  # Records include (pipeline models (pickle), hyperparameters) of each run.
    for i in range(task.run_num):
        scores, models, hyperparameters = _evaluate_pipeline(i, pipeline, feature_matrix,
                                                             task.pipeline_name,
                                                             task.problem_name,
                                                             task.dataset_name,
                                                             task.beginning_stage,
                                                             task.tuned, metrics)
        results.append(scores)
        records.append((models, hyperparameters))

    # Store the output results.
    if output_path is not None:
        # Ensure that the output directory exists.
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        # Save task meta information
        task.save_as(os.path.join(output_path, "meta.json"), "json")
        matrix = 'F1 Macro'
        best_index = np.argmax([scores[matrix] for scores in results])
        best_record = records[best_index]

        # Save pipeline models if required
        if save_model:
            model_path = os.path.join(output_path, "models")
            if not os.path.exists(model_path):
                os.mkdir(model_path)
            for fold_name, model in best_record[0].items():
                with open(os.path.join(model_path, "{}_model.pkl".format(fold_name)), 'wb') as f:
                    f.write(model)

        # Save pipeline hyperparameters if required
        if save_hyperparameters:
            with open(os.path.join(output_path, "hyperparameters.pkl"), 'wb') as f:
                pickle.dump(best_record[1], f)

    return results


def _evaluate_pipeline(run_id, pipeline, feature_matrix, pipeline_name, problem_name,
                       dataset_name, beginning_stage, optimize=False, metrics=None):
    """Evaluate a pipeline's performance on a target dataset with the given metrics.

    Args:
        run_id: int, the index to specify the execution to the pipeline.
        pipeline: MLPipeline, a pipeline instance.
        feature_matrix: pd.DataFrame, a dataframe consists of both feature values
            and target values.
        pipeline_name: str, the name of the pipeline.
        problem_name: str, the name of the problem.
        dataset_name: str, the name of the dataset.
        beginning_stage: enumerate, the stage in which the benchmarking are applied, should be
            either "data_loader", "problem_definition", "featurization".
        optimize: boolean, whether to optimize the hyper-parameters of the pipeline.
        metrics: dict, a dictionary in which metric functions are indexed by names.

    Returns:
        A tuple includes performance stored in a dictionary, a pipeline model,
            and hyperparameters.
    """
    features = feature_matrix.copy()
    features = features.sample(3000).reset_index(drop=True)
    if problem_name.lower() in features.columns:
        features.pop(problem_name.lower())
    target = features.pop(TARGET_NAME[problem_name])

    if problem_name == 'LOS' and dataset_name == 'mimic-iii':
        target = np.digitize(target, [0, 7])

    if metrics is None:
        metrics = CLASSIFICATION_METRICS

    modeler = Modeler()

    LOGGER.info("Starting pipeline {} for {} problem..".format(pipeline_name, problem_name))

    start = datetime.utcnow()
    try:
        pipelines_res = modeler.execute_pipeline_from_pipeline(features, target, [pipeline],
                                                               PROBLEM_TYPE[problem_name],
                                                               optimize=optimize,
                                                               minimize_cost=False, scoring='f1',
                                                               max_evals=10)
        elapsed = datetime.utcnow() - start
        hyperparameters = pipelines_res['pipeline0'].get('hyperparameter', None)
        models = {fold_name: fold['pipeline']
                  for fold_name, fold in pipelines_res['pipeline0']['folds'].items()}
        scores = _scoring_folds(pipelines_res['pipeline0']['folds'], metrics)
        scores['Elapsed Time(s)'] = elapsed.total_seconds()
        scores['Status'] = 'OK'

    except Exception as ex:
        LOGGER.exception(
            "Exception scoring pipeline {} in problem {}, exception {}".format(pipeline_name,
                                                                               problem_name, ex))
        elapsed = datetime.utcnow() - start
        hyperparameters = None
        models = None
        scores = {
            name: 0 for name in metrics.keys()
        }
        scores['Elapsed Time(s)'] = elapsed.total_seconds()
        scores['Status'] = 'Fail'

    scores['Pipeline Name'] = pipeline_name
    scores['Run #'] = run_id
    scores['Problem Name'] = problem_name
    scores['Dataset Name'] = dataset_name
    scores['Beginning Stage'] = beginning_stage
    scores['Tuned'] = optimize

    return scores, models, hyperparameters
