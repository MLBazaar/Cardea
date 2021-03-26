.. raw:: html

   <p align="left">
   <img width=15% src="https://dai.lids.mit.edu/wp-content/uploads/2018/06/Logo_DAI_highres.png" alt="DAI-Lab" />
   <i>An open source project from Data to AI Lab at MIT.</i>
   </p>

|Development Status| |PyPi Shield| |Run Tests| |Downloads| |Binder|

Welcome to Cardea
==================

.. figure:: images/cardea-logo.png
   :width: 200 px
   :alt: Cardea Logo

*This library is under development. Please contact dai-lab@mit.edu or any of the contributors for more information.*

**Date**: |today| **Version**: |version|

-  License: `MIT <https://github.com/MLBazaar/Cardea/blob/master/LICENSE>`__
-  Development Status:
   `Pre-Alpha <https://pypi.org/search/?c=Development+Status+%3A%3A+2+-+Pre-Alpha>`__
-  Documentation: https://mlbazaar.github.io/Cardea/
-  Homepage: https://github.com/MLBazaar/Cardea

Overview
--------

*This library is under development. Please contact dai-lab@mit.edu or any of the contributors for more information.*

Cardea is a machine learning library built on top of *schemas* that support electronic health records (EHR). The library uses a number of AutoML tools developed under `The Human Data Interaction Project`_ at
`Data to AI Lab at MIT`_.

Our goal is to provide an easy to use library to develop machine learning models from electronic health records. A typical usage of this library will involve interacting with our API to develop prediction models.

.. figure:: images/cardea-process.png
   :width: 600 px
   :alt: Cardea Process

A series of sequential processes are applied to build a machine learning model. These processes are triggered using our following APIs to perform the following:

* loading data using the automatic **data assembler**, where we capture data from its raw format into an entityset representation.

* **data labeling** where we create label times that generates (1) the time index that indicates the timespan for which I create my features (2) the encoded labels of the prediction task. this is essential for our feature engineering phase.

* **featurization** for which we automatically feature engineer our data to generate a feature matrix.

* lastly, we build, train, and tune our machine learning model using the **modeling component**.


Explore Cardea
--------------

* `Getting Started <getting_started/index.html>`_
* `Basic Concepts <basic_concepts/index.html>`_
* `API Reference <api_reference/index.html>`_
* `Community <community/index.html>`_
* `Release Notes <history.html>`_

--------------

.. |Development Status| image:: https://img.shields.io/badge/Development%20Status-2%20--%20Pre--Alpha-yellow
   :target: https://pypi.org/search/?c=Development+Status+%3A%3A+2+-+Pre-Alpha
.. |PyPi Shield| image:: https://img.shields.io/pypi/v/cardea.svg
   :target: https://pypi.python.org/pypi/cardea
.. |Run Tests| image:: https://github.com/MLBazaar/Cardea/workflows/Run%20Tests/badge.svg
   :target: https://github.com/MLBazaar/Cardea/actions?query=workflow%3A%22Run+Tests%22+branch%3Amaster
.. |Downloads| image:: https://pepy.tech/badge/cardea
   :target: https://pepy.tech/project/cardea
.. |Binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/MLBazaar/Cardea/master?filepath=notebooks


.. toctree::
    :maxdepth: 3
    :hidden:
    :titlesonly:

    getting_started/index
    basic_concepts/index
    api_reference/index
    community/index
    Release Notes <history>

.. _FHIR: https://www.hl7.org/fhir/
.. _The Human Data Interaction Project: https://github.com/HDI-Project
.. _Data to AI Lab at MIT: https://dai.lids.mit.edu/