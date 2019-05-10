.. highlight:: shell
.. _installation:

Installation
============

Stable release
--------------

To install Cardea, run this command in your terminal:

.. code-block:: console

    $ pip install cardea

This is the preferred method to install Cardea, as it will always install the most recent
stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

From sources
------------

The sources for Cardea can be downloaded from the `Github repo`_.

You can either clone the ``stable`` branch form the public repository:

.. code-block:: console

    $ git clone --branch stable git://github.com/D3-AI/Cardea

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/D3-AI/Cardea/tarball/stable

Once you have a copy of the source, you can install it with this command:

.. code-block:: console

    $ make install

.. _development:

Development Setup
-----------------

If you want to make changes in `Cardea` and contribute them, you will need to prepare
your environment to do so.

These are the required steps:

1. Fork the Cardea `Github repo`_.

2. Clone your fork locally:

   .. code-block:: console

       $ git clone git@github.com:your_name_here/Cardea.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed,
   this is how you set up your fork for local development:

   .. code-block:: console

       $ mkvirtualenv Cardea
       $ cd Cardea/
       $ make install-develop

.. _Github repo: https://github.com/D3-AI/Cardea
.. _tarball: https://github.com/D3-AI/Cardea/tarball/stable
