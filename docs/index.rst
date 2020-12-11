.. raw:: html

   <p align="left">
   <img width=15% src="https://dai.lids.mit.edu/wp-content/uploads/2018/06/Logo_DAI_highres.png" alt="DAI-Lab" />
   <i>An open source project from Data to AI Lab at MIT.</i>
   </p>

|Development Status| |PyPi Shield| |Travis CI Shield| |Downloads| |Binder|

Welcome to Cardea
==================

.. figure:: images/cardea-logo.png
   :width: 200 px
   :alt: Cardea Logo

   An open source project from Data to AI Lab at MIT.

**Date**: |today| **Version**: |version|

-  License: `MIT <https://github.com/DAI-Lab/Cardea/blob/master/LICENSE>`__
-  Development Status:
   `Pre-Alpha <https://pypi.org/search/?c=Development+Status+%3A%3A+2+-+Pre-Alpha>`__
-  Documentation: https://dai-lab.github.io/Cardea/
-  Homepage: https://github.com/DAI-Lab/Cardea

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

Explore Cardea
-----------

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
.. |Travis CI Shield| image:: https://travis-ci.org/DAI-Lab/Cardea.svg?branch=master
   :target: https://travis-ci.org/DAI-Lab/Cardea
.. |Downloads| image:: https://pepy.tech/badge/cardea
   :target: https://pepy.tech/project/cardea
.. |Binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/DAI-Lab/Cardea/master?filepath=notebooks


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