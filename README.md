# EasyVVUQ

[![Build Status](https://travis-ci.org/UCL-CCS/EasyVVUQ.svg?branch=master)](https://travis-ci.org/UCL-CCS/EasyVVUQ)

The aim of this library is to facilitate verification, validation and 
uncertainty quantification (VVUQ) for a wide variety of simulations.

Development was funded by the EU Horizon 2020 project [VECMA](http://www.vecma.eu/).

## Requirements

To use the library you will need Python 3.6+.

## Installation

We are trying to keep dependencies at a minimum but a few are inevitable, to install them use:

```
pip3 install -r requirements.txt
```

Then the library can be installed using:
```buildoutcfg
python3 setup.py install
```

To complete the tests you need to compile (requires `g++`) the `cannonsim` code:
```
make -C tests/cannonsim/src/ 
```

## Getting Started

Some very basic documentation on how to use EasyVVUQ is available in the [wiki](https://github.com/UCL-CCS/EasyVVUQ/wiki/Getting-Started).
