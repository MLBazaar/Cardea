Machine Learning Tasks
======================

The Problem Definition is considered a fundamental component that formulates the task for
Machine Learning models. It includes generating and identifying two main concepts:
the **target variable** and the **cutoff times**.

Therefore, the first step to work with Cardea is defining a Machine Learning Task (or using one
of the already defined tasks). For example, **Missed Appointment** is a common task that aims
to predict whether the patient showed to the appointment or not, helping hospitals to optimize
their scheduling policies and resources efficiently.

Outcome to predict
------------------

Following with the previous example, the **Missed Appointment** task is currently defined as
a binary classification task in the system, determining whether a patient showed to the appointment
or not from the point of appointment scheduling.

Usually, the outcome is defined over the FHIR data schema, using the resource id values for
references between instances.

Cutoff times and Labels
-----------------------

As it was stated before, the success of the Problem Definition step and its outcome depends on
two main concepts: the **target variable** and the **cutoff times**. The target variable is
generated automatically by Cardea if it does not exist in the dataset and its objective is to
set the definition of the model output. In the other hand, the objective of cutoff times is to
split the data in such manner that any events before the cutoff time are used for training while
events after the cutoff time are used for testing. The following code shows the format for these
values in the **Missed Appointment** task:

.. ipython:: python

    from cardea import Cardea
    cardea = Cardea()
    cardea.load_data_entityset()
    cardea.select_problem('MissedAppointmentProblemDefinition')

Current Prediction Problems
---------------------------

Cardea encapsulates six different prediction problems for users to explore easily,
these are described as follows:

1. Diagnosis Prediction:
   a. Predicts whether a patient will be diagnosed with a specified diagnosis.
2. Length of Stay:
   a. Predicts how many days the patient will be in the hospital.
3. Missed Appointment:
   a. Predicts whether the patient showed to the appointment or not.
4. Mortality Prediction:
   a. Predicts whether a patient will suffer from mortality.
5. Prolonged Length of Stay:
   a. Predicts whether a patient stayed in the hospital more or less than a period of time (a week by default).
6. Readmission:
   a. Predicts whether a patient will revisit the hospital within certain period of time (a month by default).

You can see the list of problems using the ``list_problems(...)`` method, example:

.. ipython:: python

    from cardea import Cardea
    cardea = Cardea()
    cardea.list_problems()
