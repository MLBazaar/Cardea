Advanced use
============

How to define a new machine learning task?
------------------------------------------

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
-------------------------------------------

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


.. _featuretools.EntitySet: https://docs.featuretools.com/generated/featuretools.EntitySet.html#featuretools.EntitySet
.. _problem_definition: https://github.com/D3-AI/Cardea/tree/master/cardea/problem_definition
.. _ProblemDefinition: https://github.com/D3-AI/Cardea/blob/master/cardea/problem_definition/definition.py
.. _init: https://github.com/D3-AI/Cardea/blob/master/cardea/problem_definition/__init__.py
.. _EntitySetLoader: https://github.com/D3-AI/Cardea/blob/master/cardea/data_loader/entityset_loader.py#L9
.. _Cardea: https://github.com/D3-AI/Cardea/blob/master/cardea/cardea.py
