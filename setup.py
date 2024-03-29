#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md', encoding='utf-8') as history_file:
    history = history_file.read()

install_requires = [
    'mlblocks>=0.6,<0.7',
    'mlprimitives>=0.3.6.dev0,<0.5',
    'baytune>=0.5,<0.6',
    'pyCLI==2.0.3',
    'scikit-learn>=1.2,<2',
    # 'featuretools>=0.20.0,<0.25',
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'rundoc>=0.4.3,<0.5',
]

development_requires = [
    # general
    'bumpversion>=0.5.3',
    'pip>=9.0.1',
    'watchdog>=0.8.3',
    'jedi<0.18',

    # docs
    'docutils>=0.12,<0.18',
    'm2r2>=0.2.5,<0.3',
    'nbsphinx>=0.5.0,<0.7',
    'sphinx_toolbox>=2.5,<3',
    'Sphinx>=3,<3.3',
    'pydata-sphinx-theme<0.5',
    'ipython>=6.5,<9',
    'Jinja2>=2,<3', # <- breaks docs

    # fails on Sphinx < v3.4
    'alabaster<=0.7.12',
    # fails on Sphins < v5.0
    'sphinxcontrib-applehelp<1.0.8',
    'sphinxcontrib-devhelp<1.0.6',
    'sphinxcontrib-htmlhelp<2.0.5',
    'sphinxcontrib-serializinghtml<1.1.10',
    'sphinxcontrib-qthelp<1.0.7',

    # style check
    'flake8>=3.7.7,<4',
    'isort>=4.3.4,<5',

    # automatically fix style issues
    'autoflake>=1.3,<2',
    'autopep8>=1.3.5,<2',

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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
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
    python_requires='>=3.8,<3.12',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/MLBazaar/Cardea',
    version='0.1.3.dev0',
    zip_safe=False
)
