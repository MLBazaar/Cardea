<p align="center"> 
<img width=20% src="https://dai.lids.mit.edu/wp-content/uploads/2018/08/cardea.png" alt=“Cardea” />
</p>

<p align="left"> 
<i>Cardea is a machine learning library built on top of FHIR schema. </I>
</p>

<p align="left"> 
<i>An open source project from Data to AI Lab at MIT </I>
</p>



[![Development Status](https://img.shields.io/badge/Development%20Status-2%20--%20Pre--Alpha-yellow)](https://pypi.org/search/?c=Development+Status+%3A%3A+2+-+Pre-Alpha)
[![PyPi Shield](https://img.shields.io/pypi/v/cardea.svg)](https://pypi.python.org/pypi/cardea)
[![Travis CI Shield](https://travis-ci.org/DAI-Lab/Cardea.svg?branch=master)](https://travis-ci.org/DAI-Lab/Cardea)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DAI-Lab/Cardea/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DAI-Lab/Cardea/master?filepath=notebooks)

# Cardea

This library is under development. Please contact dai-lab@mit.edu or any of the contributors for more information. We will announce our first release soon. 

Cardea is a machine learning library built on top of the FHIR data schema. The library uses a number of automl tools developed under ["The Human Data Interaction Project"](https://github.com/HDI-Project) at [Data to AI lab at MIT](https://dai.lids.mit.edu/). Our goal is to provide an easy to use library to develop machine learning models from electronic health records. A typical usage of this library will involve:

* Installing the library available via pypi
* Integrating their data in FHIR schema (whatever subset of data is available)
* Following the API develop some pre specified prediction models (or specify new ones using our API) The model building process is parameterized but automatically does:
    * data cleaning, auditing
    * preprocessing
    * feature engineering
    * machine learning model search and tuning 
    * model evaluation 
    * model auditing 
* Testing the models using our API
* Preparing and deploying the models 

## License 
- Free software: MIT license

## Documentation
- Documentation: https://dai-lab.github.io/Cardea
