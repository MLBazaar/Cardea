#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

install_requires = [
    'featuretools==0.6.1',
    'networkx==2.2',
    'numpy>=1.15.2,<1.17',
    'pandas>=0.23.4,<0.25',
    'scikit-learn>=0.20.0,<0.21',
    'mlblocks==0.3.0',
    'mlprimitives==0.1.6',
    'hyperopt==0.1.2',
    'Keras>=2.1.6,<2.4',
    'pyCLI==2.0.3'
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

tests_require = [
    'pytest>=3.4.2',
    'google-compute-engine==2.8.12',    # required by travis
]

development_requires = [
    # general
    'bumpversion>=0.5.3',
    'pip>=9.0.1',
    'watchdog>=0.8.3',

    # build docs
    'm2r2>=0.2.5,<0.3',
    'nbsphinx>=0.5.0,<0.7',
    'Sphinx>=1.7.1,<3',
    'pydata-sphinx-theme',
    'autodocsumm>=0.1.10,<1',
    'recommonmark>=0.4.0',
    'ipython==6.5.0',

    # style check
    'flake8>=3.5.0,<4',
    'isort>=4.3.4,<5',

    # automatically fix style issues
    'autoflake>=1.3',
    'autopep8>=1.3.5',

    # distribute on PyPI
    'twine>=1.10.0',
    'wheel>=0.30.0',

    # Advanced testing
    'tox>=2.9.1',
    'coverage>=4.5.1'
]

setup(
    author="MIT Data To AI Lab",
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Cardea",
    entry_points={
        'mlblocks': [
            'primitives=cardea:MLBLOCKS_PRIMITIVES',
            'pipelines=cardea:MLBLOCKS_PIPELINES'
        ]
    },
    extras_require={
        'dev': development_requires + tests_require,
        'test': tests_require
    },
    include_package_data=True,
    install_requires=install_requires,
    keywords='cardea',
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='cardea',
    packages=find_packages(include=['cardea', 'cardea.*']),
    python_requires='>=3.4',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/DAI-Lab/Cardea',
    version='0.1.1',
    zip_safe=False
)
