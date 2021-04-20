.. highlight:: shell

Quickstart
==========

The first step to use Cardea is to follow the :ref:`installation` instructions. Once installed and
having a working environment, you can start using the Cardea library in a Python console
using the following steps:

First, we need to have a ``data_path`` referencing the data we will be working with. This data
can be in either FHIR or MIMIC format. In this quickstart, we will use a pre-processed version of 
the Kaggle dataset: `Medical Appointment No Shows`_, using the following command:

.. ipython:: python

    from cardea.data import download
    data_path = download('kaggle')

Alternatively, we can manually download this dataset from the s3 bucket using:

::
    curl -O https://dai-cardea.s3.amazonaws.com/kaggle.zip && unzip -d kaggle kaggle.zip

Then, we load the core class to work with:

.. ipython:: python

    from cardea import Cardea

    cardea = Cardea(data_path=data_path,
                    fhir=True)

To verify that the data has been loaded, you can find the loaded entityset by viewing ``cardea.entityset`` which should output the following:

::
    Entityset: kaggle
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

After that, we need to select a specific prediction problem that I am interested in, you 
can use the command ``cardea.list_labelers`` to view the readily available functions. Once
that has been determined, we pass the function of interested to the data labeler, which in 
return gives us the ``label_times`` of the problem. 

.. ipython:: python
    
    from cardea.data_labeling import appointment_no_show 

    label_times = cardea.label(appointment_no_show, subset=100)
    label_times.head()

``label_times`` summarizes for each instance in the dataset (1) what is its corresponding label of the instance and (2) what is the time index that indicates the timespan allowed for calculating features that pertain to each instance in the dataset.

Then, you can perform the AutoML steps and take advantage of Cardea.

Cardea extracts features through automated feature engineering by supplying the ``label_times`` pertaining to the problem you aim to solve, using the following commands:

 .. ipython:: python
     :okwarning:

     feature_matrix = cardea.featurize(label_times)
     feature_matrix.head()

Once we have the features, we can now split the data into training and testing

 .. ipython:: python
     :okwarning:

     y = feature_matrix.pop('label').values
     X = feature_matrix.values

     X_train, X_test, y_train, y_test = cardea.train_test_split(
         X, y, test_size=0.2, shuffle=True)


Now that we have our feature matrix properly divided, we can use to train our machine learning pipeline, Modeling, optimizing hyperparameters and finding the most optimal model is done using the following commands:

 .. ipython:: python
     :okwarning:

     cardea.set_pipeline('Random Forest')
     cardea.fit(X_train, y_train)
     y_pred = cardea.predict(X_test)


Finally, you can see accuracy results using the following commands:

 .. ipython:: python
     :okwarning:
     
     cardea.evaluate(X_test, y_test, metrics=['Accuracy', 'F1 Macro'])


.. _Medical Appointment No Shows: https://www.kaggle.com/joniarroba/noshowappointments
