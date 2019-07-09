.. _cooling_coffee_cup:

A Cooling Coffee Cup with Polynomial Chaos Expansion
====================================================

In this tutorial we will perform a Polynomial Chaos Expansion for a model of a cooling coffee cup.
The model uses Newton's law of cooling to evolve the temperature, :math:`T`, over time (:math:`t`) in an environment at :math:`T_{env}`:

.. math::
    \frac{dT(t)}{dt} = -\kappa (T(t) -T_{env})

The constant :math:`\kappa` characterizes the rate at which the coffee cup transfers heat to the environment.
In this example we will analyze this model using the polynomial chaos expansion (PCE) UQ algorithm.
e will use a constant initial temperature :math:`T_0 = 95 ^\circ\text{C}`, and vary :math:`\kappa` and :math:`T_{env}` using a uniform distribution in the ranges :math:`0.025-0.075` and :math:`15-25` respectively.

Below we provide a commented script that shows how the Campaign is built up and then employed.
We also provide an outline of how each element is setup.

EasyVVUQ Script Overview
------------------------
We illustrate the intended workflow using the following basic example script, a python implementation of the cooling coffee cup model used in the \textit{uncertainpy} documentation (code for which is in the tests/cooling/ subdirectory of the EasyVVUQ distribution directory). The code takes a small key/value pair input and outputs a comma separated value CSV) file.

The input files for this tutorial are the *cooling_model* application (:download:`cooling_model.py <tutorial_files/cooling_model.py>`),
an input template (:download:`cooling.template <tutorial_files/cooling.template>`) and the EasyVVUQ workflow
script (:download:`easyvvuq_pce_tutorial.py <tutorial_files/easyvvuq_pce_tutorial.py>`).

To run the script execute the following command ::

    python3 easyvvuq_pce_tutorial.py


Parameter space definition
--------------------------

The parameter space is defined using a dictionary. Each entry in the dictionary follows the format: ::

    "parameter_name": {"type" : "<value>", "min": <value>, "max": <value>, "default": <value>}

With a defined type, minimum and maximum value and default. If the parameter is not selected to vary in the Sampler (see below) then the default value is used for every run.

App Creation
------------
In this example the GenericEncoder and SimpleCSV, both included in the  core EasyVVUQ library, were used as the encoder/decoder pair for this application.
GenericEncoder performs simple text substitution into a supplied template, using a specified delimiter to identify where parameters should be placed.
The template is shown below (\$ is used as the delimiter).
The template substitution approach is likely to suit most simple applications but in practice many large applications have more complex requirements, for example the multiple input files or the creation of a directory hierarchy.
In such cases, users may write their own encoders by extending the BaseEncoder class. ::

    {
       "T0":"$temp_init",
       "kappa":"$kappa",
       "t_env":"$t_env",
       "out_file":"$out_file"
    }

As can be inferred from its name SimpleCSV reads CVS files produced by the cooling model code.
Again many applications output results in different formats, potentially requiring bespoke Decoders.

In this workflow all application runs will be analyzed as individual datapoint, so we set the collator to AggregateSamples without averaging.
This element simply extracts information using the assigned decoder and adds it to a summary dataframe.

The Sampler
-----------
The user specified which parameters will vary and their corresponding distributions. In this case the kappa and t\_env parameters are varied, both according to a uniform distribution: ::

    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }

Execute Runs
------------
my\_campaign.populate\_runs\_dir() will create a directory hierarchy containing the encoded input files for every run that has not yet been completed. Finally, in this example, a shell command is executed in each directory to execute the simple test code. In practice (in a real HPC workflow) this stage would be best handled using, for example, a pilot job manager.

Collation and analysis
----------------------
Calling my\_campaign.collate() at any stage causes the campaign to aggregate decoded simulation output for all runs which have not yet been collated. This collated data is stored in the campaign database. An analysis element, here PCEAnalysis, can then be applied to the campaign's collation result. The output of this is dependent on the type of analysis element.
