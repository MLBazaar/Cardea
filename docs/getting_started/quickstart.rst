.. highlight:: shell

Quickstart
==========

The first step to use Cardea is to follow the :ref:`installation` instructions. Once installed and
having a working environment, you can start using the Cardea library in a Python console
using the following steps:

First, load the core class to work with:

.. ipython:: python

    from cardea import Cardea
    cardea = Cardea()

Second, load a dataset. By default, if no path is given, Cardea automatically loads a
pre-processed version of the Kaggle dataset: `Medical Appointment No Shows`_, using the
following command:

.. ipython:: python

    cardea.load_data_entityset()

You can see the list of problem definitions and select one with the following commands:

.. ipython:: python

    cardea.list_problems()
    problem = cardea.select_problem('MissedAppointmentProblemDefinition')

Then, you can perform the AutoML steps and take advantage of Cardea:

1. Extracting features (automated feature engineering), using the following commands:

   .. ipython:: python

       feature_matrix = cardea.generate_features(problem[:1000])  # a subset
       feature_matrix = feature_matrix.sample(frac=1)  # shuffle
       y = list(feature_matrix.pop('label'))
       X = feature_matrix.values

2. Modeling, optimizing hyperparameters and finding the most optimal model using the following commands:

   .. ipython:: python

       pipeline = [
           ['sklearn.ensemble.RandomForestClassifier'],
           ['sklearn.naive_bayes.MultinomialNB'],
           ['sklearn.neighbors.KNeighborsClassifier']
       ]

       result = cardea.execute_model(
           feature_matrix=X,
           target=y,
           primitives=pipeline
       )


Finally, you can see accuracy results using the following commands:

.. ipython:: python

    import pandas as pd
    from sklearn.metrics import accuracy_score

    y_test = []
    y_pred = []

    for i in range(0, 10):
        y_test.extend(result['pipeline0']['folds'][str(i)]['Actual'])
        y_pred.extend(result['pipeline0']['folds'][str(i)]['predicted'])

    y_test = pd.Categorical(pd.Series(y_test)).codes
    y_pred = pd.Categorical(pd.Series(y_pred)).codes
    accuracy_score(y_test, y_pred)

.. _Medical Appointment No Shows: https://www.kaggle.com/joniarroba/noshowappointments
