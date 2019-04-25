Auto - ML
=========

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


.. _MLPrimitives: https://hdi-project.github.io/MLPrimitives/
.. _MLBlocks: https://hdi-project.github.io/MLBlocks/
