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

    cardea.load_entityset(data='kaggle')
    cardea.es

You can see the list of problem definitions and select one with the following commands:

.. ipython:: python

    cardea.list_problems()

From there, you can select the prediction problem you aim to solve by specifying the name of the class, which in return gives us the ``label_times`` of the problem. 

.. ipython:: python
    
    from cardea.data_labeling import appointment_no_show 

    label_times = cardea.select_problem(appointment_no_show)
    label_times.head()

Then, you can perform the AutoML steps and take advantage of Cardea.

Cardea extracts features through automated feature engineering by supplying the ``label_times`` pertaining to the problem you aim to solve, using the following commands:

 .. ipython:: python
     :okwarning:

     feature_matrix = cardea.generate_features(label_times[:1000])  # a subset
     feature_matrix.head()

Once we have the features, we can now split the data into training and testing

 .. ipython:: python
     :okwarning:

     y = list(feature_matrix.pop('missed'))
     X = feature_matrix.values

     X_train, X_test, y_train, y_test = cardea.train_test_split(
         X, y, test_size=0.2, shuffle=True)


Now that we have our feature matrix properly divided, we can use to train our machine learning pipeline, Modeling, optimizing hyperparameters and finding the most optimal model is done using the following commands:

 .. ipython:: python
     :okwarning:

     cardea.select_pipeline('Random Forest')
     cardea.fit(X_train, y_train)
     y_pred = cardea.predict(X_test)


Finally, you can see accuracy results using the following commands:

 .. ipython:: python
     :okwarning:
     
     cardea.evaluate(X, y, test_size=0.2, metrics=['Accuracy', 'F1 Macro'])


.. _Medical Appointment No Shows: https://www.kaggle.com/joniarroba/noshowappointments
