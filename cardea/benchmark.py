import logging
from datetime import datetime

import numpy as np
import pandas as pd
import sklearn

from cardea.modeling.modeler import Modeler

LOGGER = logging.getLogger(__name__)

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


def _split_feature_label(dataset, target_name):
    """Split the feature array and the target array.

    Args:
        dataset: pd.DataFrame, a dataframe consists of both feature values and target values.
        target_name: str, the name of the target column in the dataset.

    Returns:
        features: 2-D np.array, the feature array.
        target: 1-D np.array, the target array.
    """
    dataset = dataset.copy(deep=True)
    target = np.array(dataset.pop(target_name))
    features = np.array(dataset)
    return features, target


def _evaluate_pipeline(name, run_id, primitives, dataset, problem, hyperparameters=None,
                       optimize=False, metrics=None):
    """Evaluate a pipeline's performance on a target dataset with the given metrics.

    Args:
        name: str, the name to specify the pipeline.
        run_id: int, the index to specify the execution to the pipeline.
        primitives: list, A list of the primitives within a pipeline.
        dataset: pd.DataFrame, a dataframe consists of both feature values and target values.
        problem: str, the name to specify the problem.
        hyperparameters: dict, A dictionary of hyper-parameters for each primitive.
        optimize: boolean, whether to optimize the hyper-parameters of the pipeline.
        metrics: dict, a dictionary in which metric functions are indexed by names.

    Returns:
        scores: dict, keys include "Pipeline", "Problem", "Tuned", "Elapsed Time(s)", "Status",
            and metric names.
    """
    features, target = _split_feature_label(dataset, TARGET_NAME[problem])
    if metrics is None:
        metrics = CLASSIFICATION_METRICS
    modeler = Modeler()

    LOGGER.info("Starting pipeline {} for {} problem..".format(name, problem))

    start = datetime.utcnow()
    try:
        pipelines_res = modeler.execute_pipeline(np.array(features).astype(np.float),
                                                 np.array(target).astype(np.float),
                                                 [primitives], PROBLEM_TYPE[problem],
                                                 optimize=optimize,
                                                 hyperparameters=hyperparameters,
                                                 minimize_cost=False, scoring='f1',
                                                 max_evals=10)
        elapsed = datetime.utcnow() - start
        scores = _scoring_folds(pipelines_res['pipeline0']['folds'], metrics)
        scores['Elapsed Time(s)'] = elapsed.total_seconds()
        scores['Status'] = 'OK'

    except Exception as ex:
        LOGGER.exception(
            "Exception scoring pipeline {} in problem {}, exception {}".format(name, problem, ex))
        elapsed = datetime.utcnow() - start
        scores = {
            name: 0 for name in metrics.keys()
        }
        scores['Elapsed Time(s)'] = elapsed.total_seconds()
        scores['Status'] = 'Fail'

    scores['Pipeline'] = name
    scores['Run #'] = run_id
    scores['Problem'] = problem
    scores['Tuned'] = optimize or hyperparameters is not None

    return scores


def _evaluate_pipelines(pipelines, dataset, problem, hyperparameters=None, optimize=False,
                        metrics=None, runs=1):
    """Evaluate pipelines on a dataset with given metrics.

    Args:
        pipelines: list or dict, a list or a dictionary of the pipelines.
        dataset: pd.DataFrame, a dataframe consists of both feature values and target values.
        problem: str, the name to specify the problem.
        hyperparameters: list or dict, a list or a dictionary of hyper-parameters for each
        pipeline.
        optimize: boolean, whether to optimize the hyper-parameters of the pipelines.
        metrics: dict, a dict in which metric functions are indexed by the metric names.
        runs: int, the number of executions to each pipeline.

    Returns:
        A list of pipeline performance dicts.
    """
    if metrics is None:
        metrics = CLASSIFICATION_METRICS

    if isinstance(pipelines, list):
        pipelines = {"pipeline_{}".format(i): pipeline for i, pipeline in enumerate(pipelines)}

    if hyperparameters is None:
        hyperparameters = {k: None for k in pipelines.keys()}
    elif isinstance(hyperparameters, list):
        hyperparameters = {"pipeline_{}".format(i): hyper for i, hyper in
                           enumerate(hyperparameters)}
    performance = []
    for name, pipeline in pipelines.items():
        for run_id in range(runs):
            performance.append(_evaluate_pipeline(name, run_id, pipeline, dataset, problem,
                                                  hyperparameters[name], optimize, metrics))

    return performance


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

    problems = performance['Problem'].unique()
    pipelines = performance['Pipeline'].unique()

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

    problems = performance['Problem'].unique()
    aggr_results = []
    for problem in problems:
        runs = _select_runs(performance, problem)
        problem_dict = {
            "Average {}".format(metric): runs[metric].mean(),
            "Best {}".format(metric): runs[metric].max(),
            "Best Pipeline": runs.loc[runs[metric].idxmax(), 'Pipeline']
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
        df = df[df['Problem'] == problem]
    if isinstance(pipeline, str):
        df = df[df['Pipeline'] == pipeline]
    return df


def benchmark(pipelines, datasets, problems=None, hyperparameters=None, optimize=False,
              metrics=None, runs=1, stage='data_loader', output_path=None):
    """Evaluate pipelines on a set of datasets (problems) with given metrics.

    Args:
        pipelines: list or dict, a list or a dictionary of pipelines.
        datasets: str or dict,
            * str, path to the data folder when the stage is "data_loader" or 0;
            * str, path to the entity pickle file when the stage is "problem_definition" or 1;
            * dict, a dictionary in which feature matrices (pd.DataFrame) are indexed by a problem
            name when the stage is "featurization" or 2.
        problems: list, a list of problem names (str).
        hyperparameters: list or dict, a list or a dictionary of hyper-parameters for each
        pipeline.
        optimize: boolean, whether to optimize the hyper-parameters of the pipeline.
        metrics: dict, a dictionary in which metric functions are indexed by the metric names.
        runs: int, the number of executions to each pipeline on each problem.
        stage: enumerate (int or str), the stage in which the benchmarking are applied, should be
            either "data_loader", "problem_definition", "featurization", or an index (int).
            0 is for "data_loader", 1 is for "problem_definition", 2 is for "featurization".
        output_path: str, the path to store the results.

    Returns:
        A pd.DataFrame object that stores the performance of each pipeline execution.
    """
    if metrics is None:
        metrics = CLASSIFICATION_METRICS

    if stage == "data_loader" or stage == 0:
        raise NotImplementedError
    elif stage == "problem_definition" or stage == 1:
        raise NotImplementedError
    elif stage == "featurization" or stage == 2:
        feature_matrices = datasets
    else:
        raise ValueError("stage should be either \"data_loader\", \"problem_definition\" "
                         "or \"featurization\".")

    performance = []
    for problem, dataset in feature_matrices.items():
        performance.extend(_evaluate_pipelines(pipelines, dataset, problem, hyperparameters,
                                               optimize, metrics, runs))
    result_df = pd.DataFrame.from_records(performance)

    if output_path:
        result_df.to_csv(output_path)

    return result_df
