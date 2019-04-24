.. highlight:: shell
.. _concepts:

Basic Concepts
==============

Before diving into advanced usage and contributions, let's review the basic concept of the
library to help you get started.

Data Loading
------------

Cardea makes use of a module to plugin the user's data and automatically organize it into the framework.
It expects data in Fast Healthcare Interoperability Resources (FHIR), a standard for health care data
exchange, published by HL7®. Among the advantages of FHIR over other standards are:

* Fast and easy to implement
* Specification is free for use with no restrictions
* Strong foundation in Web standards: XML, JSON, HTTP, OAuth, etc.
* Support for RESTful architectures
* Concise and easily understood specifications
* A human-readable serialization format for ease of use by developers

By default, Cardea loads a dataset hosted in `Amazon S3`_, representing a formatted version of the
Kaggle dataset: `Medical Appointment No Shows`_, but it also allows user to load datasets providing a
local path with CSV files, using the ``load_data_entityset(...)`` method. As an example, the following piece
of code will load the default Kaggle dataset:

.. code-block:: python

    from cardea import Cardea
    cardea = Cardea()
    cardea.load_data_entityset()

While local files can be loaded using the same method with a ``folder_path`` parameter:

.. code-block:: python

    cardea.load_data_entityset(folder_path="your/local/path/")

Cardea handles datasets as a collection of entities and the relationships between them because they
are useful for preparing raw, structured datasets for feature engineering. For this, it uses
the `featuretools.EntitySet`_ class.

Using the following command, you will be able to summarize the dataset:

.. code-block:: python

    cardea.es
    Entityset: fhir
      Entities:
        Address [Rows: 81, Columns: 2]
        Appointment_Participant [Rows: 6100, Columns: 2]
        Appointment [Rows: 110527, Columns: 5]
        CodeableConcept [Rows: 4, Columns: 2]
        Coding [Rows: 3, Columns: 2]
        Identifier [Rows: 227151, Columns: 1]
        Observation [Rows: 110527, Columns: 3]
        Patient [Rows: 6100, Columns: 4]
        Reference [Rows: 6100, Columns: 1]
      Relationships:
        Appointment_Participant.actor -> Reference.identifier
        Appointment.participant -> Appointment_Participant.object_id
        CodeableConcept.coding -> Coding.object_id
        Observation.code -> CodeableConcept.object_id
        Observation.subject -> Reference.identifier
        Patient.address -> Address.object_id

Showing, in this case, the resources that were loaded into the framework (**Entities** section)
and the relationship between the resources (**Relationships** section).

Machine Learning Tasks
----------------------

The Problem Definition is considered a fundamental component that formulates the task for
Machine Learning models. It includes generating and identifying two main concepts:
the **target variable** and the **cutoff times**.

Therefore, the first step to work with Cardea is defining a Machine Learning Task (or using one
of the already defined tasks). For example, **Missed Appointment** is a common task that aims
to predict whether the patient showed to the appointment or not, helping hospitals to optimize
their scheduling policies and resources efficiently.

Outcome to predict
~~~~~~~~~~~~~~~~~~

Following with the previous example, the **Missed Appointment** task is currently defined as
a binary classification task in the system, determining whether a patient showed to the appointment
or not from the point of appointment scheduling.

Usually, the outcome is defined over the FHIR data schema, using the resource id values for
references between instances.

Cutoff times and Labels
~~~~~~~~~~~~~~~~~~~~~~~

As it was stated before, the success of the Problem Definition step and its outcome depends on
two main concepts: the **target variable** and the **cutoff times**. The target variable is
generated automatically by Cardea if it does not exist in the dataset and its objective is to
set the definition of the model output. In the other hand, the objective of cutoff times is to
split the data in such manner that any events before the cutoff time are used for training while
events after the cutoff time are used for testing. The following code shows the format for these
values in the **Missed Appointment** task:

.. ipython:: python

    from cardea import Cardea
    cardea = Cardea()
    cardea.load_data_entityset()
    cardea.select_problem('MissedAppointmentProblemDefinition')

Current Prediction Problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cardea encapsulates six different prediction problems for users to explore easily,
these are described as follows:

1. Diagnosis Prediction:
   a. Predicts whether a patient will be diagnosed with a specified diagnosis.
2. Length of Stay:
   a. Predicts how many days the patient will be in the hospital.
3. Missed Appointment:
   a. Predicts whether the patient showed to the appointment or not.
4. Mortality Prediction:
   a. Predicts whether a patient will suffer from mortality.
5. Prolonged Length of Stay:
   a. Predicts whether a patient stayed in the hospital more or less than a period of time (a week by default).
6. Readmission:
   a. Predicts whether a patient will revisit the hospital within certain period of time (a month by default).

You can see the list of problems using the ``list_problems(...)`` method, example:

.. ipython:: python

    from cardea import Cardea
    cardea = Cardea()
    cardea.list_problems()


Auto - Featurization
----------------------

Cardea automatically generates features using the `Featuretools`_ package, specifically,
the `Deep Feature Synthesis (DFS)`_ algorithm to generate a feature matrix from a given dataset.
Aiming to fully automate this process, it determines the focus values of the automated feature engineering
task using the **target entity**, **cutoff times**, and **label** of the prediction problem.

Auto - ML
---------

Cardea makes use of two packages to automate and simplify the modeling step in the Machine
Learning tasks: `MLPrimitives`_ and `MLBlocks`_.

