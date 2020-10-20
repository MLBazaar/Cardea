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
    'los': 'classification',
    'mortality': 'classification',
    'readmission': 'classification'
}


def _scoring_folds(folds, metrics):
    """Score each fold from the pipeline results.
    Args:
        folds: dict, records from the prediction results of a fold of data.
            The keys must include "Actual" and "predicted".
        metrics: dict, keys are the name of the metrics and the values are metrics functions.

    Returns:
        scores: dict, keys are the name of the metrics and the values are scores
            from the corresponding metrics.
    """
    if isinstance(folds, dict):
        folds = [v for k, v in folds.items()]

    fold_tuples = [(f['Actual'], f['predicted']) for f in folds]
    scores = pd.DataFrame(
        [{item: func(para[0], para[1]) for item, func in metrics.items()} for para in
         fold_tuples]).mean().to_dict()

    return scores


def _split_feature_label(dataset, target_name):
    """Generate the feature array and the target array from the raw dataframe.

    Args:
        dataset: pd.DataFrame, raw dataset consists of the features and the labels.
        target_name: str, the name of the target column in the dataset.

    Returns:
        X: 2-D np.array, the feature array.
        y: 1-D np.array, the target array.
    """
    dataset = dataset.copy(deep=True)
    y = np.array(dataset.pop(target_name))
    X = np.array(dataset)
    return X, y


