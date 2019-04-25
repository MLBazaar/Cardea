Auditing
========

One element that is essential to prediction problems is the evaluation of the prediction results,
but this might come in various forms and users rely on different metrics to identify the best
model for a specific problem. Commonly, some metrics might be more representative than others
depending on problem.

Therefore, to facilitate the auditing process, Cardea has two components designed specifically
to cover both: data and model auditing, given that prediction problems rely mainly on the data
that is being used. While Cardea provides a set of metrics that can be used as default metrics
for certain prediction problems, it also provides the means to expand them and allow users to
introduce new kind of metrics.

Using Cardea, users have the ability to generate a data summary report describing the data through
the Data Auditor, enhancing users' understandability and engagement. Although the system includes
a set of predefined audits that are commonly applied in the literature, they can also specify special
types of audits that they want to apply on their dataset, using a dictionary of all the possible checks
that must be reported.

These checks are divided in two categories: **data quality checks** and **data representation checks**. While
the data quality checks identifies the missing information in the data; the data representation checks
identifies data represents the users assumptions.

Similarly, Cardea provides full report to users describing the performance and behavior of the model with
the `Model Auditor`_ component, aiming to give users more interpretability and understanding of the machine
learning model.

Currently, prediction problems are categorized in regression or classification problems and each of them
has a wide range of metrics (e.g., accuracy, F1 scores, precision recall, AUC for classification and
mean square errors, mean absolute errors and r squared for regression).

Additionally, given that Cardea provides the ability to run different pipelines composed of different
types of machine learning algorithms, the Model Auditor allows to compare multiple prediction
pipelines and evaluate changes in their behavior using different training and testing data sets.

.. _Model Auditor: https://github.com/HDI-Project/ModelAudit
