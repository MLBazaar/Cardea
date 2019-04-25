Auto - Featurization
====================

Cardea automatically generates features using the `Featuretools`_ package, specifically,
the `Deep Feature Synthesis (DFS)`_ algorithm to generate a feature matrix from a given dataset.
Aiming to fully automate this process, it determines the focus values of the automated feature engineering
task using the **target entity**, **cutoff times**, and **label** of the prediction problem.

.. _Featuretools: https://www.featuretools.com/
.. _Deep Feature Synthesis (DFS): https://docs.featuretools.com/automated_feature_engineering/afe.html#deep-feature-synthesis
