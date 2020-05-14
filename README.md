<img align="left" width="75" height="75" src="https://raw.githubusercontent.com/UCL-CCS/EasyVVUQ/master/docs/_static/circle-logo-75.png" alt="EasyVVUQ icon">

# EasyVVUQ

[![Build Status](https://travis-ci.org/UCL-CCS/EasyVVUQ.svg?branch=master)](https://travis-ci.org/UCL-CCS/EasyVVUQ)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/UCL-CCS/EasyVVUQ.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/UCL-CCS/EasyVVUQ/context:python)
[![Documentation Status](https://readthedocs.org/projects/easyvvuq/badge/?version=latest)](https://easyvvuq.readthedocs.io/)
[![Coverage Status](https://coveralls.io/repos/github/UCL-CCS/EasyVVUQ/badge.svg?branch=dev&service=github)](https://coveralls.io/github/UCL-CCS/EasyVVUQ?branch=dev)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3796/badge)](https://bestpractices.coreinfrastructure.org/projects/3796)

The aim of this library is to facilitate verification, validation and 
uncertainty quantification (VVUQ) for a wide variety of
simulations.

The easiest way to get started is to follow the example outlined in
this [Google Colaboratory](https://colab.research.google.com/drive/1qD07_Ry2lOB9-Is6Z2mQG0vVWskNBHjr).

Development was funded by the EU Horizon 2020 project [VECMA](http://www.vecma.eu/).

## Requirements

To use the library you will need Python 3.6+.

## Installation using pip

If you are unsure of the version of python your default `pip` works for type:
```
pip --version
```

If the output ends with `(python 2.7)` you should replace `pip` with `pip3` in the following commands.

The following should fully install the library:
```
pip install easyvvuq
```

To upgrade the library use:

```
pip install easyvvuq --upgrade
```

## Manual installation from repository

Alternatively, you can manually install EasyVVUQ.
First clone the repository to your computer:
```
git clone https://github.com/UCL-CCS/EasyVVUQ.git
```

Note: As above, you need to be sure you are installing for Python 3 - if necessary replace `pip` with `pip3` and `python` with `python3` in the commands below.

We are trying to keep dependencies at a minimum but a few are inevitable, to install them use:
```
cd EasyVVUQ/

pip install -r requirements.txt
```

Then the library can be installed using:
```buildoutcfg
python setup.py install
```

## Getting Started

Documentation, including a basic tutorial, is avalable [here](https://easyvvuq.readthedocs.io/en/dev/).

## Citing EasyVVUQ

Richardson, R A, Wright, D W, Edeling, W, Jancauskas, V, Lakhlili, J and Coveney, P V. 
2020 EasyVVUQ: A Library for Verification, Validation and Uncertainty Quantification in High Performance Computing. 
Journal of Open Research Software, 8: 11.
[DOI: 10.5334/jors.303](https://doi.org/10.5334/jors.303).
