Welcome to Cardea!
==================

.. figure:: images/cardea-logo.png
   :width: 300 px
   :alt: Cardea Logo

   An open source project from Data to AI Lab at MIT.

Overview
--------

*This library is under development. Please contact dai-lab@mit.edu or any of the contributors
for more information.*

Cardea is a machine learning library built on top of the `FHIR`_ data schema. The library uses
a number of AutoML tools developed under `The Human Data Interaction Project`_ at
`Data to AI Lab at MIT`_.

Our goal is to provide an easy to use library to develop machine learning models from
electronic health records. A typical usage of this library will involve:

* Installing the library available via pypi

* Integrating their data in FHIR schema (whatever subset of data is available)

* Following the API to develop some pre-specified prediction models (or specify new ones using
  our API). The model building process is parameterized but automatically does:

  * data cleaning, auditing

  * preprocessing

  * feature engineering

  * machine learning model search and tuning

  * model evaluation

  * model auditing

* Testing the models using our API

* Preparing and deploying the models

.. toctree::
   :caption: Getting Started
   :maxdepth: 2

   Welcome <self>
   getting_started/install
   getting_started/quickstart

.. toctree::
   :caption: Basic Concepts
   :maxdepth: 2

   Welcome <basic_concepts/concepts>
   Data Loading <basic_concepts/data_loading>
   Machine Learning Tasks <basic_concepts/machine_learning_tasks>
   Auto - Featurization <basic_concepts/auto_featurization>
   Auto - ML <basic_concepts/auto_ml>
   Auditing <basic_concepts/auditing>
   Advanced Use <basic_concepts/advanced_use>

.. toctree::
   :caption: Community
   :maxdepth: 2

   Community <community/welcome>
   Contributing <community/contributing>

.. toctree::
   :caption: Resources
   :hidden:

   API Reference <api/cardea>
   authors
   history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _FHIR: https://www.hl7.org/fhir/
.. _The Human Data Interaction Project: https://github.com/HDI-Project
.. _Data to AI Lab at MIT: https://dai.lids.mit.edu/
