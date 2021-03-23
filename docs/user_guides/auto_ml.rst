.. _modeler:

=======
Modeler
=======

Cardea makes use of two packages to automate and simplify the modeling step in the Machine
Learning tasks: `MLPrimitives`_ and `MLBlocks`_.

MLBlocks is a simple framework for seamlessly combining any possible set of Machine Learning tools developed in Python, whether they are custom developments or belong to third party libraries, and build Pipelines out of them that can be fitted and then used to make predictions.
This is achieved by providing a simple and intuitive annotation language that allows the user to specify how to integrate with each tool, called **primitives**, in order to provide a common uniform interface to each one of them.

On the other hand, *MLPrimitives* is a repository containing primitive annotations to be used by the *MLBlocks* library.

Thanks to the use of these two packages, the Machine Learning algorithm selection and the hyper-parameter tuning steps can be done easily.

Modeling Demo
-------------

Continuing from the previous example of *Missed Appointments*, let’s divide our ``feature_matrix`` into training and testing portions.

.. ipython:: python
    :okwarning:

    from cardea import Cardea
    cardea = Cardea()
    cardea.load_entityset(data='kaggle')
    label_times = cardea.select_problem('MissedAppointment')
    feature_matrix = cardea.generate_features(label_times[:1000])

    # split the data
    y = list(feature_matrix.pop('label'))
    X = feature_matrix.values
    X_train, X_test, y_train, y_test = cardea.train_test_split(
        X, y, test_size=0.2, shuffle=True)

Second, we specify the pipeline we want to use for our prediction. Cardea has a number of pre-created pipelines which you can find in `cardea pipelines <https://github.com/MLBazaar/Cardea/tree/master/cardea/pipelines>`__. We can then use the modeler component to help us train, tune, and select the best version of the pipeline.

.. ipython:: python

    cardea.select_pipeline('Random Forest')
    cardea.fit(X_train, y_train)
    y_pred = cardea.predict(X_test)

.. note:: 
    you can set ``tune=True`` to optimize the hyperparameters of the pipeline during the ``fit`` process.


Additionally, you can use ``fit_predict`` to train the pipeline then make predictions directly on the same dataset.

We can also evaluate the performance of the pipeline. You can use ``cardea.evaluate`` that will compare the predicted labels against the ground truth according to a list of given metrics. 

.. ipython:: python

    cardea.evaluate(X_test, y_test)

Metrics used are developed by `sklearn <https://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics>`__. By default classification metrics include: accuracy, f1 score, precision, and recall. On the other hand, regression metrics are shown through: variance score, mean absolute error, mean squared error, mean squared log error, median absolute error, and r2 score.

.. _MLPrimitives: https://MLBazaar.github.io/MLPrimitives/
.. _MLBlocks: https://MLBazaar.github.io/MLBlocks/
