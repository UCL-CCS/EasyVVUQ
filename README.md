<img align="left" width="75" height="75" src="https://github.com/UCL-CCS/EasyVVUQ/blob/dev/docs/images/circle-logo.svg" alt="EasyVVUQ icon">

# EasyVVUQ

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/UCL-CCS/EasyVVUQ.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/UCL-CCS/EasyVVUQ/context:python)
[![Documentation Status](https://readthedocs.org/projects/easyvvuq/badge/?version=latest)](https://easyvvuq.readthedocs.io/)
[![Coverage Status](https://coveralls.io/repos/github/UCL-CCS/EasyVVUQ/badge.svg?branch=dev&service=github)](https://coveralls.io/github/UCL-CCS/EasyVVUQ?branch=dev)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3796/badge)](https://bestpractices.coreinfrastructure.org/projects/3796)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCL-CCS/EasyVVUQ/dev?filepath=tutorials)

The aim of EasyVVUQ is to facilitate verification, validation and 
uncertainty quantification (VVUQ) for a wide variety of
simulations. While very convenient for simple cases, EasyVVUQ is particularly well suited in situations where the simulations are computationally expensive, 
heterogeneous computing resources are necessary, the sampling space is very large or book-keeping is prohibitively
complex. It coordinates execution using an efficient database, it is fault tolerant and all progress can be saved.

Here are some examples of questions EasyVVUQ can answer about your code:

 * Given the uncertainties in input parameters, what is the distribution of the output?
 * What percentage of the output variance each input parameter contributes?

It also lets you construct surrogate models that are cheaper to evaluate than the complete simulation.

The high-level overview of the library is available at our [readthedocs](https://easyvvuq.readthedocs.io/en/dev/).

## Getting Started

For the quick start with EasyVVUQ we recommend to check our basic interactive tutorial available [here](https://mybinder.org/v2/gh/UCL-CCS/EasyVVUQ/a6852d6c5ba36f15579e601d7a8d074505f31084?filepath=tutorials%2Fbasic_tutorial.ipynb).


## Functionality

Available analysis and sampling methods:

* Polynomial Chaos Expansion
* Stochastic Collocation
* Dimension-adaptive Stochastic Collocation for high-dimensional inputs (incl notebook in `./tutorials` and [theoretical tutorial](https://www.researchgate.net/publication/359296270_Adaptive_sparse-grid_tutorial))
* Simplex Stochastic Collocation for irregular outputs (incl notebook in `./tutorials` and [article](https://doi.org/10.1016/J.JCP.2015.12.034))
* Monte Carlo Sensitivity Analysis
* Markov-Chain Monte Carlo

EasyVVUQ also supports building surrogate models using:

* Polynomial Chaos Expansion
* Stochastic Collocation
* Gaussian Processes

Supported computing resources:

* Traditional clusters
* Kubernetes clusters

The easiest way to get familiar with the provided functionality is to follow the tutorials (*\*.ipynb* files) in our
[Binder](https://mybinder.org/v2/gh/UCL-CCS/EasyVVUQ/dev?filepath=tutorials).

## Installation instructions

### Requirements

To use the library you will need Python 3.7+.

### Installation using pip

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

### Installation from the Repository via Bash Script (Recommended for Developers)

Alternatively, you can manually install EasyVVUQ. Note: As above, you need to be sure you are installing for `Python3` - if necessary replace `pip` with `pip3` and `python` with `python3` in the commands below.

1. **Clone the Repository:**

```
git clone https://github.com/UCL-CCS/EasyVVUQ.git
```

2. **Install with Bash Script:**

The installation of dependencies and testing have been automated using bash script `install_EasyVVUQ.sh` included in the repository. To execute it: 

```
cd EasyVVUQ/
```

Make bash script executable:

```
chmod +x install_EasyVVUQ.sh
```

Execute bash script:

```
bash install_EasyVVUQ.sh
```

Upon successful installation, the process will end with the following message:

```
EasyVVUQ installation and testing completed successfully!
```

3. **Set the `PYTHONPATH` Environment Variable After installation:**

You may need to manually set the PYTHONPATH to ensure EasyVVUQ can be found by Python. This step is required if the library is installed locally within the repository using the provided venv.

While in EasyVVUQ directory, activate the virtual environment (Linux/macOS):

```
source venv/bin/activate
```

For Windows users, activate virtual environment using:

```
venv\Scripts\activate
```

Export `PYTHONPATH`:

```
export PYTHONPATH=$(pwd):$PYTHONPATH
```

Export `PYTHONPATH` site-packages according to your Python version (e.g., python3.10):

```
export PYTHONPATH=$(pwd)/venv/lib/python3.10/site-packages:$PYTHONPATH
```

Check PYTHONPATH:

```python
python -c "import sys; print('\n'.join(sys.path))"
```

### Manual Developer Installation From the Repository 

1.  **Clone the Repository:**
    ```
    git clone https://github.com/UCL-CCS/EasyVVUQ.git
    ```

2.  **Navigate to the EasyVVUQ directory:**

    ```
    cd EasyVVUQ
    ```

3.  **Create and Activate Virtual Environment:**
   
    Using a virtual environment isolates EasyVVUQ's dependencies and prevents conflicts with other Python projects.

    You can create a Python Virtual Environment inside EasyVVUQ directory or outside it. Git is set to ignore venv

    ```
    python3 -m venv venv        
    ```

    Activate the virtual environment (Linux/macOS):
    
    ```
    source venv/bin/activate
    ```

4. **Install Required Packages using requirements.txt**
    ```
    pip install -r requirements.txt
    ```

5.  **Install EasyVVUQ in Editable Mode in Virtual Environment:**

    ```
    pip install -e .
    ```

    The `-e` flag (editable mode) means any changes you make to the EasyVVUQ source code will be immediately reflected without needing to reinstall.

    To see easyvvuq in the list of the installed packages in the virtual environment:

    ```
    pip list
    ```

6. **Installation Verification:**

    After installation, verify the installation:
    
    ```python
    python -c "import easyvvuq; print('EasyVVUQ version:', easyvvuq.__version__)"
    ```

    Output:

    ```
    EasyVVUQ version: 1.2.3
    ```

## API

You can find the EasyVVUQ API documentation on our [GitHub Pages](https://ucl-ccs.github.io/EasyVVUQ/).

## Citing EasyVVUQ

> Richardson, R A, Wright, D W, Edeling, W, Jancauskas, V, Lakhlili, J and Coveney, P V. 
2020 EasyVVUQ: A Library for Verification, Validation and Uncertainty Quantification in High Performance Computing. 
Journal of Open Research Software, 8: 11.
> [DOI: 10.5334/jors.303](https://doi.org/10.5334/jors.303).

> Wright, D.W., Richardson, R.A., Edeling, W., Lakhlili, J., Sinclair, R.C., Jancauskas, V., Suleimenova, D., Bosak, B., Kulczewski, M., Piontek, T., Kopta, P., Chirca, I., Arabnejad, H., Luk, O.O., Hoenen, O., Weglarz, J., Crommelin, D., Groen, D. and Coveney, P.V. (2020), Building Confidence in Simulation: Applications of EasyVVUQ. Adv. Theory Simul., 3: 1900246.
> [DOI: 10.1002/adts.201900246](https://doi.org/10.1002/adts.201900246).

## Acknowledgments

Development was funded by the EU Horizon 2020 project [VECMA](http://www.vecma.eu/).
