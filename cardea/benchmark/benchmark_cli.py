import os

import cli.app
from mlblocks import add_primitives_path

from cardea import MLBLOCKS_PRIMITIVES
from cardea.benchmark import (
    aggregate_results_by_pipeline, aggregate_results_by_problem, benchmark, create_tasks)


@cli.app.CommandLineApp
def benchmark_app(app):
    # Add customized primitives from a local source.
    add_primitives_path(MLBLOCKS_PRIMITIVES)

    # STEP-1: Generate tasks from a set of pipelines to solve a list of problems.
    tasks = create_tasks(dataset_name=app.params.dataset,
                         beginning_stage=app.params.stage,
                         optimize=app.params.optimize)

    # STEP-2: Evaluate the tasks and summarize the results of each run.
    results = benchmark(tasks, output_path=app.params.path_to_save)

    # STEP-3.1: Gain a pipeline-level summary by aggregation.
    aggregate_results_by_pipeline(results, 'F1 Macro',
                                  output_path=os.path.join(app.params.path_to_save,
                                                           'pipeline.csv'))

    # STEP-3.2: Gain a problem-level summary by aggregation.
    aggregate_results_by_problem(results, 'F1 Macro', record_time=False,
                                 output_path=os.path.join(app.params.path_to_save, 'problem.csv'))


benchmark_app.add_param("-d", "--dataset", default="mimic-iii",
                        help="name of the benchmark dataset, \"mimic-iii\" in default")
benchmark_app.add_param("-s", "--stage", default="featurization",
                        help="the beginning stage of the benchmarking, \"featurization\" "
                             "in default")
benchmark_app.add_param("-p", "--path_to_save", default=None,
                        help="path to save the benchmark results.")
benchmark_app.add_param("-o", "--optimize", default=False, type=bool,
                        help="whether to optimize the hyper-parameters of the pipeline.")

if __name__ == '__main__':
    benchmark_app.run()
