<p align="center"> 
<img width=20% src="https://dai.lids.mit.edu/wp-content/uploads/2018/08/cardea.png" alt=“Cardea” />
</p>

<p align="center"> 
<i>Cardea is a machine learning library built on top of FHIR schema. </I>
</p>

<p align="center"> 
<i>An open source project from Data to AI Lab at MIT </I>
</p>




[![][pypi-img]][pypi-url] [![][travis-img]][travis-url]

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
- Documentation: https://D3-AI.github.io/Cardea

[travis-img]: https://travis-ci.org/D3-AI/Cardea.svg?branch=master
[travis-url]: https://travis-ci.org/D3-AI/Cardea
[pypi-img]: https://img.shields.io/pypi/v/cardea.svg
[pypi-url]: https://pypi.python.org/pypi/cardea