MLBlocks is a simple framework for seamlessly combining any possible set of Machine Learning
tools developed in Python, whether they are custom developments or belong to third party
libraries, and build Pipelines out of them that can be fitted and then used to make predictions.
This is achieved by providing a simple and intuitive annotation language that allows the user to
specify how to integrate with each tool, called **primitives**, in order to provide a common uniform
interface to each one of them.

In the other hand, MLPrimitives is a repository containing primitive annotations to be used by the
MLBlocks library.

Thanks to the use of these two packages, the Machine Learning algorithm selection and the
hyper-parameter tuning steps can be done easily using JSON annotations as follow:

.. code-block:: python

    pipeline = [
        ['sklearn.ensemble.RandomForestClassifier'],
        ['sklearn.naive_bayes.MultinomialNB'],
        ['sklearn.neighbors.KNeighborsClassifier']
    ]
    result = cardea.execute_model(..., primitives=pipeline)

Where, for example, the ``sklearn.naive_bayes.MultinomialNB`` primitive is defined in the
`MLPrimitives`_ package, with the following structure:

.. code-block:: python

    {
        "name": "sklearn.naive_bayes.MultinomialNB",
        "contributors": [...],
        "documentation": "...",
        "description": "...",
        "classifiers": {
            "type": "estimator",
            "subtype": "classifier"
        },
        "modalities": ["text"],
        "primitive": "sklearn.naive_bayes.MultinomialNB",
        "fit": {
            "method": "fit",
            "args": [
                {
                    "name": "X",
                    "type": "ndarray"
                },
                {
                    "name": "y",
                    "type": "array"
                }
            ]
        },
        "produce": {
            "method": "predict",
            "args": [
                {
                    "name": "X",
                    "type": "ndarray"
                }
            ],
            "output": [
                {
                    "name": "y",
                    "type": "array"
                }
            ]
        },
        "hyperparameters": {
            "fixed": {
                "fit_prior": {
                    "type": "bool",
                    "default": true
                },
                "class_prior": {
                    "type": "iterable",
                    "default": null
                }
            },
            "tunable": {
                "alpha": {
                    "type": "float",
                    "default": 1.0,
                    "range": [0.0, 1.0]
                }
            }
        }
    }


Auditing
--------

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

Advanced use
------------

How to define a new machine learning task?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The definition of a new Machine Learning task in Cardea can be made in four simple steps:

1. Go to the `problem_definition`_ directory and create a file with a class specifically for
   your problem. This class should extend the `ProblemDefinition`_ class and overwrites
   accordingly the necessary attributes and methods as needed. Usually, you should pay special
   attention to the ``generate_target_label(...)`` and ``generate_cutoff_times(...)`` methods
   as you might need to extend them or re-implemented in some cases.

2. Expose your new class definition in the `init`_ file inside the `problem_definition`_ directory

3. If you will be using a dataset in a different format that the expected by Cardea (CSV files),
   then you will need to provide a specific loading dataset method for your data in the
   `EntitySetLoader`_ class, where you will be creating your collection of entities and
   relationships between them using the `featuretools.EntitySet`_ class.

4. Finally, you need to update the `Cardea`_ class to support the new problem definition and be
   able to instantiate the proper class when it is necessary in the ``Cardea.select_problem(...)``
   method.

Features, primitives and AutoML integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have defined your problem, following the four steps in the previous section, you will be
able to perform featurization and run different primitives using the AutoML tool as follows:

.. code-block:: python

    from cardea import Cardea
    cardea = Cardea()
    cardea.load_your_custom_data()
    problem = cardea.select_problem('YourCustomProblemDefinition')
    feature_matrix = cardea.generate_features(problem[:1000])  # a subset
    feature_matrix = feature_matrix.sample(frac=1)  # shuffle
    y = list(feature_matrix.pop('label'))
    X = feature_matrix.values
    pipeline = [
        ['sklearn.ensemble.RandomForestClassifier'],
        ['sklearn.naive_bayes.MultinomialNB'],
        ['sklearn.neighbors.KNeighborsClassifier']
    ]
    result = cardea.execute_model(feature_matrix=X, target=y, primitives=pipeline)

.. _Amazon S3: https://s3.amazonaws.com/dai-cardea/
.. _Medical Appointment No Shows: https://www.kaggle.com/joniarroba/noshowappointments
.. _featuretools.EntitySet: https://docs.featuretools.com/generated/featuretools.EntitySet.html#featuretools.EntitySet
.. _Featuretools: https://www.featuretools.com/
.. _Deep Feature Synthesis (DFS): https://docs.featuretools.com/automated_feature_engineering/afe.html#deep-feature-synthesis
.. _MLPrimitives: https://hdi-project.github.io/MLPrimitives/
.. _MLBlocks: https://hdi-project.github.io/MLBlocks/
.. _Model Auditor: https://github.com/HDI-Project/ModelAudit
.. _problem_definition: https://github.com/D3-AI/Cardea/tree/master/cardea/problem_definition
.. _ProblemDefinition: https://github.com/D3-AI/Cardea/blob/master/cardea/problem_definition/definition.py
.. _init: https://github.com/D3-AI/Cardea/blob/master/cardea/problem_definition/__init__.py
.. _EntitySetLoader: https://github.com/D3-AI/Cardea/blob/master/cardea/data_loader/entityset_loader.py#L9
.. _Cardea: https://github.com/D3-AI/Cardea/blob/master/cardea/cardea.py
