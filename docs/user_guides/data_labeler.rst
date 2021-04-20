.. _data_labeler:

============
Data Labeler
============

The data labeler is considered a fundamental component that formulates the prediction task for Machine Learning models. It includes generating and identifying **label times**. In this page, we detail what label times are.

Label Times
-----------

After loading the data, you will need to define the prediction task you want to solve (or use one of the already defined tasks). For example, *Missed Appointment* is a common task that aims to predict whether the patient showed up to the appointment or not, helping hospitals to optimize their scheduling policies and resources efficiently. So how do we formulate prediction?

First, you will need to articulate what is the **label** (outcome) you want to predict? Following with the previous example, the *Missed Appointment* task is currently defined as a binary classification task in the system, determining whether a patient showed to the appointment or not.

Next, you will need to determine the **time** in which you define your features over. Continuing with the previous example of *Missed Appointments*, I would like to predict whether the patient will show up to the appointment or not from the point of scheduling appointment. In other words, I would use all the data I could get up until the time when the appointment was scheduled as data for featurization.

Lastly, you will determine the entity that contains this piece of information, **target entity**. Combining these information together, we get ``label_times``.


Available Prediction Problems 
-----------------------------
There is currently six readily available prediction problems for users to explore easily, these are described as follows:

* **Diagnosis prediction**: predicts whether a patient will be diagnosed with a given ICD diagnosis code.
* **Length of Stay (LOS) prediction**: predicts how many days the patient will be in the hospital.
* **Prolonged Length of Stay (PLOS) prediction**: predicts whether a patient stayed in the hospital more or less than a period of time (a week by default).
* **Missed Appointment prediction**: predicts whether the patient will show up to the appointment or not.
* **Mortality prediction**: predicts patient’s mortality.
* **Readmission prediction**: predicts whether a patient will revisit the hospital within a certain period of time (a month by default).


Data Labeling Demo
------------------

Contiuning from :ref:`data_assembler`, we can now use ``label`` with the desired prediction problem to generate ``label_times``.

.. code-block:: python

    from cardea.data_labeling import appointment_no_show

    label_times = cardea.label(appointment_no_show)

.. note:: 
    you can use ``cardea.list_labelers()`` to view available prediction problems.


Creating New Prediction Problems
--------------------------------

Coming Soon.
