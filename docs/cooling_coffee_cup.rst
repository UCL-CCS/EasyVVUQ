.. _cooling_coffee_cup:

A Cooling Coffee Cup with Polynomial Chaos Expansion
====================================================

In this tutorial we will perform a Polynomial Chaos Expansion for a model of a cooling coffee cup.
The model uses Newton's law of cooling to evolve the temperature, :math:`$T$`, over time (:math:`$t$`) in an environment at :math:`$T_{env}$`:

.. math::
    \frac{dT(t)}{dt} = -\kappa (T(t) -T_{env})

The constant :math:`$\kappa$` characterizes the rate at which the coffee cup transfers heat to the environment.
In this example we will analyze this model using the polynomial chaos expansion (PCE) UQ algorithm.
e will use a constant initial temperature :math:`$T_0 = 95 ^\circ\text{C}$`, and vary :math:`$\kappa$ and $T_{env}$` using a uniform distribution in the ranges 0.025-0.075 and 15-25 respectively.

Below we provide a commented script that shows how the Campaign is built up and then employed.
We also provide an outline of how each element is setup.

EasyVVUQ Script Overview
------------------------
We illustrate the intended workflow using the following basic example script, a python implementation of the cooling coffee cup model used in the \textit{uncertainpy} documentation (code for which is in the tests/cooling/ subdirectory of the EasyVVUQ distribution directory). The code takes a small key/value pair input and outputs a comma separated value CSV) file.

The full script can be found here: (:download:`easyvvuq_pce_tutorial.py <tutorial_files/easyvvuq_pce_tutorial.py>`)

To run the script execute the following command ::

    python3 easyvvuq_pce_tutorial.py
