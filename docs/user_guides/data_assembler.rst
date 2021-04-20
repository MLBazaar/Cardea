.. _data_assembler:

==============
Data Assembler
==============

Cardea makes use of a module to plugin the user’s data and automatically organize it into the framework. It is built on top of schemas that support electronic health records (EHR). One of the schemas we support is Fast Healthcare Interoperability Resources (FHIR) schema. You can read more about the supported :ref:`schemas`.

Cardea expects the raw data to be a folder pointing to data in ``.csv`` format to ingest. Each table/resource should correspond to a single ``.csv`` file which is then directly fed into cardea using ``load_entityset``. 

Entityset
---------

Entityset represents the data structure produced by the data assembler module. The process organizes the data into its corresponding table/resource within the schema and produces an entityset. Generally, the entityset is a collection of entities and relationships:

* **entities** are used to prepare the data (tables), into a structured input for later usage. It contains a ``pandas.DataFrame`` at its core, with meta information indicating the index column, time columns, and other information.
* **relationships** indicate the connection between two entities. It represents how for an entity *A* with primary key *1*, there is another entity *B* with foreign key *2* that references it. The relationship ``B.2 -> A.1`` ties them together. This parent-child relationship is embedded within the entityset.

To read more about entitisets, visit `EntitySet`_.


Data Assembling Demo
--------------------

Let's start first by looking at some raw data. Here, in this example, we have the  Kaggle dataset: `Medical Appointment No Shows`_ already preprocessed to be representative of the FHIR schema. You can download the dataset directly from `Amazon S3`_ or you can run the following command to download it and unzip it:

.. code-block:: console

    curl -O https://dai-cardea.s3.amazonaws.com/kaggle.zip && unzip -d kaggle kaggle.zip

then you would have the following directory

.. code-block:: console

    kaggle
    ├── Coding.csv
    ├── Appointment_Participant.csv
    ├── Address.csv 
    ├── CodeableConcept.csv
    ├── Reference.csv  
    ├── Observation.csv  
    ├── Identifier.csv
    └── Appointment.csv 

.. note:: 
    notice how the file names correspond to the resource name in FHIR.

Then you can directly load the dataset into cardea by supplying the folder path to the ``load_entityset``.


.. code-block:: python

    from cardea import Cardea
    cardea = Cardea(data_path='path/to/data', fhir=True)

We can investigate what the entityset looks like by simply displaying the entityset through ``es``.

.. code-block:: python

    cardea.entityset

.. note:: 
    you can use ``cardea.entityset.plot()`` to visualize your entityset.

Showing above are two sections: 

* **Entities** where we can see the resources loaded. For example, *Appointment* is a resource in FHIR that contains most of the records of this dataset and contains 5 columns. 
* **Relationships** where we can see the parent-child relationship. For example, ``Appointment.participant`` is the column ``participant`` in table ``appointment`` that references the primary key ``object_id`` in table ``Appointment_Partipant``.


We will utilize this structure to develop our :ref:`data_labeler` and :ref:`featurizer`.


FAQ
---

1. **What schemas do we support right now?**
We currently support two :ref:`schemas`, Fast Healthcare Interoperability Resources (FHIR), and Medical Information Mart for Intensive Care III (MIMIC-III).
2. **What if I only have a subset of tables?**
Cardea seamlessly integrates the available data, dropping missing variables and links. Having only a subset of the data does not preclude your from solving a prediction problem if all the necessary information is still present.


.. _EntitySet: https://featuretools.alteryx.com/en/stable/api_reference.html#entityset-entity-relationship-variable-types
.. _Amazon S3: https://dai-cardea.s3.amazonaws.com/kaggle.zip
.. _Medical Appointment No Shows: https://www.kaggle.com/joniarroba/noshowappointments
