.. _contributing:

Contributing Guidelines
=======================

Ready to contribute with your own code? Great!

Before diving deeper into the contributing guidelines, please make sure to having read
the :ref:`concepts` section and to have gone through the :ref:`development` guide.

Afterwards, please make sure to read the following contributing guidelines carefully, and
later on head to the step-by-step guides for each possible type of contribution.

General Coding Guidelines
*************************

Once you have set up your development environment, you are ready to start working on your
python code.

When doing so, make sure to follow these guidelines:

1. If it does not exist yet, create a new GitHub issue. Indicate in the issue description or
   in a comment that you are available to apply the changes yourself.

2. Wait for the feedback from the maintainers, who will approve the issue and assign it to you,
   before proceeding to implement any changes. Be open to discuss with them about the need
   of adding these changes.

3. Once the issue has been approved and assigned to you, implement the necessary changes in your
   own fork of the project. Please implement them in a branch named after the issue number and
   title, as this makes keeping track of the history of the project easier in the long run.

   You can create such a branch with the following command:

   .. code-block:: console

       $ git checkout -b name-of-your-bugfix-or-feature

4. While hacking your changes, make sure to cover all your developments with the required
   unit tests, and that none of the old tests fail as a consequence of your changes.
   For this, make sure to run the tests suite and check the code coverage:

   .. code-block:: console

       $ make test       # Run the tests
       $ make coverage   # Get the coverage report

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox:

   .. code-block:: console

       $ make lint       # Check code styling
       $ make test-all   # Execute tests on all python versions

6. Make also sure to include the necessary documentation in the code as docstrings following
   the `google docstring`_ style.
   If you want to view how your documentation will look like when it is published, you can
   generate and view the docs with this command:

   .. code-block:: console

       $ make viewdocs

7. Commit your changes and push your branch to GitHub:

   .. code-block:: console

       $ git add .
       $ git commit -m "Your detailed description of your changes."
       $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website and wait for feedback from the maintainers.

.. _google docstring: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


Unit Testing Guidelines
***********************

If you are going to contribute Python code, we will ask you to write unit tests that cover
your development, following these requirements:

1. Unit Tests should be based only in unittest and pytest modules.

2. The tests that cover a module called ``cardea/path/to/a_module.py`` should be
   implemented in a separated module called ``tests/cardea/path/to/test_a_module.py``.
   Note that the module name has the ``test_`` prefix and is located in a path similar
   to the one of the tested module, just inside the ``tests`` folder.

3. Each method of the tested module should have at least one associated test method, and
   each test method should cover only **one** use case or scenario.

4. Test case methods should start with the ``test_`` prefix and have descriptive names
   that indicate which scenario they cover.
   Names such as ``test_some_method_input_none``, ``test_some_method_value_error`` or
   ``test_some_method_timeout`` are right, but names like ``test_some_method_1``,
   ``some_method`` or ``test_error`` are not.

5. Each test should validate only what the code of the method being tested does, and not
   cover the behavior of any third party package or tool being used, which is assumed to
   work properly as far as it is being passed the right values.

6. Any third party tool that may have any kind of random behavior, such as some Machine
   Learning models, databases or Web APIs, will be mocked using the ``mock`` library, and
   the only thing that will be tested is that our code passes the right values to them.

7. Unit tests should not use anything from outside the test and the code being tested. This
   includes not reading or writing to any file system or database, which will be properly
   mocked.
