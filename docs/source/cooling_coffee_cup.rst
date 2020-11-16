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

The input files for this tutorial are the *cooling_model* application (:download:`cooling_model.py <../../tutorials/cooling_model.py>`),
an input template (:download:`cooling.template <../../tutorials/cooling.template>`) and the EasyVVUQ workflow
script (:download:`easyvvuq_pce_tutorial.py <../../tutorials/easyvvuq_pce_tutorial.py>`).

To run the script execute the following command

``python3 easyvvuq_pce_tutorial.py``

Import necessary libraries
--------------------------

For this example we import both easyvvuq and chaospy (for the distributions). EasyVVUQ will be referred to as 'uq' in the code. ::

    import easyvvuq as uq
    import chaospy as cp

Create a new Campaign
---------------------

As in the :doc:`Basic Tutorial <basic\_tutorial>`, we start by creating an EasyVVUQ Campaign. Here we call it 'coffee_pce'. ::

    my_campaign = uq.Campaign(name='coffee_pce')

Parameter space definition
--------------------------

The parameter space is defined using a dictionary. Each entry in the dictionary follows the format:

``"parameter_name": {"type" : "<value>", "min": <value>, "max": <value>, "default": <value>}``

With a defined type, minimum and maximum value and default. If the parameter is not selected to vary in the Sampler (see below) then the default value is used for every run. In this example, our full parameter space looks like the following: ::

    params = {
        "temp_init": {"type": "float", "min": 0.0, "max": 100.0, "default": 95.0},
        "kappa": {"type": "float", "min": 0.0, "max": 0.1, "default": 0.025},
        "t_env": {"type": "float", "min": 0.0, "max": 40.0, "default": 15.0},
        "out_file": {"type": "string", "default": "output.csv"}
    }

App Creation
------------
In this example the GenericEncoder and SimpleCSV, both included in the core EasyVVUQ library, were used as the encoder/decoder pair for this application. ::

    encoder = uq.encoders.GenericEncoder(
        template_fname='tutorial_files/cooling.template',
        delimiter='$',
        target_filename='cooling_in.json')

    decoder = uq.decoders.SimpleCSV(target_filename="output.csv",
                                output_columns=["te", "ti"])

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

As can be inferred from its name SimpleCSV reads CVS files produced by the cooling model code. Again many applications output results in different formats, potentially requiring bespoke Decoders. Having created an encoder, decoder and parameter space definition for our `cooling` app, we can add it to our campaign. ::

    # Add the app (automatically set as current app)
    my_campaign.add_app(name="cooling",
                        params=params,
                        encoder=encoder,
                        decoder=decoder)

The Sampler
-----------
The user specified which parameters will vary and their corresponding distributions. In this case the kappa and t\_env parameters are varied, both according to a uniform distribution: ::

    vary = {
        "kappa": cp.Uniform(0.025, 0.075),
        "t_env": cp.Uniform(15, 25)
    }

To perform a polynomial chaos expansion we will create a PCESampler, informing it which parameters to vary, and what polynomial order to use for the PCE. ::

    my_sampler = uq.sampling.PCESampler(vary=vary, polynomial_order=3)

Finally we set the campaign to use this sampler. ::

    my_campaign.set_sampler(my_sampler)

Calling the campaign's draw\_samples() method will cause the specified number of samples to be added as runs to the campaign database, awaiting encoding and execution. If no arguments are passed to draw\_samples() then all samples will be drawn, unless the sampler is not finite. In this case PCESampler is finite (produces a finite number of samples) and we elect to draw all of them at once: ::

    my_campaign.draw_samples()

Execute Runs
------------
my\_campaign.populate\_runs\_dir() will create a directory hierarchy containing the encoded input files for every run that has not yet been completed. Finally, in this example, a shell command is executed in each directory to execute the simple test code. In practice (in a real HPC workflow) this stage would be best handled using, for example, a pilot job manager. ::

    import os
    my_campaign.populate_runs_dir()
    my_campaign.apply_for_each_run_dir(uq.actions.ExecuteLocal("{} cooling_in.json".format(os.path.abspath('tutorial_files/cooling_model.py')), interpret="python3"))

Collation and analysis
----------------------
Calling my\_campaign.collate() at any stage causes the campaign to aggregate decoded simulation output for all runs which have not yet been collated. ::

    my_campaign.collate()

This collated data is stored in the campaign database. An analysis element, here PCEAnalysis, can then be applied to the campaign's collation result. ::

    my_analysis = uq.analysis.PCEAnalysis(sampler=my_sampler, qoi_cols=["te"])
    my_campaign.apply_analysis(my_analysis)

The output of this is dependent on the type of analysis element. ::

    # Get Descriptive Statistics
    results = my_campaign.get_last_analysis()
    stats = results['statistical_moments']['te']
    per = results['percentiles']['te']
    sobols = results['sobols_first']['te']

I don't want to use Polynomial Chaos
------------------------------------
If you wish to use something other than PCE, it is simply a matter of changing the sampling and analysis element used. For example, to use a Stochastic Collocation approach, replace the sampler line with: ::

    my_sampler = uq.sampling.SCSampler(vary=vary, polynomial_order=3)

And the analysis can be done with: ::

    my_analysis = uq.analysis.SCAnalysis(sampler=my_sampler, qoi_cols=["te"])
    my_campaign.apply_analysis(my_analysis)
