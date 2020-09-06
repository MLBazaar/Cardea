#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

install_requires = [
    'featuretools>=0.6.1,<0.7',
    'networkx==2.2',
    'numpy>=1.15.4,<1.17',
    'pandas>=0.23.4,<0.25',
    'mlblocks==0.3.0',
    'mlprimitives==0.1.6',
    'scikit-learn==0.20.0',
    'scipy>=1.1.0',
    'docutils<0.16,>=0.10',
    'hyperopt',
    'Keras>=2.1.6,<2.4'
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
    'bumpversion>=0.5.3,<0.6',
    'pip>=10.0.1',
    'watchdog>=0.8.3,<0.11',
    
    # build docs
    'm2r>=0.2.0,<0.3',
    'Sphinx>=1.7.1,<3',
    'sphinx_rtd_theme>=0.2.4,<0.5',
    'recommonmark>=0.4.0',
    'ipython==6.5.0',

    # style check
    'flake8>=3.5.0,<3.8',
    'isort>=4.3.4,<5',
    
    # automatically fix style issues
    'autoflake>=1.3,<2',
    'autopep8>=1.3.5,<2',

    # distribute on PyPI
    'twine>=1.10.0,<4',
    'wheel>=0.30.0',
    
    # Advanced testing
    'tox>=2.9.1,<4',
    'coverage>=4.5.1,<6'
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
    version='0.0.2',
    zip_safe=False,
)