def _evaluate_pipeline(name, primitives, dataset, problem, hyperparameters=None, optimize=False,
                       metrics=CLASSIFICATION_METRICS, target_name='TARGET'):
    """Evalute a pipeline's performance on a dataset with given metrics

    Args:
        name: str, the name of the pipeline.
        primitives: list, a list of primitives that make up the pipeline.
        dataset: pd.DataFrame, dataset for evaluation.
        problem: str, the name of the problem
        hyperparameters: dict, the hyperparameter setting of the pipeline.
            If hyperparameters is None, the pipeline will be initialized with default values.
        optimize: boolean, whether to optimize the hyperparameters used in the pipeline.
        metrics: dict, keys are the name of the metrics and the values are metrics functions.
        target_name: str, the name of the target column in the dataset.

    Returns:
        scores: dict, keys include "Pipeline", "Problem", "Tuned", "Elapsed Time(s)", "Status",
            and metric names.
    """
    X, y = _split_feature_label(dataset, target_name)
    modeler = Modeler()

    LOGGER.info("Starting pipeline {} for {} problem..".format(name, problem))

    try:
        start = datetime.utcnow()
        pipelines_res = modeler.execute_pipeline(X, y, [primitives], PROBLEM_TYPE[problem],
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
    scores['Problem'] = problem
    scores['Tuned'] = optimize or hyperparameters is not None

    return scores


def _evaluate_pipelines(pipelines, dataset, problem, hyperparameters=None, optimize=False,
                        metrics=CLASSIFICATION_METRICS, target_name='TARGET', runs=1):
    """Evalutate pipelines on a dataset with given metrics.

    Args:
        pipelines: list, a lisf of pipelines.
        dataset: pd.DataFrame, dataset for evaluation.
        problem: str, the name of the problem
        hyperparameters: dict, the hyperparameter setting of the pipeline.
            If hyperparameters is None, the pipeline will be initialized with default values.
        optimize: boolean, whether to optimize the hyperparameters used in the pipeline.
        metrics: dict, keys are the name of the metrics and the values are metrics functions.
        target_name: str, the name of the target column in the dataset.
        runs: int, the number of runs of the each pipeline.

    Returns:
        score_list, list. A list of pipeline scores (dict).
    """
    score_list = []
    if isinstance(pipelines, list):
        pipelines = {"pipeline_{}".format(i): pipeline for i, pipeline in enumerate(pipelines)}

    if hyperparameters is None:
        hyperparameters = {k: None for k in pipelines.keys()}
    elif isinstance(hyperparameters, list):
        hyperparameters = {"pipeline_{}".format(i): hyper for i, hyper in
                           enumerate(hyperparameters)}

    for name, pipeline in pipelines.items():
        for _ in range(runs):
            score_list.append(
                _evaluate_pipeline(name, pipeline, dataset, problem, hyperparameters[name],
                                   optimize, metrics,
                                   target_name))

    return score_list


def aggregate_results_by_pipeline(df, metric):
    """Aggregate the results of each pipeline.

    Args:
        df: pd.DataFrame, the results of all runs.
        metric: str, the name of the metric for aggregation.

    Returns:
        aggr_df, pd.DataFrame, each row records the aggregated scores of all pipelines
            on a dataset (problem).
    """
    if 'Status' in df.columns:
        df = df[df['Status'] == 'OK']

    problems = df['Problem'].unique()
    pipelines = df['Pipeline'].unique()

    aggr_results = []
    for problem in problems:
        problem_dict = {}
        for pipeline in pipelines:
            runs = _select_runs(df, problem, pipeline)
            problem_dict["{}_Average {}".format(pipeline, metric)] = runs[metric].mean()
            problem_dict["{}_Best {}".format(pipeline, metric)] = runs[metric].max()
            problem_dict["{}_Average Elapsed Time(s)".format(pipeline)] = runs[
                "Elapsed Time(s)"].mean()
        aggr_results.append(problem_dict)
    aggr_df = pd.DataFrame(aggr_results, index=problems)
    aggr_df.columns = aggr_df.columns.str.split('_', expand=True)

    return aggr_df


def aggregate_results_by_problem(df, metric):
    """Aggregate the results on each problem (dataset).

    Args:
        df: pd.DataFrame, the results of all runs.
        metric: str, the name of the metric for aggregation.

    Returns:
        aggr_df, pd.DataFrame, each row records the aggregated scores on a dataset (problem).
    """
    if 'Status' in df.columns:
        df = df[df['Status'] == 'OK']

    problems = df['Problem'].unique()
    aggr_results = []
    for problem in problems:
        runs = _select_runs(df, problem)
        problem_dict = {
            "Average {}".format(metric): runs[metric].mean(),
            "Best {}".format(metric): runs[metric].max(),
            "Best Pipeline": runs.loc[runs[metric].idxmax(), 'Pipeline']
        }
        aggr_results.append(problem_dict)
    aggr_df = pd.DataFrame(aggr_results, index=problems)
    return aggr_df


def _select_runs(df, problem=None, pipeline=None):
    if isinstance(problem, str):
        df = df[df['Problem'] == problem]
    if isinstance(pipeline, str):
        df = df[df['Pipeline'] == pipeline]
    return df


def benchmark(pipelines, datasets, problems, hyperparameters=None, optimize=False,
              metrics=CLASSIFICATION_METRICS, target_name='TARGET', runs=1, from_fm=True,
              output_path=None):
    """Evalutate pipelines on a set of datasets (problems) with given metrics.

    Args:
        pipelines: list, a lisf of pipelines.
        datasets: dict, keys are the name of the problem (str), values are the dataset
            for evaluation (pd.DataFrame).
        problems: list, a list of problem names (str).
        hyperparameters: dict, the hyperparameter setting of the pipeline.
            If hyperparameters is None, the pipeline will be initialized with default values.
        optimize: boolean, whether to optimize the hyperparameters used in the pipeline.
        metrics: dict, keys are the name of the metrics and the values are metrics functions.
        target_name: str, the name of the target column in the dataset.
        runs: int, the number of runs of the each pipeline.
        from_fm: boolean, whether the datasets are feature matrix data.
        output_path: str, path of a csv file to store the results.

    Returns:
        result_df: pd.DataFrame, the results of all runs.
    """
    if from_fm:
        if isinstance(datasets, list):
            datasets = {p: d for p, d in zip(problems, datasets)}
    else:
        raise NotImplementedError

    score_list = []
    for problem, dataset in datasets.items():
        score_list.extend(
            _evaluate_pipelines(pipelines, dataset, problem, hyperparameters, optimize, metrics,
                                target_name, runs))
    result_df = pd.DataFrame.from_records(score_list)

    if output_path:
        result_df.to_csv(output_path)

    return result_df
