.. _featurizer:

==========
Featurizer
==========

Cardea automatically generates features using the `Featuretools`_ package, specifically, the `Deep Feature Synthesis (DFS)`_ algorithm to generate a feature matrix from a given dataset. Aiming to fully automate this process, it determines the focus values of the automated feature engineering
task using the **target entity**, and **label times** of the prediction problem created by :ref:`data_labeler`.

Once you featurize the data, you will obtain a feature matrix, where each row pertains to a specific ``instance_id`` defined in the ``label_times``, and a collection of calculated features. 

Featurizing Demo
----------------

We can continue on our example walkthrough and generate futures on the Missed Appointment dataset.

.. code-block:: python
    
    feature_matrix = cardea.featurize(label_times)

.. note:: 
    the last column in the feature matrix is the ``label`` column which denotes the value we want to predict based on the selected prediction task.

.. _Featuretools: https://www.featuretools.com/
.. _Deep Feature Synthesis (DFS): https://docs.featuretools.com/automated_feature_engineering/afe.html#deep-feature-synthesis
