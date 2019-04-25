Data Loading
============

Cardea makes use of a module to plugin the user's data and automatically organize it into the framework.
It expects data in Fast Healthcare Interoperability Resources (FHIR), a standard for health care data
exchange, published by HL7®. Among the advantages of FHIR over other standards are:

* Fast and easy to implement
* Specification is free for use with no restrictions
* Strong foundation in Web standards: XML, JSON, HTTP, OAuth, etc.
* Support for RESTful architectures
* Concise and easily understood specifications
* A human-readable serialization format for ease of use by developers

By default, Cardea loads a dataset hosted in `Amazon S3`_, representing a formatted version of the
Kaggle dataset: `Medical Appointment No Shows`_, but it also allows user to load datasets providing a
local path with CSV files, using the ``load_data_entityset(...)`` method. As an example, the following piece
of code will load the default Kaggle dataset:

.. code-block:: python

    from cardea import Cardea
    cardea = Cardea()
    cardea.load_data_entityset()

While local files can be loaded using the same method with a ``folder_path`` parameter:

.. code-block:: python

    cardea.load_data_entityset(folder_path="your/local/path/")

Cardea handles datasets as a collection of entities and the relationships between them because they
are useful for preparing raw, structured datasets for feature engineering. For this, it uses
the `featuretools.EntitySet`_ class.

Using the following command, you will be able to summarize the dataset:

.. code-block:: python

    cardea.es
    Entityset: fhir
      Entities:
        Address [Rows: 81, Columns: 2]
        Appointment_Participant [Rows: 6100, Columns: 2]
        Appointment [Rows: 110527, Columns: 5]
        CodeableConcept [Rows: 4, Columns: 2]
        Coding [Rows: 3, Columns: 2]
        Identifier [Rows: 227151, Columns: 1]
        Observation [Rows: 110527, Columns: 3]
        Patient [Rows: 6100, Columns: 4]
        Reference [Rows: 6100, Columns: 1]
      Relationships:
        Appointment_Participant.actor -> Reference.identifier
        Appointment.participant -> Appointment_Participant.object_id
        CodeableConcept.coding -> Coding.object_id
        Observation.code -> CodeableConcept.object_id
        Observation.subject -> Reference.identifier
        Patient.address -> Address.object_id

Showing, in this case, the resources that were loaded into the framework (**Entities** section)
and the relationship between the resources (**Relationships** section).


.. _Amazon S3: https://s3.amazonaws.com/dai-cardea/
.. _Medical Appointment No Shows: https://www.kaggle.com/joniarroba/noshowappointments
.. _featuretools.EntitySet: https://docs.featuretools.com/generated/featuretools.EntitySet.html#featuretools.EntitySet
